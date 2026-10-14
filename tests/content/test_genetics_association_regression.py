"""Regression checks for synthetic Genetics association examples."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/genetics"


def test_association_effect_uncertainty_and_causal_limits_preserve_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "genetics-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "synthetic case-control example",
        "Learning objectives",
        "odds ratio",
        "95% interval",
        "multiple comparisons",
        "population structure",
        "linkage disequilibrium",
        "fine-mapping",
        "functional evidence",
        "no clinical meaning",
    ):
        assert phrase.lower() in text.lower()

    odds_ratio = (250 * 300) / (250 * 200)
    log_or_se = math.sqrt(1 / 250 + 1 / 250 + 1 / 200 + 1 / 300)
    ci_lower = math.exp(math.log(odds_ratio) - 1.96 * log_or_se)
    ci_upper = math.exp(math.log(odds_ratio) + 1.96 * log_or_se)
    assert odds_ratio == pytest.approx(1.5)
    assert log_or_se == pytest.approx(0.1278, abs=0.0001)
    assert ci_lower == pytest.approx(1.17, abs=0.01)
    assert ci_upper == pytest.approx(1.93, abs=0.01)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["genetics-4:check"]["solution_spec"]["answer"] == 1
    assert questions["genetics-4:association-vs-causation"]["solution_spec"][
        "answer"
    ] == 0
    assert lesson["question_ids"] == [
        "genetics-4:check",
        "genetics-4:association-vs-causation",
    ]
    assert lesson["card_ids"] == ["genetics-3-0", "genetics-3-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in (
        "genetics-4-objective-1",
        "genetics-4-objective-2",
    ):
        assert objectives[objective_id]["course_outcome_ids"] == [
            "genetics-outcome-3"
        ]
    assessment = next(
        item for item in manifest["assessments"] if item["id"] == "genetics-4-practice"
    )
    assert "genetics-outcome-3" in assessment["objective_ids"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    module = next(item for item in source_map["modules"] if item["lesson_id"] == "genetics-4")
    assert "price-2006-gwas-stratification" in module["source_ids"]
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    source = next(
        item
        for item in registry["sources"]
        if item["id"] == "price-2006-gwas-stratification"
    )
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
