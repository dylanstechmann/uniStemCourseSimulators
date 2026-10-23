"""Exact factorization/map, power, projection and inverse-choice cross-checks."""

from __future__ import annotations

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
DIRECTORY = ROOT / "content/courses/linear-algebra"
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
    if re.fullmatch(r"linear-algebra-(1[5-9]|20):depth-\d+", qid)
}


@cache
def calculations():
    a = sp.Matrix([[0, 1, 2], [1, 1, 0], [2, 3, 1]])
    lower, upper, swaps = a.LUdecomposition()
    permutation = sp.eye(3)
    for i, j in swaps:
        permutation.row_swap(i, j)
    assert permutation * a == lower * upper
    s = sp.Matrix([[1, 1], [0, 1]])
    x = s * sp.Matrix([1, 2])
    standard = sp.diag(2, 3)
    mapped, form = s.inv() * standard * s, s.T * standard * s
    j = sp.Matrix([[sp.Rational(1, 2), 2], [0, sp.Rational(1, 2)]])
    start = sp.Matrix([0, 1])
    first, second, third = j * start, j**2 * start, j**3 * start
    flow = sp.Matrix([[-1, 4], [0, -1]]).exp() * start
    contrast = sp.Matrix([[-2, 3], [0, -2]])
    hmax = max(((contrast + contrast.T) / 2).eigenvals())
    rectangular = sp.Matrix([[1, 0, 1], [0, 1, 1], [1, 1, 2], [2, -1, 1]])
    b = sp.Matrix([1, 2, 3, 0])
    minimum = rectangular.pinv() * b
    design = sp.Matrix([[1, 0], [1, 1], [1, 2]])
    observations = sp.Matrix([1, 2, 2])
    q, r = design.QRdecomposition()
    fitted = r.inv() * q.T * observations
    residual = observations - design * fitted
    c, d = sp.Matrix([[3, 1], [1, 3]]), sp.Matrix([2, 4])
    optimizer = c.inv() * d
    minimum_cost = (optimizer.T * c * optimizer)[0] / 2 - d.dot(optimizer)
    dynamics = sp.Matrix(
        [[sp.Rational(3, 5), sp.Rational(3, 2)], [0, sp.Rational(3, 5)]]
    )
    at2, at5 = dynamics**2 * start, dynamics**5 * start
    continuous = (contrast / 2).exp() * start
    inverse_map = sp.Matrix([[1, 1, 0], [0, 0, 2]])
    target = sp.Matrix([2, 2])
    selected = inverse_map.pinv() * target
    output_gram = inverse_map * inverse_map.T
    largest = max(output_gram.eigenvals())
    direction = (output_gram - largest * sp.eye(2)).nullspace()[0]
    retained_output = direction * direction.dot(target) / direction.dot(direction)
    truncated = inverse_map.pinv() * retained_output
    truncation_residual = target - inverse_map * truncated
    ridge = (inverse_map.T * inverse_map + 2 * sp.eye(3)).inv() * inverse_map.T * target
    ridge_residual = target - inverse_map * ridge
    return {
        (15, 1): {
            "l31": lower[2, 0],
            "l32": lower[2, 1],
            "u33": upper[2, 2],
            "determinant": a.det(),
        },
        (15, 2): {
            "x1": x[0],
            "x2": x[1],
            "norm_squared": x.dot(x),
            "pairing": sp.Matrix([1, 2]).dot(x),
        },
        (15, 3): {
            "map_entry": mapped[0, 1],
            "form_entry": form[0, 1],
            "map_trace": sp.trace(mapped),
            "form_trace": sp.trace(form),
        },
        (15, 4): {},
        (16, 1): {
            "x1": first[0],
            "x2": first[1],
            "norm": sp.sqrt(first.dot(first)),
            "eigenspace": len((j - sp.eye(2) / 2).nullspace()),
        },
        (16, 2): {
            "second_first": second[0],
            "second_second": second[1],
            "third_first": third[0],
        },
        (16, 3): {"first": flow[0], "second": flow[1], "norm": sp.sqrt(flow.dot(flow))},
        (16, 4): {"largest": hmax, "envelope": sp.exp(hmax)},
        (17, 1): {
            "rank": rectangular.rank(),
            "nullity": len(rectangular.nullspace()),
            "left_nullity": len(rectangular.T.nullspace()),
        },
        (17, 2): {
            "parameter": minimum[2],
            "norm_squared": minimum.dot(minimum),
            "observable1": (rectangular * minimum)[0],
            "observable2": (rectangular * minimum)[1],
        },
        (17, 3): {
            "pairing": rectangular.T.nullspace()[1].dot(
                sp.Matrix([1, 2, 3, sp.Rational(3, 10)])
            )
        },
        (18, 1): {
            "intercept": fitted[0],
            "slope": fitted[1],
            "residual": sp.sqrt(residual.dot(residual)),
        },
        (18, 2): {
            "first": optimizer[0],
            "second": optimizer[1],
            "minimum": minimum_cost,
        },
        (18, 3): {},
        (19, 1): {
            "first": at2[0],
            "second": at2[1],
            "radius": max(abs(value) for value in dynamics.eigenvals()),
        },
        (19, 2): {"first": at5[0], "second": at5[1]},
        (19, 3): {"first": continuous[0], "second": continuous[1], "largest": hmax},
        (20, 1): {
            "first": selected[0],
            "second": selected[1],
            "third": selected[2],
            "norm": sp.sqrt(selected.dot(selected)),
        },
        (20, 2): {
            "residual": sp.sqrt(truncation_residual.dot(truncation_residual)),
            "input_norm": sp.sqrt(truncated.dot(truncated)),
            "energy_fraction": largest / sp.trace(output_gram),
        },
        (20, 3): {
            "first": ridge[0],
            "second": ridge[1],
            "third": ridge[2],
            "residual": sp.sqrt(ridge_residual.dot(ridge_residual)),
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_linear_keys_recompute_by_exact_matrix_operations_and_actual_grader(qid):
    number, item = map(
        int, re.fullmatch(r"linear-algebra-(\d+):depth-(\d+)", qid).groups()
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


def test_similarity_congruence_metric_and_functional_identities():
    a, s = sp.diag(2, 3), sp.Matrix([[1, 1], [0, 1]])
    mapped, form, gram = s.inv() * a * s, s.T * a * s, s.T * s
    assert mapped.T * gram == gram * mapped
    assert mapped.eigenvals() == a.eigenvals() and form.eigenvals() != a.eigenvals()
    assert all(value > 0 for value in form.eigenvals())
    z, d = sp.Matrix([1, 2]), sp.Matrix([1, 2])
    assert (s * z).dot(s * z) == (z.T * gram * z)[0]
    assert d.dot(s * z) == (s.T * d).dot(z)
    assert s.T * d != s.inv() * d


def test_four_subspaces_weighted_projection_and_quadratic_certificate():
    a = sp.Matrix([[1, 0, 1], [0, 1, 1], [1, 1, 2], [2, -1, 1]])
    for vector in a.nullspace():
        assert a * vector == sp.zeros(4, 1)
    for vector in a.T.nullspace():
        assert a.T * vector == sp.zeros(3, 1)
    design = sp.Matrix([[1, 0], [1, 1], [1, 2]])
    y = sp.Matrix([1, 2, 2])
    w = sp.diag(2, 1, 1)
    projection = design * (design.T * design).inv() * design.T
    assert projection.T == projection and projection**2 == projection
    weighted = (design.T * w * design).inv() * design.T * w * y
    residual = y - design * weighted
    assert design.T * w * residual == sp.zeros(2, 1)
    assert design.T * residual != sp.zeros(2, 1)
    c, d = sp.Matrix([[3, 1], [1, 3]]), sp.Matrix([2, 4])
    optimum = c.inv() * d
    u, v = sp.symbols("u v", real=True)
    z = sp.Matrix([u, v])
    objective = (z.T * c * z)[0] / 2 - d.dot(z)
    best = (optimum.T * c * optimum)[0] / 2 - d.dot(optimum)
    assert (
        sp.simplify(objective - best - ((z - optimum).T * c * (z - optimum))[0] / 2)
        == 0
    )


def test_defective_powers_exponential_and_norm_derivative_contrast():
    j = sp.Matrix([[sp.Rational(1, 2), 2], [0, sp.Rational(1, 2)]])
    nilpotent = j - sp.eye(2) / 2
    assert nilpotent**2 == sp.zeros(2)
    for n in range(1, 9):
        assert (
            j**n
            == sp.Rational(1, 2) ** n * sp.eye(2)
            + n * sp.Rational(1, 2) ** (n - 1) * nilpotent
        )
    start = sp.Matrix([0, 1])
    first = j * start
    assert first.dot(first) > start.dot(start)
    generator = sp.Matrix([[-2, 3], [0, -2]])
    assert all(value < 0 for value in ((generator + generator.T) / 2).eigenvals())
    t = sp.Symbol("t", real=True)
    exact = sp.exp(-2 * t) * sp.Matrix([[1, 3 * t], [0, 1]])
    assert exact.subs(t, 0) == sp.eye(2)
    assert sp.simplify(sp.diff(exact, t) - generator * exact) == sp.zeros(2)


def test_mixed_proof_packets_deliver_and_keep_unreviewed_open_practice():
    assert len(NEW) == 20
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 22
    repository = ContentRepository(ROOT / "content")
    for number in range(15, 21):
        lesson = repository.lesson("linear-algebra", f"linear-algebra-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 17 else 3)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
