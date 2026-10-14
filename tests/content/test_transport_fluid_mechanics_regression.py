"""Reynolds and Poiseuille-flow regression."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/transport"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_fluid_mechanics_reading_objectives_and_practice():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(item for item in manifest["modules"] if item["id"] == "transport-module-3")
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "Re = ρ U L / μ = U L / ν",
        "Q = πR⁴ ΔP/(8 μ ℓ)",
        "halving R reduces Q by a factor of 16",
        "not a universal laminar-versus-turbulent switch",
        "velocity profile that no longer changes along the tube axis",
        "microvascular and cell-containing flows",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["transport-3-objective-1"]["course_outcome_ids"] == ["transport-outcome-3", "transport-outcome-4"]
    assert objectives["transport-3-objective-2"]["course_outcome_ids"] == ["transport-outcome-3"]
    assessment = next(item for item in manifest["assessments"] if item["id"] == "transport-3-practice")
    assert assessment["points"] == 3
    assert "transport-outcome-3" in assessment["objective_ids"]
    assert "transport-outcome-4" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    reynolds = items["transport-3:check"]
    poiseuille = items["transport-3:poiseuille-flow"]
    limits = items["transport-3:reynolds-limits"]
    assert reynolds["prompt"] == "A flow has ρ=1000 kg/m³, U=0.02 m/s, L=0.5 mm, and μ=0.001 Pa·s. What is Re?"
    assert reynolds["solution_spec"]["answer"] == pytest.approx(10)
    assert poiseuille["solution_spec"]["answer"] == pytest.approx(2.4543692606170264e-08)
    assert limits["solution_spec"]["answer"] == 1
    assert set(lesson["question_ids"]) == {reynolds["id"], poiseuille["id"], limits["id"]}
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])
    q=3.141592653589793*(5e-4)**4*100/(8*1e-3*0.1)
    assert q == pytest.approx(2.4543692606170264e-8)
    assert 1000*0.001*1e-4/1e-3 == pytest.approx(0.1)


def test_fluid_mechanics_references_are_link_only_and_mapped():
    source_ids = {"mit-ocw-transport-microfluidics", "mit-ocw-transport-reynolds"}
    registry = load(ROOT / "content/sources/registry.json")
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in source_ids:
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "transport-module-3" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(item for item in source_map["modules"] if item["module_id"] == "transport-module-3")
    assert source_ids.issubset(set(mapping["source_ids"]))
    assert mapping["original_content"] is True
