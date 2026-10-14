"""Regression checks for Calculus I outcome links and the direct limit item."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-1"


def test_first_four_calculus_lessons_align_objectives_items_and_outcomes():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    lessons = {
        lesson["id"]: lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] in {f"calculus-1-{index}" for index in range(1, 5)}
    }
    for index in range(1, 5):
        outcome_id = f"calculus-1-outcome-{index}"
        lesson = lessons[f"calculus-1-{index}"]
        for objective_id in lesson["objectives"]:
            assert objectives[objective_id]["course_outcome_ids"] == [outcome_id]

        assessment = next(
            item
            for item in manifest["assessments"]
            if item["id"] == f"calculus-1-{index}-practice"
        )
        assert outcome_id in assessment["objective_ids"]

    first_lesson = lessons["calculus-1-1"]
    assert "calculus-1-1:limit-factor-cancel" in first_lesson["question_ids"]
    first_assessment = next(
        item for item in manifest["assessments"] if item["id"] == "calculus-1-1-practice"
    )
    assert first_assessment["points"] == 3

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["calculus-1-1:check"]["objective_ids"] == [
        "calculus-1-1-objective-2"
    ]
    limit_item = questions["calculus-1-1:limit-factor-cancel"]
    assert limit_item["objective_ids"] == ["calculus-1-1-objective-1"]
    assert limit_item["options"][limit_item["solution_spec"]["answer"]] == "4"

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert f"Version: {manifest['version']}." in syllabus
    assert f"{len(questions)} public practice items" in syllabus
