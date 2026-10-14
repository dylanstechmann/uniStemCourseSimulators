"""Independently recompute the inactive protein-state and binding portfolio."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
PROJECT = COURSE / "assessment-specs/protein-state-binding-project-draft.md"
CONDITIONS = COURSE / "assessment-specs/protein-state-binding-conditions.csv"


def load_conditions():
    with CONDITIONS.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def net_charge(row):
    pH = float(row["pH"])
    acidic = int(row["acid_group_count"]) / (
        1 + 10 ** (float(row["acid_pKa"]) - pH)
    )
    basic = int(row["basic_group_count"]) / (
        1 + 10 ** (pH - float(row["basic_pKa"]))
    )
    histidine = int(row["histidine_count"]) / (
        1 + 10 ** (pH - float(row["histidine_pKa"]))
    )
    return basic + histidine - acidic


def calculate(row):
    rt = 0.008314 * 298.15
    delta_g = float(row["deltaG_water_kj_per_mol"]) - float(
        row["m_kj_per_mol_M"]
    ) * float(row["denaturant_M"])
    ku = math.exp(-delta_g / rt)
    folded_fraction = 1 / (1 + ku)
    active_total = folded_fraction * float(row["protein_total_nM"])
    ligand_total = float(row["ligand_total_nM"])
    kd = float(row["Kd_nM"])
    bound = (
        active_total
        + ligand_total
        + kd
        - math.sqrt((active_total + ligand_total + kd) ** 2 - 4 * active_total * ligand_total)
    ) / 2
    return {
        "delta_g": delta_g,
        "folded_fraction": folded_fraction,
        "active_total": active_total,
        "bound": bound,
        "folded_occupancy": bound / active_total,
        "total_fraction_bound": bound / float(row["protein_total_nM"]),
    }


def test_charge_folding_depletion_and_decision_recompute():
    conditions = {row["condition"]: row for row in load_conditions()}
    assert set(conditions) == {"A", "B"}
    assert math.isclose(net_charge(conditions["A"]), 1.0686070007, abs_tol=1e-10)
    assert math.isclose(net_charge(conditions["B"]), -0.0488050205, abs_tol=1e-10)

    a = calculate(conditions["A"])
    b = calculate(conditions["B"])
    assert math.isclose(a["delta_g"], 5.0, abs_tol=1e-12)
    assert math.isclose(a["folded_fraction"], 0.8825797226, abs_tol=1e-10)
    assert math.isclose(a["bound"], 33.8806533555, abs_tol=1e-9)
    assert math.isclose(a["folded_occupancy"], 0.7678, abs_tol=1e-4)
    assert math.isclose(a["total_fraction_bound"], 0.6776130671, abs_tol=1e-10)
    assert math.isclose(b["delta_g"], 4.5, abs_tol=1e-12)
    assert math.isclose(b["folded_fraction"], 0.8600109068, abs_tol=1e-10)
    assert math.isclose(b["bound"], 37.1018312720, abs_tol=1e-9)
    assert math.isclose(b["folded_occupancy"], 0.863, abs_tol=1e-3)
    assert math.isclose(b["total_fraction_bound"], 0.7420366254, abs_tol=1e-10)

    assert a["bound"] < a["active_total"] * 100 / (20 + 100)
    assert b["bound"] < b["active_total"] * 100 / (10 + 100)
    assert a["total_fraction_bound"] < 0.70 < b["total_fraction_bound"]


def test_project_is_linked_inactive_and_versioned():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert manifest["maturity"] == "partial"
    assert "assessment-specs/protein-state-binding-project-draft.md" in syllabus
    assert "not scheduled or assigned" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "not infer them from the net charge" in project
