"""Every existing plan offers a scheduled, ungraded route through its project."""

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
MANIFESTS = sorted((ROOT / "content/courses").glob("*/course.json"))


@pytest.mark.parametrize("path", MANIFESTS, ids=lambda path: path.parent.name)
def test_existing_plan_has_usable_project_and_current_index(path):
    manifest = json.loads(path.read_text(encoding="utf-8"))
    assert len(MANIFESTS) == 26
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    projects = [a for a in manifest["assessments"] if a["type"] == "project"]
    assert len(projects) == 1
    project = projects[0]
    assert (project["mode"], project["points"], project["question_ids"]) == ("self-assessment", 0, [])
    lessons = [lesson for module in manifest["modules"] for lesson in module["lessons"]]
    guides = [lesson for lesson in lessons if "project" in lesson["id"] and lesson["reading"].startswith("assignments/")]
    assert len(guides) == 1
    guide = guides[0]
    assert (path.parent / guide["reading"]).is_file()
    assert guide["question_ids"]
    weeks = manifest["duration"]["weeks"]
    assert any(guide["id"] in week["lesson_ids"] for week in weeks)
    assert any(project["id"] in week["assessment_ids"] for week in weeks)
    rehearsals = [a for a in manifest["assessments"] if a["mode"] == "practice"
                  and set(guide["question_ids"]) <= set(a["question_ids"])]
    assert rehearsals
    assert any(a["id"] in week["assessment_ids"] for a in rehearsals for week in weeks)
    cases = json.loads((path.parent / manifest["case_rubrics"]).read_text(encoding="utf-8"))["cases"]
    milestones = [case for case in cases if ":project-m" in case["id"]]
    assert len(milestones) >= 5
    assert all(case["mode"] == "self-assessment" for case in milestones)
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    index = (ROOT / "docs/COURSE_PLAN_COMPLETION.md").read_text(encoding="utf-8")
    row = next(line for line in index.splitlines() if f"/courses/{manifest['id']}/syllabus.md)" in line)
    assert f"| {manifest['version']} | {len(weeks)} |" in row
    assert f"../content/courses/{manifest['id']}/{guide['reading']}" in row
