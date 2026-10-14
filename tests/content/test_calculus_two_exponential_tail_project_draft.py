"""Recompute the inactive Calculus II tail and integrated Taylor certificate."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-2"
PROJECT = COURSE / "assessment-specs/exponential-tail-project-draft.md"


def test_taylor_polynomial_integral_and_integrated_error_bound_recompute():
    polynomial_integral = sum(Fraction((-1) ** n, math.factorial(n) * (n + 1)) for n in range(5))
    exact_local_integral = 1 - math.exp(-1)
    actual_error = float(polynomial_integral) - exact_local_integral
    integrated_bound = Fraction(1, 720)

    assert polynomial_integral == Fraction(19, 30)
    assert actual_error > 0
    assert actual_error < float(integrated_bound)
    assert math.isclose(actual_error, math.exp(-1) - 11 / 30, abs_tol=1e-15)
    assert math.isclose(float(integrated_bound), 1 / 720, abs_tol=1e-15)
    assert math.isclose(float(polynomial_integral) + math.exp(-1), 1 + actual_error, abs_tol=1e-15)


def test_improper_tail_and_cutoff_values_recompute():
    tail_at_three = math.exp(-3)
    cutoff = math.log(100)

    assert math.isclose(tail_at_three, 0.0497870683679, abs_tol=1e-13)
    assert math.isclose(cutoff, 4.605170185988, abs_tol=1e-12)
    assert math.exp(-cutoff) <= 0.01
    assert math.exp(-(cutoff - 1e-6)) > 0.01


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/exponential-tail-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
