"""Regression checks for discrete and continuous eigenmode reasoning."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/linear-algebra"


def test_eigenmodes_and_stability_preserve_legacy_assessments():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "linear-algebra-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "Learning objectives",
        "mode-by-mode",
        "discrete-time",
        "continuous-time",
        "asymptotically stable when every eigenvalue",
        "stationary distribution",
        "Jordan block",
        "local linearization",
        "Limits of this lesson",
        "Differential Equations and",
    ):
        assert phrase.lower() in text.lower()

    discrete_after_three = (0.8**3, 2 * (-0.5) ** 3)
    assert discrete_after_three == pytest.approx((0.512, -0.25))
    continuous_e_fold = math.exp(-2 * 0.5)
    assert continuous_e_fold == pytest.approx(math.exp(-1))
    assert -2 < 0 and -0.5 < 0
    assert 0.8 < 1 and -0.5 > -1
    assert 1.1 > 1  # A discrete mode with this eigenvalue grows.

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["linear-algebra-3:check"]["solution_spec"]["answer"] == 0
    assert questions["linear-algebra-3:mode-by-mode-decay"]["solution_spec"][
        "answer"
    ] == pytest.approx(0.512)
    assert lesson["question_ids"] == [
        "linear-algebra-3:check",
        "linear-algebra-3:mode-by-mode-decay",
    ]
    assert lesson["card_ids"] == ["linear-algebra-2-0", "linear-algebra-2-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    objective = objectives["linear-algebra-3-objective-1"]
    assert objective["description"] == (
        "Interpret eigenvalues in discrete- and continuous-time linear dynamics."
    )
    assert objective["course_outcome_ids"] == ["linear-algebra-outcome-3"]
    assert objectives["linear-algebra-3-objective-2"]["course_outcome_ids"] == [
        "linear-algebra-outcome-3"
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "linear-algebra-3-practice"
    )
    assert "linear-algebra-outcome-3" in assessment["objective_ids"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped_module = next(
        item for item in source_map["modules"] if item["lesson_id"] == "linear-algebra-3"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    source = next(item for item in registry["sources"] if item["id"] == "linearAlgebra")
    assert "linearAlgebra" in mapped_module["source_ids"]
    assert "linear-algebra-module-3" in source["mapped_modules"]
    assert source["permissions"]["linking"] is True
    assert source["permissions"]["adaptation"] is False
    assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all four compact legacy prototype readings now have expanded instructional content" in syllabus

