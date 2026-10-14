"""Independent equation checks for the biomaterials interface primer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biomaterials"


def test_surface_wetting_and_bulk_modulus_examples():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.3.")
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biomaterials-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("bulk properties", "surface properties", "contact angle", "protein layer", "modulus"):
        assert concept.lower() in text.lower()

    contact_cosine = (48 - 12) / 72
    treated_contact_cosine = (66 - 12) / 72
    assert contact_cosine == pytest.approx(0.5)
    assert math.degrees(math.acos(contact_cosine)) == pytest.approx(60)
    assert math.degrees(math.acos(treated_contact_cosine)) == pytest.approx(41.4096221)

    stress_mpa = 2 / 2
    strain = 0.5 / 20
    modulus_mpa = stress_mpa / strain
    assert stress_mpa == pytest.approx(1)
    assert strain == pytest.approx(0.025)
    assert modulus_mpa == pytest.approx(40)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["biomaterials-1:check"]["solution_spec"]["answer"] == 0
    assert items["biomaterials-1:bulk-vs-surface"]["solution_spec"]["answer"] == 0

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "Weeks 3, 9 and 13 also have expanded" in syllabus
