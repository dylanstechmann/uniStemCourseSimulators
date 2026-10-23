"""Null-hypothesis testing and multiplicity regression."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statistics"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_nhst_reading_and_objective_evidence():
    manifest = load(COURSE / "course.json")
    module = next(item for item in manifest["modules"] if item["id"] == "statistics-module-3")
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "probability of obtaining data at least as incompatible",
        "It does not mean there is a 3% probability that H0 is true.",
        "FWER = 1 − (1 − α)^m.",
        "0.05/20 = 0.0025",
        "Exploration is useful",
        "fail to reject",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["statistics-3-objective-1"]["course_outcome_ids"] == ["statistics-outcome-3"]
    assert objectives["statistics-3-objective-2"]["course_outcome_ids"] == ["statistics-outcome-2", "statistics-outcome-3"]
    assessment = next(item for item in manifest["assessments"] if item["id"] == "statistics-3-practice")
    assert assessment["points"] == 3
    assert "statistics-outcome-2" in assessment["objective_ids"]
    assert "statistics-outcome-3" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    fwer = items["statistics-3:check"]
    bonferroni = items["statistics-3:bonferroni"]
    pvalue = items["statistics-3:p-value-meaning"]
    assert fwer["prompt"] == "For 10 independent null tests each at α=0.05, what is the probability of at least one false positive? Enter percent, rounded to a whole number."
    assert fwer["solution_spec"]["answer"] == pytest.approx(40)
    assert fwer["objective_ids"] == ["statistics-3-objective-2"]
    assert bonferroni["solution_spec"]["answer"] == pytest.approx(0.0025)
    assert pvalue["solution_spec"]["answer"] == 1
    assert pvalue["objective_ids"] == ["statistics-3-objective-1"]
    assert set(lesson["question_ids"]) == {fwer["id"], bonferroni["id"], pvalue["id"]}
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])
    assert 1 - (1 - 0.05) ** 10 == pytest.approx(0.40126306)
    assert 0.05 / 20 == pytest.approx(0.0025)


def test_nhst_references_are_link_only_and_mapped():
    source_ids = {"mit-ocw-statistics-nhst", "mit-ocw-statistics-pset-9"}
    registry = load(ROOT / "content/sources/registry.json")
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in source_ids:
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "statistics-module-3" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(item for item in source_map["modules"] if item["module_id"] == "statistics-module-3")
    assert source_ids.issubset(set(mapping["source_ids"]))
    assert mapping["original_content"] is True
