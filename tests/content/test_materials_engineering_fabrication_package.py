"""Independent checks for the synthetic fabrication design-review package.

All 24 base numeric answers and 24 authored variants are recomputed from first
principles, with misconception and tolerance-boundary checks. Both public CSVs
are recomputed row by row. Agent-run checks are not engineering, statistical,
metrology, standards, supplier or production-release review.
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
COURSE = ROOT / "content/courses/materials-engineering-fabrication"
CID = "materials-engineering-fabrication"
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


# (base expected, base misconception, variant expected, variant misconception).
# Every formula is independent of the authoring generator and its solution text.
NUMERIC_FORMS = {
    "1:annual-cost": (12000 + 4000 * 3, 12000 * 4000 + 3, 18000 + 6000 * 2.5, 18000 * 6000 + 2.5),
    "1:good-throughput": (min(80, 60, 100) * 0.95, max(80, 60, 100) * 0.95, min(90, 72, 110) * 0.90, max(90, 72, 110) * 0.90),
    "1:lifecycle-energy": (500 * (40 + 12 - 4), 500 * (40 - 4), 750 * (35 + 15 - 5), 750 * (35 - 5)),
    "2:property-change": ((230 - 200) / 200 * 100, 230 / 200 * 100, (207 - 180) / 180 * 100, 207 / 180 * 100),
    "2:residual-stress": (120 + (-45), 120 - (-45), 150 + (-60), 150 - (-60)),
    "2:porosity-strength": (250 * (1 - 0.04) ** 2, 250 * (1 - 0.04), 300 * (1 - 0.03) ** 2, 300 * (1 - 0.03)),
    "3:route-yield": (0.98 * 0.95 * 0.90 * 100, (0.98 + 0.95 + 0.90) / 3 * 100, 0.97 * 0.96 * 0.92 * 100, (0.97 + 0.96 + 0.92) / 3 * 100),
    "3:powder-input": (100 / 0.92, 100 * 0.92, 80 / 0.94, 80 * 0.94),
    "3:cost-crossover": ((15000 - 5000) / (8 - 5), (15000 - 5000) / (8 + 5), (18000 - 6000) / (9 - 6), (18000 - 6000) / (9 + 6)),
    "4:wc-clearance": (10.20 - 10.10, 10.20 - 10.00, 12.30 - 12.12, 12.30 - 12.00),
    "4:wc-interference": (10.16 - 10.00, 10.16 - 10.10, 20.20 - 20.02, 20.20 - 20.10),
    "4:wc-rss-difference": (
        0.02 + 0.03 + 0.04 - math.sqrt(0.02**2 + 0.03**2 + 0.04**2),
        math.sqrt(0.02**2 + 0.03**2 + 0.04**2),
        0.025 + 0.03 + 0.045 - math.sqrt(0.025**2 + 0.03**2 + 0.045**2),
        math.sqrt(0.025**2 + 0.03**2 + 0.045**2),
    ),
    "5:tolerance-resolution": (0.20 / 0.01, 0.20 * 0.01, 0.30 / 0.02, 0.30 * 0.02),
    "5:cp": ((10.2 - 9.8) / (6 * 0.05), (10.2 - 9.8) / (3 * 0.05), (20.3 - 19.8) / (6 * 0.06), (20.3 - 19.8) / (3 * 0.06)),
    "5:cpk": (
        min((10.2 - 10.1) / (3 * 0.04), (10.1 - 9.8) / (3 * 0.04)),
        (10.2 - 9.8) / (6 * 0.04),
        min((20.2 - 20.12) / (3 * 0.05), (20.12 - 19.8) / (3 * 0.05)),
        (20.2 - 19.8) / (6 * 0.05),
    ),
    "6:risk-priority": (8 * 4 * 5, 8 + 4 + 5, 9 * 3 * 6, 9 + 3 + 6),
    "6:first-articles": (18 / 24 * 100, 6 / 24 * 100, 21 / 28 * 100, 7 / 28 * 100),
    "6:verified-closure": (6 / 12 * 100, 6 / 6 * 100, 8 / 16 * 100, 8 / 8 * 100),
    "7:p03-clearance": (10.06 - 9.98, 10.06 + 9.98, 10.10 - 10.01, 10.10 + 10.01),
    "7:l02-cpk": (
        min((10.10 - 10.01) / (3 * 0.02), (10.01 - 9.90) / (3 * 0.02)),
        (10.10 - 9.90) / (6 * 0.02),
        min((10.10 - 10.04) / (3 * 0.025), (10.04 - 9.90) / (3 * 0.025)),
        (10.10 - 9.90) / (6 * 0.025),
    ),
    "7:l01-yield": (4 / 4 * 100, 4 / 8 * 100, 3 / 4 * 100, 3 / 8 * 100),
    "8:r02-wc-clearance": (10.04 - 10.00, 10.04 + 10.00, 10.15 - 10.00, 10.15 + 10.00),
    "8:r04-rss": (math.sqrt(0.01**2 + 0.02**2 + 0.02**2), 0.01 + 0.02 + 0.02, math.sqrt(0.02**2 + 0.02**2 + 0.03**2), 0.02 + 0.02 + 0.03),
    "8:r05-lot-yield": (18 / 20 * 100, 2 / 20 * 100, 22 / 25 * 100, 3 / 25 * 100),
}


def test_structure_assessment_links_and_generated_schemas():
    assert (MANIFEST["title"], MANIFEST["version"]) == ("Materials Engineering for Fabrication", "0.1.0")
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"]) == ("partial", "unreviewed")
    assert MANIFEST["license"] == "CC-BY-4.0" and MANIFEST["content_origin"]["kind"] == "original"
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert "partial advanced university/industry design-review survey" in MANIFEST["description"]
    assert MANIFEST["prerequisites"]["course_ids"] == ["materials-science", "statics-materials"]
    assert MANIFEST["prerequisites"]["recommended_course_ids"] == ["statistics", "lab-measurement", "chemical-engineering-foundations"]
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
            wrong = next(i for i in range(len(item["options"])) if i != item["solution_spec"]["answer"])
            assert not grade(item, AttemptRequest(response=str(wrong))).correct
        elif item["type"] == "multiple_select":
            key = item["solution_spec"]["answer"]
            wrong = next(i for i in range(len(item["options"])) if i not in key)
            assert item["points"] == 2
            assert grade(item, AttemptRequest(response=key)).score == pytest.approx(2)
            assert grade(item, AttemptRequest(response=[*key, wrong])).score < 2
            assert grade(item, AttemptRequest(response=[wrong])).score == 0


def test_verified_comparator_reused_and_owner_source_links():
    expected = {
        "mit-ocw-2-008-spring-2025-calendar": "https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/pages/calendar/",
        "mit-ocw-2-830j-spring-2008-calendar": "https://ocw.mit.edu/courses/2-830j-control-of-manufacturing-processes-sma-6303-spring-2008/pages/calendar/",
        "mit-ocw-3-032-fall-2007-syllabus": "https://ocw.mit.edu/courses/3-032-mechanical-behavior-of-materials-fall-2007/pages/syllabus/",
        "nist-sematech-process-monitoring-control": "https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm",
    }
    for sid, url in expected.items():
        source = REGISTRY[sid]
        assert source["url"] == url and source["reuse_mode"] in {"link-only-comparator", "link-only-reference"}
        assert source["permissions"] == {"linking": True, "quotation": False, "adaptation": False, "redistribution": False}
        expected_courses = [CID, "chemical-process-design-scale-up"] if sid in {"mit-ocw-3-032-fall-2007-syllabus", "nist-sematech-process-monitoring-control"} else [CID]
        assert source["mapped_courses"] == expected_courses and source["imported_assets"] == []
        assert source["accessed_at"] == "2026-11-26"
    reused = {
        "mit-ocw-3-091sc-fall-2010-syllabus": ("materials-science", f"{CID}-module-2"),
        "mit-ocw-3-012-fall-2005-calendar": ("materials-science", f"{CID}-module-2"),
        "mechanics": ("statics-materials", f"{CID}-module-1"),
        "statistics": ("statistics", f"{CID}-module-5"),
        "owner-open-construction-equipment": ("agriculture-construction-habitats", f"{CID}-module-6"),
    }
    for sid, (old_course, new_module) in reused.items():
        source = REGISTRY[sid]
        assert old_course in source["mapped_courses"] and CID in source["mapped_courses"]
        assert new_module in source["mapped_modules"]
    for sid, repo in [("owner-machine-cad-agent", "machine-cad-agent"), ("owner-diaper-changing-machines", "diaper-changing-machines")]:
        source = REGISTRY[sid]
        assert source["url"] == f"https://github.com/dylanstechmann/{repo}"
        expected_courses = [CID, "chemical-process-design-scale-up"] if sid in {"mit-ocw-3-032-fall-2007-syllabus", "nist-sematech-process-monitoring-control"} else [CID]
        assert source["mapped_courses"] == expected_courses and source["imported_assets"] == []
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


def test_mechanical_pathway_related_node_and_acyclic_crosslink_preserve_planning_scope():
    assert len(CURRICULUM["pathways"]) == 10 and len(CURRICULUM["catalog_only"]) == 36
    pathway = next(p for p in CURRICULUM["pathways"] if p["id"] == "mechanical-engineering-robotics")
    assert CID in pathway["course_ids"]
    node = next(n for n in CURRICULUM["catalog_only"] if n["id"] == "mechanical-design")
    assert node["maturity"] == "catalog-only"
    assert CID in node["related_package_ids"] and CID in node["prerequisites"]["recommended_course_ids"]
    assert CID not in node["prerequisites"]["course_ids"]
    assert "without consuming or completing" in node["relation_note"]
    chemical = next(n for n in (ROOT / "content/courses").glob("*/course.json") if json.loads(n.read_text())["id"] == "chemical-engineering-foundations")
    chemical_manifest = json.loads(chemical.read_text())
    assert CID not in chemical_manifest["prerequisites"]["course_ids"]
    assert CID not in chemical_manifest["prerequisites"]["recommended_course_ids"]


def test_lab_csv_recomputes_every_clearance_capability_yield_and_lot_structure():
    rows = load_csv("labs/fabrication-evidence.csv")
    assert len(rows) == 16 and len({r["part_id"] for r in rows}) == 16
    assert {r["lot_id"] for r in rows} == {"L01", "L02", "L03", "L04"}
    assert all(r["data_status"] == "synthetic-original" for r in rows)
    assert all("repeated-reading-is-not-independent-part" in r["record_relation"] for r in rows)
    clearances = {}
    for row in rows:
        clearance = float(row["hole_actual_mm"]) - float(row["shaft_actual_mm"])
        clearances[row["part_id"]] = clearance
        assert clearance > 0
        assert float(row["repeat_reading_mm"]) == pytest.approx(float(row["dimension_mm"]) + 0.005)
    assert clearances["P03"] == pytest.approx(NUMERIC_FORMS["7:p03-clearance"][0])
    assert clearances["P07"] == pytest.approx(NUMERIC_FORMS["7:p03-clearance"][2])
    yields = {}
    for lot in ("L01", "L02", "L03", "L04"):
        group = [r for r in rows if r["lot_id"] == lot]
        assert len(group) == 4
        accepted = sum(float(r["lsl_mm"]) <= float(r["dimension_mm"]) <= float(r["usl_mm"]) for r in group)
        yields[lot] = accepted / len(group) * 100
    assert yields == {"L01": 100, "L02": 100, "L03": 100, "L04": 75}
    assert yields["L01"] == NUMERIC_FORMS["7:l01-yield"][0] and yields["L04"] == NUMERIC_FORMS["7:l01-yield"][2]
    capabilities = {}
    for lot in ("L01", "L02", "L03"):
        row = next(r for r in rows if r["lot_id"] == lot)
        assert row["process_state"] == "stable-declared"
        mean, sigma = float(row["summary_mean_mm"]), float(row["within_sigma_mm"])
        lower, upper = float(row["lsl_mm"]), float(row["usl_mm"])
        cp = (upper - lower) / (6 * sigma)
        cpk = min((upper - mean) / (3 * sigma), (mean - lower) / (3 * sigma))
        capabilities[lot] = (cp, cpk)
    assert capabilities["L02"] == pytest.approx((5 / 3, NUMERIC_FORMS["7:l02-cpk"][0]))
    assert capabilities["L03"] == pytest.approx((4 / 3, NUMERIC_FORMS["7:l02-cpk"][2]))
    for row in rows:
        if row["lot_id"] == "L04":
            assert row["process_state"] == "special-cause-signal"
            assert row["capability_interpretation"] == "withheld-unstable-special-cause"
            assert row["summary_mean_mm"] == row["within_sigma_mm"] == ""
            assert row["nonconformance_status"] == "open"
    p16 = next(r for r in rows if r["part_id"] == "P16")
    assert float(p16["dimension_mm"]) > float(p16["usl_mm"])


def test_rehearsal_csv_recomputes_all_stacks_yields_and_hold_dispositions():
    rows = load_csv("assignments/release-gap-rehearsal.csv")
    assert len(rows) == 5 and all(r["data_status"] == "synthetic-original" for r in rows)
    derived = {}
    complete_values = {"complete-synthetic", "closed-verified-synthetic", "named-synthetic-role"}
    gate_fields = ["drawing_bom_alignment", "engineering_safety_review", "material_process_qualification", "calibrated_inspection_msa", "lot_traceability", "first_article_evidence", "nonconformance_closure", "change_control", "authorized_release_role_requirement"]
    for row in rows:
        sid = row["scenario_id"]
        wc = float(row["hole_lower_limit_mm"]) - float(row["shaft_upper_limit_mm"])
        terms = [float(row[f"rss_term_{i}_mm"]) for i in range(1, 4)]
        assert row["independence_declared"] == "yes"
        rss = math.sqrt(math.fsum(term * term for term in terms))
        observed_yield = int(row["accepted_parts"]) / int(row["inspected_parts"]) * 100
        complete = all(row[field] in complete_values for field in gate_fields)
        disposition = "synthetic_review_complete" if complete else "evidence_gaps_remain"
        assert disposition == row["expected_disposition"], sid
        derived[sid] = (wc, rss, observed_yield)
    assert derived["R02"][0] == pytest.approx(NUMERIC_FORMS["8:r02-wc-clearance"][0])
    assert derived["R03"][0] == pytest.approx(NUMERIC_FORMS["8:r02-wc-clearance"][2])
    assert derived["R04"][1] == pytest.approx(NUMERIC_FORMS["8:r04-rss"][0])
    assert derived["R05"][1] == pytest.approx(NUMERIC_FORMS["8:r04-rss"][2])
    assert derived["R05"][2] == NUMERIC_FORMS["8:r05-lot-yield"][0]
    assert derived["R03"][2] == NUMERIC_FORMS["8:r05-lot-yield"][2]
    assert [r["scenario_id"] for r in rows if r["expected_disposition"] == "synthetic_review_complete"] == ["R04"]
    by_id = {r["scenario_id"]: r for r in rows}
    assert by_id["R02"]["calibrated_inspection_msa"] == "missing"
    assert by_id["R03"]["nonconformance_closure"] == "open"
    assert by_id["R05"]["material_process_qualification"] == "missing"
    assert all(r["expected_disposition"] in {"synthetic_review_complete", "evidence_gaps_remain"} for r in rows)


def test_original_substantive_readings_resources_cases_and_no_release_boundaries():
    assert len(READINGS) == 8
    for lid, text in READINGS.items():
        assert len(text.split()) >= 700, lid
        assert "synthetic" in text.lower() and "fictional" in text.lower(), lid
        assert "unreviewed" in text and "formative-only" in text, lid
    for number in range(1, 7):
        assert len(READINGS[f"{CID}-{number}"].split()) >= 800
    assert MANIFEST["learner_resources"] == ["labs/fabrication-evidence.csv", "assignments/release-gap-rehearsal.csv"]
    assert all((COURSE / reference).is_file() for reference in MANIFEST["learner_resources"])
    assert "zero-point" in READINGS[f"{CID}-project-guide"]
    limitations = " ".join(MANIFEST["limitations"])
    assert "Fabrication readiness is the review objective, never an achieved claim" in limitations
    assert "24 base numerical answers and 24 authored variant numerical answers" in limitations
    assert "Repeated gauge measurements are not independent parts" in limitations
    assert "Mechanical Design remains a broader catalog-only planning node" in limitations
    combined = "\n".join(p.read_text(encoding="utf-8") for p in COURSE.rglob("*") if p.is_file()).lower()
    forbidden = [
        r"\bASTM\s*[A-Z]", r"\bISO\s*\d{3,}", r"\bG0[01]\b", r"\bM0[36]\b",
        r"\bset (?:the )?(?:feed|speed|spindle|voltage|current|laser|nozzle|cure)\b",
        r"\bcure (?:at|for) \d+\s*(?:°?c|h|min)", r"\bweld (?:at|with) \d+\s*(?:a|amps|v)\b",
        r"\bapproved for (?:production|service|fabrication)\b", r"\bcertified (?:safe|compliant|production-ready)\b",
    ]
    assert not {pattern: re.findall(pattern, combined) for pattern in forbidden if re.search(pattern, combined)}
    assert "no feeds/speeds" in combined and "standard-specific compliance" in combined
    assert "named authorized human release" in combined
    for case in CASES:
        serialized = json.dumps(case).lower()
        assert "production_approved" not in serialized or case["id"] == f"{CID}:case"
        assert "not a grade" in case["limitations"][0]
    rehearsal = load_csv("assignments/release-gap-rehearsal.csv")
    assert "production_approved" not in {r["expected_disposition"] for r in rehearsal}
