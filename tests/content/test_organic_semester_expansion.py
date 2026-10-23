"""Independent atom/graph/order and grader checks for deeper organic coursework."""

from __future__ import annotations

import itertools
import json
import re
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path

import pytest
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/organic-chemistry"
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
    if re.fullmatch(r"organic-chemistry-(?:1[7-9]|20):depth-\d+", qid)
}


def distance(start, end):
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, steps = queue.popleft()
        if node == end:
            return steps
        for neighbor in [node % 6 + 1, (node - 2) % 6 + 1]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    raise AssertionError("cycle must be connected")


def valid_order(order):
    masked = formed = False
    for operation in order:
        if operation == "P":
            if masked or formed:
                return False
            masked = True
        elif operation == "N":
            if not masked:
                return False
            formed = True
        elif operation == "D":
            if not masked or not formed:
                return False
            masked = False
    return formed and not masked


def atoms(formula):
    return Counter(
        {
            element: int(count or 1)
            for element, count in re.findall(r"([A-Z][a-z]?)(\d*)", formula)
        }
    )


def dbe(formula):
    return (2 * formula["C"] + 2 + formula["N"] - formula["H"] - formula["X"]) // 2


def calculations():
    start = atoms("C6H4") + atoms("CHO") + atoms("C2H3O")
    ethyl = start + atoms("C2H5") + atoms("H")
    methyl = start + atoms("CH3") + atoms("H")
    aryne = atoms("C6H5X")
    aryne.subtract(atoms("HX"))
    nitrogen_product = aryne + atoms("NH2") + atoms("H")
    permutations = list(itertools.permutations("PND"))
    valid = sum(map(valid_order, permutations))
    step_yields = list(map(Fraction, [".90", ".75", ".80"]))
    total = step_yields[0] * step_yields[1] * step_yields[2]
    first_centers = int(len(set(["aryl", "methyl", "ethyl", "hydroxyl"])) == 4)
    second_centers = int(len(set(["aryl", "methyl", "methyl", "hydroxyl"])) == 4)
    permitted = [node for node in [2, 6] if node not in {6}]
    return {
        (17, 1): {
            "neighbor": permitted[0],
            "first_distance": distance(1, 4),
            "other_distance": distance(2, 4),
        },
        (17, 2): {
            "aryne_h": aryne["H"],
            "product_h": nitrogen_product["H"],
            "aryne_dbe": dbe(aryne),
            "product_dbe": dbe(nitrogen_product),
        },
        (17, 3): {
            "fraction": float(Fraction(".7") * Fraction(".8")),
            "other": float(Fraction(".3") * Fraction(".8")),
        },
        (17, 4): {},
        (18, 1): {"orders": len(permutations), "valid": valid},
        (18, 2): {"yield": float(total), "amount": float(3 * total)},
        (18, 3): {
            "carbon": ethyl["C"],
            "hydrogen": ethyl["H"],
            "dbe": dbe(ethyl),
            "centers": first_centers,
        },
        (18, 4): {
            "longer": float(Fraction(".9") ** 4),
            "shorter": float(Fraction(".8") * Fraction(".75")),
        },
        (19, 1): {
            "first": float(2 * Fraction(".75") * Fraction(".7")),
            "other": float(2 * Fraction(".75") * Fraction(".3")),
            "remaining": float(2 * (1 - Fraction(".75"))),
        },
        (19, 2): {"ipso_distance": distance(1, 4), "adjacent_distance": distance(2, 4)},
        (20, 1): {
            "carbon": methyl["C"],
            "hydrogen": methyl["H"],
            "centers": second_centers,
            "dbe": dbe(methyl),
        },
        (20, 2): {"yield": float(total), "amount": float(3 * total), "valid": valid},
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_structural_counts_amounts_and_precision_recompute_and_grade(qid):
    number, item = map(
        int, re.fullmatch(r"organic-chemistry-(\d+):depth-(\d+)", qid).groups()
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
        elif spec["significant_figures"] is None:
            assert float(values[spec["id"]]).is_integer()
            response[spec["id"]] = str(int(values[spec["id"]]))
        else:
            assert values[spec["id"]] == pytest.approx(spec["answer"], rel=1e-12)
            response[spec["id"]] = format(values[spec["id"]], ".2e")
    result = grade(question, AttemptRequest(response=response))
    assert result.correct, result.feedback
    for fid, value in values.items():
        wrong = 1 if value == 0 else value * 1.2
        assert not grade(
            question, AttemptRequest(response={**response, fid: format(wrong, ".2e")})
        ).correct


def test_new_mechanism_and_route_pages_are_scheduled_and_ungraded():
    assert len(NEW) == 12
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [
        lid for week in MANIFEST["duration"]["weeks"] for lid in week["lesson_ids"]
    ]
    assert len(scheduled) == len(set(scheduled)) == 22
    assert len(MANIFEST["duration"]["weeks"]) == 12
    content = ContentRepository(ROOT / "content")
    for number in range(17, 21):
        lesson = content.lesson("organic-chemistry", f"organic-chemistry-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 19 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )


def test_original_carbon_maps_and_reaction_order_have_separate_checks():
    # The reading and assignment deliberately use opposite blocked ortho sites and different tags.
    assert distance(1, 3) == 2 and distance(6, 3) == 3
    assert distance(1, 4) == 3 and distance(2, 4) == 2
    assert [order for order in itertools.permutations("PND") if valid_order(order)] == [
        ("P", "N", "D")
    ]
    assert not valid_order(("N", "P", "D"))
    assert not valid_order(("P", "D", "N"))


def test_protecting_group_atom_ledger_closes_without_assigning_oxygen_identity():
    start = atoms("C9H8O2")
    mask = atoms("C2H6O2")
    mask.subtract(atoms("H2O"))
    protected = start + mask
    methyl_addition = protected + atoms("CH3") + atoms("H")
    final = methyl_addition.copy()
    final.subtract(mask)
    assert protected == atoms("C11H12O3")
    assert final == atoms("C10H12O2")
    assert dbe(start) == 6 and dbe(final) == 5
    text = (DIRECTORY / "assignments/coursework-02-route-audit.md").read_text()
    assert "two identical methyl" in text and "isotope-resolved oxygen identity" in text
