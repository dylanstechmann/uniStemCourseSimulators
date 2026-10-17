"""Regression checks for the Physiology Hodgkin-Huxley reading.

Numeric keys are recomputed by integrating the gating equations rather than by the closed forms in their feedback,
and the spike, threshold and refractory numbers stated in the reading come from a simulation of the full classic
model (squid axon, 6.3 degC, written with a -65 mV rest) with fixed-step RK4 at 0.01 ms.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physiology"
LESSON = "physiology-16"
READING = COURSE / "modules/16-voltage-gated-conductances-and-the-hodgkin-huxley-action-potential.md"

G_NA, G_K, G_L = 120.0, 36.0, 0.3
E_NA, E_K, E_L = 50.0, -77.0, -54.387
DT = 0.01  # ms


def _manifest() -> dict:
    return json.loads((COURSE / "course.json").read_text(encoding="utf-8"))


def _practice() -> dict[str, dict]:
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    return {question["id"]: question for question in bank["questions"]}


def _rates(v):
    an = 0.01 * (v + 55) / (1 - math.exp(-(v + 55) / 10))
    bn = 0.125 * math.exp(-(v + 65) / 80)
    am = 0.1 * (v + 40) / (1 - math.exp(-(v + 40) / 10))
    bm = 4 * math.exp(-(v + 65) / 18)
    ah = 0.07 * math.exp(-(v + 65) / 20)
    bh = 1 / (1 + math.exp(-(v + 35) / 10))
    return an, bn, am, bm, ah, bh


def _gate_trajectory(alpha, beta, x0, t_end, dt=1e-3):
    """Integrate dx/dt = alpha(1 - x) - beta x with RK4 at a fixed voltage."""
    f = lambda x: alpha * (1 - x) - beta * x  # noqa: E731
    xs, x = [x0], x0
    for _ in range(int(round(t_end / dt))):
        k1 = f(x)
        k2 = f(x + dt / 2 * k1)
        k3 = f(x + dt / 2 * k2)
        k4 = f(x + dt * k3)
        x += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        xs.append(x)
    return xs


def _crossing_time(xs, target, dt=1e-3):
    for i in range(1, len(xs)):
        if (xs[i - 1] - target) * (xs[i] - target) <= 0 and xs[i] != xs[i - 1]:
            return dt * (i - 1 + (target - xs[i - 1]) / (xs[i] - xs[i - 1]))
    raise AssertionError("target not reached")


def _rest_gates():
    an, bn, am, bm, ah, bh = _rates(-65.0)
    return an / (an + bn), am / (am + bm), ah / (ah + bh)


def _derivative(state, i_stim):
    v, n, m, h = state
    an, bn, am, bm, ah, bh = _rates(v)
    i_ion = G_NA * m**3 * h * (v - E_NA) + G_K * n**4 * (v - E_K) + G_L * (v - E_L)
    return [-i_ion + i_stim, an * (1 - n) - bn * n, am * (1 - m) - bm * m, ah * (1 - h) - bh * h]


def _simulate(stimulus, t_end):
    """Space-clamped patch with C_m = 1 uF/cm2 starting at rest; returns rows (t, v, n, m, h)."""
    state = [-65.0, *_rest_gates()]
    rows, t = [(0.0, *state)], 0.0
    for _ in range(int(round(t_end / DT))):
        k1 = _derivative(state, stimulus(t))
        k2 = _derivative([s + DT / 2 * k for s, k in zip(state, k1)], stimulus(t + DT / 2))
        k3 = _derivative([s + DT / 2 * k for s, k in zip(state, k2)], stimulus(t + DT / 2))
        k4 = _derivative([s + DT * k for s, k in zip(state, k3)], stimulus(t + DT))
        state = [s + DT / 6 * (a + 2 * b + 2 * c + d) for s, a, b, c, d in zip(state, k1, k2, k3, k4)]
        t += DT
        rows.append((t, *state))
    return rows


def _pulse(start, width, amplitude):
    return lambda t: amplitude if start <= t < start + width else 0.0


def _spike_count(rows):
    count, above = 0, False
    for _, v, *_ in rows:
        if v > 0 and not above:
            count, above = count + 1, True
        elif v < -10:
            above = False
    return count


def _paired_pulses_fire_twice(delay, second_amplitude):
    first, second = _pulse(1.0, 1.0, 10.0), _pulse(1.0 + delay, 1.0, second_amplitude)
    return _spike_count(_simulate(lambda t: first(t) + second(t), 1.0 + delay + 15.0)) >= 2


_N_REST = _gate_trajectory(0.0582, 0.125, 0.0, 60.0)
_H_RECOVERY = _gate_trajectory(0.596 / 8.52, (1 - 0.596) / 8.52, 0.10, 20.0)

NUMERIC_KEYS = {
    # Net current divided by capacitance: 1 uA/uF is 1 mV/ms.
    "physiology-16:dvdt-net": -(-250 + 40 + 3) / 1.0,
    # The fixed point and the 63% time of the integrated gate, started from n = 0.
    "physiology-16:n-inf-rest": _N_REST[-1],
    "physiology-16:tau-n-rest": _crossing_time(_N_REST, (1 - math.exp(-1)) * _N_REST[-1]),
    "physiology-16:gk-rest": G_K * 0.318**4,
    # Integrate from n = 0.318 with rates that give n_inf = 0.909 and tau_n = 1.65 ms.
    "physiology-16:n-after-step": _gate_trajectory(0.909 / 1.65, (1 - 0.909) / 1.65, 0.318, 1.0)[-1],
    "physiology-16:gk-fold-rise": (0.587**4) / (0.318**4),
    "physiology-16:ina-instant": G_NA * 0.9**3 * 0.3 * (0.0 - E_NA),
    "physiology-16:h-recovery-time": _crossing_time(_H_RECOVERY, 0.40),
}

CHOICE_KEYS = {
    "physiology-16:voltage-clamp": "injected current equals the ionic current",
    "physiology-16:upstroke-order": "several times faster",
    "physiology-16:refractory-gates": "few sodium channels are available",
    "physiology-16:threshold-balance": "outruns the potassium and leak currents",
}


def test_hodgkin_huxley_reading_is_delivered_in_week_3_and_bounded():
    manifest = _manifest()
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"
    module = next(module for module in manifest["modules"] if module["id"] == "physiology-module-16")
    assert [lesson["id"] for lesson in module["lessons"]] == [LESSON]
    week3 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 3)
    assert week3["lesson_ids"] == ["physiology-2", LESSON]
    assert week3["assessment_ids"] == ["physiology-2-practice", f"{LESSON}-practice"]
    text = READING.read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "**C_m dV/dt = −(I_Na + I_K + I_L) + I_stim,**",
        "**g_K = ḡ_K n⁴ and g_Na = ḡ_Na m³h,**",
        "**x∞ = α_x/(α_x + β_x), with time constant τ_x = 1/(α_x + β_x),**",
        "https://doi.org/10.1113/jphysiol.1952.sp004764",
        "absolute refractory period",
        "relative refractory period",
        "Limits of this lesson",
    ):
        assert phrase in text, phrase


def test_hodgkin_huxley_numeric_keys_match_independent_recalculation():
    practice = _practice()
    numeric = {key for key, item in practice.items() if key.startswith(LESSON + ":") and item["type"] == "numeric"}
    assert numeric == set(NUMERIC_KEYS)
    for key, expected in NUMERIC_KEYS.items():
        spec = practice[key]["solution_spec"]
        assert abs(spec["answer"] - expected) <= spec["tolerance"], (key, spec["answer"], expected)


def test_stated_rest_and_clamp_kinetics_follow_from_the_rate_functions():
    text = READING.read_text(encoding="utf-8")
    an, bn, am, bm, ah, bh = _rates(-65.0)
    assert (round(an, 4), round(bn, 3)) == (0.0582, 0.125) and "α_n = 0.0582 ms⁻¹ and β_n = 0.125 ms⁻¹" in text
    n_rest = an / (an + bn)
    assert round(n_rest, 3) == 0.318 and round(1 / (an + bn), 2) == 5.46 and round(G_K * n_rest**4, 2) == 0.37
    an, bn, am, bm, ah, bh = _rates(0.0)
    assert (round(1 / (am + bm), 2), round(1 / (ah + bh), 2), round(1 / (an + bn), 2)) == (0.24, 1.03, 1.65)
    assert "about 0.24 ms for m, 1.03 ms for h and 1.65 ms for n" in text
    # Worked example: rates rounded as printed, then n, g_K and I_K at 1 ms.
    assert (round(an, 3), round(bn, 4)) == (0.552, 0.0555)
    n1 = _gate_trajectory(0.552, 0.0555, 0.318, 1.0)[-1]
    g_k = G_K * round(n1, 3) ** 4
    assert round(n1, 3) == 0.587 and round(g_k, 2) == 4.27 and round(g_k * (0.0 - E_K)) == 329
    assert "**0.587**" in text and "**4.27 mS/cm²**" in text and "**329 μA/cm²**" in text


def test_stated_spike_threshold_and_refractory_numbers_come_from_the_full_model():
    text = READING.read_text(encoding="utf-8")
    rows = _simulate(_pulse(1.0, 1.0, 10.0), 30.0)
    peak = max(rows, key=lambda row: row[1])
    trough = min((row for row in rows if row[0] > peak[0]), key=lambda row: row[1])
    up = next(row[0] for prev, row in zip(rows, rows[1:]) if prev[1] < 0 <= row[1])
    down = next(row[0] for prev, row in zip(rows, rows[1:]) if prev[1] >= 0 > row[1])
    assert round(peak[1]) == 39 and round(peak[0] - 1.0, 1) == 2.5 and "peaks near +39 mV about 2.5 ms" in text
    assert round(down - up, 1) == 1.1 and "about 1.1 ms" in text
    assert round(trough[1]) == -76 and "about −76 mV" in text
    assert (round(peak[3], 2), round(peak[4], 2), round(peak[2], 2)) == (0.90, 0.33, 0.51)
    assert "m ≈ 0.90, while h has already fallen to about 0.33 and n has risen to about 0.51" in text
    # Thresholds: a 2% margin either side of the stated values separates failure from a spike.
    for width, stated in ((1.0, 6.911), (0.1, 65.06)):
        assert _spike_count(_simulate(_pulse(1.0, width, 0.98 * stated), 20.0)) == 0
        assert _spike_count(_simulate(_pulse(1.0, width, 1.02 * stated), 20.0)) == 1
    assert "about 6.9 μA/cm²" in text and "about 65 μA/cm²" in text
    assert (round(0.1 * 65.06, 1), round(1.0 * 6.911, 1)) == (6.5, 6.9) and "6.5 rather than 6.9 nC/cm²" in text
    # Refractoriness: the second pulse fails half a millisecond before the stated delay and succeeds at it.
    for amplitude, delay in ((10.0, 15.0), (40.0, 9.5)):
        assert not _paired_pulses_fire_twice(delay - 0.5, amplitude)
        assert _paired_pulses_fire_twice(delay, amplitude)
    assert "succeeds only about 15 ms after the first" in text and "succeeds from about 9.5 ms" in text


def test_hodgkin_huxley_choice_keys_point_at_the_correct_option():
    practice = _practice()
    choice = {key for key, item in practice.items() if key.startswith(LESSON + ":") and item["type"] == "single_choice"}
    assert choice == set(CHOICE_KEYS)
    for key, phrase in CHOICE_KEYS.items():
        options = practice[key]["options"]
        assert phrase in options[practice[key]["solution_spec"]["answer"]], key
        assert sum(phrase in option for option in options) == 1, key


def test_hodgkin_huxley_assessment_lesson_cards_and_source_are_linked():
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
    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]
    source = next(item for item in registry if item["id"] == "hodgkin-huxley-1952-quantitative-description")
    assert source["reuse_mode"] == "link-only-reference" and source["permissions"]["quotation"] is False
    assert source["url"] == "https://doi.org/10.1113/jphysiol.1952.sp004764"
    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))["modules"]
    entry = next(item for item in source_map if item["lesson_id"] == LESSON)
    assert "hodgkin-huxley-1952-quantitative-description" in entry["source_ids"]
