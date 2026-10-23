"""Independent joint-law, likelihood, posterior, regression and finite-inference checks."""

from __future__ import annotations

import itertools
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
DIRECTORY = ROOT / "content/courses/statistics"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"statistics-(1[89]|2[0-5]):depth-\d+", q["id"])
}
X, Y = sp.symbols("x y", real=True)


def triangle_integral(expression, density):
    return sp.integrate(sp.integrate(expression * density, (Y, 0, X)), (X, 0, 1))


def likelihood_reference(records):
    rate = sp.symbols("rate", positive=True)
    log_likelihood = sum(
        int(event) * sp.log(rate) - rate * time for time, event in records
    )
    estimate = sp.solve(sp.diff(log_likelihood, rate), rate)[0]
    information = -sp.diff(log_likelihood, rate, 2).subs(rate, estimate)
    return estimate, 1 / estimate, information, 1 / sp.sqrt(information)


def posterior_reference(prior_mean, prior_variance, sample_mean, known_variance, count):
    mu = sp.symbols("mu", real=True)
    # Obtain mode and curvature from the original quadratic exponent, not the update recipe.
    exponent = (mu - prior_mean) ** 2 / (2 * prior_variance) + count * (
        mu - sample_mean
    ) ** 2 / (2 * known_variance)
    mean = sp.solve(sp.diff(exponent, mu), mu)[0]
    variance = 1 / sp.diff(exponent, mu, 2)
    assert (
        sp.simplify(
            exponent - exponent.subs(mu, mean) - (mu - mean) ** 2 / (2 * variance)
        )
        == 0
    )
    return mean, variance


def regression_reference(rows, point):
    design = sp.Matrix([[1, x, z] for x, z, y in rows])
    response = sp.Matrix([y for x, z, y in rows])
    coefficients = design.QRsolve(response)
    residual = response - design * coefficients
    sse = (residual.T * residual)[0]
    degrees = len(rows) - design.rank()
    mse = sse / degrees
    h = sp.Matrix([point])
    leverage = (h * (design.T * design).inv() * h.T)[0]
    return (
        coefficients,
        residual,
        sse,
        degrees,
        mse,
        (h * coefficients)[0],
        sp.sqrt(mse * leverage),
        sp.sqrt(mse * (1 + leverage)),
    )


REHEARSAL = [(0, 0, 2), (0, 1, 3), (1, 1, 4), (1, 2, 11), (2, 2, 12), (2, 3, 13)]
ASSIGNMENT = [
    (-1, -1, F(3, 2)),
    (-1, 1, F(-7, 2)),
    (0, -1, 4),
    (0, 1, 2),
    (1, -1, F(19, 2)),
    (1, 1, F(9, 2)),
]


