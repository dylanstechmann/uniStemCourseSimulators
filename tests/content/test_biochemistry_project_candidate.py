"""Keep the integrated protein-state project inactive and human-scored."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
PACKET = COURSE / "assessment-specs/protein-state-binding-project-candidate.json"
SPEC = importlib.util.spec_from_file_location(
    "assessment_candidates", ROOT / "tools/assessment_candidates.py"
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


def test_project_is_mapped_human_review_candidate_without_public_solution():
    candidate = json.loads(PACKET.read_text(encoding="utf-8"))
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    known_objectives = {item["id"] for item in manifest["lesson_objectives"]}
    project = (COURSE / candidate["instruction_path"]).read_text(encoding="utf-8")
    rubric = (COURSE / candidate["human_portfolio_path"]).read_text(encoding="utf-8")

    assert manifest["version"] == manifest["history"][-1]["version"]
    # The candidate stays bound to the released version it was drafted against.
    assert candidate["content_version"] == "0.4.85"
    assert candidate["content_version"] in {entry["version"] for entry in manifest["history"]}
    assert candidate["assessment_kind"] == "human-portfolio"
    assert candidate["state"] == "inactive-review-candidate"
    assert candidate["review"] == {"status": "unreviewed", "reviewers": []}
    assert candidate["candidate_id"] not in {
        item["id"] for item in manifest["assessments"]
    }
    assert candidate["points"] == 100
    assert len(candidate["questions"]) == 5
    assert sum(item["points"] for item in candidate["questions"]) == 100
    assert set(candidate["objective_ids"]) <= known_objectives
    assert candidate["objective_ids"] == list(
        dict.fromkeys(
            objective
            for item in candidate["questions"]
            for objective in item["learning_objective_ids"]
        )
    )
    assert AUDIT.FORBIDDEN.isdisjoint(AUDIT.keys(candidate["questions"]))
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "Author calculation key" not in project
    assert "33.8806533555" not in project
    assert "anchor from 0–4" in rubric
    assert "not an automatic grader" in project

    report = AUDIT.audit(ROOT)
    biochemistry = next(
        package for package in report["packages"] if package["course"] == "biochemistry"
    )
    assert len(biochemistry["candidates"]) == 11
    rendered = AUDIT.render(report)
    assert "100 proposed human-review points" in rendered
    assert "private_answer_sources_read" not in rendered
