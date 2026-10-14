"""Learner lesson delivery endpoints."""

from fastapi import APIRouter, Request, Response
from sqlalchemy import select

from .db import Attempt
from .dependencies import DB, optional_identity, require_course_enrollment, require_identity
from .schemas import PublicLesson
from .variants import issue_variant_token

router = APIRouter(prefix="/api/v1")


@router.get("/courses/{course_id}/lessons/{lesson_id}", response_model=PublicLesson)
def lesson(course_id: str, lesson_id: str, request: Request, db: DB):
    content = request.app.state.content
    settings = request.app.state.settings
    version = content.manifest(course_id)["version"]
    identity = optional_identity(request, db)

    def public_question(question: dict):
        preferred_variant_id = None
        if identity:
            previous = db.scalar(
                select(Attempt)
                .where(
                    Attempt.user_id == identity[0].id,
                    Attempt.course_id == course_id,
                    Attempt.content_version == version,
                    Attempt.question_id == question["id"],
                )
                .order_by(Attempt.created_at.desc(), Attempt.id.desc())
                .limit(1)
            )
            if previous and isinstance(previous.response, dict):
                saved_variant_id = previous.response.get("variant_id")
                if isinstance(saved_variant_id, str):
                    preferred_variant_id = saved_variant_id
        token, variant_id, resolved = issue_variant_token(
            question,
            course_id,
            version,
            settings.variant_token_secret,
            preferred_variant_id=preferred_variant_id,
        )
        return content.public_question(resolved, variant_id, token)

    return content.lesson(course_id, lesson_id, public_question)


@router.get(
    "/courses/{course_id}/versions/{content_version}/lessons/{lesson_id}",
    response_model=PublicLesson,
)
def archived_lesson(
    course_id: str, content_version: str, lesson_id: str, request: Request, db: DB
):
    user, _ = require_identity(request, db)
    require_course_enrollment(db, user, course_id)
    with request.app.state.course_archives.archived_repository(
        db, course_id, content_version
    ) as content:
        return content.lesson(
            course_id,
            lesson_id,
            public_question_factory=lambda question: content.public_question(question),
        )


@router.get("/courses/{course_id}/resources/{resource_path:path}")
def learner_resource(course_id: str, resource_path: str, request: Request):
    content = request.app.state.content
    return Response(
        content=content.learner_resource(course_id, resource_path),
        media_type="text/csv",
    )


@router.get(
    "/courses/{course_id}/versions/{content_version}/resources/{resource_path:path}"
)
def archived_learner_resource(
    course_id: str,
    content_version: str,
    resource_path: str,
    request: Request,
    db: DB,
):
    user, _ = require_identity(request, db)
    require_course_enrollment(db, user, course_id)
    with request.app.state.course_archives.archived_repository(
        db, course_id, content_version
    ) as content:
        payload = content.learner_resource(course_id, resource_path)
    return Response(content=payload, media_type="text/csv")


