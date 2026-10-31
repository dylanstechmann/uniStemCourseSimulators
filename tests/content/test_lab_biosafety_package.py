"""Laboratory Safety and Biosafety 0.1.0: recomputed keys, stated source facts, schedule, project route and grading.

Numeric keys are recomputed here (probability × consequence, Q = v × A, C₁V₁ = C₂V₂, N = N₀ × 10^(−t/D) with heating
lag) or checked against the paragraph of the federal text the item cites. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/lab-biosafety"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
CASES = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
READINGS = {lesson["id"]: (COURSE / lesson["reading"]).read_text(encoding="utf-8")
            for module in MANIFEST["modules"] for lesson in module["lessons"]}
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
REGISTRY = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


# Recomputed key and a named misconception for every numeric item.
KEYS = {
    "1:risk-score": (4 * 3, 4 + 3),  # adding the scores
    "1:residual-score": (2 * 3, 4 * 3),  # forgetting the control
    "1:aerosol-release": (5e8 * 2.0 * 1e-6, 5e8 * 1e-6),  # ignoring the volume
    "3:inflow-volume": (100 * 6.0 * 8.0 / 12, 100 * 6.0 * 8.0),  # inches left as feet
    "3:raised-sash": (400 / (6.0 * 12.0 / 12), 100.0),  # assuming velocity is unchanged
    "3:a1-exhaust": (0.30 * 600, 0.70 * 600),  # the recirculated share
    "3:uv-threshold": (40, 400),
    "4:bleach-volume": (2000 * 1000 / 60000, 2000 * 1000 / 6000),  # 6% read as 6,000 ppm
    "4:bleach-ppm": (75000 / 50, 7.5 / 50 * 1000),
    "4:sal-time": (12 * 1.8, 6 * 1.8),  # to one survivor only
    "4:survivors": (1e6 * 10 ** (-9.0 / 1.8), 1e6 * 10 ** (-1.8 / 9.0)),  # inverted exponent
    "4:lag": (22 + 12 * 1.5, 12 * 1.5),  # ignoring the lag
    "5:hbv-days": (10, 30),
    "5:medical-records": (8 + 30, 30),  # forgetting the employment period
    "5:training-records": (3, 30),
    "6:sds-ppe": (8, 2),
    "6:sds-spill": (6, 4),
    "6:un-category-b": (3373, 2814),  # the Category A number
    "6:pressure": (95, 9.5),
    "project:rehearsal-ranking": (12, 7),
    "project:rehearsal-inflow": (100 * 5.0 * 10.0 / 12, 100 * 5.0 * 10.0),
    "project:rehearsal-bleach": (500 * 5000 / 75000, 500 * 5000 / 7500),
    "project:rehearsal-autoclave": (20 + 12 * 1.5, 12 * 1.5),
}


def item_id(key):
    lesson, slug = key.split(":")
    return f"lab-biosafety-{lesson}:{slug}"


def shown(value, sig):
    if not sig:
        return f"{value:g}"
    return f"{value:.{max(0, sig - 1 - math.floor(math.log10(abs(value))))}f}"


def test_every_numeric_item_has_a_recomputed_key():
    assert {qid for qid, q in BANK.items() if q["type"] == "numeric"} == {item_id(key) for key in KEYS}


@pytest.mark.parametrize("key", sorted(KEYS))
def test_numeric_keys_and_misconceptions(key):
    item = BANK[item_id(key)]
    spec = item["solution_spec"]
    sig = spec["significant_figures"]
    value, wrong = KEYS[key]
    if sig:
        assert float(shown(value, sig)) == pytest.approx(spec["answer"], rel=1e-9)
        assert item["prompt"].endswith("to three significant figures.")
        assert not grade(item, AttemptRequest(response=shown(spec["answer"], sig) + "0")).correct
    else:
        assert value == pytest.approx(spec["answer"]) and item["prompt"].endswith("Enter the number only.")
    assert grade(item, AttemptRequest(response=shown(spec["answer"], sig))).correct
    assert not grade(item, AttemptRequest(response=shown(wrong, sig))).correct


def test_choice_items_accept_only_the_key():
    for qid, item in BANK.items():
        if item["type"] == "single_choice":
            accepted = [i for i in range(len(item["options"])) if grade(item, AttemptRequest(response=str(i))).correct]
            assert accepted == [item["solution_spec"]["answer"]], qid
        elif item["type"] == "multiple_select":
            key = item["solution_spec"]["answer"]
            wrong = next(i for i in range(len(item["options"])) if i not in key)
            assert grade(item, AttemptRequest(response=key)).score == pytest.approx(2.0)
            assert grade(item, AttemptRequest(response=[*key, wrong])).score < 2.0, qid


def test_readings_state_the_sourced_facts():
    stated(READINGS["lab-biosafety-1"], "six-step", "less than 20%", "correlate with, but do not equate to")
    stated(READINGS["lab-biosafety-2"], "immunocompetent adult humans", "self-closing, lockable doors", "in-line HEPA filters")
    stated(READINGS["lab-biosafety-3"], "75 linear feet per minute", "100 lfm", "1,200 cubic feet per minute", "0.5 inches of water",
           "40 µW/cm²", "never be used for cell culture materials", "Q = 100 × 2.67 = 267", "80 lfm")
    stated(READINGS["lab-biosafety-4"], "20 minutes at 121 °C", "less than one in a million", "500–6000 mg/L", "83.3 mL", "30.3 mL",
           "18 + 24 = 42 min")
    stated(READINGS["lab-biosafety-5"], "within 10 working days", "duration of employment plus 30 years", "training records for 3 years",
           "at least annually", "(d)(4)(iii)(A)", "BSL-2 practices, engineering controls and facilities")
    stated(READINGS["lab-biosafety-6"], "at least annually", "Chemical Hygiene Officer", "UN 2814", "UN 3373", "95 kPa", "−40 °C to +55 °C",
           "| 8 | Exposure controls/personal protection |")


def test_worked_example_arithmetic():
    assert round(100 * 5.0 * 10.0 / 12) == 417 and round(100 * 4.0 * 8.0 / 12) == 267
    assert round(267 / (4.0 * 10.0 / 12)) == 80
    assert round(1000 * 5000 / 60000, 1) == 83.3 and round(500 * 5000 / 82500, 1) == 30.3
    assert 18 + 12 * 2.0 == 42 and 15 + 12 * 2.0 == 39 and 20 + 12 * 1.5 == 38
    stated(READINGS["lab-biosafety-project-guide"], "417 cubic feet per minute", "33.3 mL", "38 min", "4 × 3 = 12", "2 × 3 = 6")


def test_schedule_project_and_policy():
    weeks = MANIFEST["duration"]["weeks"]
    scheduled = [lesson for week in weeks for lesson in week["lesson_ids"]]
    lessons = [lesson["id"] for module in MANIFEST["modules"] for lesson in module["lessons"]]
    assert len(weeks) == 6 and sorted(scheduled) == sorted(lessons) == sorted(set(lessons))
    assert MANIFEST["maturity"] == "partial" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert len([c for c in CASES if ":project-m" in c["id"]]) == 5
    assert all(c["points"] == 0 for case in CASES for c in case["rubric"])
    assert "#/bench/class-ii-bsc-session-with-spill" in READINGS["lab-biosafety-3"]


def test_sources_and_comparator():
    for sid in ("osha-29cfr1910-1030-bloodborne-pathogens", "osha-29cfr1910-1450-laboratory-standard",
                "osha-29cfr1910-1200-hazard-communication", "cdc-nih-bmbl-6"):
        assert REGISTRY[sid]["reuse_mode"] == "adapted" and "lab-biosafety" in REGISTRY[sid]["mapped_courses"]
    comparator = REGISTRY["absa-cbsp-examination-content"]
    assert comparator["reuse_mode"] == "link-only-comparator" and not comparator["permissions"]["quotation"]
    stated(CROSSWALK, "agent-run comparison", "Absent by design", "establishes no equivalence, eligibility, credit or endorsement")
