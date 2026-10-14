"""Concept and key checks for the General Chemistry II coordination primer."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-2"


def test_coordination_primer_maps_outcomes_and_preserves_legacy_choices():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.4.")
    module = next(
        module
        for module in manifest["modules"]
        if module["id"] == "general-chemistry-2-module-4"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "coordination sphere",
        "coordination number counts the donor atoms",
        "tetrahedral or square-planar",
        "Δₒ",
        "protein environment",
        "redox potential",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == [
            "general-chemistry-2-outcome-4"
        ]
    practice = next(
        assessment
        for assessment in manifest["assessments"]
        if assessment["id"] == "general-chemistry-2-4-practice"
    )
    assert "general-chemistry-2-outcome-4" in practice["objective_ids"]

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["general-chemistry-2-4:check"]["solution_spec"]["answer"] == 0
    assert items["general-chemistry-2-4:ligand-field"]["solution_spec"][
        "answer"
    ] == 0
    assert {item_id for item_id in items if item_id.startswith("general-chemistry-2-4:")} == {
        "general-chemistry-2-4:check",
        "general-chemistry-2-4:ligand-field",
    }


def test_coordination_references_are_link_only_and_mapped_to_the_lesson():
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {source["id"]: source for source in registry["sources"]}
    expected = {
        "openstax-chem2-coordination-chemistry",
        "openstax-chem2-coordination-properties",
    }
    module_id = "general-chemistry-2-module-4"
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

