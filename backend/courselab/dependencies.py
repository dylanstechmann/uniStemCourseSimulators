"""Shared request dependencies for database and learner identity."""

import hashlib
import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from .content import ContentRepository
from .db import Enrollment, SessionToken, User, now

COOKIE = "courselab_session"


def token_hash(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def db_session(request: Request):
    with request.app.state.sessions() as session:
        yield session


DB = Annotated[Session, Depends(db_session)]


def optional_identity(request: Request, db: Session) -> tuple[User, SessionToken] | None:
    raw = request.cookies.get(COOKIE)
    if not raw or len(raw) > 128:
        return None
    stored = db.get(SessionToken, token_hash(raw))
    if not stored or stored.expires_at <= now():
        return None
    user = db.get(User, stored.user_id)
    return (user, stored) if user else None


def require_identity(request: Request, db: Session) -> tuple[User, SessionToken]:
    identity = optional_identity(request, db)
    if not identity:
        raise HTTPException(401, "Start a guest session or sign in")
    return identity


def require_csrf(request: Request, identity: tuple[User, SessionToken]) -> None:
    supplied = request.headers.get("x-csrf-token", "")
    if not supplied or not secrets.compare_digest(supplied, identity[1].csrf_token):
        raise HTTPException(403, "CSRF token missing or invalid")


def require_enrollment(
    db: Session, user: User, course_id: str, content: ContentRepository
) -> Enrollment:
    enrollment = db.scalar(
        select(Enrollment).where(
            Enrollment.user_id == user.id, Enrollment.course_id == course_id
        )
    )
    if not enrollment:
        raise HTTPException(403, "Enroll in this course first")
    current_version = content.manifest(course_id)["version"]
    if enrollment.content_version != current_version:
        raise HTTPException(409, "The course version changed; a reviewed enrollment migration is required")
    return enrollment


def require_course_enrollment(db: Session, user: User, course_id: str) -> Enrollment:
    """Require enrollment while allowing read-only access to an older archived version."""
    enrollment = db.scalar(
        select(Enrollment).where(
            Enrollment.user_id == user.id,
            Enrollment.course_id == course_id,
        )
    )
    if not enrollment:
        raise HTTPException(403, "Enroll in this course first")
    return enrollment


def can_review(user: User) -> bool:
    """Only an operator-provisioned, registered account may adjudicate appeals."""
    return not user.is_guest and bool(user.email) and user.is_instructor


def require_reviewer(request: Request, db: Session, mutation: bool = False) -> User:
    identity = require_identity(request, db)
    user = identity[0]
    if not can_review(user):
        raise HTTPException(403, "Instructor review access is not enabled for this account")
    if mutation:
        require_csrf(request, identity)
    return user
