import hashlib
import io
import json
import zipfile

import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import select

from courselab.backfill_course_archives import backfill_course_archives, main
from courselab.content import ContentInvalid, ContentRepository
from courselab.course_archives import CourseContentArchiveService
from courselab.db import Base, CourseContentArchive, Enrollment, User, database


def test_course_package_archive_is_deterministic_and_round_trips(content_root):
    content = ContentRepository(content_root)
    service = CourseContentArchiveService(content)
    files = content.package_files("test-course")

    archive_bytes, file_hashes = service.build_archive(files)
    repeated_bytes, repeated_hashes = service.build_archive(files)

    assert archive_bytes == repeated_bytes
    assert file_hashes == repeated_hashes
    assert hashlib.sha256(archive_bytes).hexdigest()
    assert service.verify_archive(
        "test-course",
        archive_bytes,
        hashlib.sha256(archive_bytes).hexdigest(),
        file_hashes,
    ) == files
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        assert archive.namelist() == sorted(files)


def test_course_archive_rejects_unsafe_member_names():
    with pytest.raises(ContentInvalid, match="Unsafe path"):
        CourseContentArchiveService.build_archive(
            {"course.json": b'{"id":"test-course"}', "../outside.txt": b"bad"}
        )


def test_enrollment_pins_complete_public_course_archive(guest, app, content_root):
    response = guest.post("/api/v1/enrollments", json={"course_id": "test-course"})
    assert response.status_code == 201

    with app.state.sessions() as db:
        archive = db.scalar(
            select(CourseContentArchive).where(
                CourseContentArchive.course_id == "test-course",
                CourseContentArchive.content_version == "0.1.0",
            )
        )
        assert archive is not None
        assert archive.archive_sha256 == hashlib.sha256(archive.archive_bytes).hexdigest()
        files = app.state.course_archives.read_archived_course(db, "test-course", "0.1.0")
    assert files["modules/one.md"].decode("utf-8").startswith("# Experiment")
    assert json.loads(files["course.json"])["version"] == "0.1.0"


def test_same_version_content_change_fails_closed(guest, app, content_root):
    first = guest.post("/api/v1/enrollments", json={"course_id": "test-course"})
    assert first.status_code == 201
    module = content_root / "courses" / "test-course" / "modules" / "one.md"
    module.write_text("# Changed without a version increment")

    changed = guest.post("/api/v1/enrollments", json={"course_id": "test-course"})

    assert changed.status_code == 409
    assert "without a course-version update" in changed.json()["detail"]
    with app.state.sessions() as db:
        archives = db.scalars(select(CourseContentArchive)).all()
        assert len(archives) == 1


def test_course_upgrade_retains_each_pinned_package_version(guest, app, content_root):
    enrolled = guest.post("/api/v1/enrollments", json={"course_id": "test-course"})
    assert enrolled.status_code == 201
    manifest_path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["version"] = "0.2.0"
    manifest_path.write_text(json.dumps(manifest))
    module = content_root / "courses" / "test-course" / "modules" / "one.md"
    module.write_text("# Version two reading")

    upgraded = guest.put("/api/v1/enrollments/test-course/version", json={})
    assert upgraded.status_code == 200
    assert upgraded.json()["content_version"] == "0.2.0"

    with app.state.sessions() as db:
        old = app.state.course_archives.read_archived_course(db, "test-course", "0.1.0")
        new = app.state.course_archives.read_archived_course(db, "test-course", "0.2.0")
        rows = db.scalars(
            select(CourseContentArchive).order_by(CourseContentArchive.content_version)
        ).all()
        assert [row.content_version for row in rows] == ["0.1.0", "0.2.0"]
    assert old["modules/one.md"].decode("utf-8").startswith("# Experiment")
    assert new["modules/one.md"] == b"# Version two reading"
    listed_versions = guest.get("/api/v1/courses/test-course/versions")
    assert listed_versions.status_code == 200
    assert set(listed_versions.json()) == {"0.1.0", "0.2.0"}


