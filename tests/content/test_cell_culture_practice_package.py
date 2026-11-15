"""Cell Culture Practice 0.2.0: recomputed keys, sourced statements, simulator agreement and honest partial scope.

Lesson 1 keys are exact source-based integers; lesson 4 numeric keys are recomputed from the dilution factor,
mean count × 10⁴ × dilution factor, unstained/total and Poisson 100/√N. The lesson 4 worked examples are checked
against the hemocytometer bench model's own calculation, and lesson 1's protocol parameters are checked against
the reading. Same-AI checks, not human review.
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
ASEPTIC_READING = (COURSE / "modules/01-aseptic-technique.md").read_text(encoding="utf-8")
COUNTING_READING = (COURSE / "modules/04-counting-cells-and-viability.md").read_text(encoding="utf-8")
SYLLABUS = (COURSE / "syllabus.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
REGISTRY = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
COUNT_PROTOCOL = json.loads((ROOT / "content/bench/protocols/hemocytometer-cell-count-viability.json").read_text(encoding="utf-8"))
ASEPTIC_PROTOCOL = json.loads((ROOT / "content/bench/protocols/aseptic-medium-change-with-hidden-contamination.json").read_text(encoding="utf-8"))
COUNT_SIM_LINK = "#/bench/hemocytometer-cell-count-viability"
ASEPTIC_SIM_LINK = "#/bench/aseptic-medium-change-with-hidden-contamination"
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
ASSESSMENTS = {assessment["id"]: assessment for assessment in MANIFEST["assessments"]}
ASEPTIC_BANK = {qid: q for qid, q in BANK.items() if qid.startswith("cell-culture-practice-1:")}
COUNT_BANK = {qid: q for qid, q in BANK.items() if qid.startswith("cell-culture-practice-4:")}


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


def per_ml(mean_count, dilution, square_ml=1e-4):
    return mean_count / square_ml * dilution


COUNT_KEYS = {
    "cell-culture-practice-4:dilution-factor": ((15 + 35) / 15, 35 / 15),
    "cell-culture-practice-4:pre-dilution": (per_ml((33 + 38) / 2, (1000 / 100) * (20 / 10)) / 1e6,
                                             per_ml((33 + 38) / 2, 20 / 10) / 1e6),
    "cell-culture-practice-4:two-chamber-concentration": (per_ml((58 + 63) / 2, 2) / 1e6, per_ml(58 + 63, 2) / 1e6),
    "cell-culture-practice-4:viability": (100 * (72 + 66) / (72 + 11 + 66 + 13), 100 * (11 + 13) / (72 + 66)),
    "cell-culture-practice-4:poisson-uncertainty": (100 / math.sqrt(55 + 9 + 63 + 12), 100 / (55 + 9 + 63 + 12)),
    "cell-culture-practice-4:squares-for-precision": ((100 / 5) ** 2 / 50, 100 / 5),
}
ASEPTIC_KEYS = {
    "cell-culture-practice-1:sterility-total-days": (14, 7),
    "cell-culture-practice-1:dual-temperature-days": (7, 14),
    "cell-culture-practice-1:cell-lines-at-once": (1, 2),
}
NUMERIC_KEYS = COUNT_KEYS | ASEPTIC_KEYS


def shown(value, sig):
    if not sig:
        return f"{value:g}"
    return f"{value:.{max(0, sig - 1 - math.floor(math.log10(abs(value))))}f}"


def test_every_numeric_item_has_a_recomputed_key():
    assert {qid for qid, q in BANK.items() if q["type"] == "numeric"} == set(NUMERIC_KEYS)


@pytest.mark.parametrize("qid", sorted(NUMERIC_KEYS))
def test_numeric_keys_and_misconceptions(qid):
    item = BANK[qid]
    spec = item["solution_spec"]
    sig = spec["significant_figures"]
    value, wrong = NUMERIC_KEYS[qid]
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


@pytest.mark.parametrize("lesson_id,bank", [
    ("cell-culture-practice-1", ASEPTIC_BANK),
    ("cell-culture-practice-4", COUNT_BANK),
])
def test_items_map_to_objectives_and_link_the_lesson(lesson_id, bank):
    lesson = LESSONS[lesson_id]
    assert set(lesson["question_ids"]) == set(bank) and len(bank) == 12
    assert {o for q in bank.values() for o in q["objective_ids"]} == set(lesson["objectives"])
    assert all(q["feedback"]["hint"] and q["feedback"]["solution"] and q["feedback"]["lesson_ids"] == [lesson_id]
               for q in bank.values())
    cards = [card for card in CARDS if card["lesson_id"] == lesson_id]
    assert len(cards) == 4 and {card["id"] for card in cards} == set(lesson["card_ids"])
    assert sum(q["points"] for q in bank.values()) == ASSESSMENTS[f"{lesson_id}-practice"]["points"]
    assert set(ASSESSMENTS[f"{lesson_id}-practice"]["question_ids"]) == set(bank)


def test_counting_worked_examples_agree_with_the_bench_model():
    model = HemocytometerCount(COUNT_PROTOCOL)
    for counts, dilution, concentration, viability, uncertainty in (
        ({"A": {"viable": 41, "stained": 5}, "B": {"viable": 47, "stained": 7}}, 2, 8.8e5, 88.0, 10.0),
        ({"A": {"viable": 58, "stained": 7}, "B": {"viable": 63, "stained": 9}}, 2, 1.21e6, 100 * 121 / 137, 100 / math.sqrt(137)),
    ):
        expected = model.expected({"counts": counts, "dilution": dilution})
        assert expected["concentration"] == pytest.approx(concentration)
        assert expected["viability"] == pytest.approx(viability)
        assert expected["uncertainty"] == pytest.approx(uncertainty)
    assert COUNT_PROTOCOL["parameters"][0]["value"] == 1 * 1 * 0.1 / 1000
    unstained, stained = 31 + 28 + 35 + 30 + 29 + 33 + 27 + 32, 4 + 6 + 3 + 5 + 5 + 4 + 6 + 3
    assert (unstained, stained) == (245, 36)
    assert round(per_ml(unstained / 8, (20 + 30) / 20) / 1e5, 2) == 7.66
    assert round(100 * unstained / (unstained + stained), 1) == 87.2
    assert round(100 / math.sqrt(unstained + stained), 2) == 5.97 and round(100 / math.sqrt(unstained), 2) == 6.39
    assert round(math.sqrt(31 + 74), 1) == 10.2 and (74 - 31) / math.sqrt(31 + 74) > 4
    stated(COUNTING_READING, "8.8 × 10⁵", "88.0%", "1.0 × 10⁶", "7.66 × 10⁵", "87.2%", "5.97%", "6.39%", "√105 ≈ 10.2",
           "N = (100/5)² = 400")


def test_aseptic_protocol_parameters_match_the_lesson():
    params = {p["name"]: p for p in ASEPTIC_PROTOCOL["parameters"]}
    assert ASEPTIC_PROTOCOL["layer"] == 2 and len(ASEPTIC_PROTOCOL["checkpoints"]) == 25
    assert params["critical_zone_class"]["value"] == "ISO 5 (Class 100)"
    assert params["hepa_velocity_m_s"]["value"] == 0.45 and params["hepa_velocity_tolerance_pct"]["value"] == 20
    assert params["alcohol_percent"]["value"] == 70
    assert params["sterilizing_filter_um"]["value"] == 0.22
    assert params["mycoplasma_filter_um"]["value"] == 0.1
    assert params["mycoplasma_size_um"]["value"] == [0.15, 0.3]
    assert params["t75_medium_volume_ml"]["value"] == [10, 15]
    assert params["sterility_min_days"]["value"] == 14
    assert params["dual_temp_min_days_each"]["value"] == 7
    assert params["low_incubation_c"]["value"] == [20, 25]
    assert params["high_incubation_c"]["value"] == [30, 35]
    checkpoint_ids = {checkpoint["id"] for checkpoint in ASEPTIC_PROTOCOL["checkpoints"]}
    assert {
        "one-cell-line-only", "caps-never-face-down", "fresh-pipette-per-flask", "sterility-samples-incubated",
        "dual-temperature-incubation", "mycoplasma-test-requested", "no-antibiotic-rescue", "waste-decontaminated",
    } <= checkpoint_ids


def test_aseptic_reading_states_sources_conventions_and_limits():
    stated(ASEPTIC_READING, "ISO 5 (Class 100)", "0.45 m/s ±20%", "one cell line", "never place them face down",
           "fresh sterile pipette", "at least 14 days", "20–25 °C", "30–35 °C", "0.22 µm", "0.1 µm",
           "0.15–0.3 µm", "dedicated mycoplasma", "not sporicidal", "25 checkpoints", "printed p. 471",
           "current Appendix H, printed p. 473", "printed pp. 6, 13–14", "printed p. 34", "printed pp. 21, 25 and 35",
           "Simulation choices for teaching", "This is lesson 1 of the outlined cell-culture layer")
    assert ASEPTIC_READING.count(ASEPTIC_SIM_LINK) >= 2
    for claim in ("two cell lines", "expired lot", "UV lamp", "antibiotics", "turbid"):
        assert claim in ASEPTIC_READING, claim


def test_counting_reading_states_sources_conventions_and_limits():
    stated(COUNTING_READING, "1 mm × 1 mm × 0.1 mm = 0.1 mm³ = 0.1 µL = 10⁻⁴ mL", "Fuchs-Rosenthal chamber at 0.2 mm depth",
           "middle line as the dimension line", "deliberately do not describe filling or counting",
           "**At corners, exclusion wins.**", "Equivalent conventions exist", "100/√N %", "aggregates of varying size",
           "replicate agreement", "serum-free solution", "3 to 5 minutes", "pp. 466–468", "BSL-2 practices",
           "not a laboratory acceptance criterion", "nine checkpoints", "Lesson 1, aseptic technique, is also written")
    assert COUNTING_READING.count(COUNT_SIM_LINK) >= 2
    for claim in ("grow", "phenotype", "mycoplasma", "health"):
        assert re.search(rf"does not show[^.]*{claim}", COUNTING_READING), claim


def test_honest_partial_scope_and_policy():
    assert [lesson["id"] for lesson in LESSONS.values()] == ["cell-culture-practice-1", "cell-culture-practice-4"]
    assert (MANIFEST["version"], MANIFEST["maturity"], MANIFEST["review"]) == (
        "0.2.0", "partial", {"status": "unreviewed", "reviewed_version": None, "reviewers": []})
    assert MANIFEST["grading_policy"]["mode"] == "formative-only" and not MANIFEST["grading_policy"]["categories"]
    assert [a["mode"] for a in MANIFEST["assessments"]] == ["practice", "practice"]
    assert MANIFEST["duration"]["instructional_weeks"] == 2
    assert [week["lesson_ids"] for week in MANIFEST["duration"]["weeks"]] == [
        ["cell-culture-practice-1"], ["cell-culture-practice-4"]]
    assert MANIFEST["prerequisites"]["recommended_course_ids"] == ["lab-measurement", "lab-biosafety", "cell-biology"]
    assert len(CASES) == 2 and all(criterion["points"] == 0 for case in CASES for criterion in case["rubric"])
    stated(SYLLABUS, "Outline lessons 1 and 4 of the eight planned cell-culture topics", "not a cell-culture course",
           ASEPTIC_SIM_LINK, COUNT_SIM_LINK)
    assert CROSSWALK.count("| Absent, deferred |") == 6 and CROSSWALK.count("| **Covered** |") == 2
    stated(CROSSWALK, "agent-run comparison", "ISSCR standards are reserved", "simulation choices")
    text = json.dumps(MANIFEST) + SYLLABUS + ASEPTIC_READING + COUNTING_READING
    for allowed in ("certifying body", "cabinet certification", "certification and spill response"):
        text = text.replace(allowed, "")
    assert not re.search(r"\b(certif(ied|ication)|competent|qualified to|badge)\b", text, re.I)


def test_sources_and_protocol_reference():
    for module in MANIFEST["modules"]:
        assert "isscr-stem-cell-guidelines" not in module["source_ids"]
        for sid in module["source_ids"]:
            assert "cell-culture-practice" in REGISTRY[sid]["mapped_courses"], sid
            assert module["id"] in REGISTRY[sid]["mapped_modules"], sid
    assert REGISTRY["fda-aseptic-processing-2004"]["reuse_mode"] == "adapted"
    assert REGISTRY["cdc-nih-bmbl-6"]["reuse_mode"] == "adapted"
    for sid in ("geraghty-2014-cell-line-guidelines", "mit-ocw-20-109-spring-2010"):
        assert REGISTRY[sid]["reuse_mode"].startswith("link-only") and not REGISTRY[sid]["permissions"]["quotation"], sid
    assert {source["source_id"] for source in ASEPTIC_PROTOCOL["sources"]} == {
        "fda-aseptic-processing-2004", "geraghty-2014-cell-line-guidelines", "cdc-nih-bmbl-6"}
    assert "466–468" in COUNT_PROTOCOL["sources"][0]["use"] and "471" not in COUNT_PROTOCOL["sources"][0]["use"]
