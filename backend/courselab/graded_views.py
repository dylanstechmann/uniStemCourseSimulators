"""Verified learner and reviewer views for graded submissions."""

import base64
import binascii
import hashlib
import json
import math

from sqlalchemy import select
from sqlalchemy.orm import Session

from .assessment import canonical_digest
from .content import ContentInvalid, ContentMissing, ContentRepository
from .db import (
    AssessmentInstance,
    AssessmentPlan,
    AssessmentSourceArchive,
    Enrollment,
    GradedSubmission,
    GradedSubmissionAppeal,
    GradedSubmissionAppealReview,
    User,
)
from .grading import question_spec_digest
from .schemas import AttemptRequest
from .serialization import timestamp
from .variants import resolve_variant


class GradedSubmissionViews:
    def __init__(self, content: ContentRepository):
        self.content = content

    def appeal_view(
        self,
        appeal: GradedSubmissionAppeal,
        submission: GradedSubmission,
        instance: AssessmentInstance,
        course_id: str,
        review: GradedSubmissionAppealReview | None = None,
    ) -> dict:
        effective_score = (
            float(review.override_score)
            if review and review.decision == "adjusted"
            else float(submission.score)
        )
        return {
            "id": appeal.id,
            "submission_id": submission.id,
            "course_id": course_id,
            "assessment_id": instance.assessment_id,
            "attempt_number": submission.attempt_number,
            "reason": appeal.reason,
            "status": review.decision if review else "open",
            "decision": review.decision if review else None,
            "review_note": review.review_note if review else None,
            "original_score": float(submission.score),
            "effective_score": effective_score,
            "max_score": float(submission.max_score),
            "created_at": timestamp(appeal.created_at),
            "reviewed_at": timestamp(review.created_at) if review else None,
        }

    def submission_view(
        self,
        item: GradedSubmission,
        instance: AssessmentInstance,
        course_id: str,
        db: Session,
    ) -> dict:
        appeal = db.scalar(
            select(GradedSubmissionAppeal).where(GradedSubmissionAppeal.submission_id == item.id)
        )
        review = (
            db.scalar(
                select(GradedSubmissionAppealReview).where(
                    GradedSubmissionAppealReview.appeal_id == appeal.id
                )
            )
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
            "course_id": course_id,
            "assessment_id": instance.assessment_id,
            "content_version": item.content_version,
            "attempt_number": item.attempt_number,
            "responses": item.responses_json,
            "results": item.results_json,
            "score": float(item.score),
            "effective_score": effective_score,
            "max_score": float(item.max_score),
            "score_percent": round(float(item.score) / float(item.max_score) * 100, 2),
            "effective_score_percent": round(effective_score / float(item.max_score) * 100, 2),
            "submitted_at": timestamp(item.submitted_at),
            "appeal": self.appeal_view(appeal, item, instance, course_id, review) if appeal else None,
        }

    def verified_review_questions(
        self,
        db: Session,
        submission: GradedSubmission,
        enrollment: Enrollment,
        plan: AssessmentPlan,
        instance: AssessmentInstance,
    ) -> list[dict] | None:
        """Return exact answer-free question specs only while every saved digest matches."""
        try:
            if (
                submission.plan_id != plan.id
                or submission.assessment_instance_id != instance.id
                or instance.plan_id != plan.id
                or plan.enrollment_id != enrollment.id
                or plan.grading_mode != "graded-course"
                or plan.content_version != submission.content_version
                or enrollment.content_version != submission.content_version
            ):
                return None
            archive = db.scalar(
                select(AssessmentSourceArchive).where(
                    AssessmentSourceArchive.course_id == enrollment.course_id,
                    AssessmentSourceArchive.content_version == submission.content_version,
                    AssessmentSourceArchive.assessment_id == instance.assessment_id,
                    AssessmentSourceArchive.source_sha256 == instance.source_sha256,
                )
            )
            if archive is None:
                return None
            source_bytes = bytes(archive.source_bytes)
            source_sha256 = hashlib.sha256(source_bytes).hexdigest()
            if (
                source_sha256 != instance.source_sha256
                or source_sha256 != submission.source_sha256
                or instance.mode != "graded"
                or instance.question_ids == []
            ):
                return None
            package = json.loads(source_bytes.decode("utf-8"))
            if (
                package.get("course_id") != enrollment.course_id
                or not isinstance(package.get("questions"), list)
            ):
                return None
            by_id = {}
            for question in package["questions"]:
                question_id = question.get("id") if isinstance(question, dict) else None
                if not isinstance(question_id, str) or question_id in by_id:
                    return None
                by_id[question_id] = question
            question_ids = instance.question_ids
            if (
                not isinstance(question_ids, list)
                or not question_ids
                or len(question_ids) != len(set(question_ids))
                or any(question_id not in by_id for question_id in question_ids)
            ):
                return None
            source_questions = [by_id[question_id] for question_id in question_ids]
            points = sum(float(question["points"]) for question in source_questions)
            if not math.isclose(points, float(instance.points), rel_tol=0, abs_tol=1e-8):
                return None
            if not math.isclose(points, float(submission.max_score), rel_tol=0, abs_tol=1e-8):
                return None
            results = submission.results_json
            if not isinstance(results, list) or len(results) != len(question_ids):
                return None
            result_by_id = {
                result.get("question_id"): result
                for result in results
                if isinstance(result, dict) and isinstance(result.get("question_id"), str)
            }
            if set(result_by_id) != set(question_ids):
                return None
            questions = []
            variant_map = {}
            for question in source_questions:
                variant_id = result_by_id[question["id"]].get("variant_id")
                if variant_id is not None and not isinstance(variant_id, str):
                    return None
                questions.append(resolve_variant(question, variant_id))
                variant_map[question["id"]] = variant_id
            spec_digest = canonical_digest(
                {
                    "grader": [
                        question_spec_digest(question, variant_map[question["id"]])
                        for question in questions
                    ],
                    "source_sha256": instance.source_sha256,
                }
            )
            if spec_digest != submission.question_spec_sha256:
                return None
            if set(submission.responses_json) != set(question_ids):
                return None
            return questions
        except (
            ContentInvalid,
            ContentMissing,
            OSError,
            UnicodeDecodeError,
            json.JSONDecodeError,
            AttributeError,
            KeyError,
            TypeError,
            ValueError,
            ArithmeticError,
        ):
            return None

    def instructor_appeal_record(
        self, appeal: GradedSubmissionAppeal, submission: GradedSubmission, db: Session
    ) -> dict:
        enrollment = db.get(Enrollment, submission.enrollment_id)
        instance = db.get(AssessmentInstance, submission.assessment_instance_id)
        plan = db.get(AssessmentPlan, submission.plan_id)
        review = db.scalar(
            select(GradedSubmissionAppealReview).where(
                GradedSubmissionAppealReview.appeal_id == appeal.id
            )
        )
        learner = db.get(User, appeal.user_id)
        questions = (
            self.verified_review_questions(db, submission, enrollment, plan, instance)
            if enrollment and plan and instance
            else None
        )
        public_questions = None
        public_responses = {}
        if questions is not None:
            public_questions = [
                self.content.public_question(question)
                .model_copy(update={"assessment_role": "graded"})
                .model_dump()
                for question in questions
            ]
            question_by_id = {question["id"]: question for question in questions}
            try:
                for question_id, raw_response in submission.responses_json.items():
                    data = dict(raw_response)
                    value = data.get("response")
                    if question_by_id[question_id].get("type") == "file_upload":
                        encoded = value.get("content_base64") if isinstance(value, dict) else None
                        if not isinstance(encoded, str):
                            raise ValueError("Missing saved CSV upload")
                        decoded = base64.b64decode(encoded, validate=True).decode("utf-8-sig")
                        value = {"content_text": decoded}
                    data["response"] = value
                    public_responses[question_id] = AttemptRequest.model_validate(data).model_dump(
                        exclude_none=True
                    )
            except (
                AttributeError,
                binascii.Error,
                KeyError,
                TypeError,
                UnicodeDecodeError,
                ValueError,
            ):
                questions = None
                public_questions = None
                public_responses = {}
        view = (
            self.appeal_view(appeal, submission, instance, enrollment.course_id, review)
            if instance and enrollment
            else {
                "id": appeal.id,
                "submission_id": submission.id,
                "course_id": enrollment.course_id if enrollment else "",
                "assessment_id": "",
                "attempt_number": submission.attempt_number,
                "reason": appeal.reason,
                "status": review.decision if review else "open",
                "decision": review.decision if review else None,
                "review_note": review.review_note if review else None,
                "original_score": float(submission.score),
                "effective_score": (
                    float(review.override_score)
                    if review and review.decision == "adjusted"
                    else float(submission.score)
                ),
                "max_score": float(submission.max_score),
                "created_at": timestamp(appeal.created_at),
                "reviewed_at": timestamp(review.created_at) if review else None,
            }
        )
        return {
            **view,
            "learner": learner.email if learner and learner.email else "Guest account",
            "specification_verified": questions is not None,
            "assessment_title": (
                instance.title or instance.assessment_id if instance else "Unavailable assessment"
            ),
            "questions": public_questions,
            "responses": public_responses,
            "automatic_results": submission.results_json,
            "specification_pinned": bool(submission.question_spec_sha256),
        }
