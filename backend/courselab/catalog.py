"""Public course-catalog and curriculum endpoints."""

from fastapi import APIRouter, Request

from .dependencies import DB, require_course_enrollment, require_identity
from .schemas import CourseSummary, PublicCourse, PublicCurriculum

router = APIRouter(prefix="/api/v1")


@router.get("/courses", response_model=list[CourseSummary])
def courses(request: Request):
    return request.app.state.content.catalog()


@router.get("/curriculum", response_model=PublicCurriculum)
def curriculum(request: Request):
    return request.app.state.content.curriculum()


@router.get("/sources")
def sources(request: Request):
    return request.app.state.content.sources()


@router.get("/courses/{course_id}", response_model=PublicCourse)
def course(course_id: str, request: Request):
    return request.app.state.content.course(course_id)


@router.get("/courses/{course_id}/versions", response_model=list[str])
def archived_course_versions(course_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    require_course_enrollment(db, user, course_id)
    return request.app.state.course_archives.list_versions(db, course_id)


@router.get(
    "/courses/{course_id}/versions/{content_version}", response_model=PublicCourse
)
def archived_course(course_id: str, content_version: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    require_course_enrollment(db, user, course_id)
    with request.app.state.course_archives.archived_repository(
        db, course_id, content_version
    ) as content:
        return content.course(course_id)
