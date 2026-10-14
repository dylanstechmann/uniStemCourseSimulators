"""Regression checks for the expanded Organic Chemistry substitution lesson."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/organic-chemistry"


def test_sn1_sn2_lesson_maps_mechanism_rate_and_stereochemistry():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.4.")
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "organic-chemistry-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 900
    for phrase in (
        "Learning objectives",
        "one-step, concerted pathway",
        "rate = k[substrate][nucleophile]",
        "rate = k[substrate]",
        "twofold initial-rate increase",
        "geometric inversion",
        "exactly 50:50 mixture",
        "Common errors and limits",
        "not laboratory procedures",
    ):
        assert phrase.lower() in text.lower()

    # These are model consequences, not measured kinetic data.
    sn2_rate_ratio = 0.20 / 0.10
    sn1_rate_ratio = 1.0
    assert sn2_rate_ratio == pytest.approx(2)
    assert sn1_rate_ratio == pytest.approx(1)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["organic-chemistry-2:check"]["solution_spec"]["answer"] == 1
    assert questions["organic-chemistry-2:sn2-stereochemistry-and-rate"][
        "solution_spec"
    ]["answer"] == 3
    assert lesson["question_ids"] == [
        "organic-chemistry-2:check",
        "organic-chemistry-2:sn2-stereochemistry-and-rate",
    ]
    assert lesson["card_ids"] == ["organic-chemistry-1-0", "organic-chemistry-1-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["organic-chemistry-2-objective-1"]["course_outcome_ids"] == [
        "organic-chemistry-outcome-2"
    ]
    assert objectives["organic-chemistry-2-objective-2"]["course_outcome_ids"] == [
        "organic-chemistry-outcome-2",
        "organic-chemistry-outcome-3",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "organic-chemistry-2-practice"
    )
    assert "organic-chemistry-outcome-2" in assessment["objective_ids"]
    assert "organic-chemistry-outcome-3" in assessment["objective_ids"]

    source_ids = {
        "openstax-organic-sn2",
        "openstax-organic-sn2-characteristics",
        "openstax-organic-sn1",
        "openstax-organic-sn1-characteristics",
    }
    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped = next(
        item for item in source_map["modules"] if item["lesson_id"] == "organic-chemistry-2"
    )
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "organic-chemistry-module-2"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    assert source_ids <= set(mapped["source_ids"])
    assert source_ids <= set(module["source_ids"])
    for source_id in source_ids:
        source = sources[source_id]
        assert "organic-chemistry-module-2" in source["mapped_modules"]
        assert source["permissions"]["linking"] is True
        assert source["permissions"]["adaptation"] is False
        assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "no compact prototype readings remain" in syllabus
