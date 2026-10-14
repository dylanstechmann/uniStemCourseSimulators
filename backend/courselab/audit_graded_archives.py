"""Report whether saved graded submissions still have verifiable source archives.

This command is strictly read-only. It reports aggregate counts and never attempts
to recreate historical assessment content from the current content directory.
"""

import argparse
import hashlib
import json
from collections import Counter
from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from .config import Settings
from .db import (
    AssessmentInstance,
    AssessmentPlan,
    AssessmentSourceArchive,
    Enrollment,
    GradedSubmission,
    database,
)


def audit_graded_archives(session_factory: sessionmaker) -> dict:
    """Return a privacy-preserving aggregate report without changing database state."""
    with session_factory() as db:
        submissions = db.scalars(
            select(GradedSubmission).order_by(
                GradedSubmission.content_version,
                GradedSubmission.assessment_instance_id,
            ).execution_options(yield_per=500)
        )
        enrollments = {item.id: item for item in db.scalars(select(Enrollment)).all()}
        plans = {item.id: item for item in db.scalars(select(AssessmentPlan)).all()}
        instances = {item.id: item for item in db.scalars(select(AssessmentInstance)).all()}

        grouped: Counter[tuple[str, str, str, str]] = Counter()
        archive_status_cache: dict[tuple[str, str, str, str], str] = {}
        for submission in submissions:
            enrollment = enrollments.get(submission.enrollment_id)
            plan = plans.get(submission.plan_id)
            instance = instances.get(submission.assessment_instance_id)
            course_id = enrollment.course_id if enrollment else "unknown"
            version = submission.content_version or "unknown"
            assessment_id = instance.assessment_id if instance else "unknown"

            if enrollment is None:
                status = "enrollment_missing"
            elif plan is None:
                status = "plan_missing"
            elif instance is None:
                status = "assessment_instance_missing"
            elif (
                plan.enrollment_id != enrollment.id
                or plan.content_version != submission.content_version
                or enrollment.content_version != submission.content_version
                or instance.plan_id != plan.id
                or plan.grading_mode != "graded-course"
                or instance.mode != "graded"
            ):
                status = "snapshot_link_mismatch"
            elif instance.source_sha256 != submission.source_sha256:
                status = "snapshot_source_digest_mismatch"
            else:
                scope = (course_id, version, assessment_id)
                archive_key = (*scope, submission.source_sha256)
                status = archive_status_cache.get(archive_key, "")
                if not status:
                    matching = db.scalars(
                        select(AssessmentSourceArchive).where(
                            AssessmentSourceArchive.course_id == course_id,
                            AssessmentSourceArchive.content_version == version,
                            AssessmentSourceArchive.assessment_id == assessment_id,
                            AssessmentSourceArchive.source_sha256 == submission.source_sha256,
                        ).limit(2)
                    ).all()
                    if not matching:
                        any_archive = db.scalar(
                            select(AssessmentSourceArchive.id).where(
                                AssessmentSourceArchive.course_id == course_id,
                                AssessmentSourceArchive.content_version == version,
                                AssessmentSourceArchive.assessment_id == assessment_id,
                            ).limit(1)
                        )
                        status = "archive_missing" if any_archive is None else "archive_digest_mismatch"
                    elif len(matching) > 1:
                        status = "archive_ambiguous"
                    else:
                        try:
                            archived_bytes = bytes(matching[0].source_bytes)
                            intact = hashlib.sha256(archived_bytes).hexdigest() == matching[0].source_sha256
                        except (TypeError, ValueError):
                            intact = False
                        status = "source_archive_verified" if intact else "archive_bytes_corrupt"
                    archive_status_cache[archive_key] = status

            grouped[(course_id, version, assessment_id, status)] += 1

    entries = [
        {
            "course_id": course_id,
            "content_version": version,
            "assessment_id": assessment_id,
            "status": status,
            "submission_count": count,
        }
        for (course_id, version, assessment_id, status), count in sorted(grouped.items())
    ]
    counts: dict[str, int] = {}
    for entry in entries:
        counts[entry["status"]] = counts.get(entry["status"], 0) + entry["submission_count"]
    return {
        "mode": "report_only",
        "database_modified": False,
        "submission_count": sum(grouped.values()),
        "counts": counts,
        "groups": entries,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)

    settings = Settings.from_environment()
    engine, session_factory = database(settings.database_url)
    try:
        report = audit_graded_archives(session_factory)
    finally:
        engine.dispose()

    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
