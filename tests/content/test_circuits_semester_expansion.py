"""Independent nonlinear-device, modal, transient, covariance and digital references."""

from __future__ import annotations

import json
import math
import re
from functools import cache
from pathlib import Path

import pytest
import sympy as sp
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/circuits"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"circuits-(1[6-9]|2[0-5]):depth-\d+", q["id"])
}


def diode_reference(current, resistance, thermal):
    # Solve the original exponential-current residual; author inverted it analytically.
    left, right = 0.0, 1.0
    for _ in range(100):
        middle = (left + right) / 2
        if 1e-12 * math.expm1(middle / thermal) > current:
            right = middle
        else:
            left = middle
    voltage = (left + right) / 2
    source = voltage + resistance * current
    derivative = 1e-12 * math.exp(voltage / thermal) / thermal
    local = 1 / derivative
    return voltage, source, local


def mos_reference(supply, resistance, gate, coefficient):
    # kilo-ohm / mA units; select roots through the original constitutive inequalities.
    drain = sp.symbols("drain", real=True)
    overdrive = gate - 1
    current = coefficient * overdrive**2 / 2
    candidate = supply - resistance * current
    if candidate >= overdrive > 0:
        return float(candidate), float(current)
    roots = sp.solve(
        (supply - drain) / resistance
        - coefficient * (overdrive * drain - drain**2 / 2),
        drain,
    )
    admitted = [root for root in roots if 0 <= root < overdrive]
    assert len(admitted) == 1
    return float(admitted[0]), float((supply - admitted[0]) / resistance)


def feedback_matrix(gain, fraction):
    return sp.Matrix(
        [[-1000, 0, -1000 * gain * fraction], [1000, -1000, 0], [0, 1000, -1000]]
    )


@cache
def feedback_reference(gain, fraction):
    matrix = feedback_matrix(gain, fraction)
    roots = [complex(value.evalf()) for value in matrix.eigenvals()]
    real_root = next(value.real for value in roots if abs(value.imag) < 1e-10)
    pair = next(value for value in roots if value.imag > 1e-10)
    forcing = sp.Matrix([1000 * gain, 0, 0])
    equilibrium = -matrix.inv() * forcing
    return float(equilibrium[2]), real_root, pair.real, pair.imag


@cache
def calculations():
    vd, vs, rd = diode_reference(0.002, 500, 0.025)
    va, sa, ra = diode_reference(0.001, 2000, 0.026)
    md, mi = mos_reference(12, 3, 4, 1)
    ad, ai = mos_reference(9, 2, 5, sp.Rational(1, 2))
    dc, real, pr, pi = feedback_reference(200, sp.Rational(1, 200))
    _, ur, upr, upi = feedback_reference(200, sp.Rational(27, 200))
    adc, _, apr, api = feedback_reference(120, sp.Rational(1, 40))
    udc, _, ar, aii = feedback_reference(120, sp.Rational(8, 15))
    covariance = sp.Matrix([[34, 25], [25, 41]])
    weight = covariance[0, 1] / covariance[1, 1]
    minimum = (sp.Matrix([[1, -weight]]) * covariance * sp.Matrix([1, -weight]))[0]
    return {
        (16, 1): {"diode": vd, "source": vs},
        (16, 2): {"resistance": rd, "gain": rd / (500 + rd)},
        (16, 3): {"diode_power": vd * 2, "resistor_power": 2, "source_power": vs * 2},
        (16, 4): {},
        (17, 1): {"current": 1.125, "drain": 8.625},
        (17, 2): {"transconductance": 1.5, "gain": -4.5},
        (17, 3): {"drain": md, "current": mi},
        (17, 4): {"gate": 1 + (-1 + math.sqrt(73)) / 3},
        (18, 1): {"loop": 1, "gain": dc},
        (18, 2): {"real_root": real, "pair_real": pr, "pair_imaginary": pi},
        (18, 3): {"real_root": ur, "pair_real": upr, "pair_imaginary": upi},
        (18, 4): {"critical": 8},
        (19, 1): {"diode": va, "source": sa, "resistance": ra},
        (19, 2): {
            "gain": ra / (2000 + ra),
            "diode_power": va,
            "resistor_power": 2,
            "source_power": sa,
        },
        (20, 1): {"current": 1, "drain": 7, "transconductance": 1, "gain": -2},
        (20, 2): {"drain": ad, "current": ai},
        (21, 1): {"loop": 3, "gain": adc, "pair_real": apr, "pair_imaginary": api},
        (21, 2): {"pair_real": ar, "pair_imaginary": aii, "gain": udc},
        (22, 1): {
            "bandwidth": 62.5,
            "rms": math.sqrt(40**2 * 62.5),
            "step": 1 - 3 * math.exp(-2),
        },
        (22, 2): {
            "difference": 5,
            "naive": math.sqrt(75),
            "weight": weight,
            "optimal": sp.sqrt(minimum),
        },
        (23, 1): {"active_rows": 3, "index_sum": 15, "value_at_index_5": 0},
        (23, 2): {"nand_gate_count": 4, "value_at_011": 0, "value_at_000": 1},
        (23, 3): {"critical_path_ns": 6, "slack_at_10ns": 4, "critical_path_gates": 3},
        (23, 4): {"enable_rows": 5, "value_at_101": 1, "value_at_110": 0},
        (24, 1): {"excluded_pairs": 1, "q_set_then_hold": 1, "q_after_reset": 0},
        (24, 2): {"state_after_4": 13, "edges_to_load": 4, "state_after_2": 3},
        (24, 3): {"distinct_states": 8, "last_stage_khz": 250, "count_after_13": 5},
        (24, 4): {"setup_slack_ns": 3, "hold_slack_ns": 10, "max_route_delay_ns": 11},
        (25, 1): {"trip_rows": 4, "index_sum": 21, "two_input_gates": 5},
        (25, 2): {"setup_slack_ns": 8, "hold_slack_ns": 23, "passes_stipulated_checks": 1},
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_recomputed_circuit_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(int, re.fullmatch(r"circuits-(\d+):depth-(\d+)", qid).groups())
    question, values = NEW[qid], calculations()[number, item]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-11, abs=1e-13)
            response[spec["id"]] = format(value, ".2e")
    assert grade(question, AttemptRequest(response=response)).correct
    for spec in specs:
        if spec["type"] == "numeric":
            value = float(values[spec["id"]])
            # Scaling cannot perturb a zero; shift it instead so each field's
            # individual error is genuinely rejected by the actual grader.
            wrong = format(value * 1.2 if value else value + 1.1, ".2e")
        else:
            wrong = str((spec["answer"] + 1) % 3)
        assert not grade(
            question, AttemptRequest(response={**response, spec["id"]: wrong})
        ).correct


