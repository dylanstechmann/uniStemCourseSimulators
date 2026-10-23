"""Regression checks for General Chemistry I thermochemistry and state functions."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-1"


def test_thermochemistry_signs_and_formation_enthalpy_preserve_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "general-chemistry-1-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 1_000
    for phrase in (
        "Learning objectives",
        "ΔU = q + w",
        "surroundings do work on the system",
        "q_reaction = −q_surroundings",
        "q = m c ΔT",
        "q_p = ΔH",
        "Hess’s law",
        "products) − ΣνΔH_f°(reactants)",
        "does not say how fast",
        "not experimental instructions",
    ):
        assert phrase.lower() in text.lower()

    q_solution_j = 100.0 * 4.184 * 2.50
    reaction_kj = -q_solution_j / 1000
    first_delta_h = -620 - (-410)
    methane_delta_h = (-393.5 + 2 * -285.8) - (-74.8 + 2 * 0)
    assert q_solution_j == pytest.approx(1046)
    assert reaction_kj == pytest.approx(-1.046)
    assert first_delta_h == pytest.approx(-210)
    assert methane_delta_h == pytest.approx(-890.3)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["general-chemistry-1-3:check"]["solution_spec"]["answer"] == -210
    assert questions["general-chemistry-1-3:reaction-enthalpy"]["solution_spec"][
        "answer"
    ] == -890.3
    assert lesson["question_ids"] == [
        "general-chemistry-1-3:check",
        "general-chemistry-1-3:reaction-enthalpy",
    ]
    assert lesson["card_ids"] == [
        "general-chemistry-1-2-0",
        "general-chemistry-1-2-1",
    ]
    assert questions["general-chemistry-1-3:check"]["objective_ids"] == [
        "general-chemistry-1-3-objective-1",
        "general-chemistry-1-3-objective-2",
    ]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["general-chemistry-1-3-objective-1"]["course_outcome_ids"] == [
        "general-chemistry-1-outcome-3"
    ]
    assert objectives["general-chemistry-1-3-objective-2"]["course_outcome_ids"] == [
        "general-chemistry-1-outcome-3",
        "general-chemistry-1-outcome-4",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "general-chemistry-1-3-practice"
    )
    assert "general-chemistry-1-outcome-3" in assessment["objective_ids"]
    assert "general-chemistry-1-outcome-4" in assessment["objective_ids"]

    source_ids = {
        "openstax-chemistry-2e-calorimetry",
        "openstax-chemistry-2e-enthalpy",
    }
    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped = next(
        item
        for item in source_map["modules"]
        if item["lesson_id"] == "general-chemistry-1-3"
    )
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "general-chemistry-1-module-3"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    assert source_ids <= set(mapped["source_ids"])
    assert source_ids <= set(module["source_ids"])
    for source_id in source_ids:
        source = sources[source_id]
        assert "general-chemistry-1-module-3" in source["mapped_modules"]
        assert source["permissions"]["linking"] is True
        assert source["permissions"]["adaptation"] is False
        assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    calendar_row = next(row for row in syllabus.splitlines() if row.startswith("| 8 |"))
    assert lesson["title"].lower() in calendar_row
    assert lesson["id"] in manifest["duration"]["weeks"][7]["lesson_ids"]
