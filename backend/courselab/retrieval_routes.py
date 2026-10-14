"""Self-assessed retrieval-card queue and review endpoints."""

from collections import defaultdict

from fastapi import APIRouter, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from .content import ContentMissing
from .db import CardReview, User, now
from .dependencies import DB, require_csrf, require_enrollment, require_identity
from .retrieval import (
    POLICY_SUMMARY,
    POLICY_VERSION,
    ScheduleState,
    card_digest,
    next_state,
)
from .schemas import CardReviewRequest, CardReviewResponse, ReviewQueueResponse
from .serialization import timestamp

router = APIRouter(prefix="/api/v1")


def card_review_history(
    db: Session, user: User, course_id: str
) -> dict[str, list[CardReview]]:
    history: dict[str, list[CardReview]] = defaultdict(list)
    for item in db.scalars(
        select(CardReview)
        .where(CardReview.user_id == user.id, CardReview.course_id == course_id)
        .order_by(CardReview.reviewed_at, CardReview.id)
    ):
        history[item.card_id].append(item)
    return history


def current_card_reviews(reviews: list[CardReview], digest: str) -> list[CardReview]:
    """Only reviews of the exact card text carry a schedule forward."""
    return [item for item in reviews if item.card_sha256 == digest]


def card_schedule_view(reviews: list[CardReview], reference_time) -> dict:
    latest = reviews[-1]
    return {
        "policy_version": latest.policy_version,
        "last_rating": latest.rating,
        "review_count": len(reviews),
        "repetitions": latest.repetitions,
        "ease": float(latest.ease),
        "interval_days": float(latest.interval_days),
        "due_at": timestamp(latest.due_at),
        "reviewed_at": timestamp(latest.reviewed_at),
        "due": latest.due_at <= reference_time,
    }


def published_card(content, course_id: str, card_id: str) -> dict:
    for card in content.course_retrieval_cards(course_id):
        if card["id"] == card_id:
            return card
    raise ContentMissing("Retrieval card not found")


@router.get("/reviews/{course_id}", response_model=ReviewQueueResponse)
def review_queue(course_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    content = request.app.state.content
    enrollment = require_enrollment(db, user, course_id, content)
    reference_time = now()
    history = card_review_history(db, user, course_id)
    due, new, upcoming = [], [], []
    for card in content.course_retrieval_cards(course_id):
        reviews = history.get(card["id"], [])
        current = current_card_reviews(reviews, card_digest(course_id, card))
        item = {
            "card_id": card["id"],
            "lesson_id": card["lesson_id"],
            "lesson_title": card["lesson_title"],
            "front": card["front"],
            "back": card["back"],
            "learning_objective_ids": card["learning_objective_ids"],
            "schedule": card_schedule_view(current, reference_time) if current else None,
            "content_changed_since_last_review": bool(reviews) and not current,
        }
        if not current:
            new.append(item)
        elif current[-1].due_at <= reference_time:
            due.append(item)
        else:
            upcoming.append(item)
    due.sort(key=lambda item: item["schedule"]["due_at"])
    upcoming.sort(key=lambda item: item["schedule"]["due_at"])
    return {
        "course_id": course_id,
        "content_version": enrollment.content_version,
        "policy_version": POLICY_VERSION,
        "policy": POLICY_SUMMARY,
        "generated_at": timestamp(reference_time),
        "counts": {"due": len(due), "new": len(new), "upcoming": len(upcoming)},
        "due": due,
        "new": new,
        "upcoming": upcoming,
        "limitations": (
            "Ratings are your own self-assessment after revealing an answer. The schedule only decides "
            "when to show a card again; it is not a practice score, objective evidence, or mastery."
        ),
    }


@router.post(
    "/courses/{course_id}/cards/{card_id}/reviews",
    status_code=201,
    response_model=CardReviewResponse,
)
def review_card(course_id: str, card_id: str, body: CardReviewRequest, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    enrollment = require_enrollment(db, identity[0], course_id, content)
    card = published_card(content, course_id, card_id)
    digest = card_digest(course_id, card)
    reviewed_at = now()
    current = current_card_reviews(
        card_review_history(db, identity[0], course_id).get(card_id, []), digest
    )
    previous = (
        ScheduleState(
            current[-1].repetitions,
            float(current[-1].ease),
            float(current[-1].interval_days),
            current[-1].due_at,
        )
        if current
        else None
    )
    state = next_state(previous, body.rating, reviewed_at)
    item = CardReview(
        user_id=identity[0].id,
        course_id=course_id,
        lesson_id=card["lesson_id"],
        card_id=card_id,
        content_version=enrollment.content_version,
        card_sha256=digest,
        policy_version=POLICY_VERSION,
        rating=body.rating,
        repetitions=state.repetitions,
        ease=state.ease,
        interval_days=state.interval_days,
        due_at=state.due_at,
        reviewed_at=reviewed_at,
    )
    db.add(item)
    db.commit()
    return {
        "card_id": card_id,
        "lesson_id": card["lesson_id"],
        "rating": body.rating,
        "schedule": card_schedule_view([*current, item], reviewed_at),
    }
