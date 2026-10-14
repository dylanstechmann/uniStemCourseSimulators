"""Magnetic induction lesson, preserved keys, and source-link checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-em"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_magnetic_induction_reading_maps_to_outcome_and_preserves_keys():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item for item in manifest["modules"] if item["id"] == "physics-em-module-3"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "q(**v** × **B**)",
        "Φᵦ = BA cos θ",
        "ε = −N dΦᵦ/dt",
        "opposes the **change in flux**",
        "closed conducting path",
    ):
        assert concept in text

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "physics-em-outcome-3"
        ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "physics-em-3-practice"
    )
    assert "physics-em-outcome-3" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    first = items["physics-em-3:check"]
    second = items["physics-em-3:faraday-emf"]
    assert first["prompt"] == (
        "A 50-turn coil experiences a flux change of 0.004 Wb per turn in "
        "0.02 s. What is the induced emf magnitude in volts?"
    )
    assert second["prompt"] == (
        "A coil of 50 turns experiences a flux change of 2.0×10⁻³ Wb in "
        "0.10 s, uniformly. Calculate the magnitude of the induced emf. "
        "Enter a value and unit."
    )
    assert first["solution_spec"]["answer"] == pytest.approx(10)
    assert second["solution_spec"]["answer"] == pytest.approx(1)
    assert 50 * 0.004 / 0.02 == pytest.approx(10)
    assert 50 * 2e-3 / 0.10 == pytest.approx(1)
    assert {first["id"], second["id"]} == set(lesson["question_ids"])


def test_magnetic_induction_sources_remain_link_only_and_mapped():
    expected = {
        "openstax-em-particle-magnetic-force",
        "openstax-em-wire-magnetic-force",
        "openstax-em-faraday-law",
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
        assert "physics-em-module-3" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "physics-em-module-3"
    )
    assert expected.issubset(set(mapping["source_ids"]))
