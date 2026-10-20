"""Independent checks for the week-5 kinetics and mechanism lesson."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-2"


def test_kinetics_lesson_maps_outcomes_and_preserves_legacy_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert tuple(int(part) for part in manifest["version"].split(".")) >= (0, 4, 0)
    module = next(
        module
        for module in manifest["modules"]
        if module["id"] == "general-chemistry-2-module-2"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "initial-rate comparisons",
        "empirical model",
        "kelvin",
        "elementary step",
        "catalyst",
        "ln 2/k",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "general-chemistry-2-outcome-2"
        ]
    practice = next(
        assessment
        for assessment in manifest["assessments"]
        if assessment["id"] == "general-chemistry-2-2-practice"
    )
    assert "general-chemistry-2-outcome-2" in practice["objective_ids"]

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    half_life = items["general-chemistry-2-2:check"]
    assert half_life["solution_spec"]["answer"] == pytest.approx(1.98)
    assert math.log(2) / 0.35 == pytest.approx(1.98, abs=0.01)
    ratio = math.exp((50_000 / 8.314) * (1 / 298 - 1 / 308))
    arrhenius = items["general-chemistry-2-2:arrhenius-ratio"]
    assert ratio == pytest.approx(1.93, abs=0.01)
    assert arrhenius["solution_spec"]["answer"] == pytest.approx(1.93)
    assert arrhenius["solution_spec"]["tolerance"] >= abs(
        ratio - arrhenius["solution_spec"]["answer"]
    )
    assert {item["id"] for item in items.values() if item["id"].startswith("general-chemistry-2-2:")} == {
        "general-chemistry-2-2:check",
        "general-chemistry-2-2:arrhenius-ratio",
    }


def test_kinetics_references_are_link_only_and_mapped_to_the_lesson():
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {source["id"]: source for source in registry["sources"]}
    expected = {
        "openstax-chem2-reaction-rates",
        "openstax-chem2-rate-laws",
        "openstax-chem2-integrated-rate-laws",
        "openstax-chem2-collision-theory",
        "openstax-chem2-mechanisms",
    }
    module_id = "general-chemistry-2-module-2"
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

    source_map = json.loads(
        (COURSE / "source-map.json").read_text(encoding="utf-8")
    )
    mapping = next(
        item for item in source_map["modules"] if item["module_id"] == module_id
    )
    assert expected.issubset(set(mapping["source_ids"]))

