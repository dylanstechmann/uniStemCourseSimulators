"""Arithmetic and inactive-status checks for the Circuits design-project draft."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/circuits"
PROJECT = COURSE / "assessment-specs/integrative-sensor-channel-project-draft.md"


def test_ideal_sensor_channel_values_recalculate_independently():
    source_resistance = 1_000.0
    amplifier_input_resistance = 1_000_000.0
    loading_fraction = amplifier_input_resistance / (
        source_resistance + amplifier_input_resistance
    )

    differential_gain = 200.0
    common_mode_rejection_db = 80.0
    common_mode_gain = differential_gain / 10 ** (common_mode_rejection_db / 20)
    common_mode_error_out = common_mode_gain * 0.5
    common_mode_error_in = common_mode_error_out / differential_gain
    output_range = (
        2.5 - differential_gain * 0.005 - common_mode_error_out,
        2.5 + differential_gain * 0.005 + common_mode_error_out,
    )

    corner_hz = 1 / (2 * math.pi * 8_200 * 1e-6)
    def magnitude(frequency: float) -> float:
        return 1 / math.sqrt(1 + (frequency / corner_hz) ** 2)

    adc_step_v = 5 / 2**12

    assert loading_fraction == pytest.approx(0.999001, abs=1e-6)
    assert common_mode_gain == pytest.approx(0.02)
    assert common_mode_error_out == pytest.approx(0.01)
    assert common_mode_error_in == pytest.approx(50e-6)
    assert output_range == pytest.approx((1.49, 3.51))
    assert corner_hz == pytest.approx(19.4091, abs=0.001)
    assert magnitude(5) == pytest.approx(0.9684, abs=1e-4)
    assert magnitude(50) == pytest.approx(0.362, abs=0.001)
    assert 100 / 2 == 50
    assert adc_step_v == pytest.approx(1.220703125e-3)
    assert adc_step_v / differential_gain == pytest.approx(6.103515625e-6)


def test_circuits_capstone_remains_an_ungraded_draft_outside_the_schedule():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    project = PROJECT.read_text(encoding="utf-8")
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert all("integrative-sensor-channel-project" not in item["id"] for item in manifest["assessments"])
    assert "Inactive authoring draft" in project
    assert "no points, course grade or submission path" in project
    assert "not scheduled, submitted or graded" in syllabus
    assert "not a hardware build" in project
