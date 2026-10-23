"""Separate numerical checks of the impulse, convolution and transfer-function lesson.

Impulse responses come from RK4 integration with the velocity-jump initial
condition, convolutions from Simpson quadrature, and gains from a real 2x2
solve for the particular-solution coefficients rather than |p(iw)|. The same AI
assistant authored content and checks; this is not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/differential-equations"
LESSON = COURSE / "modules/15-impulse-response-convolution-and-transfer-functions.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def rk4(rhs, state, t_end, steps=4000, forcing=lambda t: 0.0):
    h, t = t_end / steps, 0.0
    state = list(state)
    for _ in range(steps):
        k1 = rhs(t, state, forcing)
        k2 = rhs(t + h / 2, [s + h / 2 * k for s, k in zip(state, k1)], forcing)
        k3 = rhs(t + h / 2, [s + h / 2 * k for s, k in zip(state, k2)], forcing)
        k4 = rhs(t + h, [s + h * k for s, k in zip(state, k3)], forcing)
        state = [
            s + h / 6 * (a + 2 * b + 2 * c + d)
            for s, a, b, c, d in zip(state, k1, k2, k3, k4)
        ]
        t += h
    return state


def second_order(b, k):
    return lambda t, s, f: [s[1], f(t) - b * s[1] - k * s[0]]


def first_order(k):
    return lambda t, s, f: [f(t) - k * s[0]]


def impulse_response_2(b, k, t):
    """Free motion after a unit velocity jump: x(0) = 0, x'(0+) = 1."""
    return rk4(second_order(b, k), (0.0, 1.0), t)[0]


def simpson(f, a, b, panels=2000):
    h = (b - a) / panels
    return (
        h
        / 3
        * math.fsum(
            (1 if i in (0, panels) else 4 if i % 2 else 2) * f(a + i * h)
            for i in range(panels + 1)
        )
    )


def convolve(w, f, t, upper=None):
    return simpson(lambda u: w(t - u) * f(u), 0.0, t if upper is None else upper)


def particular(b, k, omega):
    """Solve for A cos + B sin in x'' + b x' + k x = cos(omega t)."""
    a11, a12 = k - omega**2, b * omega
    a21, a22 = -b * omega, k - omega**2
    det = a11 * a22 - a12 * a21
    return a22 / det, -a21 / det


def gain(b, k, omega):
    return math.hypot(*particular(b, k, omega))


def lag_degrees(b, k, omega):
    a, s = particular(b, k, omega)
    return math.degrees(math.atan2(s, a))


def peak_frequency(b, k):
    low, high = 0.0, math.sqrt(k)
    ratio = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        x1, x2 = high - ratio * (high - low), low + ratio * (high - low)
        if gain(b, k, x1) > gain(b, k, x2):
            high = x2
        else:
            low = x1
    return (low + high) / 2


def pulse_velocity(mass, impulse, width=1e-4):
    """Apply force impulse/width for a short time to a resting mass on a spring and damper."""
    state = rk4(
        lambda t, s, f: [s[1], (f(t) - 3 * s[1] - 20 * s[0]) / mass],
        (0.0, 0.0),
        width,
        steps=200,
        forcing=lambda t: impulse / width,
    )
    return state[1]


def expected_answers():
    p = "differential-equations-15:"
    return {
        p + "first-order-impulse-response": rk4(first_order(3), (1.0,), 0.5)[0],
        p + "velocity-jump": pulse_velocity(4, 2),
        p + "second-order-impulse-response": impulse_response_2(6, 25, 0.25),
        p + "ramp-convolution": convolve(lambda s: math.exp(-s), lambda u: u, 2),
        p + "pulse-convolution": convolve(
            lambda s: math.exp(-2 * s), lambda u: 1.0, 2, upper=1
        ),
        p + "gain-at-four": gain(6, 25, 4),
        p + "phase-lag-at-four": lag_degrees(6, 25, 4),
        p + "peak-gain-frequency": peak_frequency(6, 25),
    }


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_transfer_keys_with_separate_methods(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(EXPECTED[question_id], abs=spec["tolerance"])


def test_transfer_numeric_inventory_is_exhaustive():
    numeric = {
        key
        for key, q in BANK.items()
        if key.startswith("differential-equations-15:") and q["type"] == "numeric"
    }
    assert numeric == set(EXPECTED) and len(EXPECTED) == 8


def test_transfer_lesson_statements_match_simulation_and_quadrature():
    text = LESSON.read_text(encoding="utf-8")
    times = [i * 0.001 for i in range(1, 1000)]
    blow = [0.5 * impulse_response_2(4, 13, t) for t in times[::10]]
    peak = max(range(len(blow)), key=blow.__getitem__)
    assert times[::10][peak] == pytest.approx(0.328, abs=0.006)
    assert round(max(blow), 4) == pytest.approx(0.0720, abs=1e-4)
    step = rk4(first_order(2), (0.0,), 1.0, forcing=lambda t: 1.0)[0]
    assert round(step, 3) == 0.432
    ramp = rk4(first_order(2), (0.0,), 1.0, forcing=lambda t: t)[0]
    assert ramp == pytest.approx(
        convolve(lambda s: math.exp(-2 * s), lambda u: u, 1)
    ) and round(ramp, 4) == 0.2838
    assert round(gain(4, 13, 3), 4) == 0.0791 and round(lag_degrees(4, 13, 3), 1) == 71.6
    assert peak_frequency(4, 13) == pytest.approx(math.sqrt(5), abs=1e-6)
    assert gain(4, 13, math.sqrt(5)) == pytest.approx(1 / 12)
    assert gain(4, 13, 0) == pytest.approx(1 / 13)
    assert round(impulse_response_2(2, 10, 0.5), 4) == 0.2017
    assert round(gain(2, 10, 3), 4) == 0.1644 and round(lag_degrees(2, 10, 3), 1) == 80.5
    assert peak_frequency(2, 10) == pytest.approx(math.sqrt(8), abs=1e-6)
    assert gain(2, 10, math.sqrt(8)) == pytest.approx(1 / 6)
    for phrase in (
        "equals **0.0720**",
        "which is **0.432** at t = 1",
        "0.5 − 0.25 + 0.0338 = **0.2838**",
        "the gain at ω = 3 is **0.0791** and the phase lag is arctan(12/4) = **71.6°**",
        "**ω_r = √5 ≈ 2.236** and the peak gain is 1/12 = 0.0833",
        "w = (1/3)(0.6065)(0.9975) = 0.2017",
        "The gain is 0.1644 and the lag is arctan 6 = 80.5°",
        "ω_r = √(10 − 2²/2) = √8 = 2.828",
    ):
        assert phrase in text, phrase


def test_transfer_unit_is_grouped_with_the_laplace_week():
    manifest = load(COURSE / "course.json")
    week = next(w for w in manifest["duration"]["weeks"] if w["week"] == 6)
    assert week["lesson_ids"] == ["differential-equations-14", "differential-equations-15", "differential-equations-17"]
    assert manifest["maturity"] == "partial"
    assert manifest["grading_policy"]["mode"] == "formative-only"
