"""Control-volume mass, species and energy-balance regression."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/transport"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_control_volume_reading_objectives_and_preserved_practice():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(item for item in manifest["modules"] if item["id"] == "transport-module-1")
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "accumulation of A = A in − A out + generation of A − consumption of A",
        "Steady state means that the stored quantity does not change with time",
        "V dC/dt = Q(Cᵢₙ − C)",
        "dEcv/dt = Q̇ − Ẇ",
        "2.5 g/L",
        "10 kJ/s = 10 kW",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in ("transport-1-objective-1", "transport-1-objective-2"):
        assert objectives[objective_id]["course_outcome_ids"] == ["transport-outcome-1"]
    assessment = next(item for item in manifest["assessments"] if item["id"] == "transport-1-practice")
    assert assessment["points"] == 3
    assert assessment["objective_ids"][-1] == "transport-outcome-1"

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    steady = items["transport-1:check"]
    accumulation = items["transport-1:accumulation-rate"]
    energy = items["transport-1:energy-balance"]
    assert steady["prompt"] == "A reactor receives 2 L/min at 5 g/L and exits at the same flow. There is no reaction. At steady state, what is the outlet concentration in g/L?"
    assert steady["solution_spec"]["answer"] == pytest.approx(5)
    assert accumulation["solution_spec"]["answer"] == pytest.approx(0.5)
    assert energy["solution_spec"]["answer"] == pytest.approx(10)
    assert energy["solution_spec"]["unit"] == "kW"
    assert energy["solution_spec"]["unit_required"] is True
    assert set(lesson["question_ids"]) == {steady["id"], accumulation["id"], energy["id"]}
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])
    assert 1 * (110 - 100) == pytest.approx(10)
    assert (2 * 5) / (2 + 0.02 * 100) == pytest.approx(2.5)


def test_control_volume_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-transport-control-volume"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "transport-module-1" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(item for item in source_map["modules"] if item["module_id"] == "transport-module-1")
    assert source_id in mapping["source_ids"]
    assert mapping["original_content"] is True
