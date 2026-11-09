"""Statics & Materials 0.8.0 frames and machines: keys re-derived from exact member equilibrium.

The checks below recompute the worked frame's link force and pin reactions and the toggle clamp's
mechanical advantage, then confirm the reading states those numbers and that each authored answer
key grades only itself. Same-AI checks, not engineering review.
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
FRAME = "statics-materials-22"
READING = (COURSE / LESSONS[FRAME]["reading"]).read_text(encoding="utf-8")


def response(value):
    return f"{float(value):.3g}" if abs(value) >= 100 else f"{float(value):#.3g}"


def test_frame_equilibrium_recomputed():
    # Beam AB from A(0,0) to B(3,0); two-force link B(3,0)->C(6,4) (3-4-5); 8 kN down at x=1.5 m.
    # Whole-structure moment about A: -12 - (12/5)F = 0  =>  F = -5 kN (compression).
    link = Fr(-5)
    assert -Fr(12) - Fr(12, 5) * link == 0
    # Dismember beam AB: link pushes on B with (3, 4) kN; A_x + 3 = 0, A_y + 4 - 8 = 0.
    ax, ay = Fr(-3), Fr(4)
    assert ax + 3 == 0 and ay + 4 - 8 == 0
    assert (link, ax, ay) == (Fr(-5), Fr(-3), Fr(4))


def test_toggle_advantage_recomputed():
    # Links AC and BC of length 5: A(0,0), C(3,4), B(6,0). Symmetry forces T1 = T2 = T.
    # Vertical equilibrium at C gives F_c = (4/5)(T+T) = (8/5)T; horizontal at slider B gives (3/5)T.
    cosine_x, cosine_y = Fr(3, 5), Fr(4, 5)
    mechanical_advantage = (2 * cosine_y) / cosine_x
    assert mechanical_advantage == Fr(8, 3)
    # 30 N input -> T = 30 * 5/3 = 50 N -> F_c = (8/5) * 50 = 80 N.
    tension = Fr(30) / cosine_x
    assert tension == 50
    assert Fr(8, 5) * tension == 80


def test_worked_values_match_reading():
    for phrase in ("F = −5 kN", "A_x = −3 kN", "A_y = +4 kN", "8/3", "30 N", "80 N"):
        assert phrase in READING, phrase


def test_numeric_keys_grade_correctly():
    item = BANK[f"{FRAME}:frame-dismember"]
    specs = {f["id"]: f for f in item["solution_spec"]["field_specs"]}
    expected = {"link_force": Fr(-5), "pin_ax": Fr(-3), "pin_ay": Fr(4)}
    assert set(specs) == set(expected)
    correct = {}
    for fid, value in expected.items():
        spec = specs[fid]
        assert abs(spec["answer"] - float(value)) <= spec["tolerance"], (fid, spec["answer"], float(value))
        assert spec["significant_figures"] == 3
        correct[fid] = response(value)
    assert grade(item, AttemptRequest(response=correct)).correct

    ma = BANK[f"{FRAME}:toggle-advantage"]
    assert abs(ma["solution_spec"]["answer"] - float(Fr(8, 3))) <= ma["solution_spec"]["tolerance"]
    assert grade(ma, AttemptRequest(response="2.67")).correct

    output = BANK[f"{FRAME}:toggle-output"]
    assert abs(output["solution_spec"]["answer"] - 80.0) <= output["solution_spec"]["tolerance"]
    assert grade(output, AttemptRequest(response="80.0")).correct
    assert not grade(output, AttemptRequest(response="80")).correct  # two significant figures


def test_choice_items_accept_only_their_key():
    for qid in LESSONS[FRAME]["question_ids"]:
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
    assert weeks[FRAME] == 1
    assert MANIFEST["version"] == "0.8.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    lesson = LESSONS[FRAME]
    assert len(lesson["question_ids"]) == 8
    assert {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]} == set(lesson["objectives"])
    assert len([c for c in CARDS if c["lesson_id"] == FRAME]) == 4
    assert "link-only scope comparator" in READING and "not taught here" in READING
    assert any("Friction (2.001 lecture 4)" in item for item in MANIFEST["intentionally_omitted"])


@pytest.mark.parametrize("fid,expected", [("link_force", Fr(-5)), ("pin_ax", Fr(-3)), ("pin_ay", Fr(4))])
def test_frame_field_keys_match_equilibrium(fid, expected):
    spec = {f["id"]: f for f in BANK[f"{FRAME}:frame-dismember"]["solution_spec"]["field_specs"]}[fid]
    assert abs(spec["answer"] - float(expected)) <= spec["tolerance"]