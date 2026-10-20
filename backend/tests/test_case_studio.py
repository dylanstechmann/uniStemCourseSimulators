import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import select

from courselab.content import ContentRepository
from courselab.db import CaseDraft

ORIGIN = "http://localhost:8080"
COURSE = "/api/v1/courses/test-course"
DRAFTS = "/api/v1/case-drafts/test-course"
CASE_ID = "test-course:case"


@pytest.fixture
def case_source(content_root):
    directory = content_root / "courses" / "test-course"
    (directory / "rubrics").mkdir()
    case_path = directory / "rubrics" / "case-studio.json"
    case_path.write_text(json.dumps({
        "schema_version": "1.0", "course_id": "test-course", "cases": [{
            "id": CASE_ID, "prompt": "Design a matched-control experiment and bound its interpretation.",
            "mode": "self-assessment", "objective_ids": [],
            "rubric": [{"id": "control", "criterion": "Matches the delivery procedure", "points": 0,
                        "levels": [], "private_annotation": "must-not-be-published"}],
            "limitations": ["Self-check only."], "solution_spec": {"answer": "must-not-be-published"},
        }],
    }))
    manifest_path = directory / "course.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["case_rubrics"] = "rubrics/case-studio.json"
    manifest_path.write_text(json.dumps(manifest))
    return case_path


@pytest.fixture
def case_learner(guest, case_source):
    assert guest.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    return guest


def payload(client, **changes):
    case = client.get(COURSE).json()["case_studies"][0]
    return {
        "content_version": "0.1.0", "case_sha256": case["case_sha256"],
        "response": "Match delivery, test the perturbation, and limit the conclusion to this system.",
        "checked_criteria": ["control"], "expected_revision": 0, **changes,
    }


def save(client, **changes):
    return client.put(f"{DRAFTS}/{CASE_ID}", json=payload(client, **changes))


def test_public_case_is_an_explicit_ungraded_dto(client, case_source):
    response = client.get(COURSE)
    assert response.status_code == 200
    case = response.json()["case_studies"][0]
    assert case["mode"] == "self-assessment"
    assert case["criteria"] == [{"id": "control", "criterion": "Matches the delivery procedure"}]
    assert len(case["case_sha256"]) == 64
    assert "must-not-be-published" not in response.text
    assert "solution_spec" not in response.text


def test_saving_requires_identity_enrollment_csrf_and_valid_source(client, case_source):
    assert client.get(DRAFTS).status_code == 401
    assert save(client).status_code == 401
    session = client.post("/api/v1/auth/guest", json={}).json()
    client.headers["X-CSRF-Token"] = session["csrf_token"]
    assert save(client).status_code == 403
    assert client.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
    token = client.headers.pop("X-CSRF-Token")
    assert save(client).status_code == 403
    client.headers["X-CSRF-Token"] = token
    assert save(client, case_sha256="0" * 64).status_code == 409
    assert save(client, content_version="0.0.0").status_code == 409
    assert client.put(f"{DRAFTS}/missing", json=payload(client)).status_code == 404
    assert save(client, checked_criteria=["unknown"]).status_code == 422
    assert save(client, checked_criteria=["control", "control"]).status_code == 422
    assert save(client, response="x" * 20001).status_code == 422
    assert save(client, score=100).status_code == 422
    assert client.get(DRAFTS).json() == []


def test_draft_updates_are_private_and_do_not_change_gradebook(case_learner, app):
    before = case_learner.get("/api/v1/gradebook/test-course").json()
    first = save(case_learner).json()
    assert first["revision"] == 1
    assert first["case_snapshot"]["prompt"].startswith("Design a matched-control")
    assert first["checked_criteria"] == ["control"]
    second = save(case_learner, response="A revised response.", checked_criteria=[], expected_revision=1).json()
    assert second["id"] == first["id"] and second["revision"] == 2
    assert second["response"] == "A revised response."
    assert case_learner.get(DRAFTS).json() == [second]
    assert case_learner.get("/api/v1/gradebook/test-course").json() == before
    assert case_learner.get("/api/v1/attempts?course_id=test-course").json() == []
    with TestClient(app, headers={"Origin": ORIGIN}) as other:
        session = other.post("/api/v1/auth/guest", json={}).json()
        other.headers["X-CSRF-Token"] = session["csrf_token"]
        assert other.post("/api/v1/enrollments", json={"course_id": "test-course"}).status_code == 201
        assert other.get(DRAFTS).json() == []
        assert save(other).json()["id"] != first["id"]
        assert case_learner.get(DRAFTS).json() == [second]


