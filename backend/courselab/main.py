"""FastAPI learner service with server-owned records and versioned assessment."""

import time
from collections import defaultdict, deque

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .assessment_plans import AssessmentPlanService
from .authentication import new_dummy_password_hash
from .authentication import router as auth_router
from .bench import BenchLibrary
from .bench_routes import router as bench_router
from .case_studio import router as case_studio_router
from .catalog import router as catalog_router
from .config import Settings
from .content import ContentInvalid, ContentMissing, ContentRepository
from .course_archives import CourseContentArchiveService
from .db import database
from .dependencies import DB
from .enrollments import router as enrollments_router
from .gradebook import router as gradebook_router
from .graded_appeals import router as graded_appeals_router
from .graded_assessments import GradedAssessmentService
from .graded_routes import router as graded_routes_router
from .graded_views import GradedSubmissionViews
from .grading import GradingUnavailable
from .instructor_appeals import router as instructor_appeals_router
from .learner_account import router as learner_account_router
from .learner_state import router as learner_state_router
from .learning import router as learning_router
from .practice_attempts import router as practice_attempts_router
from .retrieval_routes import router as retrieval_router


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or Settings.from_environment()
    app = FastAPI(title="uniStemCourseSimulators API", version="0.2.0", docs_url=None, redoc_url=None)
    engine, session_factory = database(settings.database_url)
    content = ContentRepository(settings.content_root, settings.private_assessments_root)
    assessment_plans = AssessmentPlanService(settings, content)
    course_archives = CourseContentArchiveService(content)
    graded_assessments = GradedAssessmentService(settings, content, assessment_plans)
    app.state.engine = engine
    app.state.sessions = session_factory
    app.state.content = content
    app.state.bench = BenchLibrary(settings.content_root)
    app.state.assessment_plans = assessment_plans
    app.state.course_archives = course_archives
    app.state.graded_assessments = graded_assessments
    graded_views = GradedSubmissionViews(content)
    app.state.graded_views = graded_views
    app.state.settings = settings
    app.state.dummy_password_hash = new_dummy_password_hash()
    app.include_router(catalog_router)
    app.include_router(auth_router)
    app.add_middleware(CORSMiddleware, allow_origins=list(settings.allowed_origins), allow_credentials=True,
                       allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
                       allow_headers=["Content-Type", "X-CSRF-Token"])
    app.include_router(learning_router)
    app.include_router(learner_state_router)
    app.include_router(case_studio_router)
    app.include_router(bench_router)
    app.include_router(practice_attempts_router)
    app.include_router(retrieval_router)
    app.include_router(instructor_appeals_router)
    app.include_router(gradebook_router)
    app.include_router(graded_routes_router)
    app.include_router(graded_appeals_router)
    app.include_router(learner_account_router)
    app.include_router(enrollments_router)
    # In-memory throttling is appropriate to the single-worker development slice.
    # Production multi-worker deployment must put a shared rate limiter at the proxy.
    requests: dict[tuple[str, str], deque] = defaultdict(deque)

    @app.middleware("http")
    async def boundaries(request: Request, call_next):
        unsafe = request.method not in {"GET", "HEAD", "OPTIONS"}
        if unsafe:
            origin = request.headers.get("origin")
            if origin not in settings.allowed_origins:
                return JSONResponse({"detail": "A permitted Origin is required for mutations"}, status_code=403)
            try:
                if int(request.headers.get("content-length", "0")) > settings.body_limit:
                    return JSONResponse({"detail": "Submission too large"}, status_code=413)
            except ValueError:
                return JSONResponse({"detail": "Malformed content length"}, status_code=400)
            # Stream only up to the ceiling and replay the cached body to FastAPI.
            chunks, size = [], 0
            async for chunk in request.stream():
                size += len(chunk)
                if size > settings.body_limit:
                    return JSONResponse({"detail": "Submission too large"}, status_code=413)
                chunks.append(chunk)
            request._body = b"".join(chunks)
            # Security-sensitive path decisions use the router's raw ASGI path,
            # not URL reconstruction from caller-controlled Host values.
            category = "auth" if request.scope["path"].startswith("/api/v1/auth") else "write"
            key = (request.client.host if request.client else "unknown", category)
            bucket = requests[key]
            instant = time.monotonic()
            while bucket and instant - bucket[0] >= 60:
                bucket.popleft()
            limit = settings.auth_rate_limit if category == "auth" else settings.rate_limit
            if len(bucket) >= limit:
                return JSONResponse({"detail": "Try again later"}, status_code=429, headers={"Retry-After": "60"})
            bucket.append(instant)
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.exception_handler(ContentMissing)
    async def missing(_, exception):
        return JSONResponse({"detail": str(exception)}, status_code=404)

    @app.exception_handler(ContentInvalid)
    async def invalid(_, __):
        return JSONResponse({"detail": "Invalid server content package"}, status_code=503)

    @app.exception_handler(GradingUnavailable)
    async def grading_unavailable(_, exception):
        return JSONResponse({"detail": str(exception), "capability": "unavailable"}, status_code=422)

    @app.exception_handler(IntegrityError)
    async def conflict(_, __):
        # The yielded session is closed/rolled back after the request. Never return
        # SQL, parameter values, database connection strings or driver tracebacks.
        return JSONResponse({"detail": "Conflicting or concurrent update; reload and retry"}, status_code=409)

    @app.get("/api/v1/health")
    def health(db: DB):
        db.execute(select(1))
        return {"status": "ok", "programming_runner": "disabled", "llm_feedback": "disabled"}

    return app


app = create_app()
