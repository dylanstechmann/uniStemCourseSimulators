"""Independent exact/explicit-branch and finite-sum checks for mixed calculus work."""

from __future__ import annotations

import json
import re
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from pathlib import Path

import pytest
import sympy as sp
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/calculus-1"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
BANK = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
}
NEW = {
    qid: q
    for qid, q in BANK.items()
    if re.fullmatch(r"calculus-1-(1[6-9]|20):depth-\d+", qid)
}
X = sp.Symbol("x", real=True)


def integral(polynomial, start, stop):
    return sp.integrate(polynomial, (X, start, stop))


def finite_sum(length, slope, intercept, count, right):
    step = Fraction(length, count)
    indices = range(1, count + 1) if right else range(count)
    return sum((slope * i * step + intercept) * step for i in indices)


def newton_reference():
    with localcontext() as context:
        context.prec = 50
        start = Decimal("0.5")
        iterate = start - (start + start.exp() - 2) / (1 + start.exp())
        residual = iterate + iterate.exp() - 2
        return iterate, residual, abs(residual) / 2


@cache
def calculations():
    branch = (-X + sp.sqrt(28 - 3 * X**2)) / 2
    first = sp.diff(branch, X).subs(X, 1)
    second = sp.diff(branch, X, 2).subs(X, 1)
    box = X * (14 - 2 * X) * (10 - 2 * X)
    candidates = [r for r in sp.solve(sp.diff(box, X), X) if 0 < r < 5]
    assert len(candidates) == 1
    cut = candidates[0]
    cubic = X**3 - 3 * X
    secant = (cubic.subs(X, 2) - cubic.subs(X, -2)) / 4
    matching = sorted(sp.solve(sp.diff(cubic, X) - secant, X))
    iterate, residual, bound = newton_reference()
    base_rate, final_rate = 2 * X - 2, 2 * X - 3
    moving = sp.integrate(X**2 - 1, (X, X, 2 * X))
    return {
        (16, 1): {
            "left": finite_sum(3, 2, -2, 6, False),
            "right": finite_sum(3, 2, -2, 6, True),
            "trapezoid": integral(base_rate, 0, 3),
        },
        (16, 2): {
            "net": integral(base_rate, 0, 3),
            "distance": -integral(base_rate, 0, 1) + integral(base_rate, 1, 3),
            "final": 10 + integral(base_rate, 0, 3),
        },
        (16, 3): {},
        (16, 4): {
            "value": moving.subs(X, 1),
            "derivative": sp.diff(moving, X).subs(X, 1),
        },
        (17, 1): {
            "value": sp.limit((X**2 - 9) / (X - 3), X, 3),
            "slope": sp.limit(((X**2 - 9) / (X - 3) - 6) / (X - 3), X, 3),
        },
        (17, 2): {
            "delta": min(Fraction(1), Fraction(".05") / 5),
            "secant": (Fraction("2.02") ** 2 - 4) / Fraction(".02"),
            "error": (Fraction("2.02") ** 2 - 4) / Fraction(".02") - 4,
        },
        (17, 3): {},
        (18, 1): {"first": first, "second": second, "inverse": 1 / first},
        (18, 2): {
            "log_first": sp.diff(sp.log(branch), X).subs(X, 1),
            "log_second": sp.diff(sp.log(branch), X, 2).subs(X, 1),
            "tangent": 2 + first * sp.Rational(1, 20),
        },
        (18, 3): {
            "vertical": -Fraction(5, 12) * Fraction(".6"),
            "angle": -Fraction(".6") / 12,
            "area": (5 * (-Fraction(5, 12) * Fraction(".6")) + 12 * Fraction(".6")) / 2,
        },
        (19, 1): {
            "cut": cut,
            "volume": box.subs(X, cut),
            "capped": box.subs(X, sp.Rational(3, 2)),
        },
        (19, 2): {"secant": secant, "positive": matching[1], "negative": matching[0]},
        (19, 3): {"iterate": iterate, "residual": residual, "bound": bound},
        (20, 1): {
            "net": integral(final_rate, 0, 4),
            "distance": -integral(final_rate, 0, sp.Rational(3, 2))
            + integral(final_rate, sp.Rational(3, 2), 4),
            "final": 7 + integral(final_rate, 0, 4),
            "minimum": 7 + integral(final_rate, 0, sp.Rational(3, 2)),
        },
        (20, 2): {
            "left": finite_sum(4, 2, -3, 8, False),
            "right": finite_sum(4, 2, -3, 8, True),
            "intervals": next(
                n
                for n in range(1, 1000)
                if abs(finite_sum(4, 2, -3, n, True) - 4) <= Fraction(".05")
            ),
        },
        (20, 3): {
            "net": -2 * 2 + 3 * 2,
            "absolute": 2 * 2 + 3 * 2,
            "moving": sp.diff(moving, X).subs(X, 1),
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_mixed_calculus_keys_recompute_and_actual_grader_checks_each_field(qid):
    number, item = map(int, re.fullmatch(r"calculus-1-(\d+):depth-(\d+)", qid).groups())
    values = calculations()[(number, item)]
    question = NEW[qid]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-12, abs=1e-15)
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


def test_sum_sign_and_discontinuity_checks_are_independent_of_a_rounded_answer():
    for n in [1, 2, 6, 11]:
        left = finite_sum(3, 2, -2, n, False)
        right = finite_sum(3, 2, -2, n, True)
        assert left <= 3 <= right and (left + right) / 2 == 3
        assert right - 3 == Fraction(9, n)
    assert abs(integral(2 * X - 3, 0, 4)) < -integral(
        2 * X - 3, 0, sp.Rational(3, 2)
    ) + integral(2 * X - 3, sp.Rational(3, 2), 4)
    # Compute jump accumulation branches and one-sided slopes directly.
    first = -2 * X
    second = -4 + 3 * (X - 2)
    assert first.subs(X, 2) == second.subs(X, 2) == -4
    assert sp.diff(first, X) != sp.diff(second, X)
    text = (
        DIRECTORY / "modules/piecewise-rates-and-integral-hypotheses.md"
    ).read_text()
    assert "single-point contribution has zero width" in text
    assert "largest local difference" in text


def test_domain_optimization_and_root_certificate_have_independent_checks():
    box = X * (14 - 2 * X) * (10 - 2 * X)
    values = calculations()
    cut = values[(19, 1)]["cut"]
    assert 0 < cut < 5 and box.subs(X, 0) == box.subs(X, 5) == 0
    assert sp.diff(box, X, 2).subs(X, cut) < 0
    assert values[(19, 1)]["volume"] > values[(19, 1)]["capped"]
    # Independent bisection reference verifies the MVT location certificate.
    with localcontext() as context:
        context.prec = 50
        lo, hi = Decimal(0), Decimal(1)
        for _ in range(100):
            mid = (lo + hi) / 2
            if mid + mid.exp() - 2 > 0:
                hi = mid
            else:
                lo = mid
        iterate, _, bound = newton_reference()
        assert abs(iterate - (lo + hi) / 2) < bound
        assert bound < Decimal(".002")
    branch = (-X + sp.sqrt(28 - 3 * X**2)) / 2
    assert sp.simplify(X**2 + X * branch + branch**2 - 7) == 0
    assert branch.subs(X, 1) == 2


def test_sustained_packets_deliver_and_remain_open_unreviewed_practice():
    assert len(NEW) == 16
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 6, 0)
    assert MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    # 0.7.0 adds the week-3 trigonometric reading.
    assert len(scheduled) == len(set(scheduled)) == 23
    repository = ContentRepository(ROOT / "content")
    for number in range(16, 21):
        lesson = repository.lesson("calculus-1", f"calculus-1-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number == 16 else 3)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
