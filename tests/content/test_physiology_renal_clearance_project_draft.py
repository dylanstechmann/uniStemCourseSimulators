"""Regression checks for the inactive synthetic renal-clearance ledger."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physiology"


def test_clearance_ledger_reconciles_filtered_and_excreted_mass():
    with (COURSE / "assessment-specs/renal-clearance-ledger.csv").open(
        encoding="utf-8", newline=""
    ) as source:
        rows = {
            row["substance"]: row
            for row in csv.DictReader(source)
        }

    reference = rows["reference_marker"]
    gfr = (
        float(reference["urine_mg_per_ml"])
        * float(reference["urine_flow_ml_per_min"])
        / float(reference["plasma_mg_per_ml"])
    )
    assert gfr == 120

    expected_net_transport = {
        "solute_A": ("reabsorbed", 1.2),
        "solute_B": ("balanced", 0.0),
        "solute_C": ("secreted", 0.6),
    }
    for name, (expected_class, expected_net_rate) in expected_net_transport.items():
        row = rows[name]
        plasma = float(row["plasma_mg_per_ml"])
        urine = float(row["urine_mg_per_ml"])
        flow = float(row["urine_flow_ml_per_min"])
        filtered = gfr * plasma
        excreted = urine * flow
        signed_net = excreted - filtered
        actual_class = (
            "secreted" if signed_net > 0 else "reabsorbed" if signed_net < 0 else "balanced"
        )
        assert actual_class == expected_class
        assert abs(abs(signed_net) - expected_net_rate) < 1e-9

    glucose = rows["glucose"]
    glucose_load = gfr * float(glucose["plasma_mg_per_ml"])
    glucose_excretion = (
        float(glucose["urine_mg_per_ml"])
        * float(glucose["urine_flow_ml_per_min"])
    )
    assert glucose_load == 480
    assert glucose_excretion == glucose_load - 375 == 105


def test_clearance_draft_is_synthetic_inactive_and_linked_to_course():
    draft = (
        COURSE / "assessment-specs/renal-clearance-ledger-project-draft.md"
    ).read_text(encoding="utf-8")
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    manifest = (COURSE / "course.json").read_text(encoding="utf-8")

    assert "Status: authoring draft only" in draft
    assert "All measurements are synthetic" in draft
    assert "cannot estimate anyone's kidney function" in draft
    assert "no score, rubric, gradebook mapping, platform activation" in draft
    assert "renal-clearance-ledger-project-draft.md" in syllabus
    assert '"version": "0.4.6"' in manifest
    assert "inactive, ungraded paper-exercise draft" in manifest
