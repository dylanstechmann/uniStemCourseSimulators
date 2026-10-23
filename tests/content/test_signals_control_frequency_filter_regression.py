"""Frequency-response, aliasing, preserved assessment, and source regressions."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/signals-control"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_frequency_filter_reading_maps_objectives_and_preserves_keys():
    manifest = load(COURSE / "course.json")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "signals-control-module-2"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "G(jω) = 1/(1 + jωτ)",
        "fc = 1/(2πτ)",
        "phase of **−45°**",
        "must act on the analog signal before the sampler",
        "|120 − 200| = 80 Hz",
        "cannot determine whether that component came from a genuine 80 Hz",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives[lesson["objectives"][0]]["course_outcome_ids"] == [
        "signals-control-outcome-2"
    ]
    assert objectives[lesson["objectives"][1]]["course_outcome_ids"] == [
        "signals-control-outcome-2",
        "signals-control-outcome-4",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "signals-control-2-practice"
    )
    assert {
        "signals-control-outcome-2",
        "signals-control-outcome-4",
    }.issubset(set(assessment["objective_ids"]))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    cutoff = items["signals-control-2:check"]
    alias = items["signals-control-2:aliased-frequency"]
    assert cutoff["prompt"] == (
        "A first-order low-pass has τ=0.05 s. Estimate its cutoff frequency in Hz."
    )
    assert alias["prompt"] == (
        "A 120 Hz interference tone is sampled at 200 Hz with no anti-alias filter. "
        "At what apparent frequency does it appear in the sampled data? Enter a value and unit."
    )
    assert cutoff["solution_spec"]["answer"] == pytest.approx(3.18)
    assert alias["solution_spec"]["answer"] == pytest.approx(80)
    assert 1 / (2 * 3.141592653589793 * 0.05) == pytest.approx(3.1831, abs=0.001)
    assert abs(120 - 200) == pytest.approx(80)
    assert {cutoff["id"], alias["id"]} == set(lesson["question_ids"])


def test_frequency_response_and_sampling_sources_are_link_only_and_mapped():
    expected = {
        "mit-ocw-signals-frequency-response",
        "mit-ocw-signals-sampling",
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
        assert "signals-control-module-2" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "signals-control-module-2"
    )
    assert expected.issubset(set(mapping["source_ids"]))
