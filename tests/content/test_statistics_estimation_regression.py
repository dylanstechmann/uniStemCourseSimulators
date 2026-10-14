"""Confidence-interval interpretation and estimation lesson regression."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statistics"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_estimation_reading_objectives_and_preserved_practice():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(item for item in manifest["modules"] if item["id"] == "statistics-module-2")
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "repeated many times",
        "does not mean there is a 95% probability",
        "2.0/√25 = 0.40 mm",
        "[3.17, 4.83] mm",
        "Precision is not accuracy.",
        "regression to the mean",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in ("statistics-2-objective-1", "statistics-2-objective-2"):
        assert objectives[objective_id]["course_outcome_ids"] == ["statistics-outcome-3"]
    assessment = next(item for item in manifest["assessments"] if item["id"] == "statistics-2-practice")
    assert assessment["points"] == 2
    assert "statistics-outcome-3" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    coverage = items["statistics-2:check"]
    magnitude = items["statistics-2:magnitude-vs-precision"]
    assert coverage["prompt"] == "A 95% confidence interval for a mean difference is [1, 5]. Which interpretation is best?"
    assert coverage["solution_spec"]["answer"] == 1
    assert magnitude["solution_spec"]["answer"] == 0
    assert set(lesson["question_ids"]) == {coverage["id"], magnitude["id"]}
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])
    assert 4.0 - 2.064 * (2.0 / 25**0.5) == pytest.approx(3.1744)
    assert 4.0 + 2.064 * (2.0 / 25**0.5) == pytest.approx(4.8256)


def test_confidence_interval_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-statistics-confidence"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "statistics-module-2" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(item for item in source_map["modules"] if item["module_id"] == "statistics-module-2")
    assert source_id in mapping["source_ids"]
    assert mapping["original_content"] is True
