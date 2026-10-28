"""Independent geometric, integral, convergence and precision certificates."""

from __future__ import annotations

import json
import math
import re
from decimal import Decimal, ROUND_CEILING, localcontext
from fractions import Fraction as F
from functools import cache
from pathlib import Path

import pytest
import sympy as sp
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/calculus-2"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"calculus-2-(1[6-9]|2[01]):depth-\d+", q["id"])
}
X = sp.symbols("x", real=True)


def simpson(function, left, right, panels=4000):
    step = (right - left) / panels
    return (
        step
        / 3
        * (
            function(left)
            + function(right)
            + 4 * sum(function(left + i * step) for i in range(1, panels, 2))
            + 2 * sum(function(left + i * step) for i in range(2, panels, 2))
        )
    )


@cache
def integer_certificates():
    with localcontext() as context:
        context.prec = 70
        cutoff = (1 / (Decimal(".01").exp() - 1) - 1).to_integral_value(
            rounding=ROUND_CEILING
        )
        slow = Decimal(10).exp().to_integral_value(rounding=ROUND_CEILING)
        bound = 1 / Decimal(100).ln()
        tail = (Decimal(101) / 100).ln()
        assert ((cutoff + 2) / (cutoff + 1)).ln() <= Decimal(".01")
        assert ((cutoff + 1) / cutoff).ln() > Decimal(".01")
        assert 1 / slow.ln() <= Decimal(".1") < 1 / (slow - 1).ln()
        return int(cutoff), int(slow), float(bound), float(tail)


