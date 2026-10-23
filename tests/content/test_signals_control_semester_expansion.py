"""Independent transform,compensator,state and exact sampled-loop references."""

from __future__ import annotations

import cmath
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
DIRECTORY = ROOT / "content/courses/signals-control"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"signals-control-(1[7-9]|2[0-4]):depth-\d+", q["id"])
}
R = sp.Rational
S = sp.symbols("s")


def lead_reference(plant_rate, target):
    p, k, z = sp.symbols("p k z", real=True)
    residual = sp.Poly(S * (S + plant_rate) * (S + p) + k * (S + z) - target, S)
    solution = sp.solve(residual.all_coeffs(), (p, k, z), dict=True)[0]
    pole, gain, zero = solution[p], solution[k], solution[z]
    assert pole > zero > 0 and gain > 0
    frequency = sp.sqrt(pole * zero)
    phase = sp.atan(frequency / zero) - sp.atan(frequency / pole)
    loop = (
        gain
        * (sp.I * frequency + zero)
        / (sp.I * frequency + pole)
        / (sp.I * frequency * (sp.I * frequency + plant_rate))
    )
    return (
        pole,
        gain,
        zero,
        frequency,
        phase,
        sp.simplify(sp.Abs(loop)),
        plant_rate * pole / (gain * zero),
    )


def state_reference(a0, a1, feedback_roots, observer_roots):
    a = sp.Matrix([[0, 1], [-a0, -a1]])
    b = sp.Matrix([0, 1])
    c = sp.Matrix([[1, 0]])
    k1, k2, l1, l2 = sp.symbols("k1 k2 l1 l2", real=True)
    feedback = sp.Matrix([[k1, k2]])
    observer = sp.Matrix([l1, l2])
    control_target = sp.prod(S + root for root in feedback_roots)
    error_target = sp.prod(S + root for root in observer_roots)
    ksol = sp.solve(
        sp.Poly(
            (S * sp.eye(2) - (a - b * feedback)).det() - control_target, S
        ).all_coeffs(),
        (k1, k2),
    )
    lsol = sp.solve(
        sp.Poly(
            (S * sp.eye(2) - (a - observer * c)).det() - error_target, S
        ).all_coeffs(),
        (l1, l2),
    )
    k = feedback.subs(ksol)
    observer_gain = observer.subs(lsol)
    # Derive reference multiplier from equilibrium rather than the polynomial constant recipe.
    multiplier = -1 / (c * (a - b * k).inv() * b)[0]
    return a, b, c, k, observer_gain, multiplier


def sampled_matrix(a, b, period, kp, ki):
    return sp.Matrix([[a - b * kp, b * ki], [-period, 1]])


def discrete_convolution(ratio, inputs, count=80):
    outputs = [
        sum(
            value * ratio ** (n - index)
            for index, value in enumerate(inputs)
            if n >= index
        )
        for n in range(count)
    ]
    # After the finite input ends,the remaining output is an exact geometric tail.
    energy = sum(value**2 for value in outputs) + (outputs[-1] * ratio) ** 2 / (
        1 - ratio**2
    )
    return outputs, energy


