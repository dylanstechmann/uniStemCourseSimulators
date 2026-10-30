"""Genetics 0.9.0 lessons 28 (chromosome rearrangements) and 29 (cancer genetics): stated numbers, schedule, comparators, grading.

Deletion mapping is checked with band sets, unequal crossing over by joining copy lists, inversion products by a seeded
simulation of which chromatids cross over, translocation segregation by enumerating segment content, loss-of-heterozygosity
routes by applying each route to a marker map, tumor counts by summing the Poisson series, two hits with exact exponentials,
multistage incidence with the Erlang density and clonal expansion by numerical integration, not from the readings.
Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
import random
import re
from collections import Counter
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/genetics"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
R28 = (COURSE / "modules/28-chromosome-rearrangements.md").read_text(encoding="utf-8")
R29 = (COURSE / "modules/29-genetics-of-cancer-two-hits-and-age.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


# ---- lesson 28 ----

def test_deletion_mapping_by_band_sets():
    deletions = {"Df1": set(range(1, 5)), "Df2": set(range(3, 7)), "Df3": set(range(5, 9))}
    uncovered_by = {"Df1", "Df2"}
    candidates = set.intersection(*(deletions[d] for d in uncovered_by)) - set.union(*(deletions[d] for d in deletions if d not in uncovered_by))
    assert candidates == {3, 4}
    item = BANK["genetics-28:deletion-mapping"]
    assert item["options"][item["solution_spec"]["answer"]] == "Bands 3–4"
    stated(R28, "bands 1–4 (Df1), 3–6 (Df2) and 5–8 (Df3)", "bands 3–4")


def unequal_products(copies, offset, after):
    first = [f"x{i}" for i in range(copies)]
    second = [f"y{i}" for i in range(copies)]
    # copy `after` of the first homolog pairs with copy `after - offset` of the second; exchange just after that pair
    return first[: after + 1] + second[after - offset + 1:], second[: after - offset + 1] + first[after + 1:]


def test_unequal_crossing_over_by_joining_copy_lists():
    for copies, offset in ((3, 1), (5, 2), (6, 1)):
        longer, shorter = unequal_products(copies, offset, after=copies - 1)
        assert sorted((len(longer), len(shorter))) == [copies - offset, copies + offset]
    stated(R28, "products with 4 and 2", "n copies offset by k give n + k and n − k")


def unbalanced_fraction(loop_crossover_fraction, meioses=200000, seed=7):
    """Seeded simulation: in a loop-crossover meiosis one chromatid of each homolog takes part; one random product is sampled."""
    rng = random.Random(seed)
    unbalanced = 0
    for _ in range(meioses):
        chromatids = ["normal-1", "normal-2", "inverted-1", "inverted-2"]
        crossed = set()
        if rng.random() < loop_crossover_fraction:
            crossed = {rng.choice(chromatids[:2]), rng.choice(chromatids[2:])}
        unbalanced += rng.choice(chromatids) in crossed
    return unbalanced / meioses


def test_inversion_loop_products_by_simulation():
    assert unbalanced_fraction(0.40) == pytest.approx(0.20, abs=0.005)
    assert unbalanced_fraction(0.30) == pytest.approx(0.15, abs=0.005)
    assert 2 * 0.15 == pytest.approx(0.30)
    stated(R28, "f × 2/4 = f/2", "With f = 0.40, 20% of products are unbalanced", "2 × 0.15 = 0.30",
           "show bridges in about 30% of meiocytes and lose about 15% of its products", "0.30 × 2/4 = 0.15, and 0.85 of products are balanced",
           "The inversion did not stop crossing over; it removed the recombinant products.")


SEGMENTS = {"N1": ("cen1", "A", "B"), "N2": ("cen2", "C", "D"), "T1": ("cen1", "A", "D"), "T2": ("cen2", "C", "B")}
MODES = {"alternate": (("N1", "N2"), ("T1", "T2")), "adjacent-1": (("N1", "T2"), ("N2", "T1")), "adjacent-2": (("N1", "T1"), ("N2", "T2"))}


def balanced(gamete):
    content = Counter(part for chromosome in gamete for part in SEGMENTS[chromosome][1:])
    return all(content[part] == 1 for part in "ABCD")


def test_translocation_segregation_by_enumerating_segments():
    for mode, gametes in MODES.items():
        assert all(balanced(g) == (mode == "alternate") for g in gametes), mode
    centromeres = {mode: [sorted(SEGMENTS[c][0] for c in g) for g in gametes] for mode, gametes in MODES.items()}
    assert all(c == ["cen1", "cen2"] for c in centromeres["adjacent-1"]) and all(len(set(c)) == 1 for c in centromeres["adjacent-2"])
    frequencies = {"alternate": 0.55, "adjacent-1": 0.40, "adjacent-2": 0.05}
    viable = [g for mode, gametes in MODES.items() for g in gametes for _ in range(round(frequencies[mode] * 100)) if balanced(g)]
    assert len(viable) / (2 * 100) == pytest.approx(0.55)
    assert sum(set(g) == {"T1", "T2"} for g in viable) / len(viable) == pytest.approx(0.5)
    # pseudolinkage: a marker on segment B and one on segment D are on N1/N2 or T2/T1 together in every viable gamete
    origins = {("N1", "N2"): "standard", ("T1", "T2"): "translocated"}
    assert {origins[tuple(sorted(g))] for g in viable} == {"standard", "translocated"}
    stated(R28, "55% of gametes are balanced", "half carry the balanced translocation", "pseudolinkage", "45 chromosomes")


def log2_ratio(fraction_changed, change):
    return math.log2((2 * (1 - fraction_changed) + (2 + change) * fraction_changed) / 2)


def test_copy_number_ratios_by_averaging_cells():
    assert log2_ratio(1.0, -1) == pytest.approx(-1) and log2_ratio(1.0, +1) == pytest.approx(0.585, abs=5e-4)
    assert log2_ratio(0.40, -1) == pytest.approx(-0.322, abs=5e-4)
    m = 2 * (2 ** 0.263 - 1)
    assert m == pytest.approx(0.400, abs=5e-4) and log2_ratio(m, +1) == pytest.approx(0.263)
    stated(R28, "log₂(1/2) = −1", "log₂(3/2) = 0.585", "log₂(0.8) = −0.322", "2^0.263 = 1.20 and m = 0.400",
           "Inversions and reciprocal translocations change no copy number")


# ---- lesson 29 ----

def poisson(k, mean):
    return math.exp(-mean) * mean**k / math.factorial(k)


def test_knudson_poisson_fractions_by_series():
    none = poisson(0, 3)
    # each tumor lands in either eye with probability 1/2; sum over the number of tumors
    both = sum(poisson(n, 3) * (1 - 2 * 0.5**n + (n == 0)) for n in range(80))
    one = sum(poisson(n, 3) * (2 * 0.5**n - 2 * (n == 0)) for n in range(80))
    assert none == pytest.approx(0.0498, abs=5e-5) and both == pytest.approx(0.604, abs=5e-4) and one == pytest.approx(0.347, abs=5e-4)
    assert none + both + one == pytest.approx(1)
    assert math.exp(-1.5) == pytest.approx(0.223, abs=5e-4) and 1 - none == pytest.approx(0.95, abs=0.005)
    stated(R29, "e^(−3) = 0.0498", "e^(−1.5) = 0.223", "(1 − 0.223)² = 0.604", "2 × 0.223 × 0.777 = 0.347", "0.223² = 0.0498",
           "observations on 48 cases of retinoblastoma", "average of three tumors")


def test_knudson_worked_example():
    mean = -math.log(0.08)
    eye = math.exp(-mean / 2)
    assert mean == pytest.approx(2.53, abs=0.005) and mean / 2 == pytest.approx(1.26, abs=0.005) and eye == pytest.approx(0.283, abs=5e-4)
    assert (1 - eye) ** 2 == pytest.approx(0.514, abs=5e-4) and 2 * eye * (1 - eye) == pytest.approx(0.406, abs=5e-4)
    stated(R29, "m = −ln 0.08 = 2.53", "e^(−1.26) = 0.283", "(1 − 0.283)² = 0.514", "2 × 0.283 × 0.717 = 0.406")


def test_one_hit_and_two_hit_expectations_with_exact_exponentials():
    cells, rate, years = 1e6, 1e-6, 3
    carrier = cells * (1 - math.exp(-rate * years))
    non_carrier = cells * (1 - math.exp(-rate * years)) ** 2  # either copy may be hit first
    assert carrier == pytest.approx(3, rel=1e-5) and non_carrier * 1e6 == pytest.approx(9.00, abs=0.005)
    ordered = cells * (rate * years) ** 2 / 2  # one fixed order of two steps, the multistage form
    assert non_carrier / ordered == pytest.approx(2, rel=1e-5)
    stated(R29, "Nμt = 10⁶ × 10⁻⁶ × 3 = 3", "N(μt)² = 10⁶ × (3 × 10⁻⁶)² = 9 × 10⁻⁶, or 9.00 per million people")
    assert "(μt)²/2" not in R29


def erlang_density(age, steps, rate):
    return rate**steps * age ** (steps - 1) * math.exp(-rate * age) / math.factorial(steps - 1)


def test_multistage_slope_mutator_and_expansion():
    for steps in (5, 6):
        ratio = erlang_density(80, steps, 1e-4) / erlang_density(40, steps, 1e-4)
        assert ratio == pytest.approx(2 ** (steps - 1), rel=0.01)
    assert math.log2(384 / 12) + 1 == pytest.approx(6) and (70 / 50) ** 5 == pytest.approx(5.38, abs=0.005)
    rate, factor = 1e-7, 8
    assert (1 - math.exp(-factor * rate)) ** 2 / (1 - math.exp(-rate)) ** 2 == pytest.approx(64, rel=1e-5)
    steps = 200000
    exposure = sum(math.exp(0.3 * (k + 0.5) * 20 / steps) for k in range(steps)) * 20 / steps
    assert exposure == pytest.approx(1341, abs=0.5) and exposure / 20 == pytest.approx(67, abs=0.5)
    stated(R29, "384 at age 80 rises by a factor of 32", "2^5 = 32", "k = 6 steps", "(70/50)^5 = 5.38", "2^4 = 16",
           "an eightfold rise in μ gives a 64-fold rise", "(e^6 − 1)/0.3 = 1341 cell-years", "about 67 times as many")


MARKERS = 10


def loh_route(route):
    """Return (copy numbers, heterozygous flags) for markers 0..9 after a second hit; the exchange or deletion sits at marker 4-6."""
    copies = [2] * MARKERS
    alleles = [{"A", "a"} for _ in range(MARKERS)]
    if route == "point mutation":
        pass
    elif route == "interstitial deletion":
        for i in range(4, 7):
            copies[i], alleles[i] = 1, {"A"}
    elif route == "mitotic recombination":
        for i in range(5, MARKERS):
            alleles[i] = {"A"}
    elif route == "chromosome loss":
        copies, alleles = [1] * MARKERS, [{"A"} for _ in range(MARKERS)]
    elif route == "loss and reduplication":
        alleles = [{"A"} for _ in range(MARKERS)]
    return copies, [len(a) == 2 for a in alleles]


def classify(copies, heterozygous):
    if all(heterozygous):
        return "point mutation"
    if all(c == 1 for c in copies):
        return "chromosome loss"
    if any(c == 1 for c in copies):
        return "interstitial deletion"
    if not any(heterozygous):
        return "loss and reduplication"
    lost = [i for i, h in enumerate(heterozygous) if not h]
    return "mitotic recombination" if lost == list(range(lost[0], MARKERS)) else "unclassified"


def test_loss_of_heterozygosity_routes_by_marker_maps():
    for route in ("point mutation", "interstitial deletion", "mitotic recombination", "chromosome loss", "loss and reduplication"):
        assert classify(*loh_route(route)) == route
    item = BANK["genetics-29:loh-route"]
    assert item["options"][item["solution_spec"]["answer"]] == "Mitotic recombination"
    copies, heterozygous = loh_route("mitotic recombination")
    assert set(copies) == {2} and heterozygous[:5] == [True] * 5 and not any(heterozygous[5:])
    stated(R29, "| Mitotic recombination | 2 | LOH distal to the exchange, heterozygosity proximal |",
           "| Loss followed by reduplication | 2 | LOH along the whole chromosome, copy-neutral |")


# ---- schedule, comparators and claims ----

def test_lessons_are_scheduled_after_the_lessons_they_build_on():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[6]["lesson_ids"][:2] == ["genetics-12", "genetics-28"]
    assert weeks[6]["assessment_ids"][:2] == ["genetics-12-practice", "genetics-28-practice"]
    assert weeks[8]["lesson_ids"] == ["genetics-13", "genetics-29"]
    assert weeks[8]["assessment_ids"] == ["genetics-13-practice", "genetics-29-practice"]
    for text, targets in ((R28, ("12-nondisjunction-aneuploidy-and-maternal-age.md", "phage-functional-maps.md", "29-genetics-of-cancer-two-hits-and-age.md",
                                 "14-measuring-gene-expression-normalization-and-false-discoveries.md",
                                 "../../geroscience/modules/03b-clonal-hematopoiesis-and-circulating-factors.md")),
                          (R29, ("13-mutation-rates-fluctuation-test-and-somatic-mutation.md", "28-chromosome-rearrangements.md",
                                 "01-segregation-penetrance-and-probability.md", "12-nondisjunction-aneuploidy-and-maternal-age.md",
                                 "../../cell-biology/modules/06b-dna-damage-and-repair-evidence.md",
                                 "../../cell-biology/modules/12a-cell-cycle-checkpoints-and-mitosis.md",
                                 "../../geroscience/modules/03b-clonal-hematopoiesis-and-circulating-factors.md"))):
        for target in targets:
            assert f"]({target})" in text and (COURSE / "modules" / target).resolve().exists(), target
        stated(text, "gives no genetic-counselling or medical advice", "synthetic")
    stated(R29, "checked for its record and abstract", "its scanned text was not read")
    assert (MANIFEST["version"], MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == (
        "0.9.0", "partial", "unreviewed", "formative-only")
    objectives = {o["id"]: o for o in MANIFEST["lesson_objectives"]}
    outcomes = {o["id"] for o in MANIFEST["outcomes"]}
    lessons = {x["id"]: x for m in MANIFEST["modules"] for x in m["lessons"]}
    for lesson_id, text in (("genetics-28", R28), ("genetics-29", R29)):
        lesson = lessons[lesson_id]
        covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
        assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == 12 and len(lesson["card_ids"]) == 4
        assert {c["id"] for c in CARDS if c["lesson_id"] == lesson_id} == set(lesson["card_ids"])
        assert len(text.split()) >= 1400
        for objective_id in lesson["objectives"]:
            assert objectives[objective_id]["description"] in text
            assert set(objectives[objective_id]["course_outcome_ids"]) <= outcomes
        practice = next(a for a in MANIFEST["assessments"] if a["id"] == f"{lesson_id}-practice")
        assert practice["mode"] == "practice" and practice["points"] == sum(BANK[q]["points"] for q in lesson["question_ids"]) == 14


def test_crosswalk_and_registry_record_the_comparators_and_papers():
    stated(CROSSWALK, "https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/calendar/",
           "https://biology.columbia.edu/sites/default/files/content/Syllabi/UN3031%20Genetics%20Sp23.pdf", "compiled with AI assistance",
           "not a review by the owner", "| Chromosome rearrangements | Lec 32–33 (Chromosome Anomalies) | Lec 7–9 (Rearrangements in model systems and humans) |",
           "| Genetics of cancer | Lec 34–35 | Lec 24 |", "Covered in 0.9.0; previously absent", "Absent by design")
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    local = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    local = {link for link in local if not link.startswith("https://")}
    assert all((COURSE / link).resolve().exists() for link in local)
    assert {link for link in local if link.startswith(("modules/", "labs/"))} <= readings
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    columbia = registry["genetics-columbia-un3031"]
    assert columbia["reuse_mode"] == "link-only-comparator" and not columbia["permissions"]["quotation"] and columbia["accessed_at"] == "2026-10-30"
    for sid in ("genetics-columbia-un3031", "genetics-703"):
        assert {"genetics-module-28", "genetics-module-29"} <= set(registry[sid]["mapped_modules"]), sid
    for sid, pmid in (("knudson-1971-retinoblastoma", "5279523"), ("armitage-doll-1954-multistage", "13172380")):
        record = registry[sid]
        assert record["reuse_mode"] == "link-only-reference" and record["url"] == f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        assert f"PMID {pmid}" in record["version"] and record["mapped_modules"] == ["genetics-module-29"]
    assert "scanned text was not read" in registry["armitage-doll-1954-multistage"]["version"]
    modules = {m["id"]: m for m in MANIFEST["modules"]}
    assert set(modules["genetics-module-29"]["source_ids"]) >= {"knudson-1971-retinoblastoma", "armitage-doll-1954-multistage", "genetics-columbia-un3031"}


# Topics the crosswalk labels absent are named in no local reading.
ABSENT_TERMS = (r"\bMuller", r"forward genetic", r"genetic screen", r"positional cloning", r"clonal analysis", r"\bHolliday")


def test_topics_the_crosswalk_labels_absent_appear_in_no_local_reading():
    for module in MANIFEST["modules"]:
        for lesson in module["lessons"]:
            text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
            for term in ABSENT_TERMS:
                assert not re.search(term, text, re.IGNORECASE), (lesson["id"], term)


# ---- grading ----

def shown(value, sig):
    if sig == 3:
        return f"{value:.{max(0, 2 - math.floor(math.log10(abs(value))))}f}"
    return f"{value:g}"


MISCONCEPTIONS = {
    "28": {
        "inversion-unbalanced": 0.40,  # counting all four products
        "bridge-fraction": 0.15,  # map distance without the two-of-four factor
        "balanced-gametes": 0.55 + 0.40,  # counting adjacent-1 as balanced
        "carriers-among-viable": 0.25,  # one of four products
        "unequal-crossover-copies": 7,  # the longer product
        "mosaic-loss-ratio": -1.0,  # as if every cell had lost a copy
        "mosaic-gain-fraction": 2**0.263 - 1,  # forgetting the factor of two
    },
    "29": {
        "no-tumor-fraction": 1 - math.exp(-3),  # the affected fraction
        "bilateral-fraction": 2 * math.exp(-1.5) * (1 - math.exp(-1.5)),  # the unilateral fraction
        "mean-from-unaffected": -math.log10(0.10),  # base-10 logarithm
        "sporadic-per-million": 4.5,  # the ordered-step half
        "multistage-steps": 5,  # the slope, not the number of steps
        "incidence-ratio": (70 / 50) ** 6,  # exponent k instead of k - 1
        "mutator-two-hit": 2 * 8,  # adding instead of multiplying
        "clonal-expansion-fold": (math.exp(5) - 1) / 10,  # dropping the 1/r
    },
}
CASES = [(lesson, slug, wrong) for lesson, group in MISCONCEPTIONS.items() for slug, wrong in group.items()]


@pytest.mark.parametrize("lesson,slug,wrong", CASES, ids=[f"{lesson}-{slug}" for lesson, slug, _ in CASES])
def test_numeric_keys_accept_the_key_and_reject_the_named_misconception(lesson, slug, wrong):
    item = BANK[f"genetics-{lesson}:{slug}"]
    spec = item["solution_spec"]
    sig = spec["significant_figures"]
    assert grade(item, AttemptRequest(response=shown(spec["answer"], sig))).correct, shown(spec["answer"], sig)
    assert not grade(item, AttemptRequest(response=shown(wrong, sig))).correct, shown(wrong, sig)


def test_every_new_numeric_item_has_a_named_misconception_and_three_figure_items_say_so():
    numeric = {qid for qid, q in BANK.items() if q["type"] == "numeric" and re.match(r"genetics-2[89]:", qid)}
    assert numeric == {f"genetics-{lesson}:{slug}" for lesson, group in MISCONCEPTIONS.items() for slug in group}
    for qid in numeric:
        spec = BANK[qid]["solution_spec"]
        if spec["significant_figures"] == 3:
            assert BANK[qid]["prompt"].endswith("to three significant figures."), qid
            assert not grade(BANK[qid], AttemptRequest(response=shown(spec["answer"], 3) + "0")).correct, qid
        else:
            assert BANK[qid]["prompt"].endswith("Enter the number only."), qid


@pytest.mark.parametrize("item_id", ["28:deletion-mapping", "28:inversion-suppression", "28:balanced-invisible",
                                     "29:suppressor-dominance", "29:loh-route"])
def test_single_choice_items_accept_only_the_key(item_id):
    item = BANK[f"genetics-{item_id}"]
    key = item["solution_spec"]["answer"]
    accepted = [index for index in range(len(item["options"])) if grade(item, AttemptRequest(response=str(index))).correct]
    assert accepted == [key]


@pytest.mark.parametrize("item_id,key", [("28:rearrangement-statements", [0, 1, 3]), ("28:translocation-statements", [0, 1, 2]),
                                         ("29:kinetics-statements", [0, 1, 3]), ("29:incidence-claims", [0, 1, 3])])
def test_multiple_select_items_give_partial_credit_for_correct_minus_incorrect(item_id, key):
    item = BANK[f"genetics-{item_id}"]
    assert item["solution_spec"]["answer"] == key and item["points"] == 2
    assert item["solution_spec"]["partial_credit"] == "correct-minus-incorrect-clamped-v1"
    options = range(len(item["options"]))
    wrong = next(index for index in options if index not in key)
    full = grade(item, AttemptRequest(response=key)).score
    assert full == pytest.approx(2.0)
    assert grade(item, AttemptRequest(response=[*key, wrong])).score < full
    assert grade(item, AttemptRequest(response=[wrong])).score == 0
    assert grade(item, AttemptRequest(response=list(options))).score < full
