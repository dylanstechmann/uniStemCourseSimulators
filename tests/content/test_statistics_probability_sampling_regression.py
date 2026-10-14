"""Conditional probability, sampling distributions, and assessment provenance."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statistics"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_probability_sampling_reading_and_assessment_keys():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item for item in manifest["modules"] if item["id"] == "statistics-module-1"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "P(A | B) = P(A ∩ B) / P(B)",
        "P(A | B) = P(B | A)P(A) / P(B)",
        "90/135 = 2/3 ≈ 0.667",
        "SE(X̄) = σ/√n",
        "estimated SE = s/√n",
        "quadrupling the number of independent observations halves the standard error",
        "measurement accuracy",
        "experimental unit",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["statistics-1-objective-1"]["course_outcome_ids"] == [
        "statistics-outcome-6"
    ]
    assert objectives["statistics-1-objective-2"]["course_outcome_ids"] == [
        "statistics-outcome-1"
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "statistics-1-practice"
    )
    assert assessment["points"] == 3
    assert "statistics-outcome-1" in assessment["objective_ids"]
    assert "statistics-outcome-6" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    se_check = items["statistics-1:check"]
    se_known_sigma = items["statistics-1:standard-error"]
    bayes = items["statistics-1:bayes-positive"]
    assert se_check["prompt"] == (
        "An experiment has sample SD 10 and n=25 independent biological "
        "replicates. What is the standard error?"
    )
    assert se_check["solution_spec"]["answer"] == pytest.approx(2)
    assert se_check["objective_ids"] == ["statistics-1-objective-2"]
    assert se_known_sigma["solution_spec"]["answer"] == pytest.approx(2)
    assert 10 / (25**0.5) == pytest.approx(2)
    assert 12 / (36**0.5) == pytest.approx(2)
    assert bayes["solution_spec"]["answer"] == pytest.approx(0.667)
    posterior = (0.90 * 0.10) / ((0.90 * 0.10) + (0.05 * 0.90))
    assert posterior == pytest.approx(2 / 3)
    assert set(lesson["question_ids"]) == {
        se_check["id"],
        se_known_sigma["id"],
        bayes["id"],
    }
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])


def test_bayes_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-statistics-bayes"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "statistics-module-1" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "statistics-module-1"
    )
    assert source_id in mapping["source_ids"]
    assert mapping["original_content"] is True

