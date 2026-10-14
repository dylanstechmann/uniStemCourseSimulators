"""Independent potential and free-energy checks for General Chemistry II."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-2"


def test_electrochem_lesson_maps_outcomes_and_preserves_legacy_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.4.")
    module = next(
        module
        for module in manifest["modules"]
        if module["id"] == "general-chemistry-2-module-3"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "salt bridge",
        "E°cell = E°cathode − E°anode",
        "ΔG° = −nFE°cell",
        "intensive quantity",
        "Nernst",
        "E°′",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "general-chemistry-2-outcome-3"
        ]
    practice = next(
        assessment
        for assessment in manifest["assessments"]
        if assessment["id"] == "general-chemistry-2-3-practice"
    )
    assert "general-chemistry-2-outcome-3" in practice["objective_ids"]

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    free_energy = items["general-chemistry-2-3:check"]
    cell_potential = items["general-chemistry-2-3:cell-potential"]
    assert free_energy["solution_spec"]["answer"] == pytest.approx(-57.9)
    assert -(2 * 96_485 * 0.30) / 1_000 == pytest.approx(-57.9, abs=0.01)
    assert cell_potential["solution_spec"]["answer"] == pytest.approx(1.10)
    assert 0.34 - (-0.76) == pytest.approx(1.10)
    assert {free_energy["id"], cell_potential["id"]} == {
        "general-chemistry-2-3:check",
        "general-chemistry-2-3:cell-potential",
    }


def test_electrochem_references_are_link_only_and_mapped_to_the_lesson():
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {source["id"]: source for source in registry["sources"]}
    expected = {
        "openstax-chem2-galvanic-cells",
        "openstax-chem2-electrode-cell-potentials",
        "openstax-chem2-potential-free-energy-equilibrium",
    }
    module_id = "general-chemistry-2-module-3"
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

