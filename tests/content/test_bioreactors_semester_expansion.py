"""Independent viable-state, observation, spatial and factorial evidence checks."""

from __future__ import annotations

import csv
import json
import re
from functools import cache
from pathlib import Path

import pytest
import sympy as sp
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/bioreactors"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"bioreactors-(1[6-9]|2[0-2]):depth-\d+", q["id"])
}
R = sp.Rational


@cache
def retained(assigned=False):
    d, b, leak, kd, maximum, half, feed, growth_yield, maintenance = map(
        R,
        [".3", ".25", ".2", ".03", ".6", ".5", "2", ".5", ".1"]
        if assigned
        else [".25", ".2", ".1", ".03", ".5", ".4", "2", ".4", ".05"],
    )
    x, s = sp.symbols("x s", real=True)
    loss = d * (b + leak * (1 - b))
    growth = maximum * s / (half + s)
    consumption = growth / growth_yield + maintenance
    rhs = sp.Matrix([(growth - kd - loss) * x, d * (feed - s) - consumption * x])
    states = sp.solve(list(rhs), [x, s], dict=True)
    positive = [v for v in states if v[x] > 0 and v[s] >= 0 and v[s] < feed]
    assert len(positive) == 1
    state = positive[0]
    assert rhs.subs(state) == sp.zeros(2, 1)
    observed_growth, specific = growth.subs(state), consumption.subs(state)
    jacobian = rhs.jacobian([x, s]).subs(state)
    assert jacobian.trace() < 0 and jacobian.det() > 0
    return {
        "loss": loss,
        "growth": observed_growth,
        "substrate": state[s],
        "biomass": state[x],
        "specific": specific,
        "gross": observed_growth * state[x],
        "export": loss * state[x],
        "death": kd * state[x],
        "consumption": consumption.subs(state) * state[x],
        "dead": kd * state[x] / d,
        "yield": loss / specific,
        "boundary": rhs[1].subs({x: 10 if assigned else 20, s: 0}),
    }


@cache
def probe(k, a, time):
    k, a, time = map(sp.sympify, [k, a, time])
    # Homogeneous deficits (1-C,1-P) instead of the authored partial-fraction formula.
    matrix = sp.Matrix([[-k, 0], [a, -a]])
    state = (matrix * time).exp() * sp.ones(2, 1)
    return {
        "liquid": sp.simplify(1 - state[0]),
        "probe": sp.simplify(1 - state[1]),
        "curvature": -(matrix**2 * sp.ones(2, 1))[1],
    }


def uptake(k, u, lower):
    matrix = sp.Matrix([[-k, 0], [3, -3]])
    steady = -matrix.inv() * sp.Matrix([k - u, 0])
    assert steady[0] == steady[1]
    return {"steady": steady[0], "capacity": k * (1 - lower)}


@cache
def zones(assigned=False, exchange=None):
    v1, v2, k1, k2, u1, u2 = map(
        R, [1, 2, 5, 0, ".2", ".2"] if assigned else [2, 2, 3, 0, ".3", ".3"]
    )
    e = sp.sympify(exchange if exchange is not None else (1 if assigned else R(3, 2)))
    matrix = sp.Matrix([[-k1 - e / v1, e / v1], [e / v2, -k2 - e / v2]])
    forcing = sp.Matrix([k1 - u1, k2 - u2])
    state = -matrix.inv() * forcing
    if e.is_positive:
        assert matrix.trace() < 0 and matrix.det() > 0
    return {
        "first": sp.simplify(state[0]),
        "second": sp.simplify(state[1]),
        "mean": sp.simplify((v1 * state[0] + v2 * state[1]) / (v1 + v2)),
        "demand": u1 * v1 + u2 * v2,
        "exchange": sp.simplify(e * (state[0] - state[1])),
        "uniform": 1 - (u1 * v1 + u2 * v2) / (k1 * v1 + k2 * v2),
    }


