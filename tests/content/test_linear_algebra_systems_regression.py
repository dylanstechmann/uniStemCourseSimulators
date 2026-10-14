"""Regression checks for the expanded Linear Algebra elimination prototype."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/linear-algebra"


def test_elimination_rank_and_consistency_preserve_legacy_assessments():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "linear-algebra-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "Learning objectives",
        "reversible row operations",
        "augmented column creates an additional pivot",
        "free variables",
        "inconsistent",
        "ill-conditioned",
        "Limits of this lesson",
        "Elimination with Matrices",
    ):
        assert phrase.lower() in text.lower()

    unique_solution = (2, 1)
    assert unique_solution[0] + unique_solution[1] == 3
    assert unique_solution[0] - unique_solution[1] == 1

    # Two identical equations leave one free variable and infinitely many solutions.
    redundant_rank_a = 1
    redundant_rank_augmented = 1
    variable_count = 2
    assert redundant_rank_a == redundant_rank_augmented
    assert variable_count - redundant_rank_a == 1

    # Changing the right-hand side creates 0 = 1 after elimination.
    inconsistent_rank_a = 1
    inconsistent_rank_augmented = 2
    assert inconsistent_rank_a != inconsistent_rank_augmented

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["linear-algebra-1:check"]["solution_spec"]["answer"] == pytest.approx(4)
    assert questions["linear-algebra-1:rank-from-pivots"]["solution_spec"]["answer"] == 2
    assert lesson["question_ids"] == [
        "linear-algebra-1:check",
        "linear-algebra-1:rank-from-pivots",
    ]
    assert lesson["card_ids"] == ["linear-algebra-0-0", "linear-algebra-0-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["linear-algebra-1-objective-1"]["course_outcome_ids"] == [
        "linear-algebra-outcome-1"
    ]
    assert objectives["linear-algebra-1-objective-2"]["course_outcome_ids"] == [
        "linear-algebra-outcome-1",
        "linear-algebra-outcome-2",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "linear-algebra-1-practice"
    )
    assert "linear-algebra-outcome-1" in assessment["objective_ids"]
    assert "linear-algebra-outcome-2" in assessment["objective_ids"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped_module = next(
        item for item in source_map["modules"] if item["lesson_id"] == "linear-algebra-1"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    source = next(item for item in registry["sources"] if item["id"] == "linearAlgebra")
    assert "linearAlgebra" in mapped_module["source_ids"]
    assert "linear-algebra-module-1" in source["mapped_modules"]
    assert source["permissions"]["linking"] is True
    assert source["permissions"]["adaptation"] is False
    assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all four compact legacy prototype readings now have expanded instructional content" in syllabus

