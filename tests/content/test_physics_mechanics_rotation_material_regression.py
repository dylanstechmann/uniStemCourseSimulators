"""Torque, material-response, preserved assessment, and source regressions."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-mechanics"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_rotation_material_reading_maps_objectives_and_preserves_keys():
    manifest = load(COURSE / "course.json")
    assert tuple(int(part) for part in manifest["version"].split(".")) >= (0, 4, 0)
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "physics-mechanics-module-4"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "perpendicular distance from the axis",
        "τz = rx Fy − ry Fx",
        "add the signed values",
        "engineering tensile stress",
        "strain is a ratio of lengths and is dimensionless",
        "2.5 × 10⁻³",
        "does not establish isotropy",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives[lesson["objectives"][0]]["course_outcome_ids"] == [
        "physics-mechanics-outcome-3"
    ]
    assert objectives[lesson["objectives"][1]]["course_outcome_ids"] == [
        "physics-mechanics-outcome-4"
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "physics-mechanics-4-practice"
    )
    assert {
        "physics-mechanics-outcome-3",
        "physics-mechanics-outcome-4",
    }.issubset(set(assessment["objective_ids"]))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    torque = items["physics-mechanics-4:check"]
    strain = items["physics-mechanics-4:strain-from-stress"]
    assert torque["prompt"] == (
        "A 30 N force acts perpendicular to a hinge at a 0.20 m moment arm. "
        "What is the torque magnitude in N·m?"
    )
    assert strain["prompt"] == (
        "A rod carries an axial stress of 5.0×10⁶ Pa in a linear elastic "
        "material with E = 2.0×10⁹ Pa. Calculate the strain. Enter a number."
    )
    assert torque["solution_spec"]["answer"] == pytest.approx(6)
    assert strain["solution_spec"]["answer"] == pytest.approx(0.0025)
    assert 30 * 0.20 == pytest.approx(6)
    assert 5.0e6 / 2.0e9 == pytest.approx(0.0025)
    assert {torque["id"], strain["id"]} == set(lesson["question_ids"])


def test_torque_and_stress_references_are_link_only_and_mapped():
    expected = {"openstax-physics-torque", "openstax-physics-stress-strain"}
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
        assert "physics-mechanics-module-4" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "physics-mechanics-module-4"
    )
    assert expected.issubset(set(mapping["source_ids"]))
