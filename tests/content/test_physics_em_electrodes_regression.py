"""Electrode-interface instruction, loading arithmetic, and provenance checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-em"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_electrode_reading_maps_outcome_and_preserves_practice_keys():
    manifest = load(COURSE / "course.json")
    assert manifest["version"] == manifest["history"][-1]["version"]
    module = next(
        item for item in manifest["modules"] if item["id"] == "physics-em-module-4"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "voltage-divider loading",
        "half-cell potential",
        "double-layer capacitance",
        "finite common-mode rejection",
        "does not prove that the tissue is unchanged",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "physics-em-outcome-4"
        ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "physics-em-4-practice"
    )
    assert "physics-em-outcome-4" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    divider = items["physics-em-4:check"]
    drift = items["physics-em-4:electrode-polarization"]
    assert divider["prompt"] == (
        "A 1 MΩ source drives a 9 MΩ input through a simple divider. "
        "What fraction of source voltage appears at the input?"
    )
    assert divider["solution_spec"]["answer"] == pytest.approx(0.9)
    assert 9 / (1 + 9) == pytest.approx(0.9)
    assert drift["solution_spec"]["answer"] == 2
    assert drift["options"][2] == (
        "Electrode half-cell polarization and settling, not tissue signal."
    )
    assert {divider["id"], drift["id"]} == set(lesson["question_ids"])


def test_electrode_references_are_link_only_and_mapped():
    expected = {
        "openstax-em-simple-ac",
        "pubmed-electrode-interface-models",
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
        assert "physics-em-module-4" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "physics-em-module-4"
    )
    assert expected.issubset(set(mapping["source_ids"]))
