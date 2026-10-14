"""Regression checks for the inactive synthetic rotor trade-off portfolio."""

from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-mechanics"


def test_equal_rcf_rotor_calculations_reproduce_the_documented_tradeoffs():
    with (COURSE / "assessment-specs/fictional-rotor-candidates.csv").open(
        encoding="utf-8", newline=""
    ) as source:
        candidates = list(csv.DictReader(source))

    calculations = {}
    for candidate in candidates:
        radius = float(candidate["radius_m"])
        disk_mass = float(candidate["disk_mass_kg"])
        imbalance_mass = float(candidate["imbalance_mass_kg"])
        target_rcf = float(candidate["target_rcf"])
        gravity = float(candidate["g_m_per_s2"])
        omega = math.sqrt(target_rcf * gravity / radius)
        rpm = omega * 60 / (2 * math.pi)
        inertia = 0.5 * disk_mass * radius**2
        energy = 0.5 * inertia * omega**2
        imbalance_force = imbalance_mass * omega**2 * radius
        calculations[candidate["candidate"]] = (
            omega,
            rpm,
            inertia,
            energy,
            imbalance_force,
        )
        assert math.isclose(omega**2 * radius / gravity, target_rcf)

    assert set(calculations) == {"A", "B", "C"}
    assert math.isclose(calculations["A"][1], 2590, rel_tol=0.001)
    assert math.isclose(calculations["B"][3], 211.9, rel_tol=0.001)
    assert math.isclose(calculations["C"][4], 5.886, rel_tol=0.001)
    assert calculations["B"][3] > calculations["A"][3] > calculations["C"][3]
    assert math.isclose(
        calculations["A"][4], calculations["B"][4], rel_tol=1e-12
    )
    assert calculations["C"][4] > calculations["A"][4]


def test_rotor_draft_is_fictional_nonoperational_and_linked_to_course():
    draft = (
        COURSE / "assessment-specs/fictional-rotor-tradeoff-project-draft.md"
    ).read_text(encoding="utf-8")
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    manifest = (COURSE / "course.json").read_text(encoding="utf-8")

    assert "Status: authoring draft only" in draft
    assert "Every geometry, mass, imbalance and target is invented" in draft
    assert "not an operating specification" in draft
    assert "no score, rubric, gradebook mapping, platform activation" in draft
    assert "fictional-rotor-tradeoff-project-draft.md" in syllabus
    assert '"version": "0.4.7"' in manifest
    assert "inactive, ungraded paper-exercise draft" in manifest
