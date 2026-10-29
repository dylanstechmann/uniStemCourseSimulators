"""Independent signed-cycle,translation-selection and photosynthetic balance references."""

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
DIRECTORY = ROOT / "content/courses/biochemistry"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"biochemistry-(2[89]|3[0-2]):depth-\d+", q["id"])
}
R = sp.Rational


def translation(residues, overhead):
    charging = residues
    elongation = 2 * (residues - 1)
    gtp = elongation + overhead
    return charging, 2 * charging, residues - 1, elongation, gtp, 2 * charging + gtp


def filters(correct, first_correct, second_correct, first_wrong, second_wrong):
    accepted_correct = correct * first_correct * second_correct
    accepted_wrong = (1 - correct) * first_wrong * second_wrong
    return (
        accepted_correct,
        accepted_correct + accepted_wrong,
        accepted_wrong / (accepted_correct + accepted_wrong),
    )


def pump_bound(energy, ion_cost):
    return max(n for n in range(20) if n * ion_cost - energy < 0)


@cache
def calculations():
    tr = translation(40, 4)
    correct, total, error = filters(R(9, 10), R(4, 5), R(9, 10), R(1, 100), R(1, 10))
    _, _, one = filters(R(9, 10), R(4, 5), 1, R(1, 100), 1)
    a = translation(60, 6)
    _, atotal, aerror = filters(R(98, 100), R(9, 10), R(95, 100), R(1, 10), R(1, 100))
    return {
        (28, 1): dict(initial=6 * R(4 - 1, 1 + 4 + 1), doubled=6 * R(8 - 2, 1 + 8 + 2)),
        (28, 2): dict(
            ion=sp.log(R(1, 10)) - sp.log(10),
            cycle=sp.log(1000) + 2 * (sp.log(R(1, 10)) - sp.log(10)),
            stall=sp.exp(4 * sp.log(10)),
        ),
        (28, 3): dict(
            ions=pump_bound(12, 2 * sp.log(10)),
            cost=4 * sp.log(10),
            cycle=4 * sp.log(10) - 12,
        ),
        (28, 4): {},
        (29, 1): dict(atp=tr[0], equivalents=tr[1], bonds=tr[2]),
        (29, 2): dict(elongation=tr[3], gtp=tr[4], total=tr[5]),
        (29, 3): dict(correct=correct, acceptance=total, error=error),
        (29, 4): dict(without=one, improvement=one / error),
        (30, 1): dict(co2=3, atp=9, nadph=6),
        (30, 2): dict(oxygen=1, nadph=2, photons=8, protons=12),
        (30, 3): dict(
            required_protons=9 * R(14, 3),
            linear_protons=3 * 12,
            cyclic=(9 * R(14, 3) - 36) / 2,
            photons=24 + (9 * R(14, 3) - 36) / 2,
        ),
        (30, 4): dict(output=R(9, 6), co2=3 * R(9, 6), atp_left=18 - 9 * R(9, 6)),
        (31, 1): dict(
            ion=-2 * sp.log(4),
            cycle=sp.log(64) - 4 * sp.log(4),
            stall=sp.exp(4 * sp.log(4)),
            pump=pump_bound(10, 2 * sp.log(4)),
        ),
        (31, 2): dict(equivalents=a[5], bonds=a[2], acceptance=atotal, error=aerror),
        (32, 1): dict(output=R(8, 6), co2=3 * R(8, 6), atp_left=20 - 9 * R(8, 6)),
        (32, 2): dict(
            cyclic=(45 - 36) / 3,
            photons=24 + (45 - 36) / 3,
            leak_cyclic=(45 - 30) / 3,
            leak_photons=24 + (45 - 30) / 3,
        ),
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_biochemistry_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(
        int, re.fullmatch(r"biochemistry-(\d+):depth-(\d+)", qid).groups()
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


def test_alternating_carrier_reversal_saturation_and_signed_stall():
    out, inside, v, k = sp.symbols("out inside v k", positive=True)
    flux = v * (out - inside) / (k + out + inside)
    assert (
        flux.subs(out, inside) == 0
        and sp.simplify(flux.xreplace({out: inside, inside: out}) + flux) == 0
    )
    scale = sp.symbols("scale", positive=True)
    assert (
        sp.limit(flux.subs({out: 4 * scale, inside: scale}), scale, sp.oo) == 3 * v / 5
    )
    for ratio, count in [(10, 2), (4, 2)]:
        ion = sp.log(1 / sp.Integer(ratio)) - sp.log(ratio)
        stall = sp.exp(-count * ion)
        assert sp.simplify(sp.log(stall) + count * ion) == 0
        assert sp.simplify(sp.log(stall / 2) + count * ion) < 0
    for energy, cost in [(12, 2 * sp.log(10)), (10, 2 * sp.log(4))]:
        n = pump_bound(energy, cost)
        assert n * cost < energy < (n + 1) * cost


def test_translation_count_boundaries_and_conditional_selection_denominators():
    for residues, overhead in [(10, 4), (40, 4), (60, 6)]:
        charging, eq, bonds, elong, gtp, total = translation(residues, overhead)
        assert charging == residues and bonds + 1 == residues
        assert total == 2 * residues + 2 * (residues - 1) + overhead
        assert eq + gtp == total and elong == 2 * bonds
    correct, total, error = filters(R(9, 10), R(4, 5), R(9, 10), R(1, 100), R(1, 10))
    assert correct == R(81, 125) and total == R(6481, 10000) and error == R(1, 6481)
    assert error != R(1, 10000)
    assert filters(R(98, 100), R(9, 10), R(95, 100), R(1, 10), R(1, 100))[2] == R(
        1, 41896
    )


def test_calvin_carbon_acceptor_and_electron_conservation():
    # Three carboxylations:three five-carbon acceptors plus three CO2 form six three-carbon products.
    assert 3 * 5 + 3 == 6 * 3
    # Five trioses regenerate the three acceptors,leaving one triose net output.
    assert 5 * 3 == 3 * 5 and 6 * 3 - 3 * 5 == 3
    assert 6 + 3 == 9
    # Four electrons from two waters supply two two-electron reducing equivalents and one O2.
    atom_charge = sp.Matrix([[2, 0, 1, 0], [1, 2, 0, 0], [0, 0, 1, -1]])
    assert atom_charge * sp.Matrix([-2, 1, 4, 4]) == sp.zeros(3, 1)
    assert 12 / 2 == 6 and 12 / 4 == 3


def test_photosynthetic_coupling_resource_and_loss_boundaries():
    for h, cyclic_protons, linear in [(R(14, 3), 2, 36), (5, 3, 36), (5, 3, 30)]:
        required = 9 * h
        cyclic = (required - linear) / cyclic_protons
        assert cyclic >= 0 and linear + cyclic * cyclic_protons == required
    for atp, nadph in [(18, 9), (20, 8)]:
        output = min(R(atp, 9), R(nadph, 6))
        assert 9 * output <= atp and 6 * output <= nadph
        assert 9 * output == atp or 6 * output == nadph
    assert 36 / 4 == 9 and R(36) / (R(14, 3)) < 9


def test_biochemistry_bridge_delivery_and_existing_homework_are_preserved():
    assert len(NEW) == 16 and MANIFEST["version"] == "0.7.0"
    assert (
        MANIFEST["maturity"] == "partial"
        and MANIFEST["review"]["status"] == "unreviewed"
    )
    repository = ContentRepository(ROOT / "content")
    ids = [x for w in MANIFEST["duration"]["weeks"] for x in w["lesson_ids"]]
    assert len(ids) == len(set(ids)) == 45
    for n in range(28, 33):
        lesson = repository.lesson("biochemistry", f"biochemistry-{n}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions) == len(lesson.retrieval_cards) == (4 if n < 31 else 2)
        )
    assert len(list((DIRECTORY / "assignments").glob("homework-*.md"))) == 8
    assert len(MANIFEST["outcomes"]) == 6
