"""Week-one LTI, transfer-function, assessment, and reference regressions."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/signals-control"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_lti_reading_maps_objectives_and_preserves_pole_and_gain_items():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "signals-control-module-1"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "linearity and time invariance are separate properties",
        "zero-state input–output behavior",
        "G(s) = 6/(s + 2)",
        "the pole is **s = −2**",
        "G(0) = 6/(0 + 2) = 3",
        "initial value contributes a zero-input response",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    expected_outcomes = [
        "signals-control-outcome-1",
        "signals-control-outcome-2",
    ]
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == expected_outcomes
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "signals-control-1-practice"
    )
    assert set(expected_outcomes).issubset(set(assessment["objective_ids"]))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    pole = items["signals-control-1:check"]
    gain = items["signals-control-1:dc-gain"]
    assert pole["prompt"] == "For G(s)=1/(s+4), where is the pole?"
    assert pole["options"][pole["solution_spec"]["answer"]] == "s=−4"
    assert gain["prompt"] == (
        "A first-order system obeys dy/dt + 2y = 6u. What is its steady-state "
        "(DC) gain y/u? Enter a number."
    )
    assert gain["solution_spec"]["answer"] == pytest.approx(3)
    assert 6 / 2 == pytest.approx(3)
    assert {pole["id"], gain["id"]} == set(lesson["question_ids"])


def test_lti_references_are_link_only_and_mapped():
    expected = {
        "mit-ocw-signals-convolution",
        "mit-ocw-signals-laplace-transform",
    }
    registry = load(ROOT / "content/sources/registry.json")
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in expected:
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "signals-control-module-1" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "signals-control-module-1"
    )
    assert expected.issubset(set(mapping["source_ids"]))
