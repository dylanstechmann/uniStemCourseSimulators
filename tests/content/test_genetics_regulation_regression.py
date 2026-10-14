"""Regression checks for the synthetic Genetics gene-regulation lesson."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/genetics"


def test_cis_trans_and_perturbation_evidence_preserve_legacy_items():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "genetics-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "synthetic allele-specific expression",
        "Learning objectives",
        "cis-regulatory",
        "trans-acting",
        "matched genomic DNA",
        "CRISPR interference",
        "rescue",
        "does not establish that the nearby variant caused the difference",
        "Limits of this lesson",
        "medical advice",
    ):
        assert phrase.lower() in text.lower()

    alternate_to_reference_ratio = 60 / 100
    dna_calibrated_ratio = alternate_to_reference_ratio / (100 / 100)
    target_expression_remaining = 0.60
    target_expression_reduction = 1 - target_expression_remaining
    assert alternate_to_reference_ratio == pytest.approx(0.60)
    assert dna_calibrated_ratio == pytest.approx(0.60)
    assert target_expression_reduction == pytest.approx(0.40)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["genetics-3:check"]["solution_spec"]["answer"] == 0
    assert questions["genetics-3:distinguish-correlation-from-mechanism"][
        "solution_spec"
    ]["answer"] == 3
    assert lesson["question_ids"] == [
        "genetics-3:check",
        "genetics-3:distinguish-correlation-from-mechanism",
    ]
    assert lesson["card_ids"] == ["genetics-2-0", "genetics-2-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    assert objectives["genetics-3-objective-1"]["course_outcome_ids"] == [
        "genetics-outcome-3"
    ]
    assert objectives["genetics-3-objective-2"]["course_outcome_ids"] == [
        "genetics-outcome-3",
        "genetics-outcome-4",
    ]
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == "genetics-3-practice"
    )
    assert {"genetics-outcome-3", "genetics-outcome-4"} <= set(
        assessment["objective_ids"]
    )

    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    sources = {item["id"]: item for item in registry["sources"]}
    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    module = next(item for item in source_map["modules"] if item["lesson_id"] == "genetics-3")
    for source_id in (
        "cheung-2010-cis-trans-expression",
        "larson-2013-crispri-sequence-specific",
    ):
        source = sources[source_id]
        assert source_id in module["source_ids"]
        assert source["mapped_modules"] == ["genetics-module-3"]
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all compact prototype readings now have expanded instruction" in syllabus
    assert "six abstracts were read" in syllabus
