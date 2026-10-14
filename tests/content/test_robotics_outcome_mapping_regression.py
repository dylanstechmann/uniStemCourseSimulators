"""Regression checks for Robotics outcome links and targeted formative items."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/robotics"


def test_first_four_robotics_lessons_align_objectives_items_and_outcomes():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    lessons = {
        lesson["id"]: lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] in {f"robotics-{index}" for index in range(1, 5)}
    }
    for index in range(1, 5):
        outcome_id = f"robotics-outcome-{index}"
        for objective_id in lessons[f"robotics-{index}"]["objectives"]:
            assert objectives[objective_id]["course_outcome_ids"] == [outcome_id]
        assessment = next(
            item
            for item in manifest["assessments"]
            if item["id"] == f"robotics-{index}-practice"
        )
        assert outcome_id in assessment["objective_ids"]

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    transform = questions["robotics-1:compose-transform-order"]
    assert transform["options"][transform["solution_spec"]["answer"]] == "T_WB T_BC"
    torque = questions["robotics-3:joint-torque-from-inertia"]
    assert torque["solution_spec"]["answer"] == 0.1
    assert torque["solution_spec"]["unit"] == "N*m"
    safety = questions["robotics-4:safety-clearance-margin"]
    assert safety["options"][safety["solution_spec"]["answer"]].startswith(
        "Do not advance"
    )

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert f"Version: {manifest['version']}." in syllabus
    assert f"{len(questions)} public practice items" in syllabus