@cache
def calculations():
    line = 2 + X
    length = sp.integrate(sp.sqrt(1 + sp.diff(line, X) ** 2), (X, 0, 2))
    lateral = sp.integrate(
        2 * sp.pi * line * sp.sqrt(1 + sp.diff(line, X) ** 2), (X, 0, 2)
    )
    volume = sp.integrate(sp.pi * line**2, (X, 0, 2))
    closed = lateral + sp.pi * (line.subs(X, 0) ** 2 + line.subs(X, 2) ** 2)
    triangle = sp.integrate(25 * X, (X, 0, sp.Rational(1, 5))) + sp.integrate(
        5 * (2 - 5 * X), (X, sp.Rational(1, 5), sp.Rational(2, 5))
    )
    cutoff, slow, bound, tail = integer_certificates()
    assigned = 1 + 2 * X
    assigned_surface = sp.integrate(
        2 * sp.pi * assigned * sp.sqrt(1 + sp.diff(assigned, X) ** 2), (X, 0, 1)
    )
    assigned_volume = sp.integrate(sp.pi * assigned**2, (X, 0, 1))
    density = 10 * (1 - (X / 3) ** 4)
    amount = sp.integrate(density * 2 * sp.pi * X, (X, 0, 3))
    # The admissible cubic root is obtained trigonometrically, unlike the author's bisection.
    median = sp.sqrt(2 * sp.cos(4 * sp.pi / 9))
    polynomial = sp.integrate(X - X**3 / 3, (X, 0, sp.Rational(1, 2)))
    reference = simpson(math.atan, 0, 0.5)
    b = F(1, 2)
    n = 0
    while b ** (2 * n + 4) / ((2 * n + 3) * (2 * n + 4)) > F(1, 10**6):
        n += 1
    return {
        (16, 1): {"length": length, "lateral": lateral},
        (16, 2): {"volume": volume, "closed": closed},
        (16, 3): {"coverage": 2, "surface": 4 * sp.pi},
        (16, 4): {},
        (17, 1): {
            "global": 1,
            "restricted": F(1, 2) ** 10,
            "index": next(i for i in range(1, 20) if F(1, 2) ** i < F(1, 1000)),
        },
        (17, 2): {"height": 5, "base": F(2, 5), "integral": triangle},
        (17, 3): {"value": sp.exp(-4)},
        (17, 4): {
            "tail": sp.integrate(X**-2, (X, 100, sp.oo)),
            "derivative": sp.summation(
                sp.Rational(1, 2) ** (sp.Symbol("n", integer=True, positive=True) - 1)
                / sp.Symbol("n", integer=True, positive=True),
                (sp.Symbol("n", integer=True, positive=True), 1, sp.oo),
            ),
        },
        (18, 1): {
            "rational": sp.integrate(X / (X**2 + 4 * X + 5), (X, 0, 1)),
            "parts": sp.integrate(X**2 * sp.log(1 + X), (X, 0, 1)),
        },
        (18, 2): {
            "integral": sp.integrate(1 / ((X + 1) * (X + 2)), (X, 0, sp.oo)),
            "cutoff": cutoff,
            "tail": tail,
        },
        (19, 1): {
            "lateral": assigned_surface,
            "volume": assigned_volume,
            "closed": assigned_surface + 10 * sp.pi,
        },
        (19, 2): {"amount": amount, "average": amount / (9 * sp.pi), "median": median},
        (20, 1): {"bound": bound, "index": slow},
        (20, 2): {
            "terms": next(i for i in range(1, 2000) if F(1, i + 1) <= F(1, 1000)),
            "radius": 2,
        },
        (21, 1): {
            "approximation": polynomial,
            "bound": sp.integrate(X**5 / 5, (X, 0, sp.Rational(1, 2))),
            "error": reference - float(polynomial),
        },
        (21, 2): {
            "terms": n + 1,
            "degree": 2 * n + 1,
            "bound": b ** (2 * n + 4) / ((2 * n + 3) * (2 * n + 4)),
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_recomputed_calculus_fields_and_actual_grader_rejects_individual_errors(qid):
    number, item = map(int, re.fullmatch(r"calculus-2-(\d+):depth-(\d+)", qid).groups())
    question, values = NEW[qid], calculations()[number, item]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-11, abs=1e-15)
            figures = spec["significant_figures"]
            response[spec["id"]] = (
                format(value, f".{figures - 1}e") if figures else str(int(value))
            )
    assert grade(question, AttemptRequest(response=response)).correct
    for spec in specs:
        if spec["type"] == "numeric":
            figures = spec["significant_figures"]
            wrong = (
                format(float(values[spec["id"]]) * 1.2, f".{figures - 1}e")
                if figures
                else str(int(values[spec["id"]]) + 1)
            )
        else:
            wrong = str((spec["answer"] + 1) % 3)
        assert not grade(
            question, AttemptRequest(response={**response, spec["id"]: wrong})
        ).correct


def test_geometric_element_coverage_and_admissible_weighted_quantile():
    t = sp.symbols("t", real=True)
    upper = 2 * sp.pi * sp.integrate(sp.sin(t), (t, 0, sp.pi))
    full = 2 * sp.pi * sp.integrate(sp.Abs(sp.sin(t)), (t, 0, 2 * sp.pi))
    assert upper == 4 * sp.pi and full == 2 * upper
    geometry = calculations()[19, 1]
    assert geometry["lateral"] == sp.pi * (1 + 3) * sp.sqrt(5)
    median = float(calculations()[19, 2]["median"])
    cumulative = simpson(
        lambda r: 10 * (1 - (r / 3) ** 4) * 2 * math.pi * r, 0, 3 * median
    )
    assert cumulative / (60 * math.pi) == pytest.approx(0.5, abs=1e-13)
    assert 0 < median < 1


def test_method_integrals_integer_thresholds_and_improper_domains():
    direct = simpson(lambda x: x / (x * x + 4 * x + 5), 0, 1)
    assert direct == pytest.approx(float(calculations()[18, 1]["rational"]), abs=1e-14)
    direct_parts = simpson(lambda x: x * x * math.log1p(x), 0, 1)
    assert direct_parts == pytest.approx(
        float(calculations()[18, 1]["parts"]), abs=1e-14
    )
    cutoff, slow, _, _ = integer_certificates()
    assert cutoff == 99 and slow == 22027
    assert sp.integrate(1 / X, (X, 0, 1)) == sp.oo
    # Use the real negative-side antiderivative explicitly, avoiding a principal complex-log branch.
    assert sp.diff(sp.log(-X), X) == 1 / X
    assert sp.limit(sp.log(-X), X, 0, dir="-") == -sp.oo
    assert F(1, 1000) <= F(1, 1000) < F(1, 999)


def test_function_limit_counterexamples_and_distinct_derivative_hypotheses():
    n = sp.symbols("n", positive=True, integer=True)
    assert sp.limit((1 - 1 / n**2) ** n, n, sp.oo) == 1
    assert sp.limit(1 / (n + 1), n, sp.oo) == 0
    for size in [2, 5, 20]:
        total = sp.integrate(size**2 * X, (X, 0, sp.Rational(1, size))) + sp.integrate(
            size * (2 - size * X), (X, sp.Rational(1, size), sp.Rational(2, size))
        )
        assert total == 1
    flat = sp.exp(-1 / X**2)
    for order in range(5):
        derivative = sp.diff(flat, X, order)
        assert sp.limit(derivative / X, X, 0, dir="+") == 0
        assert sp.limit(derivative / X, X, 0, dir="-") == 0
    assert flat.subs(X, sp.Rational(1, 2)) > 0
    assert sp.summation(1 / n, (n, 1, sp.oo)) == sp.oo


def test_integrated_approximation_precision_and_minimal_sufficient_degree():
    values = calculations()[21, 1]
    exact = simpson(math.atan, 0, 0.5)
    assert 0 < exact - float(values["approximation"]) < float(values["bound"])
    question = NEW["calculus-2-21:depth-1"]
    response = {"approximation": "0.119792", "bound": "5.21e-4", "error": "4.60e-4"}
    assert grade(question, AttemptRequest(response=response)).correct
    for wrong in ["0.120", "0.120252"]:
        assert not grade(
            question, AttemptRequest(response={**response, "approximation": wrong})
        ).correct
    assert float(values["approximation"]) == float(F(23, 192))
    assert abs(float(F("0.119792") - F(23, 192))) == pytest.approx(1 / 3000000)
    chosen = calculations()[21, 2]
    assert chosen["terms"] == 6 and chosen["degree"] == 11
    assert F(1, 2) ** 12 / (11 * 12) > F(1, 10**6) > chosen["bound"]


def test_mixed_calculus_packets_deliver_as_open_partial_coursework():
    assert len(NEW) == 16
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 6, 0)
    assert MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    # 0.7.0 adds the week-6 averages and probability reading.
    assert len(scheduled) == len(set(scheduled)) == 24
    repository = ContentRepository(ROOT / "content")
    for number in range(16, 22):
        lesson = repository.lesson("calculus-2", f"calculus-2-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 18 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
