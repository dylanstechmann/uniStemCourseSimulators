"""Regression checks for the synthetic Geroscience systems lesson."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/geroscience"


def test_damage_maintenance_and_biomarker_models_preserve_legacy_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "geroscience-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "Learning objectives",
        "damage-input model",
        "maintenance model",
        "adaptation model",
        "delta d",
        "surrogate endpoint",
        "synthetic tissue study",
        "did not show improved function",
        "no medical advice",
        "Limits of this lesson",
    ):
        assert phrase.lower() in text.lower()

    marker_change = 20 - 12
    marker_percent_reduction = marker_change / 20
    control_function = 100
    intervention_function = 100
    assert marker_percent_reduction == pytest.approx(0.40)
    assert intervention_function - control_function == 0

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["geroscience-1:check"]["solution_spec"]["answer"] == 1
    assert questions["geroscience-1:damage-maintenance-adaptation"][
        "solution_spec"
    ]["answer"] == 0
    assert lesson["question_ids"] == [
        "geroscience-1:check",
        "geroscience-1:damage-maintenance-adaptation",
    ]
    assert lesson["card_ids"] == ["geroscience-0-0", "geroscience-0-1"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    module = next(item for item in source_map["modules"] if item["lesson_id"] == "geroscience-1")
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in (
        "lopez-otin-2013-hallmarks",
        "lopez-otin-2023-hallmarks",
        "higgins-chen-2022-clock-reliability",
    ):
        source = sources[source_id]
        assert source_id in module["source_ids"]
        assert "geroscience-module-1" in source["mapped_modules"]
        assert source["permissions"]["adaptation"] is False
        assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all four compact legacy prototype readings in weeks 1, 5, 8 and 11 now have expanded instructional readings" in syllabus
