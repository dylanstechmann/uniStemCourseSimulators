"""Safely backfill public archives for enrollments on current package versions.

The default is a report-only dry run. This command cannot reconstruct an older
package that is no longer present in the public content directory.
"""

import argparse
import hashlib
import json
import re
import sys
from collections.abc import Sequence

from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import sessionmaker

from .config import Settings
from .content import ContentInvalid, ContentMissing, ContentRepository
from .course_archives import CourseContentArchiveService
from .db import CourseContentArchive, Enrollment, database


def backfill_course_archives(
    session_factory: sessionmaker,
    content: ContentRepository,
    *,
    apply: bool = False,
    course_id: str | None = None,
    expected_package_sha256: str | None = None,
) -> dict:
    """Report or archive distinct enrolled course versions when safe to do so."""
    if course_id is not None and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", course_id):
        raise ValueError("Course ID must be a lowercase slug")
    if expected_package_sha256 is not None:
        expected_package_sha256 = expected_package_sha256.lower()
        if course_id is None or not re.fullmatch(r"[0-9a-f]{64}", expected_package_sha256):
            raise ValueError("A valid package digest requires a single course ID")
    if apply and expected_package_sha256 is None:
        raise ValueError("Apply requires an independently verified package digest")

    archive_service = CourseContentArchiveService(content)
    entries: list[dict] = []
    with session_factory() as db:
        enrollment_query = (
            select(Enrollment.course_id, Enrollment.content_version, func.count(Enrollment.id))
            .group_by(Enrollment.course_id, Enrollment.content_version)
            .order_by(Enrollment.course_id, Enrollment.content_version)
        )
        if course_id is not None:
            enrollment_query = enrollment_query.where(Enrollment.course_id == course_id)
        enrollments = db.execute(enrollment_query).all()
        archived_keys = set(
            db.execute(select(CourseContentArchive.course_id, CourseContentArchive.content_version)).all()
        )

        for enrolled_course_id, pinned_version, enrollment_count in enrollments:
            entry = {
                "course_id": enrolled_course_id,
                "content_version": pinned_version,
                "enrollments": enrollment_count,
            }
            key = (enrolled_course_id, pinned_version)
            if key in archived_keys:
                entry["status"] = "already_archived"
                entries.append(entry)
                continue

            try:
                current_version = content.manifest(enrolled_course_id).get("version")
            except (ContentInvalid, ContentMissing, OSError, ValueError) as exc:
                entry["status"] = "package_unavailable"
                entry["reason"] = type(exc).__name__
                entries.append(entry)
                continue

            if not isinstance(current_version, str) or current_version != pinned_version:
                entry["status"] = "pinned_version_unavailable"
                entry["current_version"] = current_version
                entries.append(entry)
                continue

            try:
                package_files = content.package_files(enrolled_course_id)
                archive_bytes, _ = archive_service.build_archive(package_files)
                package_sha256 = hashlib.sha256(archive_bytes).hexdigest()
                entry["package_sha256"] = package_sha256
            except (ContentInvalid, ContentMissing, OSError) as exc:
                entry["status"] = "package_unavailable"
                entry["reason"] = type(exc).__name__
                entries.append(entry)
                continue

            if expected_package_sha256 is None:
                entry["status"] = "digest_approval_required"
                entries.append(entry)
                continue
            if package_sha256 != expected_package_sha256:
                entry["status"] = "package_digest_mismatch"
                entries.append(entry)
                continue

            if not apply:
                entry["status"] = "eligible_dry_run"
                entries.append(entry)
                continue

            try:
                archive_service.ensure_archive(db, enrolled_course_id, pinned_version)
                db.commit()
                archived_keys.add(key)
                entry["status"] = "archived"
            except HTTPException as exc:
                db.rollback()
                entry["status"] = "archive_failed"
                entry["reason"] = exc.detail
            except (ContentInvalid, ContentMissing, OSError) as exc:
                db.rollback()
                entry["status"] = "archive_failed"
                entry["reason"] = type(exc).__name__
            entries.append(entry)

    counts: dict[str, int] = {}
    for entry in entries:
        counts[entry["status"]] = counts.get(entry["status"], 0) + 1
    return {"mode": "apply" if apply else "dry_run", "counts": counts, "entries": entries}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="create archives for exact current-version matches (default: report only)",
    )
    parser.add_argument("--course-id", help="limit the report or backfill to one course slug")
    parser.add_argument(
        "--expected-package-sha256",
        help="independently verified package digest; required with --apply and --course-id",
    )
    arguments = parser.parse_args(argv)

    settings = Settings.from_environment()
    engine, session_factory = database(settings.database_url)
    try:
        report = backfill_course_archives(
            session_factory,
            ContentRepository(settings.content_root),
            apply=arguments.apply,
            course_id=arguments.course_id,
            expected_package_sha256=arguments.expected_package_sha256,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    finally:
        engine.dispose()

    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if report["counts"].get("archive_failed", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
