"""Free-body-diagram, beam equilibrium, assessment, and source regressions."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statics-materials"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_equilibrium_reading_maps_objectives_and_preserves_reaction_keys():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "statics-materials-module-1"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "ΣFx = 0",
        "ΣFy = 0",
        "ΣMO = 0",
        "can exert horizontal and vertical reaction components but no couple moment",
        "RRy = P a/L",
        "RLy = P(1 − a/L)",
        "statically determinate",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "statics-materials-outcome-1"
        ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "statics-materials-1-practice"
    )
    assert "statics-materials-outcome-1" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    center = items["statics-materials-1:check"]
    off_center = items["statics-materials-1:reaction-force"]
    assert center["prompt"] == (
        "A simply supported beam spans 4 m and carries a 600 N point load at "
        "midspan. What vertical reaction acts at either support?"
    )
    assert off_center["prompt"] == (
        "A simply supported beam 4.0 m long carries a single 200 N downward "
        "load 1.0 m from the left support. Calculate the reaction at the right "
        "support. Enter a value and unit."
    )
    assert center["solution_spec"]["answer"] == pytest.approx(300)
    assert off_center["solution_spec"]["answer"] == pytest.approx(50)
    assert 600 / 2 == pytest.approx(300)
    assert 200 * 1.0 / 4.0 == pytest.approx(50)
    assert {center["id"], off_center["id"]} == set(lesson["question_ids"])


def test_equilibrium_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-statics-equilibrium"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "statics-materials-module-1" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "statics-materials-module-1"
    )
    assert source_id in mapping["source_ids"]
