"""Check cholesterol feedback and particle-specific lipoprotein logic."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-cholesterol-lipoproteins"
OBJECTIVES = {
    "biochemistry-cholesterol-objective-1",
    "biochemistry-cholesterol-objective-2",
    "biochemistry-cholesterol-objective-3",
}


def _data():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    module = next(item for item in manifest["modules"] if item["id"] == "biochemistry-module-24")
    lesson = module["lessons"][0]
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    questions = {item["id"]: item for item in bank["questions"]}
    return manifest, module, lesson, questions


def test_sterol_feedback_and_lipoprotein_roles_are_authored():
    _, _, lesson, questions = _data()
    assert len(lesson["question_ids"]) == 9
    assert len(lesson["card_ids"]) == 5
    assert "processing and expression" in lesson["worked_example"]
    assert questions[f"{LESSON_ID}:hmgcr-reaction"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:low-sterol-response"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:lpl-activation"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:ldl-receptor-ligand"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:endogenous-route"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:hepatocyte-pool-change"]["solution_spec"]["answer"] == 30
    assert questions[f"{LESSON_ID}:pool-vs-plasma"]["solution_spec"]["answer"] == 0


def test_cholesterol_lipoprotein_lesson_is_scheduled_and_cited_link_only():
    manifest, module, lesson, _ = _data()
    week12 = next(item for item in manifest["duration"]["weeks"] if item["week"] == 12)
    assessment = next(item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice")
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LESSON_ID in week12["lesson_ids"]
    assert f"{LESSON_ID}-practice" in week12["assessment_ids"]
    assert set(lesson["objectives"]) == OBJECTIVES
    assert set(assessment["objective_ids"]) >= OBJECTIVES | {
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "SCAP-SREBP system" in reading
    assert "ApoB-48" in reading and "ApoB-100" in reading
    assert "ApoC-II activates lipoprotein lipase (LPL)" in reading
    assert "36 + 24 − 18 − 12 = +30 mg/h" in reading
    assert "does not, by itself, quantify the plasma LDL change" in reading

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in module["source_ids"][2:]:
        source = sources[source_id]
        # Scientific references and the MIT scope comparator are both link-only.
        assert source["reuse_mode"] in {"link-only-reference", "link-only-comparator"}
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        # Course-wide comparators leave mapped_modules empty by convention.
        if source["reuse_mode"] == "link-only-reference":
            assert "biochemistry-module-24" in source["mapped_modules"]
