"""Regression checks for the synthetic Geroscience senescence lesson."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/geroscience"


def test_senescence_markers_and_tissue_context_preserve_legacy_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "geroscience-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "durable loss of proliferative capacity",
        "Learning objectives",
        "operational definition",
        "synthetic example",
        "resume proliferation",
        "senescence-associated secretory phenotype",
        "wound healing",
        "not proof that senescent cells caused",
        "no medical advice",
        "Limits of this lesson",
    ):
        assert phrase.lower() in text.lower()

    total_cells = 100
    single_marker_positive = 30
    persistent_arrest_and_damage = 18
    resumed_proliferation = 12
    assert single_marker_positive / total_cells == pytest.approx(0.30)
    assert persistent_arrest_and_damage / total_cells == pytest.approx(0.18)
    assert persistent_arrest_and_damage + resumed_proliferation == single_marker_positive

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["geroscience-2:check"]["solution_spec"]["answer"] == 0
    assert questions["geroscience-2:operational-senescence"]["solution_spec"][
        "answer"
    ] == 1
    assert lesson["question_ids"] == [
        "geroscience-2:check",
        "geroscience-2:operational-senescence",
    ]
    assert lesson["card_ids"] == ["geroscience-1-0", "geroscience-1-1"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    module = next(item for item in source_map["modules"] if item["lesson_id"] == "geroscience-2")
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in (
        "baker-2016-p16-cells-healthy-lifespan",
        "demaria-2014-senescence-wound-healing",
    ):
        source = sources[source_id]
        assert source_id in module["source_ids"]
        assert "geroscience-module-2" in source["mapped_modules"]
        assert source["permissions"]["adaptation"] is False
        assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all four compact legacy prototype readings in weeks 1, 5, 8 and 11 now have expanded instructional readings" in syllabus
