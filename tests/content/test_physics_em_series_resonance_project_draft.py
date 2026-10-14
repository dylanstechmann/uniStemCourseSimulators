"""Independently recompute the inactive series-resonance project draft."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-em"
PROJECT = COURSE / "assessment-specs/series-resonance-project-draft.md"
CANDIDATES = COURSE / "assessment-specs/series-rlc-candidates.csv"


def load_candidates():
    with CANDIDATES.open(encoding="utf-8", newline="") as stream:
        return {
            row["candidate"]: {
                "resistance": float(row["resistance_ohm"]),
                "inductance": float(row["inductance_h"]),
                "capacitance": float(row["capacitance_f"]),
                "source_peak": float(row["source_peak_v"]),
            }
            for row in csv.DictReader(stream)
        }


def test_resonance_bandwidth_power_energy_and_selection_recompute():
    candidates = load_candidates()
    assert set(candidates) == {"A", "B", "C"}
    results = {}
    for name, item in candidates.items():
        r = item["resistance"]
        inductance = item["inductance"]
        capacitance = item["capacitance"]
        source_peak = item["source_peak"]
        omega_0 = 1 / math.sqrt(inductance * capacitance)
        quality = omega_0 * inductance / r
        bandwidth = r / inductance
        discriminant = math.sqrt(r**2 + 4 * inductance / capacitance)
        low = (discriminant - r) / (2 * inductance)
        high = (discriminant + r) / (2 * inductance)
        peak_current = source_peak / r
        average_power = (peak_current / math.sqrt(2)) ** 2 * r
        stored_energy = 0.5 * inductance * peak_current**2
        results[name] = (quality, bandwidth, low, high, peak_current, average_power, stored_energy)

    assert math.isclose(results["A"][0], 1.0, abs_tol=1e-15)
    assert math.isclose(results["B"][1], 2000, abs_tol=1e-12)
    assert math.isclose(results["C"][4], 0.100, abs_tol=1e-15)
    assert math.isclose(results["A"][2], 618.0339887499, abs_tol=1e-9)
    assert math.isclose(results["A"][3], 1618.0339887499, abs_tol=1e-9)
    assert math.isclose(results["B"][2], 414.2135623731, abs_tol=1e-9)
    assert math.isclose(results["C"][3], 1280.7764064044, abs_tol=1e-9)
    assert math.isclose(results["A"][5], 0.125, abs_tol=1e-15)
    assert math.isclose(results["A"][6], 0.000125, abs_tol=1e-15)

    passing = [
        name
        for name, (quality, bandwidth, _, _, current, _, _) in results.items()
        if quality >= 1 and bandwidth <= 1000 and current <= 0.080
    ]
    assert passing == ["A"]

    resistance = candidates["A"]["resistance"]
    inductance = candidates["A"]["inductance"]
    capacitance = candidates["A"]["capacitance"]
    omega = 500
    reactance = omega * inductance - 1 / (omega * capacitance)
    impedance = math.hypot(resistance, reactance)
    current_peak = 5 / impedance
    phase = -math.atan2(reactance, resistance)
    assert math.isclose(reactance, -150, abs_tol=1e-12)
    assert math.isclose(impedance, math.sqrt(32500), abs_tol=1e-12)
    assert math.isclose(current_peak, 0.0277350098, abs_tol=1e-10)
    assert math.isclose(math.degrees(phase), 56.3099324740, abs_tol=1e-9)


def test_project_is_linked_inactive_and_versioned():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert manifest["maturity"] == "partial"
    assert "0.4.6" in {entry["version"] for entry in manifest["history"]}
    assert "assessment-specs/series-resonance-project-draft.md" in syllabus
    assert "not scheduled or assigned" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
