"""Independent implicit, coordinate-coverage, singular-limit and flux references."""

from __future__ import annotations
import json
import re
import math
from functools import cache
from pathlib import Path
import pytest
import sympy as sp
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/calculus-3"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"calculus-3-(1[5-9]|2[01]):depth-\d+", q["id"])
}
R = sp.Rational


@cache
def calculations():
    x, y, r, theta = sp.symbols("x y r theta", positive=True)
    z = sp.sqrt(1 - x * x - y * y)
    point = {x: R(1, 3), y: R(2, 3)}
    gx = sp.diff(z, x).subs(point)
    gy = sp.diff(z, y).subs(point)
    f = (x * x - y * y) / (x * x + y * y) ** 2
    yfirst = sp.integrate(sp.integrate(f, (y, 0, 1)), (x, 0, 1))
    xfirst = sp.integrate(sp.integrate(f, (x, 0, 1)), (y, 0, 1))
    a = sp.symbols("a", positive=True)

    def cutoff(c):
        return sp.limit(
            sp.pi / 4 - sp.atan(c * a) - sp.atan(1 / a) + sp.atan(c), a, 0, dir="+"
        )

    def area(lo, hi):
        return sp.integrate(2 * sp.pi * r, (r, lo, hi))

    def mass(lo, hi):
        return sp.integrate(2 * sp.pi * r**3, (r, lo, hi))

    top = sp.integrate(2 * sp.pi * (4 - r**4) * r, (r, 0, 1))
    volume = sp.integrate(2 * sp.pi * (1 - r * r) * r, (r, 0, 1))
    scalar = sp.integrate(2 * sp.pi * sp.sqrt(1 + 4 * r * r) * r, (r, 0, 1))
    return {
        (15, 1): dict(
            partial_x=gx, partial_y=gy, surface_factor=sp.sqrt(1 + gx * gx + gy * gy)
        ),
        (15, 2): dict(
            hessian_xx=sp.diff(z, x, 2).subs(point),
            hessian_xy=sp.diff(z, x, y).subs(point),
            hessian_yy=sp.diff(z, y, 2).subs(point),
        ),
        (15, 3): dict(
            vertical_rate=gx / 10 + gy / 20,
            speed=sp.sqrt(R(1, 100) + R(1, 400) + (gx / 10 + gy / 20) ** 2),
        ),
        (15, 4): dict(derivative=R(1, 3), branches=3),
        (16, 1): dict(jacobian=8, radius=2),
        (16, 2): dict(pullback=2 * area(1, 4), distinct=area(1, 4), multiplicity=2),
        (16, 3): dict(
            total=mass(1, 4),
            average=mass(1, 4) / area(1, 4),
            full_pullback=2 * mass(1, 4),
        ),
        (16, 4): dict(angle_length=sp.pi),
        (17, 1): dict(y_first=yfirst, x_first=xfirst),
        (17, 2): dict(ratio_two=cutoff(2), ratio_half=cutoff(R(1, 2))),
        (17, 3): dict(angular=1, absolute=sp.integrate(1 / r, (r, R(1, 100), 1))),
        (17, 4): {},
        (18, 1): dict(
            partial_x=-1 / (2 * sp.sqrt(2)),
            partial_y=-1 / sp.sqrt(2),
            new_z=sp.sqrt(R(401, 200)),
            error=sp.sqrt(R(401, 200)) - sp.sqrt(2),
        ),
        (18, 2): dict(maximum=2, minimum=sp.sqrt(7) / 2, maximizers=2),
        (19, 1): dict(area=4, total=6, average=R(3, 2), jacobian=2),
        (19, 2): dict(
            area=area(1, 8),
            full_area=3 * area(1, 8),
            density=mass(1, 8),
            multiplicity=3,
        ),
        (20, 1): dict(top=top, bottom=-sp.pi, net=top - sp.pi, volume=volume),
        (20, 2): dict(circulation=2 * sp.pi, area=scalar),
        (21, 1): dict(y_first=yfirst, x_first=xfirst, ratio_three=cutoff(3)),
        (21, 2): dict(outer=6 * sp.pi, inner=-2 * sp.pi, sum=4 * sp.pi),
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_multivariable_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(int, re.fullmatch(r"calculus-3-(\d+):depth-(\d+)", qid).groups())
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


def test_implicit_hessian_tangency_fold_and_full_segment_bound():
    x, y = sp.symbols("x y", real=True)
    z = sp.sqrt(4 - x * y)
    h = sp.hessian(z, (x, y))
    point = {x: 2, y: 1}
    delta = sp.Matrix([R(1, 10), -R(1, 20)])
    assert (sp.Matrix([[sp.diff(z, x), sp.diff(z, y)]]).subs(point) * delta)[0] == 0
    bound = sp.Matrix(
        [
            [
                R(121, 100) / (4 * R(13, 10) ** 3),
                1 / (2 * R(13, 10)) + R(231, 100) / (4 * R(13, 10) ** 3),
            ],
            [
                1 / (2 * R(13, 10)) + R(231, 100) / (4 * R(13, 10) ** 3),
                R(441, 100) / (4 * R(13, 10) ** 3),
            ],
        ]
    )
    assert sp.sqrt(sum(v * v for v in bound)) < 2
    assert calculations()[18, 1]["error"] < delta.dot(delta)
    curve = 3 * y - y**3
    assert (
        curve.subs(y, 1) == 2
        and sp.diff(curve, y).subs(y, 1) == 0
        and sp.diff(curve, y, 2).subs(y, 1) < 0
    )
    assert sp.solve(y**3 - 3 * y, y) == [-sp.sqrt(3), 0, sp.sqrt(3)] or set(
        sp.solve(y**3 - 3 * y, y)
    ) == {0, -sp.sqrt(3), sp.sqrt(3)}
    assert sp.simplify(h[0, 1] + 1 / (2 * z) + x * y / (4 * z**3)) == 0


def test_polynomial_jacobians_and_once_covered_target_measures():
    u, v, r = sp.symbols("u v r", real=True)
    square = sp.Matrix([u * u - v * v, 2 * u * v])
    cube = sp.Matrix([u**3 - 3 * u * v * v, 3 * u * u * v - v**3])
    assert sp.expand(square.jacobian([u, v]).det() - 4 * (u * u + v * v)) == 0
    assert sp.expand(cube.jacobian([u, v]).det() - 9 * (u * u + v * v) ** 2) == 0
    for degree, map_ in [(2, square), (3, cube)]:
        assert sp.expand(map_.dot(map_) - (u * u + v * v) ** degree) == 0
        assert sp.integrate(
            degree**2 * r ** (2 * degree - 2) * 2 * sp.pi * r, (r, 1, 2)
        ) == degree * sp.pi * (2 ** (2 * degree) - 1)
    # A separate wedge is directly integrable in physical coordinates.
    x, y = sp.symbols("x y", positive=True)
    assert sp.integrate(sp.integrate(x / y, (x, y, 2 * y)), (y, 1, 3)) == 6


def test_signed_integrals_fail_absolute_integrability_and_cutoff_independence():
    t, eps = sp.symbols("t eps", positive=True)
    angular = sp.integrate(sp.cos(2 * t), (t, 0, sp.pi / 4)) - sp.integrate(
        sp.cos(2 * t), (t, sp.pi / 4, sp.pi / 2)
    )
    assert angular == 1
    assert sp.limit(sp.integrate(1 / t, (t, eps, 1)), eps, 0, dir="+") == sp.oo
    c = calculations()
    assert c[17, 1]["y_first"] == -c[17, 1]["x_first"] == sp.pi / 4
    assert float(c[17, 2]["ratio_two"]) == pytest.approx(math.atan(1 / 3))
    assert float(c[21, 1]["ratio_three"]) == pytest.approx(math.atan(0.5))


def test_curved_flux_curl_scalar_measure_and_loop_orientation():
    r, z, t = sp.symbols("r z t", real=True)
    volume_div = sp.integrate(
        sp.integrate(4 * z * 2 * sp.pi * r, (z, 1, 2 - r * r)), (r, 0, 1)
    )
    assert volume_div == calculations()[20, 1]["net"] == 8 * sp.pi / 3
    assert sp.integrate((4 - 4 * r * r) * 2 * sp.pi * r, (r, 0, 1)) == 2 * sp.pi
    for radius, traversals in [(2, 3), (1, -1)]:
        path = sp.Matrix([radius * sp.cos(t), radius * sp.sin(t), 1])
        field = sp.Matrix([-path[1] / radius**2, path[0] / radius**2, 0])
        assert sp.simplify(field.dot(sp.diff(path, t))) == 1
        assert (
            sp.integrate(field.dot(sp.diff(path, t)), (t, 0, 2 * sp.pi * traversals))
            == 2 * sp.pi * traversals
        )


def test_multivariable_packets_deliver_original_open_reports():
    assert len(NEW) == 20 and MANIFEST["version"] == "0.6.0"
    assert (
        MANIFEST["maturity"] == "partial"
        and MANIFEST["review"]["status"] == "unreviewed"
    )
    repo = ContentRepository(ROOT / "content")
    scheduled = [x for w in MANIFEST["duration"]["weeks"] for x in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 23
    for n in range(15, 22):
        lesson = repo.lesson("calculus-3", f"calculus-3-{n}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions) == len(lesson.retrieval_cards) == (4 if n < 18 else 2)
        )
