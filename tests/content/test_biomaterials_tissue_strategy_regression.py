"""Regression checks for the biomaterials tissue-strategy reading and keys."""

from __future__ import annotations

import json
from pathlib import Path

COURSE = Path(__file__).resolve().parents[2] / "content/courses/biomaterials"


def test_function_led_design_mapping_and_public_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert tuple(int(part) for part in manifest["version"].split(".")) >= (0, 3, 0)
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biomaterials-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8").lower()
    for concept in ("functional target", "cell source", "scaffold", "biochemical cues", "mechanical environment", "integration"):
        assert concept in text

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["biomaterials-3:check"]["solution_spec"]["answer"] == 1
    assert items["biomaterials-3:design-mapping"]["solution_spec"]["answer"] == 1
    assert set(items["biomaterials-3:check"]["objective_ids"]) == {
        "biomaterials-3-objective-2"
    }
    assert set(items["biomaterials-3:design-mapping"]["objective_ids"]) == {
        "biomaterials-3-objective-2"
    }

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "Weeks 3, 9 and 13 also have expanded" in syllabus
