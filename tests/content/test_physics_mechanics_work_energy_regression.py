"""Work, energy and power instruction, keys, and source mapping checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-mechanics"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_work_energy_reading_maps_objectives_and_preserves_keys():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "physics-mechanics-module-2"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "work–energy theorem",
        "net work",
        "conservative",
        "dissipated",
        "mechanical-energy difference",
        "Power has units joules per second",
        "Total energy is not destroyed",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives[lesson["objectives"][0]]["course_outcome_ids"] == [
        "physics-mechanics-outcome-2"
    ]
    assert objectives[lesson["objectives"][1]]["course_outcome_ids"] == [
        "physics-mechanics-outcome-2",
        "physics-mechanics-outcome-4",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "physics-mechanics-2-practice"
    )
    assert {
        "physics-mechanics-outcome-2",
        "physics-mechanics-outcome-4",
    }.issubset(set(assessment["objective_ids"]))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    kinetic = items["physics-mechanics-2:check"]
    energy_gap = items["physics-mechanics-2:dissipated-energy"]
    assert kinetic["prompt"] == (
        "A 2 kg object moving at 3 m/s has what kinetic energy in joules?"
    )
    assert energy_gap["prompt"] == (
        "A 2.0 kg object is dropped from 5.0 m and hits the floor at 8.0 m/s. "
        "Using g = 9.81 m/s², how much mechanical energy was dissipated? "
        "Enter a value and unit."
    )
    assert kinetic["solution_spec"]["answer"] == pytest.approx(9)
    assert energy_gap["solution_spec"]["answer"] == pytest.approx(34.1)
    assert 0.5 * 2 * 3**2 == pytest.approx(9)
    assert 2 * 9.81 * 5 - 0.5 * 2 * 8**2 == pytest.approx(34.1)
    assert {kinetic["id"], energy_gap["id"]} == set(lesson["question_ids"])


def test_work_energy_references_are_link_only_and_mapped():
    expected = {
        "openstax-physics-kinetic-energy",
        "openstax-physics-work-energy-theorem",
        "openstax-physics-power",
        "openstax-physics-conservative-forces",
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
        assert "physics-mechanics-module-2" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "physics-mechanics-module-2"
    )
    assert expected.issubset(set(mapping["source_ids"]))
