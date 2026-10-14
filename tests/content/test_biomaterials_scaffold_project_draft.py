"""Recompute the inactive Biomaterials scaffold comparison."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biomaterials"
PROJECT = COURSE / "assessment-specs/scaffold-property-project-draft.md"


def test_candidate_degradation_values_and_constraint_outcomes_recompute():
    with (COURSE / "assessment-specs/scaffold-property-comparison.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    expected = {
        "A": (0.870550563296, 0.659753955386, 46.2674833211),
        "B": (0.35, 0.220486183732, 16.9544533632),
        "C": (0.938476086623, 0.769865114624, 53.2856792213),
    }
    passed_day_42 = []
    passed_day_56 = []

    for row in rows:
        name = row["candidate"]
        porosity = float(row["porosity_fraction"])
        initial = float(row["initial_modulus_mpa"])
        permeability = float(row["permeability_scale_1e-12_m2"])
        half_time = float(row["modulus_half_time_days"])
        e42 = initial * 2 ** (-42 / half_time)
        e56 = initial * 2 ** (-56 / half_time)
        time_to_threshold = half_time * math.log2(initial / 0.8)
        structural = porosity >= 0.65 and permeability >= 4 and initial >= 1.5

        assert math.isclose(e42, expected[name][0], abs_tol=1e-11)
        assert math.isclose(e56, expected[name][1], abs_tol=1e-11)
        assert math.isclose(time_to_threshold, expected[name][2], abs_tol=1e-9)
        if structural and e42 >= 0.8:
            passed_day_42.append(name)
        if structural and e56 >= 0.8:
            passed_day_56.append(name)

    assert passed_day_42 == ["C"]
    assert passed_day_56 == []


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "0.3.7" in {entry["version"] for entry in course["history"]}
    assert "assessment-specs/scaffold-property-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
