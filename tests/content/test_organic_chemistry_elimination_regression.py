"""Regression checks for the expanded Organic Chemistry elimination lesson."""

from __future__ import annotations

import json
from pathlib import Path

COURSE = Path(__file__).resolve().parents[2] / "content/courses/organic-chemistry"
ROOT = COURSE.parents[2]


def test_elimination_lesson_maps_mechanisms_products_and_geometry():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "organic-chemistry-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 1_000
    for phrase in (
        "Learning objectives",
        "rate = k[substrate][base]",
        "rate = k[substrate]",
        "anti-periplanar",
        "trans-diaxial",
        "Zaitsev selectivity",
        "E1cB",
        "no synthesis protocol",
    ):
        assert phrase.lower() in text.lower()

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["organic-chemistry-3:check"]["solution_spec"]["answer"] == 0
    assert questions["organic-chemistry-3:zaitsev-regioselectivity"][
        "solution_spec"
    ]["answer"] == 1
    assert lesson["question_ids"] == [
        "organic-chemistry-3:check",
        "organic-chemistry-3:zaitsev-regioselectivity",
    ]
    assert lesson["card_ids"] == ["organic-chemistry-2-0", "organic-chemistry-2-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["organic-chemistry-3-objective-1"]["course_outcome_ids"] == [
        "organic-chemistry-outcome-2"
    ]
    assert objectives["organic-chemistry-3-objective-2"]["course_outcome_ids"] == [
        "organic-chemistry-outcome-2",
        "organic-chemistry-outcome-3",
    ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "organic-chemistry-3-practice"
    )
    assert "organic-chemistry-outcome-2" in assessment["objective_ids"]
    assert "organic-chemistry-outcome-3" in assessment["objective_ids"]

    source_ids = {
        "openstax-organic-elimination-zaitsev",
        "openstax-organic-e2",
        "openstax-organic-e2-cyclohexane",
        "openstax-organic-e1",
    }
    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped = next(
        item for item in source_map["modules"] if item["lesson_id"] == "organic-chemistry-3"
    )
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "organic-chemistry-module-3"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    assert source_ids <= set(mapped["source_ids"])
    assert source_ids <= set(module["source_ids"])
    for source_id in source_ids:
        source = sources[source_id]
        assert "organic-chemistry-module-3" in source["mapped_modules"]
        assert source["permissions"]["linking"] is True
        assert source["permissions"]["adaptation"] is False
        assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "no compact prototype readings remain" in syllabus
