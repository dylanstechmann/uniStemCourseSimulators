"""Instructor queue and audited decisions for formative learner appeals."""

from fastapi import APIRouter, HTTPException, Query, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from .content import ContentInvalid, ContentMissing
from .db import Appeal, AppealReview, Attempt, User
from .dependencies import DB, require_reviewer
from .grading import question_spec_digest
from .practice_attempts import appeal_view
from .schemas import AppealReviewRequest
from .variants import VariantTokenError, resolve_variant

router = APIRouter(prefix="/api/v1")


def verified_review_question(content, attempt: Attempt) -> dict | None:
    """Resolve the submitted variant and require its saved spec digest to match."""
    if not attempt.question_spec_sha256 or not isinstance(attempt.response, dict):
        return None
    try:
        manifest = content.manifest(attempt.course_id)
        if manifest["version"] != attempt.content_version:
            return None
        question = content.question(attempt.course_id, attempt.question_id)
        variant_id = attempt.response.get("variant_id")
        resolved = resolve_variant(question, variant_id)
        digest = question_spec_digest(resolved, variant_id)
        return resolved if digest == attempt.question_spec_sha256 else None
    except (ContentMissing, ContentInvalid, VariantTokenError, KeyError, TypeError, ValueError):
        return None


def instructor_appeal_record(content, appeal: Appeal, attempt: Attempt, db: Session) -> dict:
    learner = db.get(User, appeal.user_id)
    review = db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id))
    question = verified_review_question(content, attempt)
    content_is_current = question is not None
    review_question = (
        content.public_question(
            question,
            variant_id=attempt.response.get("variant_id"),
        ).model_dump()
        if question is not None
        else None
    )
    return {
        **appeal_view(appeal, attempt, review),
        "learner": learner.email if learner and learner.email else "Guest account",
        "content_is_current": content_is_current,
        "review_question": review_question,
        "question_prompt": question.get("prompt") if question else None,
        "question_options": question.get("options") if question else None,
        "response": attempt.response,
        "automatic_feedback": attempt.result,
        "specification_pinned": bool(attempt.question_spec_sha256),
    }


@router.get("/instructor/appeals")
def instructor_appeals(
    request: Request,
    db: DB,
    status: str = "open",
    limit: int = Query(default=50, ge=1, le=100),
):
    reviewer = require_reviewer(request, db)
    if status not in {"open", "reviewed", "all"}:
        raise HTTPException(422, "Status must be open, reviewed, or all")
    statement = (
        select(Appeal)
        .where(Appeal.user_id != reviewer.id)
        .order_by(Appeal.created_at, Appeal.id)
    )
    if status == "open":
        statement = statement.where(
            ~select(AppealReview.id)
            .where(AppealReview.appeal_id == Appeal.id)
            .exists()
        )
    elif status == "reviewed":
        statement = statement.where(
            select(AppealReview.id)
            .where(AppealReview.appeal_id == Appeal.id)
            .exists()
        )
    appeals = db.scalars(statement.limit(limit))
    result = []
    for appeal in appeals:
        attempt = db.get(Attempt, appeal.attempt_id)
        if attempt:
            result.append(instructor_appeal_record(request.app.state.content, appeal, attempt, db))
    return result


@router.post("/instructor/appeals/{appeal_id}/review")
def review_appeal(
    appeal_id: str, body: AppealReviewRequest, request: Request, db: DB
):
    reviewer = require_reviewer(request, db, mutation=True)
    appeal = db.get(Appeal, appeal_id)
    if not appeal:
        raise HTTPException(404, "Appeal not found")
    if appeal.user_id == reviewer.id:
        raise HTTPException(403, "An instructor cannot review their own attempt")
    if db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id)):
        raise HTTPException(409, "This appeal already has a recorded review")
    attempt = db.get(Attempt, appeal.attempt_id)
    if not attempt:
        raise HTTPException(404, "Attempt not found")
    if body.decision == "adjusted":
        if body.override_score is None or body.override_score > attempt.max_score:
            raise HTTPException(422, "An adjusted decision needs a score from zero through the attempt maximum")
    elif body.override_score is not None:
        raise HTTPException(422, "Only an adjusted decision can change the score")
    if body.decision != "declined" and verified_review_question(
        request.app.state.content, attempt
    ) is None:
        raise HTTPException(
            409,
            "The original question specification cannot be verified; only a decline explaining this limitation can be recorded",
        )
    review = AppealReview(
        appeal_id=appeal.id,
        reviewer_user_id=reviewer.id,
        reviewer_email=reviewer.email,
        decision=body.decision,
        review_note=body.review_note,
        override_score=body.override_score,
    )
    db.add(review)
    db.commit()
    return instructor_appeal_record(request.app.state.content, appeal, attempt, db)
