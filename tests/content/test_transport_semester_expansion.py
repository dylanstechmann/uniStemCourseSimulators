"""Agent-run independent checks for the expanded thermodynamics/transport core."""

from __future__ import annotations

import json
import math
import re
from fractions import Fraction
from pathlib import Path

import pytest
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/transport"
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
    if re.fullmatch(r"transport-(?:1[7-9]|2[0-2]):depth-\d+", qid)
}


def no_flux_step(values, ratio, sink_step=0):
    # Assemble shared face transfers first, then debit/credit adjacent cells.
    faces = (
        [Fraction(0)]
        + [-ratio * (right - left) for left, right in zip(values, values[1:])]
        + [Fraction(0)]
    )
    return [
        value + faces[i] - faces[i + 1] - sink_step * value
        for i, value in enumerate(values)
    ]


def solve(matrix, rhs):
    rows = [
        [Fraction(x) for x in row] + [Fraction(b)]
        for row, b in zip(matrix, rhs, strict=True)
    ]
    for j in range(len(rows)):
        pivot = rows[j][j]
        rows[j] = [v / pivot for v in rows[j]]
        for i in range(len(rows)):
            if i == j:
                continue
            scale = rows[i][j]
            rows[i] = [a - scale * b for a, b in zip(rows[i], rows[j], strict=True)]
    return [row[-1] for row in rows]


