"""Keep the Biochemistry week-14 case linked, visible and ungraded."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
OBJECTIVES = [
    "biochemistry-13-objective-1",
    "biochemistry-13-objective-2",
    "biochemistry-13-objective-3",
    "biochemistry-glycogen-objective-2",
    "biochemistry-gluconeogenesis-objective-1",
    "biochemistry-gluconeogenesis-objective-2",
    "biochemistry-fatty-acid-objective-2",
    "biochemistry-neutral-lipid-objective-2",
    "biochemistry-ketone-objective-1",
    "biochemistry-ketone-objective-2",
    "biochemistry-urea-cycle-objective-1",
]


def test_metabolic_case_maps_to_week14_objectives_and_has_an_ungraded_checklist():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    case_assessment = next(
        assessment
        for assessment in manifest["assessments"]
        if assessment["id"] == "biochemistry-case"
    )
    case_file = json.loads(
        (COURSE / manifest["case_rubrics"]).read_text(encoding="utf-8")
    )
    case = next(item for item in case_file["cases"] if item["id"] == "biochemistry:case")
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biochemistry-13"
    )
    week14 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 14)
    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert case_assessment["mode"] == case["mode"] == "self-assessment"
    assert case_assessment["points"] == 0
    assert case_assessment["question_ids"] == []
    assert case_assessment["objective_ids"] == case["objective_ids"] == OBJECTIVES
    assert case["rubric"] and all(item["points"] == 0 for item in case["rubric"])
    assert all(item["levels"] == [] for item in case["rubric"])
    assert len(case["rubric"]) == 6
    assert "fed-like versus mobilization-like hepatic dataset" in case["prompt"]
    assert "biochemistry-case" in week14["assessment_ids"]
    assert "## Ungraded case studio:" in reading
    assert "Nothing is submitted, collected or graded." in reading
    assert "0.50 mmol/(L·h)" in reading and "96%" in reading
    assert "Mobilization-like state" in reading
    assert "arbitrary relative flux indices" in reading
    assert "no net glucose carbon in humans" in reading