@cache
def factorial():
    with (DIRECTORY / "assignments/process-evidence-factorial.csv").open() as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == len({r["run_id"] for r in rows}) == 8
    data = [
        (int(r["factor_a"]), int(r["factor_b"]), R(r["response_normalized"]))
        for r in rows
    ]
    design = sp.Matrix([[1, a, b, a * b] for a, b, y in data])
    response = sp.Matrix([y for a, b, y in data])
    beta = (design.T * design).inv() * design.T * response
    residual = response - design * beta
    assert design.T * residual == sp.zeros(4, 1)
    means = {
        (a, b): sum(y for aa, bb, y in data if aa == a and bb == b) / 2
        for a in [-1, 1]
        for b in [-1, 1]
    }
    return {
        "means": means,
        "beta": beta,
        "sse": (residual.T * residual)[0],
        "mse": (residual.T * residual)[0] / (len(data) - design.rank()),
    }


@cache
def calculations():
    renal = retained()
    assigned = retained(True)
    observation = probe(1, 3, 1)
    swapped = probe(3, 1, 1)
    equal = probe(2, 2, R(1, 2))
    zone = zones()
    changed = zones(exchange=3)
    assigned_zone = zones(True)
    assigned_change = zones(True, 2)
    e = sp.symbols("e", positive=True)
    minimum = sp.solve(zones(exchange=e)["second"] - R(1, 2), e)[0]
    assigned_minimum = sp.solve(zones(True, e)["second"] - R(1, 2), e)[0]
    observation_assigned = probe(R(3, 2), 3, R(2, 3))
    table = factorial()
    means = table["means"]
    return {
        (16, 1): {k: renal[k] for k in ["loss", "growth", "substrate", "biomass"]},
        (16, 2): {k: renal[k] for k in ["specific", "gross", "export", "death"]},
        (16, 3): {k: renal[k] for k in ["consumption", "dead", "yield"]},
        (16, 4): {"derivative": renal["boundary"]},
        (17, 1): observation,
        (17, 2): {k: swapped[k] for k in ["liquid", "probe"]},
        (17, 3): {k: equal[k] for k in ["liquid", "probe"]},
        (17, 4): uptake(2, R(2, 5), R(3, 10)),
        (18, 1): {k: zone[k] for k in ["first", "second", "mean"]},
        (18, 2): {k: zone[k] for k in ["demand", "exchange", "uniform"]},
        (18, 3): {
            "minimum": minimum,
            "second": changed["second"],
            "mean": changed["mean"],
        },
        (18, 4): {},
        (19, 1): {k: assigned[k] for k in ["loss", "growth", "substrate", "biomass"]},
        (19, 2): {
            "gross": assigned["gross"],
            "export": assigned["export"],
            "death": assigned["death"],
            "substrate_use": assigned["consumption"],
        },
        (20, 1): {
            **observation_assigned,
            "apparent": -sp.log(1 - observation_assigned["probe"]) / R(2, 3),
        },
        (20, 2): {
            "equal_probe": probe(1, 1, 1)["probe"],
            **uptake(R(3, 2), R(3, 10), R(2, 5)),
        },
        (21, 1): {k: assigned_zone[k] for k in ["first", "second", "mean"]},
        (21, 2): {
            "minimum": assigned_minimum,
            "second": assigned_change["second"],
            "mean": assigned_change["mean"],
        },
        (22, 1): dict(
            zip(
                ["minus_minus", "plus_minus", "minus_plus", "plus_plus"],
                [means[-1, -1], means[1, -1], means[-1, 1], means[1, 1]],
                strict=True,
            )
        ),
        (22, 2): {
            "effect_a": 2 * table["beta"][1],
            "effect_b": 2 * table["beta"][2],
            "effect_ab": 2 * table["beta"][3],
            "simple_low": means[1, -1] - means[-1, -1],
            "simple_high": means[1, 1] - means[-1, 1],
            "mse": table["mse"],
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_recomputed_process_keys_and_actual_grader_individual_rejections(qid):
    number, item = map(
        int, re.fullmatch(r"bioreactors-(\d+):depth-(\d+)", qid).groups()
    )
    question, values = NEW[qid], calculations()[number, item]
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


def integrate(rhs, state, end, steps):
    dt = end / steps
    for _ in range(steps):
        a = rhs(state)
        b = rhs([s + dt * k / 2 for s, k in zip(state, a, strict=True)])
        c = rhs([s + dt * k / 2 for s, k in zip(state, b, strict=True)])
        d = rhs([s + dt * k for s, k in zip(state, c, strict=True)])
        state = [
            s + dt * (v + 2 * w + 2 * x + y) / 6
            for s, v, w, x, y in zip(state, a, b, c, d, strict=True)
        ]
    return state


def test_viable_ledger_domains_and_distinct_yield_definitions():
    for assigned in [False, True]:
        state = retained(assigned)
        assert state["gross"] == state["export"] + state["death"]
        assert state["yield"] == state["export"] / state["consumption"]
        assert state["gross"] / state["consumption"] > state["yield"]
        assert state["boundary"] < 0
    # These domain failures belong to the exact vector field, not an integration method.
    assert retained()["boundary"] == R(-1, 2)
    assert retained(True)["boundary"] == R(-2, 5)


def test_probe_symmetry_equal_rate_limit_and_analytic_csv_precision():
    t = sp.symbols("t", nonnegative=True)
    assert sp.simplify(probe(2, 4, t)["probe"] - probe(4, 2, t)["probe"]) == 0
    assert sp.simplify(probe(2, 4, t)["liquid"] - probe(4, 2, t)["liquid"]) != 0
    assert (
        sp.simplify(probe(2, 2, t)["probe"] - (1 - (1 + 2 * t) * sp.exp(-2 * t))) == 0
    )
    with (DIRECTORY / "assignments/probe-response-reference.csv").open() as stream:
        rows = list(csv.DictReader(stream))
    for row in rows:
        time = float(row["time_normalized"])
        numerical = integrate(
            lambda s: [2 * (1 - s[0]), 4 * (s[0] - s[1])], [0.0, 0.0], time, 500
        )[1]
        assert numerical == pytest.approx(float(row["probe_normalized"]), abs=5.1e-9)
    assert len(rows) == 5


def test_two_zone_conservation_local_requirement_and_transient_refinement():
    reference = zones(True)
    assert reference["second"] < R(1, 2) < reference["mean"]
    assert zones(True, 2)["second"] > R(1, 2)

    def rhs(state):
        first, second, ledger = state
        transfer = 5 * (1 - first)
        exchange = first - second
        return [transfer - 0.2 - exchange, (-0.4 + exchange) / 2, transfer - 0.6]

    initial = [0.9, 0.7, 0.0]
    coarse = integrate(rhs, initial, 1, 100)
    fine = integrate(rhs, initial, 1, 200)
    matrix = sp.Matrix([[-6, 1], [R(1, 2), R(-1, 2)]])
    steady = sp.Matrix([reference["first"], reference["second"]])
    exact = steady + matrix.exp() * (sp.Matrix([R(9, 10), R(7, 10)]) - steady)
    coarse_error = max(
        abs(c - float(e)) for c, e in zip(coarse[:2], exact, strict=True)
    )
    fine_error = max(abs(c - float(e)) for c, e in zip(fine[:2], exact, strict=True))
    assert fine_error < coarse_error / 10
    assert fine[0] + 2 * fine[1] - (initial[0] + 2 * initial[1]) == pytest.approx(
        fine[2], abs=1e-13
    )


def test_factorial_raw_table_contrasts_residuals_and_simple_effects():
    table = factorial()
    assert table["beta"] == sp.Matrix([10, 2, -1, 3])
    assert table["sse"] == 2 and table["mse"] == R(1, 2)
    means = table["means"]
    low, high = means[1, -1] - means[-1, -1], means[1, 1] - means[-1, 1]
    assert low < 0 < high
    assert (low + high) / 2 == 2 * table["beta"][1]
    assert high - low == 4 * table["beta"][3]


def test_model_packets_and_synthetic_tables_deliver_as_open_practice():
    assert len(NEW) == 20
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 24
    repository = ContentRepository(ROOT / "content")
    for number in range(16, 23):
        lesson = repository.lesson("bioreactors", f"bioreactors-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 19 else 2)
        )
    for number, path in [
        (20, "assignments/probe-response-reference.csv"),
        (22, "assignments/process-evidence-factorial.csv"),
    ]:
        lesson = repository.lesson("bioreactors", f"bioreactors-{number}")
        assert f"/api/v1/courses/bioreactors/resources/{path}" in lesson.markdown
        assert (
            repository.learner_resource("bioreactors", path)
            == (DIRECTORY / path).read_bytes()
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
