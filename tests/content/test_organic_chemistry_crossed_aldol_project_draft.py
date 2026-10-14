"""Check atom balance and evidence totals in the inactive aldol portfolio."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/organic-chemistry"
PROJECT = COURSE / "assessment-specs/crossed-aldol-identity-project-draft.md"
EVIDENCE = COURSE / "assessment-specs/crossed-aldol-evidence-cards.csv"


def load_evidence():
    with EVIDENCE.open(encoding="utf-8", newline="") as stream:
        return {row["card"]: row for row in csv.DictReader(stream)}


def degree_of_unsaturation(formula):
    carbon = int(formula.split("C", 1)[1].split("H", 1)[0])
    hydrogen = int(formula.split("H", 1)[1].split("O", 1)[0])
    return (2 * carbon + 2 - hydrogen) / 2


def test_atom_balance_unsaturation_and_spectral_hydrogen_counts():
    evidence = load_evidence()
    addition_formula = "C10H12O2"
    dehydrated_formula = "C10H10O"
    assert degree_of_unsaturation(addition_formula) == 5
    assert degree_of_unsaturation(dehydrated_formula) == 6

    card_a = evidence["A"]
    card_b = evidence["B"]
    hydrogen_a = sum(
        int(card_a[column])
        for column in (
            "aromatic_integral_H",
            "methyl_integral_H",
            "aldehyde_integral_H",
            "aliphatic_methine_integral_H",
            "exchangeable_hydroxyl_integral_H",
        )
    )
    hydrogen_b = sum(
        int(card_b[column])
        for column in (
            "aromatic_integral_H",
            "methyl_integral_H",
            "aldehyde_integral_H",
            "vinylic_integral_H",
            "exchangeable_hydroxyl_integral_H",
        )
    )
    assert hydrogen_a == 12
    assert hydrogen_b == 10
    assert card_a["formula"] == addition_formula
    assert card_b["formula"] == dehydrated_formula
    assert card_a["hydroxyl_observation"] == "compatible"
    assert card_b["hydroxyl_observation"] == "not_detected_under_declared_model"


def test_project_is_linked_inactive_and_versioned():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert manifest["maturity"] == "partial"
    assert manifest["history"][-1]["version"] == manifest["version"]
    assert f"Version: {manifest['version']}." in syllabus
    assert "assessment-specs/crossed-aldol-identity-project-draft.md" in syllabus
    assert "not scheduled or assigned" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "No yield, selectivity, actual product or synthesis procedure is supplied" in project