def test_nonlinear_original_network_unique_root_sensitivity_and_power():
    for current, resistance, thermal in [(0.002, 500, 0.025), (0.001, 2000, 0.026)]:
        voltage, source, local = diode_reference(current, resistance, thermal)
        assert source == pytest.approx(
            voltage + resistance * 1e-12 * math.expm1(voltage / thermal)
        )
        assert 0 < voltage < source
        assert 1 + resistance / local > 1
        assert source * current == pytest.approx(
            resistance * current**2 + voltage * current
        )
        assert voltage / current > 10 * local

        # Numerically differentiate a re-solved load line, independently of the inverse law.
        def solve(vs):
            left, right = 0.0, vs
            for _ in range(100):
                midpoint = (left + right) / 2
                residual = (
                    midpoint + resistance * 1e-12 * math.expm1(midpoint / thermal) - vs
                )
                if residual > 0:
                    right = midpoint
                else:
                    left = midpoint
            return (left + right) / 2

        step = 1e-5
        observed = (solve(source + step) - solve(source - step)) / (2 * step)
        assert observed == pytest.approx(local / (resistance + local), rel=1e-8)


def test_piecewise_mos_bias_derivative_regions_and_supply_power():
    for supply, resistance, gate, coefficient in [
        (12, 3, 2.5, 1),
        (12, 3, 4, 1),
        (9, 2, 3, 0.5),
        (9, 2, 5, 0.5),
    ]:
        drain, current = mos_reference(supply, resistance, gate, coefficient)
        assert supply * current == pytest.approx(
            resistance * current**2 + drain * current
        )
        overdrive = gate - 1
        expected_gain = (
            -resistance * coefficient * overdrive
            if drain >= overdrive
            else -resistance
            * coefficient
            * drain
            / (1 + resistance * coefficient * (overdrive - drain))
        )
        step = 1e-5
        actual_gain = (
            mos_reference(supply, resistance, gate + step, coefficient)[0]
            - mos_reference(supply, resistance, gate - step, coefficient)[0]
        ) / (2 * step)
        assert actual_gain == pytest.approx(expected_gain, rel=1e-8)
    assert 12 - 3 * 3**2 / 2 < 0
    assert 9 - 2 * 0.5 * 4**2 / 2 < 4
    boundary = calculations()[17, 4]["gate"] - 1
    assert 12 - 3 * boundary**2 / 2 == pytest.approx(boundary)


