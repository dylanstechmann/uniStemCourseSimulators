"""Check fatty-acid synthesis, neutral-lipid accounting and provenance."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-fatty-acid-synthesis"
OBJECTIVES = {
    "biochemistry-fatty-synthesis-objective-1",
    "biochemistry-fatty-synthesis-objective-2",
    "biochemistry-neutral-lipid-objective-1",
    "biochemistry-neutral-lipid-objective-2",
}


def _data():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    module = next(item for item in manifest["modules"] if item["id"] == "biochemistry-module-23")
    lesson = module["lessons"][0]
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    questions = {item["id"]: item for item in bank["questions"]}
    return manifest, module, lesson, questions


def test_palmitate_synthesis_carbon_and_cofactor_ledger():
    _, _, lesson, questions = _data()
    prefix = f"{LESSON_ID}:"
    assert questions[f"{prefix}acetyl-coa-count"]["solution_spec"]["answer"] == 8
    assert questions[f"{prefix}malonyl-coa-count"]["solution_spec"]["answer"] == 7
    assert questions[f"{prefix}acc-atp-cost"]["solution_spec"]["answer"] == 7
    assert questions[f"{prefix}nadph-cost"]["solution_spec"]["answer"] == 14
    assert len(lesson["question_ids"]) == 14
    assert len(lesson["card_ids"]) == 8
    assert "Twenty-four mol cytosolic acetyl-CoA" in lesson["worked_example"]
    assert "21 mol ATP" in lesson["worked_example"]
    assert "42 mol NADPH" in lesson["worked_example"]


def test_fatty_acid_synthesis_is_scheduled_with_link_only_sources():
    manifest, module, lesson, questions = _data()
    week13 = next(item for item in manifest["duration"]["weeks"] if item["week"] == 13)
    assessment = next(item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice")
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LESSON_ID in week13["lesson_ids"]
    assert f"{LESSON_ID}-practice" in week13["assessment_ids"]
    assert set(lesson["objectives"]) == OBJECTIVES
    assert set(assessment["objective_ids"]) >= OBJECTIVES | {
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert "biochemistry-outcome-3" in objectives[next(iter(OBJECTIVES))]["course_outcome_ids"]
    assert questions[f"{LESSON_ID}:malonyl-control"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "7 ATP at ACC and 14 NADPH" in reading
    assert "inhibits CPT1" in reading

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in module["source_ids"][2:]:
        source = sources[source_id]
        # Scientific references and the MIT scope comparator are both link-only.
        assert source["reuse_mode"] in {"link-only-reference", "link-only-comparator"}
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        # Course-wide comparators leave mapped_modules empty by convention.
        if source["reuse_mode"] == "link-only-reference":
            assert "biochemistry-module-23" in source["mapped_modules"]


def test_neutral_lipid_storage_and_lipolysis_are_separately_accounted():
    _, _, lesson, questions = _data()
    assert questions[f"{LESSON_ID}:triacylglycerol-fatty-acid-count"]["solution_spec"]["answer"] == 12
    assert questions[f"{LESSON_ID}:tag-acyl-coa"]["solution_spec"]["answer"] == 9
    assert questions[f"{LESSON_ID}:stored-lipolysis-sequence"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:capillary-vs-adipose-lipases"]["solution_spec"]["answer"] == 0
    assert "15 mol fatty acids and 5 mol glycerol" in lesson["worked_example"]

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "ATGL converts TAG to diacylglycerol" in reading
    assert "HSL" in reading and "monoacylglycerol lipase" in reading
    assert "capillary lipoprotein lipase" in reading
