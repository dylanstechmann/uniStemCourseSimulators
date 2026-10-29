"""Independent normalized-orbital, overlapping-state and closed-ledger references."""

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
DIRECTORY = ROOT / "content/courses/general-chemistry-1"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"general-chemistry-1-(1[5-9]|20):depth-\d+", q["id"])
}
R = sp.Rational


def orbital_reference(z, radius):
    r = sp.symbols("r", positive=True)
    p = 4 * z**3 * r**2 * sp.exp(-2 * z * r)
    return sp.integrate(r * p, (r, 0, sp.oo)), sp.integrate(p, (r, 0, radius))


def state_reference(alpha, beta, overlap):
    energy = sp.symbols("energy")
    h = sp.Matrix([[alpha, beta], [beta, alpha]])
    s = sp.Matrix([[1, overlap], [overlap, 1]])
    energies = sorted(sp.solve((h - energy * s).det(), energy))
    return (
        energies[0],
        energies[1],
        1 / sp.sqrt(2 + 2 * overlap),
        1 / sp.sqrt(2 - 2 * overlap),
    )


def gas_reference(a2, a, b, k, rt, enthalpy):
    xi = sp.symbols("xi")
    amounts = [a2 - xi, a + 2 * xi]
    residual = b * amounts[1] ** 2 - k * amounts[0]
    roots = sp.solve(residual, xi)
    root = next(v for v in roots if -a / 2 < v < a2)
    return (
        root,
        b * sum(n.subs(xi, root) for n in amounts),
        root * (enthalpy - rt),
        2 * a2 + a,
    )


