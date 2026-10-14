"""Outcome and objective alignment checks for the expanded prototype lessons."""

from __future__ import annotations

import json
from pathlib import Path

COURSE = Path(__file__).resolve().parents[2] / "content/courses/biomaterials"


def test_original_objectives_link_to_supported_outcomes_and_practice():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    expected = {
        "biomaterials-1-objective-1": ["biomaterials-outcome-1"],
        "biomaterials-1-objective-2": ["biomaterials-outcome-1"],
        "biomaterials-2-objective-1": ["biomaterials-outcome-2"],
        "biomaterials-2-objective-2": ["biomaterials-outcome-2"],
        "biomaterials-3-objective-1": ["biomaterials-outcome-3"],
        "biomaterials-3-objective-2": ["biomaterials-outcome-3", "biomaterials-outcome-4"],
        "biomaterials-4-objective-1": ["biomaterials-outcome-1"],
        "biomaterials-4-objective-2": ["biomaterials-outcome-4"],
    }
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id, outcome_ids in expected.items():
        assert objectives[objective_id]["course_outcome_ids"] == outcome_ids

    outcome4 = next(item for item in manifest["outcomes"] if item["id"] == "biomaterials-outcome-4")
    assert "failure modes" in outcome4["description"]
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["biomaterials-2:check"]["objective_ids"] == ["biomaterials-2-objective-2"]
    assert questions["biomaterials-3:check"]["objective_ids"] == ["biomaterials-3-objective-2"]
    architecture = questions["biomaterials-2:architecture-tradeoff"]
    cell_sources = questions["biomaterials-3:cell-source-tradeoffs"]
    assert architecture["solution_spec"]["answer"] == 1
    assert architecture["objective_ids"] == ["biomaterials-2-objective-1"]
    assert cell_sources["solution_spec"]["answer"] == 0
    assert cell_sources["objective_ids"] == ["biomaterials-3-objective-1"]

    for lesson_number, outcome_ids in (
        (1, ["biomaterials-outcome-1"]),
        (2, ["biomaterials-outcome-2"]),
        (3, ["biomaterials-outcome-3", "biomaterials-outcome-4"]),
        (4, ["biomaterials-outcome-1", "biomaterials-outcome-4"]),
    ):
        lesson_id = f"biomaterials-{lesson_number}"
        lesson = next(
            lesson
            for module in manifest["modules"]
            for lesson in module["lessons"]
            if lesson["id"] == lesson_id
        )
        assessment = next(
            item for item in manifest["assessments"]
            if item["id"] == f"{lesson_id}-practice"
        )
        assert set(outcome_ids).issubset(assessment["objective_ids"])
        assert set(lesson["question_ids"]) == set(assessment["question_ids"])
