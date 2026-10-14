"""Checks isotope-label arithmetic and objective-to-practice wiring."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def test_tca_isotopologue_example_and_practice_alignment():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    objective_id = "biochemistry-tca-cycle-objective-3"
    question_id = "biochemistry-tca-cycle:isotope-enrichment-vs-flux"
    objective = next(item for item in manifest["lesson_objectives"] if item["id"] == objective_id)
    assert objective["course_outcome_ids"] == ["biochemistry-outcome-3", "biochemistry-outcome-4"]

    module = next(item for item in manifest["modules"] if item["id"] == "biochemistry-module-15")
    lesson = next(item for item in module["lessons"] if item["id"] == "biochemistry-tca-cycle")
    assert objective_id in lesson["objectives"]
    assert question_id in lesson["question_ids"]
    assert "biochemistry-tca-cycle-card-5" in lesson["card_ids"]

    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    question = next(item for item in bank["questions"] if item["id"] == question_id)
    assert question["objective_ids"] == [objective_id]
    assert question["solution_spec"]["answer"] == 0

    early = {"M+0": 70, "M+2": 20, "M+3": 10}
    late = {"M+0": 40, "M+2": 45, "M+3": 15}
    assert sum(early.values()) == sum(late.values()) == 100
    early_labeled = early["M+2"] + early["M+3"]
    late_labeled = late["M+2"] + late["M+3"]
    assert late_labeled - early_labeled == 30
    assert late_labeled / early_labeled == 2

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "does **not** show that cycle flux doubled" in reading


def test_tca_primary_sources_are_link_only_and_mapped():
    source_ids = {"biochem-tca-mimosa-alves-2015", "biochem-tca-anaplerosis-comte-1997"}
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    module = next(item for item in manifest["modules"] if item["id"] == "biochemistry-module-15")
    assert source_ids <= set(module["source_ids"])

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped = next(item for item in source_map["modules"] if item["module_id"] == module["id"])
    assert source_ids <= set(mapped["source_ids"])

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    records = {item["id"]: item for item in registry["sources"]}
    for source_id in source_ids:
        record = records[source_id]
        assert record["reuse_mode"] == "link-only-reference"
        assert record["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert record["mapped_modules"] == ["biochemistry-module-15"]
