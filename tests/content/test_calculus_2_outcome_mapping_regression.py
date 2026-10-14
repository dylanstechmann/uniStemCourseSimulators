"""Regression checks for Calculus II objective alignment and direct practice."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-2"


def test_first_four_calculus_lessons_map_to_outcomes_and_direct_items():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert "convergence of improper integrals" in manifest["outcomes"][0]["description"]

    expected_outcomes = {
        "calculus-2-1-objective-1": ["calculus-2-outcome-1"],
        "calculus-2-1-objective-2": ["calculus-2-outcome-1"],
        "calculus-2-2-objective-1": ["calculus-2-outcome-3"],
        "calculus-2-2-objective-2": ["calculus-2-outcome-4"],
        "calculus-2-3-objective-1": ["calculus-2-outcome-2"],
        "calculus-2-3-objective-2": ["calculus-2-outcome-2"],
        "calculus-2-4-objective-1": ["calculus-2-outcome-4"],
        "calculus-2-4-objective-2": ["calculus-2-outcome-3", "calculus-2-outcome-4"],
    }
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id, outcome_ids in expected_outcomes.items():
        assert objectives[objective_id]["course_outcome_ids"] == outcome_ids

    assessments = {item["id"]: item for item in manifest["assessments"]}
    assert "calculus-2-outcome-3" in assessments["calculus-2-4-practice"]["objective_ids"]
    assert "calculus-2-outcome-4" in assessments["calculus-2-4-practice"]["objective_ids"]
    assert assessments["calculus-2-1-practice"]["points"] == 3
    assert assessments["calculus-2-4-practice"]["points"] == 4

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["calculus-2-1:check"]["objective_ids"] == [
        "calculus-2-1-objective-2"
    ]
    method_choice = questions["calculus-2-1:method-selection"]
    assert "u = x²" in method_choice["options"][method_choice["solution_spec"]["answer"]]
    taylor_choice = questions["calculus-2-4:taylor-from-derivatives"]
    assert taylor_choice["options"][taylor_choice["solution_spec"]["answer"]] == "1 + x + x²/2"
    interval_choice = questions["calculus-2-4:power-series-interval"]
    assert interval_choice["options"][interval_choice["solution_spec"]["answer"]] == "−1 < x < 5"

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert f"Version: {manifest['version']}." in syllabus
    assert f"{len(questions)} public practice items" in syllabus
