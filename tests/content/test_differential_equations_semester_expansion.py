"""Independent symbolic IVP, harmonic, fundamental-matrix and radial checks."""

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
DIRECTORY = ROOT / "content/courses/differential-equations"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"differential-equations-(1[6-9]|2[0-2]):depth-\d+", q["id"])
}
T, S = sp.symbols("t s", real=True)


def linear_ivp(p, q, initial):
    factor = sp.exp(sp.integrate(p, (T, 0, T)))
    state = sp.simplify(
        (initial + sp.integrate((factor * q).subs(T, S), (S, 0, T))) / factor
    )
    assert sp.simplify(sp.diff(state, T) + p * state - q) == 0
    assert state.subs(T, 0) == initial
    return factor, state


def harmonic(a, n):
    coefficient = (
        sp.integrate(-sp.sin(n * T), (T, -sp.pi, 0))
        + sp.integrate(sp.sin(n * T), (T, 0, sp.pi))
    ) / sp.pi
    sine, cosine = sp.Matrix([[a, -n], [n, a]]).inv() * sp.Matrix([coefficient, 0])
    return {
        "sine": sine,
        "cosine": cosine,
        "amplitude": sp.sqrt(sine**2 + cosine**2),
        "lag": sp.atan2(-cosine, sine),
    }


def squared_radius(mu, initial_squared, time):
    # Reciprocal radius-squared has a linear equation, solved independently of the logistic form.
    if mu == 0:
        inverse = 1 / initial_squared + 2 * time
    else:
        factor = sp.exp(2 * mu * T)
        inverse = ((1 / initial_squared) + sp.integrate(2 * factor, (T, 0, T))) / factor
        inverse = inverse.subs(T, time)
    return sp.simplify(1 / inverse)


@cache
def periodic_initial():
    start, e = sp.symbols("start e")
    positive_end = 1 + (start - 1) * e
    negative_end = -1 + (positive_end + 1) * e
    return sp.solve(negative_end - start, start)[0].subs(e, sp.exp(-sp.pi))


