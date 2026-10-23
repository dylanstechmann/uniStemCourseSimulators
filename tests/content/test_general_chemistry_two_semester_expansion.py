"""Independent free-ligand/charge, occupation, rate-network and redox checks."""

from __future__ import annotations

import csv
import itertools
import json
import math
import re
from fractions import Fraction
from functools import cache
from pathlib import Path

import pytest
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/general-chemistry-2"
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
    if re.fullmatch(r"general-chemistry-2-(1[6-9]|2[01]):depth-\d+", qid)
}


def bisect(function, low, high):
    left = function(low)
    assert left * function(high) <= 0
    for _ in range(100):
        middle = (low + high) / 2
        value = function(middle)
        if left * value <= 0:
            high = middle
        else:
            low, left = middle, value
    return (low + high) / 2


def species(h, ka, kf, mt, lt):
    # Solve in free ligand, rather than the author's conditional-complex quadratic.
    def complex_from_free(free):
        return mt * kf * free / (1 + kf * free)

    free = bisect(
        lambda ligand: ligand + h * ligand / ka + complex_from_free(ligand) - lt, 0, lt
    )
    complexed = complex_from_free(free)
    protonated = h * free / ka
    metal = mt - complexed
    hydroxide = 1e-14 / h
    spectator = h + 2 * metal + complexed - free - hydroxide
    assert metal + complexed == pytest.approx(mt, abs=1e-16)
    assert free + protonated + complexed == pytest.approx(lt, abs=1e-16)
    return {
        "complex": complexed,
        "metal": metal,
        "ligand": free,
        "protonated": protonated,
        "hydroxide": hydroxide,
        "spectator": spectator,
        "bound": complexed / mt,
        "alpha": free / (free + protonated),
        "ph": -math.log10(h),
    }


def occupancy_energy(occupation, splitting, pairing):
    levels = [-0.4 * splitting] * 3 + [0.6 * splitting] * 2
    return sum(
        count * energy for count, energy in zip(occupation, levels, strict=True)
    ) + pairing * sum(count == 2 for count in occupation)


def unpaired(occupation):
    return sum(count == 1 for count in occupation)


def photon_molar(wavelength_nm):
    # Frequency, photon energy and count-per-mole conversion kept as separate unit steps.
    frequency = 299792458 / (wavelength_nm / 1e9)
    photon_joules = 6.62607015e-34 * frequency
    return photon_joules * 6.02214076e23 / 1000


def reduced_d(kd, returning, capture, y):
    # Steady intermediate amount per unit ML follows its inflow/outflow balance.
    intermediate = Fraction(kd) / (
        Fraction(returning) + Fraction(capture) * Fraction(y)
    )
    return Fraction(capture) * Fraction(y) * intermediate


def reduced_a(turnover, association, y):
    ratio = Fraction(association) * Fraction(y)
    # Normalize [ML]+[I]=1 after the fast-equilibrium ratio is supplied.
    intermediate = ratio / (1 + ratio)
    return Fraction(turnover) * intermediate


