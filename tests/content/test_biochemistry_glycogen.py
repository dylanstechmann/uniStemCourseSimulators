"""Check glycogen storage/mobilization accounting and course integration."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-glycogen-metabolism"


def _course_data():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LESSON_ID
    )
    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    return manifest, lesson, {question["id"]: question for question in bank["questions"]}


def test_glycogen_storage_and_mobilization_energy_ledgers_recompute():
    _, lesson, questions = _course_data()
    atp_for_glucose_phosphorylation = 1
    atp_equivalents_for_utp_regeneration = 1
    storage_cost = atp_for_glucose_phosphorylation + atp_equivalents_for_utp_regeneration
    glycogen_residues = 4
    atp_per_residue_to_lactate = 3

    assert storage_cost == questions[
        f"{LESSON_ID}:glycogen-storage-cost"
    ]["solution_spec"]["answer"]
    assert glycogen_residues * atp_per_residue_to_lactate == questions[
        f"{LESSON_ID}:muscle-atp-yield"
    ]["solution_spec"]["answer"]
    assert len(lesson["question_ids"]) == 7
    assert len(lesson["card_ids"]) == 4


def test_glycogen_lesson_is_scheduled_with_tissue_control_and_link_only_sources():
    manifest, lesson, questions = _course_data()
    week12 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 12)
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice"
    )
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LESSON_ID in week12["lesson_ids"]
    assert f"{LESSON_ID}-practice" in week12["assessment_ids"]
    assert set(assessment["objective_ids"]) >= {
        "biochemistry-glycogen-objective-1",
        "biochemistry-glycogen-objective-2",
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-glycogen-objective-2"
    ]["course_outcome_ids"]
    assert questions[f"{LESSON_ID}:tissue-roles"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:phosphorylation-switch"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "Skeletal muscle lacks this glucose-export step" in reading
    assert "two ATP equivalents per residue incorporated" in reading

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in (
        "kegg-glycogen-map00500",
        "reactome-human-glycogen-metabolism",
        "human-glycogen-metabolism-review-2016",
    ):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-17" in source["mapped_modules"]
