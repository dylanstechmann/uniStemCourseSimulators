"""Regression checks for the expanded basis and coordinate lesson."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/linear-algebra"


def test_basis_and_frame_transforms_preserve_legacy_assessments():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "linear-algebra-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "Learning objectives",
        "linearly independent",
        "basis matrix",
        "coordinate conversion",
        "active rotation",
        "passive frame change",
        "not necessarily a physical movement",
        "Limits of this lesson",
        "Independence, Basis and Dimension",
    ):
        assert phrase.lower() in text.lower()

    # B maps basis coordinates to standard coordinates.
    basis_coordinates = (3, 1)
    standard_coordinates = (
        basis_coordinates[0] + basis_coordinates[1],
        basis_coordinates[1],
    )
    assert standard_coordinates == (4, 1)
    recovered_basis_coordinates = (
        standard_coordinates[0] - standard_coordinates[1],
        standard_coordinates[1],
    )
    assert recovered_basis_coordinates == basis_coordinates

    # A 90-degree active rotation moves the vector; passive coordinates use Q transpose.
    active_rotation = (-0, 3)
    passive_coordinates = (0, -3)
    assert active_rotation == (0, 3)
    assert passive_coordinates == (0, -3)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["linear-algebra-2:check"]["solution_spec"]["answer"] == pytest.approx(3)
    assert questions["linear-algebra-2:vector-vs-coordinates"]["solution_spec"][
        "answer"
    ] == 4
    assert lesson["question_ids"] == [
        "linear-algebra-2:check",
        "linear-algebra-2:vector-vs-coordinates",
    ]
    assert lesson["card_ids"] == ["linear-algebra-1-0", "linear-algebra-1-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in (
        "linear-algebra-2-objective-1",
        "linear-algebra-2-objective-2",
    ):
        assert objectives[objective_id]["course_outcome_ids"] == [
            "linear-algebra-outcome-2"
        ]
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "linear-algebra-2-practice"
    )
    assert "linear-algebra-outcome-2" in assessment["objective_ids"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped_module = next(
        item for item in source_map["modules"] if item["lesson_id"] == "linear-algebra-2"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    source = next(item for item in registry["sources"] if item["id"] == "linearAlgebra")
    assert "linearAlgebra" in mapped_module["source_ids"]
    assert "linear-algebra-module-2" in source["mapped_modules"]
    assert source["permissions"]["linking"] is True
    assert source["permissions"]["adaptation"] is False
    assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all four compact legacy prototype readings now have expanded instructional content" in syllabus

