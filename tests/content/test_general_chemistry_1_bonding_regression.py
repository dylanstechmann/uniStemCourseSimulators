"""Equation and model checks for the General Chemistry I bonding primer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-1"


def test_configuration_lewis_vsepr_and_polarity_examples():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "general-chemistry-1-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("valence electrons", "effective nuclear charge"):
        assert concept.lower() in text.lower()
    # Lewis/VSEPR moved to the week-2 bonding lesson when week 1 was narrowed.
    bonding = (COURSE / "modules/08-bonding-geometry-and-molecular-properties.md").read_text(encoding="utf-8")
    for concept in (
        "formal charge",
        "electron-domain geometry",
        "molecular shape",
        "trigonal planar",
        "tetrahedral",
        "vector sum",
        "molecular orbitals",
    ):
        assert concept.lower() in bonding.lower()

    water_valence_electrons = 6 + 2 * 1
    water_oxygen_formal_charge = 6 - 4 - 4 / 2
    water_hydrogen_formal_charge = 1 - 0 - 2 / 2
    assert water_valence_electrons == 8
    assert water_oxygen_formal_charge == pytest.approx(0)
    assert water_hydrogen_formal_charge == pytest.approx(0)
    assert 2 * math.cos(math.radians(104.5 / 2)) == pytest.approx(1.225, abs=0.001)
    assert 1 + (-1) == 0  # equal, opposite bond dipoles cancel in linear CO2

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["general-chemistry-1-1:check"]["solution_spec"]["answer"] == 2
    assert items["general-chemistry-1-1:vsepr-water"]["solution_spec"][
        "answer"
    ] == 0
    assert items["general-chemistry-1-1:check"]["objective_ids"] == [
        "general-chemistry-1-1-objective-2"
    ]
    periodic = items["general-chemistry-1-1:periodic-trend"]
    assert periodic["solution_spec"]["answer"] == 0
    assert periodic["objective_ids"] == ["general-chemistry-1-1-objective-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    outcome = next(
        item for item in manifest["outcomes"]
        if item["id"] == "general-chemistry-1-outcome-2"
    )
    assert "electronic structure" in outcome["description"]
    assert objectives["general-chemistry-1-1-objective-1"]["course_outcome_ids"] == [
        "general-chemistry-1-outcome-2"
    ]
    assert objectives["general-chemistry-1-1-objective-2"]["course_outcome_ids"] == [
        "general-chemistry-1-outcome-2"
    ]
    assessment = next(
        item for item in manifest["assessments"]
        if item["id"] == "general-chemistry-1-1-practice"
    )
    assert assessment["points"] == 3
    assert "general-chemistry-1-outcome-2" in assessment["objective_ids"]
    assert set(assessment["question_ids"]) == {
        periodic["id"],
        "general-chemistry-1-1:oxygen-valence",
        "general-chemistry-1-1:effective-charge",
    }
    lessons = {lesson["id"]: lesson for module in manifest["modules"] for lesson in module["lessons"]}
    assert set(assessment["question_ids"]) <= set(lessons["general-chemistry-1-1"]["question_ids"])
    # The Lewis/VSEPR items keep their IDs but moved with that instruction to the bonding lesson.
    assert {"general-chemistry-1-1:check", "general-chemistry-1-1:vsepr-water"} <= set(
        lessons["general-chemistry-1-8"]["question_ids"]
    )

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
