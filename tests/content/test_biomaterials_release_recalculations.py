"""Separate numerical checks of the controlled-release kinetics lesson.

Reservoir release is integrated as a membrane flux over time, Higuchi release by
a moving-front mass balance solved numerically, slab release from the exact
Fickian series, and first-order release by RK4. The shared registry in
test_ai_assisted_checks.py checks the closed forms. The same AI assistant
authored content and checks; this is not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biomaterials"
LESSON = COURSE / "modules/15-controlled-release-reservoirs-matrices-and-release-exponents.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def bisect(f, low, high):
    assert f(low) * f(high) <= 0
    for _ in range(100):
        mid = (low + high) / 2
        if f(low) * f(mid) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def reservoir_released(area, d, k, cs, h, seconds, steps=1000):
    """Sum the membrane flux (linear profile, sink outside) over time."""
    dt = seconds / steps
    return math.fsum(area * d * k * (cs - 0.0) / h * dt for _ in range(steps))


def higuchi_time(d, loading, cs, q, panels=200):
    """Pseudo-steady front: dQ/dt = D Cs (A - Cs/2)/Q, so t(Q) is the Simpson integral of dt/dQ."""
    h = q / panels

    def inverse_rate(value):
        return value / (d * cs * (loading - cs / 2))

    return h / 3 * math.fsum(
        (1 if i in (0, panels) else 4 if i % 2 else 2) * inverse_rate(i * h)
        for i in range(panels + 1)
    )


def higuchi_released(d, loading, cs, seconds):
    return bisect(lambda q: higuchi_time(d, loading, cs, q) - seconds, 0.0, 1e3)


def slab_fraction(d, thickness, seconds, terms=400):
    """Exact Crank series for a slab releasing from both faces."""
    total = 0.0
    for n in range(terms):
        m = 2 * n + 1
        total += 8 / (m * m * math.pi**2) * math.exp(-d * m * m * math.pi**2 * seconds / thickness**2)
    return 1 - total


def first_order_fraction(k, t, steps=2000):
    remaining, dt = 1.0, t / steps
    for _ in range(steps):
        k1 = -k * remaining
        k2 = -k * (remaining + dt / 2 * k1)
        k3 = -k * (remaining + dt / 2 * k2)
        k4 = -k * (remaining + dt * k3)
        remaining += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return 1 - remaining


def fitted_exponent(t1, f1, t2, f2):
    """Least-squares slope through two points on log-log axes."""
    xs, ys = [math.log(t1), math.log(t2)], [math.log(f1), math.log(f2)]
    mx, my = sum(xs) / 2, sum(ys) / 2
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)


def expected_answers():
    p = "biomaterials-15:"
    per_hour = reservoir_released(1.5, 2.0e-7, 0.30, 6.0, 0.015, 3600)
    return {
        p + "reservoir-rate": per_hour,
        p + "reservoir-duration": bisect(lambda hours: reservoir_released(1.5, 2.0e-7, 0.30, 6.0, 0.015, hours * 3600, 50) - 20, 1, 1000),
        p + "higuchi-amount": higuchi_released(2.0e-6, 40.0, 1.0, 2 * 86400),
        p + "higuchi-time-factor": higuchi_time(
            2.0e-6, 40.0, 1.0, 3 * higuchi_released(2.0e-6, 40.0, 1.0, 86400)
        )
        / 86400,
        p + "slab-diffusivity": bisect(lambda d: slab_fraction(d, 0.20, 7200) - 0.30, 1e-9, 1e-6) * 1e8,
        p + "first-order-percent": first_order_fraction(0.05, 24) * 100,
        p + "first-order-half-time": bisect(lambda t: first_order_fraction(0.05, t, 400) - 0.5, 1, 50),
        p + "release-exponent": fitted_exponent(1.0, 0.10, 4.0, 0.30),
    }


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_release_keys_with_separate_methods(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(EXPECTED[question_id], abs=spec["tolerance"])


def test_release_numeric_inventory_is_exhaustive():
    numeric = {
        key for key, q in BANK.items() if key.startswith("biomaterials-15:") and q["type"] == "numeric"
    }
    assert numeric == set(EXPECTED) and len(EXPECTED) == 8


def test_release_lesson_statements_match_numerical_models():
    text = LESSON.read_text(encoding="utf-8")
    hourly = reservoir_released(2.0, 1.0e-7, 0.50, 10.0, 0.010, 3600)
    assert round(hourly, 2) == 0.36 and round(50 / hourly) == 139
    assert round(higuchi_released(1.0e-6, 50.0, 2.0, 86400), 2) == 4.12
    assert round(higuchi_released(1.0e-6, 50.0, 2.0, 4 * 86400), 2) == 8.23
    d = bisect(lambda dd: slab_fraction(dd, 0.10, 3600) - 0.20, 1e-10, 1e-6)
    assert round(d * 1e8, 1) == 2.2
    assert round(first_order_fraction(0.10, 12), 2) == 0.70
    assert round(bisect(lambda t: first_order_fraction(0.10, t, 400) - 0.5, 1, 30), 1) == 6.9
    assert round(fitted_exponent(1, 0.20, 4, 0.40), 2) == 0.50
    worked = reservoir_released(3.0, 5.0e-8, 0.40, 8.0, 0.020, 3600)
    assert round(worked, 4) == 0.0864 and round(1 / worked, 1) == 11.6
    assert round(fitted_exponent(1, 0.30, 3, 0.45), 2) == 0.37
    for phrase in (
        "or **0.36 mg/h**",
        "= **139 h**",
        "Q is **4.12 mg/cm²** after one day and **8.23 mg/cm²** after four",
        "= **2.2 × 10⁻⁸ cm²/s**",
        "70% is released after 12 h and the half-time is 6.9 h",
        "n = log(0.40/0.20)/log 4 = **0.50**",
        "= 0.0864 mg/h",
        "about 11.6 h",
        "n = log(0.45/0.30)/log 3 = 0.37",
        "Nothing here is a formulation, dosing schedule, release specification or clinical recommendation",
    ):
        assert phrase in text, phrase