def test_stale_browser_revision_cannot_overwrite_saved_text(case_learner):
    first = save(case_learner).json()
    assert save(case_learner, expected_revision=0, response="Stale tab").status_code == 409
    second = save(case_learner, expected_revision=1, response="Winning update").json()
    assert second["revision"] == 2
    assert save(case_learner, expected_revision=first["revision"], response="Stale edit").status_code == 409
    assert case_learner.get(DRAFTS).json()[0]["response"] == "Winning update"


def test_prompt_edits_create_separate_drafts_even_without_version_bump(case_learner, case_source):
    first = save(case_learner).json()
    old_payload = payload(case_learner, expected_revision=1)
    source = json.loads(case_source.read_text())
    source["cases"][0]["prompt"] = "A changed prompt with different evidence requirements."
    case_source.write_text(json.dumps(source))
    assert case_learner.put(f"{DRAFTS}/{CASE_ID}", json=old_payload).status_code == 409
    second = save(case_learner, response="Response to changed prompt").json()
    assert second["case_sha256"] != first["case_sha256"]
    assert second["id"] != first["id"]
    drafts = case_learner.get(DRAFTS).json()
    assert len(drafts) == 2
    assert next(item for item in drafts if item["id"] == first["id"]) == first


def test_version_update_preserves_draft_and_archived_prompt(case_learner, case_source):
    first = save(case_learner).json()
    manifest_path = case_source.parent.parent / "course.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["version"] = "0.2.0"
    manifest_path.write_text(json.dumps(manifest))
    assert save(case_learner).status_code == 409
    assert case_learner.get(DRAFTS).json() == [first]
    archived = case_learner.get(f"{COURSE}/versions/0.1.0").json()
    assert archived["case_studies"][0] == first["case_snapshot"]
    assert case_learner.put("/api/v1/enrollments/test-course/version", json={}).status_code == 200
    second = save(case_learner, content_version="0.2.0", response="New version response").json()
    assert second["id"] != first["id"]
    assert len(case_learner.get(DRAFTS).json()) == 2


def test_export_registration_and_deletion_include_case_drafts(case_learner, app):
    first = save(case_learner).json()
    account = case_learner.post("/api/v1/auth/register", json={
        "email": "case-learner@example.org", "password": "long-unique-case-password",
    })
    assert account.status_code in {200, 201}
    case_learner.headers["X-CSRF-Token"] = case_learner.get("/api/v1/auth/session").json()["csrf_token"]
    exported = case_learner.get("/api/v1/learner/export").json()
    assert exported["case_drafts"] == [first]
    assert case_learner.delete("/api/v1/learner").status_code == 204
    with app.state.sessions() as db:
        assert list(db.scalars(select(CaseDraft))) == []


@pytest.mark.parametrize("mutation", ["graded", "points", "duplicate"])
def test_case_studio_rejects_graded_or_ambiguous_content(client, case_source, mutation):
    source = json.loads(case_source.read_text())
    case = source["cases"][0]
    if mutation == "graded":
        case["mode"] = "graded"
    elif mutation == "points":
        case["rubric"][0]["points"] = 10
    else:
        case["rubric"].append(case["rubric"][0])
    case_source.write_text(json.dumps(source))
    assert client.get(COURSE).status_code == 503


def test_all_authored_courses_expose_their_existing_case_studies():
    root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(root)
    courses = repository.catalog()
    assert len(courses) >= 25
    # Courses whose project has a learner route add five milestone self-checks after the preserved case.
    milestone_cases = {
        course_id: 5
        for course_id in (
            "cell-biology", "biochemistry", "genetics", "calculus-1", "physics-mechanics", "statics-materials",
            "general-chemistry-2", "programming", "biomaterials", "bioreactors",
            "cellular-biomechanics", "transport", "calculus-2", "calculus-3",
        )
    }
    for summary in courses:
        course = repository.course(summary.id)
        assert len(course.case_studies) == 1 + milestone_cases.get(summary.id, 0)
        assert len(course.case_studies[0].criteria) >= 3
        assert all(case.mode == "self-assessment" for case in course.case_studies)
