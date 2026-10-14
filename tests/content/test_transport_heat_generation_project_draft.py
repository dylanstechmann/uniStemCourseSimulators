"""Recompute the inactive Transport heat-generation slab project."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/transport"
PROJECT = COURSE / "assessment-specs/heat-generation-slab-project-draft.md"


def test_temperature_profile_flux_energy_balance_and_simpson_average():
    length = 0.010
    conductivity = 0.50
    generation = 10_000.0
    convection = 20.0
    ambient = 25.0

    def profile(ratio: float) -> float:
        return ambient + generation * length / convection + generation * length**2 / (2 * conductivity) * (1 - ratio**2)

    nodes = [profile(ratio) for ratio in (0, 0.25, 0.5, 0.75, 1)]
    average_simpson = (nodes[0] + 4 * nodes[1] + 2 * nodes[2] + 4 * nodes[3] + nodes[4]) / 12
    average_exact = ambient + generation * length / convection + generation * length**2 / (3 * conductivity)
    surface_flux_generation = generation * length
    surface_flux_convection = convection * (profile(1) - ambient)

    assert math.isclose(profile(0), 31.0, abs_tol=1e-12)
    assert math.isclose(profile(1), 30.0, abs_tol=1e-12)
    assert nodes == [31.0, 30.9375, 30.75, 30.4375, 30.0]
    assert math.isclose(average_simpson, 30.6666666667, abs_tol=1e-10)
    assert math.isclose(average_exact, average_simpson, abs_tol=1e-12)
    assert math.isclose(surface_flux_generation, surface_flux_convection, abs_tol=1e-12)
    assert math.isclose(convection * length / conductivity, 0.4, abs_tol=1e-15)


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["maturity"] == "partial"
    assert course["history"][-1]["version"] == course["version"]
    assert "assessment-specs/heat-generation-slab-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
