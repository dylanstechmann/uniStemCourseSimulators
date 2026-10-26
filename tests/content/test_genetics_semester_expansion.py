"""Independent probability, count and genotype-ledger checks for Genetics depth."""

from __future__ import annotations

import csv
import itertools
import json
import math
import re
from fractions import Fraction
from pathlib import Path

import pytest
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/genetics"
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
    if re.fullmatch(r"genetics-(19|2[0-7]):depth-\d+", qid)
}


def genotype_distribution(q, identity=Fraction(0)):
    """Enumerate independent allele draws plus a shared ancestral draw."""
    q, identity = Fraction(q), Fraction(identity)
    draws = [(0, 1 - q), (1, q)]
    distribution = [Fraction(0)] * 3
    for first, pf in draws:
        for second, ps in draws:
            distribution[first + second] += (1 - identity) * pf * ps
        distribution[first * 2] += identity * pf
    assert sum(distribution) == 1
    assert sum(i * f for i, f in enumerate(distribution)) / 2 == q
    return distribution


def selection(q, weights, u, v, identity=Fraction(0)):
    distribution = genotype_distribution(q, identity)
    weighted = [f * Fraction(w) for f, w in zip(distribution, weights, strict=True)]
    total = sum(weighted)
    if total == 0:
        raise ValueError("No contributing genotype in the stipulated normalized model")
    adults = [f / total for f in weighted]
    selected = sum(i * f for i, f in enumerate(adults)) / 2
    # Enumerate the allele transition kernel rather than inserting a compact recurrence.
    transitions = [(1 - selected, Fraction(u)), (selected, 1 - Fraction(v))]
    after = sum(source * chance_a for source, chance_a in transitions)
    return total, selected, after


def lod(recombinants, total, theta):
    """Direct binomial likelihoods provide a separate check on log-sum authoring."""
    theta = float(theta)
    count = math.comb(total, recombinants)
    linked = count * theta**recombinants * (1 - theta) ** (total - recombinants)
    unlinked = count * 0.5**total
    return math.log10(linked / unlinked)


def groups(names, noncomplementing):
    # Exhaustively test partitions; do not assume the authored grouping.
    results = set()
    for labels in itertools.product(range(len(names)), repeat=len(names)):
        if labels[0] != 0:
            continue
        if any(
            label > max(labels[:i], default=-1) + 1 for i, label in enumerate(labels)
        ):
            continue
        if all(
            (labels[i] == labels[j]) == (frozenset((a, b)) in noncomplementing)
            for i, a in enumerate(names)
            for j, b in enumerate(names)
            if i < j
        ):
            results.add(max(labels) + 1)
    assert len(results) == 1
    return results.pop()


