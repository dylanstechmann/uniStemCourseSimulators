"""Regression checks for synthetic Genetics linkage and recombination examples."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/genetics"


def test_testcross_recombination_estimates_preserve_legacy_items():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "genetics-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "synthetic two-locus testcross",
        "Learning objectives",
        "AB/ab",
        "recombination fraction",
        "standard error",
        "double crossovers",
        "0.5",
        "Limits of this lesson",
    ):
        assert phrase.lower() in text.lower()

    observed_fraction = 72 / 400
    sampling_standard_error = math.sqrt(
        observed_fraction * (1 - observed_fraction) / 400
    )
    second_fraction = 12 / 200
    assert observed_fraction == pytest.approx(0.18)
    assert sampling_standard_error == pytest.approx(0.0192, abs=0.0001)
    assert second_fraction * 100 == pytest.approx(6.0)
    assert 0 <= observed_fraction <= 0.5

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["genetics-2:check"]["solution_spec"]["answer"] == 18
    assert questions["genetics-2:map-distance"]["solution_spec"][
        "answer"
    ] == pytest.approx(6.0)
    assert lesson["question_ids"] == [
        "genetics-2:check",
        "genetics-2:map-distance",
    ]
    assert lesson["card_ids"] == ["genetics-1-0", "genetics-1-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in (
        "genetics-2-objective-1",
        "genetics-2-objective-2",
    ):
        assert objectives[objective_id]["course_outcome_ids"] == [
            "genetics-outcome-2"
        ]
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all compact prototype readings now have expanded instruction" in syllabus
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == "genetics-2-practice"
    )
    assert "genetics-outcome-2" in assessment["objective_ids"]
