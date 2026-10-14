"""Torsion/bending mechanics, practice mappings, and source checks."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statics-materials"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_torsion_and_bending_reading_and_formative_calculations():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "statics-materials-module-3"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "τ(r) = Tr/J",
        "J = πd⁴/32",
        "J = π(dₒ⁴ − dᵢ⁴)/32",
        "τ_max = 16T/(πd³)",
        "σₓ(y) = −My/I",
        "I = bh³/12",
        "local stress",
        "linear and elastic",
        "material axes",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["statics-materials-3-objective-1"]["course_outcome_ids"] == [
        "statics-materials-outcome-2",
        "statics-materials-outcome-3",
    ]
    assert objectives["statics-materials-3-objective-2"]["course_outcome_ids"] == [
        "statics-materials-outcome-2",
        "statics-materials-outcome-3",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "statics-materials-3-practice"
    )
    assert assessment["points"] == 3
    assert "statics-materials-outcome-2" in assessment["objective_ids"]
    assert "statics-materials-outcome-3" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    bending_location = items["statics-materials-3:check"]
    bending_stress = items["statics-materials-3:bending-stress"]
    torsion_stress = items["statics-materials-3:torsion-stress"]
    assert bending_location["prompt"] == (
        "In elementary beam bending, where is the magnitude of normal stress greatest?"
    )
    assert bending_location["solution_spec"]["answer"] == 1
    assert bending_location["objective_ids"] == ["statics-materials-3-objective-2"]
    assert bending_stress["prompt"] == (
        "A rectangular beam section (width 0.050 m, depth 0.100 m) carries a bending "
        "moment of 500 N·m. Calculate the maximum bending stress σ = M c / I. "
        "Enter a value and unit."
    )
    assert bending_stress["solution_spec"]["answer"] == pytest.approx(6.0)
    assert 500 * 0.050 / (0.050 * 0.100**3 / 12) / 1_000_000 == pytest.approx(6.0)
    assert torsion_stress["solution_spec"]["answer"] == pytest.approx(6.37)
    assert 16 * 10_000 / (math.pi * 20**3) == pytest.approx(6.3662, abs=0.0001)
    assert set(lesson["question_ids"]) == {
        bending_location["id"],
        bending_stress["id"],
        torsion_stress["id"],
    }


def test_torsion_bending_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-torsion-bending"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "statics-materials-module-3" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "statics-materials-module-3"
    )
    assert source_id in mapping["source_ids"]
    assert mapping["original_content"] is True

