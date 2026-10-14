"""Separate numerical checks of the multiaxial strain, thermal-stress and vessel lesson.

Strains come from solving the isotropic stiffness relation (Lamé constants) by
Gaussian elimination rather than the compliance formula; thermal stresses from
bisection on a length-compatibility condition; vessel stresses from integrating
the pressure over a cut. The same AI assistant authored content and checks;
this is not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statics-materials"
LESSON = COURSE / "modules/15-multiaxial-hookes-law-thermal-strain-and-pressure-vessels.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def solve(matrix, rhs):
    a = [row[:] + [b] for row, b in zip(matrix, rhs)]
    n = len(a)
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[pivot] = a[pivot], a[col]
        for r in range(n):
            if r != col:
                factor = a[r][col] / a[col][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[col])]
    return [a[i][n] / a[i][i] for i in range(n)]


def stiffness(e, nu):
    lam = e * nu / ((1 + nu) * (1 - 2 * nu))
    mu = e / (2 * (1 + nu))
    return [[lam + 2 * mu if i == j else lam for j in range(3)] for i in range(3)]


def strains(stress, e, nu):
    """Solve sigma = C eps for the normal strains."""
    return solve(stiffness(e, nu), list(stress))


def bisect(f, low, high):
    for _ in range(100):
        mid = (low + high) / 2
        if f(low) * f(mid) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def constrained_stress(e, alpha, rise, length, gap):
    """Stress that makes free thermal plus elastic extension equal the gap (or zero if it fits)."""
    free = alpha * rise * length
    if free <= gap:
        return 0.0
    return bisect(lambda s: free + s / e * length - gap, -10 * e * alpha * rise, 0.0)


def lateral_stress(sigma_x, e, nu):
    return bisect(lambda s: strains((sigma_x, s, 0.0), e, nu)[1], -sigma_x, sigma_x)


def hoop_from_cut(p, r, t, panels=4000):
    """Half-cylinder: integrate the vertical pressure component, then share it between two walls."""
    h = math.pi / panels
    force = math.fsum(p * r * math.sin((i + 0.5) * h) * h for i in range(panels))
    return force / (2 * t)


def axial_from_cut(p, r, t, rings=4000):
    h = r / rings
    end_force = math.fsum(p * 2 * math.pi * (i + 0.5) * h * h for i in range(rings))
    return end_force / (2 * math.pi * r * t)


def expected_answers():
    p = "statics-materials-15:"
    hoop, axial = hoop_from_cut(1.2, 0.40, 0.008), axial_from_cut(1.2, 0.40, 0.008)
    return {
        p + "biaxial-strain": strains((60, -40, 0), 100_000, 0.25)[0] * 1e4,
        p + "lateral-diameter-change": strains((150, 0, 0), 200_000, 0.30)[1] * 10e3,
        p + "constrained-thermal-stress": constrained_stress(70_000, 23e-6, 40, 1000.0, 0.0),
        p + "gap-thermal-stress": constrained_stress(200_000, 12e-6, 60, 2000.0, 0.80),
        p + "lateral-constraint-stress": lateral_stress(80, 200_000, 0.30),
        p + "hoop-stress": hoop,
        p + "sphere-stress": axial_from_cut(1.2, 0.40, 0.008),
        p + "vessel-radius-growth": strains((hoop, axial, 0), 200_000, 0.30)[0] * 400,
    }


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_multiaxial_keys_with_separate_methods(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(EXPECTED[question_id], abs=spec["tolerance"])


def test_multiaxial_numeric_inventory_is_exhaustive():
    numeric = {
        key
        for key, q in BANK.items()
        if key.startswith("statics-materials-15:") and q["type"] == "numeric"
    }
    assert numeric == set(EXPECTED) and len(EXPECTED) == 8


def test_multiaxial_lesson_statements_match_stiffness_solutions():
    text = LESSON.read_text(encoding="utf-8")
    rod = strains((80, 0, 0), 70_000, 0.33)
    assert round(rod[0] * 1e3, 3) == 1.143 and round(rod[1] * 1e4, 2) == -3.77
    assert round(-rod[1] * 20e3, 1) == 7.5
    plate = strains((100, 50, 0), 200_000, 0.30)
    assert [round(x * 1e4, 2) for x in plate] == [4.25, 1.0, -2.25]
    assert round(sum(plate) * 1e4, 2) == 3.0
    assert lateral_stress(100, 200_000, 0.30) == pytest.approx(30)
    assert strains((100, 30, 0), 200_000, 0.30)[0] == pytest.approx(4.55e-4)
    assert constrained_stress(200_000, 12e-6, 50, 1000.0, 0.0) == pytest.approx(-120)
    assert constrained_stress(200_000, 12e-6, 50, 1000.0, 0.10) == pytest.approx(-100)
    assert constrained_stress(200_000, 12e-6, 50, 1000.0, 0.70) == 0.0
    hoop, axial = hoop_from_cut(2.0, 0.50, 0.010), axial_from_cut(2.0, 0.50, 0.010)
    assert (round(hoop, 3), round(axial, 3)) == (100.0, 50.0)
    assert round(strains((hoop, axial, 0), 200_000, 0.30)[0] * 500, 2) == 0.21
    tank = 1.5 * 0.30 / 120
    assert round(tank * 1e3, 2) == 3.75 and round(0.30 / tank) == 80
    th, ax = hoop_from_cut(1.5, 0.30, tank), axial_from_cut(1.5, 0.30, tank)
    eps = strains((th, ax, 0), 200_000, 0.30)
    assert (round(eps[0] * 1e4, 2), round(eps[1] * 1e4, 2)) == (5.1, 1.2)
    assert round((2 * eps[0] + eps[1]) * 1e3, 2) == 1.14
    for phrase in (
        "the diameter shrinks by **7.5 μm**",
        "= **4.25 × 10⁻⁴**",
        "σ_y = νσ_x = **30 MPa**",
        "the constrained stress is **−120 MPa**",
        "σ = −200 000 × 0.50/1000 = **−100 MPa**",
        "The hoop stress is **100 MPa** and the axial stress **50 MPa**",
        "= **0.21 mm**",
        "t ≥ 1.5 × 0.30/120 = 3.75 mm",
        "2ε_θ + ε_z = 1.14 × 10⁻³",
        "Nothing here is a design basis, pressure rating, test protocol or safety assessment",
    ):
        assert phrase in text, phrase


def test_multiaxial_unit_is_grouped_with_combined_stress():
    manifest = load(COURSE / "course.json")
    week = next(w for w in manifest["duration"]["weeks"] if w["week"] == 7)
    assert week["lesson_ids"] == ["statics-materials-10", "statics-materials-15"]
    assert manifest["maturity"] == "partial"
    assert manifest["grading_policy"]["mode"] == "formative-only"
