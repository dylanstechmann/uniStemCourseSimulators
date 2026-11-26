"""Independent checks for Chemical Process Design & Scale-Up.

All 24 base numeric answers and 24 authored variants are recomputed from first
principles, with misconception, domain and tolerance-boundary checks. Both
public CSVs are recomputed row by row, including G0–G7 fail-closed evidence
states. Agent-run checks are not engineering, safety, inspection, statistical,
quality, regulatory, validation or release review.
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
from courselab.variants import resolve_variant

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/chemical-process-design-scale-up"
CID = "chemical-process-design-scale-up"
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


def annuity(cash, rate, years):
    return cash * (1 - (1 + rate) ** (-years)) / rate


def lag_one(values):
    mean = math.fsum(values) / len(values)
    centered = [value - mean for value in values]
    return math.fsum(a * b for a, b in zip(centered, centered[1:])) / math.fsum(v * v for v in centered)


# (base expected, base misconception, variant expected, variant misconception).
# Formulas are independent of the authoring script and solution strings.
NUMERIC_FORMS = {
    "1:heat-recovery": (min(120 * 4, 90 * 5), max(120 * 4, 90 * 5), min(150 * 3, 80 * 6), max(150 * 3, 80 * 6)),
    "1:scenario-npv": (-1000 + annuity(300, 0.08, 4), -1000 + 300 * 4, -1200 + annuity(360, 0.10, 5), -1200 + 360 * 5),
    "1:lifecycle-emissions": (120 * 8 + 300 * 0.5 - 40, 120 * 8 + 300 * 0.5, 150 * 6 + 400 * 0.25 - 60, 150 * 6 + 400 * 0.25),
    "2:wetted-coverage": (9 / 12 * 100, 3 / 12 * 100, 14 / 16 * 100, 2 / 16 * 100),
    "2:fatigue-sum": (2000 / 10000 + 500 / 2500, 2000 / 10000 - 500 / 2500, 1200 / 8000 + 900 / 3000, 1200 / 8000 - 900 / 3000),
    "2:inspection-closure": (6 / 10 * 100, 4 / 10 * 100, 8 / 16 * 100, 8 / 8 * 100),
    "3:fopdt-gain": ((18 - 12) / (8 - 5), (18 - 12) * (8 - 5), (25 - 19) / (10 - 7), (25 - 19) * (10 - 7)),
    "3:lag-one-autocorrelation": (-3 / 4, 3 / 4, 0, 1),
    "3:saturated-command": (min(40, max(0, 20 + 3 * (9 - 4))), 20 + 3 * (9 - 4) + 10, min(50, max(0, 25 + 4 * 12 - 4 * 5)), 25 + 4 * (12 - 5)),
    "4:bowtie-at-least-one-fails": (1 - (1 - 0.10) * (1 - 0.20), 0.10 * 0.20, 1 - (1 - 0.10) * (1 - 0.25), 0.10 * 0.25),
    "4:lopa-product": (0.20 * 0.10 * 0.05, 0.20 + 0.10 + 0.05, 0.25 * 0.10 * 0.02, 0.25 + 0.10 + 0.02),
    "4:rpn": (6 * 4 * 3, 6 + 4 + 3, 8 * 3 * 5, 8 + 3 + 5),
    "5:scale-power-ratio": (3**2, 3**3, 2.5**2, 2.5**3),
    "5:area-volume-ratio": (1 / 4, 4, 1 / 2, 2),
    "5:damkohler": (0.3 * 8, 0.3 / 8, 0.25 * 12, 0.25 / 12),
    "6:gate-coverage": (6 / 8 * 100, 2 / 8 * 100, 7 / 8 * 100, 1 / 8 * 100),
    "6:residual-rms": (
        math.sqrt((0.2**2 + (-0.1)**2 + 0.1**2) / 3),
        math.sqrt((0.2**2 + (-0.1)**2 + 0.1**2) / 2),
        math.sqrt((0.3**2 + (-0.2)**2 + 0.1**2 + 0**2) / 4),
        math.sqrt((0.3**2 + (-0.2)**2 + 0.1**2 + 0**2) / 3),
    ),
    "6:verified-capa": (8 / 10 * 100, 2 / 10 * 100, 9 / 15 * 100, 6 / 15 * 100),
    "7:l02-npv": (-800 + annuity(250, 0.10, 4), -800 + 250 * 4, -900 + annuity(300, 0.08, 4), -900 + 300 * 4),
    "7:l04-autocorrelation": (1 / 4, -1 / 4, -3 / 4, 3 / 4),
    "7:l06-scale-power": (2**2, 2**3, 1.5**2, 1.5**3),
    "8:r02-npv": (-600 + annuity(200, 0.10, 3), -600 + 200 * 3, -750 + annuity(250, 0.08, 4), -750 + 250 * 4),
    "8:r05-lifecycle": (200 * 5 + 100 * 0.2 - 30, 200 * 5 + 100 * 0.2, 240 * 4 + 80 * 0.25 - 20, 240 * 4 + 80 * 0.25),
    "8:r06-verified-capa": (8 / 10 * 100, 2 / 10 * 100, 9 / 15 * 100, 6 / 15 * 100),
}


def test_structure_assessment_links_and_generated_schemas():
    assert (MANIFEST["title"], MANIFEST["version"]) == ("Chemical Process Design & Scale-Up", "0.1.0")
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"]) == ("partial", "unreviewed")
    assert MANIFEST["license"] == "CC-BY-4.0" and MANIFEST["content_origin"]["kind"] == "original"
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert "explicitly partial advanced university/industry survey" in MANIFEST["description"]
    assert MANIFEST["prerequisites"]["course_ids"] == ["chemical-engineering-foundations", "signals-control"]
    assert MANIFEST["prerequisites"]["recommended_course_ids"] == ["materials-engineering-fabrication", "statistics", "lab-biosafety"]
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


def test_all_base_and_variant_numeric_keys_misconceptions_and_precision_boundaries():
    numeric = {qid for qid, item in BANK.items() if item["type"] == "numeric"}
    assert numeric == {item_id(key) for key in NUMERIC_FORMS}
    assert len(numeric) == 24
    for key, (base_answer, base_wrong, variant_answer, variant_wrong) in NUMERIC_FORMS.items():
        item = BANK[item_id(key)]
        forms = [("base", base_answer, base_wrong), ("alternate-1", variant_answer, variant_wrong)]
        assert item["randomization"]["seeded"] is True
        assert item["randomization"]["generator_id"] == "authored-variants-v1"
        assert len(item["randomization"]["variants"]) == 1
        for variant_id, expected, wrong in forms:
            resolved = resolve_variant(item, variant_id)
            spec = resolved["solution_spec"]
            assert spec["answer"] == pytest.approx(expected, abs=spec["tolerance"] + 1e-12), (key, variant_id)
            assert spec["tolerance"] > 0
            assert (spec["unit_required"], spec["significant_figures"], spec["dimensions"]) == (False, None, None)
            assert resolved["prompt"].endswith("Enter the number only.")
            assert grade(resolved, AttemptRequest(response=str(spec["answer"]))).correct, (key, variant_id)
            assert not grade(resolved, AttemptRequest(response=str(wrong))).correct, (key, variant_id)
            assert not grade(resolved, AttemptRequest(response=str(spec["answer"] + 2 * spec["tolerance"]))).correct
            assert not grade(resolved, AttemptRequest(response=str(spec["answer"] - 2 * spec["tolerance"]))).correct


def test_choice_keys_partial_credit_and_grader_misconceptions_are_executable():
    for qid, item in BANK.items():
        if item["type"] == "single_choice":
            accepted = [i for i in range(len(item["options"])) if grade(item, AttemptRequest(response=str(i))).correct]
            assert accepted == [item["solution_spec"]["answer"]], qid
            for wrong in range(len(item["options"])):
                if wrong != item["solution_spec"]["answer"]:
                    assert not grade(item, AttemptRequest(response=str(wrong))).correct, (qid, wrong)
        elif item["type"] == "multiple_select":
            key = item["solution_spec"]["answer"]
            wrong = next(i for i in range(len(item["options"])) if i not in key)
            assert item["points"] == 2
            assert grade(item, AttemptRequest(response=key)).score == pytest.approx(2)
            assert grade(item, AttemptRequest(response=[*key, wrong])).score < 2
            assert grade(item, AttemptRequest(response=[wrong])).score == 0
    lopa = BANK[f"{CID}-4:lopa-limits"]
    assert lopa["options"][lopa["solution_spec"]["answer"]].startswith("Report only")
    saturated = resolve_variant(BANK[f"{CID}-3:saturated-command"], "alternate-1")
    assert saturated["solution_spec"]["answer"] == 50
    assert not grade(saturated, AttemptRequest(response="53")).correct


def test_verified_comparator_reused_owner_case_and_resource_links():
    expected = {
        "mit-ocw-10-490-fall-2006-syllabus": "https://ocw.mit.edu/courses/10-490-integrated-chemical-engineering-i-fall-2006/pages/syllabus/",
        "mit-ocw-10-491-spring-2006-syllabus": "https://ocw.mit.edu/courses/10-491-integrated-chemical-engineering-ii-spring-2006/pages/syllabus/",
        "osha-29cfr1910-119-public": "https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.119",
        "nist-sematech-process-monitoring-control": "https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm",
        "asme-bpvc-viii-1-public-catalog": "https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-bpvc-section-viii-rules-construction-pressure-vessels-division-1",
        "fda-2011-process-validation": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/process-validation-general-principles-and-practices",
    }
    for sid, url in expected.items():
        source = REGISTRY[sid]
        assert source["url"] == url and source["reuse_mode"] in {"link-only-comparator", "link-only-reference"}
        assert source["permissions"] == {"linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        assert CID in source["mapped_courses"] and source["imported_assets"] == []
        assert source["accessed_at"] == "2026-11-26"
    assert "Fall 2006" in REGISTRY["mit-ocw-10-490-fall-2006-syllabus"]["version"]
    assert "HTTP 404" in REGISTRY["mit-ocw-10-490-fall-2006-syllabus"]["version"]
    assert "Spring 2006" in REGISTRY["mit-ocw-10-491-spring-2006-syllabus"]["version"]
    assert "2025" in REGISTRY["asme-bpvc-viii-1-public-catalog"]["version"]
    assert "January 2011" in REGISTRY["fda-2011-process-validation"]["version"]
    reused = {
        "control": ("signals-control", f"{CID}-module-3"),
        "statistics": ("statistics", f"{CID}-module-5"),
        "mit-ocw-10-302-fall-2004-syllabus": ("chemical-engineering-foundations", f"{CID}-module-5"),
        "mit-ocw-3-032-fall-2007-syllabus": ("materials-engineering-fabrication", f"{CID}-module-2"),
        "mechanics": ("statics-materials", f"{CID}-module-2"),
        "osha-29cfr1910-1450-laboratory-standard": ("lab-biosafety", f"{CID}-module-4"),
    }
    for sid, (old_course, new_module) in reused.items():
        source = REGISTRY[sid]
        assert old_course in source["mapped_courses"] and CID in source["mapped_courses"]
        assert new_module in source["mapped_modules"]
    for sid, repo in [
        ("owner-open-perfusion-rig", "open-perfusion-rig"),
        ("owner-perfusion-calibration-lab", "perfusion-calibration-lab"),
        ("owner-habitat-resource-sandbox", "habitat-resource-sandbox"),
        ("owner-rural-florida-agriculture", "rural-florida-agriculture"),
    ]:
        source = REGISTRY[sid]
        assert source["url"] == f"https://github.com/dylanstechmann/{repo}"
        assert CID in source["mapped_courses"] and source["imported_assets"] == []
    mapping = json.loads((COURSE / "source-map.json").read_text())
    assert len(mapping["modules"]) == 6 and all(m["original_content"] for m in mapping["modules"])
    for module in mapping["modules"]:
        assert (COURSE / module["reading"]).is_file()
        assert set(module["source_ids"]) <= set(REGISTRY)
        assert "no source prose" in module["modifications"][0]
    crosswalk = (COURSE / "scope-crosswalk.md").read_text()
    for url in expected.values():
        assert url in crosswalk
    assert "Absent/deferred" in crosswalk and "Shallow" in crosswalk and "HTTP 404" in crosswalk
    assert MANIFEST["learner_resources"] == ["labs/process-design-evidence.csv", "assignments/industry-design-review-rehearsal.csv"]
    for reference in MANIFEST["learner_resources"]:
        assert (COURSE / reference).is_file()
        assert any(reference in text for text in READINGS.values())
    combined_readings = "\n".join(READINGS.values())
    assert "/api/v1/courses/chemical-process-design-scale-up/resources/labs/process-design-evidence.csv" in combined_readings
    assert "/api/v1/courses/chemical-process-design-scale-up/resources/assignments/industry-design-review-rehearsal.csv" in combined_readings
    for case in CASES:
        assert "not a grade" in case["limitations"][0]
        assert case["rubric"]


def test_pathway_order_references_and_combined_graph_are_acyclic():
    assert len(CURRICULUM["pathways"]) == 10 and len(CURRICULUM["catalog_only"]) == 36
    pathway = next(p for p in CURRICULUM["pathways"] if p["id"] == "chemical-process-engineering")
    assert pathway["course_ids"][-2:] == ["chemical-engineering-foundations", CID]
    nodes = {path.parent.name: json.loads(path.read_text()) for path in (ROOT / "content/courses").glob("*/course.json")}
    nodes.update({node["id"]: node for node in CURRICULUM["catalog_only"]})
    for node in nodes.values():
        for field in ("course_ids", "recommended_course_ids", "concurrent_course_ids"):
            assert set(node["prerequisites"].get(field, [])) <= set(nodes), node["id"]
    visiting, visited = set(), set()
    def visit(node_id):
        assert node_id not in visiting, f"cycle at {node_id}"
        if node_id in visited:
            return
        visiting.add(node_id)
        for field in ("course_ids", "recommended_course_ids", "concurrent_course_ids"):
            for predecessor in nodes[node_id]["prerequisites"].get(field, []):
                visit(predecessor)
        visiting.remove(node_id)
        visited.add(node_id)
    for node_id in nodes:
        visit(node_id)
    fabrication = nodes["materials-engineering-fabrication"]["prerequisites"]
    assert CID not in fabrication["course_ids"] and CID not in fabrication["recommended_course_ids"]


def test_lab_csv_recomputes_every_numeric_row_and_fail_closed_evidence_state():
    rows = load_csv("labs/process-design-evidence.csv")
    assert len(rows) == 8 and {r["scenario_id"] for r in rows} == {f"L{i:02d}" for i in range(1, 9)}
    assert all(r["data_status"] == "synthetic-original" for r in rows)
    assert all("correlated-not-independent-replicate" in r["record_relation"] for r in rows)
    assert all("repeated-instrument-residuals-correlated-descriptive" in r["record_relation"] for r in rows)
    complete = {"complete-synthetic", "closed-verified-synthetic", "named-synthetic-roles"}
    evidence_fields = ["compatibility_all_wetted", "joint_traceability", "inspection_nde", "nonconformance", "safety_moc", "measurement_control", "acceptance_evidence", "responsible_reviewers"]
    derived = {}
    for row in rows:
        sid = row["scenario_id"]
        recovered = min(float(row["hot_capacity_kw"]) * float(row["hot_availability_factor"]), float(row["cold_demand_kw"]) * float(row["cold_demand_factor"]))
        npv = -float(row["initial_investment_cost_units"]) + annuity(float(row["annual_net_cash_cost_units"]), float(row["discount_rate"]), int(row["years"]))
        residuals = [float(row[f"residual_{i}"]) for i in range(1, 5)]
        autocorrelation = lag_one(residuals)
        diameter = float(row["diameter_ratio"])
        power_ratio, area_volume = diameter**2, 1 / diameter
        is_complete = all(row[field] in complete for field in evidence_fields)
        expected = "synthetic_review_complete" if is_complete else "evidence_gaps_remain"
        gate = "REVIEW_COMPLETE_SYNTHETIC_ONLY" if is_complete else "HOLD"
        assert (row["expected_disposition"], row["expected_gate_state"]) == (expected, gate), sid
        derived[sid] = (recovered, npv, autocorrelation, power_ratio, area_volume)
    assert derived["L01"][0] == NUMERIC_FORMS["1:heat-recovery"][0]
    assert derived["L02"][0] == NUMERIC_FORMS["1:heat-recovery"][2]
    assert derived["L02"][1] == pytest.approx(NUMERIC_FORMS["7:l02-npv"][0])
    assert derived["L05"][1] == pytest.approx(NUMERIC_FORMS["7:l02-npv"][2])
    assert derived["L04"][2] == pytest.approx(NUMERIC_FORMS["7:l04-autocorrelation"][0])
    assert derived["L07"][2] == pytest.approx(NUMERIC_FORMS["7:l04-autocorrelation"][2])
    assert derived["L06"][3] == NUMERIC_FORMS["7:l06-scale-power"][0]
    assert derived["L08"][3] == NUMERIC_FORMS["7:l06-scale-power"][2]
    assert all(row["expected_disposition"] == "evidence_gaps_remain" and row["expected_gate_state"] == "HOLD" for row in rows)
    by_id = {r["scenario_id"]: r for r in rows}
    assert by_id["L01"]["compatibility_all_wetted"] == "missing-seals-gaskets"
    assert by_id["L03"]["inspection_nde"] == "missing-coverage"
    assert by_id["L08"]["acceptance_evidence"] == "missing"


def test_rehearsal_csv_recomputes_closure_and_every_g0_g7_hold():
    rows = load_csv("assignments/industry-design-review-rehearsal.csv")
    assert len(rows) == 9 and all(r["data_status"] == "synthetic-original" for r in rows)
    assert all("correlated-descriptive-not-independent-replication" in r["record_relation"] for r in rows)
    gate_fields = ["g0_design_basis", "g1_model_verification", "g2_scale_evidence", "g3_equipment_evidence", "g4_safety_moc", "g5_measurement_control", "g6_pilot_readiness", "g7_transfer_continued_verification"]
    derived = {}
    for index, row in enumerate(rows):
        sid = row["scenario_id"]
        npv = -float(row["initial_investment_cost_units"]) + annuity(float(row["annual_net_cash_cost_units"]), float(row["discount_rate"]), int(row["years"]))
        lifecycle = float(row["upstream_inventory_units"]) * float(row["upstream_emission_factor"]) + float(row["use_inventory_units"]) * float(row["use_emission_factor"]) + float(row["end_of_life_credit_emission_units"])
        # The CSV credit is stored as a negative signed term, never silently zeroed.
        assert float(row["end_of_life_credit_emission_units"]) < 0
        capa = int(row["verified_capa_actions"]) / int(row["total_capa_actions"]) * 100
        complete = all(row[field] == "complete-synthetic" for field in gate_fields) and row["responsible_reviewers"] == "named-synthetic-roles"
        expected = "synthetic_review_complete" if complete else "evidence_gaps_remain"
        gate = "REVIEW_COMPLETE_SYNTHETIC_ONLY" if complete else "HOLD"
        assert (row["expected_disposition"], row["expected_gate_state"]) == (expected, gate), sid
        derived[sid] = (npv, lifecycle, capa)
        if index < 8:
            assert row[gate_fields[index]] in {"missing", "open"}, (sid, gate_fields[index])
            assert gate == "HOLD"
        else:
            assert sid == "R09" and complete
    assert derived["R02"][0] == pytest.approx(NUMERIC_FORMS["8:r02-npv"][0])
    assert derived["R04"][0] == pytest.approx(NUMERIC_FORMS["8:r02-npv"][2])
    assert derived["R05"][1] == NUMERIC_FORMS["8:r05-lifecycle"][0]
    assert derived["R07"][1] == NUMERIC_FORMS["8:r05-lifecycle"][2]
    assert derived["R06"][2] == NUMERIC_FORMS["8:r06-verified-capa"][0]
    assert derived["R08"][2] == NUMERIC_FORMS["8:r06-verified-capa"][2]
    assert [r["scenario_id"] for r in rows if r["expected_gate_state"] == "HOLD"] == [f"R{i:02d}" for i in range(1, 9)]
    assert [r["scenario_id"] for r in rows if r["expected_disposition"] == "synthetic_review_complete"] == ["R09"]
    assert "production_approved" not in {r["expected_disposition"] for r in rows}


def test_original_substantive_readings_cases_and_correlation_disclosures():
    assert len(READINGS) == 8
    assert len([p for p in COURSE.rglob("*") if p.is_file()]) == 17
    for lid, text in READINGS.items():
        assert len(text.split()) >= 700, lid
        assert "synthetic" in text.lower() and "fictional" in text.lower(), lid
        assert "unreviewed" in text and "formative-only" in text, lid
    for number in range(1, 7):
        assert len(READINGS[f"{CID}-{number}"].split()) >= 800
    assert "zero-point" in READINGS[f"{CID}-project-guide"]
    limitations = " ".join(MANIFEST["limitations"])
    assert "Readiness is the review objective, never an achieved claim" in limitations
    assert "24 base numerical answers and 24 authored variant numerical answers" in limitations
    assert "correlated and descriptive, not independent replication" in limitations
    assert "MIT 10.490 Fall 2005" in limitations and "Fall 2006" in limitations
    combined = "\n".join(READINGS.values()).lower()
    assert "correlated and descriptive, not independent replicates" in combined
    assert "missing evidence is unresolved, never zero or pass" in combined
    assert "g0" in combined and "g7" in combined and "hold" in combined


def test_no_real_species_operational_design_or_release_instruction():
    combined = "\n".join(p.read_text(encoding="utf-8") for p in COURSE.rglob("*") if p.is_file()).lower()
    real_species = [r"\bethanol\b", r"\bmethanol\b", r"\bbenzene\b", r"\bammonia\b", r"\bacetone\b"]
    forbidden = real_species + [
        r"\bset (?:the )?(?:temperature|pressure|flow|controller|valve)\b",
        r"\brelief (?:valve )?(?:set|size|sizing) (?:at|to)\b",
        r"\bwall thickness\s*(?:=|of)\s*\d",
        r"\bweld (?:at|with) \d+\s*(?:a|amps|v)\b",
        r"\bpressure[- ]test (?:at|to) \d",
        r"\bapproved for (?:operation|production|release|service)\b",
        r"\bcertified (?:safe|compliant|production-ready)\b",
        r"\bplant operating target (?:is|=)\b",
        r"\bproduction setpoint (?:is|=)\b",
        r"\bdownload (?:this|the) controller\b",
    ]
    assert not {pattern: re.findall(pattern, combined) for pattern in forbidden if re.search(pattern, combined)}
    assert "no real chemical identifier" in combined
    assert "lopa arithmetic cannot assign sil" in combined
    assert "missing compatibility, inspection, safety or acceptance evidence" in combined
    assert "current authoritative standards" in combined
    assert "no source prose" in combined
    for row in load_csv("assignments/industry-design-review-rehearsal.csv") + load_csv("labs/process-design-evidence.csv"):
        assert row["expected_disposition"] in {"synthetic_review_complete", "evidence_gaps_remain"}
        assert row["expected_gate_state"] in {"REVIEW_COMPLETE_SYNTHETIC_ONLY", "HOLD"}
