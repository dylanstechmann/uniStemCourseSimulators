"""Recompute the inactive statics beam project's stress/deflection tradeoffs."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statics-materials"
PROJECT = COURSE / "assessment-specs/beam-strength-and-stiffness-project-draft.md"


def test_candidate_stress_deflection_and_load_limits_recompute():
    length = 0.3
    width = 0.02
    force = 30.0
    moment = force * length / 4
    expected = {
        "A": (2.0833333333, 0.8680555556, 144.0, 20.736),
        "B": (1.171875, 0.48828125, 192.0, 36.864),
        "C": (1.6875, 1.265625, 160.0, 14.2222222222),
    }
    passing = []

    with (COURSE / "assessment-specs/beam-candidate-comparison.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    for row in rows:
        name = row["candidate"]
        depth = float(row["depth_mm"]) / 1000
        modulus = float(row["elastic_modulus_gpa"]) * 1e9
        yield_strength = float(row["yield_strength_mpa"]) * 1e6
        inertia = width * depth**3 / 12
        stress_mpa = 6 * moment / (width * depth**2) / 1e6
        deflection_mm = force * length**3 / (48 * modulus * inertia) * 1000
        strength_load = (yield_strength / 2) * width * depth**2 / (1.5 * length)
        deflection_load = 0.0006 * 48 * modulus * inertia / length**3

        for actual, target in zip((stress_mpa, deflection_mm, strength_load, deflection_load), expected[name]):
            assert math.isclose(actual, target, abs_tol=1e-9)
        if stress_mpa <= yield_strength / 2 / 1e6 and deflection_mm <= 0.6:
            passing.append(name)
        if name == "B":
            assert math.isclose(deflection_mm * 1.2, 0.5859375, abs_tol=1e-12)

    assert math.isclose(moment, 2.25, abs_tol=1e-15)
    assert passing == ["B"]


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/beam-strength-and-stiffness-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
