"""Protected graded delivery, public practice delivery and submission routes."""

import hashlib
import json
import math
import secrets

from fastapi import APIRouter, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .assessment import canonical_digest
from .content import ContentInvalid, ContentMissing
from .db import (
    AssessmentInstance,
    GradedAssessmentAssignment,
    GradedSubmission,
    now,
)
from .dependencies import DB, require_csrf, require_enrollment, require_identity
from .grading import GradingUnavailable, grade, question_spec_digest
from .schemas import (
    AssessmentQuestionsResponse,
    AssessmentSubmissionRequest,
    AssessmentSubmissionResponse,
    PracticeAssessmentResponse,
)
from .variants import (
    VariantTokenError,
    assignment_form_ids,
    issue_variant_token,
    resolve_variant,
)

router = APIRouter()


@router.get(
    "/api/v1/assessments/{course_id}/{assessment_id}/questions",
    response_model=AssessmentQuestionsResponse,
)
def graded_assessment_questions(course_id: str, assessment_id: str, request: Request, db: DB):
    user, _ = require_identity(request, db)
    content = request.app.state.content
    enrollment = require_enrollment(db, user, course_id, content)
    manifest = content.manifest(course_id)
    graded_assessments = request.app.state.graded_assessments
    _, instance, questions, attempts_used, _ = graded_assessments.load(
        db, enrollment, manifest, assessment_id
    )
    current = now()
    if instance.release_at and current < instance.release_at:
        raise HTTPException(409, "This assessment has not been released")
    status = "closed" if instance.due_at and current > instance.due_at else "open"
    questions, assignment_token = graded_assessments.assignment_form(
        db, enrollment, instance, questions, attempts_used, status
    )
    assignment = db.get(GradedAssessmentAssignment, assignment_token) if assignment_token else None
    assignment_variants = assignment.variant_ids_json if assignment else {}
    db.commit()
    return {
        "course_id": course_id,
        "assessment_id": instance.assessment_id,
        "title": instance.title or instance.assessment_id.replace("-", " ").title(),
        "content_version": enrollment.content_version,
        "points": float(instance.points),
        "questions": [
            content.public_question(question)
            .model_copy(
                update={
                    "assessment_role": "graded",
                    "variant_id": assignment_variants.get(question["id"]),
                }
            )
            .model_dump()
            for question in questions
        ],
        "attempts_used": attempts_used,
        "attempt_limit": instance.attempt_limit,
        "schedule_status": status,
        "assignment_token": assignment_token,
    }


