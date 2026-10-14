"""Exercise migrated archive reads in the built, read-only API image."""

import hashlib
import json
import subprocess
import sys

from fastapi.testclient import TestClient
from sqlalchemy import delete, inspect, select, text

from courselab.config import Settings
from courselab.course_archives import CourseContentArchiveService
from courselab.db import CourseContentArchive
from courselab.main import create_app


def main() -> None:
    app = create_app(Settings.from_environment())
    try:
        assert "course_content_archives" in inspect(app.state.engine).get_table_names()
        if app.state.engine.dialect.name == "postgresql":
            with app.state.engine.connect() as connection:
                role = connection.execute(
                    text(
                        "SELECT current_user, rolsuper, rolcreatedb, rolcreaterole, "
                        "rolreplication, rolbypassrls FROM pg_roles "
                        "WHERE rolname = current_user"
                    )
                ).one()
            assert role[0] == "courselab_app" and not any(role[1:])
        with TestClient(app, headers={"Origin": "http://localhost:8080"}) as client:
            health = client.get("/api/v1/health")
            assert health.status_code == 200, health.text

            course_id = "cell-biology"
            course = client.get(f"/api/v1/courses/{course_id}")
            assert course.status_code == 200, course.text
            version = course.json()["version"]
            lesson_id = course.json()["modules"][0]["lessons"][0]["id"]

            session = client.post("/api/v1/auth/guest", json={})
            assert session.status_code == 200, session.text
            client.headers["X-CSRF-Token"] = session.json()["csrf_token"]
            enrollment = client.post(
                "/api/v1/enrollments", json={"course_id": course_id}
            )
            assert enrollment.status_code == 201, enrollment.text

            # Simulate a pre-0011 enrollment, then exercise the operator CLI as
            # the same restricted role used by the API and deployment.
            with app.state.sessions() as db:
                db.execute(
                    delete(CourseContentArchive).where(
                        CourseContentArchive.course_id == course_id,
                        CourseContentArchive.content_version == version,
                    )
                )
                db.commit()

            dry_run = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "courselab.backfill_course_archives",
                    "--course-id",
                    course_id,
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            assert json.loads(dry_run.stdout)["counts"] == {
                "digest_approval_required": 1
            }
            with app.state.sessions() as db:
                assert (
                    db.scalar(
                        select(CourseContentArchive).where(
                            CourseContentArchive.course_id == course_id,
                            CourseContentArchive.content_version == version,
                        )
                    )
                    is None
                )

            package_bytes, _ = CourseContentArchiveService.build_archive(
                app.state.content.package_files(course_id)
            )
            package_sha256 = hashlib.sha256(package_bytes).hexdigest()
            blocked_apply = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "courselab.backfill_course_archives",
                    "--apply",
                    "--course-id",
                    course_id,
                ],
                capture_output=True,
                text=True,
            )
            assert blocked_apply.returncode == 2
            assert "independently verified package digest" in blocked_apply.stderr
            with app.state.sessions() as db:
                assert (
                    db.scalar(
                        select(CourseContentArchive).where(
                            CourseContentArchive.course_id == course_id,
                            CourseContentArchive.content_version == version,
                        )
                    )
                    is None
                )

            applied = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "courselab.backfill_course_archives",
                    "--apply",
                    "--course-id",
                    course_id,
                    "--expected-package-sha256",
                    package_sha256,
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            assert json.loads(applied.stdout)["counts"] == {"archived": 1}

            versions = client.get(f"/api/v1/courses/{course_id}/versions")
            assert versions.status_code == 200 and version in versions.json(), versions.text
            archived_course = client.get(
                f"/api/v1/courses/{course_id}/versions/{version}"
            )
            assert (
                archived_course.status_code == 200
                and archived_course.json()["version"] == version
            ), archived_course.text
            archived_lesson = client.get(
                f"/api/v1/courses/{course_id}/versions/{version}/lessons/{lesson_id}"
            )
            assert archived_lesson.status_code == 200, archived_lesson.text
            for question in archived_lesson.json()["questions"]:
                assert question.get("variant_token") is None
                assert not {"solution_spec", "feedback", "answer", "solution"}.intersection(
                    question
                )

        print(
            "Production API archive smoke passed: restricted runtime role, Alembic 0011, "
            "health, enrollment, digest-gated operator backfill, version index, archived "
            "course/lesson, and answer-free DTOs."
        )
    finally:
        app.state.engine.dispose()


if __name__ == "__main__":
    main()
