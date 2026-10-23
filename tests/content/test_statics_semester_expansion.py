"""Independent displacement-field and constitutive-history checks for new mechanics."""

from __future__ import annotations

import json
import re
from fractions import Fraction
from pathlib import Path

import pytest
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/statics-materials"
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
    if re.fullmatch(r"statics-materials-1[6-9]:depth-\d+", qid)
}


def coefficients(length, load, rigidity, settlement):
    # Solve the integrated beam equation y''''=w/EI with fixed A and y(L)=Delta,y''(L)=0.
    length, load, rigidity, settlement = map(
        Fraction, [length, load, rigidity, settlement]
    )
    a, b = length, Fraction(1)
    c, d = length**3 / 6, length**2 / 2
    first = -load * length**2 / (2 * rigidity)
    second = settlement - load * length**4 / (24 * rigidity)
    determinant = a * d - b * c
    cubic = (first * d - b * second) / determinant
    quadratic = (a * second - first * c) / determinant
    ra = -rigidity * cubic
    rb = load * length - ra
    couple = rigidity * quadratic
    return length, load, rigidity, cubic, quadratic, ra, rb, couple


def released_displacement(length, load, rigidity):
    length, load, rigidity = map(Fraction, [length, load, rigidity])
    cubic = -load * length / rigidity  # y'''(L)=0
    quadratic = -load * length**2 / (2 * rigidity) - cubic * length  # y''(L)=0
    return (
        load * length**4 / (24 * rigidity)
        + cubic * length**3 / 6
        + quadratic * length**2 / 2
    )


def free_history(modulus, yield_stress, maximum, length):
    modulus, yield_stress, maximum, length = map(
        Fraction, [modulus, yield_stress, maximum, length]
    )
    stress = min(modulus * maximum, yield_stress)
    elastic_strain = stress / modulus
    plastic_strain = maximum - elastic_strain
    points = [(Fraction(0), Fraction(0)), (elastic_strain, stress), (maximum, stress)]
    work = sum(
        (x2 - x1) * (s1 + s2) / 2 for (x1, s1), (x2, s2) in zip(points, points[1:])
    )
    recoverable = stress * elastic_strain / 2
    return {
        "yield": yield_stress / modulus,
        "plastic": plastic_strain,
        "extension": length * plastic_strain,
        "work": work,
        "recoverable": recoverable,
        "dissipated": work - recoverable,
    }


def parallel(maximum):
    maximum = Fraction(maximum)
    moduli = [Fraction("100e9"), Fraction("200e9")]
    yields = [Fraction("100e6"), Fraction("300e6")]
    area = Fraction(".0001")
    stresses = [min(e * maximum, y) for e, y in zip(moduli, yields, strict=True)]
    plastic = [maximum - stress / e for e, stress in zip(moduli, stresses, strict=True)]
    final = sum(e * p for e, p in zip(moduli, plastic, strict=True)) / sum(moduli)
    residual = [e * (final - p) for e, p in zip(moduli, plastic, strict=True)]
    assert sum(area * s for s in residual) == 0
    assert all(
        abs(stress) < limit for stress, limit in zip(residual, yields, strict=True)
    )
    return stresses, area * sum(stresses), final, residual


