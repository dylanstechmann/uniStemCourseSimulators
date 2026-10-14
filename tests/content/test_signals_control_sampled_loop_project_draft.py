"""Recompute the inactive sampled-loop project's signal and control values."""

from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/signals-control"
PROJECT = COURSE / "assessment-specs/sampled-loop-project-draft.md"


def test_alias_filter_hold_margin_pi_and_sampled_plant_values_recompute():
    sample_period = 0.25
    sample_frequency = 1 / sample_period
    alias = abs(3 - round(3 / sample_frequency) * sample_frequency)
    disturbance_gain = 1 / math.sqrt(1 + (3 / 1) ** 2)
    desired_gain = 1 / math.sqrt(1 + (0.25 / 1) ** 2)
    phase_rad = (1 / 3) * sample_period / 2
    phase_deg = math.degrees(phase_rad)
    candidate = 19.9 + 6.667 * (1.2 - 0.9) + 6.667 * (sample_period / 10) * 1.2
    applied = min(20, max(0, candidate))
    a = math.exp(-sample_period / 10)
    next_state = 0.5 * (1 - a) * applied

    assert sample_frequency == 4
    assert sample_frequency / 2 == 2
    assert alias == 1
    assert math.isclose(disturbance_gain, 0.316227766017, abs_tol=1e-12)
    assert math.isclose(desired_gain, 0.970142500145, abs_tol=1e-12)
    assert sample_period <= 3 / 10
    assert math.isclose(phase_rad, 1 / 24, abs_tol=1e-15)
    assert math.isclose(phase_deg, 2.38732414638, abs_tol=1e-11)
    assert math.isclose(70.9 - phase_deg, 68.5126758536, abs_tol=1e-10)
    assert math.isclose(candidate, 22.10011, abs_tol=1e-12)
    assert applied == 20
    assert math.isclose(a, 0.975309912028, abs_tol=1e-12)
    assert math.isclose(next_state, 0.246900879719, abs_tol=1e-11)


def test_project_is_linked_inactive_and_versioned():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert course["version"] == course["history"][-1]["version"]
    assert course["maturity"] == "partial"
    assert "assessment-specs/sampled-loop-project-draft.md" in syllabus
    assert "not scheduled, submitted or graded" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "automatic prose grader" in project
