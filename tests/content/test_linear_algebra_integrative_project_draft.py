"""Recompute the inactive linear-algebra project and enforce its draft status."""

from __future__ import annotations

import csv
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/linear-algebra"
PROJECT = COURSE / "assessment-specs/hidden-state-reconstruction-project-draft.md"


def test_project_least_squares_dataset_and_solution_are_consistent():
    with (COURSE / "assessment-specs/state-readouts.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    a = [[Fraction(row[f"weight_state_{state}"]) for state in "ABC"] for row in rows]
    b = [Fraction(row["observed_readout"]) for row in rows]
    gram = [[sum(a[i][j] * a[i][k] for i in range(len(a))) for k in range(3)] for j in range(3)]
    rhs = [sum(a[i][j] * b[i] for i in range(len(a))) for j in range(3)]
    estimate = [rhs[j] / gram[j][j] for j in range(3)]
    residual = [b[i] - sum(a[i][j] * estimate[j] for j in range(3)) for i in range(len(a))]
    residual_projection = [sum(a[i][j] * residual[i] for i in range(len(a))) for j in range(3)]

    assert gram == [[2, 0, 0], [0, 2, 0], [0, 0, 1]]
    assert rhs == [Fraction(2, 5), 1, Fraction(3, 10)]
    assert estimate == [Fraction(1, 5), Fraction(1, 2), Fraction(3, 10)]
    assert residual == [Fraction(1, 100), Fraction(-1, 100), 0, Fraction(-1, 100), Fraction(1, 100)]
    assert residual_projection == [0, 0, 0]
    assert sum(value * value for value in residual) == Fraction(1, 2500)


def test_project_transition_basis_and_stationary_values_recompute():
    p = [0.2, 0.5, 0.3]
    transition = [[0.8, 0.1, 0.1], [0.1, 0.8, 0.1], [0.1, 0.1, 0.8]]
    propagated = [sum(transition[i][j] * p[j] for j in range(3)) for i in range(3)]
    stationary = [1 / 3] * 3
    q0 = [1 / math.sqrt(3)] * 3
    q1 = [1 / math.sqrt(2), -1 / math.sqrt(2), 0]
    q2 = [1 / math.sqrt(6), 1 / math.sqrt(6), -2 / math.sqrt(6)]
    coordinates = [sum(q[i] * p[i] for i in range(3)) for q in (q0, q1, q2)]
    next_coordinates = [sum(q[i] * propagated[i] for i in range(3)) for q in (q0, q1, q2)]

    assert all(math.isclose(sum(row), 1.0) for row in transition)
    assert all(math.isclose(sum(transition[i][j] for i in range(3)), 1.0) for j in range(3))
    assert all(math.isclose(propagated[i], value) for i, value in enumerate((0.24, 0.45, 0.31)))
    assert all(math.isclose(sum(transition[i][j] * stationary[j] for j in range(3)), stationary[i]) for i in range(3))
    assert math.isclose(coordinates[0], next_coordinates[0], abs_tol=1e-12)
    assert math.isclose(next_coordinates[1], 0.7 * coordinates[1], abs_tol=1e-12)
    assert math.isclose(next_coordinates[2], 0.7 * coordinates[2], abs_tol=1e-12)


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/hidden-state-reconstruction-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
