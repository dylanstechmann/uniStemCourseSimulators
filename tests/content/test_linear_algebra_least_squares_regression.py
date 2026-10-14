"""Regression checks for the expanded Linear Algebra least-squares lesson."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/linear-algebra"


def test_least_squares_derivation_and_residuals_preserve_legacy_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "linear-algebra-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "Learning objectives",
        "normal equations",
        "full column rank",
        "residual is orthogonal",
        "residual sum of squares",
        "conditioning problems",
        "cannot establish causality",
        "Limits of this lesson",
        "Projection Matrices and Least Squares",
    ):
        assert phrase.lower() in text.lower()

    intercept = 7 / 6
    slope = 1 / 2
    predictions = [intercept + slope * t for t in (0, 1, 2)]
    observed = [1, 2, 2]
    residuals = [y - predicted for y, predicted in zip(observed, predictions)]
    assert predictions == pytest.approx([7 / 6, 5 / 3, 13 / 6])
    assert residuals == pytest.approx([-1 / 6, 1 / 3, -1 / 6])
    assert sum(residuals) == pytest.approx(0)
    assert sum(t * residual for t, residual in zip((0, 1, 2), residuals)) == pytest.approx(0)
    residual_sum_squares = sum(residual**2 for residual in residuals)
    assert residual_sum_squares == pytest.approx(1 / 6)

    # Verify the two scalar normal equations for A=[[1,0],[1,1],[1,2]].
    assert 3 * intercept + 3 * slope == pytest.approx(5)
    assert 3 * intercept + 5 * slope == pytest.approx(6)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["linear-algebra-4:check"]["solution_spec"]["answer"] == pytest.approx(2)
    assert questions["linear-algebra-4:residual-pattern"]["solution_spec"]["answer"] == 0
    assert lesson["question_ids"] == [
        "linear-algebra-4:check",
        "linear-algebra-4:residual-pattern",
    ]
    assert lesson["card_ids"] == ["linear-algebra-3-0", "linear-algebra-3-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in (
        "linear-algebra-4-objective-1",
        "linear-algebra-4-objective-2",
    ):
        assert objectives[objective_id]["course_outcome_ids"] == [
            "linear-algebra-outcome-4"
        ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "linear-algebra-4-practice"
    )
    assert "linear-algebra-outcome-4" in assessment["objective_ids"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped_module = next(
        item for item in source_map["modules"] if item["lesson_id"] == "linear-algebra-4"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    source = next(item for item in registry["sources"] if item["id"] == "linearAlgebra")
    assert "linearAlgebra" in mapped_module["source_ids"]
    assert "linear-algebra-module-4" in source["mapped_modules"]
    assert source["permissions"]["linking"] is True
    assert source["permissions"]["adaptation"] is False
    assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all four compact legacy prototype readings now have expanded instructional content" in syllabus

