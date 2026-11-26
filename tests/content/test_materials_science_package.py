"""Materials Science: independent numeric/CSV keys, sources and honest boundaries.

All 24 base numeric answers are recomputed from displayed synthetic inputs, with
independent misconception and precision-boundary checks. Every public CSV derived
relationship is recomputed row by row. These are agent-run checks, not scientific,
engineering, standards or material-approval review.
"""
from __future__ import annotations

import csv
import json
import math
import re
from pathlib import Path

import jsonschema
import pytest
from referencing import Registry, Resource

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/materials-science"
CID = "materials-science"
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


# Independent correct arithmetic and one independently derived misconception each.
NUMERIC_KEYS = {
    "1:fictional-density": (54 / 20, 20 / 54),
    "1:thermal-resistance": (0.020 / (200 * 0.005), 200 * 0.005 / 0.020),
    "1:resistivity-change": ((8 - 2) / 2 * 100, 8 / 2 * 100),
    "2:cubic-d100": (0.400 / math.sqrt(1**2 + 0**2 + 0**2), 0.400 / math.sqrt(2)),
    "2:cubic-d210": (0.400 / math.sqrt(2**2 + 1**2 + 0**2), 0.400 / math.sqrt(2 + 1 + 0)),
    "2:bragg-two-theta": (2 * math.degrees(math.asin(0.154 / (2 * 0.200))), math.degrees(math.asin(0.154 / (2 * 0.200)))),
    "3:arrhenius-diffusivity": (1e-5 * math.exp(-80000 / (8.314 * 1000)), 1e-5 * math.exp(80000 / (8.314 * 1000))),
    "3:steady-diffusion-flux": (1e-10 * 0.80 / 0.0020, 1e-10 * 0.80 * 0.0020),
    "3:hall-petch": (100 + 0.50 / math.sqrt(4e-6), 100 + 0.50 * math.sqrt(4e-6)),
    "4:lever-liquid": ((40 - 20) / (60 - 20) * 100, 40 / 60 * 100),
    "4:lever-alpha": ((60 - 30) / (60 - 20) * 100, 30 / 60 * 100),
    "4:avrami-fraction": ((1 - math.exp(-0.020 * 10**2)) * 100, math.exp(-0.020 * 10**2) * 100),
    "5:toughness-area": (0.5 * 200 * 0.010 + 200 * (0.030 - 0.010), 200 * (0.030 - 0.010)),
    "5:miner-fatigue": (20000 / 100000 + 300000 / 1000000, (20000 + 300000) / 1000000),
    "5:stress-intensity": (1.12 * 150 * math.sqrt(math.pi * 0.0020), 1.12 * 150 * math.pi * 0.0020),
    "6:polymer-mn": ((10 * 20 + 20 * 40 + 10 * 80) / (10 + 20 + 10), 10 * 20 + 20 * 40 + 10 * 80),
    "6:polymer-mw": ((10 * 20**2 + 20 * 40**2 + 10 * 80**2) / (10 * 20 + 20 * 40 + 10 * 80), 44),
    "6:polymer-pdi": (((10 * 20**2 + 20 * 40**2 + 10 * 80**2) / (10 * 20 + 20 * 40 + 10 * 80)) / 45, 45 / ((10 * 20**2 + 20 * 40**2 + 10 * 80**2) / (10 * 20 + 20 * 40 + 10 * 80))),
    "7:c02-bragg-spacing": (0.154 / (2 * math.sin(math.radians(40.0 / 2))), 0.154 / (2 * math.sin(math.radians(40.0)))),
    "7:c03-mass-loss": ((100.0 - 96.5) / 100.0 * 100, (100.0 - 96.5) / 96.5 * 100),
    "7:c04-cubic-lattice": (0.154 / (2 * math.sin(math.radians(44.0 / 2))) * math.sqrt(1**2 + 1**2 + 1**2), 0.154 / (2 * math.sin(math.radians(44.0 / 2)))),
    "8:r02-specific-stiffness": (120 * 10**9 / 2700, 120 / 2700),
    "8:r03-mass": (7800 * 0.0015, 7800 / 0.0015),
    "8:r04-embodied-energy": ((1450 * 0.0020) * 20, (1450 * 0.0020) / 20),
}

DISPLAY_FRAGMENTS = {
    "2:bragg-two-theta": "45.28748",
    "3:arrhenius-diffusivity": "6.62335",
    "5:stress-intensity": "13.317",
    "7:c02-bragg-spacing": "0.225133",
    "7:c04-cubic-lattice": "0.356021",
}


