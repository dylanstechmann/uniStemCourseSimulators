"""Protect urea-cycle atom, compartment and energy accounting."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-urea-cycle"


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


def test_urea_cycle_nitrogen_and_energy_ledgers_recompute():
    _, lesson, questions = _course_data()
    nitrogen_atoms_per_urea = 1 + 1  # ammonium plus aspartate
    atp_molecules = 2 + 1  # CPS1 plus argininosuccinate synthesis
    high_energy_bonds = 2 + 2  # two ATP-to-ADP plus ATP-to-AMP
    nitrogen_atoms = 5

    assert nitrogen_atoms_per_urea == 2
    assert atp_molecules == questions[
        f"{LESSON_ID}:atp-molecules"
    ]["solution_spec"]["answer"]
    assert high_energy_bonds == questions[
        f"{LESSON_ID}:phosphate-equivalents"
    ]["solution_spec"]["answer"]
    assert nitrogen_atoms / nitrogen_atoms_per_urea == 2.5
    assert questions[f"{LESSON_ID}:nitrogen-to-urea"]["solution_spec"]["answer"] == 2.5
    assert questions[f"{LESSON_ID}:urea-energy-scale"]["solution_spec"]["answer"] == 0
    assert len(lesson["question_ids"]) == 9
    assert len(lesson["card_ids"]) == 5


def test_urea_cycle_is_scheduled_and_uses_link_only_sources():
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
        "biochemistry-urea-cycle-objective-1",
        "biochemistry-urea-cycle-objective-2",
        "biochemistry-urea-cycle-objective-3",
        "biochemistry-outcome-3",
        "biochemistry-outcome-4",
    }
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-urea-cycle-objective-2"
    ]["course_outcome_ids"]
    assert "biochemistry-outcome-4" in objectives[
        "biochemistry-urea-cycle-objective-3"
    ]["course_outcome_ids"]
    assert questions[f"{LESSON_ID}:fumarate-link"]["solution_spec"]["answer"] == 0

    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "3 ATP molecules but 4 high-energy phosphate equivalents" in reading
    assert "ammonium supplies one urea nitrogen" in reading
    assert "not a pathway rate" in reading

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in (
        "kegg-arginine-proline-urea-cycle-map00330",
        "reactome-human-urea-cycle",
        "ncbi-physiology-urea-cycle",
    ):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-20" in source["mapped_modules"]