def calculations():
    # Exact conservation + ratio equations rather than the author's substituted balance formula.
    ca, cb = solve(
        [[Fraction(".002"), Fraction(".001")], [-3, 1]], [Fraction(".010"), 0]
    )
    ca2, cb2 = solve(
        [[Fraction(".004"), Fraction(".001")], [-2, 1]], [Fraction(".012"), 0]
    )
    # Find the spinodal from the derivative function by bisection, independently of the quadratic roots.
    left, right = 0.001, 0.5
    for _ in range(100):
        x = (left + right) / 2
        if 1 / x + 1 / (1 - x) - 5 > 0:
            left = x
        else:
            right = x
    spinodal = (left + right) / 2
    rt = 8.314 * 300
    electrical = 96485 * (-0.010)
    chemical = rt * math.log(2)
    total = chemical + electrical
    count = max(n for n in range(1, 100) if -9000 + n * total < 0)
    cost3 = rt * math.log(3) + electrical
    count3 = max(n for n in range(1, 100) if -10000 + n * cost3 < 0)
    noflux = no_flux_step(list(map(Fraction, [0, 1, 0])), Fraction(".2"))
    four = solve(
        [[3, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 3]], [4, 0, 0, 0]
    )
    first_flux = Fraction(2) * Fraction("2e-9") * (2 - four[0]) / Fraction(".001")
    assert all(
        -Fraction("2e-9") * (b - a) / Fraction(".001") == first_flux
        for a, b in zip(four, four[1:])
    )
    reservoir_total = 0.004
    total_amount = 0.004 + 0.008
    equilibrium_c = total_amount / reservoir_total
    four_step = no_flux_step(list(map(Fraction, [0, 1, 0, 0])), Fraction(".2"))
    return {
        (17, 1): {
            "alpha": float(ca),
            "beta": float(cb),
            "beta_amount": float(cb * Fraction(".001")),
        },
        (17, 2): {"fraction": (0.7 - 0.4) / (0.7 - 0.1)},
        (17, 3): {
            "curvature": 1 / 0.5 + 1 / (1 - 0.5) - 2 * 2.5,
            "lower": spinodal,
            "upper": 1 - spinodal,
        },
        (17, 4): {"ratio": 4 * 0.5 / 2},
        (18, 1): {"chemical": chemical, "electrical": electrical, "total": total},
        (18, 2): {"count": count},
        (18, 3): {"voltage": math.log(0.5) * rt / 96485},
        (18, 4): {"osmotic": rt * 2, "flux": (8000 - rt * 2) / 1e12},
        (19, 1): {
            "diffusion_step": 1 / (2 * 2e-9 / 0.0001**2),
            "combined_step": 1 / (2 * 2e-9 / 0.0001**2 + 0.1),
        },
        (19, 2): dict(
            zip(["first", "center", "last"], map(float, noflux), strict=True)
        ),
        (19, 3): {
            "first": float(four[0]),
            "last": float(four[-1]),
            "flux": float(first_flux),
        },
        (19, 4): {"bound": 1 / 3},
        (20, 1): {"ratio": float(cb2 / ca2), "alpha": float(ca2), "beta": float(cb2)},
        (20, 2): {"fraction": (0.75 - 0.3) / (0.75 - 0.15)},
        (21, 1): {"cost": cost3, "count": count3},
        (21, 2): {
            "volume_a": 0.004 / equilibrium_c,
            "volume_b": 0.008 / equilibrium_c,
            "initial_flow": 0.001 * 1e-12 * rt * (0.008 / 0.002 - 0.004 / 0.002),
        },
        (22, 1): dict(
            zip(["first", "second", "third"], map(float, four_step[:3]), strict=True)
        ),
        (22, 2): {
            "length": math.sqrt(2e-9 / 0.002),
            "ratio": (0.004 / 4) / math.sqrt(2e-9 / 0.002),
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_new_numeric_fields_recompute_and_grade(qid):
    number, item = map(int, re.fullmatch(r"transport-(\d+):depth-(\d+)", qid).groups())
    values = calculations()[(number, item)]
    question = NEW[qid]
    numeric = {
        s["id"]: s
        for s in question["solution_spec"]["field_specs"]
        if s["type"] == "numeric"
    }
    assert set(values) == set(numeric)
    response = {}
    for spec in question["solution_spec"]["field_specs"]:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        elif spec["significant_figures"] is None:
            assert float(values[spec["id"]]).is_integer()
            response[spec["id"]] = str(int(values[spec["id"]]))
        else:
            assert values[spec["id"]] == pytest.approx(
                spec["answer"], rel=1e-10, abs=1e-14
            )
            response[spec["id"]] = format(values[spec["id"]], ".2e")
    result = grade(question, AttemptRequest(response=response))
    assert result.correct, result.feedback
    for fid, value in values.items():
        assert not grade(
            question,
            AttemptRequest(response={**response, fid: format(value * 1.2, ".2e")}),
        ).correct


def test_new_foundations_and_coursework_are_delivered_and_scheduled_once():
    assert len(NEW) == 18
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 6, 0)
    assert MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [
        lid for week in MANIFEST["duration"]["weeks"] for lid in week["lesson_ids"]
    ]
    # 0.7.0 adds the week-1 closed-system first-law reading.
    assert len(scheduled) == len(set(scheduled)) == 25
    content = ContentRepository(ROOT / "content")
    for number in range(17, 23):
        lesson = content.lesson("transport", f"transport-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 20 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )


def test_curvature_and_coexistence_are_distinct_for_the_stipulated_regular_solution():
    def g(x):
        return x * math.log(x) + (1 - x) * math.log(1 - x) + 3 * x * (1 - x)

    def slope(x):
        return math.log(x / (1 - x)) + 3 * (1 - 2 * x)

    left, right = 0.001, 0.2
    for _ in range(100):
        mid = (left + right) / 2
        if slope(mid) < 0:
            left = mid
        else:
            right = mid
    coexist = (left + right) / 2
    spinodal = (1 - math.sqrt(1 - 2 / 3)) / 2
    assert coexist < spinodal < 0.5
    assert g(coexist) == pytest.approx(g(1 - coexist))
    assert abs(slope(coexist)) < 1e-12
    assert g(coexist) < g(0.5)
    h = 1e-4
    curvature = (g(0.5 + h) - 2 * g(0.5) + g(0.5 - h)) / h**2
    assert curvature == pytest.approx(-2, abs=1e-6)


def test_shared_face_update_preserves_amount_and_exposes_a_positivity_failure():
    initial = list(map(Fraction, [1, 0, 0]))
    first = no_flux_step(initial, Fraction(".25"))
    second = no_flux_step(first, Fraction(".25"))
    assert second == list(map(Fraction, [".625", ".3125", ".0625"]))
    assert sum(second) == sum(initial)
    failure = no_flux_step(list(map(Fraction, [0, 1, 0])), Fraction(".6"))
    assert failure[1] < 0 and sum(failure) == 1
    with_sink = no_flux_step(initial, Fraction(".2"), Fraction(".1"))
    assert sum(with_sink) == Fraction(".9") * sum(initial)


def test_closed_reservoir_direction_and_equilibrium_are_independent_of_a_solver():
    # Dimensionless volume fraction u; its equilibrium is p=1/3.
    p = 1 / 3

    def rate(u):
        return p / u - (1 - p) / (1 - u)

    assert rate(0.5) < 0 and rate(p) == pytest.approx(0)
    u = 0.5
    for _ in range(500):
        h = 0.01
        k1 = rate(u)
        k2 = rate(u + h * k1 / 2)
        k3 = rate(u + h * k2 / 2)
        k4 = rate(u + h * k3)
        u += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        assert 0 < u < 1
    assert u == pytest.approx(p, abs=1e-9)
    assert 0.004 / (0.004 * u) == pytest.approx(0.008 / (0.004 * (1 - u)), rel=1e-8)
