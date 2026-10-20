"""Axial stress/strain instruction, assessment-key, and provenance checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statics-materials"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_axial_reading_covers_model_and_preserves_practice_items():
    manifest = load(COURSE / "course.json")
    assert tuple(int(part) for part in manifest["version"].split(".")) >= (0, 4, 0)
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "statics-materials-module-2"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "σ_avg = F/A",
        "ε = ΔL/L₀",
        "σ = Eε",
        "ΔL = FL/(AE)",
        "k = AE/L",
        "N/mm² = 1 MPa",
        "boundary conditions",
        "small-strain approximation",
        "viscoelastic",
        "not a design basis",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["statics-materials-2-objective-1"]["course_outcome_ids"] == [
        "statics-materials-outcome-2",
        "statics-materials-outcome-3",
    ]
    assert objectives["statics-materials-2-objective-2"]["course_outcome_ids"] == [
        "statics-materials-outcome-3"
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "statics-materials-2-practice"
    )
    assert "statics-materials-outcome-2" in assessment["objective_ids"]
    assert "statics-materials-outcome-3" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    stress = items["statics-materials-2:check"]
    units = items["statics-materials-2:stress-units"]
    assert stress["prompt"] == (
        "A 50 mm² rod carries 500 N axial tension. What is the average stress in MPa?"
    )
    assert units["prompt"] == (
        "A rod carries an axial force of 1200 N over a cross-section of 30 mm². "
        "Calculate the axial stress. Enter a value and unit."
    )
    assert stress["solution_spec"]["answer"] == pytest.approx(10)
    assert units["solution_spec"]["answer"] == pytest.approx(40)
    assert 500 / 50 == pytest.approx(10)
    assert 1200 / 30 == pytest.approx(40)
    # The axial-compatibility extension adds items alongside the preserved pair.
    assert {stress["id"], units["id"]} <= set(lesson["question_ids"])

    # Independently recompute the preserved bar example using N and mm units.
    modulus_n_per_mm2 = 2_000  # 2 GPa = 2,000 MPa = 2,000 N/mm²
    extension_mm = 20 * 100 / (10 * modulus_n_per_mm2)
    assert extension_mm == pytest.approx(0.1)


def test_axial_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-axial-materials"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "statics-materials-module-2" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "statics-materials-module-2"
    )
    assert source_id in mapping["source_ids"]
    assert mapping["original_content"] is True

