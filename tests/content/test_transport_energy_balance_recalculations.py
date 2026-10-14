"""Separate numerical checks of the steady-flow energy-balance lesson.

Efflux speed comes from an RK4 free-fall simulation, constriction pressure from
integrating dP = -rho v dv, Poiseuille losses from integrating the parabolic
velocity profile and bisecting for the pressure drop, and feed height from
bisection on a hydrostatic integral. The shared registry in
test_ai_assisted_checks.py checks the closed forms. The same AI assistant
authored content and checks; this is not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/transport"
LESSON = COURSE / "modules/16-steady-flow-energy-balances-bernoulli-and-friction-losses.md"
RHO, G, CP = 1000.0, 9.81, 4180.0


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


def simpson(f, a, b, panels=2000):
    h = (b - a) / panels
    return h / 3 * math.fsum(
        (1 if i in (0, panels) else 4 if i % 2 else 2) * f(a + i * h) for i in range(panels + 1)
    )


def hydrostatic_pressure(height):
    return simpson(lambda z: RHO * G, 0.0, height, 200)


def frictionless_drop_speed(height, dt=1e-5):
    """Step a parcel falling freely from rest (dv/dt = g, dz/dt = v) until it has dropped the height."""
    z, v = 0.0, 0.0
    while True:
        z_next = z + v * dt + 0.5 * G * dt * dt
        if z_next >= height:
            # Interpolate the speed at the exact height within the last step.
            return v + G * dt * (height - z) / (z_next - z)
        z, v = z_next, v + G * dt


def bernoulli_drop(flow, d1, d2):
    v1, v2 = flow / (math.pi * d1**2 / 4), flow / (math.pi * d2**2 / 4)
    return simpson(lambda v: RHO * v, v1, v2, 400)


def laminar_flow(dp, mu, length, diameter):
    radius = diameter / 2
    return simpson(
        lambda r: 2 * math.pi * r * dp * (radius**2 - r**2) / (4 * mu * length), 0.0, radius, 400
    )


def poiseuille_loss(flow, mu, length, diameter):
    return bisect(lambda dp: laminar_flow(dp, mu, length, diameter) - flow, 0.0, 1e6)


def expected_answers():
    p = "transport-16:"
    q = 5e-6 / 60
    loss = poiseuille_loss(q, 0.90e-3, 0.50, 1.0e-3)
    return {
        p + "stream-heating": RHO * 15e-6 / 60 * CP * (37 - 25),
        p + "feed-height": bisect(lambda h: hydrostatic_pressure(h) - 50 * 133.322, 0.0, 2.0),
        p + "efflux-speed": frictionless_drop_speed(0.80),
        p + "constriction-drop": bernoulli_drop(2e-6, 3.0e-3, 1.5e-3),
        p + "poiseuille-loss": loss,
        p + "tubing-reynolds": RHO * (q / (math.pi * 1e-6 / 4)) * 1e-3 / 0.90e-3,
        p + "pump-hydraulic-power": (loss + hydrostatic_pressure(0.20)) * q * 1e3,
        p + "viscous-heating": 2000 / (RHO * CP) * 1e3,
    }


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_energy_balance_keys_with_separate_methods(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(EXPECTED[question_id], abs=spec["tolerance"])


def test_energy_balance_numeric_inventory_is_exhaustive():
    numeric = {key for key, q in BANK.items() if key.startswith("transport-16:") and q["type"] == "numeric"}
    assert numeric == set(EXPECTED) and len(EXPECTED) == 8


def test_energy_balance_lesson_statements_match_numerical_models():
    text = LESSON.read_text(encoding="utf-8")
    q = 10e-6 / 60
    assert round(RHO * q * CP * 15, 1) == 10.4 or round(RHO * q * CP * 15, 2) == 10.45
    assert round(hydrostatic_pressure(0.50)) == 4905 and round(hydrostatic_pressure(0.50) / 133.322, 1) == 36.8
    assert round(frictionless_drop_speed(0.50), 2) == 3.13
    assert round(bernoulli_drop(5e-6, 4e-3, 2e-3)) == 1187
    loss = poiseuille_loss(q, 0.80e-3, 2.0, 1.6e-3)
    assert round(loss) == 1658
    v = q / (math.pi * 1.6e-3**2 / 4)
    assert round(v, 3) == 0.083 and round(RHO * v * 1.6e-3 / 0.80e-3, -1) == 170
    assert round(0.5 * RHO * v * v, 1) == 3.4
    assert round((loss + hydrostatic_pressure(0.30)) * q * 1e3, 2) == 0.77
    assert round(loss / (RHO * CP), 4) == 0.0004
    q2 = 20e-6 / 60
    worked_loss = poiseuille_loss(q2, 1.0e-3, 1.5, 2.0e-3)
    assert round(RHO * q2 * CP * 17, 1) == 23.7 and round(worked_loss) == 1273
    hydraulic = (worked_loss + hydrostatic_pressure(0.50)) * q2
    assert round(hydraulic * 1e3, 2) == 2.06 and round(hydraulic / 0.25 * 1e3, 2) == 8.24
    for phrase in (
        "ṁ c_p ΔT is **10.5 W**",
        "supplies 1000 × 9.81 × 0.50 = **4.9 kPa**, about **36.8 mmHg**",
        "which is **3.13 m/s** for h = 0.50 m",
        "½ρ(v₂² − v₁²) = **1.19 kPa**",
        "The friction loss is **1.66 kPa**",
        "a hydraulic power of **0.77 mW**",
        "about 0.0004 K here",
        "= 23.7 W",
        "= 1.27 kPa",
        "the input is 8.24 mW",
    ):
        assert phrase in text, phrase