def test_enrolled_learner_can_read_old_version_through_safe_archived_dtos(
    guest, app, content_root
):
    enrolled = guest.post("/api/v1/enrollments", json={"course_id": "test-course"})
    assert enrolled.status_code == 201
    manifest_path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["version"] = "0.2.0"
    manifest_path.write_text(json.dumps(manifest))
    reading_path = content_root / "courses" / "test-course" / "modules" / "one.md"
    reading_path.write_text("# Version two reading")
    assert guest.put("/api/v1/enrollments/test-course/version", json={}).status_code == 200

    archived_course = guest.get("/api/v1/courses/test-course/versions/0.1.0")
    archived_lesson = guest.get(
        "/api/v1/courses/test-course/versions/0.1.0/lessons/lesson-one"
    )

    assert archived_course.status_code == 200
    assert archived_course.json()["version"] == "0.1.0"
    assert archived_course.json()["syllabus_markdown"].startswith("# Partial test package")
    assert archived_lesson.status_code == 200
    lesson = archived_lesson.json()
    assert lesson["markdown"].startswith("# Experiment")
    assert lesson["questions"]
    assert all(question["variant_token"] is None for question in lesson["questions"])
    assert all(
        not {"solution_spec", "feedback", "answer", "solution"}.intersection(question)
        for question in lesson["questions"]
    )
    assert "PRIVATE_TEST_SENTINEL" not in archived_lesson.text


def test_archived_course_view_requires_enrollment(app, guest):
    with TestClient(app) as anonymous:
        assert anonymous.get("/api/v1/courses/test-course/versions/0.1.0").status_code == 401
        assert anonymous.get("/api/v1/courses/test-course/versions").status_code == 401
    response = guest.get("/api/v1/courses/test-course/versions/0.1.0")
    assert response.status_code == 403
    assert guest.get("/api/v1/courses/test-course/versions").status_code == 403


def test_corrupt_course_package_archive_is_not_returned(guest, app):
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    with app.state.sessions() as db:
        archived = db.scalar(select(CourseContentArchive))
        archived.archive_bytes += b"tampered"
        db.commit()
        with pytest.raises(HTTPException) as error:
            app.state.course_archives.read_archived_course(db, "test-course", "0.1.0")
    assert error.value.status_code == 409


def test_legacy_archive_backfill_is_dry_run_first_and_skips_stale_versions(app, content_root):
    with app.state.sessions() as db:
        current_user = User(is_guest=True)
        stale_user = User(is_guest=True)
        db.add_all([current_user, stale_user])
        db.flush()
        db.add_all(
            [
                Enrollment(
                    user_id=current_user.id,
                    course_id="test-course",
                    content_version="0.1.0",
                ),
                Enrollment(
                    user_id=stale_user.id,
                    course_id="test-course",
                    content_version="0.0.9",
                ),
            ]
        )
        db.commit()

    dry_run = backfill_course_archives(
        app.state.sessions, ContentRepository(content_root)
    )

    assert dry_run["mode"] == "dry_run"
    assert dry_run["counts"] == {
        "digest_approval_required": 1,
        "pinned_version_unavailable": 1,
    }
    with app.state.sessions() as db:
        assert db.scalars(select(CourseContentArchive)).all() == []

    package_bytes, _ = CourseContentArchiveService.build_archive(
        ContentRepository(content_root).package_files("test-course")
    )
    package_sha256 = hashlib.sha256(package_bytes).hexdigest()
    approved_dry_run = backfill_course_archives(
        app.state.sessions,
        ContentRepository(content_root),
        course_id="test-course",
        expected_package_sha256=package_sha256,
    )
    assert approved_dry_run["counts"] == {
        "eligible_dry_run": 1,
        "pinned_version_unavailable": 1,
    }

    with pytest.raises(ValueError, match="independently verified package digest"):
        backfill_course_archives(
            app.state.sessions,
            ContentRepository(content_root),
            apply=True,
            course_id="test-course",
        )

    applied = backfill_course_archives(
        app.state.sessions,
        ContentRepository(content_root),
        apply=True,
        course_id="test-course",
        expected_package_sha256=package_sha256,
    )

    assert applied["mode"] == "apply"
    assert applied["counts"] == {"archived": 1, "pinned_version_unavailable": 1}
    repeated = backfill_course_archives(
        app.state.sessions,
        ContentRepository(content_root),
        apply=True,
        course_id="test-course",
        expected_package_sha256=package_sha256,
    )
    assert repeated["counts"] == {
        "already_archived": 1,
        "pinned_version_unavailable": 1,
    }
    with app.state.sessions() as db:
        archive = db.scalar(select(CourseContentArchive))
        assert archive is not None
        assert (archive.course_id, archive.content_version) == ("test-course", "0.1.0")


