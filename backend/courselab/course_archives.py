"""Versioned, digest-verified snapshots of public course packages."""

import hashlib
import io
import json
import re
import stat
import zipfile
from contextlib import contextmanager
from typing import Iterator

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .content import ContentInvalid, ContentMissing, ContentRepository
from .db import CourseContentArchive

MAX_ARCHIVE_BYTES = 64 * 1024 * 1024


class CourseContentArchiveService:
    def __init__(self, content: ContentRepository):
        self.content = content

    @staticmethod
    def build_archive(files: dict[str, bytes]) -> tuple[bytes, dict[str, str]]:
        if not files or "course.json" not in files:
            raise ContentInvalid("Course package is missing its manifest")
        if len(files) > 10_000 or sum(map(len, files.values())) > MAX_ARCHIVE_BYTES:
            raise ContentInvalid("Course package exceeds the archive limit")
        file_hashes = {
            name: hashlib.sha256(payload).hexdigest()
            for name, payload in sorted(files.items())
        }
        output = io.BytesIO()
        with zipfile.ZipFile(output, mode="w", compression=zipfile.ZIP_STORED) as archive:
            for name, payload in sorted(files.items()):
                CourseContentArchiveService._validate_name(name)
                info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_STORED
                info.create_system = 3
                info.external_attr = (stat.S_IFREG | 0o644) << 16
                info.flag_bits = 0
                archive.writestr(info, payload)
        archive_bytes = output.getvalue()
        if len(archive_bytes) > MAX_ARCHIVE_BYTES:
            raise ContentInvalid("Course package exceeds the archive limit")
        return archive_bytes, file_hashes

    @staticmethod
    def _validate_name(name: str) -> None:
        parts = name.split("/")
        if (
            not name
            or name.startswith("/")
            or "\\" in name
            or ":" in name
            or any(part in {"", ".", ".."} for part in parts)
        ):
            raise ContentInvalid("Unsafe path in course content archive")

    @classmethod
    def verify_archive(
        cls,
        course_id: str,
        archive_bytes: bytes,
        expected_archive_sha256: str,
        expected_file_hashes: dict,
    ) -> dict[str, bytes]:
        if hashlib.sha256(archive_bytes).hexdigest() != expected_archive_sha256:
            raise ContentInvalid("Course content archive digest mismatch")
        if not isinstance(expected_file_hashes, dict):
            raise ContentInvalid("Course content archive manifest is invalid")
        try:
            with zipfile.ZipFile(io.BytesIO(archive_bytes), mode="r") as archive:
                infos = archive.infolist()
                names = [info.filename for info in infos]
                if len(names) != len(set(names)) or len(names) != len(expected_file_hashes):
                    raise ContentInvalid("Course content archive file list mismatch")
                files = {}
                total_bytes = 0
                for info in infos:
                    cls._validate_name(info.filename)
                    mode = (info.external_attr >> 16) & 0xFFFF
                    if (
                        info.is_dir()
                        or stat.S_ISLNK(mode)
                        or stat.S_IFMT(mode) not in {0, stat.S_IFREG}
                        or info.compress_type != zipfile.ZIP_STORED
                        or info.file_size > MAX_ARCHIVE_BYTES
                    ):
                        raise ContentInvalid("Unsupported entry in course content archive")
                    payload = archive.read(info)
                    total_bytes += len(payload)
                    if total_bytes > MAX_ARCHIVE_BYTES:
                        raise ContentInvalid("Course content archive exceeds the size limit")
                    files[info.filename] = payload
        except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
            raise ContentInvalid("Course content archive is unreadable") from exc
        actual_hashes = {
            name: hashlib.sha256(payload).hexdigest()
            for name, payload in sorted(files.items())
        }
        if actual_hashes != expected_file_hashes:
            raise ContentInvalid("Course content file digest mismatch")
        try:
            manifest = json.loads(files["course.json"].decode("utf-8"))
        except (KeyError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ContentInvalid("Archived course manifest is invalid") from exc
        if manifest.get("id") != course_id:
            raise ContentInvalid("Archived course manifest ID mismatch")
        return files

    def read_archived_course(
        self, db: Session, course_id: str, content_version: str
    ) -> dict[str, bytes]:
        archived = db.scalar(
            select(CourseContentArchive).where(
                CourseContentArchive.course_id == course_id,
                CourseContentArchive.content_version == content_version,
            )
        )
        if archived is None:
            raise HTTPException(404, "Course content archive not found")
        try:
            return self.verify_archive(
                course_id,
                bytes(archived.archive_bytes),
                archived.archive_sha256,
                archived.files_sha256_json,
            )
        except ContentInvalid as exc:
            raise HTTPException(409, "The archived course content failed its integrity check") from exc

    @staticmethod
    def list_versions(db: Session, course_id: str) -> list[str]:
        """List snapshot versions without returning archive bytes or file metadata."""
        return list(
            db.scalars(
                select(CourseContentArchive.content_version)
                .where(CourseContentArchive.course_id == course_id)
                .order_by(
                    CourseContentArchive.created_at.desc(),
                    CourseContentArchive.content_version.desc(),
                )
            ).all()
        )

    @contextmanager
    def archived_repository(
        self, db: Session, course_id: str, content_version: str
    ) -> Iterator[ContentRepository]:
        """Materialize one verified public snapshot for existing DTO readers."""
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", course_id):
            raise HTTPException(404, "Course content archive not found")
        files = self.read_archived_course(db, course_id, content_version)
        # Rendering consumes only a verified in-memory public package snapshot;
        # private answer-source configuration is intentionally not provided.
        yield ContentRepository(
            self.content.root,
            package_snapshot=(course_id, files),
            archived_version=content_version,
        )

    def ensure_archive(
        self, db: Session, course_id: str, content_version: str
    ) -> str:
        try:
            files = self.content.package_files(course_id)
            archive_bytes, file_hashes = self.build_archive(files)
        except (ContentInvalid, ContentMissing, OSError) as exc:
            raise HTTPException(409, "The course package cannot be archived") from exc
        archive_sha256 = hashlib.sha256(archive_bytes).hexdigest()
        existing = db.scalar(
            select(CourseContentArchive).where(
                CourseContentArchive.course_id == course_id,
                CourseContentArchive.content_version == content_version,
            )
        )
        if existing is not None:
            try:
                archived_files = self.verify_archive(
                    course_id,
                    bytes(existing.archive_bytes),
                    existing.archive_sha256,
                    existing.files_sha256_json,
                )
            except ContentInvalid as exc:
                raise HTTPException(
                    409, "The archived course content failed its integrity check"
                ) from exc
            if (
                existing.archive_sha256 != archive_sha256
                or bytes(existing.archive_bytes) != archive_bytes
                or existing.files_sha256_json != file_hashes
                or archived_files != files
            ):
                raise HTTPException(
                    409, "Course content changed without a course-version update"
                )
            return archive_sha256
        try:
            with db.begin_nested():
                db.add(
                    CourseContentArchive(
                        course_id=course_id,
                        content_version=content_version,
                        archive_sha256=archive_sha256,
                        archive_bytes=archive_bytes,
                        files_sha256_json=file_hashes,
                    )
                )
                db.flush()
        except IntegrityError:
            archived = db.scalar(
                select(CourseContentArchive).where(
                    CourseContentArchive.course_id == course_id,
                    CourseContentArchive.content_version == content_version,
                )
            )
            if archived is None:
                raise HTTPException(409, "The course content archive could not be verified")
            try:
                archived_files = self.verify_archive(
                    course_id,
                    bytes(archived.archive_bytes),
                    archived.archive_sha256,
                    archived.files_sha256_json,
                )
            except ContentInvalid as exc:
                raise HTTPException(
                    409, "The archived course content failed its integrity check"
                ) from exc
            if (
                archived.archive_sha256 != archive_sha256
                or bytes(archived.archive_bytes) != archive_bytes
                or archived.files_sha256_json != file_hashes
                or archived_files != files
            ):
                raise HTTPException(
                    409, "Course content changed without a course-version update"
                )
        return archive_sha256
