"""Failure-criterion distinctions, margins, and aligned practice evidence."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statics-materials"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_failure_reading_and_assessment_mapping():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "statics-materials-module-4"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "onset of permanent deformation",
        "maximum engineering stress",
        "Fatigue concerns damage during repeated or fluctuating loading",
        "Functional failure is defined by a requirement",
        "n = R_capacity/R_demand",
        "factor of safety is not a probability of survival",
        "pre-factored allowable",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "statics-materials-outcome-4"
        ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "statics-materials-4-practice"
    )
    assert assessment["points"] == 4
    assert "statics-materials-outcome-4" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    allowable_ratio = items["statics-materials-4:check"]
    yield_ratio = items["statics-materials-4:factor-of-safety"]
    criteria = items["statics-materials-4:failure-criteria"]
    assert allowable_ratio["prompt"] == (
        "A part has a specified allowable stress of 120 MPa and a calculated "
        "maximum stress of 40 MPa. What is the factor of safety?"
    )
    assert allowable_ratio["solution_spec"]["answer"] == pytest.approx(3)
    assert allowable_ratio["objective_ids"] == ["statics-materials-4-objective-2"]
    assert 120 / 40 == pytest.approx(3)
    assert yield_ratio["solution_spec"]["answer"] == pytest.approx(2.5)
    assert 250 / 100 == pytest.approx(2.5)
    assert criteria["type"] == "multiple_select"
    assert criteria["solution_spec"]["answer"] == [0, 1, 2, 3]
    assert criteria["objective_ids"] == ["statics-materials-4-objective-1"]
    assert set(lesson["question_ids"]) == {
        allowable_ratio["id"],
        yield_ratio["id"],
        criteria["id"],
    }
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])


def test_failure_criteria_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-failure-criteria"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "statics-materials-module-4" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "statics-materials-module-4"
    )
    assert source_id in mapping["source_ids"]
    assert mapping["original_content"] is True

