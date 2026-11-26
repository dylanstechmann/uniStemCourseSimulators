"""Agriculture/habitat survey: independent keys, source links, synthetic ledgers and honest boundaries.

All 24 numeric answers are recomputed here from displayed inputs, independently of the
question-bank formulas. CSV residuals are also recomputed row by row. These are
agent-run structural/arithmetic checks, not scientific, engineering or owner review.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import jsonschema
import pytest
from referencing import Registry, Resource

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/agriculture-construction-habitats"
CID = "agriculture-construction-habitats"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text())["questions"]}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text())["cards"]
CASES = json.loads((COURSE / "rubrics/case-studio.json").read_text())["cases"]
REGISTRY = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text())["sources"]}
CURRICULUM = json.loads((ROOT / "content/curriculum-map.json").read_text())
LESSONS = [lesson for module in MANIFEST["modules"] for lesson in module["lessons"]]
READINGS = {lesson["id"]: (COURSE / lesson["reading"]).read_text(encoding="utf-8") for lesson in LESSONS}
OBJECTIVES = {o["id"]: o for o in MANIFEST["lesson_objectives"]}
OUTCOMES = {o["id"] for o in MANIFEST["outcomes"]}


def load_csv(relative):
    with (COURSE / relative).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def item_id(key):
    lesson, slug = key.split(":")
    return f"{CID}-{lesson}:{slug}"


# (independently recomputed answer, one independently recomputed misconception).
NUMERIC_KEYS = {
    "1:reclaimed-share": (32 / (18 + 32 + 50) * 100, 32 / 50 * 100),
    "1:production-area": (120 + 80 - 30, 120 + 80),
    "1:closing-water-stock": (240 + 60 - 180, 240 + 60),
    "2:dli-from-ppfd": (200 * 14 * 3600 / 1e6, 200 * 14 * 3600 / 1000),
    "2:ppfd-from-dli": (12e6 / (16 * 3600), 12e6 / (16 * 60)),
    "2:fixture-energy": (4 * 0.12 * 14, 4 * 0.12 * 14 * 60),
    "3:tank-closing-stock": (180 + 40 + 30 - 70, 180 + 40 - 70),
    "3:material-inventory": (12 - 3 - 4, 12 - 3),
    "3:sensor-mean": ((22 + 24 + 23) / 3, 22 + 24 + 23),
    "4:molecular-outcome-percent": (18 / 72 * 100, 18 / 72),
    "4:phenotype-percentage-points": ((14 / 60 - 6 / 60) * 100, 14 / 60 * 100 - 6),
    "4:excess-variant-count": (10 - 4, 10 + 4),
    "5:equal-support-reaction": (12 / 2, 12),
    "5:parallel-then-review": (max(3, 4) + 2, 3 + 4 + 2),
    "5:critical-path-duration": (max(2 + 5 + 3, 2 + 4 + 3), 2 + 4 + 3),
    "6:outage-critical-energy": (0.35 * 8, 0.35 * 8 * 60),
    "6:outage-water-stock": (150 + 0 + 12 - 30, 150 + 12),
    "6:recovery-share": (36 / (36 + 24) * 100, 36 / 24 * 100),
    "7:a03-energy-residual": (30 - (14.4 + 9.6 + 4.8), 30 - 14.4),
    "7:a03-water-residual": (138 + 30 + 40 - 50 - 156, 138 + 30 + 40 - 50),
    "7:outage-backup-total": (3.6 + 2.4, 3.6 * 2.4),
    "8:r02-rehearsal-dli": (220 * 14 * 3600 / 1e6, 220 * 14 * 3600 / 1000),
    "8:r03-closing-water": (90 + 20 + 28 - 46, 90 + 20 + 28),
    "8:r04-outage-energy": (0.30 * 6, 0.30 * 6 * 60),
}


def test_structure_assessment_and_generated_schemas():
    assert (MANIFEST["version"], MANIFEST["maturity"], MANIFEST["review"]["status"]) == ("0.1.0", "partial", "unreviewed")
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert len(MANIFEST["modules"]) == 6 and len(LESSONS) == 8
    assert [len(m["lessons"]) for m in MANIFEST["modules"]] == [1, 1, 1, 1, 1, 3]
    assert len(BANK) == 48 and len(CARDS) == 24 and len(CASES) == 6
    assert sum(q["points"] for q in BANK.values()) == 56
    assert len([case for case in CASES if ":project-m" in case["id"]]) == 5
    assert all(case["mode"] == "self-assessment" for case in CASES)
    assert all(criterion["points"] == 0 for case in CASES for criterion in case["rubric"])
    scheduled = [lid for week in MANIFEST["duration"]["weeks"] for lid in week["lesson_ids"]]
    assert sorted(scheduled) == sorted(lesson["id"] for lesson in LESSONS)
    for number, lesson in enumerate(LESSONS, start=1):
        assert lesson["id"] == (f"{CID}-project-guide" if number == 8 else f"{CID}-{number}")
        assert len(lesson["objectives"]) == 3 and len(lesson["question_ids"]) == 6 and len(lesson["card_ids"]) == 3
    for number in range(1, 9):
        assessment = next(a for a in MANIFEST["assessments"] if f"{CID}-{number}-practice" == a["id"] or (number == 8 and a["id"] == f"{CID}-project-rehearsal-practice"))
        assert assessment["mode"] == "practice" and assessment["points"] == 7
        assert set(assessment["question_ids"]) == set(LESSONS[number - 1]["question_ids"])
        assert set(assessment["objective_ids"]) == {*LESSONS[number - 1]["objectives"], f"{CID}-outcome-{number}"}
    mapped = {oid for a in MANIFEST["assessments"] for oid in a["objective_ids"]}
    assert set(OBJECTIVES) <= mapped and OUTCOMES <= mapped
    practised = {oid for q in BANK.values() for oid in q["objective_ids"]}
    assert practised == set(OBJECTIVES)
    for schema, value in [
        ("course.schema.json", MANIFEST),
        ("question-bank.schema.json", {"schema_version": "1.0", "course_id": CID, "license": "CC-BY-4.0", "questions": list(BANK.values())}),
        ("curriculum-map.schema.json", CURRICULUM),
        ("source.schema.json", {"schema_version": "1.0", "sources": list(REGISTRY.values())}),
    ]:
        schema_path = ROOT / "content/schemas" / schema
        question_schema = json.loads((ROOT / "content/schemas/question.schema.json").read_text())
        registry = Registry().with_resource(
            "urn:uni-stem-course-simulators:schema:question:1.0",
            Resource.from_contents(question_schema),
        )
        validator = jsonschema.Draft202012Validator(json.loads(schema_path.read_text()), registry=registry)
        validator.validate(value)


def test_every_objective_has_cards_and_original_practice_provenance():
    card_objectives = {oid for card in CARDS for oid in card["objective_ids"]}
    assert card_objectives == set(OBJECTIVES)
    for card in CARDS:
        assert card["lesson_id"] in READINGS and card["license"] == "CC-BY-4.0"
    for item in BANK.values():
        assert item["visibility"] == "public-practice-authoring"
        assert item["provenance"]["kind"] == "original"
        assert "synthetic" in item["provenance"]["modifications"][0]
        assert "no external problem, code or dataset imported" in item["provenance"]["modifications"][0]


def test_all_numeric_keys_are_independently_recomputed_and_executable():
    numeric = {qid for qid, item in BANK.items() if item["type"] == "numeric"}
    assert numeric == {item_id(key) for key in NUMERIC_KEYS}
    assert len(numeric) == 24
    for key, (expected, wrong) in NUMERIC_KEYS.items():
        item = BANK[item_id(key)]
        spec = item["solution_spec"]
        assert spec["answer"] == pytest.approx(expected, abs=spec["tolerance"] + 1e-9), key
        assert (spec["unit_required"], spec["significant_figures"], spec["dimensions"]) == (False, None, None)
        assert item["prompt"].endswith("Enter the number only.")
        assert grade(item, AttemptRequest(response=str(spec["answer"]))).correct, key
        assert not grade(item, AttemptRequest(response=str(wrong))).correct, key


def test_choice_keys_and_partial_credit_are_executable():
    for qid, item in BANK.items():
        if item["type"] == "single_choice":
            accepted = [i for i in range(len(item["options"])) if grade(item, AttemptRequest(response=str(i))).correct]
            assert accepted == [item["solution_spec"]["answer"]], qid
        elif item["type"] == "multiple_select":
            key = item["solution_spec"]["answer"]
            wrong = next(i for i in range(len(item["options"])) if i not in key)
            assert item["points"] == 2
            assert grade(item, AttemptRequest(response=key)).score == pytest.approx(2)
            assert grade(item, AttemptRequest(response=[*key, wrong])).score < 2
            assert grade(item, AttemptRequest(response=[wrong])).score == 0


def test_source_registry_links_identifiers_and_prerequisite_mappings():
    expected = {
        "mit-ocw-1-74-fall-2020", "mit-ocw-1-040-spring-2004",
        "usda-nrcs-urban-agriculture-subpart-t-2024", "nasa-eclss",
        "zong-2017-plant-cbe", "zong-2017-plant-cbe-correction-2025", "jin-2019-rice-base-editor-off-target",
        "owner-rural-florida-agriculture", "owner-iran-vertical-agriculture",
        "owner-open-construction-equipment", "owner-habitat-resource-sandbox",
    }
    for sid in expected:
        source = REGISTRY[sid]
        assert source["url"].startswith("https://") and source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {"linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        expected_courses = [CID, "materials-engineering-fabrication"] if sid == "owner-open-construction-equipment" else ([CID, "chemical-process-design-scale-up"] if sid in {"owner-rural-florida-agriculture", "owner-habitat-resource-sandbox"} else [CID])
        assert source["mapped_courses"] == expected_courses and source["imported_assets"] == []
        assert source["mapped_modules"]
    assert REGISTRY["zong-2017-plant-cbe"]["version"].endswith("DOI 10.1038/nbt.3811; PMID 28244994")
    assert REGISTRY["zong-2017-plant-cbe-correction-2025"]["version"].endswith("DOI 10.1038/s41587-025-02671-3; PMID 40275090")
    assert REGISTRY["jin-2019-rice-base-editor-off-target"]["version"].endswith("DOI 10.1126/science.aaw7166; PMID 30819931")
    assert REGISTRY["owner-iran-vertical-agriculture"]["title"].endswith("iran_vertical_agriculture")
    assert REGISTRY["owner-iran-vertical-agriculture"]["url"].endswith("/iran-vertical-agriculture")
    for sid, module in [("genetics-703", 4), ("biochemistry", 4), ("mechanics", 5)]:
        assert CID in REGISTRY[sid]["mapped_courses"]
        assert f"{CID}-module-{module}" in REGISTRY[sid]["mapped_modules"]
    assert MANIFEST["prerequisites"]["recommended_course_ids"] == ["genetics", "biochemistry", "physics-mechanics"]
    mapping = json.loads((COURSE / "source-map.json").read_text())
    assert len(mapping["modules"]) == 6 and all(m["original_content"] for m in mapping["modules"])
    assert all("no source prose, figure, table, code, protocol or dataset imported" in m["modifications"][0] for m in mapping["modules"])


def test_agriculture_pathway_discovers_course():
    assert len(CURRICULUM["pathways"]) == 10
    pathway = next(p for p in CURRICULUM["pathways"] if p["id"] == "agriculture-construction-habitat-systems")
    assert pathway["id"] == "agriculture-construction-habitat-systems"
    assert CID in pathway["course_ids"]
    assert {"genetics", "biochemistry", "physics-mechanics"} <= set(pathway["course_ids"])


def test_synthetic_audit_csv_and_every_residual():
    rows = load_csv("labs/habitat-audit.csv")
    assert len(rows) == 6 and len({r["record_id"] for r in rows}) == 6
    assert all(r["data_status"] == "synthetic-original" for r in rows)
    expected = {"A01": (0, 0), "A02": (0, 0), "A03": (1.2, 2), "A04": (0, 0), "A05": (0, 0), "A06": (0, 0)}
    for row in rows:
        def value(key):
            return float(row[key])
        energy = value("grid_kwh") + value("backup_kwh") - value("lighting_kwh") - value("climate_kwh") - value("pumps_controls_kwh")
        water = value("water_start_l") + value("water_input_l") + value("water_recovered_l") - value("water_consumed_l") - value("water_end_l")
        assert (energy, water) == pytest.approx(expected[row["record_id"]], abs=1e-9)
    assert next(r for r in rows if r["record_id"] == "A04")["temperature_status"] == "missing"
    assert [r["record_id"] for r in rows if r["human_gate"] == "unresolved"] == ["A03", "A04"]
    assert sum(float(r["backup_kwh"]) for r in rows if r["record_id"] in {"A02", "A05"}) == pytest.approx(6.0)


def test_synthetic_project_csv_recomputes_all_rehearsal_rows():
    rows = load_csv("assignments/habitat-project-rehearsal.csv")
    assert len(rows) == 4 and all(r["data_status"] == "synthetic-original" for r in rows)
    expected_dli = [7.776, 11.088, 11.52, 5.76]
    expected_water = [100, 110, 92, 96]
    expected_outage = [1.0, 1.5, 1.96, 1.8]
    for index, row in enumerate(rows):
        def value(key):
            return float(row[key])
        dli = value("ppfd_umol_m2_s") * value("photoperiod_h") * 3600 / 1e6
        water = value("water_start_l") + value("water_input_l") + value("water_recovered_l") - value("water_consumed_l")
        outage = value("critical_load_kw") * value("outage_h")
        assert dli == pytest.approx(expected_dli[index], abs=1e-9)
        assert water == pytest.approx(expected_water[index], abs=1e-9)
        assert outage == pytest.approx(expected_outage[index], abs=1e-9)
        assert value("fixture_kw") * value("photoperiod_h") > 0
        assert value("predecessor_days") + value("review_days") > 0


def test_original_substantive_readings_have_explicit_honest_boundaries():
    assert len(READINGS) == 8
    for lid, text in READINGS.items():
        assert len(text.split()) >= 400, lid
        assert "synthetic" in text.lower(), lid
        assert "unreviewed" in text and "formative-only" in text, lid
    assert "DOI 10.1038/nbt.3811, PMID 28244994" in READINGS[f"{CID}-4"]
    assert "DOI 10.1038/s41587-025-02671-3, PMID 40275090" in READINGS[f"{CID}-4"]
    assert "DOI 10.1126/science.aaw7166, PMID 30819931" in READINGS[f"{CID}-4"]
    assert "not a life-support design" in READINGS[f"{CID}-6"]
    assert "do not pool" in READINGS[f"{CID}-7"].lower()
    assert "zero-point" in READINGS[f"{CID}-project-guide"]
    limitations = " ".join(MANIFEST["limitations"])
    assert "Of the 24 numerical answers, 0 require units, 0 check significant figures and 0 check dimensions." in limitations
    assert "not independent replicates" in limitations


def test_no_operational_editing_nutrient_construction_or_life_support_protocol():
    combined = "\n".join(p.read_text(encoding="utf-8") for p in COURSE.rglob("*") if p.is_file()).lower()
    forbidden = [
        r"\bsg\s*[- ]?rna\b", r"\bprotospacer\b", r"\bagrobacterium\b", r"\bcallus\b",
        r"\bpeg-mediated\b", r"\bpam\s+sequence\b", r"\bguide\s+rna\b", r"\btarget\s+sequence\b",
        r"\bediting window\b", r"\btransformation protocol\b", r"\btissue[- ]culture protocol\b",
        r"\b\d+(?:\.\d+)?\s*mg\s*/\s*l\b", r"\b\d+(?:\.\d+)?\s*mm\b",
        r"\brebar\b", r"\bformwork\b", r"\bweld(?:ing)?\b", r"\btorque\s+setting\b",
        r"\bcertified\s+habitable\b", r"\bsafe\s+for\s+human\s+occupancy\b", r"\bself-sufficient\s+habitat\b",
    ]
    assert not {pattern: re.findall(pattern, combined) for pattern in forbidden if re.search(pattern, combined)}
    assert "no guide/target design" in combined
    assert "no nutrient formulation" in combined
    assert "no real construction instructions" in combined
    assert "not independent replicates" in combined
