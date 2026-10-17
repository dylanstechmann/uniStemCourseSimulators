"""Regression checks for the Signals & Control impedance-modeling reading.

Each numeric key is recomputed by a different route from the closed form in its feedback: step responses are
simulated, the corner frequency is found by bisection on the magnitude, and natural frequencies and damping ratios
come from the poles of the derived characteristic polynomial.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/signals-control"
LESSON = "signals-control-16"


def _manifest() -> dict:
    return json.loads((COURSE / "course.json").read_text(encoding="utf-8"))


def _practice() -> dict[str, dict]:
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    return {question["id"]: question for question in bank["questions"]}


def _rk4(derivative, state, dt, steps):
    """Integrate dx/dt = derivative(x) with fixed-step RK4 and return every state."""
    states = [state]
    for _ in range(steps):
        k1 = derivative(state)
        k2 = derivative([s + dt / 2 * k for s, k in zip(state, k1)])
        k3 = derivative([s + dt / 2 * k for s, k in zip(state, k2)])
        k4 = derivative([s + dt * k for s, k in zip(state, k3)])
        state = [s + dt / 6 * (a + 2 * b + 2 * c + d) for s, a, b, c, d in zip(state, k1, k2, k3, k4)]
        states.append(state)
    return states


def _time_to_reach(values, dt, target):
    """First time a rising response reaches target, by linear interpolation between steps."""
    for i in range(1, len(values)):
        if values[i] >= target:
            return dt * (i - 1 + (target - values[i - 1]) / (values[i] - values[i - 1]))
    raise AssertionError("response never reached the target")


def _second_order_from_poles(a2, a1, a0):
    """Natural frequency and damping ratio of a2 s² + a1 s + a0 from its complex poles."""
    pole = (-a1 + cmath.sqrt(a1 * a1 - 4 * a2 * a0)) / (2 * a2)
    return abs(pole), -pole.real / abs(pole)


def _rc_time_constant_ms(r, c):
    # A unit input step settles at 1 V (the capacitor draws no current at s = 0); time it to 1 - 1/e of that.
    dt = 1e-5
    values = [s[0] for s in _rk4(lambda v: [(1.0 - v[0]) / (r * c)], [0.0], dt, 60_000)]
    return 1000 * _time_to_reach(values, dt, 1 - math.exp(-1))


def _rc_corner_hz(r, c):
    low, high = 1.0, 1e5
    for _ in range(200):
        mid = (low + high) / 2
        if abs(1 / (1 + 1j * 2 * math.pi * mid * r * c)) > 1 / math.sqrt(2):
            low = mid
        else:
            high = mid
    return (low + high) / 2


def _msd_final_deflection_mm(m, b, k, force):
    states = _rk4(lambda s: [s[1], (force - b * s[1] - k * s[0]) / m], [0.0, 0.0], 1e-4, 100_000)
    return 1000 * states[-1][0]


def _thermal_capacitance(r_th, tau_s):
    """Find C_th by bisection so that a simulated heater step reaches 63.2% of its rise at tau_s."""

    def rise_time(c_th):
        # A 1 W step settles at a rise of r_th kelvin; simulate well past the trial time constant.
        dt = 0.5
        steps = int(5 * r_th * c_th / dt) + 10
        values = [s[0] for s in _rk4(lambda t: [(1.0 - t[0] / r_th) / c_th], [0.0], dt, steps)]
        return _time_to_reach(values, dt, (1 - math.exp(-1)) * r_th)

    low, high = 100.0, 10_000.0
    for _ in range(60):
        mid = (low + high) / 2
        low, high = (mid, high) if rise_time(mid) < tau_s else (low, mid)
    return (low + high) / 2


NUMERIC_KEYS = {
    "signals-control-16:rc-time-constant": _rc_time_constant_ms(20e3, 4.7e-6),
    "signals-control-16:rc-corner-hz": _rc_corner_hz(10e3, 100e-9),
    "signals-control-16:rlc-natural-frequency": _second_order_from_poles(25e-3 * 10e-6, 20 * 10e-6, 1)[0],
    "signals-control-16:rlc-damping-ratio": _second_order_from_poles(25e-3 * 10e-6, 20 * 10e-6, 1)[1],
    "signals-control-16:msd-static-deflection": _msd_final_deflection_mm(1.5, 12, 300, 6),
    "signals-control-16:msd-natural-frequency": _second_order_from_poles(4, 36, 900)[0],
    "signals-control-16:msd-damping-ratio": _second_order_from_poles(4, 36, 900)[1],
    "signals-control-16:thermal-capacitance": _thermal_capacitance(0.8, 15 * 60),
}

CHOICE_KEYS = {
    "signals-control-16:impedance-forms": "R, 1/(sC), sL; and b, k/s, ms",
    "signals-control-16:static-check": "Setting s = 0 gives 1/k",
    "signals-control-16:spring-analog": "A capacitor with C = 1/k",
    "signals-control-16:thermal-no-overshoot": "rises without overshoot",
}


def test_impedance_reading_is_delivered_in_week_5_and_bounded():
    manifest = _manifest()
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    module = next(module for module in manifest["modules"] if module["id"] == "signals-control-module-16")
    assert [lesson["id"] for lesson in module["lessons"]] == [LESSON]
    week5 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 5)
    assert week5["lesson_ids"] == ["signals-control-8", LESSON]
    assert week5["assessment_ids"] == ["signals-control-8-practice", f"{LESSON}-practice"]
    text = (COURSE / module["lessons"][0]["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "**Z = 1/(sC)**",
        "**Z = k/s**",
        "**Z = ms**",
        "**C = 1/k**",
        "**X/F = 1/(ms² + bs + k),**",
        "**ΔT/U = R_th/(R_th C_th s + 1).**",
        "heat has no inertia",
        "2.004",
        "Limits of this lesson",
    ):
        assert phrase in text, phrase


def test_impedance_numeric_keys_match_independent_recalculation():
    practice = _practice()
    numeric = {key for key, item in practice.items() if key.startswith(LESSON + ":") and item["type"] == "numeric"}
    assert numeric == set(NUMERIC_KEYS)
    for key, expected in NUMERIC_KEYS.items():
        spec = practice[key]["solution_spec"]
        assert abs(spec["answer"] - expected) <= spec["tolerance"], (key, spec["answer"], expected)


def test_lesson_numbers_agree_with_simulation_and_poles():
    text = (COURSE / "modules/16-impedance-models-of-electrical-mechanical-and-thermal-plants.md").read_text(encoding="utf-8")
    # RC example: 10 kOhm and 10 uF.
    assert round(_rc_time_constant_ms(10e3, 10e-6) / 1000, 3) == 0.1 and "τ = 0.1 s" in text
    assert round(_rc_corner_hz(10e3, 10e-6), 2) == 1.59 and "1.59 Hz" in text
    # RLC example: 10 mH, 1 uF and 50 Ohm.
    wn, zeta = _second_order_from_poles(10e-3 * 1e-6, 50 * 1e-6, 1)
    assert round(wn) == 10_000 and round(zeta, 3) == 0.25 and "ωn = 10,000 rad/s and ζ = 0.25" in text
    # Mass-spring-damper example: 2 kg, 800 N/m and 16 N s/m.
    wn, zeta = _second_order_from_poles(2, 16, 800)
    assert round(wn, 6) == 20 and round(zeta, 6) == 0.2
    assert round(_msd_final_deflection_mm(2, 16, 800, 1), 3) == 1.25 and "1.25 mm/N" in text
    # Incubator: K = 0.5 K/W and tau = 10 min.
    assert abs(_thermal_capacitance(0.5, 600) - 1200) < 1 and "1,200 J/K" in text


def test_worked_example_overshoot_matches_a_simulated_step():
    m, b, k = 0.5, 3.0, 50.0
    wn, zeta = _second_order_from_poles(m, b, k)
    assert round(wn, 6) == 10 and round(zeta, 6) == 0.3
    states = _rk4(lambda s: [s[1], (k - b * s[1] - k * s[0]) / m], [0.0, 0.0], 1e-4, 40_000)
    overshoot = max(s[0] for s in states) - 1.0
    assert abs(overshoot - math.exp(-math.pi * zeta / math.sqrt(1 - zeta**2))) < 1e-4
    text = (COURSE / "modules/16-impedance-models-of-electrical-mechanical-and-thermal-plants.md").read_text(encoding="utf-8")
    assert f"{100 * overshoot:.1f}%" == "37.2%" and "**37.2%**" in text
    assert "**20 mm/N**" in text and "**10 rad/s**" in text and "**0.3**" in text


def test_passive_thermal_chain_rises_without_overshoot():
    # Heater block -> chamber -> sensor, each a capacitance joined by resistances, the chamber losing heat to the room.
    c_block, c_chamber, c_sensor = 300.0, 1200.0, 20.0
    r_block, r_room, r_sensor = 0.2, 0.5, 2.0

    def derivative(t):
        block, chamber, sensor = t
        q_block = (block - chamber) / r_block
        q_sensor = (chamber - sensor) / r_sensor
        return [(10.0 - q_block) / c_block,
                (q_block - chamber / r_room - q_sensor) / c_chamber,
                q_sensor / c_sensor]

    states = _rk4(derivative, [0.0, 0.0, 0.0], 0.5, 60_000)
    sensor = [s[2] for s in states]
    assert all(later >= earlier - 1e-12 for earlier, later in zip(sensor, sensor[1:]))
    assert abs(sensor[-1] - 10.0 * r_room) < 1e-3  # steady rise is heater power times the loss resistance


def test_impedance_choice_keys_point_at_the_correct_option():
    practice = _practice()
    choice = {key for key, item in practice.items() if key.startswith(LESSON + ":") and item["type"] == "single_choice"}
    assert choice == set(CHOICE_KEYS)
    for key, phrase in CHOICE_KEYS.items():
        options = practice[key]["options"]
        assert phrase in options[practice[key]["solution_spec"]["answer"]], key
        assert sum(phrase in option for option in options) == 1, key


def test_impedance_assessment_lesson_and_cards_are_linked():
    manifest = _manifest()
    practice = _practice()
    items = [key for key in practice if key.startswith(LESSON + ":")]
    assessment = next(item for item in manifest["assessments"] if item["id"] == f"{LESSON}-practice")
    assert assessment["question_ids"] == items
    assert assessment["points"] == sum(practice[key]["points"] for key in items)
    lesson = next(lesson for module in manifest["modules"] for lesson in module["lessons"] if lesson["id"] == LESSON)
    assert lesson["question_ids"] == items
    objectives = {objective["id"] for objective in manifest["lesson_objectives"]}
    cards = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
    new_cards = [card for card in cards if card["lesson_id"] == LESSON]
    assert len(new_cards) == 4 and lesson["card_ids"] == [card["id"] for card in new_cards]
    covered = {objective for card in new_cards for objective in card["objective_ids"]}
    assert covered <= objectives and covered == {f"{LESSON}-objective-{n}" for n in range(1, 4)}
