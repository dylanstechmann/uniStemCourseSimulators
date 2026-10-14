"""Learner gradebook routes and their provisional evidence summary."""

from collections import defaultdict

from fastapi import APIRouter, HTTPException, Request
from sqlalchemy import select

from .assessment import calculate_weighted_grade
from .db import (
    Appeal,
    AppealReview,
    AssessmentInstance,
    AssessmentPlan,
    Attempt,
    GradedSubmission,
    GradedSubmissionAppeal,
    GradedSubmissionAppealReview,
    now,
)
from .dependencies import DB, require_enrollment, require_identity
from .evidence import (
    MIN_DISTINCT_ITEMS,
    MIN_ITEM_COVERAGE,
    MIN_PERFORMANCE,
    POLICY_VERSION,
    objective_evidence,
)
from .schemas import GradebookResponse
from .serialization import timestamp

router = APIRouter()


@router.get("/api/v1/gradebook/{course_id}", response_model=GradebookResponse)
def gradebook(course_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    content = request.app.state.content
    enrollment = require_enrollment(db, user, course_id, content)
    questions = content.questions(course_id)
    rows = list(
        db.scalars(
            select(Attempt)
            .where(
                Attempt.user_id == user.id,
                Attempt.course_id == course_id,
                Attempt.content_version == enrollment.content_version,
            )
            .order_by(Attempt.created_at, Attempt.id)
        )
    )
    reviewed = db.execute(
        select(Appeal.attempt_id, AppealReview.override_score)
        .join(AppealReview, AppealReview.appeal_id == Appeal.id)
        .join(Attempt, Attempt.id == Appeal.attempt_id)
        .where(
            Attempt.user_id == user.id,
            Attempt.course_id == course_id,
            Attempt.content_version == enrollment.content_version,
            AppealReview.decision == "adjusted",
        )
    )
    score_overrides = {attempt_id: float(score) for attempt_id, score in reviewed}
    best = {}
    for item in rows:
        effective_score = score_overrides.get(item.id, float(item.score))
        best[item.question_id] = max(best.get(item.question_id, 0), effective_score)

    course_grade = None
    plan = db.scalar(
        select(AssessmentPlan).where(
            AssessmentPlan.enrollment_id == enrollment.id,
            AssessmentPlan.content_version == enrollment.content_version,
        )
    )
    if plan and plan.grading_mode == "graded-course":
        instances = list(
            db.scalars(select(AssessmentInstance).where(AssessmentInstance.plan_id == plan.id))
        )
        submissions = list(
            db.scalars(
                select(GradedSubmission).where(
                    GradedSubmission.enrollment_id == enrollment.id,
                    GradedSubmission.plan_id == plan.id,
                )
            )
        )
        graded_submission_ids = [item.id for item in submissions]
        graded_score_overrides = {}
        if graded_submission_ids:
            override_rows = db.execute(
                select(GradedSubmissionAppeal.submission_id, GradedSubmissionAppealReview.override_score)
                .join(
                    GradedSubmissionAppealReview,
                    GradedSubmissionAppealReview.appeal_id == GradedSubmissionAppeal.id,
                )
                .where(
                    GradedSubmissionAppeal.submission_id.in_(graded_submission_ids),
                    GradedSubmissionAppealReview.decision == "adjusted",
                )
            )
            graded_score_overrides = {
                submission_id: float(score) for submission_id, score in override_rows
            }
        attempts_by_assessment = defaultdict(list)
        instances_by_id = {item.id: item for item in instances}
        for submission in submissions:
            instance = instances_by_id.get(submission.assessment_instance_id)
            if instance:
                attempts_by_assessment[instance.assessment_id].append(
                    {
                        "id": submission.id,
                        "score": graded_score_overrides.get(submission.id, submission.score),
                        "max_score": submission.max_score,
                        "submitted_at": timestamp(submission.submitted_at),
                    }
                )
        try:
            calculated = calculate_weighted_grade(
                [
                    {
                        "id": item.assessment_id,
                        "mode": item.mode,
                        # The pinned source lets the protection check see private:// paths.
                        "path": item.source_path,
                        "category_id": item.category_id,
                        "points": item.points,
                        "release_at": timestamp(item.release_at) if item.release_at else None,
                        "due_at": timestamp(item.due_at) if item.due_at else None,
                        "attempt_limit": item.attempt_limit,
                        "attempt_scoring": item.attempt_scoring,
                    }
                    for item in instances
                ],
                plan.policy_json,
                dict(attempts_by_assessment),
                now(),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise HTTPException(
                409, "Saved assessment results do not match the pinned grade policy"
            ) from exc
        course_grade = {
            **calculated,
            "manual_override_count": len(graded_score_overrides),
            "status": "in_progress" if submissions else "configured_no_submissions",
            "explanation": (
                "This percentage follows the saved assessment weights, deterministic attempt rules, and any "
                "recorded instructor adjustments. The original automatic score for every submission remains saved. "
                "Only released work enters the current calculation; the active category weight shows "
                "how much of the configured grade currently has evidence. It does not establish credit, "
                "course equivalency, or completion."
            ),
        }

    return {
        "course_id": course_id,
        "assessment_role": "formative",
        "aggregation": "best reviewed practice result per question",
        "score": sum(best.values()),
        "max_score": sum(float(item.get("points", 1)) for item in questions),
        "attempt_count": len(rows),
        "manual_override_count": len(score_overrides),
        "course_grade": course_grade,
        "objective_evidence_policy": {
            "version": POLICY_VERSION,
            "minimum_distinct_items": MIN_DISTINCT_ITEMS,
            "minimum_item_coverage": MIN_ITEM_COVERAGE,
            "minimum_performance": MIN_PERFORMANCE,
        },
        "objective_evidence": objective_evidence(
            questions,
            rows,
            score_overrides,
            [item["id"] for item in content.manifest(course_id).get("lesson_objectives", [])],
        ),
        "limitations": (
            "The provisional practice indicator requires at least 3 distinct tagged items, 80% of available "
            "tagged-item coverage, and 80% best points on attempted items. Instructor adjustments are audited "
            "separately from automatic scores. This remains a study signal from short formative checks; it does "
            "not establish reasoning, transfer, course mastery, credit, or course completion."
        ),
    }
