"""Regression checks for biomaterials translation framing and answer keys."""

from __future__ import annotations

import json
from pathlib import Path

COURSE = Path(__file__).resolve().parents[2] / "content/courses/biomaterials"


def test_application_specific_evidence_and_failure_categories():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert tuple(int(part) for part in manifest["version"].split(".")) >= (0, 3, 0)
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biomaterials-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8").lower()
    for concept in (
        "specific application",
        "intended function",
        "host response",
        "mechanical",
        "degradation chemistry",
        "process and manufacturing",
        "matched controls",
    ):
        assert concept in text

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["biomaterials-4:check"]["solution_spec"]["answer"] == 1
    assert items["biomaterials-4:failure-mode"]["solution_spec"]["answer"] == 2

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "Weeks 3, 9 and 13 also have expanded" in syllabus
