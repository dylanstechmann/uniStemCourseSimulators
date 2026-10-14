"""Check fatty-acid beta-oxidation counts and assumption-bound ATP yield."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-fatty-acid-oxidation"


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


def test_palmitate_cycle_carrier_and_atp_ledgers_recompute():
    _, lesson, questions = _course_data()
    carbons = 16
    turns = carbons // 2 - 1
    acetyl_coa = carbons // 2
    nadh = turns + acetyl_coa * 3
    fadh2 = turns + acetyl_coa
    gtp = acetyl_coa
    p_o_nadh = 2.5
    p_o_fadh2 = 1.5
    activation_cost = 2
    atp_equivalents = nadh * p_o_nadh + fadh2 * p_o_fadh2 + gtp - activation_cost

    assert turns == questions[f"{LESSON_ID}:palmitate-cycles"]["solution_spec"]["answer"]
    assert acetyl_coa == questions[f"{LESSON_ID}:palmitate-acetyl-coa"]["solution_spec"]["answer"]
    yield_question = questions[f"{LESSON_ID}:palmitate-atp-yield"]
    assert atp_equivalents == yield_question["solution_spec"]["answer"]
    assert "biochemistry-fatty-acid-objective-2" in yield_question["objective_ids"]
    assert questions[f"{LESSON_ID}:cycle-carriers"]["solution_spec"]["answer"] == 0
    assert len(lesson["question_ids"]) == 7
    assert len(lesson["card_ids"]) == 4


def test_fatty_acid_oxidation_is_scheduled_and_uses_link_only_sources():
    manifest, lesson, questions = _course_data()
    week11 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 11)
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice"
    )
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LESSON_ID in week11["lesson_ids"]
    assert f"{LESSON_ID}-practice" in week11["assessment_ids"]
    assert set(assessment["objective_ids"]) >= {
        "biochemistry-fatty-acid-objective-1",
        "biochemistry-fatty-acid-objective-2",
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-fatty-acid-objective-2"
    ]["course_outcome_ids"]
    assert questions[f"{LESSON_ID}:malonyl-cpt1"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "P/O = 2.5 ATP per mitochondrial NADH and 1.5 ATP per FADH2" in reading
    assert "106 mol ATP equivalents per mol palmitate" in reading

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in (
        "kegg-fatty-acid-degradation-map00071",
        "reactome-human-mitochondrial-fatty-acid-beta-oxidation",
        "pubmed-lipid-metabolism-34470787",
    ):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-19" in source["mapped_modules"]
