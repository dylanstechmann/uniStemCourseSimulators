"""Biochemistry 0.7.0 lessons 33 (membranes) and 34 (signal transduction): stated numbers, schedule, comparators, grading.

Diffusion is checked with a seeded two-dimensional random walk, leaflet asymmetry and messenger levels by integrating their rate
equations, EC50 by bisection of the transducer response, and hydropathy by scoring the sequence, not from the readings.
Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
import random
import re
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
R33 = (COURSE / "modules/33-membrane-lipids-bilayers-and-membrane-proteins.md").read_text(encoding="utf-8")
R34 = (COURSE / "modules/34-receptors-g-protein-switches-and-second-messengers.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
SCALE = {**dict.fromkeys("ILVFMAC", 1), **dict.fromkeys("GSTPYHW", 0), **dict.fromkeys("DEKRNQ", -1)}


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


def packing(volume, area, length):
    return volume / (area * length)


def aggregate(p):
    return "spherical micelles" if p < 1 / 3 else "cylindrical micelles" if p < 1 / 2 else "bilayer" if p <= 1 else "inverted"


def integrate(rate, start, end, steps=20000):
    """Fourth-order Runge-Kutta for a scalar ODE dy/dt = rate(y) from t = 0 to end."""
    y, h = start, end / steps
    for _ in range(steps):
        k1 = rate(y)
        k2 = rate(y + h * k1 / 2)
        k3 = rate(y + h * k2 / 2)
        k4 = rate(y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return y


def response(ligand, kd, tau):
    theta = ligand / (ligand + kd)
    return theta * tau / (1 + theta * tau)  # unnormalized transducer output; its maximum is tau / (1 + tau)


def ec50(kd, tau):
    half = tau / (1 + tau) / 2
    low, high = 0.0, 1000 * kd
    for _ in range(200):
        middle = (low + high) / 2
        low, high = (middle, high) if response(middle, kd, tau) < half else (low, middle)
    return (low + high) / 2


def test_membrane_reading_numbers_recompute():
    single, double, small_head = packing(0.35, 0.70, 1.67), packing(0.92, 0.70, 1.75), packing(0.92, 0.45, 1.75)
    assert [aggregate(p) for p in (single, double, small_head)] == ["spherical micelles", "bilayer", "inverted"]
    stated(R33, f"= {single:.3f}, below 1/3", f"= {double:.3f}, so it forms a bilayer", f"gives P = {small_head:.2f}")
    sequence = "LLVAIFGLLAVLMSCAVLW"
    mean = sum(SCALE[residue] for residue in sequence) / len(sequence)
    assert len(sequence) == 19 and sum(SCALE[r] == 1 for r in sequence) == 16 and mean > 0.5
    stated(R33, f"16/19 = {mean:.3f}", f"{19 * 0.15:.2f} nm long", "3.0/0.15 = 20 residues", f"560/800 = {560 / 800:.2f}")
    assert round(3.0 / 0.15) == 20 and (760 - 200) / (1000 - 200) == pytest.approx(0.70)
    stated(R33, "⟨r²⟩ = 4.0 µm² after 1 s, a root-mean-square displacement of 2.0 µm", f"moves {math.sqrt(4 * 0.05):.2f} µm in the same second",
           f"takes {4.0 / (4 * 0.05):.0f} s to reach 2.0 µm", "⟨r²⟩ = 4 × 0.10 × 10 = 4.0 µm²")


def test_two_dimensional_random_walk_gives_four_d_t():
    rng = random.Random(20261029)
    diffusion, total, steps, walkers = 0.10, 10.0, 40, 4000
    sigma = math.sqrt(2 * diffusion * total / steps)  # per-axis step for variance 2 D dt
    squares = []
    for _ in range(walkers):
        x = y = 0.0
        for _ in range(steps):
            x += rng.gauss(0, sigma)
            y += rng.gauss(0, sigma)
        squares.append(x * x + y * y)
    assert math.fsum(squares) / walkers == pytest.approx(4 * diffusion * total, rel=0.05)


def test_leaflet_asymmetry_halves_in_half_the_flip_half_time():
    half_time = 8.0
    k = math.log(2) / half_time
    outer = integrate(lambda x: k * (1 - 2 * x), 1.0, half_time)
    assert outer == pytest.approx(0.625, abs=1e-6)
    assert integrate(lambda x: k * (1 - 2 * x), 1.0, half_time / 2) - 0.5 == pytest.approx(0.25, abs=1e-6)
    stated(R33, "x − 1/2 decays as e^(−2kt)", "the asymmetry halves every t½/2")


def test_signalling_reading_numbers_recompute():
    kd, tau, ligand = 5.0, 9.0, 15.0
    theta = ligand / (ligand + kd)
    normalized = response(ligand, kd, tau) / (tau / (1 + tau))
    assert normalized == pytest.approx((1 + tau) * theta / (1 + tau * theta))
    assert ec50(kd, tau) == pytest.approx(kd / (1 + tau), rel=1e-9)
    assert ec50(kd, 0.2 * tau) == pytest.approx(5.0 / 2.8, rel=1e-9)
    top = (0.2 * tau / (1 + 0.2 * tau)) / (tau / (1 + tau))
    half_occupancy = (kd / (1 + tau)) / (kd / (1 + tau) + kd)
    assert half_occupancy == pytest.approx(1 / (2 + tau))
    stated(R34, f"θ = 15/(15 + 5.0) = {theta:.2f}", f"7.5/7.75 = {normalized:.3f}", "5.0/10 = 0.50 nM", f"5.0/2.8 = {5.0 / 2.8:.2f} nM",
           f"= {top:.3f}", f"about {round(100 * (1 - top))} per cent", "half-maximal at 1/11 occupancy")
    lifetime_slow, lifetime_fast = 1 / 0.05, 1 / 2.0
    stated(R34, f"lasts {lifetime_slow:.0f} s on average", f"it lasts {lifetime_fast} s", f"20 × 20 = {20 * 20:.0f} cAMP",
           f"20 × 0.5 = {20 * 0.5:.0f} with it", f"produces {30 * 400:,} cAMP", f"at most {30 * 400 // 4 * 2:,} catalytic subunits")


def test_g_protein_timer_and_camp_balance_by_integration():
    # Mean active lifetime = integral of the surviving fraction e^(-kt).
    k = 0.05
    survivors = math.fsum(math.exp(-k * (i + 0.5) * 0.01) * 0.01 for i in range(100_000))
    assert survivors == pytest.approx(1 / k, rel=1e-3)
    for synthesis, removal, expected in ((1.2, 3.0, 0.40), (1.2, 0.75, 1.6), (0.90, 1.5, 0.60), (0.90, 0.50, 1.80)):
        level = integrate(lambda c: synthesis - removal * c, 0.0, 20 / removal)
        assert level == pytest.approx(expected, rel=1e-6)
        one_tau = integrate(lambda c: synthesis - removal * c, 0.0, 1 / removal)
        assert one_tau / expected == pytest.approx(1 - math.exp(-1), rel=1e-6)
    stated(R34, "the steady state is 0.40 µM and the time constant 0.33 s", "fourfold, to 1.6 µM")


def test_lessons_are_scheduled_before_the_lessons_that_use_them():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[8]["lesson_ids"] == ["biochemistry-6", "biochemistry-nucleotide-biosynthesis", "biochemistry-33", "biochemistry-28"]
    assert weeks[8]["assessment_ids"][-2:] == ["biochemistry-33-practice", "biochemistry-28-practice"]
    assert weeks[12]["lesson_ids"][:3] == ["biochemistry-34", "biochemistry-4", "biochemistry-glycogen-metabolism"]
    assert weeks[12]["assessment_ids"][0] == "biochemistry-34-practice"
    for text, targets in ((R33, ("alternating-access-and-coupled-transport-cycles.md", "11-mitochondrial-bioenergetics-and-atp-yield.md",
                                 "09-protein-folding-and-stability.md", "../../cell-biology/modules/02-membranes-transport-and-compartmentalization.md")),
                          (R34, ("17-glycogen-storage-and-mobilization.md", "23-fatty-acid-synthesis.md", "07-binding-equilibria-and-cooperativity.md",
                                 "../../cell-biology/modules/10a-receptor-signaling-and-network-logic.md",
                                 "../../geroscience/modules/07-nutrient-sensing-and-lifespan-interventions.md"))):
        for target in targets:
            assert f"]({target})" in text and (COURSE / "modules" / target).resolve().exists(), target
        stated(text, "link-only scope comparators", "partial, unreviewed and formative-only", "gives no laboratory protocol", "substantial AI assistance")
    assert "medical advice" in R34 and "Nothing here describes a drug, a dose or a treatment" in R34
    assert (MANIFEST["version"], MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == (
        "0.7.0", "partial", "unreviewed", "formative-only")
    objectives = {o["id"]: o for o in MANIFEST["lesson_objectives"]}
    outcomes = {o["id"] for o in MANIFEST["outcomes"]}
    lessons = {x["id"]: x for m in MANIFEST["modules"] for x in m["lessons"]}
    for lesson_id, text, count in (("biochemistry-33", R33, 12), ("biochemistry-34", R34, 13)):
        lesson = lessons[lesson_id]
        covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
        assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == count and len(lesson["card_ids"]) == 4
        assert {c["id"] for c in CARDS if c["lesson_id"] == lesson_id} == set(lesson["card_ids"])
        assert len(text.split()) >= 1500
        for objective_id in lesson["objectives"]:
            assert objectives[objective_id]["description"] in text
            assert set(objectives[objective_id]["course_outcome_ids"]) <= outcomes


def test_crosswalk_records_both_comparators_and_its_limits():
    stated(CROSSWALK, "https://ocw.mit.edu/courses/7-05-general-biochemistry-spring-2020/pages/calendar/",
           "https://www.uoguelph.ca/mcb/system/files/BIOC3560_W23_SG_Final_0.pdf", "compiled with AI assistance", "not a review by the owner",
           "| Membrane lipids, bilayer organization, membrane proteins and dynamics | Session 12 (introduction to membranes) | Part E |",
           "Covered in 0.7.0; previously absent", "Covered in 0.7.0; previously shallow", "| The Bohr effect and O₂, H⁺ and CO₂ transport | Session 7 | Part A | [7](modules/07-binding-equilibria-and-cooperativity.md) | Shallow:",
           "| Proteolytic activation of enzymes | — | Part B | — | Absent; named only by Guelph |", "Absent by design", "third-year course")
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    local = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    local = {link for link in local if not link.startswith("https://")}
    assert all((COURSE / link).resolve().exists() for link in local)
    assert {link for link in local if link.startswith(("modules/", "labs/"))} <= readings
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for sid in ("biochem-guelph-bioc3560", "biochem-semester-calendar"):
        assert registry[sid]["reuse_mode"] == "link-only-comparator" and not registry[sid]["permissions"]["quotation"], sid
        assert {"biochemistry-module-33", "biochemistry-module-34"} <= set(registry[sid]["mapped_modules"]), sid
    modules = {m["id"]: m for m in MANIFEST["modules"]}
    assert all("biochem-guelph-bioc3560" in modules[f"biochemistry-module-{n}"]["source_ids"] for n in (33, 34))


# Lesson 7 names 2,3-bisphosphoglycerate, pH and CO2 in one sentence, so the crosswalk labels the Bohr effect shallow, not absent.
ABSENT_TERMS = (r"\bBohr\b", r"\bzymogen", r"proteolytic activation", r"\blay summary\b")


def test_topics_the_crosswalk_labels_absent_appear_in_no_local_reading():
    for module in MANIFEST["modules"]:
        for lesson in module["lessons"]:
            text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
            for term in ABSENT_TERMS:
                assert not re.search(term, text, re.IGNORECASE), (lesson["id"], term)


def three(value):
    return f"{value:.{max(0, 2 - math.floor(math.log10(abs(value))))}f}"


MISCONCEPTIONS = {
    "33": {
        "packing-parameter-single-chain": 0.400 / 0.900 * 1.50,  # multiplying by the length
        "helix-residues-to-span": 3.3 / 0.33,  # the beta-strand rise
        "hydropathy-window-mean": 13 / 19,  # ignoring the charged residues
        "frap-mobile-fraction": 840 / 1200,  # plateau over the starting intensity
        "lateral-rms-displacement": 4 * 0.30 * 3.0,  # forgetting the square root
        "lipid-diffusion-time": 36 / (2 * 1.5),  # the one-dimensional 2Dt
        "leaflet-asymmetry-decay": 0.75,  # decay at k instead of 2k
    },
    "34": {
        "receptor-occupancy": 8.0 / 20,  # K_d over the total
        "ligand-for-ninety-percent": 0.9 * 3.0,  # occupancy times K_d
        "spare-receptor-ec50": 20,  # EC50 equal to K_d
        "receptor-loss-ec50": 5.0 / (1 + 0.6 * 9),  # keeping the removed fraction
        "galpha-active-fraction": 1 - math.exp(-0.5),  # the hydrolyzed fraction
        "camp-per-activation": 15 * 0.050,  # multiplying by the rate constant
        "pka-catalytic-subunits": 25 * 400,  # one cAMP per catalytic subunit
        "camp-steady-state": 0.90 * 1.5,  # multiplying by the rate constant
        "pde-inhibitor-steady-state": 0.90 / 1.5 / 3,  # lowering instead of raising
    },
}
CASES = [(lesson, slug, wrong) for lesson, group in MISCONCEPTIONS.items() for slug, wrong in group.items()]


@pytest.mark.parametrize("lesson,slug,wrong", CASES, ids=[f"{lesson}-{slug}" for lesson, slug, _ in CASES])
def test_numeric_keys_accept_the_key_and_reject_the_named_misconception(lesson, slug, wrong):
    item = BANK[f"biochemistry-{lesson}:{slug}"]
    spec = item["solution_spec"]
    answer = spec["answer"]
    shown = three(answer) if spec["significant_figures"] == 3 else f"{answer:.0f}"
    assert grade(item, AttemptRequest(response=shown)).correct, shown
    wrong_shown = three(wrong) if spec["significant_figures"] == 3 else f"{wrong:.0f}"
    assert not grade(item, AttemptRequest(response=wrong_shown)).correct, wrong_shown


def test_every_new_numeric_item_has_a_named_misconception_and_three_figure_items_say_so():
    numeric = {qid for qid, q in BANK.items() if q["type"] == "numeric" and re.match(r"biochemistry-3[34]:", qid)}
    assert numeric == {f"biochemistry-{lesson}:{slug}" for lesson, group in MISCONCEPTIONS.items() for slug in group}
    for qid in numeric:
        spec = BANK[qid]["solution_spec"]
        if spec["significant_figures"] == 3:
            assert BANK[qid]["prompt"].endswith("to three significant figures."), qid
            full = grade(BANK[qid], AttemptRequest(response=three(spec["answer"]) + "0"))  # a fourth figure
            assert not full.correct, qid


@pytest.mark.parametrize("item_id", ["33:packing-parameter-aggregate", "33:small-headgroup-effect", "33:transition-temperature-order",
                                     "33:peripheral-classification", "34:cholera-toxin-mechanism", "34:phospholipase-c-messengers",
                                     "34:insulin-route-order"])
def test_single_choice_items_accept_only_the_key(item_id):
    item = BANK[f"biochemistry-{item_id}"]
    key = item["solution_spec"]["answer"]
    accepted = [index for index in range(len(item["options"])) if grade(item, AttemptRequest(response=str(index))).correct]
    assert accepted == [key]


def test_choice_keys_follow_from_the_models():
    assert aggregate(packing(0.96, 0.75, 1.60)) == BANK["biochemistry-33:packing-parameter-aggregate"]["options"][
        BANK["biochemistry-33:packing-parameter-aggregate"]["solution_spec"]["answer"]].lower().removeprefix("a ")


@pytest.mark.parametrize("item_id", ["33:membrane-claims", "34:signaling-claims"])
def test_multiple_select_items_give_partial_credit_for_correct_minus_incorrect(item_id):
    item = BANK[f"biochemistry-{item_id}"]
    assert item["solution_spec"]["answer"] == [0, 2, 4] and item["points"] == 2
    scores = {tuple(r): grade(item, AttemptRequest(response=r)).score for r in ([0, 2, 4], [0, 2, 4, 1], [0, 2], [1, 3], [0, 1, 2, 3, 4])}
    assert scores[(0, 2, 4)] == pytest.approx(2.0) and scores[(0, 2, 4, 1)] == pytest.approx(4 / 3) and scores[(0, 2)] == pytest.approx(4 / 3)
    assert scores[(1, 3)] == 0 and scores[(0, 1, 2, 3, 4)] == pytest.approx(2 / 3)
