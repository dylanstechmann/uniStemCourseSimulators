"""Recompute the inactive stiff-system project's exact and Euler values."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/differential-equations"
PROJECT = COURSE / "assessment-specs/stiff-two-compartment-project-draft.md"


def exact(t: float) -> tuple[float, float]:
    return math.exp(-t), (math.exp(-t) - math.exp(-100 * t)) / 99


def forward_euler(h: float, steps: int) -> tuple[float, float]:
    x, y = 1.0, 0.0
    for _ in range(steps):
        x, y = (1 - h) * x, h * x + (1 - 100 * h) * y
    return x, y


def backward_euler(h: float, steps: int) -> tuple[float, float]:
    x, y = 1.0, 0.0
    for _ in range(steps):
        x_next = x / (1 + h)
        y_next = (y + h * x_next) / (1 + 100 * h)
        x, y = x_next, y_next
    return x, y


def test_exact_solution_peak_and_step_restrictions_recompute():
    peak_time = math.log(100) / 99
    peak_value = math.exp(-peak_time) / 100
    exact_state = exact(0.1)
    forward_coarse = forward_euler(0.025, 4)
    backward_coarse = backward_euler(0.025, 4)
    forward_fine = forward_euler(0.01, 10)

    assert math.isclose(exact(0)[0], 1.0, abs_tol=1e-15)
    assert math.isclose(exact(0)[1], 0.0, abs_tol=1e-15)
    assert math.isclose(peak_time, 0.0465168705655, abs_tol=1e-12)
    assert math.isclose(peak_value, 0.00954548456662, abs_tol=1e-14)
    assert 0.025 > 2 / 100 and 0.01 <= 1 / 100
    assert all(math.isclose(a, b, abs_tol=1e-8) for a, b in zip(forward_coarse, (0.903687890625, -0.042008203125)))
    assert all(math.isclose(a, b, abs_tol=1e-8) for a, b in zip(backward_coarse, (0.905950644800, 0.009083704593)))
    assert all(math.isclose(a, b, abs_tol=1e-8) for a, b in zip(forward_fine, (0.904382075009, 0.009135172475)))
    assert math.isclose(exact_state[0], 0.904837418036, abs_tol=1e-12)
    assert math.isclose(exact_state[1], 0.0091393133142, abs_tol=1e-13)
    assert forward_coarse[1] < 0 < backward_coarse[1] and exact_state[1] > 0


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/stiff-two-compartment-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