@cache
def calculations():
    factor, variable = linear_ivp(T, 3 * T, 5)
    assigned_factor, assigned_variable = linear_ivp(2 * T, 2 * T, 3)
    first, third = harmonic(1, 1), harmonic(1, 3)
    r = sp.symbols("r", real=True)
    radial_derivative = sp.diff(4 * r - r**3, r).subs(r, 2)
    w = squared_radius(4, sp.Integer(1), sp.log(3) / 8)
    zero_w = squared_radius(0, sp.Integer(1), 1)
    resonant = sp.simplify(
        sp.integrate(sp.sin(2 * (T - S)) * sp.sin(2 * S) / 2, (S, 0, T))
    )
    matrix = sp.Matrix([[-1, 2], [0, -1]])
    forced = ((matrix * (T - S)).exp() * sp.Matrix([0, 1])).integrate((S, 0, T))
    equilibrium = matrix.inv() * sp.Matrix([0, -1])
    transfer = sp.Matrix([[-3, 1], [3, -1]])
    closed = (transfer * sp.log(2) / 4).exp() * sp.Matrix([4, 0])
    euler = (sp.eye(2) + sp.Rational(2, 5) * transfer) * sp.Matrix([4, 0])
    cycle_w = squared_radius(sp.Rational(1, 4), sp.Rational(1, 16), 2 * sp.log(3))
    boundary_w = squared_radius(0, sp.Rational(1, 4), 2)
    return {
        (16, 1): {
            "factor": factor.subs(T, 2),
            "state": variable.subs(T, 2),
            "derivative": sp.diff(variable, T).subs(T, 2),
        },
        (16, 2): {"state": (3 - 1) ** 2, "derivative": 2 * (3 - 1)},
        (16, 3): {"state": 1 / sp.Rational(1, 2), "escape": 1},
        (16, 4): {"propagator": sp.exp(-sp.integrate(T, (T, 1, 2)))},
        (17, 1): first,
        (17, 2): {
            "amplitude": third["amplitude"],
            "ratio": third["amplitude"] / first["amplitude"],
        },
        (17, 3): {
            "bound20": sp.integrate(4 / (sp.pi * T**2), (T, 20, sp.oo)),
            "bound64": sp.integrate(4 / (sp.pi * T**2), (T, 64, sp.oo)),
            "index": sp.floor(4 / (sp.Rational(2, 100) * sp.pi)) + 1,
        },
        (17, 4): {
            "periodic_initial": periodic_initial(),
            "transient": -periodic_initial() / sp.E,
        },
        (18, 1): {
            "radius": sp.sqrt(4),
            "period": 2 * sp.pi / 2,
            "exponent": radial_derivative,
        },
        (18, 2): {"time": sp.log(3) / 8, "squared": w, "radius": sp.sqrt(w)},
        (18, 3): {"radius": sp.sqrt(zero_w), "lyapunov_derivative": -(zero_w**2)},
        (18, 4): {},
        (19, 1): {
            "factor": assigned_factor.subs(T, 1),
            "state": assigned_variable.subs(T, 1),
            "particular": 1,
        },
        (19, 2): {
            "escape": sp.Rational(1, 2),
            "state": 1 / (sp.Rational(1, 2) - sp.Rational(1, 4)),
            "delayed": sp.Rational(9, 4),
            "delayed_derivative": sp.Rational(9, 2),
        },
        (20, 1): {
            "first_state": resonant.subs(T, sp.pi / 4),
            "velocity": sp.diff(resonant, T).subs(T, sp.pi / 4),
            "second_state": resonant.subs(T, sp.pi / 2),
        },
        (20, 2): {
            "jump": 3,
            "impulse_state": 3 * sp.exp(-sp.pi / 2),
            "tail": sp.integrate(4 / (sp.pi * T**2), (T, 64, sp.oo)),
            "transient": -periodic_initial() / sp.E,
        },
        (21, 1): {
            "first": forced[0].subs(T, 1),
            "second": forced[1].subs(T, 1),
            "steady_first": equilibrium[0],
            "steady_second": equilibrium[1],
        },
        (21, 2): {
            "first": closed[0],
            "second": closed[1],
            "euler_first": euler[0],
            "euler_second": euler[1],
        },
        (22, 1): {
            "cycle_radius": sp.sqrt(sp.Rational(1, 4)),
            "period": 2 * sp.pi / 2,
            "exponent": sp.diff(r / 4 - r**3, r).subs(r, sp.Rational(1, 2)),
            "observed_radius": sp.sqrt(cycle_w),
        },
        (22, 2): {
            "radius": sp.sqrt(boundary_w),
            "lyapunov_derivative": -(boundary_w**2),
            "amplification": 1 - 4 * sp.Rational(2, 5),
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_recomputed_de_fields_pass_and_each_individual_perturbation_fails(qid):
    number, item = map(
        int, re.fullmatch(r"differential-equations-(\d+):depth-(\d+)", qid).groups()
    )
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
            response[spec["id"]] = (
                format(value, ".2e") if spec["significant_figures"] else str(int(value))
            )
    assert grade(question, AttemptRequest(response=response)).correct
    for spec in specs:
        wrong = (
            (
                format(float(values[spec["id"]]) * 1.2, ".2e")
                if spec["significant_figures"]
                else str(int(values[spec["id"]]) + 1)
            )
            if spec["type"] == "numeric"
            else str((spec["answer"] + 1) % 3)
        )
        assert not grade(
            question, AttemptRequest(response={**response, spec["id"]: wrong})
        ).correct


def test_domains_explicit_nonunique_families_and_original_residuals():
    for multiplier in [2, 3]:
        for delay in [0, 1, 2]:
            branch = sp.Rational(multiplier**2, 4) * (T - delay) ** 2
            assert (
                sp.simplify(sp.diff(branch, T) - multiplier**2 * (T - delay) / 2) == 0
            )
            assert branch.subs(T, delay) == sp.diff(branch, T).subs(T, delay) == 0
            # For t>=delay the square root gives multiplier*(t-delay)/2.
            assert branch.subs(T, delay + 1) > 0
    escaping = 2 / (1 - 2 * T)
    assert sp.simplify(sp.diff(escaping, T) - escaping**2) == 0
    assert sp.limit(escaping, T, sp.Rational(1, 2), dir="-") == sp.oo
    assert escaping.subs(T, 0) == 2


def test_fourier_coefficients_phase_uniform_certificate_and_independent_map():
    n, samples = 64, 1001
    coefficients = [
        (j, float(harmonic(1, j)["sine"]), float(harmonic(1, j)["cosine"]))
        for j in range(1, n + 1, 2)
    ]
    initial = float(periodic_initial())
    errors = []
    for i in range(samples):
        t = 2 * math.pi * i / (samples - 1)
        if t <= math.pi:
            exact = 1 + (initial - 1) * math.exp(-t)
        else:
            half_end = 1 + (initial - 1) * math.exp(-math.pi)
            exact = -1 + (half_end + 1) * math.exp(-(t - math.pi))
        series = sum(
            a * math.sin(j * t) + b * math.cos(j * t) for j, a, b in coefficients
        )
        errors.append(abs(series - exact))
    assert max(errors) < 4 / (math.pi * n) < 0.02
    assert harmonic(1, 2)["amplitude"] == 0
    assert -initial / math.e > 4 / (math.pi * n)
    assert float(harmonic(2, 3)["amplitude"]) == pytest.approx(0.11771103755105271)


def test_resonant_and_impulse_initial_data_and_forced_system_identities():
    resonant = sp.integrate(sp.sin(2 * (T - S)) * sp.sin(2 * S) / 2, (S, 0, T))
    assert sp.simplify(sp.diff(resonant, T, 2) + 4 * resonant - sp.sin(2 * T)) == 0
    assert resonant.subs(T, 0) == sp.diff(resonant, T).subs(T, 0) == 0
    impulse = 3 * sp.exp(-T) * sp.sin(T)  # Time since the event.
    assert (
        sp.simplify(sp.diff(impulse, T, 2) + 2 * sp.diff(impulse, T) + 2 * impulse) == 0
    )
    assert impulse.subs(T, 0) == 0 and sp.diff(impulse, T).subs(T, 0) == 3
    a = sp.Matrix([[-1, 2], [0, -1]])
    phi = (a * T).exp()
    assert sp.simplify(phi.diff(T) - a * phi) == sp.zeros(2)
    assert phi.subs(T, 0) == sp.eye(2)
    closed = sp.Matrix([[-3, 1], [3, -1]])
    assert sp.ones(1, 2) * closed == sp.zeros(1, 2)
    h = sp.symbols("h", nonnegative=True)
    implicit = (sp.eye(2) - h * closed).inv()
    assert sp.simplify(sp.ones(1, 2) * implicit) == sp.ones(1, 2)
    assert all(entry.is_nonnegative for entry in implicit)


def test_radial_identity_and_independent_cartesian_integration():
    x, y, mu, omega = sp.symbols("x y mu omega", real=True)
    square = x**2 + y**2
    dx, dy = (mu - square) * x - omega * y, omega * x + (mu - square) * y
    assert sp.expand(x * dx + y * dy - (mu * square - square**2)) == 0
    assert sp.expand(x * dy - y * dx - omega * square) == 0

    def integrate(steps, parameter, initial, end):
        dt, state = end / steps, [initial, 0.0]

        def rhs(s):
            radius_squared = sum(v * v for v in s)
            return [
                (parameter - radius_squared) * s[0] - 2 * s[1],
                2 * s[0] + (parameter - radius_squared) * s[1],
            ]

        for _ in range(steps):
            a = rhs(state)
            b = rhs([s + dt * k / 2 for s, k in zip(state, a, strict=True)])
            c = rhs([s + dt * k / 2 for s, k in zip(state, b, strict=True)])
            d = rhs([s + dt * k for s, k in zip(state, c, strict=True)])
            state = [
                s + dt * (v + 2 * w + 2 * z + q) / 6
                for s, v, w, z, q in zip(state, a, b, c, d, strict=True)
            ]
        return math.hypot(*state)

    exact = float(
        sp.sqrt(squared_radius(sp.Rational(1, 4), sp.Rational(1, 16), 2 * sp.log(3)))
    )
    coarse = abs(integrate(200, 0.25, 0.25, 2 * math.log(3)) - exact)
    fine = abs(integrate(400, 0.25, 0.25, 2 * math.log(3)) - exact)
    assert fine < coarse / 10
    assert integrate(1000, 0, 0.5, 2) == pytest.approx(
        1 / (2 * math.sqrt(2)), abs=1e-11
    )


def test_new_reports_and_foundations_deliver_as_open_practice():
    assert len(NEW) == 20
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 24
    repository = ContentRepository(ROOT / "content")
    for number in range(16, 23):
        lesson = repository.lesson(
            "differential-equations", f"differential-equations-{number}"
        )
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 19 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