def test_structure_assessment_links_and_generated_schemas():
    assert (MANIFEST["title"], MANIFEST["version"]) == ("Materials Science", "0.1.0")
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"]) == ("partial", "unreviewed")
    assert MANIFEST["license"] == "CC-BY-4.0" and MANIFEST["content_origin"]["kind"] == "original"
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert "partial foundational university survey" in MANIFEST["description"]
    assert MANIFEST["prerequisites"]["course_ids"] == ["general-chemistry-1"]
    assert MANIFEST["prerequisites"]["recommended_course_ids"] == ["physics-mechanics", "calculus-1"]
    assert len(MANIFEST["outcomes"]) == 8 and len(OBJECTIVES) == 24
    assert len(MANIFEST["modules"]) == 6 and len(LESSONS) == 8
    assert [len(m["lessons"]) for m in MANIFEST["modules"]] == [1, 1, 1, 1, 1, 3]
    assert len(BANK) == 48 and len(CARDS) == 24 and len(CASES) == 6
    assert sum(q["points"] for q in BANK.values()) == 56
    assert len([case for case in CASES if ":project-m" in case["id"]]) == 5
    assert all(case["mode"] == "self-assessment" for case in CASES)
    assert all(criterion["points"] == 0 for case in CASES for criterion in case["rubric"])
    assert len({criterion["id"] for case in CASES for criterion in case["rubric"]}) == sum(len(case["rubric"]) for case in CASES)
    scheduled = [lid for week in MANIFEST["duration"]["weeks"] for lid in week["lesson_ids"]]
    assert sorted(scheduled) == sorted(lesson["id"] for lesson in LESSONS)
    for number, lesson in enumerate(LESSONS, start=1):
        assert lesson["id"] == (f"{CID}-project-guide" if number == 8 else f"{CID}-{number}")
        assert len(lesson["objectives"]) == 3 and len(lesson["question_ids"]) == 6 and len(lesson["card_ids"]) == 3
        aid = f"{CID}-{number}-practice" if number < 8 else f"{CID}-project-rehearsal-practice"
        assessment = next(a for a in MANIFEST["assessments"] if a["id"] == aid)
        assert assessment["mode"] == "practice" and assessment["points"] == 7
        assert set(assessment["question_ids"]) == set(lesson["question_ids"])
        assert set(assessment["objective_ids"]) == {*lesson["objectives"], f"{CID}-outcome-{number}"}
    mapped = {oid for a in MANIFEST["assessments"] for oid in a["objective_ids"]}
    assert set(OBJECTIVES) <= mapped and OUTCOMES <= mapped
    assert {oid for q in BANK.values() for oid in q["objective_ids"]} == set(OBJECTIVES)
    for case in CASES:
        assert set(case["objective_ids"]) <= set(OBJECTIVES)
        assert len(case["rubric"]) >= 3
    project = next(a for a in MANIFEST["assessments"] if a["type"] == "project")
    assert (project["points"], project["mode"], project["question_ids"]) == (0, "self-assessment", [])
    for schema, value in [
        ("course.schema.json", MANIFEST),
        ("question-bank.schema.json", {"schema_version": "1.0", "course_id": CID, "license": "CC-BY-4.0", "questions": list(BANK.values())}),
        ("curriculum-map.schema.json", CURRICULUM),
        ("source.schema.json", {"schema_version": "1.0", "sources": list(REGISTRY.values())}),
    ]:
        question_schema = json.loads((ROOT / "content/schemas/question.schema.json").read_text())
        registry = Registry().with_resource("urn:uni-stem-course-simulators:schema:question:1.0", Resource.from_contents(question_schema))
        validator = jsonschema.Draft202012Validator(json.loads((ROOT / "content/schemas" / schema).read_text()), registry=registry)
        validator.validate(value)


def test_every_objective_has_cards_and_original_practice_provenance():
    assert {oid for card in CARDS for oid in card["objective_ids"]} == set(OBJECTIVES)
    for card in CARDS:
        assert card["lesson_id"] in READINGS and card["license"] == "CC-BY-4.0"
    for item in BANK.values():
        assert item["visibility"] == "public-practice-authoring"
        assert item["provenance"]["kind"] == "original"
        assert "synthetic" in item["provenance"]["modifications"][0]
        assert "no external problem, code or dataset imported" in item["provenance"]["modifications"][0]
        assert set(item["feedback"]["lesson_ids"]) <= set(READINGS)


