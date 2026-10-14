"""Protect the gluconeogenesis energy ledger and course integration."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-gluconeogenesis"


def _course_data():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LESSON_ID
    )
    questions = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )["questions"]
    by_id = {question["id"]: question for question in questions}
    return manifest, lesson, by_id


def test_gluconeogenesis_energy_cost_recomputes_from_reaction_counts():
    _, lesson, questions = _course_data()
    pyruvate_per_glucose = 2
    atp = pyruvate_per_glucose * (1 + 1)  # pyruvate carboxylase + phosphoglycerate kinase
    gtp = pyruvate_per_glucose * 1  # PEPCK
    nadh = pyruvate_per_glucose * 1  # glyceraldehyde-3-phosphate dehydrogenase direction

    assert atp == questions[f"{LESSON_ID}:atp-cost"]["solution_spec"]["answer"]
    assert gtp == questions[f"{LESSON_ID}:gtp-cost"]["solution_spec"]["answer"]
    assert nadh == 2
    assert 2.5 * atp == questions[f"{LESSON_ID}:energy-cost-scaling"]["solution_spec"]["answer"]
    assert len(lesson["question_ids"]) == 7
    assert len(lesson["card_ids"]) == 4


def test_gluconeogenesis_lesson_is_scheduled_and_maps_regulation_and_sources():
    manifest, lesson, questions = _course_data()
    week10 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 10)
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice"
    )
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LESSON_ID in week10["lesson_ids"]
    assert f"{LESSON_ID}-practice" in week10["assessment_ids"]
    assert set(assessment["objective_ids"]) >= {
        "biochemistry-gluconeogenesis-objective-1",
        "biochemistry-gluconeogenesis-objective-2",
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert objectives["biochemistry-gluconeogenesis-objective-1"]["course_outcome_ids"] == [
        "biochemistry-outcome-3"
    ]
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-gluconeogenesis-objective-2"
    ]["course_outcome_ids"]
    assert questions[f"{LESSON_ID}:f26bp-control"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:net-glucose-carbon"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "not the reverse of ATP-driven PFK-1" in reading
    assert "even-chain fatty acids" in reading
    assert "Nothing is submitted" not in reading

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in (
        "kegg-glycolysis-gluconeogenesis-map00010",
        "reactome-human-gluconeogenesis",
        "van-schaftingen-hers-1981-f26bp-fbpase",
    ):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-16" in source["mapped_modules"]
