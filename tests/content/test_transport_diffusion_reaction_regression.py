"""Diffusion-reaction time and flux-direction regression."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/transport"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_diffusion_reaction_reading_and_practice():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(item for item in manifest["modules"] if item["id"] == "transport-module-2")
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "J = −D∇C",
        "tD ≈ L²/D",
        "Da = tD/tR ≈ kL²/D",
        "λ = √(D/k)",
        "Da ≈ 1",
        "100 μm = 1×10⁻⁴ m",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["transport-2-objective-1"]["course_outcome_ids"] == ["transport-outcome-2"]
    assert objectives["transport-2-objective-2"]["course_outcome_ids"] == ["transport-outcome-2", "transport-outcome-4"]
    assessment = next(item for item in manifest["assessments"] if item["id"] == "transport-2-practice")
    assert assessment["points"] == 4
    assert "transport-outcome-2" in assessment["objective_ids"]
    assert "transport-outcome-4" in assessment["objective_ids"]

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    original = items["transport-2:check"]
    diffusion_time = items["transport-2:diffusion-time"]
    flux = items["transport-2:flux-direction"]
    regime = items["transport-2:regime"]
    assert original["prompt"] == "For D=1×10⁻⁹ m²/s and a characteristic length L=100 μm, estimate L²/D in seconds."
    assert original["solution_spec"]["answer"] == pytest.approx(10)
    assert original["objective_ids"] == ["transport-2-objective-2"]
    assert diffusion_time["solution_spec"]["answer"] == pytest.approx(10)
    assert flux["solution_spec"]["answer"] == 1
    assert regime["solution_spec"]["answer"] == 2
    assert set(lesson["question_ids"]) == {original["id"], diffusion_time["id"], flux["id"], regime["id"]}
    assert set(lesson["question_ids"]) == set(assessment["question_ids"])
    length = 200e-6
    td = length**2 / (2e-9)
    tr = 1 / 0.05
    assert td == pytest.approx(20)
    assert tr == pytest.approx(20)
    assert td / tr == pytest.approx(1)
    assert (2e-9 / 0.05) ** 0.5 == pytest.approx(200e-6)


def test_reaction_diffusion_reference_is_link_only_and_mapped():
    source_id = "mit-ocw-transport-reaction-diffusion"
    registry = load(ROOT / "content/sources/registry.json")
    source = next(item for item in registry["sources"] if item["id"] == source_id)
    assert source["reuse_mode"] == "link-only-reference"
    assert source["permissions"] == {
        "linking": True,
        "quotation": False,
        "adaptation": False,
        "redistribution": False,
    }
    assert "transport-module-2" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(item for item in source_map["modules"] if item["module_id"] == "transport-module-2")
    assert source_id in mapping["source_ids"]
    assert mapping["original_content"] is True
