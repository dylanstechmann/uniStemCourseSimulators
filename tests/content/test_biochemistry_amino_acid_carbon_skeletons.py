"""Check amino-acid carbon-fate classification and course integration."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-amino-acid-carbon-skeletons"


def _course_data():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LESSON_ID
    )
    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    return manifest, lesson, {question["id"]: question for question in bank["questions"]}


def test_amino_acid_carbon_fates_retain_glucogenic_and_ketogenic_categories():
    _, lesson, questions = _course_data()
    entries = {
        "pyruvate",
        "oxaloacetate",
        "succinyl-CoA",
        "fumarate",
        "Alpha-ketoglutarate",
    }
    options = questions[f"{LESSON_ID}:gluconeogenic-entry-points"]["options"]
    answer_indices = questions[f"{LESSON_ID}:gluconeogenic-entry-points"][
        "solution_spec"
    ]["answer"]
    selected = {options[index].casefold() for index in answer_indices}

    assert selected == {entry.casefold() for entry in entries}
    assert questions[f"{LESSON_ID}:leucine-lysine"]["solution_spec"]["answer"] == 0
    assert questions[f"{LESSON_ID}:both-classification"]["solution_spec"]["answer"] == 0
    assert len(lesson["question_ids"]) == 9
    assert len(lesson["card_ids"]) == 5


def test_amino_acid_carbon_lesson_is_scheduled_and_uses_link_only_sources():
    manifest, lesson, questions = _course_data()
    week2 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 2)
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice"
    )
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LESSON_ID in week2["lesson_ids"]
    assert f"{LESSON_ID}-practice" in week2["assessment_ids"]
    assert set(assessment["objective_ids"]) >= {
        "biochemistry-amino-carbon-objective-1",
        "biochemistry-amino-carbon-objective-2",
        "biochemistry-amino-carbon-objective-3",
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-amino-carbon-objective-2"
    ]["course_outcome_ids"]
    assert questions[f"{LESSON_ID}:acetylcoa-net-glucose"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "Leucine and lysine are the two exclusively ketogenic amino acids" in reading
    assert "not a net glucose precursor in mammals" in reading
    assert "18.0 percentage points" in questions[
        f"{LESSON_ID}:bcaas-share-change"
    ]["options"][0]
    assert questions[f"{LESSON_ID}:tracer-scope"]["solution_spec"][
        "answer"
    ] == 0
    assert objectives["biochemistry-amino-carbon-objective-3"][
        "course_outcome_ids"
    ] == ["biochemistry-outcome-3"]

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in (
        "ncbi-protein-catabolism-amino-acid-fates",
        "review-amino-acid-metabolism-2021",
        "biochem-amino-bcaa-adipocyte-tracing-green-2016",
    ):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-21" in source["mapped_modules"]


def test_homework_one_tracer_case_uses_synthetic_values_and_existing_objective():
    candidate = json.loads(
        (COURSE / "assessment-specs/homework-01-candidate.json").read_text(
            encoding="utf-8"
        )
    )
    data = (COURSE / "assessment-specs/homework-01-candidate-data.csv").read_text(
        encoding="utf-8"
    )
    case = next(
        item
        for item in candidate["questions"]
        if item["id"].endswith(":case-07")
    )
    fields = {field["id"]: field for field in case["response_fields"]}
    assert candidate["points"] == 80
    assert len(candidate["questions"]) == 8
    assert fields["bcaas-share-change"]["unit"] == "pp"
    assert fields["tracer-inference"]["options"][0].startswith(
        "The larger share supports a larger assigned BCAA contribution"
    )
    assert "8.0,percent,synthetic teaching value" in data
    assert "26.0,percent,synthetic teaching value" in data
    assert "not a paper dataset" in data