def test_feedback_characteristic_threshold_and_independent_transient_modes():
    s, loop = sp.symbols("s loop", real=True)
    normalized = sp.Matrix([[-1, 0, -loop], [1, -1, 0], [0, 1, -1]])
    assert sp.expand((s * sp.eye(3) - normalized).det() - ((s + 1) ** 3 + loop)) == 0
    for gain, fraction, stable in [
        (200, sp.Rational(1, 200), True),
        (200, sp.Rational(27, 200), False),
        (120, sp.Rational(1, 40), True),
        (120, sp.Rational(8, 15), False),
    ]:
        dc, real, pr, pi = feedback_reference(gain, fraction)
        assert (max(real, pr) < 0) is stable
        assert dc == pytest.approx(float(gain / (1 + gain * fraction)))
        eigen = complex(pr, pi)
        # Original 3-lag state realization gives a full eigenvector; independently step its ODE.
        initial = [complex((1 + eigen / 1000) ** 2), complex(1 + eigen / 1000), 1 + 0j]

        def derivative(state):
            return [
                -1000 * state[0] - 1000 * float(gain * fraction) * state[2],
                1000 * (state[0] - state[1]),
                1000 * (state[1] - state[2]),
            ]

        def integrate(steps):
            state = initial[:]
            step = 0.002 / steps
            for _ in range(steps):
                k1 = derivative(state)
                k2 = derivative([v + step * k / 2 for v, k in zip(state, k1)])
                k3 = derivative([v + step * k / 2 for v, k in zip(state, k2)])
                k4 = derivative([v + step * k for v, k in zip(state, k3)])
                state = [
                    v + step * (a + 2 * b + 2 * c + d) / 6
                    for v, a, b, c, d in zip(state, k1, k2, k3, k4)
                ]
            return state[2]

        import cmath

        exact = cmath.exp(eigen * 0.002)
        assert abs(integrate(200) - exact) < abs(integrate(100) - exact) / 10
        assert abs(integrate(200)) < 1 if stable else abs(integrate(200)) > 1
    boundary = feedback_matrix(1, 8)
    assert sorted(
        complex(v.evalf()).real for v in boundary.eigenvals()
    ) == pytest.approx([-3000, 0, 0], abs=1e-10)


def test_two_pole_noise_integral_transient_and_positive_covariance_optimum():
    angle = sp.symbols("angle", real=True)
    # f substitution x=2pi f tau then x=tan(angle) avoids using the authored bandwidth formula.
    bandwidth = sp.integrate(sp.cos(angle) ** 2, (angle, 0, sp.pi / 2)) / (
        2 * sp.pi * sp.Rational(1, 500)
    )
    assert bandwidth == sp.Rational(125, 2)
    t = sp.symbols("t", nonnegative=True)
    first = 1 - sp.exp(-500 * t)
    second = 1 - (1 + 500 * t) * sp.exp(-500 * t)
    assert sp.simplify(sp.diff(second, t) - 500 * (first - second)) == 0
    assert first.subs(t, 0) == second.subs(t, 0) == 0
    assert float(second.subs(t, sp.Rational(1, 250))) == pytest.approx(
        calculations()[22, 1]["step"]
    )
    covariance = sp.Matrix([[34, 25], [25, 41]])
    assert covariance.det() == 769 and covariance.is_positive_definite
    g = sp.symbols("g", real=True)
    variance = (sp.Matrix([[1, -g]]) * covariance * sp.Matrix([1, -g]))[0]
    optimal = sp.solve(sp.diff(variance, g), g)[0]
    assert optimal == sp.Rational(25, 41)
    assert variance.subs(g, 1) == 25 and variance.subs(g, optimal) == sp.Rational(
        769, 41
    )
    assert sp.expand(variance - 41 * (g - optimal) ** 2 - sp.Rational(769, 41)) == 0