def test_all_numeric_keys_precision_and_misconceptions_are_executable():
    numeric = {qid for qid, item in BANK.items() if item["type"] == "numeric"}
    assert numeric == {item_id(key) for key in NUMERIC_KEYS}
    assert len(numeric) == 24
    for key, (expected, wrong) in NUMERIC_KEYS.items():
        item = BANK[item_id(key)]
        spec = item["solution_spec"]
        assert spec["answer"] == pytest.approx(expected, abs=spec["tolerance"] + 1e-12), key
        assert spec["tolerance"] > 0
        assert (spec["unit_required"], spec["significant_figures"], spec["dimensions"]) == (False, None, None)
        assert item["prompt"].endswith("Enter the number only.")
        if key in DISPLAY_FRAGMENTS:
            assert DISPLAY_FRAGMENTS[key] in item["feedback"]["solution"]
        assert "randomization" not in item
        assert grade(item, AttemptRequest(response=str(spec["answer"]))).correct, key
        assert not grade(item, AttemptRequest(response=str(wrong))).correct, key
        assert not grade(item, AttemptRequest(response=str(spec["answer"] + 2 * spec["tolerance"]))).correct, key


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


def test_comparator_and_reused_source_mappings_preserve_old_links():
    expected = {
        "mit-ocw-3-091sc-fall-2010-syllabus": "https://ocw.mit.edu/courses/3-091sc-introduction-to-solid-state-chemistry-fall-2010/pages/syllabus/",
        "mit-ocw-3-012-fall-2005-calendar": "https://ocw.mit.edu/courses/3-012-fundamentals-of-materials-science-fall-2005/pages/calendar/",
    }
    for sid, url in expected.items():
        source = REGISTRY[sid]
        assert source["url"] == url and source["reuse_mode"] == "link-only-comparator"
        assert source["permissions"] == {"linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        assert source["mapped_courses"] == [CID, "materials-engineering-fabrication"] and source["imported_assets"] == []
        assert source["accessed_at"] == "2026-11-26"
    reused = {
        "chemistry": ("general-chemistry-1", f"{CID}-module-1"),
        "mechanics": ("physics-mechanics", f"{CID}-module-5"),
        "biomaterials-materials-3-051j": ("biomaterials", f"{CID}-module-6"),
    }
    for sid, (old_course, new_module) in reused.items():
        source = REGISTRY[sid]
        assert old_course in source["mapped_courses"] and CID in source["mapped_courses"]
        assert new_module in source["mapped_modules"]
    mapping = json.loads((COURSE / "source-map.json").read_text())
    assert len(mapping["modules"]) == 6 and all(m["original_content"] for m in mapping["modules"])
    for module in mapping["modules"]:
        assert (COURSE / module["reading"]).is_file()
        assert set(module["source_ids"]) <= set(REGISTRY)
        assert "no source prose, figure, table, code, protocol, problem or dataset imported" in module["modifications"][0]
    crosswalk = (COURSE / "scope-crosswalk.md").read_text()
    for url in expected.values():
        assert url in crosswalk
    assert "Absent/deferred" in crosswalk and "Shallow" in crosswalk


def test_catalog_promotion_and_existing_pathways_without_pathway_growth():
    assert len(CURRICULUM["pathways"]) == 10
    assert len(CURRICULUM["catalog_only"]) == 36
    assert "materials-science" not in {node["id"] for node in CURRICULUM["catalog_only"]}
    assert sum(node["id"] == CID for node in CURRICULUM["catalog_only"]) == 0
    by_path = {p["id"]: p["course_ids"] for p in CURRICULUM["pathways"]}
    for pathway in ("science-mathematics-foundation", "mechanical-engineering-robotics", "biomedical-engineering"):
        assert CID in by_path[pathway]


def test_synthetic_characterization_csv_recomputes_every_row():
    rows = load_csv("labs/materials-characterization.csv")
    assert len(rows) == 6 and len({r["record_id"] for r in rows}) == 6
    assert all(r["data_status"] == "synthetic-original" for r in rows)
    assert all(r["fictional_material"] for r in rows)
    derived = {}
    for row in rows:
        h, k, l_index = (int(row[key]) for key in ("h", "k", "l"))
        theta = math.radians(float(row["two_theta_deg"]) / 2)
        d = float(row["wavelength_nm"]) / (2 * math.sin(theta))
        a = d * math.sqrt(h**2 + k**2 + l_index**2)
        loss = (float(row["mass_start_mg"]) - float(row["mass_end_mg"])) / float(row["mass_start_mg"]) * 100
        assert d > 0 and a >= d and loss >= 0
        derived[row["record_id"]] = (d, a, loss)
    assert derived["C02"][0] == pytest.approx(NUMERIC_KEYS["7:c02-bragg-spacing"][0], abs=1e-12)
    assert derived["C03"][2] == pytest.approx(3.5, abs=1e-12)
    assert derived["C04"][1] == pytest.approx(NUMERIC_KEYS["7:c04-cubic-lattice"][0], abs=1e-12)
    c05 = next(r for r in rows if r["record_id"] == "C05")
    assert c05["thermal_event_c"] == "" and c05["evidence_status"] == "thermal-event-unknown"
    for row in rows:
        if row["record_id"] != "C05":
            assert row["thermal_event_c"]


def test_synthetic_selection_csv_recomputes_all_relationships_and_constraints():
    rows = load_csv("assignments/material-selection-rehearsal.csv")
    assert len(rows) == 4 and all(r["data_status"] == "synthetic-original" for r in rows)
    derived = {}
    eligible = []
    for row in rows:
        rho, modulus = float(row["density_kg_m3"]), float(row["modulus_gpa"])
        volume = float(row["volume_m3"])
        mass = rho * volume
        specific = modulus * 10**9 / rho
        energy = mass * float(row["embodied_energy_mj_kg"])
        derived[row["candidate_id"]] = (specific, mass, energy)
        passes = (
            modulus >= 50 and float(row["yield_mpa"]) >= 150
            and float(row["max_temperature_c"]) >= 120
            and int(row["corrosion_evidence_score"]) >= 3
            and int(row["cost_index"]) <= 8
        )
        if passes:
            eligible.append(row["candidate_id"])
    assert eligible == ["R02", "R04"]
    assert derived["R02"][0] == pytest.approx(NUMERIC_KEYS["8:r02-specific-stiffness"][0], abs=1e-6)
    assert derived["R03"][1] == pytest.approx(11.7, abs=1e-12)
    assert derived["R04"][2] == pytest.approx(58, abs=1e-12)
    assert derived["R02"][0] > derived["R04"][0]
    assert derived["R04"][1] < derived["R02"][1] and derived["R04"][2] < derived["R02"][2]


def test_original_substantive_readings_resources_and_honest_boundaries():
    assert len(READINGS) == 8
    for lid, text in READINGS.items():
        assert len(text.split()) >= 600, lid
        assert "synthetic" in text.lower() and "fictional" in text.lower(), lid
        assert "unreviewed" in text and "formative-only" in text, lid
    for number in range(1, 7):
        assert len(READINGS[f"{CID}-{number}"].split()) >= 800
    assert MANIFEST["learner_resources"] == ["labs/materials-characterization.csv", "assignments/material-selection-rehearsal.csv"]
    assert all((COURSE / reference).is_file() for reference in MANIFEST["learner_resources"])
    assert "do not" in READINGS[f"{CID}-7"].lower() or "no instrument" in READINGS[f"{CID}-7"].lower()
    assert "zero-point" in READINGS[f"{CID}-project-guide"]
    limitations = " ".join(MANIFEST["limitations"])
    assert "Of the 24 numerical answers, 0 require units, 0 check significant figures and 0 check dimensions." in limitations
    assert "No numeric question uses authored randomization variants" in limitations
    assert "Statics & Mechanics of Materials" in limitations


def test_no_operational_recipe_fabrication_compliance_or_approval_instruction():
    combined = "\n".join(p.read_text(encoding="utf-8") for p in COURSE.rglob("*") if p.is_file()).lower()
    forbidden = [
        r"\bASTM\s*[A-Z]", r"\bISO\s*\d{3,}", r"\bset (?:the )?(?:voltage|current|scan rate)\b",
        r"\bheat (?:at|to) \d+\s*°?c\b", r"\bquench (?:at|in) \d+", r"\bhold (?:at|for) \d+\s*(?:h|min)",
        r"\bapproved for (?:service|flight|implant|construction)\b", r"\bcertified (?:safe|compliant)\b",
        r"\bfatigue life (?:is|equals) \d+\s+cycles\b",
    ]
    assert not {pattern: re.findall(pattern, combined) for pattern in forbidden if re.search(pattern, combined)}
    assert "no instrument operating procedure" in combined
    assert "no heat-treatment recipe" in combined
    assert "standard-specific compliance" in combined
    assert "missing evidence remains unknown" in combined
