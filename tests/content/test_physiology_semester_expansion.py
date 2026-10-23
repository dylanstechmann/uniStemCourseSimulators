"""Independent transport ledgers, controller modes and gate integration checks."""

from __future__ import annotations

import json
import math
import re
from fractions import Fraction as F
from functools import cache
from pathlib import Path

import pytest
import sympy as sp
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/physiology"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"physiology-(1[7-9]|2[0-3]):depth-\d+", q["id"])
}


def segments(inflow, removals):
    # Explicit recovered amounts and delivered outputs, rather than just a product.
    delivered = F(str(inflow))
    recovered = []
    for fraction in removals:
        amount = delivered * F(str(fraction))
        recovered.append(amount)
        delivered -= amount
    assert sum(recovered) + delivered == F(str(inflow))
    assert delivered >= 0 and all(r >= 0 for r in recovered)
    return delivered


def nephron(gfr, plasma, salt, water):
    filtered = F(gfr) * F(plasma) / 1000
    excreted = segments(filtered, salt)
    volume = segments(gfr, water)
    return {
        "filtered": filtered,
        "excreted": excreted,
        "fraction": excreted / filtered,
        "urine_flow": volume,
        "urine_na": excreted / (volume / 1000),
    }


def controller(tau_w, tau_h, gain, feedback, drive, bias=0):
    matrix = sp.Matrix(
        [
            [-1 / sp.Rational(tau_w), sp.Rational(gain, tau_w)],
            [-sp.Rational(feedback, tau_h), -1 / sp.Rational(tau_h)],
        ]
    )
    forcing = sp.Matrix(
        [
            sp.Rational(str(drive)) / tau_w,
            -sp.Rational(feedback) * sp.Rational(str(bias)) / tau_h,
        ]
    )
    equilibrium = matrix.inv() * (-forcing)
    eigenvalues = list(matrix.eigenvals())
    return {
        "water": float(equilibrium[0]),
        "signal": float(equilibrium[1]),
        "real": float(sp.re(eigenvalues[0])),
        "imaginary": abs(float(sp.im(eigenvalues[0]))),
        "initial": float(forcing[0]),
    }


def gas(capacity, half, p1, p2, q1, q2, venous):
    def content(pressure):
        return F(capacity * pressure**2, half**2 + pressure**2)

    first, second = content(p1), content(p2)
    amount = q1 * first + q2 * second
    mixed = amount / (q1 + q2)
    return {
        "content_one": first,
        "content_two": second,
        "mixed": mixed,
        "equivalent": half * math.sqrt(mixed / (capacity - mixed)),
        "weighted": F(q1 * p1 + q2 * p2, q1 + q2),
        "delivery": amount,
        "uptake": amount - (q1 + q2) * venous,
        "extraction": (mixed - venous) / mixed,
        "equivalent_fraction": (first - mixed) / (first - venous),
    }


