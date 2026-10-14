"""Independently recompute the inactive viscoelastic material-selection draft."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cellular-biomechanics"
PROJECT = COURSE / "assessment-specs/viscoelastic-material-selection-project-draft.md"
CANDIDATES = COURSE / "assessment-specs/viscoelastic-material-candidates.csv"


def load_candidates():
    with CANDIDATES.open(encoding="utf-8", newline="") as stream:
        return {
            row["candidate"]: {
                "equilibrium": float(row["equilibrium_modulus_kpa"]),
                "relaxing": float(row["relaxing_modulus_kpa"]),
                "tau": float(row["relaxation_time_s"]),
            }
            for row in csv.DictReader(stream)
        }


def complex_moduli(candidate, omega):
    x = omega * candidate["tau"]
    denominator = 1 + x**2
    storage = candidate["equilibrium"] + candidate["relaxing"] * x**2 / denominator
    loss = candidate["relaxing"] * x / denominator
    return storage, loss


def test_relaxation_rheology_and_dissipation_recompute():
    candidates = load_candidates()
    assert set(candidates) == {"A", "B", "C"}

    instantaneous = {
        name: c["equilibrium"] + c["relaxing"] for name, c in candidates.items()
    }
    assert instantaneous == {"A": 10.0, "B": 8.0, "C": 7.0}

    at_five_seconds = {
        name: 0.050 * (c["equilibrium"] + c["relaxing"] * math.exp(-5.0 / c["tau"]))
        for name, c in candidates.items()
    }
    assert math.isclose(at_five_seconds["A"], 0.3229387969, abs_tol=1e-10)
    assert math.isclose(at_five_seconds["B"], 0.2000000000, abs_tol=1e-10)
    assert math.isclose(at_five_seconds["C"], 0.1016844868, abs_tol=1e-10)

    slow = {name: complex_moduli(c, 0.010) for name, c in candidates.items()}
    fast = {name: complex_moduli(c, 1.0) for name, c in candidates.items()}
    assert math.isclose(slow["A"][0], 1.0891089109, abs_tol=1e-10)
    assert math.isclose(slow["B"][1], 0.0039999960, abs_tol=1e-10)
    assert math.isclose(fast["A"][0], 9.9108910891, abs_tol=1e-10)
    assert math.isclose(fast["C"][1], 2.5, abs_tol=1e-12)
    assert slow["B"][0] > slow["A"][0]
    assert fast["A"][0] > fast["B"][0]

    loss_tangent = {name: loss / storage for name, (storage, loss) in fast.items()}
    assert math.isclose(loss_tangent["A"], 0.0899, abs_tol=1e-4)
    assert math.isclose(loss_tangent["B"], 0.0980, abs_tol=1e-4)
    assert math.isclose(loss_tangent["C"], 0.5555555556, abs_tol=1e-10)
    dissipated_j_m3 = {
        name: math.pi * loss * 0.030**2 * 1000
        for name, (_, loss) in fast.items()
    }
    assert math.isclose(dissipated_j_m3["A"], 2.5195, abs_tol=0.001)
    assert math.isclose(dissipated_j_m3["B"], 1.1198, abs_tol=0.001)
    assert math.isclose(dissipated_j_m3["C"], 7.0686, abs_tol=0.001)


def test_project_is_linked_inactive_and_versioned():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert manifest["maturity"] == "partial"
    assert "assessment-specs/viscoelastic-material-selection-project-draft.md" in syllabus
    assert "not scheduled or assigned" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "cannot establish how any cell would signal" in project
