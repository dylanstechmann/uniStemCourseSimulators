"""Formative attempt submission and learner-facing attempt views."""

from fastapi import APIRouter, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from .db import Appeal, AppealReview, Attempt
from .dependencies import DB, require_csrf, require_enrollment, require_identity
from .grading import grade, question_spec_digest
from .schemas import AppealRequest, AttemptRequest
from .serialization import timestamp
from .variants import VariantTokenError, verify_variant_token

router = APIRouter(prefix="/api/v1")


def appeal_view(appeal: Appeal, attempt: Attempt, review: AppealReview | None = None) -> dict:
    status = review.decision if review else "open"
    effective_score = (
        float(review.override_score)
        if review and review.decision == "adjusted"
        else float(attempt.score)
    )
    return {
        "id": appeal.id,
        "attempt_id": attempt.id,
        "course_id": attempt.course_id,
        "question_id": attempt.question_id,
        "reason": appeal.reason,
        "status": status,
        "decision": review.decision if review else None,
        "review_note": review.review_note if review else None,
        "original_score": float(attempt.score),
        "effective_score": effective_score,
        "max_score": float(attempt.max_score),
        "created_at": timestamp(appeal.created_at),
        "reviewed_at": timestamp(review.created_at) if review else None,
    }


def attempt_view(item: Attempt, db: Session) -> dict:
    appeal = db.scalar(select(Appeal).where(Appeal.attempt_id == item.id))
    review = (
        db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id))
        if appeal
        else None
    )
    effective_score = (
        float(review.override_score)
        if review and review.decision == "adjusted"
        else float(item.score)
    )
    return {
        "id": item.id,
        "course_id": item.course_id,
        "question_id": item.question_id,
        "content_version": item.content_version,
        "response": item.response,
        "score": float(item.score),
        "effective_score": effective_score,
        "max_score": float(item.max_score),
        "result": item.result,
        "objective_ids": item.objective_ids,
        "created_at": timestamp(item.created_at),
        "appeal": appeal_view(appeal, item, review) if appeal else None,
    }


@router.post("/courses/{course_id}/questions/{question_id}/attempts", status_code=201)
def submit(course_id: str, question_id: str, body: AttemptRequest, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    enrollment = require_enrollment(db, identity[0], course_id, content)
    question = content.question(course_id, question_id)
    try:
        resolved_question, variant_id = verify_variant_token(
            question,
            course_id,
            enrollment.content_version,
            body.variant_token,
            request.app.state.settings.variant_token_secret,
        )
    except VariantTokenError as exc:
        raise HTTPException(422, "Question variant token is invalid or expired") from exc
    result = grade(resolved_question, body)
    stored_response = {"response": body.response}
    if body.unit is not None:
        stored_response["unit"] = body.unit
    if variant_id is not None:
        stored_response["variant_id"] = variant_id
    item = Attempt(
        user_id=identity[0].id,
        course_id=course_id,
        question_id=question_id,
        content_version=enrollment.content_version,
        response=stored_response,
        grading_policy_version=result.grading_policy_version,
        question_spec_sha256=question_spec_digest(resolved_question, variant_id),
        score=result.score,
        max_score=result.max_score,
        result=result.model_dump(),
        objective_ids=resolved_question.get("objective_ids", []),
    )
    db.add(item)
    db.commit()
    return attempt_view(item, db)


@router.post("/attempts/{attempt_id}/appeals", status_code=201)
def create_appeal(attempt_id: str, body: AppealRequest, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    attempt = db.scalar(
        select(Attempt).where(
            Attempt.id == attempt_id, Attempt.user_id == identity[0].id
        )
    )
    if not attempt:
        raise HTTPException(404, "Attempt not found")
    if db.scalar(select(Appeal).where(Appeal.attempt_id == attempt.id)):
        raise HTTPException(409, "This attempt already has a human-review request")
    appeal = Appeal(attempt_id=attempt.id, user_id=identity[0].id, reason=body.reason)
    db.add(appeal)
    db.commit()
    return appeal_view(appeal, attempt)


@router.get("/appeals")
def learner_appeals(request: Request, db: DB):
    user, _ = require_identity(request, db)
    appeals = db.scalars(
        select(Appeal)
        .where(Appeal.user_id == user.id)
        .order_by(Appeal.created_at, Appeal.id)
    )
    result = []
    for appeal in appeals:
        attempt = db.get(Attempt, appeal.attempt_id)
        review = db.scalar(select(AppealReview).where(AppealReview.appeal_id == appeal.id))
        if attempt:
            result.append(appeal_view(appeal, attempt, review))
    return result


@router.get("/attempts")
def attempts(request: Request, db: DB, course_id: str | None = None):
    user, _ = require_identity(request, db)
    query = select(Attempt).where(Attempt.user_id == user.id).order_by(Attempt.created_at, Attempt.id)
    if course_id:
        query = query.where(Attempt.course_id == course_id)
    return [attempt_view(item, db) for item in db.scalars(query)]
