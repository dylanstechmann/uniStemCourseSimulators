"""Recompute the inactive Calculus I washout portfolio's calculus and quadrature."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-1"
PROJECT = COURSE / "assessment-specs/washout-model-project-draft.md"


def signal(t: float) -> float:
    return 18 * math.exp(-0.08 * t) + 6 * math.exp(-0.015 * t)


def derivative(t: float) -> float:
    return -1.44 * math.exp(-0.08 * t) - 0.09 * math.exp(-0.015 * t)


def test_project_csv_matches_constructed_model_and_simpson_key():
    with (COURSE / "assessment-specs/washout-capstone-signals.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    times = [int(row["time_hours"]) for row in rows]
    observed = [float(row["observed_signal"]) for row in rows]
    blank = [float(row["known_blank"]) for row in rows]
    corrected = [y - b for y, b in zip(observed, blank)]

    assert times == [0, 4, 8, 12, 16, 20, 24]
    assert all(math.isclose(y, signal(t) + 3, abs_tol=5.1e-7) for t, y in zip(times, observed))
    assert blank == [3.0] * 7
    simpson = 4 / 3 * (corrected[0] + corrected[-1] + 4 * sum(corrected[1:-1:2]) + 2 * sum(corrected[2:-1:2]))
    exact = 18 / 0.08 * (1 - math.exp(-0.08 * 24)) + 6 / 0.015 * (1 - math.exp(-0.015 * 24))

    assert math.isclose(simpson, 312.953964, abs_tol=1e-8)
    assert math.isclose(exact, 312.9429030923, abs_tol=1e-9)
    assert math.isclose(simpson - exact, 0.0110609077, abs_tol=1e-8)
    assert math.isclose((simpson - exact) / exact, 0.000035344, abs_tol=2e-7)


def test_project_newton_derivatives_and_blank_sensitivity_recompute():
    t = 20.0
    first = t - (signal(t) - 8) / derivative(t)
    second = first - (signal(first) - 8) / derivative(first)
    second_derivative_at_zero = 1.44 * 0.08 + 6 * 0.015**2

    assert math.isclose(derivative(0), -1.53, abs_tol=1e-12)
    assert second_derivative_at_zero > 0
    assert derivative(24) < 0
    assert math.isclose(first, 20.2211685084, abs_tol=1e-9)
    assert math.isclose(second, 20.2228440790, abs_tol=1e-9)
    assert abs(signal(second) - 8) < 4e-8
    assert math.isclose((3.05 - 3.00) * 24, 1.2, abs_tol=1e-12)


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    lab = (COURSE / "labs/01-washout-background.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/washout-model-project-draft.md" in syllabus
    assert "inactive, unscheduled and ungraded" in lab
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "no automatic prose grader" in project
