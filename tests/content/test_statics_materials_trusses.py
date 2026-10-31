"""Statics & Materials 0.7.0 trusses: every key re-solved from full joint equilibrium, two displacement methods compared.

The solver below writes ΣFx = ΣFy = 0 at every joint of each practice truss with exact fractions and solves for all
member forces and reactions; a non-unique or inconsistent system fails. Same-AI checks, not engineering review.
"""

from __future__ import annotations

import json
from fractions import Fraction as Fr
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statics-materials"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
TRUSS, DEFORM = "statics-materials-20", "statics-materials-21"
READING = {lid: (COURSE / LESSONS[lid]["reading"]).read_text(encoding="utf-8") for lid in (TRUSS, DEFORM)}
PRATT_MEMBERS = [("L0", "L1"), ("L1", "L2"), ("L2", "L3"), ("L3", "L4"), ("U1", "U2"), ("U2", "U3"), ("L0", "U1"),
                 ("U3", "L4"), ("U1", "L1"), ("U2", "L2"), ("U3", "L3"), ("U1", "L2"), ("U3", "L2")]
PIN_ROLLER = lambda left, right: [(left, "x"), (left, "y"), (right, "y")]  # noqa: E731


def length(dx, dy):
    square = dx * dx + dy * dy
    root = Fr(round(float(square) ** 0.5 * 10**6), 10**6)
    assert root * root == square, "practice geometry uses exact lengths"
    return root


