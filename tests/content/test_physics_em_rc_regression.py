"""Independent time-constant and step-response checks for Physics II."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-em"


def test_rc_reading_maps_outcome_and_preserves_legacy_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.4.")
    module = next(
        module
        for module in manifest["modules"]
        if module["id"] == "physics-em-module-2"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "τ = RC",
        "V꜀(t) = Vₛ(1 − e⁻ᵗ⁄τ)",
        "V꜀(t) = V₀e⁻ᵗ⁄τ",
        "ohmic resistor",
        "63%",
        "finite input impedance",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "physics-em-outcome-2"
        ]
    practice = next(
        assessment
        for assessment in manifest["assessments"]
        if assessment["id"] == "physics-em-2-practice"
    )
    assert "physics-em-outcome-2" in practice["objective_ids"]

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    tau_item = items["physics-em-2:check"]
    charging_item = items["physics-em-2:rc-charging"]
    assert tau_item["solution_spec"]["answer"] == pytest.approx(10)
    assert (2e3 * 5e-6) * 1e3 == pytest.approx(10)  # seconds to milliseconds
    assert charging_item["solution_spec"]["answer"] == pytest.approx(4.323)
    assert 5.0 * (1 - math.exp(-2.0)) == pytest.approx(4.323, abs=0.001)
    assert {tau_item["id"], charging_item["id"]} == {
        "physics-em-2:check",
        "physics-em-2:rc-charging",
    }


def test_rc_references_are_link_only_and_mapped_to_the_lesson():
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {source["id"]: source for source in registry["sources"]}
    expected = {
        "openstax-em-resistivity",
        "openstax-em-ohms-law",
        "openstax-em-rc-circuits",
    }
    module_id = "physics-em-module-2"
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