def calculations():
    length, w, ei, cubic, quadratic, ra, rb, couple = coefficients("1.5", 600, 30000, 0)
    maximum_x = -ei * cubic / w
    maximum_m = -ei * (w * maximum_x**2 / (2 * ei) + cubic * maximum_x + quadratic)
    # The other root of M=0 follows from the quadratic product, given the free-end root L.
    inner_zero = (2 * ei * quadratic / w) / length
    settled = coefficients("1.5", 600, 30000, ".005")
    free = free_history("80e9", "160e6", ".005", ".20")
    stresses, force, final, residual = parallel(".0011")
    assignment = coefficients("1.20", 500, 18000, ".002")
    assignment_delta = released_displacement("1.20", 500, 18000)
    free2 = free_history("120e9", "240e6", ".006", ".15")
    _, force2, final2, residual2 = parallel(".0013")
    return {
        (16, 1): {"prop": rb, "fixed_force": ra, "couple": couple},
        (16, 2): {
            "released": released_displacement("1.5", 600, 30000),
            "prop": settled[6],
        },
        (16, 3): {
            "zero": inner_zero,
            "position": maximum_x,
            "positive": maximum_m,
            "fixed": -couple,
        },
        (16, 4): {},
        (17, 1): {
            "yield_strain": free["yield"],
            "plastic_strain": free["plastic"],
            "extension": free["extension"],
        },
        (17, 2): {
            "input": free["work"],
            "recoverable": free["recoverable"],
            "plastic_work": free["dissipated"],
        },
        (17, 3): {
            "stress1": stresses[0] / 10**6,
            "stress2": stresses[1] / 10**6,
            "force": force,
        },
        (17, 4): {
            "strain": final,
            "stress1": residual[0] / 10**6,
            "stress2": residual[1] / 10**6,
        },
        (18, 1): {
            "prop": assignment[6],
            "fixed_force": assignment[5],
            "couple": assignment[7],
        },
        (18, 2): {
            "released": assignment_delta,
            "gap": Fraction(".010") - assignment_delta,
        },
        (19, 1): {
            "plastic_strain": free2["plastic"],
            "extension": free2["extension"],
            "input": free2["work"],
            "recoverable": free2["recoverable"],
        },
        (19, 2): {
            "maximum_force": force2,
            "final_strain": final2,
            "stress1": residual2[0] / 10**6,
            "stress2": residual2[1] / 10**6,
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_new_mechanics_answers_recompute_from_independent_equations_and_grade(qid):
    number, item = map(
        int, re.fullmatch(r"statics-materials-(\d+):depth-(\d+)", qid).groups()
    )
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
        else:
            assert float(values[spec["id"]]) == pytest.approx(
                spec["answer"], rel=1e-12, abs=1e-15
            )
            response[spec["id"]] = format(float(values[spec["id"]]), ".2e")
    result = grade(question, AttemptRequest(response=response))
    assert result.correct, result.feedback
    for fid, value in values.items():
        assert not grade(
            question,
            AttemptRequest(
                response={**response, fid: format(float(value) * 1.2, ".2e")}
            ),
        ).correct


def test_new_foundations_and_paper_reports_are_scheduled_without_grades():
    assert len(NEW) == 12
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 21
    assert len(MANIFEST["duration"]["weeks"]) == 14
    content = ContentRepository(ROOT / "content")
    for number in range(16, 20):
        lesson = content.lesson("statics-materials", f"statics-materials-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 18 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )


def test_polynomial_beam_field_checks_boundary_values_and_global_equilibrium():
    length, w, ei, cubic, quadratic, ra, rb, couple = coefficients(
        "1.20", 500, 18000, ".002"
    )

    def displacement(x):
        return w * x**4 / (24 * ei) + cubic * x**3 / 6 + quadratic * x**2 / 2

    def moment(x):
        return -ei * (w * x * x / (2 * ei) + cubic * x + quadratic)

    assert displacement(length) == Fraction(".002")
    assert moment(length) == 0 and moment(0) == -couple
    assert ra + rb == w * length
    assert couple + rb * length - w * length * length / 2 == 0
    candidate = coefficients("1.20", 500, 18000, ".010")
    assert candidate[6] < 0  # contact-constrained solution is not an admissible prop
    gap = Fraction(".010") - released_displacement("1.20", 500, 18000)
    assert (
        gap > 0
    )  # released state with zero reaction satisfies the unilateral inequalities


def test_energy_flexibility_and_unloading_limiting_cases():
    length, w, ei = Fraction(2), Fraction(400), Fraction(20000)
    # Integrate polynomial unit-load products using a midpoint-independent exact antiderivative.
    flexibility = length**3 / (3 * ei)
    load_displacement = (w / (2 * ei)) * length**4 / 4
    assert load_displacement == released_displacement(length, w, ei)
    assert load_displacement / flexibility == 300
    stresses, force, final, residual = parallel(".0008")
    assert all(stresses) and force > 0 and final == 0 and residual == [0, 0]
    free = free_history("120e9", "240e6", ".006", ".15")
    assert free["work"] == free["recoverable"] + free["dissipated"]
    assert free["dissipated"] > 0
    text = (
        DIRECTORY / "modules/plasticity-unloading-and-redistribution.md"
    ).read_text()
    assert "zero external force" in text and "zero displacement" in text
