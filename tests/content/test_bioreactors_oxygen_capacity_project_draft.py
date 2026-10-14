"""Recompute the inactive oxygen-capacity project's transient calculations."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/bioreactors"
PROJECT = COURSE / "assessment-specs/oxygen-capacity-project-draft.md"


def deficit(t: float) -> float:
    return 0.1 * (math.exp(0.2 * t) - math.exp(-0.8 * t))


def test_deficit_solution_capacity_and_threshold_times_recompute():
    quasi_steady_time = math.log(4.8) / 0.2
    low, high = 8.0, 9.0
    for _ in range(80):
        middle = (low + high) / 2
        if deficit(middle) < 0.6:
            low = middle
        else:
            high = middle
    crossing = (low + high) / 2
    derivative_at_zero = 0.1 * (0.2 + 0.8)

    assert deficit(0) == 0
    assert derivative_at_zero > 0
    assert math.isclose(0.8 * (1 - 0.4) - 0.1, 0.38, abs_tol=1e-15)
    assert math.isclose(quasi_steady_time, 7.84307958957, abs_tol=1e-11)
    assert math.isclose(deficit(quasi_steady_time), 0.479811619888, abs_tol=1e-12)
    assert math.isclose(1 - deficit(quasi_steady_time), 0.520188380112, abs_tol=1e-12)
    assert math.isclose(deficit(8), 0.495137086712, abs_tol=1e-12)
    assert math.isclose(deficit(9), 0.604890087860, abs_tol=1e-12)
    assert math.isclose(crossing, 8.95943997847, abs_tol=1e-10)
    assert math.isclose(deficit(crossing), 0.6, abs_tol=1e-12)


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/oxygen-capacity-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