@router.get(
    "/api/v1/assessments/{course_id}/{assessment_id}/practice-questions",
    response_model=PracticeAssessmentResponse,
)
def practice_assessment_questions(course_id: str, assessment_id: str, request: Request, db: DB):
    """Serve only enrollment-pinned, explicitly public formative questions."""
    user, _ = require_identity(request, db)
    content = request.app.state.content
    enrollment = require_enrollment(db, user, course_id, content)
    manifest = content.manifest(course_id)
    plan = request.app.state.assessment_plans.ensure_assessment_plan(db, enrollment, manifest)
    instance = db.scalar(
        select(AssessmentInstance).where(
            AssessmentInstance.plan_id == plan.id,
            AssessmentInstance.assessment_id == assessment_id,
        )
    )
    if (
        not instance
        or instance.mode != "practice"
        or instance.assessment_type
        not in {"practice", "homework", "lab", "simulation", "data-analysis"}
        or instance.source_path != "question-banks/practice.json"
        or instance.points <= 0
        or not instance.question_ids
    ):
        raise HTTPException(404, "Public practice assessment not found")
    try:
        source_path = content.assessment_source_file(enrollment.course_id, instance.source_path)
        source_bytes = source_path.read_bytes()
    except (ContentInvalid, ContentMissing, OSError) as exc:
        raise HTTPException(409, "The pinned practice source is unavailable") from exc
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    if not secrets.compare_digest(source_sha256, instance.source_sha256):
        raise HTTPException(409, "Practice content changed after this enrollment version was pinned")
    try:
        package = json.loads(source_bytes.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise HTTPException(409, "The pinned practice source is invalid") from exc
    if (
        not isinstance(package, dict)
        or package.get("course_id") != enrollment.course_id
        or not isinstance(package.get("questions"), list)
    ):
        raise HTTPException(409, "The pinned practice source has an invalid course mapping")
    questions_by_id = {}
    for question in package["questions"]:
        question_id = question.get("id") if isinstance(question, dict) else None
        if not isinstance(question_id, str) or question_id in questions_by_id:
            raise HTTPException(409, "The pinned practice bank has invalid question identifiers")
        questions_by_id[question_id] = question
    question_ids = instance.question_ids
    if (
        not isinstance(question_ids, list)
        or any(not isinstance(question_id, str) for question_id in question_ids)
        or len(question_ids) != len(set(question_ids))
        or any(
            question_id not in questions_by_id
            or questions_by_id[question_id].get("visibility") != "public-practice-authoring"
            for question_id in question_ids
        )
    ):
        raise HTTPException(
            409, "The practice assessment must reference only explicit public practice items"
        )
    questions = [questions_by_id[question_id] for question_id in question_ids]
    try:
        question_points = sum(float(question["points"]) for question in questions)
    except (KeyError, TypeError, ValueError) as exc:
        raise HTTPException(409, "The pinned practice point mapping is invalid") from exc
    if not math.isclose(question_points, float(instance.points), rel_tol=0, abs_tol=1e-8):
        raise HTTPException(409, "Question points do not match the pinned practice total")
    public_questions = []
    for question in questions:
        try:
            token, variant_id, resolved = issue_variant_token(
                question,
                course_id,
                enrollment.content_version,
                request.app.state.settings.variant_token_secret,
            )
        except VariantTokenError as exc:
            raise HTTPException(409, "The pinned practice variant configuration is invalid") from exc
        public_questions.append(content.public_question(resolved, variant_id, token).model_dump())
    db.commit()
    return {
        "course_id": course_id,
        "assessment_id": instance.assessment_id,
        "title": instance.title or instance.assessment_id.replace("-", " ").title(),
        "content_version": enrollment.content_version,
        "points": float(instance.points),
        "questions": public_questions,
    }


@router.post(
    "/api/v1/assessments/{course_id}/{assessment_id}/submissions",
    status_code=201,
    response_model=AssessmentSubmissionResponse,
)
def submit_graded_assessment(
    course_id: str,
    assessment_id: str,
    body: AssessmentSubmissionRequest,
    request: Request,
    db: DB,
):
    identity = require_identity(request, db)
    require_csrf(request, identity)
    content = request.app.state.content
    enrollment = require_enrollment(db, identity[0], course_id, content)
    manifest = content.manifest(course_id)
    graded_assessments = request.app.state.graded_assessments
    plan, instance, questions, attempts_used, spec_digest = graded_assessments.load(
        db, enrollment, manifest, assessment_id
    )
    try:
        forms = assignment_form_ids(questions)
    except VariantTokenError as exc:
        raise HTTPException(409, "The pinned assessment authored-form configuration is invalid") from exc
    attempt_number = attempts_used + 1
    variant_map: dict[str, str | None] = {}
    if forms:
        if not body.assignment_token:
            raise HTTPException(409, "The assigned authored form token is required for this submission")
        assignment = db.get(GradedAssessmentAssignment, body.assignment_token)
        if (
            assignment is None
            or assignment.enrollment_id != enrollment.id
            or assignment.assessment_instance_id != instance.id
            or assignment.content_version != enrollment.content_version
            or assignment.source_sha256 != instance.source_sha256
            or not isinstance(assignment.variant_ids_json, dict)
            or set(assignment.variant_ids_json) != {question["id"] for question in questions}
        ):
            raise HTTPException(409, "The assigned authored form token is invalid for this learner and assessment")
        variant_map = assignment.variant_ids_json
        attempt_number = assignment.attempt_number
        try:
            questions = [
                resolve_variant(question, variant_map[question["id"]]) for question in questions
            ]
            spec_digest = canonical_digest(
                {
                    "grader": [
                        question_spec_digest(question, variant_map[question["id"]])
                        for question in questions
                    ],
                    "source_sha256": instance.source_sha256,
                }
            )
        except (VariantTokenError, TypeError, ValueError) as exc:
            raise HTTPException(409, "The assigned authored form is invalid") from exc
        if not secrets.compare_digest(spec_digest, assignment.question_spec_sha256):
            raise HTTPException(409, "The assigned authored form failed verification")

        # A retry with the same opaque token returns the already-saved outcome, even
        # if it arrives after the deadline or the learner has used the last attempt.
        previous = db.scalar(
            select(GradedSubmission).where(
                GradedSubmission.enrollment_id == enrollment.id,
                GradedSubmission.assessment_instance_id == instance.id,
                GradedSubmission.attempt_number == attempt_number,
            )
        )
        if previous is not None:
            if (
                previous.source_sha256 != assignment.source_sha256
                or previous.question_spec_sha256 != assignment.question_spec_sha256
            ):
                raise HTTPException(409, "The saved submission does not match its authored-form assignment")
            return request.app.state.graded_views.submission_view(previous, instance, course_id, db)
        if attempt_number != attempts_used + 1:
            raise HTTPException(409, "This authored-form assignment is no longer the current attempt")
    elif body.assignment_token:
        raise HTTPException(409, "This fixed-form assessment does not accept an assignment token")

    current = now()
    if instance.release_at and current < instance.release_at:
        raise HTTPException(409, "This assessment has not been released")
    if instance.due_at and current > instance.due_at:
        raise HTTPException(409, "The submission deadline has passed")
    if instance.attempt_limit is not None and attempts_used >= instance.attempt_limit:
        raise HTTPException(409, "The attempt limit has been reached")
    expected_ids = {question["id"] for question in questions}
    if set(body.responses) != expected_ids:
        raise HTTPException(422, "Submit exactly one response for every question in this assessment")

    item_results = []
    normalized_responses = {}
    earned = 0.0
    try:
        for question in questions:
            question_id = question["id"]
            answer = body.responses[question_id]
            result = grade(question, answer)
            earned += result.score
            normalized_responses[question_id] = answer.model_dump(exclude_none=True)
            item_results.append(
                {
                    "question_id": question_id,
                    "variant_id": variant_map.get(question_id),
                    "score": result.score,
                    "max_score": result.max_score,
                    "feedback": result.feedback.model_dump(),
                }
            )
    except (GradingUnavailable, ArithmeticError, KeyError, TypeError, ValueError) as exc:
        raise HTTPException(
            409, "This assessment contains an unsupported or invalid grading specification"
        ) from exc

    maximum = float(instance.points)
    if not math.isclose(
        sum(result["max_score"] for result in item_results), maximum, rel_tol=0, abs_tol=1e-8
    ):
        raise HTTPException(409, "The assessment grading total does not match its pinned points")
    row = GradedSubmission(
        enrollment_id=enrollment.id,
        plan_id=plan.id,
        assessment_instance_id=instance.id,
        content_version=enrollment.content_version,
        attempt_number=attempt_number,
        source_sha256=instance.source_sha256,
        question_spec_sha256=spec_digest,
        responses_json=normalized_responses,
        results_json=item_results,
        score=earned,
        max_score=maximum,
        submitted_at=current,
    )
    db.add(row)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        if forms and body.assignment_token:
            previous = db.scalar(
                select(GradedSubmission).where(
                    GradedSubmission.enrollment_id == enrollment.id,
                    GradedSubmission.assessment_instance_id == instance.id,
                    GradedSubmission.attempt_number == attempt_number,
                )
            )
            if previous is not None and previous.question_spec_sha256 == spec_digest:
                return request.app.state.graded_views.submission_view(
                    previous, instance, course_id, db
                )
        raise HTTPException(
            409, "A concurrent submission changed the attempt count; reload this assessment"
        ) from exc
    db.refresh(row)
    return request.app.state.graded_views.submission_view(row, instance, course_id, db)
