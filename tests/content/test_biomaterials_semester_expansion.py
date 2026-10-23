"""Independent interface kinetics, assay-population and coupled-constraint references."""

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
DIRECTORY = ROOT / "content/courses/biomaterials"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"biomaterials-(1[6-9]|20):depth-\d+", q["id"])
}
R = sp.Rational


def layer_reference(a, b, da, db):
    matrix = sp.Matrix([[-a - da, -a], [-b, -b - db]])
    source = sp.Matrix([a, b])
    eq = -matrix.inv() * source
    return 1 - sum(eq), eq[0], eq[1], matrix, source


@cache
def calculations():
    free, a, b, matrix, source = layer_reference(1, 2, 1, 2)
    slopes = source + matrix * sp.Matrix([R(4, 5), 0])
    roots = sorted(matrix.eigenvals())
    af, aa, ab, _, _ = layer_reference(2, 1, 1, 3)
    return {
        (16, 1): dict(one=R(2, 5), two=R(3, 5), ceiling=R(4, 5)),
        (16, 2): dict(cosine=R(1, 10), angle=sp.acos(R(1, 10)) * 180 / sp.pi),
        (16, 3): dict(free=free, a=a, b=b, access=R(3, 5) * free),
        (16, 4): dict(
            a_slope=slopes[0], b_slope=slopes[1], slow=roots[1], fast=roots[0]
        ),
        (17, 1): dict(
            attachment=R(600, 1000), fold=R(1200, 600), net_rate=sp.log(2) / 2
        ),
        (17, 2): dict(
            signal_fold=R(190 - 10, 70 - 10),
            initial_alpha=R(60, 600),
            final_alpha=R(180, 1200),
            alpha_ratio=R(180, 1200) / R(60, 600),
        ),
        (17, 3): dict(loss=R(1, 2) - sp.log(2) / 2, recovery_factor=R(5, 4)),
        (17, 4): {},
        (18, 1): dict(
            graft=R(9, 10) * R(3, 4),
            cosine=R(7, 40),
            angle=sp.acos(R(7, 40)) * 180 / sp.pi,
        ),
        (18, 2): dict(free=af, a=aa, b=ab, access=R(27, 40) * af),
        (19, 1): dict(
            attachment=R(1, 2),
            net_rate=sp.log(2) / 3,
            signal_fold=3,
            alpha_ratio=R(3, 2),
        ),
        (19, 2): dict(a_per_cell=R(80, 2000), b_per_cell=R(72, 1200), factor=R(4, 3)),
        (20, 1): dict(
            stiffness=R(1, 4) ** 2,
            permeability=R(3, 4) ** 3 / R(1, 4) ** 2,
            upper_porosity=R(4, 5),
        ),
        (20, 2): dict(
            initial_free=R(1, 4),
            initial_access=R(7, 10) / 4,
            changed_access=R(7, 10) / 6,
        ),
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_biomaterials_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(
        int, re.fullmatch(r"biomaterials-(\d+):depth-(\d+)", qid).groups()
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


def test_surface_reaction_solution_and_wetting_cosine_measure():
    t = sp.symbols("t", nonnegative=True)
    g = R(4, 5) * (1 - sp.exp(-sp.log(2) * t))
    assert sp.simplify(sp.diff(g, t) - sp.log(2) * (R(4, 5) - g)) == 0
    assert g.subs(t, 0) == 0 and sp.limit(g, t, sp.oo) == R(4, 5)
    graft = R(27, 40)
    cosine = graft * sp.cos(sp.pi / 3) + (1 - graft) * sp.cos(2 * sp.pi / 3)
    assert cosine == R(7, 40)
    assert sp.cos(graft * sp.pi / 3 + (1 - graft) * 2 * sp.pi / 3) != cosine


def test_competing_site_equilibrium_boundary_invariance_and_transient():
    for a, b, da, db in [(1, 2, 1, 2), (2, 1, 1, 3), (1, 2, 1, 1), (1, 4, 1, 1)]:
        free, aa, bb, matrix, source = layer_reference(a, b, da, db)
        assert free > 0 and aa > 0 and bb > 0 and free + aa + bb == 1
        assert source + matrix * sp.Matrix([aa, bb]) == sp.zeros(2, 1)
        # The vector field points into the triangle on each of its three faces.
        for theta in [R(0), R(1, 4), R(1)]:
            assert a * (1 - theta) >= 0 and b * (1 - theta) >= 0
            assert -da * theta - db * (1 - theta) <= 0
        assert all(float(e.evalf()) < 0 for e in matrix.eigenvals())
    matrix = layer_reference(1, 2, 1, 2)[3]
    assert matrix.trace() == -6 and matrix.det() == 6


def test_assay_signal_model_and_net_growth_nonidentifiability():
    r = sp.log(2) / 3
    for division in [R(2, 5), R(3, 5)]:
        loss = division - r
        assert loss > 0 and sp.simplify(1000 * sp.exp((division - loss) * 3)) == 2000
    assert R(320 - 20, 120 - 20) == 3
    assert R(300, 2000) / R(100, 1000) == R(3, 2)
    assert R(90) * R(4, 3) == 120
    assert R(72, 1200) > R(80, 2000) and 72 < 80


def test_coupled_architecture_window_and_interface_threshold_failure():
    phi = sp.symbols("phi", positive=True)
    k = phi**3 / (1 - phi) ** 2
    assert sp.simplify(sp.diff(sp.log(k), phi) - (3 / phi + 2 / (1 - phi))) == 0
    assert R(1, 4) ** 2 > R(1, 25) and k.subs(phi, R(3, 4)) > 4
    assert (1 - R(17, 20)) ** 2 < R(1, 25)
    assert R(7, 40) > R(15, 100) > R(7, 60)
    assert layer_reference(1, 2, 1, 1)[0] == R(1, 4)
    assert layer_reference(1, 4, 1, 1)[0] == R(1, 6)


def test_biomaterials_open_delivery_preserves_partial_boundary():
    assert len(NEW) == 14 and MANIFEST["version"] == "0.5.0"
    assert (
        MANIFEST["maturity"] == "partial"
        and MANIFEST["review"]["status"] == "unreviewed"
    )
    repository = ContentRepository(ROOT / "content")
    ids = [x for w in MANIFEST["duration"]["weeks"] for x in w["lesson_ids"]]
    assert len(ids) == len(set(ids)) == 22
    for n in range(16, 21):
        lesson = repository.lesson("biomaterials", f"biomaterials-{n}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions) == len(lesson.retrieval_cards) == (4 if n < 18 else 2)
        )
