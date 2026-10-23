"""Independent equation checks for the physiology electrophysiology primer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physiology"


def test_ionic_driving_force_and_passive_multi_ion_balance():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "physiology-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "outward-positive" in text
    assert "a multi-ion model" in text

    potassium_example_pa = 2 * (-60 - (-90))
    potassium_steady_pa = 2 * (-77.2727272727 - (-90))
    sodium_current_pa = 0.2 * (-77.2727272727 - 50)
    steady_voltage_mv = (2 * -90 + 0.2 * 50) / (2 + 0.2)
    assert potassium_example_pa == pytest.approx(60)
    assert steady_voltage_mv == pytest.approx(-77.2727272727)
    assert potassium_steady_pa == pytest.approx(25.45454545)
    assert sodium_current_pa == pytest.approx(-25.45454545)
    assert potassium_steady_pa + sodium_current_pa == pytest.approx(0, abs=1e-9)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["physiology-2:check"]["solution_spec"]["answer"] == pytest.approx(-400)
    assert items["physiology-2:ionic-current"]["solution_spec"]["answer"] == pytest.approx(
        0.5
    )

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert f"({lesson['reading']})" in syllabus
