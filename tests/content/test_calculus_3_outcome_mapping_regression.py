"""Regression checks for Calculus III objective links and corrected items."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-3"


def test_first_four_multivariable_lessons_align_outcomes_and_practice():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert "Represent vectors in frames" in manifest["outcomes"][0]["description"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    lessons = {
        lesson["id"]: lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] in {f"calculus-3-{index}" for index in range(1, 5)}
    }
    for index in range(1, 5):
        outcome_id = f"calculus-3-outcome-{index}"
        for objective_id in lessons[f"calculus-3-{index}"]["objectives"]:
            assert objectives[objective_id]["course_outcome_ids"] == [outcome_id]
        assessment = next(
            item
            for item in manifest["assessments"]
            if item["id"] == f"calculus-3-{index}-practice"
        )
        assert outcome_id in assessment["objective_ids"]

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["calculus-3-1:check"]["objective_ids"] == [
        "calculus-3-1-objective-2"
    ]
    assert questions["calculus-3-2:check"]["objective_ids"] == [
        "calculus-3-2-objective-2"
    ]
    assert questions["calculus-3-4:check"]["objective_ids"] == [
        "calculus-3-4-objective-2"
    ]

    expected_answers = {
        "calculus-3-1:vector-frame-components": "(2, −3)",
        "calculus-3-2:stationary-classification": "Strict local minimum",
        "calculus-3-4:line-integral-work": "Work done by the force along the path",
    }
    for question_id, answer_text in expected_answers.items():
        question = questions[question_id]
        assert question["options"][question["solution_spec"]["answer"]] == answer_text

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert f"Version: {manifest['version']}." in syllabus
    assert f"{len(questions)} public practice items" in syllabus
