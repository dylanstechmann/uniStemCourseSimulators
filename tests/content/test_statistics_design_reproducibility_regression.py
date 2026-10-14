"""Experimental design, replication and regression-reading regression."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statistics"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_design_reading_objectives_and_preserved_practice():
    manifest = load(COURSE / "course.json")
    assert manifest["version"] == manifest["history"][-1]["version"]
    module = next(item for item in manifest["modules"] if item["id"] == "statistics-module-4")
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "smallest unit independently assigned",
        "Randomize at the level where the intervention is assigned.",
        "three to each condition at random within every day",
        "residual-versus-fitted plot",
        "24 experimental units",
        "cannot separate their effects",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["statistics-4-objective-1"]["course_outcome_ids"] == ["statistics-outcome-4"]
    assert objectives["statistics-4-objective-2"]["course_outcome_ids"] == ["statistics-outcome-1", "statistics-outcome-2", "statistics-outcome-4"]
    assessment = next(item for item in manifest["assessments"] if item["id"] == "statistics-4-practice")
    assert assessment["points"] == 3
    assert all(outcome in assessment["objective_ids"] for outcome in ("statistics-outcome-1", "statistics-outcome-2", "statistics-outcome-4"))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    sample_size = items["statistics-4:check"]
    pseudorep = items["statistics-4:pseudoreplication"]
    blocking = items["statistics-4:randomization-blocking"]
    assert sample_size["prompt"] == "A study measures 100 cells from each of 4 animals per group. What is the primary biological sample size per group?"
    assert sample_size["solution_spec"]["answer"] == 2
    assert sample_size["objective_ids"] == ["statistics-4-objective-2"]
    assert pseudorep["solution_spec"]["answer"] == 0
    assert blocking["solution_spec"]["answer"] == 1
    assert set(lesson["question_ids"]) == {sample_size["id"], pseudorep["id"], blocking["id"]}
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])


def test_design_references_are_link_only_and_mapped():
    source_ids = {"mit-ocw-statistics-regression", "plos-statistics-experimental-unit"}
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
        assert "statistics-module-4" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(item for item in source_map["modules"] if item["module_id"] == "statistics-module-4")
    assert source_ids.issubset(set(mapping["source_ids"]))
    assert mapping["original_content"] is True
