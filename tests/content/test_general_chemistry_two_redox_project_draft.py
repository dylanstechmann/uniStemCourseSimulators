"""Recompute the inactive General Chemistry II fictional-redox portfolio."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-2"
PROJECT = COURSE / "assessment-specs/fictional-redox-cell-project-draft.md"


def test_redox_balance_cell_potential_gibbs_nernst_and_charge_recompute():
    faraday = 96_485.0
    gas_constant = 8.314
    temperature = 298.15
    electrons = 6
    anode_electrons = 3 * 2
    cathode_electrons = 2 * 3
    reactant_charge = 2 * 3
    product_charge = 3 * 2
    standard_potential = 0.400 - (-0.200)
    delta_g = -electrons * faraday * standard_potential
    ln_k = electrons * faraday * standard_potential / (gas_constant * temperature)
    quotient = 0.1**3 / 0.01**2
    potential = standard_potential - gas_constant * temperature / (electrons * faraday) * math.log(quotient)
    charge = 0.200 * 30.0 * 60
    electron_moles = charge / faraday
    extent = electron_moles / electrons

    assert anode_electrons == cathode_electrons == electrons
    assert reactant_charge == product_charge
    assert math.isclose(standard_potential, 0.600, abs_tol=1e-15)
    assert math.isclose(delta_g, -347_346.0, abs_tol=1e-9)
    assert math.isclose(ln_k, 140.1255944817, abs_tol=1e-10)
    assert math.isclose(ln_k / math.log(10), 60.8557724568, abs_tol=1e-10)
    assert math.isclose(quotient, 10.0, abs_tol=1e-14)
    assert math.isclose(potential, 0.590140623054, abs_tol=1e-12)
    assert math.isclose(charge, 360.0, abs_tol=1e-12)
    assert math.isclose(extent, 0.000621858319946, abs_tol=1e-15)
    assert math.isclose(3 * extent, 0.00186557495984, abs_tol=1e-14)
    assert math.isclose(2 * extent, 0.00124371663989, abs_tol=1e-14)


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/fictional-redox-cell-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
    assert "The symbols `A` and `B` denote fictional bookkeeping tokens" in project
