"""Independent arithmetic checks for the expanded physiology feedback primer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physiology"


def test_concentration_balance_and_response_time_example():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "physiology-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "removal is $kVC=18$ µmol/min" in text
    assert "about 36.8% of the initial deviation remains" in text

    input_rate, volume, clearance = 12.0, 2.0, 0.3
    steady_concentration = input_rate / (clearance * volume)
    net_rate_at_30 = input_rate / volume - clearance * 30
    net_rate_at_10 = input_rate / volume - clearance * 10
    time_constant = 1 / clearance
    remaining_fraction = math.exp(-clearance * time_constant)
    assert steady_concentration == pytest.approx(20)
    assert net_rate_at_30 == pytest.approx(-3)
    assert net_rate_at_10 == pytest.approx(3)
    assert time_constant == pytest.approx(3.333333333)
    assert remaining_fraction == pytest.approx(1 / math.e)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["physiology-1:check"]["solution_spec"]["answer"] == pytest.approx(
        steady_concentration
    )
    assert items["physiology-1:feedback-classification"]["solution_spec"][
        "answer"
    ] == 3

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "weeks 1, 3, 5 and 11 now have expanded" in syllabus
    assert "the four original prototype readings remain short primers despite this expansion" in syllabus.lower()
