"""Organic Chemistry I 0.7.0 reaction-energetics lesson: stated numbers, schedule and comparator boundary.

Each number the reading states is recomputed here from Boltzmann weights, transition-state-theory rate
constants and bond ledgers, not read from the lesson. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/organic-chemistry"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
READING = (COURSE / "modules/21-reaction-energetics-equilibria-barriers-and-energy-diagrams.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
RT = 8.314 * 298 / 1000  # kJ/mol
PREFACTOR = 1.380649e-23 * 298 / 6.62607015e-34  # k_B T / h, s^-1


def boltzmann(*energies):
    """Normalized populations of states at the given free energies (kJ/mol)."""
    weights = [math.exp(-energy / RT) for energy in energies]
    return [w / math.fsum(weights) for w in weights]


def half_life(barrier):
    return math.log(2) / (PREFACTOR * math.exp(-barrier / RT))


def stated(*phrases):
    missing = [phrase for phrase in phrases if phrase not in READING]
    assert not missing, missing


def signed(value, digits=1):
    """Format with the typographic minus the readings use."""
    return f"{value:.{digits}f}".replace("-", "−")


def test_equilibrium_statements_match_boltzmann_populations_and_bond_ledgers():
    equatorial, axial = boltzmann(0, 7.0)
    association = {temp: -40 + temp * 0.120 for temp in (298, 350)}
    stated(
        f"RT = {RT:.2f} kJ/mol", f"RT ln 10 = {RT * math.log(10):.1f} kJ/mol",
        f"= {axial / equatorial:.3f}, and about {100 * axial:.1f}% of molecules are axial",
        f"−RT ln 10⁴ = −{RT * math.log(1e4):.1f} kJ/mol",
        f"ΔG° = −40 + {298 * 0.120:.1f} = {signed(association[298])} kJ/mol and K = {math.exp(-association[298] / RT):.1f}",
        f"ΔG° = +{association[350]:.1f} kJ/mol and K = {math.exp(-association[350] * 1000 / (8.314 * 350)):.2f}",
        f"the sign changes at {40 / 0.120:.0f} K",
    )
    broken, formed = 415 + 190, 285 + 365
    stated(f"cost {broken} kJ/mol", f"return {formed} kJ/mol", f"ΔH° ≈ −{formed - broken} kJ/mol")


def test_rate_statements_match_transition_state_theory():
    stated(f"k_B T/h = {PREFACTOR / 1e12:.2f} × 10¹² s⁻¹")
    assert math.exp(5.7 / RT) == pytest.approx(10, rel=0.01)
    assert round(math.exp(4 / RT)) == 5  # the SN2-over-SN1 factor the reading calls "about five times"
    stated(
        f"about {math.exp(10 / RT):.0f} times faster",
        f"about {half_life(80):.0f} s", f"about {half_life(90) / 60:.0f} minutes", f"about {half_life(100) / 3600:.1f} hours",
        "about five times",
        f"drops by {0.70 * 30:.0f} kJ/mol and ionization becomes about {round(math.exp(21 / RT), -2):.0f} times faster",
        f"≈ {math.exp(10 / RT):.0f} in favor of P_K", f"≈ {round(math.exp(15 / RT), -1):.0f} in favor of P_T",
        f"about {round(math.exp(20 / RT), -2):.0f} times",
    )


def test_worked_example_matches_an_independent_profile_calculation():
    reactant, product = boltzmann(0, -20)
    products = product / reactant
    rate = PREFACTOR * math.exp(-96 / RT)
    faster = half_life(96 - 0.70 * 30)
    capture = PREFACTOR * math.exp(-(68 - 60) / RT)
    stated(
        f"K = e^(20/2.48) ≈ {products / 1e3:.1f} × 10³", f"= {rate * 1e5:.1f} × 10⁻⁵ s⁻¹",
        f"ln 2/k ≈ {round(half_life(96), -2):.0f} s, about {half_life(96) / 3600:.1f} hours",
        f"half-life falls to about {faster:.1f} s", f"near {capture / 1e11:.1f} × 10¹¹ s⁻¹",
    )
    worked = next(
        lesson for module in MANIFEST["modules"] for lesson in module["lessons"] if lesson["id"] == "organic-chemistry-21"
    )["worked_example"]
    assert "K ≈ 3.2 × 10³" in worked and "9.2 × 10⁻⁵ s⁻¹" in worked and "about 1.6 s" in worked


def test_rate_determining_item_is_a_profile_where_the_largest_climb_misleads():
    ts1, intermediate, ts2 = 70, 45, 82
    assert ts1 - 0 > ts2 - intermediate  # step 1 has the larger single climb
    assert max(ts1, ts2) == ts2  # yet TS2 is the highest point and limits the rate
    assert BANK["organic-chemistry-21:rate-determining-step"]["solution_spec"]["answer"] == 1


def test_lesson_is_scheduled_before_substitution_and_links_its_prerequisite_course():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[2]["lesson_ids"] == ["organic-chemistry-8", "organic-chemistry-21"]
    assert "organic-chemistry-21-practice" in weeks[2]["assessment_ids"]
    assert "organic-chemistry-6" in weeks[3]["lesson_ids"]
    assert "general-chemistry-2" in MANIFEST["prerequisites"]["course_ids"]
    for target in ("08-free-energy-and-equilibrium.md", "06-rate-laws-half-lives-and-arrhenius.md"):
        assert f"](../../general-chemistry-2/modules/{target})" in READING
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == (
        "partial", "unreviewed", "formative-only")
    assert "link-only scope comparators" in READING and "partial, unreviewed and formative-only" in READING


def test_crosswalk_records_both_comparators_and_its_title_level_limits():
    for phrase in (
        "https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2005/pages/calendar/",
        "https://open.uci.edu/courses/chem_51a_organic_chemistry_nowick.html",
        "compiled with AI assistance", "not a review by the owner", "first course of UCI's three-quarter organic sequence",
        "| Reaction energetics: thermodynamics, kinetics and energy diagrams | 8–11 | 18–20 |", "| Alkane nomenclature | — | 11 | — | Absent |",
        "| Alcohols and phenols | 27 | — | — | Shallow", "Absent by policy",
    ):
        assert phrase in CROSSWALK, phrase
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    links = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    assert {link for link in links if not link.startswith("https://")} <= readings
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    uci = registry["orgo-uci-chem51a"]
    assert uci["reuse_mode"] == "link-only-comparator" and not uci["permissions"]["adaptation"]
    assert "organic-chemistry-module-21" in uci["mapped_modules"]


MISCONCEPTIONS = {
    "conformer-minor-fraction": 19.9,  # K reported as the fraction
    "pka-free-energy": 17.1,  # sign dropped
    "bde-enthalpy": 120,  # bonds formed minus bonds broken
    "entropy-crossover": 0.3,  # joules and kilojoules mixed
    "barrier-for-hundredfold": 5.7,  # tenfold value
    "tst-half-life": 127.8,  # 1/k instead of ln 2/k
    "kinetic-ratio": 37.8,  # product energies used under irreversible conditions
    "thermodynamic-ratio": 11.3,  # barriers used at equilibrium
}


@pytest.mark.parametrize("slug,wrong", MISCONCEPTIONS.items(), ids=list(MISCONCEPTIONS))
def test_numeric_keys_reject_the_named_misconception(slug, wrong):
    item = BANK[f"organic-chemistry-21:{slug}"]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct
