"""Regression checks for the synthetic Genetics week-1 probability lesson."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/genetics"


def test_segregation_and_population_probabilities_preserve_legacy_items():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "genetics-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "synthetic pedigree",
        "Learning objectives",
        "Worked example",
        "penetrance",
        "Hardy–Weinberg",
        "Limits of this lesson",
        "not an estimate for a real person",
    ):
        assert phrase.lower() in text.lower()

    unaffected_carrier_probability = (1 / 2) / (3 / 4)
    affected_child_probability = unaffected_carrier_probability * (1 / 4)
    recessive_allele_frequency = math.sqrt(0.04)
    carrier_frequency = 2 * recessive_allele_frequency * (
        1 - recessive_allele_frequency
    )
    assert unaffected_carrier_probability == pytest.approx(2 / 3)
    assert affected_child_probability == pytest.approx(1 / 6)
    assert carrier_frequency == pytest.approx(0.32)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["genetics-1:check"]["solution_spec"]["answer"] == 1
    assert questions["genetics-1:genotype-vs-phenotype-frequency"][
        "solution_spec"
    ]["answer"] == pytest.approx(0.32)
    assert lesson["question_ids"] == [
        "genetics-1:check",
        "genetics-1:genotype-vs-phenotype-frequency",
    ]
    assert lesson["card_ids"] == ["genetics-0-0", "genetics-0-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["genetics-1-objective-1"]["course_outcome_ids"] == [
        "genetics-outcome-1"
    ]
    assert objectives["genetics-1-objective-2"]["course_outcome_ids"] == [
        "genetics-outcome-1"
    ]
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all compact prototype readings now have expanded instruction" in syllabus
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == "genetics-1-practice"
    )
    assert "genetics-outcome-1" in assessment["objective_ids"]