@cache
def calculations():
    salt, water = [0.5, 0.8, 0.75, 0.9], [0.5, 0.5, 0, 0.96]
    renal = nephron(80, 125, salt, water)
    changed = nephron(80, 125, salt, [0.5, 0.5, 0, 0.8])
    control = controller(3, 1, 2, 1, 0.3)
    bias = controller(3, 1, 2, 1, 0.3, 0.05)
    oxygen = gas(180, 20, 60, 20, 2, 1, 54)
    assigned_oxygen = gas(200, 25, 75, 25, 3, 1, 80)
    assigned_renal = nephron(90, 120, [0.5, 0.75, 0.8, 0.9], [0.6, 0.5, 0, 0.9])
    assigned_water = nephron(90, 120, [0.5, 0.75, 0.8, 0.9], [0.6, 0.5, 0, 0.5])
    assigned_salt = nephron(90, 120, [0.5, 0.75, 0.8, 0.8], [0.6, 0.5, 0, 0.9])
    assigned_control = controller(2, 1, 1, 2, 0.3)
    assigned_bias = controller(2, 1, 1, 2, 0.3, 0.05)
    # Matrix exponentials solve separate fixed-voltage gate and passive current-step ODEs.
    gate_matrix = sp.Matrix([[-sp.Rational(4, 10), sp.Rational(1, 10)], [0, 0]])
    gate = float(((gate_matrix * 5).exp() * sp.Matrix([sp.Rational(1, 10), 1]))[0])
    passive_matrix = sp.Matrix([[-sp.Rational(1, 5), -10], [0, 0]])
    voltage = float(((passive_matrix * 5).exp() * sp.Matrix([-60, 1]))[0])
    return {
        (17, 1): {k: renal[k] for k in ["filtered", "excreted", "fraction"]},
        (17, 2): {k: renal[k] for k in ["urine_flow", "urine_na"]},
        (17, 3): {k: changed[k] for k in ["urine_flow", "urine_na", "excreted"]},
        (17, 4): {},
        (18, 1): {k: control[k] for k in ["water", "signal", "initial"]},
        (18, 2): {k: control[k] for k in ["real", "imaginary"]},
        (18, 3): {"water": F(3, 10) + 2 * F(-5, 100), "signal": F(-5, 100)},
        (18, 4): {k: bias[k] for k in ["water", "signal"]},
        (19, 1): {k: oxygen[k] for k in ["content_one", "content_two", "mixed"]},
        (19, 2): {k: oxygen[k] for k in ["equivalent", "weighted"]},
        (19, 3): {k: oxygen[k] for k in ["delivery", "uptake", "extraction"]},
        (19, 4): {"equivalent_fraction": oxygen["equivalent_fraction"]},
        (20, 1): {"tau": 1 / F(".2"), "steady": -60 + 2 / F(".2"), "voltage": voltage},
        (20, 2): {
            "gate": gate,
            "conductance": 20 * gate**4,
            "current": 20 * gate**4 * (-20 - -80),
            "cable": 20 * math.exp(-3 / 1.5),
        },
        (21, 1): {
            k: assigned_oxygen[k] for k in ["mixed", "equivalent", "delivery", "uptake"]
        },
        (21, 2): {
            "resistance": 1 / (F(1, 10) + F(1, 30)),
            "equivalent_fraction": assigned_oxygen["equivalent_fraction"],
            "new_flow": F(30, 10) + F(30, 60),
            "new_delivery": F(30, 10) * 180 + F(30, 60) * 100,
        },
        (22, 1): assigned_renal,
        (22, 2): {
            "water_flow": assigned_water["urine_flow"],
            "water_concentration": assigned_water["urine_na"],
            "water_excreted": assigned_water["excreted"],
            "salt_excreted": assigned_salt["excreted"],
        },
        (23, 1): assigned_control,
        (23, 2): {
            "bounded_water": F(3, 10) - F(1, 10),
            "bounded_signal": F(-1, 10),
            "biased_water": assigned_bias["water"],
            "biased_signal": assigned_bias["signal"],
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_new_physiological_model_keys_and_each_rejected_perturbation(qid):
    number, item = map(int, re.fullmatch(r"physiology-(\d+):depth-(\d+)", qid).groups())
    question, values = NEW[qid], calculations()[(number, item)]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-12, abs=1e-16)
            response[spec["id"]] = format(value, ".2e")
    assert grade(question, AttemptRequest(response=response)).correct
    for spec in specs:
        wrong = (
            format(float(values[spec["id"]]) * 1.2, ".2e")
            if spec["type"] == "numeric"
            else str((spec["answer"] + 1) % 3)
        )
        assert not grade(
            question, AttemptRequest(response={**response, spec["id"]: wrong})
        ).correct


def integrate(rhs, state, dt, steps):
    for _ in range(steps):
        a = rhs(state)
        b = rhs([s + dt * v / 2 for s, v in zip(state, a, strict=True)])
        c = rhs([s + dt * v / 2 for s, v in zip(state, b, strict=True)])
        d = rhs([s + dt * v for s, v in zip(state, c, strict=True)])
        state = [
            s + dt * (v + 2 * w + 2 * x + y) / 6
            for s, v, w, x, y in zip(state, a, b, c, d, strict=True)
        ]
    return state


def test_feedback_transients_saturation_and_bias_are_different_equations():
    def rhs(state):
        w, h = state
        return [(0.3 - w + h) / 2, -h - 2 * w]

    matrix = sp.Matrix([[-sp.Rational(1, 2), sp.Rational(1, 2)], [-2, -1]])
    equilibrium = sp.Matrix([sp.Rational(1, 10), -sp.Rational(1, 5)])
    exact = equilibrium - (matrix * 5).exp() * equilibrium
    coarse = integrate(rhs, [0, 0], 0.05, 100)
    fine = integrate(rhs, [0, 0], 0.025, 200)
    error_coarse = max(abs(c - float(e)) for c, e in zip(coarse, exact, strict=True))
    error_fine = max(abs(c - float(e)) for c, e in zip(fine, exact, strict=True))
    assert error_fine < error_coarse / 12
    bounded = integrate(
        lambda s: [(0.3 - s[0] + s[1]) / 2, max(-0.1, min(0.4, -2 * s[0])) - s[1]],
        [0, 0],
        0.01,
        10000,
    )
    assert bounded == pytest.approx([0.2, -0.1], abs=1e-12)
    assert -0.1 <= bounded[1] <= 0.4 and -2 * bounded[0] < -0.1
    biased = integrate(
        lambda s: [(0.3 - s[0] + s[1]) / 2, -s[1] - 2 * (s[0] + 0.05)],
        [0, 0],
        0.01,
        10000,
    )
    assert biased == pytest.approx([1 / 15, -7 / 30], abs=1e-12)
    assert integrate(rhs, [0, 0], 0.001, 1)[0] / 0.001 == pytest.approx(0.15, rel=0.001)


def test_content_conservation_and_fixed_pressure_delivery_counterexample():
    state = gas(180, 20, 60, 20, 2, 1, 54)
    p = state["equivalent"]
    assert 180 * p**2 / (20**2 + p**2) == pytest.approx(float(state["mixed"]))
    wrong = state["weighted"]
    assert abs(180 * wrong**2 / (20**2 + wrong**2) - state["mixed"]) > 10
    old_delivery, new_delivery = 3 * 180 + 100, 3 * 180 + F(1, 2) * 100
    assert new_delivery < old_delivery and new_delivery / F(7, 2) > old_delivery / 4
    # Distinct unequal-exchange and two-content mixtures share this same arterial result.
    q = state["equivalent_fraction"]
    assert (1 - q) * 162 + q * 54 == state["mixed"]


def test_nonzero_initial_gate_conductance_slope_and_fixed_rate_integration():
    n0, alpha, beta, maximum = 0.318, 0.552, 0.0555, 36
    expected = 4 * maximum * n0**3 * (alpha * (1 - n0) - beta * n0)
    dt = 1e-7
    n = alpha / (alpha + beta) + (n0 - alpha / (alpha + beta)) * math.exp(
        -(alpha + beta) * dt
    )
    assert (maximum * n**4 - maximum * n0**4) / dt == pytest.approx(expected, rel=1e-6)
    assert expected > 1.6
    assert 4 * maximum * 0**3 * alpha == 0
    gate = integrate(lambda s: [0.1 * (1 - s[0]) - 0.3 * s[0]], [0.1], 0.01, 500)[0]
    assert gate == pytest.approx(calculations()[(20, 2)]["gate"], abs=1e-12)
    text = (
        DIRECTORY
        / "modules/16-voltage-gated-conductances-and-the-hodgkin-huxley-action-potential.md"
    ).read_text()
    assert "Because n⁴ starts with zero slope" not in text
    assert "1.66155" in text


def test_connected_model_reports_deliver_with_honest_partial_scope():
    assert len(NEW) == 20
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 25
    repository = ContentRepository(ROOT / "content")
    for number in range(17, 24):
        lesson = repository.lesson("physiology", f"physiology-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 20 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
