"""Independent equation checks for the biomaterials scaffold primer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biomaterials"


def test_scaffold_architecture_degradation_and_support():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.3.")
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biomaterials-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("relative density", "porosity", "first-order mass model", "modulus loss", "load-sharing"):
        assert concept.lower() in text.lower()

    porosity = 0.90
    solid_modulus_mpa = 1000
    relative_density_exponent = 2
    effective_modulus_mpa = solid_modulus_mpa * (1 - porosity) ** relative_density_exponent
    assert effective_modulus_mpa == pytest.approx(10)

    initial_mass_mg = 100
    retained_fraction_per_week = 0.85
    assert initial_mass_mg * retained_fraction_per_week == pytest.approx(85)
    assert initial_mass_mg * retained_fraction_per_week**4 == pytest.approx(52.200625)

    modulus_mpa = 2 * math.exp(-0.05 * 14)
    assert modulus_mpa == pytest.approx(0.9931706076)
    assert 50 + 20 == pytest.approx(70)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["biomaterials-2:check"]["solution_spec"]["answer"] == pytest.approx(85)
    assert items["biomaterials-2:degradation-modulus"]["solution_spec"]["answer"] == pytest.approx(
        0.9932
    )

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "Weeks 3, 9 and 13 also have expanded" in syllabus