@cache
def calculations():
    state = species(2e-5, 1e-5, 3750, 0.0015, 0.0021)
    log_h = bisect(
        lambda log: species(10**log, 4e-6, 2500, 0.0012, 0.0018)["spectator"]
        - 0.00080099,
        -12,
        -2,
    )
    assignment = species(10**log_h, 4e-6, 2500, 0.0012, 0.0018)
    spectral600, spectral650 = photon_molar(600), photon_molar(650)
    high4, low4 = (1, 1, 1, 1, 0), (2, 1, 1, 0, 0)
    high5, low5 = (1, 1, 1, 1, 1), (2, 2, 1, 0, 0)
    high7, low7 = (2, 2, 1, 1, 1), (2, 2, 2, 1, 0)
    rate = reduced_d(".0004", ".06", 100, ".0006")
    other = reduced_a(".0004", Fraction(100) / Fraction(".06"), ".0006")
    doubled = reduced_d(".0004", ".12", 100, ".0006")
    # Reconstruct free oxidation-state concentrations before applying Nernst.
    oxidized_total, reduced_total, free_ligand = 0.002, 0.002, 0.001
    free_oxidized = oxidized_total / (1 + 10000 * free_ligand)
    free_reduced = reduced_total / (1 + 100 * free_ligand)
    factor = (free_oxidized / free_reduced) / (oxidized_total / reduced_total)
    shift = 8.31446262 * 298.15 / 96485.33212 * math.log(free_oxidized / free_reduced)
    return {
        (16, 1): {
            "alpha": state["alpha"],
            "conditional": 3750 * state["alpha"],
            "complex": state["complex"],
        },
        (16, 2): {
            key: state[key] for key in ["metal", "ligand", "protonated", "bound"]
        },
        (16, 3): {key: state[key] for key in ["hydroxide", "spectator", "ph"]},
        (16, 4): {},
        (17, 1): {
            "electrons": 8 - 3,
            "high_unpaired": unpaired(high5),
            "low_unpaired": unpaired(low5),
            "low_pairs": sum(c == 2 for c in low5),
        },
        (17, 2): {
            "splitting": spectral600,
            "difference": occupancy_energy(low4, spectral600, 210)
            - occupancy_energy(high4, spectral600, 210),
        },
        (17, 3): {
            "difference": occupancy_energy(low5, 150, 180)
            - occupancy_energy(high5, 150, 180),
            "unpaired": unpaired(high5),
            "moment": 2 * math.sqrt(Fraction(5, 2) * (Fraction(5, 2) + 1)),
        },
        (17, 4): {
            "high_unpaired": unpaired(high7),
            "low_unpaired": unpaired(low7),
            "difference": occupancy_energy(low7, 200, 150)
            - occupancy_energy(high7, 200, 150),
        },
        (18, 1): {
            "observed": rate,
            "plateau": Fraction(".0004"),
            "half": Fraction(".06") / 100,
        },
        (18, 2): {"rate": other},
        (18, 3): {
            "dissociation": doubled,
            "association": other,
            "ratio": doubled / rate,
        },
        (18, 4): {
            "ratio": Fraction(".0004") / Fraction(".12"),
            "relaxation": 1 / Fraction(".12"),
        },
        (19, 1): {
            key: assignment[key] for key in ["alpha", "complex", "metal", "ligand"]
        },
        (19, 2): {
            key: assignment[key] for key in ["ph", "hydroxide", "bound", "spectator"]
        },
        (20, 1): {
            "rate": reduced_d(".0006", ".04", 80, ".0005"),
            "half": Fraction(".04") / 80,
            "plateau": Fraction(".0006"),
        },
        (20, 2): {
            "dissociation": reduced_d(".0006", ".08", 80, ".0005"),
            "association": reduced_a(".0006", 2000, ".0005"),
        },
        (21, 1): {
            "splitting": spectral650,
            "difference": occupancy_energy(low4, spectral650, 190)
            - occupancy_energy(high4, spectral650, 190),
            "unpaired": unpaired(high4),
            "moment": 2 * math.sqrt(2 * 3),
        },
        (21, 2): {"factor": factor, "shift": shift, "potential": 0.2 + shift},
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_new_chemical_keys_recompute_and_actual_grader_rejects_each_perturbation(qid):
    number, item = map(
        int, re.fullmatch(r"general-chemistry-2-(\d+):depth-(\d+)", qid).groups()
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
            assert value == pytest.approx(spec["answer"], rel=1e-12, abs=1e-16)
            response[spec["id"]] = (
                format(value, ".3f")
                if spec["id"] == "ph"
                else format(value, ".2e")
                if spec["significant_figures"]
                else str(int(value))
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


def test_closed_state_original_equilibria_and_spectator_constraints():
    state = species(1e-6, 4e-6, 2500, 0.0012, 0.0018)
    assert state["complex"] / (state["metal"] * state["ligand"]) == pytest.approx(2500)
    assert 1e-6 * state["ligand"] / state["protonated"] == pytest.approx(4e-6)
    assert state["spectator"] == pytest.approx(0.00080099)
    # Arbitrarily changing a fixed spectator amount makes the same imposed h inconsistent.
    assert abs(state["spectator"] - 0.001) > 0.0001
    ph_question = NEW["general-chemistry-2-16:depth-3"]
    response = {"hydroxide": "5.00e-10", "spectator": "1.72e-3", "ph": "4.699"}
    assert grade(ph_question, AttemptRequest(response=response)).correct
    assert not grade(
        ph_question, AttemptRequest(response={**response, "ph": "4.70"})
    ).correct
    for kf in [1, 2500, 1e8]:
        variant = species(1e-6, 4e-6, kf, 0.0012, 0.0007)
        assert 0 <= variant["complex"] <= 0.0007
        assert variant["ligand"] >= 0 and variant["metal"] >= 0


def test_occupations_enumerate_admissible_states_and_spectral_units():
    for electrons, splitting, pairing, expected_unpaired in [
        (4, photon_molar(600), 210, 4),
        (4, photon_molar(650), 190, 4),
        (5, 150, 180, 5),
        (7, 200, 150, 1),
    ]:
        states = [
            s for s in itertools.product(range(3), repeat=5) if sum(s) == electrons
        ]
        minimum = min(occupancy_energy(s, splitting, pairing) for s in states)
        winners = [
            s
            for s in states
            if abs(occupancy_energy(s, splitting, pairing) - minimum) < 1e-10
        ]
        assert {unpaired(s) for s in winners} == {expected_unpaired}
    assert photon_molar(500) == pytest.approx(239.253131277394, abs=1e-10)
    assert photon_molar(600) > photon_molar(650)
    text = (
        DIRECTORY / "modules/ligand-field-spin-and-spectral-evidence.md"
    ).read_text()
    assert "239.253" in text


def test_reduced_curves_reference_rounding_and_full_network_limits():
    rows = list(
        csv.DictReader((DIRECTORY / "assignments/ligand-exchange-reference.csv").open())
    )
    for row in rows:
        y = Fraction(row["free_y_mol_L"])
        dissociation = reduced_d(".0004", ".06", 100, y)
        association = reduced_a(".0004", Fraction(100) / Fraction(".06"), y)
        assert dissociation == association
        assert float(dissociation) == pytest.approx(
            float(row["reduced_kobs_s_inverse"]), abs=5.1e-9
        )
    # Separately integrate a conserved full D network. It need not equal the reduced curve exactly.
    ml, intermediate, product = 1.0, 0.0, 0.0
    dt = 0.005

    def rhs(state):
        parent, free, _ = state
        return [
            -0.0004 * parent + 0.06 * free,
            0.0004 * parent - 0.12 * free,
            0.06 * free,
        ]

    for _ in range(20000):
        state = [ml, intermediate, product]
        a = rhs(state)
        b = rhs([s + dt * k / 2 for s, k in zip(state, a, strict=True)])
        c = rhs([s + dt * k / 2 for s, k in zip(state, b, strict=True)])
        d = rhs([s + dt * k for s, k in zip(state, c, strict=True)])
        ml, intermediate, product = [
            s + dt * (ka + 2 * kb + 2 * kc + kd) / 6
            for s, ka, kb, kc, kd in zip(state, a, b, c, d, strict=True)
        ]
    assert ml + intermediate + product == pytest.approx(1, abs=1e-12)
    observed = 0.06 * intermediate / (ml + intermediate)
    assert 0 < abs(observed / 0.0002 - 1) < 0.01
    assert intermediate / ml < 0.004


def test_connected_reports_and_analytic_resource_deliver_as_open_practice():
    assert len(NEW) == 18
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert (
        len(scheduled) == len(set(scheduled)) == 23
        and len(MANIFEST["duration"]["weeks"]) == 11
    )
    repository = ContentRepository(ROOT / "content")
    for number in range(16, 22):
        lesson = repository.lesson(
            "general-chemistry-2", f"general-chemistry-2-{number}"
        )
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 19 else 2)
        )
    lesson = repository.lesson("general-chemistry-2", "general-chemistry-2-20")
    assert (
        "/api/v1/courses/general-chemistry-2/resources/assignments/ligand-exchange-reference.csv"
        in lesson.markdown
    )
    assert (
        repository.learner_resource(
            "general-chemistry-2", "assignments/ligand-exchange-reference.csv"
        )
        == (DIRECTORY / "assignments/ligand-exchange-reference.csv").read_bytes()
    )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
