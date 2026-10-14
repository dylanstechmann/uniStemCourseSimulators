"""Private case drafts; self-checks never enter grades or objective evidence."""

from fastapi import APIRouter, HTTPException, Request
from sqlalchemy import select, update

from .db import CaseDraft, now
from .dependencies import DB, require_course_enrollment, require_csrf, require_enrollment, require_identity
from .schemas import CaseDraftRequest
from .serialization import timestamp

router = APIRouter(prefix="/api/v1/case-drafts")


def draft_view(draft: CaseDraft) -> dict:
    return {
        "id": draft.id, "course_id": draft.course_id, "case_id": draft.case_id,
        "content_version": draft.content_version, "case_sha256": draft.case_sha256,
        "case_snapshot": draft.case_snapshot_json, "response": draft.response,
        "checked_criteria": draft.checked_criteria_json, "revision": draft.revision,
        "updated_at": timestamp(draft.updated_at),
    }


@router.get("/{course_id}")
def drafts(course_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    require_course_enrollment(db, user, course_id)
    return [draft_view(draft) for draft in db.scalars(
        select(CaseDraft).where(CaseDraft.user_id == user.id, CaseDraft.course_id == course_id)
        .order_by(CaseDraft.updated_at.desc(), CaseDraft.id)
    )]


@router.put("/{course_id}/{case_id}")
def save_draft(course_id: str, case_id: str, body: CaseDraftRequest, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    enrollment = require_enrollment(db, identity[0], course_id, content)
    case = next((case for case in content.case_studies(course_id) if case.id == case_id), None)
    if case is None:
        raise HTTPException(404, "Case study not found")
    if body.content_version != enrollment.content_version or body.case_sha256 != case.case_sha256:
        raise HTTPException(409, "The case changed; reload its prompt before saving a new draft")
    criterion_ids = {criterion.id for criterion in case.criteria}
    if any(criterion not in criterion_ids for criterion in body.checked_criteria):
        raise HTTPException(422, "Self-check criteria must belong to this case")
    checked = [criterion.id for criterion in case.criteria if criterion.id in body.checked_criteria]
    draft = db.scalar(select(CaseDraft).where(
        CaseDraft.user_id == identity[0].id, CaseDraft.course_id == course_id,
        CaseDraft.case_id == case_id, CaseDraft.content_version == body.content_version,
        CaseDraft.case_sha256 == case.case_sha256,
    ))
    if draft is None:
        if body.expected_revision != 0:
            raise HTTPException(409, "The saved draft changed; load its saved copy before editing")
        draft = CaseDraft(
            user_id=identity[0].id, course_id=course_id, case_id=case_id,
            content_version=body.content_version, case_sha256=case.case_sha256,
            case_snapshot_json=case.model_dump(), response=body.response,
            checked_criteria_json=checked, revision=1, updated_at=now(),
        )
        db.add(draft)
    else:
        result = db.execute(update(CaseDraft).where(
            CaseDraft.id == draft.id, CaseDraft.revision == body.expected_revision,
        ).values(response=body.response, checked_criteria_json=checked,
                 revision=body.expected_revision + 1, updated_at=now()))
        if result.rowcount != 1:
            db.rollback()
            raise HTTPException(409, "The saved draft changed; load its saved copy before editing")
    db.commit()
    db.refresh(draft)
    return draft_view(draft)
