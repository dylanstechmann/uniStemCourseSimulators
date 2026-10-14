"""Enrollment-pinned assessment plans and immutable graded-source archives."""

import hashlib

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .assessment import (
    canonical_digest,
    effective_protection,
    utc_datetime,
    validate_assessment_configuration,
)
from .config import Settings
from .content import ContentInvalid, ContentMissing, ContentRepository
from .db import AssessmentInstance, AssessmentPlan, AssessmentSourceArchive, Enrollment


class AssessmentPlanService:
    def __init__(self, settings: Settings, content: ContentRepository):
        self.settings = settings
        self.content = content

    def policy(self, manifest: dict) -> dict:
        policy = dict(manifest.get("grading_policy") or {})
        policy.setdefault("mode", "formative-only")
        policy.setdefault("categories", [])
        policy.setdefault("category_aggregation", "points")
        policy.setdefault("late_submission_policy", "strict-deadline")
        policy.setdefault("attempt_policy", "No course grade is configured.")
        policy.setdefault("solution_release", "Not specified.")
        policy.setdefault("late_policy", "No course grade is configured.")
        policy.setdefault("appeals", "Use the supported formative attempt review workflow.")
        # Report the protection mode that is actually in force, not only the course's request.
        policy["assessment_protection"] = effective_protection(
            policy, self.settings.assessment_protection
        )
        return policy

    def archive_graded_source(
        self,
        db: Session,
        course_id: str,
        content_version: str,
        assessment_id: str,
        source_bytes: bytes,
    ) -> str:
        """Preserve exact graded bytes and reject unversioned source replacement."""
        source_sha256 = hashlib.sha256(source_bytes).hexdigest()
        prior_archives = db.scalars(
            select(AssessmentSourceArchive).where(
                AssessmentSourceArchive.course_id == course_id,
                AssessmentSourceArchive.content_version == content_version,
                AssessmentSourceArchive.assessment_id == assessment_id,
            )
        ).all()
        if any(archived.source_sha256 != source_sha256 for archived in prior_archives):
            raise HTTPException(
                409, "A graded assessment source changed without a course-version update"
            )
        archived = next(
            (item for item in prior_archives if item.source_sha256 == source_sha256), None
        )
        if archived:
            if (
                bytes(archived.source_bytes) != source_bytes
                or hashlib.sha256(archived.source_bytes).hexdigest() != source_sha256
            ):
                raise HTTPException(409, "The archived assessment source failed its integrity check")
            return source_sha256
        try:
            with db.begin_nested():
                db.add(
                    AssessmentSourceArchive(
                        course_id=course_id,
                        content_version=content_version,
                        assessment_id=assessment_id,
                        source_sha256=source_sha256,
                        source_bytes=source_bytes,
                    )
                )
                db.flush()
        except IntegrityError:
            # Another enrollment may have archived the same source concurrently.
            archived = db.scalar(
                select(AssessmentSourceArchive).where(
                    AssessmentSourceArchive.course_id == course_id,
                    AssessmentSourceArchive.content_version == content_version,
                    AssessmentSourceArchive.assessment_id == assessment_id,
                    AssessmentSourceArchive.source_sha256 == source_sha256,
                )
            )
            if archived is None or bytes(archived.source_bytes) != source_bytes:
                raise HTTPException(409, "The assessment source archive could not be verified")
        return source_sha256

    def ensure_assessment_plan(
        self, db: Session, enrollment: Enrollment, manifest: dict
    ) -> AssessmentPlan:
        existing = db.scalar(
            select(AssessmentPlan).where(
                AssessmentPlan.enrollment_id == enrollment.id,
                AssessmentPlan.content_version == enrollment.content_version,
            )
        )
        if existing:
            return existing
        if enrollment.content_version != manifest["version"]:
            raise HTTPException(
                409,
                "This historical enrollment has no assessment snapshot; review the current version first",
            )

        source_assessments = manifest.get("assessments", [])
        policy = self.policy(manifest)
        normalized_assessments = []
        for source in source_assessments:
            item = dict(source)
            item["attempt_scoring"] = item.get("attempt_scoring", "highest")
            item["attempt_limit"] = item.get("attempt_limit")
            item["release_at"] = item.get("release_at")
            item["due_at"] = item.get("due_at")
            normalized_assessments.append(item)
        try:
            validate_assessment_configuration(
                normalized_assessments, policy, self.settings.assessment_protection
            )
        except (AttributeError, KeyError, TypeError, ValueError) as exc:
            raise HTTPException(409, "The course assessment configuration is invalid") from exc

        for item in normalized_assessments:
            try:
                source_file = self.content.assessment_source_file(
                    enrollment.course_id, item["path"]
                )
                source_bytes = source_file.read_bytes()
                item["_source_sha256"] = (
                    self.archive_graded_source(
                        db,
                        enrollment.course_id,
                        enrollment.content_version,
                        item["id"],
                        source_bytes,
                    )
                    if item["mode"] == "graded"
                    else hashlib.sha256(source_bytes).hexdigest()
                )
            except (ContentInvalid, ContentMissing, KeyError, OSError) as exc:
                raise HTTPException(409, "An assessment source is missing or invalid") from exc

        snapshot = {
            "course_id": enrollment.course_id,
            "content_version": enrollment.content_version,
            "grading_policy": policy,
            "assessments": normalized_assessments,
        }
        plan = AssessmentPlan(
            enrollment_id=enrollment.id,
            content_version=enrollment.content_version,
            grading_mode=policy["mode"],
            policy_json=policy,
            snapshot_sha256=canonical_digest(snapshot),
        )
        db.add(plan)
        db.flush()
        for item in normalized_assessments:
            db.add(
                AssessmentInstance(
                    plan_id=plan.id,
                    assessment_id=item["id"],
                    assessment_type=item["type"],
                    mode=item["mode"],
                    title=item.get("title"),
                    category_id=item.get("category_id"),
                    week=item.get("week"),
                    points=float(item["points"]),
                    source_path=item["path"],
                    source_sha256=item["_source_sha256"],
                    objective_ids=item.get("objective_ids", []),
                    question_ids=item.get("question_ids", []),
                    release_at=utc_datetime(item.get("release_at")),
                    due_at=utc_datetime(item.get("due_at")),
                    attempt_limit=item.get("attempt_limit"),
                    attempt_scoring=item["attempt_scoring"],
                )
            )
        db.flush()
        return plan