@cache
def calculations():
    mean, p = orbital_reference(2, R(1, 2))
    plus, minus, cp, cm = state_reference(-1, -R(2, 5), R(1, 5))
    amean, ap = orbital_reference(3, R(1, 2))
    aplus, aminus, acp, _ = state_reference(-2, -R(1, 2), R(1, 10))
    g = gas_reference(1, R(1, 2), R(1, 2), R(2, 3), 2, 6)
    ag = gas_reference(2, 1, R(1, 4), 1, 1, 5)
    concentrations = sp.Matrix([[2, 1], [1, 3]]).inv() * sp.Matrix(
        [R(7, 10), R(11, 10)]
    )
    return {
        (15, 1): dict(photon=4 * (R(1, 4) - R(1, 9)), ionization=1),
        (15, 2): dict(mode=R(1, 2), mean=mean, inside_mode=p),
        (15, 3): dict(orbitals=5, radial_nodes=1, angular_nodes=2, shell_capacity=32),
        (15, 4): {},
        (16, 1): dict(plus=plus, minus=minus),
        (16, 2): dict(plus_coefficient=cp, minus_coefficient=cm),
        (16, 3): dict(
            lower_electrons=2, upper_electrons=1, order=R(1, 2), energy=2 * plus + minus
        ),
        (16, 4): {},
        (17, 1): dict(photon=9 * (R(1, 4) - R(1, 16)), ionization=R(9, 16)),
        (17, 2): dict(mode=R(1, 3), mean=amean, probability=ap),
        (18, 1): dict(plus=aplus, minus=aminus, coefficient=acp),
        (18, 2): dict(
            energy=2 * aplus + aminus, lowering=-6 - (2 * aplus + aminus), order=R(1, 2)
        ),
        (19, 1): dict(extent=g[0], molecules=R(3, 2) + g[0], pressure=g[1], atoms=g[3]),
        (19, 2): dict(internal=4, heat=g[2]),
        (20, 1): dict(
            offset=R(1, 50),
            x=concentrations[0],
            y=concentrations[1],
            total=sum(concentrations),
        ),
        (20, 2): dict(extent=ag[0], pressure=ag[1], heat=ag[2], atoms=ag[3]),
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_chemistry_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(
        int, re.fullmatch(r"general-chemistry-1-(\d+):depth-(\d+)", qid).groups()
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


def test_radial_normalization_shell_measure_mode_and_cumulative_limits():
    r, z, R0 = sp.symbols("r z R0", positive=True)
    p = 4 * z**3 * r**2 * sp.exp(-2 * z * r)
    cumulative = 1 - sp.exp(-2 * z * R0) * (1 + 2 * z * R0 + 2 * z * z * R0 * R0)
    assert sp.integrate(p, (r, 0, sp.oo)) == 1
    assert sp.simplify(sp.diff(cumulative, R0) - p.subs(r, R0)) == 0
    assert cumulative.subs(R0, 0) == 0 and sp.limit(cumulative, R0, sp.oo) == 1
    assert sp.simplify(sp.diff(p, r).subs(r, 1 / z)) == 0
    assert sp.diff(p, r, 2).subs({z: 2, r: R(1, 2)}) < 0
    assert [sum(2 * angular + 1 for angular in range(n)) for n in range(1, 5)] == [
        1,
        4,
        9,
        16,
    ]


def test_overlap_norm_projected_equations_and_consistent_phase_change():
    for alpha, beta, overlap in [(-1, -R(2, 5), R(1, 5)), (-2, -R(1, 2), R(1, 10))]:
        plus, minus, cp, cm = state_reference(alpha, beta, overlap)
        h = sp.Matrix([[alpha, beta], [beta, alpha]])
        s = sp.Matrix([[1, overlap], [overlap, 1]])
        vectors = [sp.Matrix([cp, cp]), sp.Matrix([cm, -cm])]
        for energy, v in zip([plus, minus], vectors):
            assert sp.simplify((v.T * s * v)[0]) == 1
            assert (h - energy * s) * v == sp.zeros(2, 1)
        assert sp.simplify((vectors[0].T * s * vectors[1])[0]) == 0
        phase = sp.diag(1, -1)
        e = sp.symbols("e")
        assert (
            sp.expand(
                (phase * h * phase - e * phase * s * phase).det() - (h - e * s).det()
            )
            == 0
        )


def test_gas_domain_atoms_quotient_and_rigid_energy_are_independent():
    for a2, a, b, k, rt, dh in [
        (1, R(1, 2), R(1, 2), R(2, 3), 2, 6),
        (2, 1, R(1, 4), 1, 1, 5),
    ]:
        root, pressure, heat, atoms = gas_reference(a2, a, b, k, rt, dh)
        final_a2 = a2 - root
        final_a = a + 2 * root
        assert final_a2 > 0 and final_a > 0
        assert sp.simplify(2 * final_a2 + final_a - atoms) == 0
        assert sp.simplify(b * final_a**2 / final_a2 - k) == 0
        assert sp.simplify(pressure - b * (final_a2 + final_a)) == 0
        assert sp.simplify(heat + root * rt - root * dh) == 0


def test_reference_offset_composition_and_corrected_reconstruction():
    matrix = sp.Matrix([[2, 1], [1, 3]])
    reference = sp.Matrix([R(1, 10), R(1, 5)])
    assert matrix * reference == sp.Matrix([R(2, 5), R(7, 10)])
    offset = sp.Matrix([R(1, 50)] * 2)
    reported = sp.Matrix([R(18, 25), R(28, 25)])
    corrected = matrix.inv() * (reported - offset)
    assert corrected == sp.Matrix([R(1, 5), R(3, 10)])
    assert matrix.inv() * reported != corrected


def test_chemistry_packets_have_open_delivery_and_preserve_paired_primers():
    assert len(NEW) == 16 and tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 6, 0)
    assert (
        MANIFEST["maturity"] == "partial"
        and MANIFEST["review"]["status"] == "unreviewed"
    )
    repository = ContentRepository(ROOT / "content")
    weeks = MANIFEST["duration"]["weeks"]
    ids = [x for w in weeks for x in w["lesson_ids"]]
    assert len(ids) == len(set(ids)) == 24 and len(weeks) == 14
    for n in range(15, 21):
        lesson = repository.lesson("general-chemistry-1", f"general-chemistry-1-{n}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions) == len(lesson.retrieval_cards) == (4 if n < 17 else 2)
        )
    for pair in [(1, 7), (2, 9), (3, 11), (4, 12)]:
        assert (
            len(
                {
                    w["week"]
                    for w in weeks
                    for n in pair
                    if f"general-chemistry-1-{n}" in w["lesson_ids"]
                }
            )
            == 1
        )
