"""Chemical Engineering Foundations: independent numeric/CSV/model-domain checks.

All 24 base numeric answers are recomputed independently from displayed synthetic
inputs, with misconception and precision-boundary checks. Both public CSVs are
recomputed row by row. These agent-run checks are not scientific, engineering,
process-safety, operability or release review.
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
COURSE = ROOT / "content/courses/chemical-engineering-foundations"
CID = "chemical-engineering-foundations"
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
    "1:unit-scale": (2.5 * 3600, 2.5 / 3600),
    "1:outlet-total": (40 + 60, 40 + 60 - 20),
    "1:degrees-of-freedom": (3 - 2, 3 - 1),
    "2:conversion": ((80 - 20) / 80 * 100, 20 / 80 * 100),
    "2:selectivity": (36 / 60 * 100, 36 / 80 * 100),
    "2:overall-yield": (36 / 80 * 100, 36 / 60 * 100),
    "3:energy-duty": (5 * 2 * (20 - 8), 5 * 2 * (20 + 8)),
    "3:flash-vapor-fraction": ((0.9 - 0.24) / (0.54 + 0.36), 0.6),
    "3:flash-vapor-composition": (2.5 * (0.6 / (1 + (11 / 15) * 1.5)), 0.6 / (1 + (11 / 15) * 1.5)),
    "4:continuity-speed": (0.020 / 0.005, 0.020 * 0.005),
    "4:friction-head": (0.020 * 100 * 2**2 / (2 * 10), 0.020 * 100 * 2**2),
    "4:lmtd": ((40 - 20) / math.log(40 / 20), (40 + 20) / 2),
    "5:batch-conversion": (1 - math.exp(-0.2 * 10), math.exp(-0.2 * 10)),
    "5:cstr-conversion": (0.2 * 5 / (1 + 0.2 * 5), 1 - math.exp(-0.2 * 5)),
    "5:pfr-conversion": (1 - math.exp(-0.2 * 5), 0.2 * 5 / (1 + 0.2 * 5)),
    "6:a-recovery": (80 / 100 * 100, (100 - 80) / 100 * 100),
    "6:product-purity": (80 / (80 + 15 + 5) * 100, 80 / (80 + 15) * 100),
    "6:extraction-fraction": (3 * 2 / (1 + 3 * 2) * 100, 1 / (1 + 3 * 2) * 100),
    "7:lab01-product-a": (20 + 18, 41),
    "7:lab02-total-residual": (102 - 100, 102),
    "7:lab03-product-b": (12 + 35, 13),
    "8:r01-recovered-b": (42 * 0.90, 42 * (1 - 0.90)),
    "8:r02-selectivity": (48 / (48 + 24) * 100, 48 / 120 * 100),
    "8:r03-overall-yield": (24 / 90 * 100, 30 / 90 * 100),
}

DISPLAY_FRAGMENTS = {
    "3:flash-vapor-fraction": "0.7333333",
    "3:flash-vapor-composition": "0.7142857",
    "4:lmtd": "28.8539008",
    "5:batch-conversion": "0.8646647",
    "5:pfr-conversion": "0.6321206",
    "6:extraction-fraction": "85.7142857",
    "8:r02-selectivity": "66.6666667",
    "8:r03-overall-yield": "26.6666667",
}


def test_structure_assessment_links_and_generated_schemas():
    assert (MANIFEST["title"], MANIFEST["version"]) == ("Chemical Engineering Foundations", "0.1.0")
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"]) == ("partial", "unreviewed")
    assert MANIFEST["license"] == "CC-BY-4.0" and MANIFEST["content_origin"]["kind"] == "original"
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert "explicitly partial university-level survey" in MANIFEST["description"]
    assert MANIFEST["prerequisites"]["course_ids"] == ["general-chemistry-2", "calculus-2"]
    assert MANIFEST["prerequisites"]["recommended_course_ids"] == ["transport", "statistics", "lab-measurement"]
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
    question_schema = json.loads((ROOT / "content/schemas/question.schema.json").read_text())
    registry = Registry().with_resource("urn:uni-stem-course-simulators:schema:question:1.0", Resource.from_contents(question_schema))
    for schema, value in [
        ("course.schema.json", MANIFEST),
        ("question-bank.schema.json", {"schema_version": "1.0", "course_id": CID, "license": "CC-BY-4.0", "questions": list(BANK.values())}),
        ("curriculum-map.schema.json", CURRICULUM),
        ("source.schema.json", {"schema_version": "1.0", "sources": list(REGISTRY.values())}),
    ]:
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


def test_choice_keys_partial_credit_and_grader_misconceptions_are_executable():
    for qid, item in BANK.items():
        if item["type"] == "single_choice":
            accepted = [i for i in range(len(item["options"])) if grade(item, AttemptRequest(response=str(i))).correct]
            assert accepted == [item["solution_spec"]["answer"]], qid
            wrong = next(i for i in range(len(item["options"])) if i != item["solution_spec"]["answer"])
            assert not grade(item, AttemptRequest(response=str(wrong))).correct
        elif item["type"] == "multiple_select":
            key = item["solution_spec"]["answer"]
            wrong = next(i for i in range(len(item["options"])) if i not in key)
            assert item["points"] == 2
            assert grade(item, AttemptRequest(response=key)).score == pytest.approx(2)
            assert grade(item, AttemptRequest(response=[*key, wrong])).score < 2
            assert grade(item, AttemptRequest(response=[wrong])).score == 0


def test_comparator_and_reused_source_mappings_preserve_old_links():
    expected = {
        "mit-ocw-10-302-fall-2004-syllabus": "https://ocw.mit.edu/courses/10-302-transport-processes-fall-2004/pages/syllabus/",
        "mit-ocw-10-40-fall-2003-syllabus": "https://ocw.mit.edu/courses/10-40-chemical-engineering-thermodynamics-fall-2003/pages/syllabus/",
        "mit-ocw-10-37-spring-2007-syllabus": "https://ocw.mit.edu/courses/10-37-chemical-and-biological-reaction-engineering-spring-2007/pages/syllabus/",
        "mit-ocw-10-32-spring-2005-syllabus": "https://ocw.mit.edu/courses/10-32-separation-processes-spring-2005/pages/syllabus/",
    }
    for sid, url in expected.items():
        source = REGISTRY[sid]
        assert source["url"] == url and source["reuse_mode"] == "link-only-comparator"
        assert source["permissions"] == {"linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        expected_courses = [CID, "chemical-process-design-scale-up"] if sid == "mit-ocw-10-302-fall-2004-syllabus" else [CID]
        assert source["mapped_courses"] == expected_courses and source["imported_assets"] == []
        assert source["accessed_at"] == "2026-11-26"
    assert "Fall 2003" in REGISTRY["mit-ocw-10-40-fall-2003-syllabus"]["version"]
    assert "Spring 2005" in REGISTRY["mit-ocw-10-32-spring-2005-syllabus"]["version"]
    reused = {
        "chemistry": ("general-chemistry-1", f"{CID}-module-1"),
        "transport": ("transport", f"{CID}-module-4"),
        "statistics": ("statistics", f"{CID}-module-2"),
        "control": ("signals-control", f"{CID}-module-6"),
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
    assert "Spring 2012" in crosswalk and "Fall 2005" in crosswalk and "HTTP 404" in crosswalk


def test_new_pathway_and_catalog_only_deep_nodes_remain_unpromoted():
    assert len(CURRICULUM["pathways"]) == 10 and len(CURRICULUM["catalog_only"]) == 36
    catalog = {node["id"]: node for node in CURRICULUM["catalog_only"]}
    for node_id in ("thermodynamics", "fluid-mechanics", "heat-mass-transfer"):
        assert catalog[node_id]["maturity"] == "catalog-only"
    pathway = next(p for p in CURRICULUM["pathways"] if p["id"] == "chemical-process-engineering")
    assert pathway["course_ids"] == ["calculus-1", "calculus-2", "general-chemistry-1", "general-chemistry-2", "statistics", "transport", "lab-measurement", CID, "chemical-process-design-scale-up"]
    assert len(pathway["course_ids"]) >= 6
    assert not {"thermodynamics", "fluid-mechanics", "heat-mass-transfer"} & set(pathway["course_ids"])


def test_synthetic_reconciliation_csv_recomputes_every_conservation_relation():
    rows = load_csv("labs/process-reconciliation.csv")
    assert len(rows) == 9 and len({r["stream_id"] for r in rows}) == 9
    assert all(r["data_status"] == "synthetic-original" for r in rows)
    assert all(r["record_relation"] == "correlated-within-scenario-not-independent-replicate" for r in rows)
    for row in rows:
        total = float(row["reconciled_total_kg_h"])
        components = [float(row[f"reconciled_{species}_kg_h"]) for species in ("A", "B", "S")]
        assert sum(components) == pytest.approx(total, abs=1e-12)
        assert total >= 0 and all(value >= 0 for value in components)
        for species in ("total", "A", "B", "S"):
            measured = row[f"measured_{species}_kg_h"]
            if measured == "":
                assert "unknown" in row["evidence_status"]
    for scenario in ("LAB-01", "LAB-02", "LAB-03"):
        group = [r for r in rows if r["scenario_id"] == scenario]
        feeds = [r for r in group if r["stream_role"].startswith("feed")]
        product = next(r for r in group if r["stream_role"] == "product")
        assert len(feeds) == 2
        for species in ("total", "A", "B", "S"):
            key = f"reconciled_{species}_kg_h"
            assert sum(float(r[key]) for r in feeds) == pytest.approx(float(product[key]), abs=1e-12)
    lab01 = next(r for r in rows if r["stream_id"] == "LAB-01-product")
    assert float(lab01["reconciled_A_kg_h"]) == NUMERIC_KEYS["7:lab01-product-a"][0]
    assert float(lab01["measured_A_kg_h"]) == 41
    lab02 = next(r for r in rows if r["stream_id"] == "LAB-02-product")
    assert float(lab02["measured_total_kg_h"]) - float(lab02["reconciled_total_kg_h"]) == NUMERIC_KEYS["7:lab02-total-residual"][0]
    lab03 = next(r for r in rows if r["stream_id"] == "LAB-03-product")
    assert lab03["measured_B_kg_h"] == "" and float(lab03["reconciled_B_kg_h"]) == NUMERIC_KEYS["7:lab03-product-b"][0]


def test_synthetic_rehearsal_csv_recomputes_all_closure_recovery_and_unknowns():
    rows = load_csv("assignments/flowsheet-audit-rehearsal.csv")
    assert len(rows) == 4 and all(r["data_status"] == "synthetic-original" for r in rows)
    assert all("correlated-derived-columns-not-replicates" in r["record_relation"] for r in rows)
    derived = {}
    for row in rows:
        feed, converted, unreacted = (float(row[key]) for key in ("feed_A_kg_h", "converted_A_kg_h", "unreacted_A_kg_h"))
        b_formed, s_formed = float(row["B_formed_kg_h"]), float(row["S_formed_kg_h"])
        assert feed == pytest.approx(converted + unreacted, abs=1e-12)
        assert converted == pytest.approx(b_formed + s_formed, abs=1e-12)
        if row["B_recovery_fraction"]:
            recovery = float(row["B_recovery_fraction"])
            recovered = float(row["recovered_B_kg_h"])
            assert 0 <= recovery <= 1 and recovered == pytest.approx(b_formed * recovery, abs=1e-12)
            assert 0 <= float(row["separator_B_purity_pct"]) <= 100
            derived[row["scenario_id"]] = recovered
        else:
            assert row["recovered_B_kg_h"] == row["separator_B_purity_pct"] == ""
            assert "unknown" in row["model_boundary"]
    assert derived["R01"] == pytest.approx(NUMERIC_KEYS["8:r01-recovered-b"][0], abs=1e-12)
    r02 = next(r for r in rows if r["scenario_id"] == "R02")
    assert float(r02["B_formed_kg_h"]) / (float(r02["B_formed_kg_h"]) + float(r02["S_formed_kg_h"])) * 100 == NUMERIC_KEYS["8:r02-selectivity"][0]
    r03 = next(r for r in rows if r["scenario_id"] == "R03")
    assert derived["R03"] / float(r03["feed_A_kg_h"]) * 100 == NUMERIC_KEYS["8:r03-overall-yield"][0]


def test_model_domains_invalid_flash_and_unknown_cases_are_explicit():
    flash = BANK[f"{CID}-3:flash-domain"]
    assert flash["solution_spec"]["answer"] == 1
    assert not grade(flash, AttemptRequest(response="0")).correct
    # With both synthetic K values below one, every numerator is negative and
    # every denominator positive for 0 <= V <= 1: no interior root exists.
    for index in range(101):
        vapor = index / 100
        residual = sum(z * (k - 1) / (1 + vapor * (k - 1)) for z, k in ((0.6, 0.7), (0.4, 0.5)))
        assert residual < 0
    vapor = NUMERIC_KEYS["3:flash-vapor-fraction"][0]
    assert 0 < vapor < 1
    x_a = 0.6 / (1 + vapor * (2.5 - 1))
    x_b = 0.4 / (1 + vapor * (0.4 - 1))
    y_a, y_b = 2.5 * x_a, 0.4 * x_b
    assert x_a + x_b == pytest.approx(1) and y_a + y_b == pytest.approx(1)
    assert (1 - vapor) * x_a + vapor * y_a == pytest.approx(0.6)
    unknown = BANK[f"{CID}-8:r04-unknown-recovery"]
    assert unknown["solution_spec"]["answer"] == 2
    assert not grade(unknown, AttemptRequest(response="0")).correct
    correlation = BANK[f"{CID}-4:correlation-applicability"]
    assert 2 not in correlation["solution_spec"]["answer"]
    nonisothermal = BANK[f"{CID}-5:nonisothermal-boundary"]
    assert 2 not in nonisothermal["solution_spec"]["answer"]


def test_original_substantive_readings_resources_and_honest_boundaries():
    assert len(READINGS) == 8
    for lid, text in READINGS.items():
        assert len(text.split()) >= 700, lid
        assert "synthetic" in text.lower() and "fictional" in text.lower(), lid
        assert "unreviewed" in text and "formative-only" in text, lid
    assert MANIFEST["learner_resources"] == ["labs/process-reconciliation.csv", "assignments/flowsheet-audit-rehearsal.csv"]
    assert all((COURSE / reference).is_file() for reference in MANIFEST["learner_resources"])
    assert "zero-point" in READINGS[f"{CID}-project-guide"]
    limitations = " ".join(MANIFEST["limitations"])
    assert "Of the 24 numerical answers, 0 require units, 0 check significant figures and 0 check dimensions." in limitations
    assert "No numeric question uses authored randomization variants" in limitations
    assert "Arithmetic closure is not proof of safe or feasible operation" in limitations
    assert "thermodynamics, fluid-mechanics and heat-mass-transfer" in limitations
    combined = "\n".join(READINGS.values()).lower()
    assert "correlated records, not independent replicates" in combined
    assert "blank means unknown, never zero" in combined


def test_no_real_species_operational_design_or_approval_instruction():
    combined = "\n".join(p.read_text(encoding="utf-8") for p in COURSE.rglob("*") if p.is_file()).lower()
    real_species = [r"\bwater\b", r"\bethanol\b", r"\bmethanol\b", r"\bbenzene\b", r"\bammonia\b", r"\bacetone\b"]
    forbidden = real_species + [
        r"\bset (?:the )?(?:temperature|pressure|flow|controller|valve)\b",
        r"\brelief (?:valve )?(?:set|size|sizing) (?:at|to)\b",
        r"\bpump (?:size|sizing|rating) (?:is|=)\b",
        r"\bapproved for (?:operation|production|release|service)\b",
        r"\bcertified (?:safe|compliant)\b",
        r"\bplant operating target (?:is|=)\b",
    ]
    assert not {pattern: re.findall(pattern, combined) for pattern in forbidden if re.search(pattern, combined)}
    assert "no real production recipe" in combined
    assert "arithmetic closure is not proof of safe or feasible operation" in combined
    assert "missing values remain unknown" in combined
    assert "no source prose" in combined
