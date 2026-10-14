"""Check nucleotide branch accounting and synthesis/salvage distinctions."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-nucleotide-biosynthesis"
OBJECTIVES = {
    "biochemistry-nucleotide-objective-1",
    "biochemistry-nucleotide-objective-2",
    "biochemistry-nucleotide-objective-3",
}


def _data():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    module = next(item for item in manifest["modules"] if item["id"] == "biochemistry-module-25")
    lesson = module["lessons"][0]
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    questions = {item["id"]: item for item in bank["questions"]}
    return manifest, module, lesson, questions


def test_imp_branch_energy_and_nucleotide_pathways_are_authored():
    _, _, lesson, questions = _data()
    assert questions[f"{LESSON_ID}:gmp-branch-atp"]["solution_spec"]["answer"] == 2
    assert questions[f"{LESSON_ID}:amp-branch-gtp"]["solution_spec"]["answer"] == 4
    assert len(lesson["question_ids"]) == 9
    assert len(lesson["card_ids"]) == 5
    assert questions[f"{LESSON_ID}:prpp-route-accounting"]["solution_spec"]["answer"] == 7
    assert questions[f"{LESSON_ID}:branch-energy-ledger"]["solution_spec"]["answer"] == 0
    assert "four mol GTP" in lesson["worked_example"]
    assert "two mol ATP" in lesson["worked_example"]


def test_nucleotide_lesson_is_scheduled_and_uses_link_only_sources():
    manifest, module, lesson, questions = _data()
    week8 = next(item for item in manifest["duration"]["weeks"] if item["week"] == 8)
    assessment = next(item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice")
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LESSON_ID in week8["lesson_ids"]
    assert f"{LESSON_ID}-practice" in week8["assessment_ids"]
    assert set(lesson["objectives"]) == OBJECTIVES
    assert set(assessment["objective_ids"]) >= OBJECTIVES | {
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert questions[f"{LESSON_ID}:purine-ring-order"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:pyrimidine-ring-order"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "Purine biosynthesis builds the ring directly on PRPP" in reading
    assert "Pyrimidine synthesis constructs the ring before attaching it" in reading
    assert "Ribonucleotide reductase converts ribonucleoside diphosphates" in reading
    assert "5,10-methylene-tetrahydrofolate" in reading

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in module["source_ids"][2:]:
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-25" in source["mapped_modules"]


def test_mixed_route_accounting_keeps_prpp_and_branch_costs_separate():
    _, _, lesson, questions = _data()
    assert "Calculate PRPP use across synthetic de novo purine synthesis" in next(
        item["description"]
        for item in json.loads((COURSE / "course.json").read_text(encoding="utf-8"))["lesson_objectives"]
        if item["id"] == "biochemistry-nucleotide-objective-3"
    )
    assert questions[f"{LESSON_ID}:prpp-route-accounting"]["solution_spec"]["answer"] == 7
    assert "7 mol PRPP" in lesson["worked_example"]
    assert "2 mol GTP" in lesson["worked_example"]
    assert "1 mol ATP" in lesson["worked_example"]
