"""Independent equation checks for the physiology renal/endocrine primer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physiology"


def test_clearance_filtered_load_and_sensor_sensitivity():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "physiology-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("filtered load", "clearance", "sensitivity", "input}-\\text{output"):
        assert concept.lower() in text.lower()

    urine_concentration_mg_per_l = 50
    urine_flow_l_per_min = 1 / 1000
    plasma_concentration_mg_per_l = 2
    excretion_mg_per_min = urine_concentration_mg_per_l * urine_flow_l_per_min
    clearance_l_per_min = excretion_mg_per_min / plasma_concentration_mg_per_l
    assert excretion_mg_per_min == pytest.approx(0.05)
    assert clearance_l_per_min * 1000 == pytest.approx(25)

    filtered_load_mg_per_min = (100 / 1000) * 2
    excretion_mg_per_min = 50 * (4 / 1000)
    clearance_ml_per_min = excretion_mg_per_min / 2 * 1000
    assert filtered_load_mg_per_min == pytest.approx(0.2)
    assert excretion_mg_per_min == pytest.approx(filtered_load_mg_per_min)
    assert clearance_ml_per_min == pytest.approx(100)

    sensed_threshold = 10
    hormone_at_full_sensitivity = sensed_threshold / 1.0
    hormone_at_half_sensitivity = sensed_threshold / 0.5
    assert hormone_at_full_sensitivity == pytest.approx(10)
    assert hormone_at_half_sensitivity == pytest.approx(20)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["physiology-4:check"]["solution_spec"]["answer"] == pytest.approx(12)
    assert items["physiology-4:hormonal-set-point"]["solution_spec"]["answer"] == 3

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert f"({lesson['reading']})" in syllabus
