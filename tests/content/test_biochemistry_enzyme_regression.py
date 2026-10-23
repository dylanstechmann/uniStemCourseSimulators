"""Independent equation checks for the biochemistry enzyme primer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def test_michaelis_menten_inhibition_and_efficiency():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biochemistry-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("transition state", "initial-rate", "competitive", "mixed", "uncompetitive"):
        assert concept.lower() in text.lower()

    vmax_umol_per_min = 100
    substrate_mm = 2
    km_mm = 2
    competitive_factor = 4
    uninhibited_rate = vmax_umol_per_min * substrate_mm / (km_mm + substrate_mm)
    inhibited_rate = vmax_umol_per_min * substrate_mm / (
        competitive_factor * km_mm + substrate_mm
    )
    assert uninhibited_rate == pytest.approx(50)
    assert inhibited_rate == pytest.approx(20)
    assert vmax_umol_per_min * 1000 / (1000 + km_mm) == pytest.approx(99.8003992)
    assert vmax_umol_per_min * 1000 / (competitive_factor * km_mm + 1000) == pytest.approx(
        99.2063492
    )

    kcat_per_s = 500
    km_mol_per_l = 25e-6
    efficiency = kcat_per_s / km_mol_per_l
    assert efficiency == pytest.approx(20_000_000)

    barrier_difference_j_per_mol = 5.71e3
    temperature_k = 298.0
    gas_constant_j_per_mol_k = 8.314
    rate_ratio = math.exp(
        barrier_difference_j_per_mol / (gas_constant_j_per_mol_k * temperature_k)
    )
    assert gas_constant_j_per_mol_k * temperature_k * math.log(10) == pytest.approx(
        barrier_difference_j_per_mol, abs=10.0
    )
    assert rate_ratio == pytest.approx(10, rel=0.003)

    assert "acyl-enzyme intermediate" in text
    assert "transition states" in text
    assert "assumptions" in text.lower()

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["biochemistry-2:check"]["solution_spec"]["answer"] == 0
    assert items["biochemistry-2:catalytic-efficiency"]["solution_spec"]["answer"] == pytest.approx(
        20_000_000
    )

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "Enzyme mechanisms and inhibition](modules/02-enzyme-mechanisms-and-inhibition.md)" in next(row for row in syllabus.splitlines() if row.startswith("| 5 |"))
    assert "The citric acid cycle: carbon, reduci" in syllabus

    source_registry = json.loads(
        (ROOT / "content/sources/registry.json").read_text(encoding="utf-8")
    )
    source_ids = {source["id"] for source in source_registry["sources"]}
    assert {
        "biochem-chymotrypsin-blow-1969",
        "biochem-chymotrypsin-fastrez-houyet-1977",
        "eyring-activated-complex-1935",
    } <= source_ids