def test_legacy_archive_backfill_validates_course_filter(app, content_root):
    with pytest.raises(ValueError, match="lowercase slug"):
        backfill_course_archives(
            app.state.sessions,
            ContentRepository(content_root),
            course_id="../test-course",
        )


def test_legacy_archive_backfill_rejects_unverified_digest(app, content_root):
    with app.state.sessions() as db:
        user = User(is_guest=True)
        db.add(user)
        db.flush()
        db.add(Enrollment(user_id=user.id, course_id="test-course", content_version="0.1.0"))
        db.commit()

    report = backfill_course_archives(
        app.state.sessions,
        ContentRepository(content_root),
        apply=True,
        course_id="test-course",
        expected_package_sha256="0" * 64,
    )

    assert report["counts"] == {"package_digest_mismatch": 1}
    with app.state.sessions() as db:
        assert db.scalars(select(CourseContentArchive)).all() == []


def test_archive_backfill_cli_is_dry_run_first_and_requires_verified_digest(
    tmp_path, content_root, monkeypatch, capsys
):
    database_url = f"sqlite:///{(tmp_path / 'archive-cli.db').as_posix()}"
    engine, session_factory = database(database_url)
    Base.metadata.create_all(engine)
    with session_factory() as db:
        user = User(is_guest=True)
        db.add(user)
        db.flush()
        db.add(Enrollment(user_id=user.id, course_id="test-course", content_version="0.1.0"))
        db.commit()
    engine.dispose()
    monkeypatch.setenv("DATABASE_URL", database_url)
    monkeypatch.setenv("CONTENT_ROOT", str(content_root))
    monkeypatch.delenv("PRIVATE_ASSESSMENTS_ROOT", raising=False)

    assert main(["--course-id", "test-course"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["counts"] == {"digest_approval_required": 1}

    assert main(["--apply", "--course-id", "test-course"]) == 2
    capsys.readouterr()
    assert main(
        [
            "--apply",
            "--course-id",
            "test-course",
            "--expected-package-sha256",
            "0" * 64,
        ]
    ) == 0
    mismatch = json.loads(capsys.readouterr().out)
    assert mismatch["counts"] == {"package_digest_mismatch": 1}

    package_bytes, _ = CourseContentArchiveService.build_archive(
        ContentRepository(content_root).package_files("test-course")
    )
    expected_digest = hashlib.sha256(package_bytes).hexdigest()
    assert main(
        [
            "--apply",
            "--course-id",
            "test-course",
            "--expected-package-sha256",
            expected_digest,
        ]
    ) == 0
    applied = json.loads(capsys.readouterr().out)
    assert applied["counts"] == {"archived": 1}

    verify_engine, verify_factory = database(database_url)
    try:
        with verify_factory() as db:
            archive = db.scalar(select(CourseContentArchive))
            assert archive is not None
            assert archive.archive_sha256 == expected_digest
    finally:
        verify_engine.dispose()
