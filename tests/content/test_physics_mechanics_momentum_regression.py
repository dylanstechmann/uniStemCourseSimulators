"""Momentum, collision, impulse, and source mapping regression checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-mechanics"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_momentum_reading_maps_objectives_and_preserves_collision_keys():
    manifest = load(COURSE / "course.json")
    assert tuple(int(part) for part in manifest["version"].split(".")) >= (0, 4, 0)
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "physics-mechanics-module-3"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "Momentum is a vector",
        "external impulse",
        "force–time curve",
        "average force over the 0.020 s pulse is 100 N",
        "kinetic-energy decrease is 1.0 J",
        "does not imply kinetic-energy conservation",
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
        if item["id"] == "physics-mechanics-3-practice"
    )
    assert {
        "physics-mechanics-outcome-2",
        "physics-mechanics-outcome-4",
    }.issubset(set(assessment["objective_ids"]))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    collision = items["physics-mechanics-3:check"]
    pulse = items["physics-mechanics-3:impulse-area"]
    assert collision["prompt"] == (
        "A 0.10 kg cart moving at 5 m/s sticks to a stationary 0.40 kg cart. "
        "What is their shared speed in m/s?"
    )
    assert pulse["prompt"] == (
        "A triangular force pulse rises linearly from 0 to 200 N over 0.020 s "
        "and then stops. Calculate the impulse. Enter a value and unit."
    )
    assert collision["solution_spec"]["answer"] == pytest.approx(1)
    assert pulse["solution_spec"]["answer"] == pytest.approx(2)
    assert (0.10 * 5 + 0.40 * 0) / (0.10 + 0.40) == pytest.approx(1)
    assert 0.5 * 0.020 * 200 == pytest.approx(2)
    assert {collision["id"], pulse["id"]} == set(lesson["question_ids"])


def test_momentum_references_are_link_only_and_mapped():
    expected = {
        "openstax-physics-linear-momentum",
        "openstax-physics-impulse-collisions",
        "openstax-physics-momentum-conservation",
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
        assert "physics-mechanics-module-3" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "physics-mechanics-module-3"
    )
    assert expected.issubset(set(mapping["source_ids"]))
