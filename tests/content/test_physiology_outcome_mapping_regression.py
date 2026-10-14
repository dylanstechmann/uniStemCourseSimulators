"""Regression checks for first-four Physiology outcomes and direct practice."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physiology"


def test_first_four_physiology_lessons_align_objectives_items_and_outcomes():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    expected_objectives = {
        "physiology-1-objective-1": ["physiology-outcome-1"],
        "physiology-1-objective-2": ["physiology-outcome-4"],
        "physiology-2-objective-1": ["physiology-outcome-3"],
        "physiology-2-objective-2": ["physiology-outcome-3"],
        "physiology-3-objective-1": ["physiology-outcome-2"],
        "physiology-3-objective-2": ["physiology-outcome-3"],
        "physiology-4-objective-1": ["physiology-outcome-1"],
        "physiology-4-objective-2": ["physiology-outcome-4"],
    }
    for objective_id, outcome_ids in expected_objectives.items():
        assert objectives[objective_id]["course_outcome_ids"] == outcome_ids

    expected_assessments = {
        "physiology-1-practice": {"physiology-outcome-1", "physiology-outcome-4"},
        "physiology-2-practice": {"physiology-outcome-3"},
        "physiology-3-practice": {"physiology-outcome-2", "physiology-outcome-3"},
        "physiology-4-practice": {"physiology-outcome-1", "physiology-outcome-4"},
    }
    for assessment_id, outcome_ids in expected_assessments.items():
        assessment = next(
            item for item in manifest["assessments"] if item["id"] == assessment_id
        )
        assert outcome_ids <= set(assessment["objective_ids"])

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["physiology-2:check"]["objective_ids"] == [
        "physiology-2-objective-2"
    ]
    expected_answers = {
        "physiology-1:feedback-loop-components": "The sensor measures the regulated variable, the controller compares it with a reference, and the effector changes the variable.",
        "physiology-2:voltage-state-variable": "The inside is 70 mV more negative than the outside.",
        "physiology-3:ventilation-limitation": "Increase alveolar ventilation to restore gas delivery to the exchange surface.",
    }
    for question_id, answer_text in expected_answers.items():
        question = questions[question_id]
        assert question["options"][question["solution_spec"]["answer"]] == answer_text

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert f"Version: {manifest['version']}." in syllabus
