"""Learner data export and account deletion routes."""

from fastapi import APIRouter, Request, Response
from sqlalchemy import delete, select, update

from .authentication import user_view
from .case_studio import draft_view
from .db import (
    Appeal,
    AppealReview,
    AssessmentInstance,
    Attempt,
    Bookmark,
    CardReview,
    CaseDraft,
    Enrollment,
    GradedSubmission,
    GradedSubmissionAppeal,
    GradedSubmissionAppealReview,
    Note,
    Progress,
    SessionToken,
    now,
)
from .dependencies import COOKIE, DB, require_csrf, require_identity
from .practice_attempts import appeal_view, attempt_view
from .serialization import timestamp

router = APIRouter()


@router.get("/api/v1/learner/export")
def export(request: Request, db: DB):
    user, _ = require_identity(request, db)
    user_enrollments = list(db.scalars(select(Enrollment).where(Enrollment.user_id == user.id)))
    enrollment_by_id = {item.id: item for item in user_enrollments}
    graded_rows = list(
        db.scalars(
            select(GradedSubmission).where(
                GradedSubmission.enrollment_id.in_(list(enrollment_by_id))
                if enrollment_by_id
                else False
            )
        )
    )
    views = request.app.state.graded_views
    return {
        "schema_version": "1.0",
        "exported_at": timestamp(now()),
        "user": user_view(user),
        "enrollments": [
            {"course_id": item.course_id, "content_version": item.content_version}
            for item in user_enrollments
        ],
        "attempts": [
            attempt_view(item, db)
            for item in db.scalars(select(Attempt).where(Attempt.user_id == user.id))
        ],
        "graded_submissions": [
            views.submission_view(
                item,
                db.get(AssessmentInstance, item.assessment_instance_id),
                enrollment_by_id[item.enrollment_id].course_id,
                db,
            )
            for item in graded_rows
            if item.assessment_instance_id and item.enrollment_id in enrollment_by_id
        ],
        "appeals": [
            appeal_view(
                appeal,
                db.get(Attempt, appeal.attempt_id),
                db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id)),
            )
            for appeal in db.scalars(select(Appeal).where(Appeal.user_id == user.id))
            if db.get(Attempt, appeal.attempt_id)
        ],
        "graded_submission_appeals": [
            views.appeal_view(
                appeal,
                submission,
                instance,
                enrollment_by_id[submission.enrollment_id].course_id,
                db.scalar(
                    select(GradedSubmissionAppealReview).where(
                        GradedSubmissionAppealReview.appeal_id == appeal.id
                    )
                ),
            )
            for appeal in db.scalars(
                select(GradedSubmissionAppeal).where(
                    GradedSubmissionAppeal.user_id == user.id
                )
            )
            if (submission := db.get(GradedSubmission, appeal.submission_id))
            and (instance := db.get(AssessmentInstance, submission.assessment_instance_id))
            and submission.enrollment_id in enrollment_by_id
        ],
        "progress": [
            {"course_id": item.course_id, "lesson_id": item.lesson_id, "completed": item.completed}
            for item in db.scalars(select(Progress).where(Progress.user_id == user.id))
        ],
        "notes": [
            {"course_id": item.course_id, "lesson_id": item.lesson_id, "body": item.body}
            for item in db.scalars(select(Note).where(Note.user_id == user.id))
        ],
        "case_drafts": [draft_view(draft) for draft in db.scalars(
            select(CaseDraft).where(CaseDraft.user_id == user.id)
            .order_by(CaseDraft.updated_at, CaseDraft.id)
        )],
        "card_reviews": [
            {
                "course_id": item.course_id,
                "lesson_id": item.lesson_id,
                "card_id": item.card_id,
                "content_version": item.content_version,
                "card_sha256": item.card_sha256,
                "policy_version": item.policy_version,
                "rating": item.rating,
                "repetitions": item.repetitions,
                "ease": float(item.ease),
                "interval_days": float(item.interval_days),
                "due_at": timestamp(item.due_at),
                "reviewed_at": timestamp(item.reviewed_at),
            }
            for item in db.scalars(
                select(CardReview)
                .where(CardReview.user_id == user.id)
                .order_by(CardReview.reviewed_at, CardReview.id)
            )
        ],
        "bookmarks": [
            item.course_id
            for item in db.scalars(select(Bookmark).where(Bookmark.user_id == user.id))
        ],
    }


@router.delete("/api/v1/learner", status_code=204)
def delete_learner(request: Request, response: Response, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    # Explicit child deletion also protects SQLite test deployments.
    appeal_ids = select(Appeal.id).where(Appeal.user_id == identity[0].id)
    db.execute(delete(AppealReview).where(AppealReview.appeal_id.in_(appeal_ids)))
    db.execute(delete(Appeal).where(Appeal.user_id == identity[0].id))
    graded_appeal_ids = select(GradedSubmissionAppeal.id).where(
        GradedSubmissionAppeal.user_id == identity[0].id
    )
    db.execute(
        delete(GradedSubmissionAppealReview).where(
            GradedSubmissionAppealReview.appeal_id.in_(graded_appeal_ids)
        )
    )
    db.execute(
        delete(GradedSubmissionAppeal).where(
            GradedSubmissionAppeal.user_id == identity[0].id
        )
    )
    enrollment_ids = select(Enrollment.id).where(Enrollment.user_id == identity[0].id)
    db.execute(delete(GradedSubmission).where(GradedSubmission.enrollment_id.in_(enrollment_ids)))
    db.execute(
        update(AppealReview)
        .where(AppealReview.reviewer_user_id == identity[0].id)
        .values(reviewer_user_id=None, reviewer_email="deleted instructor account")
    )
    db.execute(
        update(GradedSubmissionAppealReview)
        .where(GradedSubmissionAppealReview.reviewer_user_id == identity[0].id)
        .values(reviewer_user_id=None, reviewer_email="deleted instructor account")
    )
    for model in (SessionToken, Attempt, CardReview, CaseDraft, Bookmark, Note, Progress, Enrollment):
        db.execute(delete(model).where(model.user_id == identity[0].id))
    db.delete(identity[0])
    db.commit()
    response.delete_cookie(COOKIE, path="/api")
