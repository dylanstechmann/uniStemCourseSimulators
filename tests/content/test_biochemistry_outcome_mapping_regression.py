"""Regression checks for Biochemistry I objective and outcome alignment."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def test_first_four_biochemistry_lessons_map_to_outcomes_and_assess_them():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]

    lessons = {
        lesson["id"]: lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] in {"biochemistry-1", "biochemistry-2", "biochemistry-3", "biochemistry-4"}
    }
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for index in range(1, 5):
        lesson = lessons[f"biochemistry-{index}"]
        for objective_id in lesson["objectives"]:
            assert objectives[objective_id]["course_outcome_ids"] == [
                f"biochemistry-outcome-{index}"
            ]

        assessment = next(
            item
            for item in manifest["assessments"]
            if item["id"] == f"biochemistry-{index}-practice"
        )
        assert f"biochemistry-outcome-{index}" in assessment["objective_ids"]

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["biochemistry-1:check"]["objective_ids"] == [
        "biochemistry-1-objective-2"
    ]
    assert questions["biochemistry-4:check"]["objective_ids"] == [
        "biochemistry-4-objective-2"
    ]
    assert questions["biochemistry-1:structure-levels"]["objective_ids"] == [
        "biochemistry-1-objective-1"
    ]
    assert questions["biochemistry-1:structure-levels"]["solution_spec"]["answer"] == 0
    assert questions["biochemistry-4:regulatory-layers"]["objective_ids"] == [
        "biochemistry-4-objective-1"
    ]
    assert questions["biochemistry-4:regulatory-layers"]["solution_spec"]["answer"] == 0