@cache
def calculations():
    t = sp.symbols("t", real=True)
    transform = sp.integrate(sp.exp(-sp.I * sp.pi * t / 2), (t, -1, 1))
    triangle_energy = 2 * sp.integrate((2 - t) ** 2, (t, 0, 2))
    output, energy = discrete_convolution(R(1, 2), [1, 1, 1])
    ap, ak, az, af, aph, alm, ae = lead_reference(2, (S + 4) * (S**2 + 4 * S + 8))
    p, k, z, f, phase, lm, error = lead_reference(3, (S + 5) * (S**2 + 6 * S + 13))
    a, b, c, feedback, observer, reference = state_reference(6, 5, [5, 6], [8, 9])
    aa, ab, ac, afbk, aobs, aref = state_reference(4, 4, [3, 7], [6, 9])
    sampled = sampled_matrix(R(4, 5), R(1, 5), 1, 2, 1)
    roots = [complex(root.evalf()) for root in sampled.eigenvals()]
    pair = next(root for root in roots if root.imag > 0)
    signed_transform = sp.integrate(
        sp.exp(-sp.I * sp.pi * t), (t, 0, 1)
    ) - sp.integrate(sp.exp(-sp.I * sp.pi * t), (t, 1, 2))
    signed_energy = sum(
        sp.integrate(expression**2, (t, left, right))
        for expression, left, right in [
            (t, 0, 1),
            (4 - 3 * t, 1, 2),
            (3 * t - 8, 2, 3),
            (4 - t, 3, 4),
        ]
    )
    dy, de = discrete_convolution(R(1, 3), [1, -1])
    quarter = (1 - sp.exp(-sp.I * sp.pi / 2)) / (1 - sp.exp(-sp.I * sp.pi / 2) / 3)
    assigned = sampled_matrix(R(1, 2), R(1, 2), 1, 1, R(1, 2))
    state = sp.zeros(2, 1)
    for _ in range(2):
        state = assigned * state + sp.Matrix([R(1, 2), 1])
    return {
        (17, 1): {
            "area": sp.integrate(1, (t, -1, 1)),
            "transform": transform,
            "zero": sp.pi,
        },
        (17, 2): {"peak": 2, "halfwidth": 2, "energy": triangle_energy},
        (17, 3): {
            "dc": 2,
            "nyquist": R(2, 3),
            "quarter": sp.Abs(1 / (1 - sp.exp(-sp.I * sp.pi / 2) / 2)),
        },
        (17, 4): {"sample_two": output[2], "sample_three": output[3], "energy": energy},
        (18, 1): {"pole": ap, "gain": ak, "zero": az},
        (18, 2): {"real_root": -4, "pair_real": -2, "pair_imaginary": 2},
        (18, 3): {"velocity_constant": 1 / ae, "ramp_error": ae},
        (18, 4): {"frequency": af, "phase": aph * 180 / sp.pi, "loop_magnitude": alm},
        (19, 1): {
            "controllable": b.row_join(a * b).rank(),
            "observable": c.col_join(c * a).rank(),
            "dc": (-c * a.inv() * b)[0],
        },
        (19, 2): {"k_one": feedback[0], "k_two": feedback[1], "reference": reference},
        (19, 3): {"l_one": observer[0], "l_two": observer[1], "slow_pole": -8},
        (19, 4): {"controllable": 1, "observable": 2, "growth": 2},
        (20, 1): {"trace": sampled.trace(), "determinant": sampled.det()},
        (20, 2): {"real": pair.real, "imaginary": pair.imag, "modulus": abs(pair)},
        (20, 3): {"upper": 3},
        (20, 4): {"modulus": sp.sqrt(sampled_matrix(R(4, 5), R(1, 5), 1, 2, 4).det())},
        (21, 1): {
            "input_energy": 2,
            "magnitude": sp.Abs(signed_transform),
            "output_energy": signed_energy,
            "transform_real": sp.re(signed_transform**2),
        },
        (21, 2): {"first": dy[1], "energy": de, "magnitude": sp.Abs(quarter)},
        (22, 1): {"pole": p, "gain": k, "zero": z},
        (22, 2): {"frequency": f, "phase": phase * 180 / sp.pi, "ramp_error": error},
        (23, 1): {"k_one": afbk[0], "k_two": afbk[1], "reference": aref},
        (23, 2): {"l_one": aobs[0], "l_two": aobs[1], "slowest": -3},
        (24, 1): {
            "trace": assigned.trace(),
            "determinant": assigned.det(),
            "pole": R(1, 2),
            "sample_two": state[0],
        },
        (24, 2): {
            "upper": 2,
            "unstable_modulus": sp.sqrt(
                sampled_matrix(R(1, 2), R(1, 2), 1, 1, 3).det()
            ),
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_signal_control_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(
        int, re.fullmatch(r"signals-control-(\d+):depth-(\d+)", qid).groups()
    )
    question = NEW[qid]
    values = calculations()[number, item]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-11, abs=1e-13)
            response[spec["id"]] = (
                format(value, ".2e") if spec["significant_figures"] else str(int(value))
            )
    assert grade(question, AttemptRequest(response=response)).correct
    for spec in specs:
        if spec["type"] == "numeric":
            wrong = (
                format(float(values[spec["id"]]) * 1.2, ".2e")
                if spec["significant_figures"]
                else str(int(values[spec["id"]]) + 1)
            )
        else:
            wrong = str((spec["answer"] + 1) % 3)
        assert not grade(
            question, AttemptRequest(response={**response, spec["id"]: wrong})
        ).correct


def test_continuous_and_discrete_transform_phase_convolution_and_full_energy():
    t = sp.symbols("t", real=True)
    pieces = [(t, 0, 1), (4 - 3 * t, 1, 2), (3 * t - 8, 2, 3), (4 - t, 3, 4)]
    exact_transform = sum(
        sp.integrate(expression * sp.exp(-sp.I * sp.pi * t), (t, left, right))
        for expression, left, right in pieces
    )
    assert sp.simplify(exact_transform + 16 / sp.pi**2) == 0
    assert (
        sum(
            sp.integrate(expression, (t, left, right))
            for expression, left, right in pieces
        )
        == 0
    )
    assert sum(
        sp.integrate(expression**2, (t, left, right))
        for expression, left, right in pieces
    ) == R(8, 3)
    # Independent periodic frequency quadrature checks both complete discrete energy sums.
    for ratio, inputs in [(0.5, [1, 1, 1]), (1 / 3, [1, -1])]:
        count = 4096
        total = (
            sum(
                abs(
                    sum(
                        value * cmath.exp(-1j * 2 * math.pi * j * n / count)
                        for n, value in enumerate(inputs)
                    )
                    / (1 - ratio * cmath.exp(-1j * 2 * math.pi * j / count))
                )
                ** 2
                for j in range(count)
            )
            / count
        )
        _, reference = discrete_convolution(
            R(1, 2) if ratio == 0.5 else R(1, 3), inputs
        )
        assert total == pytest.approx(float(reference), abs=5e-13)
    assert calculations()[17, 4]["energy"] == R(22, 3)
    assert calculations()[21, 2]["energy"] == R(3, 2)


def test_proper_lead_full_realization_phase_peak_and_final_value():
    for rate, target in [
        (2, (S + 4) * (S**2 + 4 * S + 8)),
        (3, (S + 5) * (S**2 + 6 * S + 13)),
    ]:
        pole, gain, zero, frequency, phase, magnitude, error = lead_reference(
            rate, target
        )
        realization = sp.Matrix(
            [[0, 1, 0], [-gain, -rate, gain * (zero - pole)], [-1, 0, -pole]]
        )
        assert sp.expand((S * sp.eye(3) - realization).det() - target) == 0
        omega = sp.symbols("omega", positive=True)
        boost = sp.atan(omega / zero) - sp.atan(omega / pole)
        assert sp.simplify(sp.diff(boost, omega).subs(omega, frequency)) == 0
        loop = gain * (S + zero) / (S + pole) / (S * (S + rate))
        assert sp.limit(S * (1 / S**2) / (1 + loop), S, 0) == error
        assert sp.limit(S * (1 / S) / (1 + loop), S, 0) == 0
        assert magnitude < 1 and phase > 0
        assert sp.simplify(1 / (1 + loop) + loop / (1 + loop)) == 1
    assert calculations()[18, 4]["loop_magnitude"] == sp.sqrt(5) / 5


def test_state_information_feedback_observer_equilibrium_and_hidden_growth():
    for a0, a1, control_poles, observer_poles in [
        (6, 5, [5, 6], [8, 9]),
        (4, 4, [3, 7], [6, 9]),
    ]:
        a, b, c, k, observer_gain, n = state_reference(
            a0, a1, control_poles, observer_poles
        )
        assert b.row_join(a * b).rank() == c.col_join(c * a).rank() == 2
        block = (
            (a - b * k)
            .row_join(b * k)
            .col_join(sp.zeros(2).row_join(a - observer_gain * c))
        )
        assert sorted(block.eigenvals()) == sorted(
            [-v for v in control_poles + observer_poles]
        )
        equilibrium = -(a - b * k).inv() * b * n
        assert (c * equilibrium)[0] == 1
        assert (
            sp.simplify(
                (c * (S * sp.eye(2) - a).inv() * b)[0] - 1 / (S**2 + a1 * S + a0)
            )
            == 0
        )
    hidden = sp.diag(-1, 2)
    b = sp.Matrix([1, 0])
    c = sp.Matrix([[1, 1]])
    assert b.row_join(hidden * b).rank() == 1 and c.col_join(c * hidden).rank() == 2
    assert sp.simplify((c * (S * sp.eye(2) - hidden).inv() * b)[0]) == 1 / (S + 1)
    t = sp.symbols("t", positive=True)
    autonomous = sp.exp(hidden * t) * sp.Matrix([0, 1])
    assert autonomous[1] == sp.exp(2 * t) and (c * autonomous)[0] == sp.exp(2 * t)


def test_sampled_jury_mapping_gain_boundaries_recurrence_and_defective_decay():
    lam, eta, trace, det = sp.symbols("lambda eta trace det", real=True)
    transformed = sp.cancel(
        (1 - eta) ** 2
        * ((((1 + eta) / (1 - eta)) ** 2) - trace * (1 + eta) / (1 - eta) + det)
    )
    expected = (1 + trace + det) * eta**2 + 2 * (1 - det) * eta + 1 - trace + det
    assert sp.expand(transformed - expected) == 0
    assert sp.expand(expected.subs(eta, 1)) == 4
    for ki in [R(1, 10), 1, 2, R(29, 10), 3, 4]:
        matrix = sampled_matrix(R(4, 5), R(1, 5), 1, 2, ki)
        poles = [complex(value.evalf()) for value in matrix.eigenvals()]
        stable = max(abs(pole) for pole in poles) < 1 - 1e-10
        assert stable == (0 < ki < 3)
        conditions = [
            1 - matrix.trace() + matrix.det(),
            1 + matrix.trace() + matrix.det(),
            1 - matrix.det(),
        ]
        assert stable == all(value > 0 for value in conditions)
    assigned = sampled_matrix(R(1, 2), R(1, 2), 1, 1, R(1, 2))
    nilpotent = assigned - sp.eye(2) / 2
    assert nilpotent != sp.zeros(2) and nilpotent**2 == sp.zeros(2)
    for n in [1, 2, 5]:
        assert assigned**n == sp.eye(2) / 2**n + n * nilpotent / 2 ** (n - 1)
    y = z = R(0)
    for index, expected_y in enumerate([R(1, 2), R(3, 4), R(7, 8)], 1):
        command = 1 - y + z / 2
        y, z = y / 2 + command / 2, z + 1 - y
        assert y == expected_y
    continuous_tau = -1 / math.log(0.8)
    roots = [complex(value) for value in sp.nroots(continuous_tau * S**2 + 3 * S + 4)]
    assert max(root.real for root in roots) < 0
    unstable = sampled_matrix(R(4, 5), R(1, 5), 1, 2, 4)
    assert max(abs(complex(value.evalf())) for value in unstable.eigenvals()) > 1


def test_hold_amplitude_and_input_index_change_the_declared_feedback():
    time = sp.symbols("time", real=True)
    frequency = sp.pi / 2
    held = sp.integrate(sp.exp(-sp.I * frequency * time), (time, 0, 1))
    expected = sp.exp(-sp.I * frequency / 2) * sp.sin(frequency / 2) / (frequency / 2)
    assert sp.simplify(sp.expand_complex(held - expected)) == 0
    assert float(sp.Abs(held)) < 1
    # Current-input recurrence has an algebraic feedback denominator;
    # the one-step held plant has its explicit prior-sample command instead.
    a, b, kp = R(4, 5), R(1, 5), sp.Integer(2)
    current_pole = a / (1 + b * kp)
    next_pole = a - b * kp
    assert (
        current_pole == R(4, 7) and next_pole == R(2, 5) and current_pole != next_pole
    )


def test_signals_packets_deliver_as_open_partial_coursework():
    assert len(NEW) == 24
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 26
    repository = ContentRepository(ROOT / "content")
    for number in range(17, 25):
        lesson = repository.lesson("signals-control", f"signals-control-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 21 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
