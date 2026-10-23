"""Feedback-sign, margin, assessment-key, and source regressions."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/signals-control"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_feedback_reading_maps_objectives_and_preserves_loop_items():
    manifest = load(COURSE / "course.json")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "signals-control-module-3"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "the error **e = r − y**",
        "G/(1 + G)",
        "closed-loop characteristic factor",
        "S = 1/(1 + G)",
        "measurement noise is injected",
        "GM = 1/0.4 = 2.5",
        "robustness asks whether stability or performance persists",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives[lesson["objectives"][0]]["course_outcome_ids"] == [
        "signals-control-outcome-1",
        "signals-control-outcome-3",
    ]
    assert objectives[lesson["objectives"][1]]["course_outcome_ids"] == [
        "signals-control-outcome-3",
        "signals-control-outcome-4",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "signals-control-3-practice"
    )
    assert {
        "signals-control-outcome-1",
        "signals-control-outcome-3",
        "signals-control-outcome-4",
    }.issubset(set(assessment["objective_ids"]))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    closed_loop = items["signals-control-3:check"]
    margin = items["signals-control-3:gain-margin"]
    assert closed_loop["prompt"] == (
        "In negative unity feedback, what is the closed-loop transfer function "
        "from reference to output?"
    )
    assert closed_loop["options"][closed_loop["solution_spec"]["answer"]] == "G/(1+G)"
    assert margin["prompt"] == (
        "At the phase-crossover frequency, a loop's magnitude is |L| = 0.4. "
        "What is the gain margin as a linear factor? Enter a number."
    )
    assert margin["solution_spec"]["answer"] == pytest.approx(2.5)
    assert 1 / 0.4 == pytest.approx(2.5)
    assert {closed_loop["id"], margin["id"]} == set(lesson["question_ids"])


def test_feedback_references_are_link_only_and_mapped():
    expected = {"mit-ocw-feedback-analysis", "mit-ocw-gain-phase-margins"}
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
        assert "signals-control-module-3" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "signals-control-module-3"
    )
    assert expected.issubset(set(mapping["source_ids"]))
