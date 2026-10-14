"""Regression checks for Cellular Biomechanics objectives and item alignment."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cellular-biomechanics"


def test_first_four_mechanics_lessons_map_to_outcomes_and_direct_items():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    expected_outcomes = {
        "cellular-biomechanics-1-objective-1": ["cellular-biomechanics-outcome-1"],
        "cellular-biomechanics-1-objective-2": ["cellular-biomechanics-outcome-2"],
        "cellular-biomechanics-2-objective-1": ["cellular-biomechanics-outcome-3"],
        "cellular-biomechanics-2-objective-2": ["cellular-biomechanics-outcome-3"],
        "cellular-biomechanics-3-objective-1": ["cellular-biomechanics-outcome-3"],
        "cellular-biomechanics-3-objective-2": ["cellular-biomechanics-outcome-3"],
        "cellular-biomechanics-4-objective-1": ["cellular-biomechanics-outcome-4"],
        "cellular-biomechanics-4-objective-2": ["cellular-biomechanics-outcome-4"],
    }
    for objective_id, outcome_ids in expected_outcomes.items():
        assert objectives[objective_id]["course_outcome_ids"] == outcome_ids

    expected_assessments = {
        "cellular-biomechanics-1-practice": {
            "cellular-biomechanics-outcome-1",
            "cellular-biomechanics-outcome-2",
        },
        "cellular-biomechanics-2-practice": {"cellular-biomechanics-outcome-3"},
        "cellular-biomechanics-3-practice": {"cellular-biomechanics-outcome-3"},
        "cellular-biomechanics-4-practice": {"cellular-biomechanics-outcome-4"},
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
    assert questions["cellular-biomechanics-1:check"]["objective_ids"] == [
        "cellular-biomechanics-1-objective-2"
    ]
    assert questions["cellular-biomechanics-3:check"]["objective_ids"] == [
        "cellular-biomechanics-3-objective-2"
    ]

    expected_answers = {
        "cellular-biomechanics-1:mechanical-quantity-definitions": 0,
        "cellular-biomechanics-2:force-path": 0,
        "cellular-biomechanics-3:input-versus-readout": 0,
    }
    for question_id, expected_index in expected_answers.items():
        assert questions[question_id]["solution_spec"]["answer"] == expected_index
        assert questions[question_id]["options"][expected_index]

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert f"Version: {manifest['version']}." in syllabus
