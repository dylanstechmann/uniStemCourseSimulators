"""Kinematics and Newton-law instruction, keys, and source mapping checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-mechanics"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_kinematics_lesson_maps_objectives_and_preserves_force_keys():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "physics-mechanics-module-1"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "average velocity",
        "net force in that direction",
        "Do not draw the net force as an additional arrow",
        "4.905\\,\\mathrm{m/s^2}",
        "mass cancels",
        "frictionless",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives[lesson["objectives"][0]]["course_outcome_ids"] == [
        "physics-mechanics-outcome-2"
    ]
    assert objectives[lesson["objectives"][1]]["course_outcome_ids"] == [
        "physics-mechanics-outcome-1",
        "physics-mechanics-outcome-2",
        "physics-mechanics-outcome-4",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "physics-mechanics-1-practice"
    )
    assert {
        "physics-mechanics-outcome-1",
        "physics-mechanics-outcome-2",
        "physics-mechanics-outcome-4",
    }.issubset(set(assessment["objective_ids"]))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    cart = items["physics-mechanics-1:check"]
    incline = items["physics-mechanics-1:incline-acceleration"]
    assert cart["prompt"] == (
        "A 3 kg cart experiences a net horizontal force of 12 N. "
        "What is its acceleration in m/s²?"
    )
    assert incline["prompt"] == (
        "A 10 kg block slides without friction down a 30° incline. Calculate its "
        "acceleration along the incline using g = 9.81 m/s². Enter a value and unit."
    )
    assert cart["solution_spec"]["answer"] == pytest.approx(4)
    assert incline["solution_spec"]["answer"] == pytest.approx(4.905)
    assert 12 / 3 == pytest.approx(4)
    assert 9.81 * 0.5 == pytest.approx(4.905)
    assert {cart["id"], incline["id"]} == set(lesson["question_ids"])


def test_kinematics_references_are_link_only_and_mapped():
    expected = {
        "openstax-physics-acceleration",
        "openstax-physics-newton-second-law",
        "openstax-physics-free-body-diagrams",
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
        assert "physics-mechanics-module-1" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "physics-mechanics-module-1"
    )
    assert expected.issubset(set(mapping["source_ids"]))
