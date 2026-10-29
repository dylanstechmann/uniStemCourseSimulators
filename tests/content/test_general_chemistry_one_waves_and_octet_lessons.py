"""General Chemistry I 0.7.0 lessons 21 (photons, matter waves, box) and 22 (octet exceptions): stated numbers, schedule, comparators.

Box energies come from a finite-difference solution of the Schrodinger equation, box probabilities from quadrature, shapes and
polarity from placing bond vectors in ideal geometries, and electron counts from a bookkeeping routine, not from the readings.
Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-1"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
R21 = (COURSE / "modules/21-photons-matter-waves-and-quantization-in-a-box.md").read_text(encoding="utf-8")
R22 = (COURSE / "modules/22-beyond-the-octet-lewis-structures-and-shape.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
H, C, E_CHARGE, ME = 6.62607015e-34, 299792458.0, 1.602176634e-19, 9.109e-31  # exact SI values and the stated measured electron mass
HBAR = H / (2 * math.pi)
HC_EV_NM = H * C / E_CHARGE * 1e9
VALENCE = {"B": 3, "N": 5, "O": 6, "F": 7, "P": 5, "S": 6, "Cl": 7, "Br": 7, "I": 7, "Xe": 8}


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


def simpson(function, lower, upper, pieces=20000):
    step = (upper - lower) / pieces
    return step / 3 * math.fsum((1 if i in (0, pieces) else 4 if i % 2 else 2) * function(lower + i * step) for i in range(pieces + 1))


def box_levels(length, count, grid=1200):
    """Lowest eigenvalues (J) of -(hbar^2/2m) psi'' = E psi with psi = 0 at both walls, by Sturm bisection on the tridiagonal matrix."""
    step = length / grid
    diagonal, off = HBAR**2 / (ME * step**2), -(HBAR**2) / (2 * ME * step**2)

    def below(energy):
        negatives, d = 0, diagonal - energy
        negatives += d < 0
        for _ in range(1, grid - 1):
            d = (diagonal - energy) - off * off / (d if d != 0 else 1e-300)
            negatives += d < 0
        return negatives

    levels = []
    for target in range(1, count + 1):
        low, high = 0.0, 2 * (target + 1) ** 2 * H**2 / (8 * ME * length**2)
        for _ in range(80):
            middle = (low + high) / 2
            low, high = (low, middle) if below(middle) >= target else (middle, high)
        levels.append((low + high) / 2)
    return levels


def test_box_energies_match_a_finite_difference_solution_of_the_schrodinger_equation():
    numeric = [energy / E_CHARGE for energy in box_levels(1.0e-9, 3)]
    closed = [n * n * H**2 / (8 * ME * 1.0e-18) / E_CHARGE for n in (1, 2, 3)]
    assert numeric == pytest.approx(closed, rel=3e-5) and [round(x, 4) for x in closed] == [0.3760, 1.5042, 3.3844]
    gap = closed[1] - closed[0]
    assert gap == pytest.approx(3 * closed[0]) and round(gap, 3) == 1.128 and round(HC_EV_NM / gap) == 1099
    assert (closed[2] - closed[1]) / gap == pytest.approx(5 / 3) and round(4 * gap, 3) == 4.513 and round(HC_EV_NM / (4 * gap), 1) == 274.8
    # halving the box quadruples every level (checked on the numerical solution too)
    half = [energy / E_CHARGE for energy in box_levels(0.5e-9, 1)]
    assert half[0] == pytest.approx(4 * numeric[0], rel=3e-5)
    stated(R21, "E₁ = 0.3760 eV, E₂ = 1.504 eV and E₃ = 3.384 eV", "ΔE = 3E₁ = 1.128 eV", "1239.84/1.128 = 1099 nm", "ΔE = 4.513 eV", "274.8 nm")


def test_box_probabilities_by_quadrature():
    def probability(n, upper):
        return simpson(lambda x: 2 * math.sin(n * math.pi * x) ** 2, 0, upper)

    assert round(probability(1, 0.25), 4) == 0.0908 and round(probability(2, 1 / 3), 4) == 0.4022 and round(probability(1, 1.0), 6) == 1.0
    assert probability(1, 0.25) < 0.25 and probability(2, 0.5) == pytest.approx(0.5)  # n = 2 has a node at the centre, splitting the probability evenly
    stated(R21, "P = 1/4 − 1/(2π) = 0.0908", "P(0 → L/3) = 1/3 − sin(4π/3)/(4π) = 0.4022", "0.0908")


def test_photoelectric_worked_example_and_threshold():
    photon = HC_EV_NM / 400
    kinetic = photon - 2.30
    threshold = HC_EV_NM / 2.30
    speed = math.sqrt(2 * kinetic * E_CHARGE / ME)
    wavelength = H / (ME * speed)
    assert round(photon, 3) == 3.100 and round(kinetic, 3) == 0.800 and round(threshold) == 539
    assert round(speed / 1e5, 2) == 5.30 and round(wavelength * 1e9, 2) == 1.37
    assert C / (threshold * 1e-9) == pytest.approx(5.5614e14, rel=1e-4) and HC_EV_NM == pytest.approx(1239.84, abs=0.005)
    stated(R21, "hc = 1239.84 eV·nm", "E = 1239.84/400 = 3.100 eV", "KE_max = 3.100 − 2.30 = 0.800 eV", "V_s = 0.800 V", "λ₀ = 1239.84/2.30 = 539 nm",
           "= 1.28 × 10⁻¹⁹ J", "v = √(2KE/m) = 5.30 × 10⁵ m/s", "λ = h/(mv) = 1.37 nm")
    worked = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == "general-chemistry-1-21")["worked_example"]
    for phrase in ("3.100 eV", "0.800 eV", "539 nm", "5.30 × 10⁵ m/s", "1.37 nm"):
        assert phrase in worked, phrase


def test_matter_wave_and_uncertainty_numbers():
    assert round(H / (ME * 1.00e6) * 1e9, 3) == 0.727 and f"{H / (0.145 * 40):.2e}" == "1.14e-34"
    assert round(H / math.sqrt(2 * ME * E_CHARGE * 100) * 1e9, 3) == 0.123
    momentum = HBAR / (2 * 0.10e-9)
    assert f"{momentum:.2e}" == "5.27e-25" and round(momentum / ME / 1e5, 1) == 5.8 and f"{HBAR / (2 * 1e-9 * 1e-6):.1e}" == "5.3e-20"
    # a box of width L confines the wave to a momentum spread of about hbar/L, so E_1 = h^2/(8 m L^2) exceeds zero
    assert H**2 / (8 * ME * 1e-18) > 0 and HBAR / 1e-9 > 0
    stated(R21, "= 7.27 × 10⁻¹⁰ m = 0.727 nm", "λ = 1.14 × 10⁻³⁴ m", "At 100 V this is 0.123 nm", "5.27 × 10⁻²⁵ kg·m/s", "Δv ≥ 5.8 × 10⁵ m/s", "Δv ≥ 5.3 × 10⁻²⁰ m/s")


GEOMETRY = {
    5: [(0, 0, 1), (0, 0, -1), (1, 0, 0), (math.cos(2 * math.pi / 3), math.sin(2 * math.pi / 3), 0), (math.cos(4 * math.pi / 3), math.sin(4 * math.pi / 3), 0)],
    6: [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)],
}
LONE_PAIR_SLOTS = {5: [2, 3, 4], 6: [4, 5]}  # equatorial positions first in a trigonal bipyramid, opposite positions in an octahedron


def placement(steric, lone_pairs):
    slots = set(LONE_PAIR_SLOTS[steric][:lone_pairs])
    return [vector for index, vector in enumerate(GEOMETRY[steric]) if index not in slots]


def dipole_sum(vectors):
    return math.dist(tuple(map(math.fsum, zip(*vectors))), (0, 0, 0))


def lewis(center, terminals, charge=0):
    total = VALENCE[center] + sum(VALENCE[atom] for atom in terminals) - charge
    leftover = total - 8 * len(terminals)
    return total, len(terminals), leftover // 2, 2 * len(terminals) + leftover, len(terminals) + leftover // 2


SPECIES = {
    "SF₆": ("S", ["F"] * 6, 0, "octahedral, nonpolar"), "PCl₅": ("P", ["Cl"] * 5, 0, "trigonal bipyramidal, nonpolar"), "SF₄": ("S", ["F"] * 4, 0, "see-saw, polar"),
    "ClF₃": ("Cl", ["F"] * 3, 0, "T-shaped, polar"), "XeF₂": ("Xe", ["F"] * 2, 0, "linear, nonpolar"), "BrF₅": ("Br", ["F"] * 5, 0, "square pyramidal, polar"),
    "XeF₄": ("Xe", ["F"] * 4, 0, "square planar, nonpolar"), "ICl₄⁻": ("I", ["Cl"] * 4, -1, "square planar, symmetric ion"),
}


@pytest.mark.parametrize("name", SPECIES)
def test_expanded_octet_table_rows_match_counting_and_bond_vector_sums(name):
    center, terminals, charge, description = SPECIES[name]
    total, bonds, lone, around, steric = lewis(center, terminals, charge)
    vectors = placement(steric, lone)
    assert len(vectors) == bonds
    polar = dipole_sum(vectors) > 1e-9
    assert polar == description.endswith(", polar")
    assert (around > 8) == (center in {"S", "P", "Xe", "Br", "I", "Cl"})
    row = f"| {name} | {total} | {bonds} | {lone} | {around} | {steric} | {description} |"
    assert row in R22, row


def test_ideal_angles_and_formal_charges():
    def angle(u, v):
        return math.degrees(math.acos(sum(a * b for a, b in zip(u, v)) / (math.dist(u, (0, 0, 0)) * math.dist(v, (0, 0, 0)))))

    tbp = GEOMETRY[5]
    assert (round(angle(tbp[0], tbp[1])), round(angle(tbp[0], tbp[2])), round(angle(tbp[2], tbp[3]))) == (180, 90, 120)
    octahedron = GEOMETRY[6]
    assert (round(angle(octahedron[0], octahedron[2])), round(angle(octahedron[0], octahedron[1]))) == (90, 180)

    def formal(valence, nonbonding, bonding):
        return valence - nonbonding - bonding // 2

    sulfate_single = [formal(6, 0, 8)] + [formal(6, 6, 2)] * 4
    sulfate_double = [formal(6, 0, 12)] + [formal(6, 4, 4)] * 2 + [formal(6, 6, 2)] * 2
    assert (sulfate_single[0], sum(sulfate_single), sulfate_double[0], sum(sulfate_double)) == (2, -2, 0, -2)
    bf3_single = [formal(3, 0, 6)] + [formal(7, 6, 2)] * 3
    bf3_double = [formal(3, 0, 8), formal(7, 4, 4)] + [formal(7, 6, 2)] * 2
    assert (bf3_single, sum(bf3_double), bf3_double[:2]) == ([0, 0, 0, 0], 0, [-1, 1])
    no2 = [formal(5, 1, 6), formal(6, 4, 4), formal(6, 6, 2)]  # unpaired electron counted as nonbonding on nitrogen
    assert no2 == [1, 0, -1] and sum(no2) == 0 and (5 + 2 * 6) % 2 == 1
    stated(R22, "BF₃ the count is 3 + 3 × 7 = 24", "formal charge is 3 − 0 − 6/2 = 0", "5 + 2 × 6 = 17 valence electrons", "6 + 4 × 6 + 2 = 32 valence electrons",
           "formal charge 6 − 0 − 8/2 = +2", "formal charge 0", "+1 on nitrogen and −1 on the singly bonded oxygen")
    stated(R22, "Xenon: 8 − 4 − 8/2 = 0", "Each fluorine: 7 − 6 − 2/2 = 0", "so there are 36 electrons", "remaining 36 − 32 = 4 electrons", "giving 28 electrons")


def test_lessons_are_scheduled_after_their_prerequisites_and_link_them():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[2]["lesson_ids"] == ["general-chemistry-1-21", "general-chemistry-1-15"]
    assert weeks[2]["assessment_ids"] == ["general-chemistry-1-21-practice", "general-chemistry-1-15-practice"]
    assert weeks[4]["lesson_ids"] == ["general-chemistry-1-8", "general-chemistry-1-22", "general-chemistry-1-14", "general-chemistry-1-16"]
    assert weeks[4]["assessment_ids"][1] == "general-chemistry-1-22-practice"
    for text, targets in ((R21, ("07-atoms-amount-and-photon-accounting.md", "hydrogenic-orbitals-and-radial-probability.md")),
                          (R22, ("08-bonding-geometry-and-molecular-properties.md",))):
        for target in targets:
            assert f"]({target})" in text and (COURSE / "modules" / target).exists()
        assert "link-only scope comparators" in text and "partial, unreviewed and formative-only" in text
        assert "synthetic" in text.lower() or "textbook examples" in text
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == ("partial", "unreviewed", "formative-only")
    objectives = {o["id"]: o for o in MANIFEST["lesson_objectives"]}
    outcomes = {o["id"] for o in MANIFEST["outcomes"]}
    for lesson_id, text in (("general-chemistry-1-21", R21), ("general-chemistry-1-22", R22)):
        lesson = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == lesson_id)
        covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
        assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == 13 and len(lesson["card_ids"]) == 4
        for objective_id in lesson["objectives"]:
            assert objectives[objective_id]["description"] in text
            assert set(objectives[objective_id]["course_outcome_ids"]) <= outcomes


def test_crosswalk_records_both_comparators_and_its_limits():
    stated(CROSSWALK, "https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/lecture-videos/", "https://ocw.uci.edu/courses/chem_1a_general_chemistry.html",
           "https://ocw.uci.edu/courses/chem_1b_general_chemistry.html", "https://ocw.uci.edu/courses/chem_1c_general_chemistry.html", "compiled with AI assistance", "not a review by the owner",
           "Covered in 0.7.0; previously absent", "| Black-body radiation | — | 1A Lectures 3 and 5 (topic index) | — | Absent; named only by UC Irvine |",
           "| Nuclear chemistry | Lecture 31 | — | — | Absent; named only by MIT |", "Elsewhere and shallow", "Covered in 0.7.0; previously only octet-obeying structures", "Absent by design")
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    local = {part.split(")")[0] for part in CROSSWALK.split("](")[1:] if not part.startswith("https://")}
    local = {link for link in local if not link.startswith("https://")}
    assert all((COURSE / link).resolve().exists() for link in local)
    assert {link for link in local if link.startswith(("modules/", "assignments/"))} <= readings
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for sid in ("gchem1-uci-chem1a", "gchem1-uci-chem1b", "gchem1-uci-chem1c", "chem1-semester-atom", "chem1-semester-bonding"):
        assert registry[sid]["reuse_mode"] == "link-only-comparator" and not registry[sid]["permissions"]["quotation"], sid
        assert "general-chemistry-1" in registry[sid]["mapped_courses"], sid
    assert {"general-chemistry-1-module-21", "general-chemistry-1-module-22"} <= set(registry["gchem1-uci-chem1a"]["mapped_modules"])
    assert "general-chemistry-1-module-21" in registry["chem1-semester-atom"]["mapped_modules"] and "general-chemistry-1-module-22" in registry["chem1-semester-bonding"]["mapped_modules"]


ABSENT_TERMS = ("Rydberg", r"black.?body", "van der Waals", "effusion", "vapor pressure", "phase diagram", r"nuclear chemistry", "nomenclature", "second law", "third law", "microstate")


def test_topics_the_crosswalk_labels_absent_appear_in_no_local_reading():
    for module in MANIFEST["modules"]:
        for lesson in module["lessons"]:
            text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
            if lesson["id"] == "general-chemistry-1-21":  # its limits sentence names black-body radiation as not developed
                text = text.replace("Black-body radiation and the history of the Bohr model are not developed", "")
            for term in ABSENT_TERMS:
                assert not re.search(term, text, re.IGNORECASE), (lesson["id"], term)
    assert "Black-body radiation and the history of the Bohr model are not developed" in R21
    assert "Schrödinger equation is named and its box solutions are used, but it is not derived or solved in general" in R21
    assert "d-orbital hybrids" in R22


MISCONCEPTIONS = {
    "21": {
        "photoelectron-energy": 2.755,  # the whole photon energy, forgetting the work function
        "threshold-wavelength": 3967.5,  # multiplying instead of dividing
        "stopping-potential": 3.309,  # forgetting the work function
        "de-broglie-electron": 3.637,  # answering in angstrom
        "electron-wavelength-voltage": 0.1416,  # forgetting the 2 in the square root
        "de-broglie-macroscopic": 0.002454,  # mass entered in grams
        "uncertainty-speed": 2.316,  # forgetting the factor of 1/2
        "box-ground-energy": 4.701,  # forgetting the 8
        "box-absorption-wavelength": 807.7,  # E_n taken proportional to n
        "box-probability": 0.25,  # the uniform value
    },
    "22": {
        "valence-electrons-pcl5": 35,  # forgetting phosphorus
        "valence-electrons-icl4": 35,  # forgetting the charge
        "lone-pairs-xef2": 6,  # electrons instead of pairs
        "lone-pairs-icl4": 4,  # electrons instead of pairs
        "electrons-around-sulfur": 8,  # forcing an octet
        "formal-charge-sulfate": -2,  # the ion's charge
        "steric-number-clf3": 3,  # bonds only
        "unpaired-electrons-no2": 0,  # forcing pairs
        "total-lone-pairs-xef4": 12,  # forgetting xenon
        "angle-axial-equatorial": 120,  # the equatorial-equatorial angle
    },
}
CASES = [(lesson, slug, wrong) for lesson, group in MISCONCEPTIONS.items() for slug, wrong in group.items()]


@pytest.mark.parametrize("lesson,slug,wrong", CASES, ids=[f"{lesson}-{slug}" for lesson, slug, _ in CASES])
def test_numeric_keys_reject_the_named_misconception(lesson, slug, wrong):
    item = BANK[f"general-chemistry-1-{lesson}:{slug}"]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct


@pytest.mark.parametrize("item_id", ["21:intensity-effect", "21:box-level-pattern", "22:clf3-shape", "22:bf3-lewis-acid"])
def test_single_choice_items_accept_only_the_key(item_id):
    item = BANK[f"general-chemistry-1-{item_id}"]
    key = item["solution_spec"]["answer"]
    accepted = [index for index in range(len(item["options"])) if grade(item, AttemptRequest(response=str(index))).correct]
    assert accepted == [key]


@pytest.mark.parametrize("item_id", ["21:wave-claims", "22:octet-claims"])
def test_multiple_select_items_give_partial_credit_for_correct_minus_incorrect(item_id):
    item = BANK[f"general-chemistry-1-{item_id}"]
    assert item["solution_spec"]["answer"] == [0, 2, 4] and item["points"] == 2
    scores = {tuple(r): grade(item, AttemptRequest(response=r)).score for r in ([0, 2, 4], [0, 2, 4, 1], [0, 2], [1, 3], [0, 1, 2, 3, 4])}
    assert scores[(0, 2, 4)] == pytest.approx(2.0) and scores[(0, 2, 4, 1)] == pytest.approx(4 / 3) and scores[(0, 2)] == pytest.approx(4 / 3)
    assert scores[(1, 3)] == 0 and scores[(0, 1, 2, 3, 4)] == pytest.approx(2 / 3)
