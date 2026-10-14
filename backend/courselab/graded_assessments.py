"""Protected graded assessment loading and persisted authored-form assignments."""

import hashlib
import json
import math
import secrets

from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .assessment import canonical_digest, effective_protection
from .assessment_plans import AssessmentPlanService
from .config import Settings
from .content import ContentInvalid, ContentMissing, ContentRepository
from .db import (
    AssessmentInstance,
    AssessmentPlan,
    Enrollment,
    GradedAssessmentAssignment,
    GradedSubmission,
)
from .grading import question_spec_digest
from .variants import (
    VariantTokenError,
    assignment_form_ids,
    resolve_variant,
    variant_ids,
)


class GradedAssessmentService:
    def __init__(
        self,
        settings: Settings,
        content: ContentRepository,
        plans: AssessmentPlanService,
    ):
        self.settings = settings
        self.content = content
        self.plans = plans

    def load(
        self, db: Session, enrollment: Enrollment, manifest: dict, assessment_id: str
    ) -> tuple[AssessmentPlan, AssessmentInstance, list[dict], int, str]:
        """Load only an enrollment-pinned graded activity with verified source bytes."""
        plan = self.plans.ensure_assessment_plan(db, enrollment, manifest)
        if plan.grading_mode != "graded-course":
            raise HTTPException(404, "No graded assessments are configured for this course")
        instance = db.scalar(
            select(AssessmentInstance).where(
                AssessmentInstance.plan_id == plan.id,
                AssessmentInstance.assessment_id == assessment_id,
            )
        )
        if not instance or instance.mode != "graded":
            raise HTTPException(404, "Graded assessment not found")
        try:
            protection = effective_protection(
                dict(plan.policy_json or {}), self.settings.assessment_protection
            )
        except ValueError as exc:
            raise HTTPException(409, "The assessment protection setting is invalid") from exc
        if protection == "protected" and not str(instance.source_path).startswith("private://"):
            raise HTTPException(
                409, "Assessment protection is on and this assessment is not in the private store"
            )
        try:
            source_path = self.content.assessment_source_file(
                enrollment.course_id, instance.source_path
            )
            source_bytes = source_path.read_bytes()
        except (ContentInvalid, ContentMissing, OSError) as exc:
            raise HTTPException(409, "The pinned assessment source is unavailable") from exc
        source_sha256 = hashlib.sha256(source_bytes).hexdigest()
        if not secrets.compare_digest(source_sha256, instance.source_sha256):
            raise HTTPException(
                409, "Assessment content changed after this enrollment version was pinned"
            )
        self.plans.archive_graded_source(
            db,
            enrollment.course_id,
            enrollment.content_version,
            instance.assessment_id,
            source_bytes,
        )
        try:
            package = json.loads(source_bytes.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise HTTPException(409, "The pinned assessment source is invalid") from exc
        if (
            not isinstance(package, dict)
            or package.get("course_id") != enrollment.course_id
            or not isinstance(package.get("questions"), list)
        ):
            raise HTTPException(409, "The pinned assessment source has an invalid course mapping")
        questions_by_id = {}
        for question in package["questions"]:
            question_id = question.get("id") if isinstance(question, dict) else None
            if not isinstance(question_id, str) or question_id in questions_by_id:
                raise HTTPException(409, "The pinned assessment has invalid question identifiers")
            questions_by_id[question_id] = question
        question_ids = instance.question_ids
        if (
            not isinstance(question_ids, list)
            or not question_ids
            or any(not isinstance(question_id, str) for question_id in question_ids)
            or len(question_ids) != len(set(question_ids))
            or any(question_id not in questions_by_id for question_id in question_ids)
        ):
            raise HTTPException(409, "The pinned assessment question mapping is invalid")
        questions = [questions_by_id[question_id] for question_id in question_ids]
        try:
            assignment_form_ids(questions)
        except VariantTokenError as exc:
            raise HTTPException(
                409, "The pinned assessment authored-form configuration is invalid"
            ) from exc
        try:
            question_points = sum(float(question["points"]) for question in questions)
        except (KeyError, TypeError, ValueError) as exc:
            raise HTTPException(409, "The pinned assessment point mapping is invalid") from exc
        if not math.isclose(question_points, float(instance.points), rel_tol=0, abs_tol=1e-8):
            raise HTTPException(409, "Question points do not match the pinned assessment total")
        attempts_used = (
            db.scalar(
                select(func.count())
                .select_from(GradedSubmission)
                .where(
                    GradedSubmission.enrollment_id == enrollment.id,
                    GradedSubmission.assessment_instance_id == instance.id,
                )
            )
            or 0
        )
        try:
            spec_digest = canonical_digest(
                {
                    "grader": [question_spec_digest(question) for question in questions],
                    "source_sha256": instance.source_sha256,
                }
            )
        except (TypeError, ValueError) as exc:
            raise HTTPException(
                409, "The pinned assessment grading specification is invalid"
            ) from exc
        return plan, instance, questions, int(attempts_used), spec_digest

    def assignment_form(
        self,
        db: Session,
        enrollment: Enrollment,
        instance: AssessmentInstance,
        questions: list[dict],
        attempts_used: int,
        schedule_status: str,
    ) -> tuple[list[dict], str | None]:
        """Load or persist the exact authored form for this learner's next attempt."""
        try:
            forms = assignment_form_ids(questions)
        except VariantTokenError as exc:
            raise HTTPException(
                409, "The pinned assessment authored-form configuration is invalid"
            ) from exc
        if not forms:
            return questions, None

        has_attempt_slot = instance.attempt_limit is None or attempts_used < instance.attempt_limit
        if schedule_status == "open" and has_attempt_slot:
            attempt_number = attempts_used + 1
        elif attempts_used:
            attempt_number = attempts_used
        else:
            # A closed, not-yet-started assessment need not create a usable attempt assignment.
            return [
                resolve_variant(question, "base" if variant_ids(question) else None)
                for question in questions
            ], None

        assignment = db.scalar(
            select(GradedAssessmentAssignment).where(
                GradedAssessmentAssignment.enrollment_id == enrollment.id,
                GradedAssessmentAssignment.assessment_instance_id == instance.id,
                GradedAssessmentAssignment.attempt_number == attempt_number,
            )
        )
        if assignment is None:
            if schedule_status != "open" or not has_attempt_slot:
                raise HTTPException(409, "The saved authored-form assignment is unavailable")
            cycle_start = ((attempt_number - 1) // len(forms)) * len(forms) + 1
            prior = list(
                db.scalars(
                    select(GradedAssessmentAssignment).where(
                        GradedAssessmentAssignment.enrollment_id == enrollment.id,
                        GradedAssessmentAssignment.assessment_instance_id == instance.id,
                        GradedAssessmentAssignment.attempt_number >= cycle_start,
                        GradedAssessmentAssignment.attempt_number < attempt_number,
                    )
                )
            )
            used_forms = {
                variant_id
                for item in prior
                for variant_id in (item.variant_ids_json or {}).values()
                if variant_id is not None
            }
            available = [variant_id for variant_id in forms if variant_id not in used_forms]
            selected = secrets.choice(available or forms)
            variant_map = {
                question["id"]: selected if variant_ids(question) else None
                for question in questions
            }
            resolved = [
                resolve_variant(question, variant_map[question["id"]]) for question in questions
            ]
            try:
                digest = canonical_digest(
                    {
                        "grader": [
                            question_spec_digest(question, variant_map[question["id"]])
                            for question in resolved
                        ],
                        "source_sha256": instance.source_sha256,
                    }
                )
            except (TypeError, ValueError) as exc:
                raise HTTPException(
                    409, "The pinned assessment grading specification is invalid"
                ) from exc
            assignment = GradedAssessmentAssignment(
                id=secrets.token_urlsafe(32),
                enrollment_id=enrollment.id,
                assessment_instance_id=instance.id,
                attempt_number=attempt_number,
                content_version=enrollment.content_version,
                source_sha256=instance.source_sha256,
                variant_ids_json=variant_map,
                question_spec_sha256=digest,
            )
            db.add(assignment)
            try:
                db.commit()
            except IntegrityError:
                db.rollback()
                assignment = db.scalar(
                    select(GradedAssessmentAssignment).where(
                        GradedAssessmentAssignment.enrollment_id == enrollment.id,
                        GradedAssessmentAssignment.assessment_instance_id == instance.id,
                        GradedAssessmentAssignment.attempt_number == attempt_number,
                    )
                )
                if assignment is None:
                    raise HTTPException(
                        409, "A concurrent request could not persist this attempt assignment"
                    )

        if (
            assignment.enrollment_id != enrollment.id
            or assignment.assessment_instance_id != instance.id
            or assignment.attempt_number != attempt_number
            or assignment.content_version != enrollment.content_version
            or assignment.source_sha256 != instance.source_sha256
            or not isinstance(assignment.variant_ids_json, dict)
            or set(assignment.variant_ids_json) != {question["id"] for question in questions}
        ):
            raise HTTPException(409, "The saved authored-form assignment does not match this assessment")
        try:
            resolved = [
                resolve_variant(question, assignment.variant_ids_json[question["id"]])
                for question in questions
            ]
            digest = canonical_digest(
                {
                    "grader": [
                        question_spec_digest(question, assignment.variant_ids_json[question["id"]])
                        for question in resolved
                    ],
                    "source_sha256": instance.source_sha256,
                }
            )
        except (VariantTokenError, TypeError, ValueError) as exc:
            raise HTTPException(409, "The saved authored-form assignment is invalid") from exc
        if not secrets.compare_digest(digest, assignment.question_spec_sha256):
            raise HTTPException(409, "The saved authored-form assignment failed verification")
        return resolved, assignment.id
