"""Independent field, potential, and capacitor-energy checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-em"


def test_fields_and_capacitors_lesson_maps_outcome_and_preserves_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.4.")
    module = next(
        module
        for module in manifest["modules"]
        if module["id"] == "physics-em-module-1"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "potential difference between points",
        "ΔU = qΔV",
        "parallel plates",
        "C ≈ εA/d",
        "U = ½ Q|ΔV|",
        "fringing",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "physics-em-outcome-1"
        ]
    practice = next(
        assessment
        for assessment in manifest["assessments"]
        if assessment["id"] == "physics-em-1-practice"
    )
    assert "physics-em-outcome-1" in practice["objective_ids"]

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    first = items["physics-em-1:check"]
    second = items["physics-em-1:capacitor-energy"]
    assert first["solution_spec"]["answer"] == pytest.approx(45)
    assert 0.5 * 10 * 3**2 == pytest.approx(45)  # μF·V² = μJ
    assert second["solution_spec"]["answer"] == pytest.approx(1e-4)
    assert 0.5 * (2e-6) * 10**2 == pytest.approx(1e-4)
    assert {first["id"], second["id"]} == {
        "physics-em-1:check",
        "physics-em-1:capacitor-energy",
    }


def test_electrostatics_references_are_link_only_and_mapped_to_the_lesson():
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {source["id"]: source for source in registry["sources"]}
    expected = {
        "openstax-em-potential",
        "openstax-em-capacitance",
        "openstax-em-capacitor-energy",
    }
    module_id = "physics-em-module-1"
    for source_id in expected:
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert module_id in source["mapped_modules"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapping = next(
        item for item in source_map["modules"] if item["module_id"] == module_id
    )
    assert expected.issubset(set(mapping["source_ids"]))

