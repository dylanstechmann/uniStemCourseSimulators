"""Regression checks for General Chemistry I stoichiometry and concentration."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-1"


def test_stoichiometry_limiter_and_dilution_preserve_assessment_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.4.")
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "general-chemistry-1-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 900
    for phrase in (
        "Learning objectives",
        "mole-ratio map",
        "smallest value",
        "theoretical amount",
        "M = n(solute) / V(solution)",
        "C₁V₁ = C₂V₂",
        "final solution volume",
        "significant-figure",
        "not laboratory instructions",
    ):
        assert phrase.lower() in text.lower()

    n_h2 = 4.0 / 2.016
    n_o2 = 32.0 / 32.00
    extent_h2 = n_h2 / 2
    extent_o2 = n_o2 / 1
    theoretical_water_g = min(extent_h2, extent_o2) * 2 * 18.015
    stock_volume_ml = (0.10 * 300) / 1.5
    assert extent_h2 < extent_o2
    assert theoretical_water_g == pytest.approx(35.74, abs=0.02)
    assert stock_volume_ml == pytest.approx(20)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["general-chemistry-1-2:check"]["solution_spec"]["answer"] == 20
    assert questions["general-chemistry-1-2:limiting-reagent"]["solution_spec"][
        "answer"
    ] == 35.74
    assert lesson["question_ids"] == [
        "general-chemistry-1-2:check",
        "general-chemistry-1-2:limiting-reagent",
    ]
    assert lesson["card_ids"] == [
        "general-chemistry-1-1-0",
        "general-chemistry-1-1-1",
    ]
    assert questions["general-chemistry-1-2:check"]["objective_ids"] == [
        "general-chemistry-1-2-objective-2"
    ]
    assert questions["general-chemistry-1-2:limiting-reagent"]["objective_ids"] == [
        "general-chemistry-1-2-objective-1",
        "general-chemistry-1-2-objective-2",
    ]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["general-chemistry-1-2-objective-1"]["course_outcome_ids"] == [
        "general-chemistry-1-outcome-1"
    ]
    assert objectives["general-chemistry-1-2-objective-2"]["course_outcome_ids"] == [
        "general-chemistry-1-outcome-1",
        "general-chemistry-1-outcome-4",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "general-chemistry-1-2-practice"
    )
    assert "general-chemistry-1-outcome-1" in assessment["objective_ids"]
    assert "general-chemistry-1-outcome-4" in assessment["objective_ids"]

    source_ids = {
        "openstax-chemistry-2e-molarity",
        "openstax-chemistry-2e-stoichiometry",
        "openstax-chemistry-2e-reaction-yields",
    }
    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped = next(
        item
        for item in source_map["modules"]
        if item["lesson_id"] == "general-chemistry-1-2"
    )
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "general-chemistry-1-module-2"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    assert source_ids <= set(mapped["source_ids"])
    assert source_ids <= set(module["source_ids"])
    for source_id in source_ids:
        source = sources[source_id]
        assert "general-chemistry-1-module-2" in source["mapped_modules"]
        assert source["permissions"]["linking"] is True
        assert source["permissions"]["adaptation"] is False
        assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "| 3 | stoichiometry, solution concentration and reaction extents |" in syllabus
