"""Recalculate the synthetic purification table and protect its objective links."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LESSON_ID = "biochemistry-protein-purification"


def _table_rows(markdown: str) -> dict[str, list[float]]:
    rows = {}
    for line in markdown.splitlines():
        if line.startswith(("| Crude extract |", "| Ion-exchange pool |", "| Affinity pool |")):
            cells = [cell.strip().replace(",", "") for cell in line.strip("|").split("|")]
            rows[cells[0]] = [float(value) for value in cells[1:]]
    return rows


def test_purification_table_values_and_formative_numeric_keys_recompute():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LESSON_ID
    )
    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    rows = _table_rows(reading)
    assert set(rows) == {"Crude extract", "Ion-exchange pool", "Affinity pool"}

    calculated = {}
    for name, (volume, protein_concentration, activity_concentration, *_reported) in rows.items():
        total_protein = volume * protein_concentration
        total_activity = volume * activity_concentration
        specific_activity = total_activity / total_protein
        calculated[name] = (total_protein, total_activity, specific_activity)

    start_activity = calculated["Crude extract"][1]
    start_specific = calculated["Crude extract"][2]
    for name, row in rows.items():
        total_protein, total_activity, specific_activity = calculated[name]
        reported_protein, reported_activity, reported_specific, recovery, fold = row[3:]
        assert math.isclose(total_protein, reported_protein, rel_tol=1e-12)
        assert math.isclose(total_activity, reported_activity, rel_tol=1e-12)
        assert math.isclose(specific_activity, reported_specific, rel_tol=1e-12)
        assert math.isclose(total_activity / start_activity * 100, recovery, rel_tol=1e-12)
        assert math.isclose(specific_activity / start_specific, fold, rel_tol=1e-12)

    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    items = {item["id"]: item for item in bank["questions"]}
    assert items[f"{LESSON_ID}:ion-exchange-specific-activity"]["solution_spec"]["answer"] == calculated[
        "Ion-exchange pool"
    ][2]
    assert items[f"{LESSON_ID}:ion-exchange-recovery"]["solution_spec"]["answer"] == 70
    assert math.isclose(
        calculated["Affinity pool"][2] / start_specific,
        70,
        rel_tol=1e-12,
    )


def test_purification_lesson_is_scheduled_and_linked_to_its_new_course_outcome():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LESSON_ID
    )
    outcome = next(item for item in manifest["outcomes"] if item["id"] == "biochemistry-outcome-5")
    assessment = next(item for item in manifest["assessments"] if item["id"] == f"{LESSON_ID}-practice")
    week4 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 4)

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert outcome["id"] in assessment["objective_ids"]
    assert set(lesson["objectives"]).issubset(assessment["objective_ids"])
    assert f"{LESSON_ID}-practice" in week4["assessment_ids"]
    assert LESSON_ID in week4["lesson_ids"]
    assert len(lesson["question_ids"]) == 6
    assert len(lesson["card_ids"]) == 4

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    sources = {source["id"]: source for source in registry["sources"]}
    for source_id in (
        "cytiva-protein-purification-strategies",
        "cytiva-ion-exchange-handbook",
        "cytiva-size-exclusion-handbook",
    ):
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "biochemistry-module-14" in source["mapped_modules"]

