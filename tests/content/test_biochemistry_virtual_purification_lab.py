"""Recalculate the synthetic purification lab and guard its formative status."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
LAB_ID = "biochemistry-lab-02"


def _tables():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    cards = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))
    questions = {item["id"]: item for item in bank["questions"]}
    return manifest, questions, cards


def test_purification_lab_is_scheduled_as_ungraded_practice_with_mapped_checks():
    manifest, questions, cards = _tables()
    module_lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LAB_ID
    )
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == "biochemistry-week4-purification-lab"
    )
    week = next(item for item in manifest["duration"]["weeks"] if item["week"] == 4)

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert LAB_ID in week["lesson_ids"]
    assert assessment["mode"] == "practice" and assessment["type"] == "lab"
    assert assessment["question_ids"] == module_lesson["question_ids"]
    assert assessment["points"] == len(module_lesson["question_ids"]) == 7
    assert all(question_id in questions for question_id in module_lesson["question_ids"])
    assert len(module_lesson["card_ids"]) == 4
    assert {card["id"] for card in cards["cards"]} >= set(module_lesson["card_ids"])
    text = (COURSE / module_lesson["reading"]).read_text(encoding="utf-8").lower()
    assert "synthetic" in text and "no experimental procedure" in text


def test_purification_lab_numeric_keys_recompute_from_raw_fractions():
    manifest, questions, _ = _tables()
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LAB_ID
    )
    with (COURSE / "labs/protein-purification-fractions.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = {
            row["fraction"]: {
                key: float(row[key])
                for key in ("volume_ml", "protein_mg_per_ml", "activity_U_per_ml")
            }
            for row in csv.DictReader(handle)
        }

    total_protein = {
        name: row["volume_ml"] * row["protein_mg_per_ml"] for name, row in rows.items()
    }
    total_activity = {
        name: row["volume_ml"] * row["activity_U_per_ml"] for name, row in rows.items()
    }
    specific_activity = {
        name: total_activity[name] / total_protein[name] for name in rows
    }
    expected = {
        "biochemistry-lab2:ion-exchange-protein-mass": total_protein["ion-exchange pool"],
        "biochemistry-lab2:ion-exchange-total-activity": total_activity["ion-exchange pool"],
        "biochemistry-lab2:ion-exchange-specific-activity": specific_activity["ion-exchange pool"],
        "biochemistry-lab2:ion-exchange-recovery": (
            total_activity["ion-exchange pool"] / total_activity["crude extract"] * 100
        ),
        "biochemistry-lab2:sec-enrichment": (
            specific_activity["size-exclusion pool"] / specific_activity["crude extract"]
        ),
    }
    assert {question_id for question_id in lesson["question_ids"] if question_id in expected} == set(expected)
    for question_id, value in expected.items():
        spec = questions[question_id]["solution_spec"]
        allowed = spec["tolerance"] + (spec.get("relative_tolerance") or 0) * abs(spec["answer"])
        assert spec["answer"] == pytest.approx(value, abs=allowed)




def test_purification_lab_worked_table_matches_all_four_synthetic_fractions():
    manifest, _, _ = _tables()
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == LAB_ID
    )
    reading = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    section = reading.split("## Worked comparison across all fractions", 1)[1].split("\n## ", 1)[0]
    with (COURSE / "labs/protein-purification-fractions.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = {row["fraction"].capitalize(): {
            key: float(row[key])
            for key in ("volume_ml", "protein_mg_per_ml", "activity_U_per_ml")
        } for row in csv.DictReader(handle)}
    displayed = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells[0] in rows:
            displayed[cells[0]] = [float(value.replace(",", "")) for value in cells[1:]]

    assert set(displayed) == set(rows)
    crude_activity = rows["Crude extract"]["volume_ml"] * rows["Crude extract"]["activity_U_per_ml"]
    crude_specific = rows["Crude extract"]["activity_U_per_ml"] / rows["Crude extract"]["protein_mg_per_ml"]
    for fraction, row in rows.items():
        protein = row["volume_ml"] * row["protein_mg_per_ml"]
        activity = row["volume_ml"] * row["activity_U_per_ml"]
        specific = activity / protein
        expected = [protein, activity, specific, activity / crude_activity * 100, specific / crude_specific]
        assert displayed[fraction] == pytest.approx(expected, rel=0.003, abs=0.01)
    assert "cannot estimate replicate variability" in section
