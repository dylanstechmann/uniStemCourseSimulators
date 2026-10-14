"""Independently recompute the inactive robotics trajectory project."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/robotics"
PROJECT = COURSE / "assessment-specs/trajectory-timing-actuator-margin-project-draft.md"
CANDIDATES = COURSE / "assessment-specs/trajectory-timing-candidates.csv"


def load_durations():
    with CANDIDATES.open(encoding="utf-8", newline="") as stream:
        return [float(row["duration_s"]) for row in csv.DictReader(stream)]


def torque(q, s, duration):
    inertia = 0.20
    mass, gravity, radius = 2.00, 9.81, 0.250
    acceleration = (6 - 12 * s) / duration**2
    position = 3 * s**2 - 2 * s**3
    return inertia * acceleration + mass * gravity * radius * math.cos(q + position)


def test_trajectory_actuator_stopping_and_energy_recompute():
    durations = load_durations()
    assert durations == [0.8, 1.0, 1.5]

    speed_limit = 1.0
    torque_limit = 5.5
    clearance = 0.4
    latency = 0.05
    braking = 4.0
    allowance = 0.02
    results = {}
    for duration in durations:
        peak_speed = 1.5 / duration
        peak_acceleration = 6 / duration**2
        peak_torque = 4.905 + 1.2 / duration**2
        stop_distance = peak_speed * latency + peak_speed**2 / (2 * braking) + allowance
        start_torque = torque(0.0, 0.0, duration)
        end_torque = torque(0.0, 1.0, duration)
        assert math.isclose(start_torque, peak_torque, abs_tol=1e-12)
        assert start_torque >= end_torque
        results[duration] = (peak_speed, peak_acceleration, peak_torque, stop_distance)

    assert all(
        math.isclose(actual, expected, abs_tol=1e-12)
        for actual, expected in zip(
            results[0.8], (1.875, 9.375, 6.78, 0.553203125)
        )
    )
    assert all(
        math.isclose(actual, expected, abs_tol=1e-12)
        for actual, expected in zip(results[1.0], (1.5, 6.0, 6.105, 0.37625))
    )
    assert math.isclose(results[1.5][0], speed_limit, abs_tol=1e-15)
    assert math.isclose(results[1.5][2], 5.438333333333333, abs_tol=1e-12)
    assert math.isclose(results[1.5][3], 0.195, abs_tol=1e-15)

    feasible = [
        duration
        for duration, (speed, _, torque_peak, stop) in results.items()
        if speed <= speed_limit and torque_peak <= torque_limit and stop <= clearance
    ]
    assert feasible == [1.5]
    energy = 2.0 * 9.81 * 0.250 * math.sin(1.0)
    assert math.isclose(energy, 4.127415180482733, abs_tol=1e-12)


def test_project_is_linked_inactive_and_versioned():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert manifest["maturity"] == "partial"
    assert "assessment-specs/trajectory-timing-actuator-margin-project-draft.md" in syllabus
    assert "not scheduled or assigned" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "establishes no real robot performance, protective function or safety" in project