@cache
def calculations():
    ex = triangle_integral(X, 2)
    ey = triangle_integral(Y, 2)
    vx = triangle_integral((X - ex) ** 2, 2)
    vy = triangle_integral((Y - ey) ** 2, 2)
    cov = triangle_integral((X - ex) * (Y - ey), 2)
    rate, mean, info, se = likelihood_reference(
        [(2, True), (3, False), (5, True), (6, False)]
    )
    pm, pv = posterior_reference(4, 4, 6, 16, 3)
    coefficients, residual, sse, degrees, mse, prediction, mean_se, new_se = (
        regression_reference(REHEARSAL, [1, 1, F(3, 2)])
    )
    assigned, _, asse, _, _, apred, amean, anew = regression_reference(
        ASSIGNMENT, [1, 0, 0]
    )
    arate, amean_wait, ainfo, ase = likelihood_reference(
        [(1, True), (2, True), (3, False), (4, True), (2, False)]
    )
    am, av = posterior_reference(0, 4, 3, 4, 4)
    objects = [1, 1, 0, 0, 0]
    counts = [
        sum(objects[i] for i in pair) for pair in itertools.combinations(range(5), 2)
    ]
    expected = sum(counts) / len(counts)
    variance = sum((k - expected) ** 2 for k in counts) / len(counts)
    return {
        (18, 1): {"normalization": triangle_integral(1, 2), "mean_x": ex, "mean_y": ey},
        (18, 2): {"covariance": cov, "correlation": cov / sp.sqrt(vx * vy)},
        (18, 3): {
            "event": sp.integrate(2 * (1 - Y), (Y, 0, F(1, 4))),
            "conditional": F(3, 10),
        },
        (18, 4): {"within": triangle_integral(X**2 / 12, 2), "between": vx / 4},
        (19, 1): {"rate": rate, "mean": mean},
        (19, 2): {"information": info, "standard_error": se},
        (19, 3): {"ratio": sp.exp(2 * sp.log(2) - 2), "log_ratio": 2 * sp.log(2) - 2},
        (19, 4): {
            "mle": F(7, 10),
            "ratio": (F(1, 2) / F(7, 10)) ** 7 * (F(1, 2) / F(3, 10)) ** 3,
        },
        (20, 1): {"mean": pm, "variance": pv},
        (20, 2): {"single_sd": sp.sqrt(16 + pv), "average_sd": sp.sqrt(8 + pv)},
        (20, 3): {"covariance": pv, "correlation": pv / (16 + pv)},
        (20, 4): {
            "lower": pm - F(49, 25) * sp.sqrt(pv),
            "upper": pm + F(49, 25) * sp.sqrt(pv),
        },
        (21, 1): {
            "intercept": coefficients[0],
            "slope_x": coefficients[1],
            "slope_z": coefficients[2],
        },
        (21, 2): {"simple": 5, "full": coefficients[1], "shift": 5 - coefficients[1]},
        (21, 3): {"sse": sse, "degrees": degrees, "mse": mse},
        (21, 4): {"prediction": prediction, "mean_se": mean_se, "new_se": new_se},
        (22, 1): {
            "pairs": len(counts),
            "mean": expected,
            "variance": variance,
            "covariance": F(1, 10) - F(4, 25),
        },
        (22, 2): {
            "mean_x": triangle_integral(X, 6 * Y),
            "mean_y": triangle_integral(Y, 6 * Y),
            "event": sp.integrate(6 * Y * (1 - Y), (Y, 0, F(1, 2))),
            "conditional": F(2, 5),
        },
        (23, 1): {
            "coverage": F(14, 16),
            "miss": F(2, 16),
            "upper": 1 - sp.Rational(1, 40) ** sp.Rational(1, 4),
        },
        (23, 2): {"allocations": 6, "extreme": 2, "difference": 3, "p_value": F(1, 3)},
        (24, 1): {
            "intercept": assigned[0],
            "slope_x": assigned[1],
            "slope_z": assigned[2],
            "sse": asse,
        },
        (24, 2): {"prediction": apred, "mean_se": amean, "new_se": anew},
        (25, 1): {
            "rate": arate,
            "mean": amean_wait,
            "information": ainfo,
            "standard_error": ase,
        },
        (25, 2): {
            "posterior_mean": am,
            "posterior_variance": av,
            "predictive_sd": sp.sqrt(4 + av),
            "future_covariance": av,
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_recomputed_statistical_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(int, re.fullmatch(r"statistics-(\d+):depth-(\d+)", qid).groups())
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


def test_joint_density_marginals_total_variance_and_zero_covariance_dependence():
    for density in [sp.Integer(2), 6 * Y]:
        marginal_x = sp.integrate(density, (Y, 0, X))
        marginal_y = sp.integrate(density, (X, Y, 1))
        assert (
            triangle_integral(1, density)
            == sp.integrate(marginal_x, (X, 0, 1))
            == sp.integrate(marginal_y, (Y, 0, 1))
            == 1
        )
        conditional = sp.cancel(density / marginal_x)
        cm = sp.integrate(Y * conditional, (Y, 0, X))
        cv = sp.integrate((Y - cm) ** 2 * conditional, (Y, 0, X))
        overall = sp.integrate(Y * marginal_y, (Y, 0, 1))
        direct = sp.integrate((Y - overall) ** 2 * marginal_y, (Y, 0, 1))
        within = sp.integrate(cv * marginal_x, (X, 0, 1))
        between = sp.integrate((cm - overall) ** 2 * marginal_x, (X, 0, 1))
        assert sp.simplify(direct - within - between) == 0
        assert conditional.subs(X, sp.Rational(3, 5)) != marginal_y
    pairs = [(-1, 1), (0, 0), (1, 1)]
    ex = sum(F(x, 3) for x, y in pairs)
    ey = sum(F(y, 3) for x, y in pairs)
    assert sum(F(x * y, 3) for x, y in pairs) - ex * ey == 0
    assert sum(x == 0 and y == 0 for x, y in pairs) / 3 != (1 / 3) * (1 / 3)


def test_likelihood_original_score_curvature_censoring_and_boundary():
    rate, mean, info, se = likelihood_reference(
        [(2, True), (3, False), (5, True), (6, False)]
    )
    assert rate == sp.Rational(1, 8) and mean == 8 and info == 128
    lam, m = sp.symbols("lambda m", positive=True)
    loglike = 2 * sp.log(lam) - 16 * lam
    assert sp.diff(loglike, lam).subs(lam, rate) == 0
    assert sp.diff(loglike, lam, 2).subs(lam, rate) < 0
    assert sp.solve(sp.diff(loglike.subs(lam, 1 / m), m), m) == [mean]
    assert (
        sp.diff(-16 * lam, lam) < 0
        and sp.limit(sp.exp(-16 * lam), lam, 0, dir="+") == 1
    )
    # A change from one time unit to a half-sized unit doubles exposures and halves rate.
    scaled = likelihood_reference([(4, True), (6, False), (10, True), (12, False)])
    assert scaled[0] == rate / 2 and scaled[1] == 2 * mean
    assert sp.simplify(se**2 - 1 / info) == 0
    p = sp.symbols("p", positive=True)
    assert sp.solve(sp.diff(7 * sp.log(p) + 3 * sp.log(1 - p), p), p) == [
        sp.Rational(7, 10)
    ]


def test_normal_completed_square_predictive_moments_and_shared_covariance():
    mean, variance = posterior_reference(4, 4, 6, 16, 3)
    assert mean == sp.Rational(34, 7) and variance == sp.Rational(16, 7)
    mu = sp.symbols("mu", real=True)
    density = sp.exp(-((mu - mean) ** 2) / (2 * variance)) / sp.sqrt(
        2 * sp.pi * variance
    )
    assert sp.integrate(density, (mu, -sp.oo, sp.oo)) == 1
    assert sp.integrate(mu * density, (mu, -sp.oo, sp.oo)) == mean
    assert sp.integrate((mu - mean) ** 2 * density, (mu, -sp.oo, sp.oo)) == variance
    prediction = 16 + variance
    assert variance / prediction == sp.Rational(1, 8)
    assert (2 * prediction + 2 * variance) / 4 == 8 + variance
    assert 16 / sp.Integer(100) + variance > variance
    # Work through the distinct worked example, checking the text's variance versus SD targets.
    wm, wv = posterior_reference(5, 9, 8, 9, 4)
    assert wm == sp.Rational(37, 5) and wv == sp.Rational(9, 5)
    assert 9 + wv == sp.Rational(54, 5) and 9 / sp.Integer(3) + wv == sp.Rational(24, 5)


def test_multiple_regression_qr_residualization_rank_and_prediction():
    coefficients, residual, sse, degrees, mse, prediction, mean_se, new_se = (
        regression_reference(REHEARSAL, [1, 1, F(3, 2)])
    )
    design = sp.Matrix([[1, x, z] for x, z, y in REHEARSAL])
    response = sp.Matrix([y for x, z, y in REHEARSAL])
    assert design.T * residual == sp.zeros(3, 1)
    nuisance = design[:, [0, 2]]
    project = nuisance * (nuisance.T * nuisance).inv() * nuisance.T
    rx = (sp.eye(6) - project) * design[:, 1]
    ry = (sp.eye(6) - project) * response
    partial = (rx.T * ry)[0] / (rx.T * rx)[0]
    assert partial == coefficients[1] == 2
    xs = [F(x) for x, z, y in REHEARSAL]
    ys = [F(y) for x, z, y in REHEARSAL]
    xbar = sum(xs) / 6
    ybar = sum(ys) / 6
    simple = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / sum(
        (x - xbar) ** 2 for x in xs
    )
    assert simple == 5
    assert sse == 12 and degrees == 3 and mse == 4 and prediction == F(15, 2)
    assert sp.simplify(new_se**2 - mean_se**2) == mse
    deficient = sp.Matrix([[1, x, x] for x in range(6)])
    assert deficient.rank() == 2 and deficient * sp.Matrix(
        [1, 2, 3]
    ) == deficient * sp.Matrix([1, 4, 1])


def test_exact_binomial_coverage_bootstrap_boundary_and_inclusive_randomization():
    coverage = F(0)
    exact_coverage = F(0)
    for count in range(5):
        probability = F(math.comb(4, count), 16)
        observed = count / 4
        half = 1.96 * math.sqrt(observed * (1 - observed) / 4)
        if observed - half <= 0.5 <= observed + half:
            coverage += probability
        low_tail = sum(F(math.comb(4, k), 16) for k in range(count + 1))
        high_tail = sum(F(math.comb(4, k), 16) for k in range(count, 5))
        if min(low_tail, high_tail) >= F(1, 40):
            exact_coverage += probability
    assert coverage == F(7, 8) and exact_coverage == 1
    upper = 1 - 0.025**0.25
    assert (1 - upper) ** 4 == pytest.approx(0.025)
    assert {sum(sample) for sample in itertools.product([0], repeat=4)} == {0}
    observed = [0, 1, 3, 4]
    statistics = []
    for allocation in itertools.combinations(range(4), 2):
        treated = sum(observed[i] for i in allocation) / 2
        control = sum(observed[i] for i in range(4) if i not in allocation) / 2
        statistics.append(treated - control)
    assert sorted(statistics) == [-3, -1, 0, 0, 1, 3]
    assert F(sum(abs(t) >= 3 for t in statistics), len(statistics)) == F(1, 3)
    assert sum(abs(t) > 3 for t in statistics) == 0


def test_statistical_packets_deliver_as_open_partial_coursework():
    assert len(NEW) == 24
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 27
    repository = ContentRepository(ROOT / "content")
    for number in range(18, 26):
        lesson = repository.lesson("statistics", f"statistics-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 22 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
