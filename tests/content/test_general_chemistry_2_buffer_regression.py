"""Independent equilibrium and buffer-accounting checks for General Chemistry II."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-2"


def test_weak_acid_buffer_ratio_capacity_and_legacy_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"].startswith("0.4.")
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "general-chemistry-2-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "activities",
        "mass and charge balances",
        "Henderson–Hasselbalch",
        "Neutralize first",
        "buffer capacity",
        "water autoionization",
        "0.576",
    ):
        assert concept.lower() in text.lower()

    ka = 1e-5
    formal_acid = 0.10
    dissociation_exact = (-ka + math.sqrt(ka**2 + 4 * ka * formal_acid)) / 2
    dissociation_approx = math.sqrt(ka * formal_acid)
    assert dissociation_exact == pytest.approx(0.0009950, abs=1e-7)
    assert dissociation_approx == pytest.approx(0.001)
    assert abs(dissociation_approx - dissociation_exact) / dissociation_exact < 0.01

    pka_and_ratio = 7.2 + math.log10(10)
    acetate_ph = 4.76 + math.log10(0.20 / 0.10)
    acid_added_ph_shift = math.log10(9 / 11)
    capacity_max = (2.303 / 4) * 0.10
    assert pka_and_ratio == pytest.approx(8.2)
    assert acetate_ph == pytest.approx(5.06103, abs=1e-5)
    assert acid_added_ph_shift == pytest.approx(-0.08715, abs=1e-5)
    assert capacity_max == pytest.approx(0.0576, abs=1e-4)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["general-chemistry-2-1:check"]["solution_spec"][
        "answer"
    ] == pytest.approx(8.2)
    assert items["general-chemistry-2-1:henderson-hasselbalch"]["solution_spec"][
        "answer"
    ] == pytest.approx(5.06)
    assert items["general-chemistry-2-1:check"]["objective_ids"] == [
        "general-chemistry-2-1-objective-2"
    ]
    mass_balance = items["general-chemistry-2-1:weak-acid-mass-balance"]
    assert mass_balance["solution_spec"]["answer"] == 0
    assert mass_balance["objective_ids"] == ["general-chemistry-2-1-objective-1"]

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id in (
        "general-chemistry-2-1-objective-1",
        "general-chemistry-2-1-objective-2",
    ):
        assert objectives[objective_id]["course_outcome_ids"] == [
            "general-chemistry-2-outcome-1"
        ]
    assessment = next(
        item for item in manifest["assessments"]
        if item["id"] == "general-chemistry-2-1-practice"
    )
    assert assessment["points"] == 3
    assert "general-chemistry-2-outcome-1" in assessment["objective_ids"]
    assert set(assessment["question_ids"]) == {
        "general-chemistry-2-1:check",
        "general-chemistry-2-1:henderson-hasselbalch",
        mass_balance["id"],
    }

