"""Heat-transfer mechanisms, resistance networks, and lumped-model regression."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/transport"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_heat_transfer_reading_objectives_and_preserved_practice():
    manifest = load(COURSE / "course.json")
    assert manifest["version"] == manifest["history"][-1]["version"]
    module = next(item for item in manifest["modules"] if item["id"] == "transport-module-4")
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "q''x = −k dT/dx",
        "Rcond = L/(kA)",
        "Rconv = 1/(hA)",
        "hrad = εσ(Ts+Tsur)(Ts²+Tsur²)",
        "Bi = hLc/k",
        "Fo = αt/Lc²",
        "τ = ρcpV/(hAs)",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["transport-4-objective-1"]["course_outcome_ids"] == ["transport-outcome-4"]
    assert objectives["transport-4-objective-2"]["course_outcome_ids"] == ["transport-outcome-1", "transport-outcome-4"]
    assessment = next(item for item in manifest["assessments"] if item["id"] == "transport-4-practice")
    assert assessment["points"] == 3
    assert {"transport-outcome-1", "transport-outcome-4"}.issubset(assessment["objective_ids"])

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    slab = items["transport-4:check"]
    series = items["transport-4:series-thermal-resistance"]
    modes = items["transport-4:heat-transfer-modes"]
    assert slab["prompt"] == "A slab has thickness 0.02 m, conductivity 0.5 W/(m·K), and area 0.10 m². What is its conductive thermal resistance in K/W?"
    assert slab["solution_spec"]["answer"] == pytest.approx(0.4)
    assert slab["objective_ids"] == ["transport-4-objective-2"]
    assert series["prompt"] == "Heat flows through two thermal resistances in series, 0.20 K/W and 0.30 K/W, under a total temperature difference of 50 K. Calculate the heat flow. Enter a value and unit."
    assert series["solution_spec"]["answer"] == pytest.approx(100)
    assert series["solution_spec"]["unit"] == "W"
    assert modes["solution_spec"]["answer"] == 0
    assert modes["objective_ids"] == ["transport-4-objective-1"]
    assert set(lesson["question_ids"]) == {slab["id"], series["id"], modes["id"]}
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])
    assert 0.020 / (0.50 * 0.10) == pytest.approx(0.40)
    assert 1 / (100 * 0.10) == pytest.approx(0.10)
    assert 50 / (0.40 + 0.10) == pytest.approx(100)
    assert 10 * 0.02 / 0.5 == pytest.approx(0.4)


def test_heat_transfer_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-transport-heat-transfer"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "transport-module-4" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(item for item in source_map["modules"] if item["module_id"] == "transport-module-4")
    assert source_id in mapping["source_ids"]
    assert mapping["original_content"] is True
