"""Recompute the inactive abstract equilibrium project's extent and energy."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-1"
PROJECT = COURSE / "assessment-specs/abstract-gas-equilibrium-project-draft.md"


def test_extent_equilibrium_conservation_and_enthalpy_recompute():
    beta = 0.2
    k_equilibrium = 1.8
    initial_a = 1.0
    initial_b = 0.5
    initial_quotient = beta * initial_b**2 / initial_a
    root = (-11 + math.sqrt(261)) / 8
    amount_a = initial_a - root
    amount_b = initial_b + 2 * root
    heat_kj = root * 20.0

    assert math.isclose(initial_quotient, 0.05, abs_tol=1e-15)
    assert initial_quotient < k_equilibrium
    assert 0 <= root <= initial_a
    assert math.isclose(root, 0.644436802675439, abs_tol=1e-15)
    assert math.isclose(amount_a, 0.355563197324561, abs_tol=1e-15)
    assert math.isclose(amount_b, 1.788873605350878, abs_tol=1e-15)
    assert math.isclose(2 * initial_a + initial_b, 2 * amount_a + amount_b, abs_tol=1e-14)
    assert math.isclose(beta * amount_b**2 / amount_a, k_equilibrium, abs_tol=1e-14)
    assert math.isclose(heat_kj, 12.8887360535, abs_tol=1e-10)


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/abstract-gas-equilibrium-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
