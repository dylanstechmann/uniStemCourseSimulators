"""Cell Culture Practice 0.1.0 pilot: recomputed keys, sourced statements, simulator agreement and honest pilot scope.

Numeric keys are recomputed here from the dilution factor, mean count × 10⁴ × dilution factor, unstained/total and
Poisson 100/√N, and the lesson's worked examples are checked against the hemocytometer bench model's own
calculation. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import pytest

from courselab.bench.cell_count import HemocytometerCount
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cell-culture-practice"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
CASES = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
READING = (COURSE / "modules/04-counting-cells-and-viability.md").read_text(encoding="utf-8")
SYLLABUS = (COURSE / "syllabus.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
REGISTRY = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
PROTOCOL = json.loads((ROOT / "content/bench/protocols/hemocytometer-cell-count-viability.json").read_text(encoding="utf-8"))
SIM_LINK = "#/bench/hemocytometer-cell-count-viability"


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


def per_ml(mean_count, dilution, square_ml=1e-4):
    return mean_count / square_ml * dilution


# Recomputed key and a named misconception for every numeric item.
KEYS = {
    "dilution-factor": ((15 + 35) / 15, 35 / 15),  # dye/sample ratio
    "pre-dilution": (per_ml((33 + 38) / 2, (1000 / 100) * (20 / 10)) / 1e6,
                     per_ml((33 + 38) / 2, 20 / 10) / 1e6),  # forgetting the medium step
    "two-chamber-concentration": (per_ml((58 + 63) / 2, 2) / 1e6, per_ml(58 + 63, 2) / 1e6),  # not averaging
    "viability": (100 * (72 + 66) / (72 + 11 + 66 + 13), 100 * (11 + 13) / (72 + 66)),  # stained/unstained
    "poisson-uncertainty": (100 / math.sqrt(55 + 9 + 63 + 12), 100 / (55 + 9 + 63 + 12)),  # 100/N
    "squares-for-precision": ((100 / 5) ** 2 / 50, 100 / 5),  # √N mistaken for N
}


def shown(value, sig):
    if not sig:
        return f"{value:g}"
    return f"{value:.{max(0, sig - 1 - math.floor(math.log10(abs(value))))}f}"


def test_every_numeric_item_has_a_recomputed_key():
    assert {qid for qid, q in BANK.items() if q["type"] == "numeric"} == {f"cell-culture-practice-4:{k}" for k in KEYS}


@pytest.mark.parametrize("key", sorted(KEYS))
def test_numeric_keys_and_misconceptions(key):
    item = BANK[f"cell-culture-practice-4:{key}"]
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
    assert not grade(item, AttemptRequest(response="seven")).correct


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


def test_items_map_to_objectives_and_link_the_lesson():
    lesson = MANIFEST["modules"][0]["lessons"][0]
    assert set(lesson["question_ids"]) == set(BANK) and 10 <= len(BANK) <= 12
    assert {o for q in BANK.values() for o in q["objective_ids"]} == set(lesson["objectives"])
    assert all(q["feedback"]["hint"] and q["feedback"]["solution"] and q["feedback"]["lesson_ids"] == [lesson["id"]]
               for q in BANK.values())
    assert len(CARDS) == 4 and {c["lesson_id"] for c in CARDS} == {lesson["id"]}
    assert sum(q["points"] for q in BANK.values()) == MANIFEST["assessments"][0]["points"]


def test_worked_examples_agree_with_the_bench_model():
    model = HemocytometerCount(PROTOCOL)
    for counts, dilution, concentration, viability, uncertainty in (
        ({"A": {"viable": 41, "stained": 5}, "B": {"viable": 47, "stained": 7}}, 2, 8.8e5, 88.0, 10.0),
        ({"A": {"viable": 58, "stained": 7}, "B": {"viable": 63, "stained": 9}}, 2, 1.21e6, 100 * 121 / 137, 100 / math.sqrt(137)),
    ):
        expected = model.expected({"counts": counts, "dilution": dilution})
        assert expected["concentration"] == pytest.approx(concentration)
        assert expected["viability"] == pytest.approx(viability)
        assert expected["uncertainty"] == pytest.approx(uncertainty)
    assert PROTOCOL["parameters"][0]["value"] == 1 * 1 * 0.1 / 1000  # 1 mm × 1 mm × 0.1 mm in mL
    unstained, stained = 31 + 28 + 35 + 30 + 29 + 33 + 27 + 32, 4 + 6 + 3 + 5 + 5 + 4 + 6 + 3
    assert (unstained, stained) == (245, 36)
    assert round(per_ml(unstained / 8, (20 + 30) / 20) / 1e5, 2) == 7.66
    assert round(100 * unstained / (unstained + stained), 1) == 87.2
    assert round(100 / math.sqrt(unstained + stained), 2) == 5.97 and round(100 / math.sqrt(unstained), 2) == 6.39
    assert round(math.sqrt(31 + 74), 1) == 10.2 and (74 - 31) / math.sqrt(31 + 74) > 4
    stated(READING, "8.8 × 10⁵", "88.0%", "1.0 × 10⁶", "7.66 × 10⁵", "87.2%", "5.97%", "6.39%", "√105 ≈ 10.2",
           "N = (100/5)² = 400")


def test_reading_states_sources_conventions_and_limits():
    stated(READING, "1 mm × 1 mm × 0.1 mm = 0.1 mm³ = 0.1 µL = 10⁻⁴ mL", "Fuchs-Rosenthal chamber at 0.2 mm depth",
           "middle line as the dimension line", "deliberately do not describe filling or counting",
           "**At corners, exclusion wins.**", "Equivalent conventions exist", "100/√N %", "aggregates of varying size",
           "replicate agreement", "serum-free solution", "3 to 5 minutes", "pp. 466–468", "BSL-2 practices",
           "not a laboratory acceptance criterion", "nine checkpoints", "only lesson that exists")
    assert READING.count(SIM_LINK) >= 2
    for claim in ("grow", "phenotype", "mycoplasma", "health"):
        assert re.search(rf"does not show[^.]*{claim}", READING), claim


def test_honest_pilot_scope_and_policy():
    lessons = [lesson for module in MANIFEST["modules"] for lesson in module["lessons"]]
    assert [lesson["id"] for lesson in lessons] == ["cell-culture-practice-4"]
    assert (MANIFEST["version"], MANIFEST["maturity"], MANIFEST["review"]) == (
        "0.1.0", "partial", {"status": "unreviewed", "reviewed_version": None, "reviewers": []})
    assert MANIFEST["grading_policy"]["mode"] == "formative-only" and not MANIFEST["grading_policy"]["categories"]
    assert [a["mode"] for a in MANIFEST["assessments"]] == ["practice"]
    assert MANIFEST["prerequisites"]["recommended_course_ids"] == ["lab-measurement", "lab-biosafety", "cell-biology"]
    assert len(CASES) == 1 and all(c["points"] == 0 for c in CASES[0]["rubric"])
    stated(SYLLABUS, "Only lesson 4 of the eight outlined cell-culture topics", "not a cell-culture course", SIM_LINK)
    assert CROSSWALK.count("| Absent, deferred |") == 7 and CROSSWALK.count("| **Covered** |") == 1
    stated(CROSSWALK, "agent-run comparison", "ISSCR standards are reserved", "simulation choices")
    text = json.dumps(MANIFEST) + SYLLABUS + READING
    assert not re.search(r"\b(certif(ied|ication)|competent|qualified to|badge)\b", text.replace("certifying body", ""), re.I)


def test_sources_and_protocol_reference():
    module_sources = MANIFEST["modules"][0]["source_ids"]
    assert "isscr-stem-cell-guidelines" not in module_sources
    for sid in module_sources:
        assert "cell-culture-practice" in REGISTRY[sid]["mapped_courses"], sid
    assert REGISTRY["cdc-nih-bmbl-6"]["reuse_mode"] == "adapted"
    for sid in set(module_sources) - {"cdc-nih-bmbl-6"}:
        assert REGISTRY[sid]["reuse_mode"].startswith("link-only") and not REGISTRY[sid]["permissions"]["quotation"], sid
    assert "466–468" in PROTOCOL["sources"][0]["use"] and "471" not in PROTOCOL["sources"][0]["use"]
