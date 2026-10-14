"""Independent equation checks for the bioreactors growth primer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/bioreactors"


def test_growth_rate_doubling_time_and_cell_balance():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "bioreactors-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "specific growth rate",
        "total viable cell number",
        "substrate",
        "loss rate",
        "exponential assumption",
    ):
        assert concept.lower() in text.lower()

    growth_rate = math.log(2) / 30
    doubling_time = math.log(2) / (math.log(1_280_000 / 200_000) / 24)
    fourfold_rate = math.log(4) / 48
    batch_accumulation = (0.030 - 0.005) * 2e9
    assert growth_rate == pytest.approx(0.0231, abs=5e-5)
    assert doubling_time == pytest.approx(8.962, abs=0.01)
    assert fourfold_rate == pytest.approx(0.0289, abs=5e-5)
    assert batch_accumulation == pytest.approx(5e7)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["bioreactors-1:check"]["solution_spec"]["answer"] == pytest.approx(0.0231)
    assert items["bioreactors-1:doubling-time"]["solution_spec"]["answer"] == pytest.approx(
        8.962
    )

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "all four original compact prototype readings have expanded primers" in syllabus.lower()


def test_oxygen_transfer_uptake_units_and_dynamic_balance():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "bioreactors-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "OTR=k_La(C^*-C)",
        "OUR=q_{O_2}X_v",
        r"\frac{dC}{dt}",
        "chosen target",
        "bulk probe",
    ):
        assert concept.lower() in text.lower()

    specific_uptake = 1e-16  # mol/(cell s)
    viable_density = 2e6 * 1000  # cells/L
    demand_mmol_l_h = specific_uptake * viable_density * 3600 * 1000
    transfer_mmol_l_h = 10 * (0.20 - 0.10)
    demand_at_second_example = 1.5
    accumulation_mmol_l_h = transfer_mmol_l_h - demand_at_second_example
    steady_bulk_do = 0.20 - demand_at_second_example / 10
    target_capacity = 10 * (0.20 - 0.10)
    critical_density = target_capacity / 1e-10

    assert demand_mmol_l_h == pytest.approx(0.72)
    assert transfer_mmol_l_h == pytest.approx(1.00)
    assert accumulation_mmol_l_h == pytest.approx(-0.50)
    assert steady_bulk_do == pytest.approx(0.05)
    assert critical_density == pytest.approx(1e10)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["bioreactors-2:check"]["solution_spec"]["answer"] == pytest.approx(0.72)
    assert items["bioreactors-2:oxygen-supply-vs-demand"]["solution_spec"][
        "answer"
    ] == pytest.approx(-0.5)
    assert items["bioreactors-2:check"]["objective_ids"] == [
        "bioreactors-2-objective-2"
    ]
    assert items["bioreactors-2:oxygen-supply-vs-demand"]["objective_ids"] == [
        "bioreactors-2-objective-1",
        "bioreactors-2-objective-2",
    ]


def test_geometric_scale_up_criteria_and_legacy_answers():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "bioreactors-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "constant tip speed",
        "power per volume",
        "Reynolds number",
        "mixing time",
        "scale-down",
        "geometrically similar",
    ):
        assert concept.lower() in text.lower()

    volume_ratio = 200 / 2
    linear_scale = volume_ratio ** (1 / 3)
    speed_ratio_at_constant_tip = 1 / linear_scale
    speed_ratio_at_constant_power_density = linear_scale ** (-2 / 3)
    tip_speed_ratio_at_constant_power_density = (
        speed_ratio_at_constant_power_density * linear_scale
    )

    assert linear_scale == pytest.approx(4.6416, abs=5e-5)
    assert speed_ratio_at_constant_tip == pytest.approx(0.2154, abs=5e-5)
    assert speed_ratio_at_constant_power_density == pytest.approx(0.3594, abs=5e-5)
    assert tip_speed_ratio_at_constant_power_density == pytest.approx(1.6681, abs=5e-5)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["bioreactors-3:check"]["solution_spec"]["answer"] == 0
    assert items["bioreactors-3:similarity-constraints"]["solution_spec"][
        "answer"
    ] == 1
    reynolds = items["bioreactors-3:reynolds-number"]
    assert reynolds["solution_spec"]["answer"] == pytest.approx(8000)
    assert reynolds["objective_ids"] == ["bioreactors-3-objective-1"]
    assert 1000 * 0.80 * 0.10**2 / 0.001 == pytest.approx(8000)


def test_monitoring_control_and_quality_evidence():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "bioreactors-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "critical process parameter",
        "critical quality attribute",
        "control loop",
        "sensor bias",
        "acceptance criteria",
        "raw values",
        "sterile boundary",
        "log-reduction calculation",
        "no detection",
    ):
        assert concept.lower() in text.lower()

    reference_value = 100
    reference_tolerance = 0.02
    initial_titre = 100
    final_titre = 80
    titre_decline = (initial_titre - final_titre) / initial_titre
    relative_scale = titre_decline / reference_tolerance
    assert titre_decline == pytest.approx(0.20)
    assert relative_scale == pytest.approx(10)
    assert reference_value * (1 - reference_tolerance) == pytest.approx(98)
    assert reference_value * (1 + reference_tolerance) == pytest.approx(102)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["bioreactors-4:check"]["solution_spec"]["answer"] == 0
    assert items["bioreactors-4:drift-vs-assay-variation"]["solution_spec"][
        "answer"
    ] == 0
    assert items["bioreactors-4:modeled-survivors"]["solution_spec"][
        "answer"
    ] == pytest.approx(120)
    assert 1.2e6 * 10**-4 == pytest.approx(120)
    assert items["bioreactors-4:contamination-pathways"]["solution_spec"][
        "answer"
    ] == 0
    assert items["bioreactors-4:sterility-evidence-limits"]["solution_spec"][
        "answer"
    ] == 0


def test_original_objectives_map_to_supported_process_outcomes():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    expected = {
        "bioreactors-1-objective-1": ["bioreactors-outcome-3"],
        "bioreactors-1-objective-2": ["bioreactors-outcome-3"],
        "bioreactors-2-objective-1": ["bioreactors-outcome-2"],
        "bioreactors-2-objective-2": ["bioreactors-outcome-2"],
        "bioreactors-3-objective-1": ["bioreactors-outcome-2"],
        "bioreactors-3-objective-2": ["bioreactors-outcome-2"],
        "bioreactors-4-objective-1": ["bioreactors-outcome-4"],
        "bioreactors-4-objective-2": ["bioreactors-outcome-3", "bioreactors-outcome-4"],
        "bioreactors-4-objective-3": ["bioreactors-outcome-4"],
    }
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    for objective_id, outcome_ids in expected.items():
        assert objectives[objective_id]["course_outcome_ids"] == outcome_ids

    for lesson_number, outcome_ids in (
        (1, ["bioreactors-outcome-3"]),
        (2, ["bioreactors-outcome-2"]),
        (3, ["bioreactors-outcome-2"]),
        (4, ["bioreactors-outcome-3", "bioreactors-outcome-4"]),
    ):
        assessment = next(
            item for item in manifest["assessments"]
            if item["id"] == f"bioreactors-{lesson_number}-practice"
        )
        assert set(outcome_ids).issubset(assessment["objective_ids"])
