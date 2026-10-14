"""Regression checks for the expanded Organic Chemistry structure lesson."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/organic-chemistry"


def test_resonance_and_acid_base_reasoning_preserve_legacy_items():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "organic-chemistry-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "Learning objectives",
        "conjugate base",
        "formal charge",
        "only electrons move",
        "resonance hybrid",
        "pKa values defined under compatible conditions",
        "not a reaction rate",
        "Limits of this lesson",
        "chemical handling",
    ):
        assert phrase.lower() in text.lower()

    acid_pka = 5
    conjugate_acid_pka = 9
    equilibrium_constant = 10 ** (conjugate_acid_pka - acid_pka)
    assert equilibrium_constant == pytest.approx(10_000)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["organic-chemistry-1:check"]["solution_spec"]["answer"] == 1
    assert questions["organic-chemistry-1:resonance-carboxylate"][
        "solution_spec"
    ]["answer"] == 0
    assert lesson["question_ids"] == [
        "organic-chemistry-1:check",
        "organic-chemistry-1:resonance-carboxylate",
    ]
    assert lesson["card_ids"] == ["organic-chemistry-0-0", "organic-chemistry-0-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in (
        "organic-chemistry-1-objective-1",
        "organic-chemistry-1-objective-2",
    ):
        assert objectives[objective_id]["course_outcome_ids"] == [
            "organic-chemistry-outcome-1"
        ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "organic-chemistry-1-practice"
    )
    assert "organic-chemistry-outcome-1" in assessment["objective_ids"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped_module = next(
        item
        for item in source_map["modules"]
        if item["lesson_id"] == "organic-chemistry-1"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in (
        "openstax-organic-resonance",
        "openstax-organic-acid-strength",
    ):
        assert source_id in mapped_module["source_ids"]
        assert source_id in next(
            module
            for module in manifest["modules"]
            if module["id"] == "organic-chemistry-module-1"
        )["source_ids"]
        source = sources[source_id]
        assert "organic-chemistry-module-1" in source["mapped_modules"]
        assert source["permissions"]["linking"] is True
        assert source["permissions"]["adaptation"] is False
        assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "no compact prototype readings remain" in syllabus

