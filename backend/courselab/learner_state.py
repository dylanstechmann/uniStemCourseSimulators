"""Authenticated learner progress, notes and bookmarks."""

from fastapi import APIRouter, HTTPException, Query, Request
from sqlalchemy import func, select

from .db import Bookmark, Enrollment, Note, Progress, now
from .dependencies import DB, require_csrf, require_enrollment, require_identity
from .schemas import BookmarkRequest, NoteRequest, ProgressRequest
from .serialization import timestamp

router = APIRouter(prefix="/api/v1")


@router.patch("/progress/{course_id}/{lesson_id}")
def save_progress(course_id: str, lesson_id: str, body: ProgressRequest, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    require_enrollment(db, identity[0], course_id, content)
    content.lesson_record(course_id, lesson_id)
    record = db.scalar(
        select(Progress).where(
            Progress.user_id == identity[0].id,
            Progress.course_id == course_id,
            Progress.lesson_id == lesson_id,
        )
    )
    if not record:
        record = Progress(user_id=identity[0].id, course_id=course_id, lesson_id=lesson_id)
        db.add(record)
    record.completed, record.updated_at = body.completed, now()
    db.commit()
    return {"lesson_id": lesson_id, "completed": record.completed, "evidence": "learner-marked"}


@router.get("/progress/{course_id}")
def progress(course_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    content = request.app.state.content
    require_enrollment(db, user, course_id, content)
    return [
        {
            "lesson_id": item.lesson_id,
            "completed": item.completed,
            "updated_at": timestamp(item.updated_at),
            "evidence": "learner-marked",
        }
        for item in db.scalars(
            select(Progress).where(Progress.user_id == user.id, Progress.course_id == course_id)
        )
    ]


@router.put("/notes/{course_id}/{lesson_id}")
def save_note(course_id: str, lesson_id: str, body: NoteRequest, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    require_enrollment(db, identity[0], course_id, content)
    content.lesson_record(course_id, lesson_id)
    note = db.scalar(
        select(Note).where(
            Note.user_id == identity[0].id,
            Note.course_id == course_id,
            Note.lesson_id == lesson_id,
        )
    )
    if not note:
        note = Note(user_id=identity[0].id, course_id=course_id, lesson_id=lesson_id)
        db.add(note)
    # Plain text storage: frontend must render as text, never unsanitized HTML.
    note.body, note.updated_at = body.body, now()
    db.commit()
    return {"lesson_id": lesson_id, "body": note.body, "updated_at": timestamp(note.updated_at)}


@router.get("/notes/{course_id}")
def notes(course_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    require_enrollment(db, user, course_id, request.app.state.content)
    return [
        {"lesson_id": item.lesson_id, "body": item.body, "updated_at": timestamp(item.updated_at)}
        for item in db.scalars(select(Note).where(Note.user_id == user.id, Note.course_id == course_id))
    ]


@router.get("/notes")
def notebook_notes(
    request: Request,
    db: DB,
    q: str = Query(default="", max_length=200),
    course_id: str | None = Query(default=None, max_length=100),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=50, ge=1, le=100),
):
    user, _ = require_identity(request, db)
    content = request.app.state.content
    enrollments = db.scalars(select(Enrollment).where(Enrollment.user_id == user.id)).all()
    enrollment_by_course = {item.course_id: item for item in enrollments}

    if course_id is not None:
        if course_id not in enrollment_by_course:
            raise HTTPException(403, "Enroll in this course first")
        require_enrollment(db, user, course_id, content)
        course_ids = [course_id]
    else:
        course_ids = [
            item.course_id
            for item in enrollments
            if item.content_version == content.manifest(item.course_id)["version"]
        ]

    if not course_ids:
        return {"items": [], "total": 0, "offset": offset, "limit": limit}

    criteria = [
        Note.user_id == user.id,
        Note.course_id.in_(course_ids),
        func.trim(Note.body) != "",
    ]
    search_text = q.strip().lower()
    if search_text:
        criteria.append(func.lower(Note.body).contains(search_text, autoescape=True))
    total = db.scalar(select(func.count(Note.id)).where(*criteria)) or 0
    records = db.scalars(
        select(Note)
        .where(*criteria)
        .order_by(Note.updated_at.desc(), Note.course_id, Note.lesson_id)
        .offset(offset)
        .limit(limit)
    ).all()

    course_labels = {}
    for selected_course_id in {item.course_id for item in records}:
        manifest = content.manifest(selected_course_id)
        lesson_titles = {
            lesson["id"]: lesson["title"] for module in manifest["modules"] for lesson in module["lessons"]
        }
        course_labels[selected_course_id] = (manifest["title"], lesson_titles)

    return {
        "items": [
            {
                "course_id": item.course_id,
                "course_title": course_labels[item.course_id][0],
                "lesson_id": item.lesson_id,
                "lesson_title": course_labels[item.course_id][1].get(item.lesson_id, item.lesson_id),
                "body": item.body,
                "updated_at": timestamp(item.updated_at),
            }
            for item in records
        ],
        "total": total,
        "offset": offset,
        "limit": limit,
    }


@router.put("/bookmarks/{course_id}")
def save_bookmark(course_id: str, body: BookmarkRequest, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    content.manifest(course_id)
    bookmark = db.scalar(
        select(Bookmark).where(Bookmark.user_id == identity[0].id, Bookmark.course_id == course_id)
    )
    if body.saved and not bookmark:
        db.add(Bookmark(user_id=identity[0].id, course_id=course_id))
    elif not body.saved and bookmark:
        db.delete(bookmark)
    db.commit()
    return {"course_id": course_id, "saved": body.saved}


@router.get("/bookmarks")
def bookmarks(request: Request, db: DB):
    user, _ = require_identity(request, db)
    return [item.course_id for item in db.scalars(select(Bookmark).where(Bookmark.user_id == user.id))]