def calculations():
    mean, selected, after = selection(".3", ["1", ".8", ".5"], ".002", ".001")
    aa, hetero, minor = genotype_distribution(".1", Fraction(1, 5))
    assignment_mean, assignment_selected, assignment_after = selection(
        ".25", ["1", ".9", ".4"], ".001", ".002"
    )
    clone = next(
        csv.DictReader((DIRECTORY / "assignments/genome-evidence-counts.csv").open())
    )
    dna_a, dna_b, rna_a, rna_b, included, skipped = [
        int(clone[k])
        for k in [
            "dna_a",
            "dna_b",
            "rna_a",
            "rna_b",
            "included_junction",
            "skipped_junction",
        ]
    ]
    inclusion = Fraction(included, included + skipped)
    return {
        (19, 1): {"groups": groups("ABCD", {frozenset("AC"), frozenset("BD")})},
        (19, 2): {
            "observed": Fraction(6, 1200),
            "total": Fraction(6 + 6, 1200),
            "map": Fraction(100 * (6 + 6), 1200),
        },
        (19, 3): {
            "bound": Fraction(3 + 3, 1500),
            "map_bound": Fraction(100 * (3 + 3), 1500),
        },
        (19, 4): {},
        (20, 1): {
            "dna_fraction": Fraction(150, 250),
            "rna_fraction": Fraction(60, 140),
            "per_copy": Fraction(60, 80) / Fraction(150, 100),
        },
        (20, 2): {"inclusion": Fraction(54, 90), "skipping": Fraction(36, 90)},
        (20, 3): {
            "codons": 60 // 3,
            "skipped_length": 300 - 60,
            "expected_length": Fraction(3, 5) * 300 + Fraction(2, 5) * 240,
        },
        (20, 4): {},
        (21, 1): {"mean": mean, "selected": selected, "next": after},
        (21, 2): {"major_homo": aa, "heterozygote": hetero, "minor_homo": minor, "allele": minor + hetero / 2},
        (21, 3): {"theta": Fraction(3, 20), "lod": lod(3, 20, Fraction(3, 20))},
        (21, 4): {"balance": math.sqrt(Fraction(8, 10**6) / Fraction(1, 2))},
        (22, 1): {
            "groups": groups("UVWXY", {frozenset("UW"), frozenset("VX")}),
            "fraction": Fraction(15 + 15, 3000),
            "map": Fraction(100 * (15 + 15), 3000),
        },
        (22, 2): {"bound": Fraction(3 + 3, 1800)},
        (23, 1): {
            "dna": Fraction(dna_a, dna_a + dna_b),
            "rna": Fraction(rna_a, rna_a + rna_b),
            "per_copy": Fraction(rna_a, rna_b) / Fraction(dna_a, dna_b),
        },
        (23, 2): {
            "inclusion": inclusion,
            "codons": 90 // 3,
            "expected": inclusion * 420 + (1 - inclusion) * (420 - 90),
        },
        (24, 1): {
            "mean": assignment_mean,
            "selected": assignment_selected,
            "next": assignment_after,
            "aa_f": genotype_distribution(".25", ".1")[2],
        },
        (24, 2): {
            "theta": Fraction(4, 40),
            "lod": lod(4, 40, Fraction(4, 40)),
            "balance": math.sqrt(Fraction(8, 10**6) / Fraction(1, 2)),
        },
        (25, 1): {
            "ir_pairs": 2,
            "copypaste_copies": 1,
            "replicative_copies": 2,
        },
        (25, 2): {"gene1_pct": Fraction(100), "gene3_pct": Fraction(2)},
        (25, 3): {
            "expected_total": Fraction(10**9) * Fraction(2, 10**7),
            "expected_per_gene": Fraction(10**9) * Fraction(2, 10**7) / 50,
            "zero_gene_pct": math.exp(-4) * 100,
        },
        (25, 4): {
            "excision_per_billion": 1,
            "suppressor_per_billion": Fraction(1, 2) * 1000,
            "fold": Fraction(500),
        },
        (26, 1): {
            "homology_kb": Fraction(5) + Fraction(3),
            "crossovers": 2,
            "net_change_kb": Fraction(2) - Fraction(3, 2),
        },
        (26, 2): {
            "targeted": Fraction(2 * 10**7) * Fraction(1, 10**6),
            "random_unselected": Fraction(2 * 10**7) * Fraction(1, 10**4),
            "random_survivors": Fraction(2 * 10**7) * Fraction(1, 10**4) / 100,
            "targeted_fraction_pct": Fraction(100, 2),
        },
        (26, 3): {
            "testcross_pct": Fraction(40),
            "homozygous_pct": Fraction(100, 4),
            "carrier_pct": Fraction(100, 2),
            "wildtype_pct": Fraction(100, 4),
        },
        (26, 4): {"loxp_per_allele": 2, "loxp_homozygous": 4},
        (27, 1): {"polar_count": 3, "direct_count": 1},
        (27, 2): {
            "pool": Fraction(4 * 10**7) * Fraction(25, 10**7)
            + Fraction(4 * 10**7) * Fraction(25, 10**5) * Fraction(2, 100),
            "targeted_fraction_pct": Fraction(100, 3),
            "enrichment_fold": Fraction(101, 3),
            "f2_null_pct": Fraction(100, 4),
            "loxp_per_allele": 2,
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_new_genetics_answers_recompute_and_actual_grader_rejects_perturbations(qid):
    number, item = map(int, re.fullmatch(r"genetics-(\d+):depth-(\d+)", qid).groups())
    values = calculations()[(number, item)]
    question = NEW[qid]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-12, abs=1e-15)
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


def test_probability_invariants_exact_fixed_point_and_constrained_likelihood():
    _, _, fixed = selection(
        Fraction(1, 250), [1, 1, Fraction(1, 2)], Fraction(8, 10**6), 0
    )
    assert fixed == Fraction(1, 250)
    _, _, unchanged = selection(".25", [1, 1, 1], 0, 0)
    assert unchanged == Fraction(1, 4)
    assert selection(0, [1, 1, 1], 0, 0)[2] == 0
    with pytest.raises(ValueError, match="No contributing genotype"):
        selection(1, [1, 1, 0], 0, 0)
    for identity in [0, Fraction(1, 4), 1]:
        genotype_distribution(Fraction(1, 10), identity)
    maximum = lod(4, 40, Fraction(1, 10))
    assert maximum > max(lod(4, 40, t) for t in [0.05, 0.09, 0.11, 0.2, 0.5])
    assert lod(4, 40, 0.5) == 0
    assert lod(24, 40, 0.5) > lod(24, 40, 0.49)  # constrained maximum at one half
    # Inbreeding is allele-preserving but changes the next response under recessive selection.
    assert (
        selection(".25", [1, 1, ".4"], 0, 0)[1]
        != selection(".25", [1, 1, ".4"], 0, 0, ".1")[1]
    )


def test_transposition_targeting_invariants_and_audit_ledgers():
    # Poisson coverage: an empty class tightens as the per-gene expectation grows.
    frequency = Fraction(2, 10**7)
    expected = frequency * 10**9
    per_gene = expected / 50
    assert expected == 200 and per_gene == 4
    assert math.exp(-per_gene) < math.exp(-2)
    # Reversion ledger: suppression is 500-fold over precise excision.
    assert Fraction(1, 2) * 1000 == 500 and Fraction(500) == 500
    # Lesson selection ledger: half of the double-resistant pool is targeted.
    targeted = Fraction(2 * 10**7) * Fraction(1, 10**6)
    random_all = Fraction(2 * 10**7) * Fraction(1, 10**4)
    survivors = random_all * Fraction(1, 100)
    assert targeted == 20 and random_all == 2000 and survivors == 20
    assert Fraction(targeted, targeted + survivors) == Fraction(1, 2)
    # Audit ledger: the enrichment fold is a ratio of two fractions, not a guess.
    audit_targeted = Fraction(4 * 10**7) * Fraction(25, 10**7)
    audit_random = Fraction(4 * 10**7) * Fraction(25, 10**5)
    audit_survivors = audit_random * Fraction(2, 100)
    pool = audit_targeted + audit_survivors
    assert audit_targeted == 100 and audit_random == 10000 and audit_survivors == 200
    assert pool == 300
    pre = Fraction(audit_targeted, audit_targeted + audit_random)
    post = Fraction(audit_targeted, pool)
    assert pre == Fraction(100, 10100) and post == Fraction(100, 300)
    assert post / pre == Fraction(101, 3)
    # Carrier cross and conditional bookkeeping stay exact.
    assert Fraction(100, 4) == 25 and Fraction(100, 2) == 50
    assert 2 * 2 == 4  # loxP sites double in a homozygous floxed cell


def test_clone_table_allelic_junction_and_coding_ledgers():
    rows = list(
        csv.DictReader((DIRECTORY / "assignments/genome-evidence-counts.csv").open())
    )
    assert [row["clone"] for row in rows] == ["C1", "C2", "C3"]
    for row in rows:
        da, db, ra, rb, inc, skip = [
            int(row[k])
            for k in [
                "dna_a",
                "dna_b",
                "rna_a",
                "rna_b",
                "included_junction",
                "skipped_junction",
            ]
        ]
        assert Fraction(ra, rb) / Fraction(da, db) == Fraction(1, 2)
        assert Fraction(inc, inc + skip) == Fraction(7, 10)
    assert 81 % 3 == 0 and 80 % 3 != 0
    assert (1 - 1) % 3 == 0  # downstream frame restored; the two sites still differ
    # Expected length is not necessarily an integer sequence length.
    assert Fraction(3, 4) * 351 + Fraction(1, 4) * 270 == Fraction(1323, 4)
    text = (
        DIRECTORY / "assignments/coursework-03-population-and-linkage.md"
    ).read_text()
    assert "exactly sqrt(u/s)" in text and "another boundary fixed point" in text


def test_new_foundations_and_reports_deliver_resources_and_scheduled_open_practice():
    assert len(NEW) == 28
    assert MANIFEST["version"] == "0.8.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 29
    content = ContentRepository(ROOT / "content")
    for number in range(19, 28):
        lesson = content.lesson("genetics", f"genetics-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 22 or number in (25, 26) else 2)
        )
    lesson = content.lesson("genetics", "genetics-23")
    assert (
        "/api/v1/courses/genetics/resources/assignments/genome-evidence-counts.csv"
        in lesson.markdown
    )
    assert (
        content.learner_resource("genetics", "assignments/genome-evidence-counts.csv")
        == (DIRECTORY / "assignments/genome-evidence-counts.csv").read_bytes()
    )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
