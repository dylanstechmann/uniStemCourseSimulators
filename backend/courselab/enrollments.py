"""Enrollment lifecycle and the learner-facing assessment-plan view."""

from fastapi import APIRouter, HTTPException, Request
from sqlalchemy import func, select

from .assessment import effective_protection
from .db import AssessmentInstance, Enrollment, GradedSubmission, now
from .dependencies import DB, require_csrf, require_enrollment, require_identity
from .schemas import AssessmentPlanResponse, EnrollmentRequest
from .serialization import timestamp

router = APIRouter()


@router.post("/api/v1/enrollments", status_code=201)
def enroll(body: EnrollmentRequest, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    manifest = content.manifest(body.course_id)
    if manifest["maturity"] in {"catalog-only", "outlined"} and not manifest["modules"]:
        raise HTTPException(409, "This course has no authored lessons yet")
    existing = db.scalar(
        select(Enrollment).where(
            Enrollment.user_id == identity[0].id,
            Enrollment.course_id == body.course_id,
        )
    )
    if not existing:
        existing = Enrollment(
            user_id=identity[0].id,
            course_id=body.course_id,
            content_version=manifest["version"],
        )
        db.add(existing)
        db.flush()
    if existing.content_version == manifest["version"]:
        request.app.state.assessment_plans.ensure_assessment_plan(db, existing, manifest)
        request.app.state.course_archives.ensure_archive(
            db, body.course_id, manifest["version"]
        )
    db.commit()
    return {
        "course_id": existing.course_id,
        "content_version": existing.content_version,
        "created_at": timestamp(existing.created_at),
    }


@router.put("/api/v1/enrollments/{course_id}/version")
def upgrade_enrollment(course_id: str, request: Request, db: DB):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    manifest = content.manifest(course_id)
    enrollment = db.scalar(
        select(Enrollment).where(
            Enrollment.user_id == identity[0].id,
            Enrollment.course_id == course_id,
        )
    )
    if not enrollment:
        raise HTTPException(403, "Enroll in this course before updating its version")
    # This explicit operation preserves every prior attempt and its original version.
    enrollment.content_version = manifest["version"]
    request.app.state.assessment_plans.ensure_assessment_plan(db, enrollment, manifest)
    request.app.state.course_archives.ensure_archive(db, course_id, manifest["version"])
    db.commit()
    return {
        "course_id": enrollment.course_id,
        "content_version": enrollment.content_version,
        "created_at": timestamp(enrollment.created_at),
    }


@router.get("/api/v1/enrollments")
def enrollments(request: Request, db: DB):
    user, _ = require_identity(request, db)
    return [
        {
            "course_id": item.course_id,
            "content_version": item.content_version,
            "created_at": timestamp(item.created_at),
        }
        for item in db.scalars(select(Enrollment).where(Enrollment.user_id == user.id))
    ]


@router.get("/api/v1/assessments/{course_id}", response_model=AssessmentPlanResponse)
def assessment_plan(course_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    content = request.app.state.content
    enrollment = require_enrollment(db, user, course_id, content)
    manifest = content.manifest(course_id)
    plan = request.app.state.assessment_plans.ensure_assessment_plan(db, enrollment, manifest)
    db.commit()
    policy = plan.policy_json
    instances = list(
        db.scalars(
            select(AssessmentInstance)
            .where(AssessmentInstance.plan_id == plan.id)
            .order_by(AssessmentInstance.week, AssessmentInstance.assessment_id)
        )
    )
    submission_count = (
        db.scalar(
            select(func.count())
            .select_from(GradedSubmission)
            .where(
                GradedSubmission.enrollment_id == enrollment.id,
                GradedSubmission.plan_id == plan.id,
            )
        )
        or 0
    )
    current = now()
    visible_assessments = []
    for item in instances:
        if item.mode != "graded":
            schedule_status = "practice"
        elif item.release_at and current < item.release_at:
            schedule_status = "upcoming"
        elif item.due_at and current > item.due_at:
            schedule_status = "closed"
        else:
            schedule_status = "open"
        visible_assessments.append(
            {
                "id": item.assessment_id,
                "title": item.title or item.assessment_id.replace("-", " ").title(),
                "type": item.assessment_type,
                "mode": item.mode,
                "category_id": item.category_id,
                "week": item.week,
                "points": item.points,
                "item_count": len(item.question_ids),
                "objective_count": len(item.objective_ids),
                "release_at": timestamp(item.release_at) if item.release_at else None,
                "due_at": timestamp(item.due_at) if item.due_at else None,
                "attempt_limit": item.attempt_limit,
                "attempt_scoring": item.attempt_scoring,
                "schedule_status": schedule_status,
            }
        )
    return {
        "course_id": course_id,
        "content_version": plan.content_version,
        "assessment_protection": effective_protection(
            dict(policy or {}), request.app.state.settings.assessment_protection
        ),
        "grading_mode": plan.grading_mode,
        "course_grade_status": (
            ("configured_with_submissions" if submission_count else "configured_no_submissions")
            if plan.grading_mode == "graded-course"
            else "not_configured"
        ),
        "categories": policy["categories"],
        "category_aggregation": policy.get("category_aggregation", "points"),
        "attempt_policy": policy["attempt_policy"],
        "solution_release": policy["solution_release"],
        "late_policy": policy["late_policy"],
        "appeals": policy["appeals"],
        "assessments": visible_assessments,
    }
