"""Regression checks for the inactive synthetic Geroscience evidence dossier."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/geroscience"


def test_surrogate_dossier_intervals_support_the_intended_careful_reading():
    with (COURSE / "assessment-specs/surrogate-endpoint-evidence.csv").open(
        encoding="utf-8", newline=""
    ) as source:
        rows = {row["study_id"]: row for row in csv.DictReader(source)}

    assert set(rows) == {"A", "B", "C"}
    assert rows["A"]["design"] == "observational_age_groups"
    assert float(rows["A"]["marker_ci_low"]) > 0
    assert float(rows["A"]["function_ci_high"]) < 0
    assert rows["A"]["survival_hazard_ratio"] == ""

    b = rows["B"]
    assert float(b["marker_ci_low"]) < float(b["marker_ci_high"]) < 0
    assert float(b["function_ci_low"]) < 0 < float(b["function_ci_high"])
    assert float(b["survival_ci_low"]) < 1 < float(b["survival_ci_high"])

    c = rows["C"]
    assert float(c["marker_ci_low"]) < 0 < float(c["marker_ci_high"])
    assert float(c["function_ci_low"]) > 0
    assert float(c["survival_ci_high"]) < 1


def test_dossier_remains_a_nonclinical_ungraded_draft_linked_to_the_course():
    draft = (
        COURSE / "assessment-specs/surrogate-endpoint-evidence-dossier-draft.md"
    ).read_text(encoding="utf-8")
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    manifest = (COURSE / "course.json").read_text(encoding="utf-8")

    assert "Status: authoring draft only" in draft
    assert "All estimates and confidence intervals" in draft
    assert "do not constitute formal validation or disproof" in draft
    assert "no claim about a real intervention, clinical outcome or human aging" in draft
    assert "no score, rubric, gradebook mapping, platform activation" in draft
    assert "surrogate-endpoint-evidence-dossier-draft.md" in syllabus
    assert '"version": "0.5.9"' in manifest
    assert "inactive, ungraded paper-exercise draft" in manifest
