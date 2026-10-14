"""Check that the free-energy lesson's displayed examples use consistent conventions."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def test_free_energy_examples_reproduce_the_displayed_values():
    manifest = json.loads(
        (COURSE / "course.json").read_text(encoding="utf-8")
    )
    lesson_entry = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biochemistry-6"
    )
    lesson = (COURSE / lesson_entry["reading"]).read_text(encoding="utf-8")
    rt = 2.577

    atp_q = (3.0e-4 * 3.0e-3) / 3.0e-3
    atp_delta_g = -30.5 + rt * math.log(atp_q)
    phosphorylation_equilibrium = math.exp(-13.8 / rt)
    hexokinase_delta_g0 = 13.8 - 30.5
    nadh_oxygen_delta_g0 = -2 * 96.485 * (0.815 - (-0.320))
    isomerization_delta_g = 5 + rt * math.log(0.05)
    isomerization_equilibrium = math.exp(-5 / rt)

    assert atp_q == pytest.approx(3.0e-4)
    assert atp_delta_g == pytest.approx(-51.4, abs=0.1)
    assert phosphorylation_equilibrium == pytest.approx(4.73e-3, rel=0.01)
    assert hexokinase_delta_g0 == pytest.approx(-16.7)
    assert nadh_oxygen_delta_g0 == pytest.approx(-219, abs=0.2)
    assert isomerization_delta_g == pytest.approx(-2.72, abs=0.01)
    assert isomerization_equilibrium == pytest.approx(0.144, abs=0.001)
    assert "Strictly, Q is dimensionless" in lesson
    assert "aᵢ = [i]/c°" in lesson
    assert "Q = a_ADP a_Pᵢ/a_ATP = 3.0×10⁻⁴" in lesson