def solve(joints, members, loads, supports):
    """Joint equilibrium for all unknowns (tension-positive members, reactions along +x/+y)."""
    joints = {name: (Fr(x), Fr(y)) for name, (x, y) in joints.items()}
    unknowns = [("m", a, b) for a, b in members] + [("r", j, d) for j, d in supports]
    rows = []
    for name, (x, y) in joints.items():
        for axis in (0, 1):
            row = []
            for kind, a, b in unknowns:
                if kind == "m" and name in (a, b):
                    other = joints[b if name == a else a]
                    dx, dy = other[0] - x, other[1] - y
                    row.append((dx, dy)[axis] / length(dx, dy))
                elif kind == "r" and a == name:
                    row.append(Fr(1) if b == "xy"[axis] else Fr(0))
                else:
                    row.append(Fr(0))
            row.append(-Fr(loads.get(name, (0, 0))[axis]))
            rows.append(row)
    n, pivots, r = len(unknowns), [], 0
    for c in range(n):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        rows[r] = [v / rows[r][c] for v in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                factor = rows[i][c]
                rows[i] = [a - factor * b for a, b in zip(rows[i], rows[r])]
        pivots.append(c)
        r += 1
    assert r == n, "statically determinate and stable"
    assert all(all(v == 0 for v in row) for row in rows[r:]), "consistent"
    return {"".join(unknowns[c][1:]): rows[i][-1] for i, c in enumerate(pivots)}


def pratt(panel, height, load):
    joints = {f"L{i}": (panel * i, 0) for i in range(5)} | {f"U{i}": (panel * i, height) for i in range(1, 4)}
    return solve(joints, PRATT_MEMBERS, {f"L{i}": (0, -load) for i in (1, 2, 3)}, PIN_ROLLER("L0", "L4"))


TRIANGLE_6 = solve({"A": (0, 0), "B": (6, 0), "C": (3, 4)}, [("A", "B"), ("A", "C"), ("B", "C")], {"C": (0, -24)}, PIN_ROLLER("A", "B"))
TRIANGLE_8 = solve({"A": (0, 0), "B": (8, 0), "C": (4, 3)}, [("A", "B"), ("A", "C"), ("B", "C")], {"C": (0, -12)}, PIN_ROLLER("A", "B"))
PRATT_PRACTICE = pratt(Fr(2), Fr(3, 2), 6)
PRATT_WORKED = pratt(3, 4, 10)


def unit_load(real, members, lengths, load, rigidity):
    return sum(real[m] * 1000 * (real[m] / load) * lengths[m] for m in members) / rigidity


def three_bar(load, centre, side, cosine, rigidity_centre, rigidity_side):
    stiffness = Fr(rigidity_centre) / centre + 2 * Fr(rigidity_side) * cosine * cosine / side
    drop = Fr(load) / stiffness
    return Fr(rigidity_centre) * drop / centre, Fr(rigidity_side) * cosine * drop / side, drop


def fields(qid):
    return {f["id"]: f for f in BANK[qid]["solution_spec"]["field_specs"]}


def response(value):
    return f"{float(value):.3g}" if abs(value) >= 100 else f"{float(value):#.3g}"


EXPECTED_FIELDS = {
    f"{TRUSS}:triangle-joints": {"reaction_a": TRIANGLE_6["Ay"], "force_ac": TRIANGLE_6["AC"], "force_ab": TRIANGLE_6["AB"]},
    f"{TRUSS}:pratt-section": {"top": PRATT_PRACTICE["U1U2"], "bottom": PRATT_PRACTICE["L1L2"], "diagonal": PRATT_PRACTICE["U1L2"]},
    f"{DEFORM}:bracket-deflection": {
        "roller": TRIANGLE_6["AB"] * 1000 * 6 / Fr(5 * 10**7) * 1000,
        "ac_change": TRIANGLE_6["AC"] * 1000 * 5 / Fr(5 * 10**7) * 1000,
        "apex": unit_load(TRIANGLE_6, ["AB", "AC", "BC"], {"AB": 6, "AC": 5, "BC": 5}, 24, Fr(5 * 10**7)) * 1000,
    },
    f"{DEFORM}:three-bar": dict(zip(("centre", "side", "drop"),
                                    (v / s for v, s in zip(three_bar(20_000, 3, 5, Fr(3, 5), 5 * 10**7, 5 * 10**7), (1000, 1000, Fr(1, 1000)))))),
}


@pytest.mark.parametrize("qid", sorted(EXPECTED_FIELDS))
def test_data_interpretation_keys_match_full_joint_equilibrium(qid):
    specs = fields(qid)
    assert set(specs) == set(EXPECTED_FIELDS[qid])
    for fid, expected in EXPECTED_FIELDS[qid].items():
        spec = specs[fid]
        assert abs(spec["answer"] - float(expected)) <= spec["tolerance"], (qid, fid, spec["answer"], float(expected))
        assert spec["significant_figures"] == 3 and spec["tolerance"] <= abs(spec["answer"]) * 0.0025 + 1e-12
    correct = {fid: response(v) for fid, v in EXPECTED_FIELDS[qid].items()}
    assert grade(BANK[qid], AttemptRequest(response=correct)).correct
    flipped = {**correct, next(iter(correct)): response(-float(next(iter(EXPECTED_FIELDS[qid].values()))) * 1.5)}
    assert not grade(BANK[qid], AttemptRequest(response=flipped)).correct


def test_compression_sign_errors_are_rejected():
    item = BANK[f"{TRUSS}:end-post"]
    assert grade(item, AttemptRequest(response="-15.0")).correct
    assert not grade(item, AttemptRequest(response="15.0")).correct  # magnitude without compression sign
    assert not grade(item, AttemptRequest(response="-15")).correct  # two significant figures
    assert PRATT_PRACTICE["L0U1"] == -15


def test_worked_examples_and_reading_statements():
    worked = {k: float(v) for k, v in PRATT_WORKED.items()}
    assert (worked["L0U1"], worked["L0L1"], worked["U1U2"], worked["U1L2"], worked["U1L1"], worked["U2L2"]) == (
        -18.75, 11.25, -15.0, 6.25, 10.0, 0.0)
    assert len(PRATT_MEMBERS) + 3 - 2 * 8 == 0
    assert (TRIANGLE_8["AB"], TRIANGLE_8["AC"]) == (8, -10)
    rigidity = Fr(8 * 10**7)
    by_unit_load = unit_load(TRIANGLE_8, ["AB", "AC", "BC"], {"AB": 8, "AC": 5, "BC": 5}, 12, rigidity)
    roller = Fr(8000 * 8) / rigidity
    shortening = Fr(-10_000 * 5) / rigidity
    by_compatibility = (shortening - (roller / 2) * Fr(4, 5)) / Fr(3, 5)
    assert by_unit_load * 1000 == Fr(1575, 1000) and -by_compatibility == by_unit_load
    centre, side, drop = three_bar(30_000, 4, 5, Fr(4, 5), rigidity, rigidity)
    assert centre + 2 * Fr(4, 5) * side == 30_000
    doubled = three_bar(30_000, 4, 5, Fr(4, 5), 2 * rigidity, rigidity)
    assert centre < doubled[0] < 2 * centre and doubled[1] < side and doubled[2] < drop
    stated = {
        TRUSS: ["m + r = 16 = 2j", "F_L0U1 = −18.75 kN", "F_L0L1 = +11.25 kN", "F_U1L2 = +6.25 kN", "F_U1U2 = −15 kN",
                "carries **zero**", "−90 + 30 − 4F_U1U2 = 0", "−15 + 11.25 + (3/5)(6.25) = 0"],
        DEFORM: ["+0.800 mm", "−0.625 mm", "v_C = −1.575 mm", "1.575 mm, downward", "v = 0.741 mm",
                 f"F_c = {float(centre) / 1000:.1f} kN", f"F_s = {float(side) / 1000:.2f} kN",
                 f"F_c rises to {float(doubled[0]) / 1000:.1f} kN", f"F_s falls to {float(doubled[1]) / 1000:.2f} kN",
                 f"v drops to {float(doubled[2]) * 1000:.3f} mm"],
    }
    for lesson, phrases in stated.items():
        missing = [p for p in phrases if p not in READING[lesson]]
        assert not missing, (lesson, missing)


def test_choice_items_accept_only_their_key():
    for qid in LESSONS[TRUSS]["question_ids"] + LESSONS[DEFORM]["question_ids"]:
        item = BANK[qid]
        if item["type"] == "single_choice":
            accepted = [i for i in range(len(item["options"])) if grade(item, AttemptRequest(response=str(i))).correct]
            assert accepted == [item["solution_spec"]["answer"]], qid
        elif item["type"] == "multiple_select":
            key = item["solution_spec"]["answer"]
            wrong = next(i for i in range(len(item["options"])) if i not in key)
            assert grade(item, AttemptRequest(response=key)).correct
            assert not grade(item, AttemptRequest(response=[*key, wrong])).correct, qid


def test_schedule_scope_and_status():
    weeks = {lid: w["week"] for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]}
    assert (weeks[TRUSS], weeks["statics-materials-1"], weeks[DEFORM], weeks["statics-materials-2"]) == (1, 1, 3, 3)
    assert MANIFEST["version"] == "0.7.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    for lid in (TRUSS, DEFORM):
        lesson = LESSONS[lid]
        assert {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]} == set(lesson["objectives"])
        assert len([c for c in CARDS if c["lesson_id"] == lid]) == 4
        assert "link-only scope comparator" in READING[lid] and "not taught here" in READING[lid]
    assert "Planar Trusses" in READING[TRUSS] and "lecture 9" in READING[DEFORM] and "lecture 10" in READING[DEFORM]
    assert any("Friction (2.001 lecture 4)" in item for item in MANIFEST["intentionally_omitted"])
