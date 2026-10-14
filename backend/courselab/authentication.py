"""Cookie-backed learner sessions and account authentication routes."""

import secrets
from datetime import timedelta

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError
from fastapi import APIRouter, HTTPException, Request, Response
from sqlalchemy import select

from .db import SessionToken, User, now
from .dependencies import (
    COOKIE,
    DB,
    can_review,
    optional_identity,
    require_csrf,
    require_identity,
    token_hash,
)
from .schemas import Credentials

PASSWORDS = PasswordHasher(time_cost=3, memory_cost=65536, parallelism=2)
router = APIRouter(prefix="/api/v1/auth")


def user_view(user: User) -> dict:
    return {"id": user.id, "email": user.email, "is_guest": user.is_guest}


def new_dummy_password_hash() -> str:
    return PASSWORDS.hash(secrets.token_urlsafe(24))


def start_session(db, user: User, response: Response, request: Request) -> dict:
    """Replace any current session and issue a new cookie and CSRF token."""
    old = optional_identity(request, db)
    if old:
        db.delete(old[1])
    raw, csrf = secrets.token_urlsafe(32), secrets.token_urlsafe(32)
    settings = request.app.state.settings
    hours = settings.guest_hours if user.is_guest else settings.session_hours
    db.add(
        SessionToken(
            token_hash=token_hash(raw),
            user_id=user.id,
            csrf_token=csrf,
            expires_at=now() + timedelta(hours=hours),
        )
    )
    db.commit()
    response.set_cookie(
        COOKIE,
        raw,
        httponly=True,
        secure=settings.cookie_secure,
        samesite="lax",
        max_age=hours * 3600,
        path="/api",
    )
    return {"user": user_view(user), "csrf_token": csrf, "can_review": can_review(user)}


@router.get("/session")
def session_info(request: Request, response: Response, db: DB):
    identity = optional_identity(request, db)
    if not identity:
        response.delete_cookie(COOKIE, path="/api")
        return {"user": None, "csrf_token": None, "can_review": False}
    user = identity[0]
    return {
        "user": user_view(user),
        "csrf_token": identity[1].csrf_token,
        "can_review": can_review(user),
    }


@router.post("/guest")
def guest(request: Request, response: Response, db: DB):
    identity = optional_identity(request, db)
    if identity:
        require_csrf(request, identity)
        user = identity[0]
        return {
            "user": user_view(user),
            "csrf_token": identity[1].csrf_token,
            "can_review": can_review(user),
        }
    user = User(is_guest=True)
    db.add(user)
    db.flush()
    return start_session(db, user, response, request)


@router.post("/register", status_code=201)
def register(body: Credentials, request: Request, response: Response, db: DB):
    if db.scalar(select(User).where(User.email == body.email)):
        raise HTTPException(409, "Account unavailable")
    identity = optional_identity(request, db)
    if identity:
        require_csrf(request, identity)
        if not identity[0].is_guest:
            raise HTTPException(409, "Sign out before registering another account")
        user = identity[0]
    else:
        user = User()
        db.add(user)
    user.email = body.email
    user.password_hash = PASSWORDS.hash(body.password)
    user.is_guest = False
    db.flush()
    return start_session(db, user, response, request)


@router.post("/login")
def login(body: Credentials, request: Request, response: Response, db: DB):
    identity = optional_identity(request, db)
    if identity:
        require_csrf(request, identity)
    user = db.scalar(select(User).where(User.email == body.email, User.is_guest.is_(False)))
    # Keep hash verification work similar for unknown accounts.
    candidate = user.password_hash if user else request.app.state.dummy_password_hash
    try:
        valid = PASSWORDS.verify(candidate, body.password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        valid = False
    if not user or not valid:
        raise HTTPException(401, "Email or password incorrect")
    return start_session(db, user, response, request)


@router.post("/logout", status_code=204)
def logout(request: Request, response: Response, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    db.delete(identity[1])
    db.commit()
    response.delete_cookie(COOKIE, path="/api")
