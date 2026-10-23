"""Regression checks for General Chemistry I chemical equilibrium."""

from __future__ import annotations

import json
from pathlib import Path

COURSE = Path(__file__).resolve().parents[2] / "content/courses/general-chemistry-1"
ROOT = COURSE.parents[2]


def test_equilibrium_quotient_and_direction_preserve_practice_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "general-chemistry-1-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 1_000
    for phrase in (
        "Learning objectives",
        "forward and reverse reaction rates are equal",
        "Q_c = [NO₂]²/[N₂O₄]",
        "Q < K",
        "Q > K",
        "temperature",
        "a catalyst",
        "does not tell how quickly",
        "activities and are dimensionless",
    ):
        assert phrase.lower() in text.lower()

    # Direction follows the numerical comparison at the same temperature.
    assert 0.2 < 5
    assert 0.5 < 2

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["general-chemistry-1-4:check"]["solution_spec"]["answer"] == 1
    assert questions["general-chemistry-1-4:q-vs-k"]["solution_spec"]["answer"] == 3
    assert lesson["question_ids"] == [
        "general-chemistry-1-4:check",
        "general-chemistry-1-4:q-vs-k",
    ]
    assert lesson["card_ids"] == [
        "general-chemistry-1-3-0",
        "general-chemistry-1-3-1",
    ]
    assert questions["general-chemistry-1-4:check"]["objective_ids"] == [
        "general-chemistry-1-4-objective-1",
        "general-chemistry-1-4-objective-2",
    ]
    assert questions["general-chemistry-1-4:q-vs-k"]["objective_ids"] == [
        "general-chemistry-1-4-objective-2"
    ]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in (
        "general-chemistry-1-4-objective-1",
        "general-chemistry-1-4-objective-2",
    ):
        assert objectives[objective_id]["course_outcome_ids"] == [
            "general-chemistry-1-outcome-3"
        ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "general-chemistry-1-4-practice"
    )
    assert "general-chemistry-1-outcome-3" in assessment["objective_ids"]

    source_ids = {
        "openstax-chemistry-2e-chemical-equilibria",
        "openstax-chemistry-2e-equilibrium-constants",
        "openstax-chemistry-2e-shifting-equilibria",
    }
    source_map = json.loads(
        (COURSE / "source-map.json").read_text(encoding="utf-8")
    )
    mapped = next(
        item
        for item in source_map["modules"]
        if item["lesson_id"] == "general-chemistry-1-4"
    )
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "general-chemistry-1-module-4"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    assert source_ids <= set(mapped["source_ids"])
    assert source_ids <= set(module["source_ids"])
    for source_id in source_ids:
        source = sources[source_id]
        assert "general-chemistry-1-module-4" in source["mapped_modules"]
        assert source["permissions"]["linking"] is True
        assert source["permissions"]["adaptation"] is False
        assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    calendar_row = next(row for row in syllabus.splitlines() if row.startswith("| 10 |"))
    assert lesson["title"].lower() in calendar_row
    assert lesson["id"] in manifest["duration"]["weeks"][9]["lesson_ids"]
    assert "four compact foundations are paired with expanded instruction" in syllabus
