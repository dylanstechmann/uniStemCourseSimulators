"""Learner history and human review routes for graded submissions."""

from fastapi import APIRouter, HTTPException, Query, Request
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .db import (
    AssessmentInstance,
    AssessmentPlan,
    Enrollment,
    GradedSubmission,
    GradedSubmissionAppeal,
    GradedSubmissionAppealReview,
)
from .dependencies import DB, require_csrf, require_enrollment, require_identity, require_reviewer
from .schemas import (
    AppealRequest,
    AppealReviewRequest,
    AssessmentSubmissionResponse,
    GradedSubmissionAppealResponse,
    InstructorGradedSubmissionAppealResponse,
)

router = APIRouter()


@router.get(
    "/api/v1/assessments/{course_id}/submissions",
    response_model=list[AssessmentSubmissionResponse],
)
def graded_submission_history(course_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    enrollment = require_enrollment(db, user, course_id, request.app.state.content)
    plan = db.scalar(
        select(AssessmentPlan).where(
            AssessmentPlan.enrollment_id == enrollment.id,
            AssessmentPlan.content_version == enrollment.content_version,
        )
    )
    if not plan:
        return []
    rows = list(
        db.scalars(
            select(GradedSubmission)
            .where(
                GradedSubmission.enrollment_id == enrollment.id,
                GradedSubmission.plan_id == plan.id,
            )
            .order_by(GradedSubmission.submitted_at, GradedSubmission.id)
        )
    )
    by_instance = {
        item.id: item
        for item in db.scalars(
            select(AssessmentInstance).where(AssessmentInstance.plan_id == plan.id)
        )
    }
    views = request.app.state.graded_views
    return [
        views.submission_view(row, by_instance[row.assessment_instance_id], course_id, db)
        for row in rows
        if row.assessment_instance_id in by_instance
    ]


@router.post("/api/v1/graded-submissions/{submission_id}/appeals", status_code=201)
def create_graded_submission_appeal(
    submission_id: str, body: AppealRequest, request: Request, db: DB
):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    user = identity[0]
    submission = db.scalar(
        select(GradedSubmission)
        .join(Enrollment, Enrollment.id == GradedSubmission.enrollment_id)
        .where(GradedSubmission.id == submission_id, Enrollment.user_id == user.id)
    )
    if not submission:
        raise HTTPException(404, "Graded submission not found")
    if db.scalar(
        select(GradedSubmissionAppeal).where(
            GradedSubmissionAppeal.submission_id == submission.id
        )
    ):
        raise HTTPException(409, "This submission already has a human-review request")
    appeal = GradedSubmissionAppeal(
        submission_id=submission.id,
        user_id=user.id,
        reason=body.reason,
    )
    db.add(appeal)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(409, "This submission already has a human-review request") from exc
    instance = db.get(AssessmentInstance, submission.assessment_instance_id)
    if not instance:
        raise HTTPException(409, "The assessment snapshot for this submission is unavailable")
    db.refresh(appeal)
    enrollment = db.get(Enrollment, submission.enrollment_id)
    return request.app.state.graded_views.appeal_view(
        appeal, submission, instance, enrollment.course_id
    )


@router.get("/api/v1/graded-appeals", response_model=list[GradedSubmissionAppealResponse])
def learner_graded_submission_appeals(request: Request, db: DB):
    user, _ = require_identity(request, db)
    appeals = db.scalars(
        select(GradedSubmissionAppeal)
        .where(GradedSubmissionAppeal.user_id == user.id)
        .order_by(GradedSubmissionAppeal.created_at, GradedSubmissionAppeal.id)
    )
    records = []
    for appeal in appeals:
        submission = db.get(GradedSubmission, appeal.submission_id)
        instance = db.get(AssessmentInstance, submission.assessment_instance_id) if submission else None
        enrollment = db.get(Enrollment, submission.enrollment_id) if submission else None
        review = db.scalar(
            select(GradedSubmissionAppealReview).where(
                GradedSubmissionAppealReview.appeal_id == appeal.id
            )
        )
        if submission and instance and enrollment:
            records.append(
                request.app.state.graded_views.appeal_view(
                    appeal, submission, instance, enrollment.course_id, review
                )
            )
    return records


@router.get(
    "/api/v1/instructor/graded-appeals",
    response_model=list[InstructorGradedSubmissionAppealResponse],
)
def instructor_graded_submission_appeals(
    request: Request,
    db: DB,
    status: str = "open",
    limit: int = Query(default=50, ge=1, le=100),
):
    reviewer = require_reviewer(request, db)
    if status not in {"open", "reviewed", "all"}:
        raise HTTPException(422, "Status must be open, reviewed, or all")
    review_exists = select(GradedSubmissionAppealReview.id).where(
        GradedSubmissionAppealReview.appeal_id == GradedSubmissionAppeal.id
    ).exists()
    statement = (
        select(GradedSubmissionAppeal)
        .where(GradedSubmissionAppeal.user_id != reviewer.id)
        .order_by(GradedSubmissionAppeal.created_at, GradedSubmissionAppeal.id)
    )
    if status == "open":
        statement = statement.where(~review_exists)
    elif status == "reviewed":
        statement = statement.where(review_exists)
    appeals = db.scalars(statement.limit(limit))
    records = []
    for appeal in appeals:
        submission = db.get(GradedSubmission, appeal.submission_id)
        if submission:
            records.append(
                request.app.state.graded_views.instructor_appeal_record(appeal, submission, db)
            )
    return records


@router.post("/api/v1/instructor/graded-appeals/{appeal_id}/review")
def review_graded_submission_appeal(
    appeal_id: str, body: AppealReviewRequest, request: Request, db: DB
):
    reviewer = require_reviewer(request, db, mutation=True)
    appeal = db.get(GradedSubmissionAppeal, appeal_id)
    if not appeal:
        raise HTTPException(404, "Graded submission appeal not found")
    if appeal.user_id == reviewer.id:
        raise HTTPException(403, "An instructor cannot review their own submission")
    if db.scalar(
        select(GradedSubmissionAppealReview).where(
            GradedSubmissionAppealReview.appeal_id == appeal.id
        )
    ):
        raise HTTPException(409, "This appeal already has a recorded review")
    submission = db.get(GradedSubmission, appeal.submission_id)
    if not submission:
        raise HTTPException(404, "Graded submission not found")
    instance = db.get(AssessmentInstance, submission.assessment_instance_id)
    enrollment = db.get(Enrollment, submission.enrollment_id)
    plan = db.get(AssessmentPlan, submission.plan_id)
    if not instance or not enrollment or not plan:
        raise HTTPException(409, "The original assessment snapshot is unavailable")
    if body.decision == "adjusted":
        if body.override_score is None or body.override_score > submission.max_score:
            raise HTTPException(
                422,
                "An adjusted decision needs a score from zero through the submission maximum",
            )
    elif body.override_score is not None:
        raise HTTPException(422, "Only an adjusted decision can change the score")
    if body.decision != "declined" and request.app.state.graded_views.verified_review_questions(
        db, submission, enrollment, plan, instance
    ) is None:
        raise HTTPException(
            409,
            "The original assignment specification cannot be verified; only a decline explaining this limitation can be recorded",
        )
    review = GradedSubmissionAppealReview(
        appeal_id=appeal.id,
        reviewer_user_id=reviewer.id,
        reviewer_email=reviewer.email,
        decision=body.decision,
        review_note=body.review_note,
        override_score=body.override_score,
    )
    db.add(review)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(409, "This appeal already has a recorded review") from exc
    db.refresh(review)
    return request.app.state.graded_views.instructor_appeal_record(appeal, submission, db)
