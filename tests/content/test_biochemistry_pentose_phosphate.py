"""Protect pentose-phosphate redox/carbon accounting and course integration."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-pentose-phosphate"


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


def test_pentose_phosphate_redox_and_carbon_ledgers_recompute():
    _, lesson, questions = _course_data()
    oxidative_nadph_per_g6p = 2
    oxidative_co2_per_g6p = 1
    g6p_passes = 6
    nonoxidative_pentose_carbon = 3 * 5
    nonoxidative_glycolytic_carbon = 2 * 6 + 3

    assert oxidative_nadph_per_g6p == questions[
        f"{LESSON_ID}:oxidative-nadph"
    ]["solution_spec"]["answer"]
    assert oxidative_co2_per_g6p == questions[
        f"{LESSON_ID}:oxidative-co2"
    ]["solution_spec"]["answer"]
    assert g6p_passes * oxidative_nadph_per_g6p == questions[
        f"{LESSON_ID}:scale-nadph"
    ]["solution_spec"]["answer"]
    assert nonoxidative_pentose_carbon == nonoxidative_glycolytic_carbon == 15
    labeled_fraction = 45 + 15
    assert labeled_fraction == questions[
        f"{LESSON_ID}:tracer-labeled-ribose"
    ]["solution_spec"]["answer"]
    assert len(lesson["question_ids"]) == 9
    assert len(lesson["card_ids"]) == 5


def test_pentose_phosphate_lesson_is_scheduled_and_uses_link_only_sources():
    manifest, lesson, questions = _course_data()
    week13 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 13)
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice"
    )
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LESSON_ID in week13["lesson_ids"]
    assert f"{LESSON_ID}-practice" in week13["assessment_ids"]
    assert set(assessment["objective_ids"]) >= {
        "biochemistry-ppp-objective-1",
        "biochemistry-ppp-objective-2",
        "biochemistry-ppp-objective-3",
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-ppp-objective-2"
    ]["course_outcome_ids"]
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-ppp-objective-3"
    ]["course_outcome_ids"]
    assert questions[f"{LESSON_ID}:no-direct-atp"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:ribose-demand"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "NADPH, 1 CO2 and 1 ribulose 5-phosphate" in reading
    assert "3 pentose phosphates (15 carbons)" in reading
    assert "labeling alone" in reading
    assert "not an observed biological result" in reading

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in (
        "kegg-pentose-phosphate-map00030",
        "reactome-human-pentose-phosphate",
        "biochem-ppp-tracer-lee-1998",
        "biochem-ppp-tracer-metallo-2009",
    ):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-18" in source["mapped_modules"]
    module = next(
        item for item in manifest["modules"] if item["id"] == "biochemistry-module-18"
    )
    assert {
        "biochem-ppp-tracer-lee-1998",
        "biochem-ppp-tracer-metallo-2009",
    } <= set(module["source_ids"])

