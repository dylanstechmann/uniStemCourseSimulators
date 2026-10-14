"""Recalculate and protect the citric-acid-cycle teaching model."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-tca-cycle"


def test_tca_per_turn_and_per_glucose_accounting_recomputes():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LESSON_ID
    )
    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    items = {item["id"]: item for item in bank["questions"]}

    acetyl_per_glucose = 2
    turns_per_glucose = acetyl_per_glucose
    nadh_per_turn = 3
    co2_per_turn = 2
    gtp_per_turn = 1
    assert turns_per_glucose * nadh_per_turn == items[f"{LESSON_ID}:nadh-two-turns"]["solution_spec"]["answer"]
    assert 3.0 * turns_per_glucose * gtp_per_turn == items[f"{LESSON_ID}:gtp-two-turns"]["solution_spec"]["answer"]
    assert turns_per_glucose * co2_per_turn == 4
    assert "Pyruvate dehydrogenase separately contributes 2 CO₂ and 2 NADH" in reading
    assert "carbon atoms mix" in reading.casefold()


def test_tca_lesson_is_scheduled_and_uses_link_only_pathway_sources():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LESSON_ID
    )
    assessment = next(item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice")
    week9 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 9)

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert f"{LESSON_ID}-practice" in week9["assessment_ids"]
    assert LESSON_ID in week9["lesson_ids"]
    assert "biochemistry-outcome-3" in assessment["objective_ids"]
    assert "biochemistry-outcome-4" in assessment["objective_ids"]
    assert len(lesson["question_ids"]) == 8
    assert len(lesson["card_ids"]) == 5

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in ("kegg-citrate-cycle-map00020", "reactome-human-tca-cycle"):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-15" in source["mapped_modules"]

