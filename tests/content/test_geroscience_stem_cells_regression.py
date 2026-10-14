"""Regression checks for the expanded Geroscience stem-cell prototype."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/geroscience"


def test_stem_cell_function_and_niche_lesson_preserves_legacy_assessments():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "geroscience-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "Learning objectives",
        "cell-associated influences",
        "stem-cell niche",
        "synthetic example",
        "durable self-renewal",
        "Conboy and colleagues",
        "not proof that age alone caused",
        "Limits of this lesson",
        "medical advice",
    ):
        assert phrase.lower() in text.lower()

    attempts = 40
    young_cells_young_niche = 28
    young_cells_aged_niche = 16
    aged_cells_young_niche = 19
    aged_cells_aged_niche = 9
    assert young_cells_young_niche / attempts == pytest.approx(0.70)
    assert young_cells_aged_niche / attempts == pytest.approx(0.40)
    assert aged_cells_young_niche / attempts == pytest.approx(0.475)
    assert aged_cells_aged_niche / attempts == pytest.approx(0.225)
    assert young_cells_young_niche > young_cells_aged_niche
    assert aged_cells_young_niche > aged_cells_aged_niche

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["geroscience-3:check"]["solution_spec"]["answer"] == 1
    assert questions["geroscience-3:niche-and-stem-cell-function"]["solution_spec"][
        "answer"
    ] == 1
    assert lesson["question_ids"] == [
        "geroscience-3:check",
        "geroscience-3:niche-and-stem-cell-function",
    ]
    assert lesson["card_ids"] == ["geroscience-2-0", "geroscience-2-1"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped_module = next(
        item for item in source_map["modules"] if item["lesson_id"] == "geroscience-3"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    source = next(
        item
        for item in registry["sources"]
        if item["id"] == "conboy-2005-heterochronic-parabiosis"
    )
    assert "conboy-2005-heterochronic-parabiosis" in mapped_module["source_ids"]
    assert "conboy-2005-heterochronic-parabiosis" in next(
        module
        for module in manifest["modules"]
        if module["id"] == "geroscience-module-3"
    )["source_ids"]
    assert "geroscience-module-3" in source["mapped_modules"]
    assert source["permissions"]["linking"] is True
    assert source["permissions"]["adaptation"] is False
    assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all four compact legacy prototype readings in weeks 1, 5, 8 and 11 now have expanded instructional readings" in syllabus

