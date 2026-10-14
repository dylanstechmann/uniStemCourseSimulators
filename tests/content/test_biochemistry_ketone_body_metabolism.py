"""Protect ketone-body tissue distinctions and ketolysis carbon accounting."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-ketone-body-metabolism"


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


def test_ketolysis_acetyl_coa_stoichiometry_recomputes():
    _, lesson, questions = _course_data()
    acetoacetate_moles = 3
    acetyl_coa_per_acetoacetate = 2

    assert acetoacetate_moles * acetyl_coa_per_acetoacetate == questions[
        f"{LESSON_ID}:acetyl-coa-yield"
    ]["solution_spec"]["answer"]
    assert questions[f"{LESSON_ID}:liver-scot"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:fasting-integration"]["solution_spec"]["answer"] == 0
    assert len(lesson["question_ids"]) == 9
    assert len(lesson["card_ids"]) == 6


def test_ketone_body_lesson_is_scheduled_and_uses_link_only_sources():
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
        "biochemistry-ketone-objective-1",
        "biochemistry-ketone-objective-2",
        "biochemistry-ketone-objective-3",
        "biochemistry-ketone-objective-4",
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-ketone-objective-2"
    ]["course_outcome_ids"]
    assert questions[f"{LESSON_ID}:redox-ratio"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert (
        "Human tissue measurements reported SCOT protein in several oxidative tissues "
        "but did not detect it in liver samples"
    ) in reading
    assert "red blood cells cannot perform mitochondrial ketolysis" in reading.casefold()
    assert (
        "not evidence that hepatocytes perform the canonical SCOT-dependent oxidative route"
        in reading
    )

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in (
        "reactome-human-ketone-body-metabolism",
        "ncbi-biochemistry-ketogenesis",
        "review-metabolic-signaling-ketone-bodies",
        "biochem-ketone-scot-tissue-fukao-1997",
        "biochem-ketone-hepatic-anabolism-queathem-2025",
    ):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-22" in source["mapped_modules"]


def test_conditional_ketone_yields_recompute_and_match_formative_items():
    manifest, lesson, questions = _course_data()
    acetoacetate_atp_eq = 6 * 2.5 + 2 * 1.5 + 1
    beta_hydroxybutyrate_atp_eq = 7 * 2.5 + 2 * 1.5 + 1
    assert acetoacetate_atp_eq == 19
    assert beta_hydroxybutyrate_atp_eq == 21.5
    assert 2.0 * beta_hydroxybutyrate_atp_eq == 43
    assert questions[f"{LESSON_ID}:conditional-atp-yield"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:hepatic-fate-nuance"]["solution_spec"]["answer"] == 1

    objective_ids = {item["id"] for item in manifest["lesson_objectives"]}
    assert {"biochemistry-ketone-objective-3", "biochemistry-ketone-objective-4"} <= objective_ids
    assert {"biochemistry-ketone-objective-3", "biochemistry-ketone-objective-4"} <= set(lesson["objectives"])