def test_device_feedback_and_digital_packets_deliver_as_open_partial_coursework():
    assert len(NEW) == 30
    assert MANIFEST["version"] == "0.7.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 27
    repository = ContentRepository(ROOT / "content")
    for number in range(16, 26):
        lesson = repository.lesson("circuits", f"circuits-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 19 or number in (23, 24) else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )


def boolean_rows(function):
    return [index for index in range(8) if function(index >> 2 & 1, index >> 1 & 1, index & 1)]


def nand(x, y):
    return int(not (x and y))


def nor(x, y):
    return int(not (x or y))


def test_combinational_truth_table_de_morgan_and_enable_audits():
    # Lesson 23 row-by-row recalculation of the declared functions.
    rows = boolean_rows(lambda a, b, c: int((a and b) or (b and not c)))
    assert rows == [2, 6, 7]
    assert len(rows) == calculations()[23, 1]["active_rows"]
    assert sum(rows) == calculations()[23, 1]["index_sum"]
    index5 = (1, 0, 1)
    assert int((index5[0] and index5[1]) or (index5[1] and not index5[2])) == (
        calculations()[23, 1]["value_at_index_5"]
    ) == 0

    def g(a, b, c):
        return int(not (a or (b and c)))

    # The stated four-gate NAND construction, checked against the complement.
    def route(a, b, c):
        not_a = nand(a, a)
        pair = nand(b, c)
        middle = nand(not_a, pair)
        return nand(middle, middle)

    gate_count = 4
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                assert route(a, b, c) == g(a, b, c)
    assert gate_count == calculations()[23, 2]["nand_gate_count"] == 4
    assert route(0, 1, 1) == calculations()[23, 2]["value_at_011"] == 0
    assert route(0, 0, 0) == calculations()[23, 2]["value_at_000"] == 1

    # Delay ledger: the complemented term carries the inverter.
    direct, complemented = 2 + 3, 1 + 2 + 3
    assert max(direct, complemented) == calculations()[23, 3]["critical_path_ns"] == 6
    assert 10 - max(direct, complemented) == calculations()[23, 3]["slack_at_10ns"] == 4
    assert 3 == calculations()[23, 3]["critical_path_gates"]

    heater = boolean_rows(lambda t, lamp, m: int((t and not lamp) or m))
    assert len(heater) == calculations()[23, 4]["enable_rows"] == 5
    assert int((1 and not 0) or 1) == calculations()[23, 4]["value_at_101"] == 1
    assert int((1 and not 1) or 0) == calculations()[23, 4]["value_at_110"] == 0


def latch(s, r, q=0):
    # Cross-coupled NOR pair iterated to its stable state.
    qbar = 1 - q
    for _ in range(4):
        q, qbar = nor(r, qbar), nor(s, q)
    return q, qbar


def test_latch_register_counter_and_timing_audits():
    excluded = 0
    for s in (0, 1):
        for r in (0, 1):
            q, qbar = latch(s, r)
            if s and r:
                excluded += int(q == 0 and qbar == 0)
    assert excluded == calculations()[24, 1]["excluded_pairs"] == 1
    stored = latch(1, 0)[0]
    assert stored == 1
    assert latch(0, 0, q=stored)[0] == calculations()[24, 1]["q_set_then_hold"] == 1
    assert latch(0, 1)[0] == calculations()[24, 1]["q_after_reset"] == 0

    # Shift register: serial input enters at Q0 and shifts toward Q3.
    state = 0
    states = []
    for bit in (1, 1, 0, 1):
        state = ((state << 1) | bit) & 0b1111
        states.append(state)
    assert states == [1, 3, 6, 13]
    assert states[3] == calculations()[24, 2]["state_after_4"] == 13
    assert 4 == calculations()[24, 2]["edges_to_load"]
    assert states[1] == calculations()[24, 2]["state_after_2"] == 3

    assert sp.Integer(2**3) == calculations()[24, 3]["distinct_states"] == 8
    assert sp.Rational(2000, 8) == calculations()[24, 3]["last_stage_khz"] == 250
    assert 13 % 8 == calculations()[24, 3]["count_after_13"] == 5

    period, clock_to_q, route_delay, setup, hold = 20, 4, 8, 5, 2
    assert period - clock_to_q - route_delay - setup == (
        calculations()[24, 4]["setup_slack_ns"]
    ) == 3
    assert clock_to_q + route_delay - hold == calculations()[24, 4]["hold_slack_ns"] == 10
    assert period - clock_to_q - setup == calculations()[24, 4]["max_route_delay_ns"] == 11

    trips = boolean_rows(lambda o, c, d: int((o and c) or (c and d) or (o and d)))
    assert trips == [3, 5, 6, 7]
    assert len(trips) == calculations()[25, 1]["trip_rows"] == 4
    assert sum(trips) == calculations()[25, 1]["index_sum"] == 21
    assert 3 + 2 == calculations()[25, 1]["two_input_gates"] == 5

    latched_period, latched_route = 40, 22
    latched_setup_slack = latched_period - clock_to_q - latched_route - 6
    latched_hold_slack = clock_to_q + latched_route - 3
    assert latched_setup_slack == calculations()[25, 2]["setup_slack_ns"] == 8
    assert latched_hold_slack == calculations()[25, 2]["hold_slack_ns"] == 23
    assert int(latched_setup_slack >= 0 and latched_hold_slack >= 0) == (
        calculations()[25, 2]["passes_stipulated_checks"]
    ) == 1
