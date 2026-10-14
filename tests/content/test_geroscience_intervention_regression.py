"""Regression checks for the expanded Geroscience intervention prototype."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/geroscience"


def test_intervention_claims_and_endpoint_example_preserve_legacy_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "geroscience-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "Learning objectives",
        "target engagement",
        "mechanistic claim",
        "Harrison and colleagues",
        "synthetic example",
        "serious adverse event",
        "survivor-only motor averages",
        "not proof that the survival result depended on that target",
        "Limits of this lesson",
        "not medical advice",
    ):
        assert phrase.lower() in text.lower()

    randomized_per_arm = 100
    treatment_deaths = 20
    control_deaths = 30
    intervention_survival = (randomized_per_arm - treatment_deaths) / randomized_per_arm
    control_survival = (randomized_per_arm - control_deaths) / randomized_per_arm
    absolute_survival_difference = intervention_survival - control_survival
    target_inhibition_treatment = 70 / 100
    target_inhibition_control = 5 / 100
    treatment_adverse_events = 12
    control_adverse_events = 4
    assert intervention_survival == pytest.approx(0.80)
    assert control_survival == pytest.approx(0.70)
    assert absolute_survival_difference == pytest.approx(0.10)
    assert target_inhibition_treatment == pytest.approx(0.70)
    assert target_inhibition_control == pytest.approx(0.05)
    assert treatment_adverse_events > control_adverse_events

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    questions = {item["id"]: item for item in bank["questions"]}
    assert questions["geroscience-4:check"]["solution_spec"]["answer"] == 0
    assert questions["geroscience-4:intervention-mechanism-vs-endpoints"][
        "solution_spec"
    ]["answer"] == 1
    assert lesson["question_ids"] == [
        "geroscience-4:check",
        "geroscience-4:intervention-mechanism-vs-endpoints",
    ]
    assert lesson["card_ids"] == ["geroscience-3-0", "geroscience-3-1"]

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped_module = next(
        item for item in source_map["modules"] if item["lesson_id"] == "geroscience-4"
    )
    registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    source = next(
        item
        for item in registry["sources"]
        if item["id"] == "harrison-2009-rapamycin-itp"
    )
    assert "harrison-2009-rapamycin-itp" in mapped_module["source_ids"]
    assert "harrison-2009-rapamycin-itp" in next(
        module
        for module in manifest["modules"]
        if module["id"] == "geroscience-module-4"
    )["source_ids"]
    assert "geroscience-module-4" in source["mapped_modules"]
    assert source["permissions"]["linking"] is True
    assert source["permissions"]["adaptation"] is False
    assert source["permissions"]["redistribution"] is False

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert f"version: {manifest['version']}." in syllabus
    assert "all four compact legacy prototype readings in weeks 1, 5, 8 and 11 now have expanded instructional readings" in syllabus

