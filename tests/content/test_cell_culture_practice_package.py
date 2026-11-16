"""Cell Culture Practice 0.4.0: independent keys, sourced statements, simulator agreement and partial scope.

Lesson 1 keys are exact source-based integers; lesson 4 numeric keys are recomputed from dilution, chamber
geometry and Poisson counting. Phase A adds exact Fraction medium calculations and six passage calculations.
Phase B independently recomputes seven cryopreservation keys and two synthetic STR shared-call keys.
Readings and protocol parameters are cross-checked. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from fractions import Fraction
from pathlib import Path

import jsonschema
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
MEDIA_READING = (COURSE / "modules/02-media-supplements-and-reagent-preparation.md").read_text(encoding="utf-8")
PASSAGE_READING = (COURSE / "modules/03-passaging-adherent-and-suspension-cells.md").read_text(encoding="utf-8")
CRYOPRESERVATION_READING = (COURSE / "modules/05-cryopreservation-and-thawing.md").read_text(encoding="utf-8")
CONTAMINATION_READING = (COURSE / "modules/06-contamination-mycoplasma-and-authentication.md").read_text(encoding="utf-8")
SYLLABUS = (COURSE / "syllabus.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
REGISTRY = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
COUNT_PROTOCOL = json.loads((ROOT / "content/bench/protocols/hemocytometer-cell-count-viability.json").read_text(encoding="utf-8"))
ASEPTIC_PROTOCOL = json.loads((ROOT / "content/bench/protocols/aseptic-medium-change-with-hidden-contamination.json").read_text(encoding="utf-8"))
MEDIA_PROTOCOL = json.loads((ROOT / "content/bench/protocols/filter-sterilize-and-qc-a-supplemented-medium.json").read_text(encoding="utf-8"))
PASSAGE_PROTOCOL = json.loads((ROOT / "content/bench/protocols/passage-an-adherent-line-to-a-target-density.json").read_text(encoding="utf-8"))
CRYOPRESERVATION_PROTOCOL = json.loads((ROOT / "content/bench/protocols/freeze-and-thaw-with-viability-outcomes.json").read_text(encoding="utf-8"))
CONTAMINATION_PROTOCOL = json.loads((ROOT / "content/bench/protocols/diagnose-a-contaminated-culture-from-clues.json").read_text(encoding="utf-8"))
COURSE_SCHEMA = json.loads((ROOT / "content/schemas/course.schema.json").read_text(encoding="utf-8"))
QUESTION_SCHEMA = json.loads((ROOT / "content/schemas/question.schema.json").read_text(encoding="utf-8"))
SOURCE_MAP = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))["modules"]
COUNT_SIM_LINK = "#/bench/hemocytometer-cell-count-viability"
ASEPTIC_SIM_LINK = "#/bench/aseptic-medium-change-with-hidden-contamination"
MEDIA_SIM_LINK = "#/bench/filter-sterilize-and-qc-a-supplemented-medium"
PASSAGE_SIM_LINK = "#/bench/passage-an-adherent-line-to-a-target-density"
CRYOPRESERVATION_SIM_LINK = "#/bench/freeze-and-thaw-with-viability-outcomes"
CONTAMINATION_SIM_LINK = "#/bench/diagnose-a-contaminated-culture-from-clues"
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
ASSESSMENTS = {assessment["id"]: assessment for assessment in MANIFEST["assessments"]}
ASEPTIC_BANK = {qid: q for qid, q in BANK.items() if qid.startswith("cell-culture-practice-1:")}
COUNT_BANK = {qid: q for qid, q in BANK.items() if qid.startswith("cell-culture-practice-4:")}
MEDIA_BANK = {qid: q for qid, q in BANK.items() if qid.startswith("cell-culture-practice-2:")}
PASSAGE_BANK = {qid: q for qid, q in BANK.items() if qid.startswith("cell-culture-practice-3:")}
CRYOPRESERVATION_BANK = {qid: q for qid, q in BANK.items() if qid.startswith("cell-culture-practice-5:")}
CONTAMINATION_BANK = {qid: q for qid, q in BANK.items() if qid.startswith("cell-culture-practice-6:")}


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
MEDIA_KEYS = {
    "cell-culture-practice-2:serum-stock-volume": (Fraction(8, 100) * 250, Fraction(250, 8)),
    "cell-culture-practice-2:glutamine-stock-volume": (Fraction(2 * 400, 200), Fraction(400, 200)),
    "cell-culture-practice-2:basal-volume": (500 - 50 - 5, 500 - 50),
    "cell-culture-practice-2:osmolality-estimate": (
        Fraction(445 * 290 + 50 * 300 + 5 * 400, 500), Fraction(290 + 300 + 400, 3)),
}
PASSAGE_KEYS = {
    "cell-culture-practice-3:seed-volume": (500000 / 1210000, 500000 / (1210000 / (121 / 130))),
    "cell-culture-practice-3:fresh-medium-volume": (12 - 500000 / 1210000, 12.0),
    "cell-culture-practice-3:three-flask-total-inoculum": (3 * 400000 / 1500000, 400000 / 1500000),
    "cell-culture-practice-3:split-denominator": (8.0 / 2.0, 2.0 / 8.0),
    "cell-culture-practice-3:pdl-increment": (math.log(7.26 / 1.815, 2), 7.26 / 1.815),
    "cell-culture-practice-3:cumulative-pdl": (18 + math.log(5.00 / 1.25, 2), 18 + 5.00 / 1.25),
}
CRYOPRESERVATION_KEYS = {
    "cell-culture-practice-5:freeze-medium-dmso-volume": (Fraction(4) * Fraction(1, 10), Fraction(4) * Fraction(1, 100)),
    "cell-culture-practice-5:freeze-medium-base-volume": (Fraction(4) - Fraction(4) * Fraction(1, 10), Fraction(4)),
    "cell-culture-practice-5:vial-count": (Fraction(10000000, 2500000), Fraction(2500000, 1000000)),
    "cell-culture-practice-5:freeze-cell-concentration": (
        Fraction(4 * 2500000, 4) / 1000000, Fraction(2500000, 4) / 1000000),
    "cell-culture-practice-5:post-dilution-dmso": (Fraction(10) * Fraction(1, 1 + 9), Fraction(10)),
    "cell-culture-practice-5:post-thaw-viable-yield": (
        Fraction(5, 2) * Fraction(92, 95), Fraction(5, 2) * Fraction(92, 100)),
    "cell-culture-practice-5:residual-dmso": (
        Fraction(100) * Fraction(1, 10) * Fraction(5, 100) / 2, Fraction(1, 200)),
}
STR_SAMPLE = [Counter([8, 8]), Counter([10, 11]), Counter([12, 14]), Counter([7, 9])]
STR_REFERENCE = [Counter([8, 9]), Counter([10, 11]), Counter([12, 12]), Counter([7, 9])]
STR_SHARED = sum(sum((sample & reference).values()) for sample, reference in zip(STR_SAMPLE, STR_REFERENCE, strict=True))
CONTAMINATION_KEYS = {
    "cell-culture-practice-6:str-shared-alleles": (STR_SHARED, 3),
    "cell-culture-practice-6:str-classroom-percentage": (100 * STR_SHARED / 8, 37.5),
}
NUMERIC_KEYS = COUNT_KEYS | ASEPTIC_KEYS | MEDIA_KEYS | PASSAGE_KEYS | CRYOPRESERVATION_KEYS | CONTAMINATION_KEYS


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



def test_numeric_answer_limitation_is_recomputed_from_the_bank():
    specs = [item["solution_spec"] for item in BANK.values() if item["type"] == "numeric"]
    significant = sum(bool(spec["significant_figures"]) for spec in specs)
    units = sum(bool(spec["unit_required"]) for spec in specs)
    dimensions = sum(bool(spec["dimensions"]) for spec in specs)
    expected = f"Of the {len(specs)} numerical answers, {units} require units, {significant} check significant figures and {dimensions} check dimensions."
    assert (len(specs), units, significant, dimensions) == (28, 0, 16, 0)
    assert expected in MANIFEST["limitations"]


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
    ("cell-culture-practice-2", MEDIA_BANK),
    ("cell-culture-practice-3", PASSAGE_BANK),
    ("cell-culture-practice-4", COUNT_BANK),
    ("cell-culture-practice-5", CRYOPRESERVATION_BANK),
    ("cell-culture-practice-6", CONTAMINATION_BANK),
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
           "not a laboratory acceptance criterion", "nine checkpoints", "Lessons 1–6")
    assert COUNTING_READING.count(COUNT_SIM_LINK) >= 2
    for claim in ("grow", "phenotype", "mycoplasma", "health"):
        assert re.search(rf"does not show[^.]*{claim}", COUNTING_READING), claim


def test_early_readings_agree_on_current_package_availability():
    availability = ("Lessons 1–6 of the outlined cell-culture layer are written and available; "
                    "only lessons 7–8 (human pluripotent stem cells and records) remain deferred.")
    for reading in (ASEPTIC_READING, PASSAGE_READING, COUNTING_READING):
        assert reading.count(availability) == 1
    assert "media preparation, passaging, cryopreservation, full contamination management" not in ASEPTIC_READING
    assert "lessons 5–8" not in COUNTING_READING
    assert "not written yet" not in COUNTING_READING
    assert "planned lesson 6" not in PASSAGE_READING
    stated(PASSAGE_READING, "to the lesson 6 discussion of contamination, mycoplasma and authentication")


def test_honest_partial_scope_and_policy():
    assert [lesson["id"] for lesson in LESSONS.values()] == [
        "cell-culture-practice-1", "cell-culture-practice-4", "cell-culture-practice-2", "cell-culture-practice-3",
        "cell-culture-practice-5", "cell-culture-practice-6"]
    assert (MANIFEST["version"], MANIFEST["maturity"], MANIFEST["review"]) == (
        "0.4.0", "partial", {"status": "unreviewed", "reviewed_version": None, "reviewers": []})
    assert MANIFEST["grading_policy"]["mode"] == "formative-only" and not MANIFEST["grading_policy"]["categories"]
    assert [a["mode"] for a in MANIFEST["assessments"]] == ["practice"] * 6
    assert MANIFEST["duration"]["instructional_weeks"] == 6
    assert [week["lesson_ids"] for week in MANIFEST["duration"]["weeks"]] == [
        ["cell-culture-practice-1"], ["cell-culture-practice-4"],
        ["cell-culture-practice-2"], ["cell-culture-practice-3"],
        ["cell-culture-practice-5"], ["cell-culture-practice-6"]]
    assert MANIFEST["prerequisites"]["recommended_course_ids"] == ["lab-measurement", "lab-biosafety", "cell-biology"]
    assert len(CASES) == 6 and all(criterion["points"] == 0 for case in CASES for criterion in case["rubric"])
    stated(SYLLABUS, "Outline lessons 1–6 of the eight planned cell-culture topics", "not a cell-culture course",
           ASEPTIC_SIM_LINK, COUNT_SIM_LINK, MEDIA_SIM_LINK, PASSAGE_SIM_LINK,
           CRYOPRESERVATION_SIM_LINK, CONTAMINATION_SIM_LINK)
    assert CROSSWALK.count("| Absent, deferred |") == 2 and CROSSWALK.count("| **Covered** |") == 6
    stated(CROSSWALK, "agent-run comparison", "ISSCR standards are reserved", "simulation choices")
    text = (json.dumps(MANIFEST) + SYLLABUS + ASEPTIC_READING + COUNTING_READING + MEDIA_READING + PASSAGE_READING
            + CRYOPRESERVATION_READING + CONTAMINATION_READING)
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


@pytest.mark.parametrize("lesson_id,outcome_id", [
    ("cell-culture-practice-2", "cell-culture-practice-outcome-5"),
    ("cell-culture-practice-3", "cell-culture-practice-outcome-6"),
    ("cell-culture-practice-5", "cell-culture-practice-outcome-7"),
    ("cell-culture-practice-6", "cell-culture-practice-outcome-8"),
])
def test_lesson_objective_assessment_card_case_and_source_map_mappings(lesson_id, outcome_id):
    lesson = LESSONS[lesson_id]
    objectives = [item for item in MANIFEST["lesson_objectives"] if item["id"].startswith(f"{lesson_id}-objective-")]
    assert len(objectives) == 5
    assert all(item["course_outcome_ids"] == [outcome_id] for item in objectives)
    assessment = ASSESSMENTS[f"{lesson_id}-practice"]
    assert assessment["objective_ids"] == [*lesson["objectives"], outcome_id]
    case = next(case for case in CASES if case["id"] == f"{lesson_id}:case")
    assert case["mode"] == "self-assessment" and set(case["objective_ids"]) == set(lesson["objectives"])
    assert len(case["rubric"]) == 5 and "zero-point self-check" in case["limitations"][0]
    cards = [card for card in CARDS if card["lesson_id"] == lesson_id]
    assert {oid for card in cards for oid in card["objective_ids"]} == set(lesson["objectives"])
    assert all(card["license"] == "CC-BY-4.0" for card in cards)
    module = next(module for module in MANIFEST["modules"] if module["lessons"][0]["id"] == lesson_id)
    mapped = next(item for item in SOURCE_MAP if item["module_id"] == module["id"])
    assert mapped["source_ids"] == module["source_ids"]
    assert mapped["original_content"] and mapped["license"] == "CC-BY-4.0"
    assert mapped["relationship"].startswith("original-instruction")


def test_media_numeric_calculations_and_worked_solutions_are_exact():
    assert MEDIA_KEYS["cell-culture-practice-2:serum-stock-volume"][0] == 20
    assert MEDIA_KEYS["cell-culture-practice-2:glutamine-stock-volume"][0] == 4
    assert MEDIA_KEYS["cell-culture-practice-2:basal-volume"][0] == 445
    assert MEDIA_KEYS["cell-culture-practice-2:osmolality-estimate"][0] == Fraction(2921, 10)
    stated(MEDIA_READING, "146,050/500 = **292.1 mOsm/kg**", "500 − 50 − 5 = **445 mL**",
           "(2 mM × 400 mL)/(200 mM) = **4 mL stock**", "0.08 × 250)/1 = **20 mL serum**")
    for qid in MEDIA_KEYS | PASSAGE_KEYS:
        assert any(token in BANK[qid]["feedback"]["solution"] for token in ("=", "log₂")), qid


def test_media_protocol_parameters_match_the_lesson():
    params = {p["name"]: p for p in MEDIA_PROTOCOL["parameters"]}
    assert MEDIA_PROTOCOL["version"] == "0.2.0"
    assert MEDIA_PROTOCOL["layer"] == 2
    assert len(MEDIA_PROTOCOL["actions"]) == len(MEDIA_PROTOCOL["checkpoints"]) == 14
    assert params["basal_medium_role"]["source"]["source_id"] == "geraghty-2014-cell-line-guidelines"
    eagle_use = next(source for source in MEDIA_PROTOCOL["sources"] if source["source_id"] == "eagle-1955-medium-nutrition")
    assert "Bibliographic citation only" in eagle_use["use"]
    assert "article body neither retrieved nor read" in eagle_use["use"]
    assert params["basal_lot_id"]["value"] == "BASAL-2026-11-01"
    assert params["filter_lot_id"]["value"] == "FILTER-PVDF-022-01"
    assert params["serum_lot_a_id"]["value"] != params["serum_lot_b_id"]["value"]
    assert params["glutamine_aliquot_a_id"]["value"] != params["glutamine_aliquot_b_id"]["value"]
    label_action = next(action for action in MEDIA_PROTOCOL["actions"] if action["name"] == "label_bottle")
    assert {"basal_lot_id", "serum_lot_id", "glutamine_lot_id", "filter_lot_id", "component_lots_linked"} <= {
        parameter["name"] for parameter in label_action["params"]
    }
    assert params["final_batch_volume_ml"]["value"] == 500
    assert params["serum_final_fraction"]["value"] == 0.1
    assert params["glutamine_stock_fold"]["value"] == 100
    assert params["glutamine_stock_mm"]["value"] == 200 and params["glutamine_final_mm"]["value"] == 2
    assert params["basal_volume_ml"]["value"] == 445
    assert params["serum_volume_ml"]["value"] == 50 and params["glutamine_volume_ml"]["value"] == 5
    assert params["filter_pore_um"]["value"] == 0.22 and params["filter_membrane"]["value"] == "pvdf"
    assert params["ph_range"]["value"] == [7.1, 7.3]
    assert params["osmolality_range_mosm_kg"]["value"] == [280, 310]
    assert params["filter_recovery_fraction"]["value"] == 0.98
    assert params["sterility_control_volume_ml"]["value"] == 10
    assert params["storage_temperature_c"]["value"] == [2, 8]
    assert params["supplemented_expiry_days"]["value"] == 14
    assert params["sterility_min_days"]["value"] == 14 and params["dual_temp_min_days_each"]["value"] == 7
    assert params["base_ph_range"]["value"] == [7.16, 7.24]
    assert params["expiry_date"]["value"] == "2026-11-29"
    assert params["batch_id"]["value"] == "MED-2026-11-15-01"
    assert params["medium_name"]["value"] == "MEM-serum-glutamine"
    assert params["cell_line_id"]["value"] == "synthetic-line-1"
    assert {checkpoint["id"] for checkpoint in MEDIA_PROTOCOL["checkpoints"]} == {
        "supplies-inspected", "serum-in-date", "glutamine-aliquot-cold", "supplement-volumes",
        "prefiltration-qc", "correct-filter", "filter-integrity-verified", "labeled-collection-bottle",
        "sterility-samples-incubated", "dual-temperature-incubation", "mycoplasma-test-requested",
        "complete-label-and-lot-trace", "cold-dark-storage", "release-pending-qc",
    }
    for name in ("ph_range", "osmolality_range_mosm_kg", "filter_recovery_fraction", "supplemented_expiry_days"):
        assert params[name]["source"]["kind"] in {"simulation-typical", "simulation-model"}


def test_media_reading_states_sources_conventions_and_limits():
    stated(MEDIA_READING, "**Status:**", "## Learning objectives", "## Common mistakes", "## Scope and sources",
           "final** batch volume", "500 mL final volume", "50 mL", "5 mL", "445 mL", "292.1 mOsm/kg",
           "0.22 µm", "bubble-point or pressure-hold", "2–8 °C", "2026-11-29",
           "at least 7 days at 20–25 °C, followed by at least 7 days at 30–35 °C", "14 checkpoints",
           "simulation choices", "not laboratory acceptance criteria", "does not establish laboratory competency",
           "validate a physical preparation", "14-day supplemented-medium expiry")
    assert MEDIA_READING.count(MEDIA_SIM_LINK) >= 2 and len(MEDIA_READING.split()) >= 800
    for claim in ("L-glutamine", "freeze–thaw", "heat-inactivat", "serum-free", "chemically defined",
                  "osmolality", "bicarbonate/CO₂", "phenol red", "dedicated mycoplasma", "one cell line",
                  "independently of whether a filtrate control was drawn", "pending/indeterminate",
                  "a “lots linked” assertion without those IDs does not pass",
                  "integrated package source map and source registry",
                  "Only Crossref bibliographic metadata were retrieved", "article body was neither retrieved nor read",
                  "no methods, results or historical-influence claim", "already-read Thermo Fisher and Geraghty references",
                  "Eagle bibliographic citation only; no article methods, results or historical-role claim"):
        assert claim in MEDIA_READING, claim
    assert "integration fragments and report" not in MEDIA_READING
    assert "lesson's integration fragments" not in MEDIA_READING
    assert "Eagle's 1955 analysis" not in MEDIA_READING
    assert "Basal nutrition and the historical role" not in MEDIA_READING


def test_media_sources_and_protocol_reference():
    expected = {"eagle-1955-medium-nutrition", "thermo-fisher-media-preparation-powder-concentrates",
                "thermo-fisher-cell-culture-environment", "thermo-fisher-serum-heat-inactivation-faq",
                "geraghty-2014-cell-line-guidelines", "fda-aseptic-processing-2004", "mit-ocw-20-109-spring-2010"}
    module = next(module for module in MANIFEST["modules"] if module["id"] == "cell-culture-practice-module-2")
    assert set(module["source_ids"]) == expected
    for sid in expected:
        assert "cell-culture-practice" in REGISTRY[sid]["mapped_courses"]
        assert module["id"] in REGISTRY[sid]["mapped_modules"]
    for sid in expected - {"fda-aseptic-processing-2004"}:
        assert REGISTRY[sid]["reuse_mode"].startswith("link-only") and not REGISTRY[sid]["permissions"]["quotation"], sid
    for sid in expected - {"geraghty-2014-cell-line-guidelines", "fda-aseptic-processing-2004",
                           "mit-ocw-20-109-spring-2010"}:
        assert REGISTRY[sid]["permissions"] == {
            "linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        assert REGISTRY[sid]["accessed_at"] == "2026-11-15" and not REGISTRY[sid]["imported_assets"]
    assert REGISTRY["fda-aseptic-processing-2004"]["reuse_mode"] == "adapted"
    eagle_rights = REGISTRY["eagle-1955-medium-nutrition"]["rights_notes"]
    stated(eagle_rights, "Only Crossref bibliographic metadata", "article body was neither retrieved nor read",
           "historical-role claims")
    mapped = next(item for item in SOURCE_MAP if item["module_id"] == "cell-culture-practice-module-2")
    stated(mapped["modifications"][0], "metadata-only bibliographic citation", "no historical-role claim",
           "already-read Thermo Fisher pages")
    stated(CROSSWALK, "Bibliographic citation only; no methods, results or historical-role claim",
           "Modern basal-medium formulation", "Modern basal-medium components")
    assert "Historical basis for defined basal nutritional requirements" not in CROSSWALK
    history = next(item for item in MANIFEST["history"] if item["version"] == "0.3.0")["summary"]
    stated(history, "six Thermo Fisher pages", "article body was neither retrieved nor read")
    assert "seven Thermo Fisher pages" not in history
    assert {source["source_id"] for source in MEDIA_PROTOCOL["sources"]} == expected - {
        "thermo-fisher-serum-heat-inactivation-faq", "mit-ocw-20-109-spring-2010"}


def test_passage_protocol_reading_and_worked_arithmetic_agree():
    params = {item["name"]: item["value"] for item in PASSAGE_PROTOCOL["parameters"]}
    assert PASSAGE_PROTOCOL["version"] == "0.1.0"
    assert PASSAGE_PROTOCOL["layer"] == 2 and len(PASSAGE_PROTOCOL["checkpoints"]) == 16
    assert len(PASSAGE_PROTOCOL["actions"]) == 15
    label_action = next(action for action in PASSAGE_PROTOCOL["actions"] if action["name"] == "label_flasks")
    pdl_increment = next(parameter for parameter in label_action["params"] if parameter["name"] == "pdl_increment")
    assert (pdl_increment["min"], pdl_increment["max"]) == (-20, 20)
    assert params["routine_confluence_pct"] == [70, 85] and params["overconfluent_pct"] == 95
    assert params["wash_volume_ml"] == 75 / 10 * 2 == 15
    assert params["dissociation_volume_ml"] == 75 / 10 * 0.5 == 3.75
    assert params["neutralization_volume_ml"] == 2 * params["dissociation_volume_ml"] == 7.5
    assert params["resuspension_volume_ml"] == 6 and params["target_flasks"] == 2
    assert params["target_viable_cells_per_flask"] == 500000 and params["target_final_volume_ml"] == 12
    concentration = ((58 + 63) / 2) * 10000 * ((10 + 10) / 10)
    viability = 100 * (58 + 63) / (58 + 5 + 63 + 4)
    harvest = concentration * 6
    inoculum = 500000 / concentration
    assert concentration == 1210000 and round(viability, 1) == 93.1
    assert harvest == 7260000 and round(inoculum, 6) == 0.413223
    assert round(12 - inoculum, 6) == 11.586777 and math.log2(harvest / 1815000) == 2
    stated(PASSAGE_READING, "**Status:**", "70–85%", "95%", "15 mL", "3.75 mL", "7.5 mL",
           "1.21 × 10⁶", "93.1%", "0.413223 mL", "11.586777 mL", "7.26 × 10⁶", "20.00",
           "16 checkpoints", "simulation choices", "not laboratory acceptance criteria", "does not predict attachment",
           "The bench simulator does not model suspension", "source-map.json", "source registry")
    assert PASSAGE_READING.count(PASSAGE_SIM_LINK) >= 2
    assert "integration fragments and report" not in PASSAGE_READING


def test_passage_sources_and_protocol_reference():
    expected = {"thermo-gibco-adherent-subculture", "thermo-gibco-suspension-subculture",
                "thermo-gibco-maintaining-cultured-cells"}
    module = next(module for module in MANIFEST["modules"] if module["id"] == "cell-culture-practice-module-3")
    assert set(module["source_ids"]) == expected | {"mit-ocw-20-109-spring-2010"}
    for sid in expected:
        source = REGISTRY[sid]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {"linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        assert source["accessed_at"] == "2026-11-15" and "Terms" in source["rights_notes"]
        assert source["mapped_modules"] == ["cell-culture-practice-module-3"] and not source["imported_assets"]
    assert REGISTRY["mit-ocw-20-109-spring-2010"]["reuse_mode"] == "link-only-comparator"
    assert "cell-culture-practice-module-3" in REGISTRY["mit-ocw-20-109-spring-2010"]["mapped_modules"]
    assert {item["source_id"] for item in PASSAGE_PROTOCOL["sources"]} == expected


# Phase B: joint cryopreservation and contamination package checks -------------


def test_phase_b_inventory_schema_and_single_joint_history():
    jsonschema.validate(MANIFEST, COURSE_SCHEMA)
    assert (len(BANK), len(CARDS), len(CASES)) == (72, 24, 6)
    assert len(MANIFEST["modules"]) == len(MANIFEST["assessments"]) == len(SOURCE_MAP) == 6
    assert len(MANIFEST["outcomes"]) == 8 and len(MANIFEST["lesson_objectives"]) == 30
    assert [assessment["points"] for assessment in MANIFEST["assessments"]] == [17, 14, 16, 14, 14, 17]
    assert sum(assessment["points"] for assessment in MANIFEST["assessments"]) == 92
    history = [entry for entry in MANIFEST["history"] if entry["version"] == "0.4.0"]
    assert len(history) == 1
    stated(history[0]["summary"], "lessons 5 and 6 jointly in Phase B", "72 items and 92 practice points",
           "24 cards and six cases", "Partial, unreviewed and formative-only")
    assert MANIFEST["history"][-2]["version"] == "0.3.0"
    assert [week["week"] for week in MANIFEST["duration"]["weeks"]] == [1, 2, 3, 4, 5, 6]


@pytest.mark.parametrize("bank", [CRYOPRESERVATION_BANK, CONTAMINATION_BANK])
def test_phase_b_items_are_original_canonical_and_fully_mapped(bank):
    assert len(bank) == 12
    for item in bank.values():
        jsonschema.validate(item, QUESTION_SCHEMA)
        assert item["provenance"]["kind"] == "original"
        assert item["visibility"] == "public-practice-authoring"
        assert item["feedback"]["hint"] and item["feedback"]["solution"]
        if item["type"] == "numeric":
            assert "=" in item["feedback"]["solution"]
        else:
            assert len(item["feedback"]["solution"]) > 100


def test_phase_b_independent_key_groups_and_misconception_feedback():
    assert STR_SHARED == 6 and 100 * STR_SHARED / 8 == 75.0
    assert len(CRYOPRESERVATION_KEYS) == 7 and len(CONTAMINATION_KEYS) == 2
    for qid in CRYOPRESERVATION_KEYS:
        assert len(BANK[qid]["feedback"]["solution"]) > 100
    for qid, item in CONTAMINATION_BANK.items():
        if item["type"] != "numeric":
            assert len(item["feedback"]["solution"]) > 150
            assert any(token in item["feedback"]["solution"].lower()
                       for token in ("misconception", "not", "rather than", "cannot"))


def test_cryopreservation_quarantine_key_and_per_vial_case_wording():
    item = BANK["cell-culture-practice-5:quarantine-bank-record"]
    key = item["solution_spec"]["answer"]
    assert key == 2 and item["options"][key].startswith("Quarantine pending required QC")
    assert "working-stock tier" in item["options"][key]
    assert item["options"][1].startswith("Discard every vial automatically")
    assert grade(item, AttemptRequest(response="2")).correct
    assert not grade(item, AttemptRequest(response="1")).correct
    case = next(case for case in CASES if case["id"] == "cell-culture-practice-5:case")
    stated(case["prompt"], "each contains 2.50 × 10⁶ viable cells per vial",
           "separately from the batch concentration of 2.50 × 10⁶ cells/mL")
    assert "viable cells per vial for each of four vials and, separately" in case["rubric"][1]["criterion"]
    assert all(criterion["points"] == 0 and criterion["levels"] == [] for criterion in case["rubric"])


def test_cryopreservation_protocol_reading_and_worked_arithmetic_agree():
    params = {item["name"]: item["value"] for item in CRYOPRESERVATION_PROTOCOL["parameters"]}
    assert CRYOPRESERVATION_PROTOCOL["version"] == "0.1.0" and CRYOPRESERVATION_PROTOCOL["layer"] == 2
    assert len(CRYOPRESERVATION_PROTOCOL["actions"]) == 13
    assert len(CRYOPRESERVATION_PROTOCOL["checkpoints"]) == 15
    assert params["vial_count"] == 4 and params["viable_cells_per_vial"] == 2500000
    assert params["volume_per_vial_ml"] == 1 and params["dmso_final_fraction"] == 0.1
    assert params["freeze_medium_temperature_c"] == 4 and params["cooling_rate_c_per_min"] == 1
    assert params["thaw_temperature_c"] == 37 and params["post_thaw_medium_ml"] == 9
    total = 4 * 1.0
    dmso = total * 0.1
    base = total - dmso
    diluted = 0.1 * 1 / (1 + 9) * 100
    residual_volume = 0.1 * (1 - 0.95)
    residual_pct = residual_volume / 2 * 100
    recovered = 2.5 * 92 / 95
    concentration = recovered / 2
    assert (total, dmso, base) == (4, 0.4, 3.6)
    assert diluted == 1 and residual_pct == pytest.approx(0.25)
    assert recovered == pytest.approx(2.4210526315789473)
    assert concentration == pytest.approx(1.2105263157894737)
    stated(CRYOPRESERVATION_READING, "permeating", "non-permeating", "cold", "dropwise", "1 °C/min", "passive",
           "two-factor", "vapour", "liquid", "37 °C", "0.400 mL", "3.60 mL", "1.00% v/v", "0.250% v/v",
           "2.421053 × 10⁶", "1.210526 × 10⁶", "quarantine_pending_qc", "15 checkpoints", "simulation choices",
           "not laboratory acceptance criteria", "No output establishes physical validation", "10.1126/science.168.3934.939",
           "10.1038/1831394a0")
    assert CRYOPRESERVATION_READING.count(CRYOPRESERVATION_SIM_LINK) >= 2
    assert "**Status:**" in CRYOPRESERVATION_READING and "partial Cell Culture Practice" in CRYOPRESERVATION_READING
    assert ".972" not in CRYOPRESERVATION_READING


def test_cryopreservation_sources_are_link_only_with_access_limits():
    expected = {"thermo-gibco-freezing-cells", "thermo-gibco-thawing-cells", "mazur-1970-cryobiology-freezing-systems",
                "lovelock-bishop-1959-dmso", "murray-gibson-2022-chemical-cryopreservation"}
    module = next(module for module in MANIFEST["modules"] if module["id"] == "cell-culture-practice-module-5")
    assert set(module["source_ids"]) == expected | {"mit-ocw-20-109-spring-2010"}
    for source_id in expected:
        source = REGISTRY[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {"linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        assert source["accessed_at"] == "2026-11-15" and source["mapped_modules"] == ["cell-culture-practice-module-5"]
        assert not source["imported_assets"] and source["rights_notes"] and source["url"].startswith("https://")
    assert REGISTRY["mazur-1970-cryobiology-freezing-systems"]["url"].endswith("939")
    assert "full text was not accessible" in REGISTRY["mazur-1970-cryobiology-freezing-systems"]["third_party_notes"].lower()
    assert "time-limited" in REGISTRY["murray-gibson-2022-chemical-cryopreservation"]["license"]
    assert {item["source_id"] for item in CRYOPRESERVATION_PROTOCOL["sources"]} == expected


def test_contamination_protocol_reading_and_worked_arithmetic_agree():
    params = {item["name"]: item["value"] for item in CONTAMINATION_PROTOCOL["parameters"]}
    assert CONTAMINATION_PROTOCOL["version"] == "0.1.0" and CONTAMINATION_PROTOCOL["layer"] == 2
    assert len(CONTAMINATION_PROTOCOL["actions"]) == 9 and len(CONTAMINATION_PROTOCOL["checkpoints"]) == 13
    assert params["flask_count"] == 5 and params["str_locus_count"] == 4 and params["str_reference_allele_calls"] == 8
    assert params["quarantine_requirement"] == "all_five_before_any_test_disposition_or_antibiotic"
    assert params["antibiotic_release_pathway"] == "none"
    assert params["linked_record_bundles"] == "revealed_per_flask_at_inspection"
    assert "all five linked flasks" in CONTAMINATION_PROTOCOL["guided_steps"][1]
    assert "ASN-a2" not in json.dumps(CONTAMINATION_PROTOCOL) and "ASN-0002" in CONTAMINATION_PROTOCOL["limitations"][2]
    assert STR_SHARED == 6 and 100 * STR_SHARED / 8 == 75.0
    stated(CONTAMINATION_READING, "turbid", "filaments", "micro-colonies", "culture", "PCR", "DNA",
           "Quarantine precedes identification", "Antibiotic masking is not rescue", "HeLa", "locus", "allele", "75.0%",
           "incoming", "source", "13 checkpoints", "simulation choices", "not laboratory acceptance criteria",
           "physically validated", "Tanabe or Masters algorithm", "no real cell-line or donor data",
           "linked-record bundle", "competing hypotheses", "five anonymous synthetic flasks")
    assert CONTAMINATION_READING.count(CONTAMINATION_SIM_LINK) >= 2
    assert "shared medium for the bacterial pattern" not in CONTAMINATION_READING
    assert "The simulation assigns five independent source hypotheses:" not in CONTAMINATION_READING
    assert "linked-record bundle" in json.dumps(CONTAMINATION_PROTOCOL["guided_steps"])


def test_contamination_sources_rights_and_bounded_release_scope():
    expected = {"drexler-uphoff-mycoplasma-detection", "atcc-ansi-str-standard", "iclac-misidentified-cells-register"}
    for source_id in expected:
        source = REGISTRY[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {"linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        assert source["accessed_at"] == "2026-11-15" and source["mapped_modules"] == ["cell-culture-practice-module-6"]
        assert not source["imported_assets"] and source["url"].startswith("https://") and source["rights_notes"]
    drexler = REGISTRY["drexler-uphoff-mycoplasma-detection"]
    stated(drexler["version"], "10.1023/A:1022913015916", "PMC3463982")
    assert "16-page PDF" in drexler["third_party_notes"]
    atcc = REGISTRY["atcc-ansi-str-standard"]
    assert "ASN-0002-2022" in atcc["title"] and "full paid standard text was not accessed" in atcc["third_party_notes"]
    iclac = REGISTRY["iclac-misidentified-cells-register"]
    assert "CC BY-NC-ND 4.0" in iclac["license"] and "2026-02-15" in iclac["version"]
    assert "No register row" in iclac["third_party_notes"] and "Cross-Contaminations" not in CONTAMINATION_READING
    assert {item["source_id"] for item in CONTAMINATION_PROTOCOL["sources"]} == {
        "drexler-uphoff-mycoplasma-detection", "geraghty-2014-cell-line-guidelines", "atcc-ansi-str-standard"}
    stated(CONTAMINATION_READING, "partial", "unreviewed", "formative", "does not establish competency",
           "No register row", "CC BY-NC-ND 4.0", "15 February 2026", "no real cell-line or donor data")
    assert all("physical_validation" not in item for item in CONTAMINATION_BANK.values())


def test_phase_b_existing_source_unions_and_source_maps_preserve_prior_work():
    mit = REGISTRY["mit-ocw-20-109-spring-2010"]
    assert mit["reuse_mode"] == "link-only-comparator" and mit["license"] == "CC-BY-NC-SA-4.0"
    assert set(mit["mapped_modules"]) == {
        "cell-culture-practice-module-1", "cell-culture-practice-module-2", "cell-culture-practice-module-3",
        "cell-culture-practice-module-4", "cell-culture-practice-module-5", "cell-culture-practice-module-6"}
    geraghty = REGISTRY["geraghty-2014-cell-line-guidelines"]
    assert set(geraghty["mapped_modules"]) == {
        "cell-culture-practice-module-1", "cell-culture-practice-module-2", "cell-culture-practice-module-6"}
    for module in MANIFEST["modules"]:
        mapped = next(item for item in SOURCE_MAP if item["module_id"] == module["id"])
        assert mapped["source_ids"] == module["source_ids"]
        assert mapped["original_content"] and mapped["license"] == "CC-BY-4.0"
        assert mapped["relationship"].startswith("original-instruction")
