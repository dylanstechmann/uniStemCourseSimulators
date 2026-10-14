"""Independent solution and unit checks for the first-order ODE primer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/differential-equations"


def test_first_order_solution_equilibrium_time_constant_and_keys():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "differential-equations-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "initial condition",
        "equilibrium",
        "time constant",
        "integrating factor",
        "inverse time",
        "asymptotically",
    ):
        assert concept.lower() in text.lower()

    x_at_4 = 8 * math.exp(-0.25 * 4)
    characteristic_time = 1 / 0.5
    completion_at_one_tau = 1 - math.exp(-1)
    completion_at_three_tau = 1 - math.exp(-3)
    nonzero_equilibrium_at_2s = 4 + (10 - 4) * math.exp(-0.5 * 2)
    assert x_at_4 == pytest.approx(2.9430, abs=0.001)
    assert characteristic_time == pytest.approx(2.0)
    assert completion_at_one_tau == pytest.approx(0.6321, abs=5e-5)
    assert completion_at_three_tau == pytest.approx(0.9502, abs=5e-5)
    assert nonzero_equilibrium_at_2s == pytest.approx(6.2073, abs=0.001)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["differential-equations-1:check"]["solution_spec"][
        "answer"
    ] == pytest.approx(x_at_4, abs=0.01)
    assert items["differential-equations-1:characteristic-time"]["solution_spec"][
        "answer"
    ] == pytest.approx(characteristic_time)

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert "the four former compact readings now have expanded instruction" in syllabus


def test_mass_spring_damper_frequency_and_damping_regimes():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "differential-equations-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "free-body diagram",
        "natural angular frequency",
        "damping ratio",
        "underdamped",
        "critically damped",
        "overdamped",
        "initial displacement",
        "initial velocity",
        "forced response",
    ):
        assert concept.lower() in text.lower()

    mass_kg, spring_n_per_m, damper_n_s_per_m = 2, 8, 3
    natural_frequency = math.sqrt(spring_n_per_m / mass_kg)
    damping_ratio = damper_n_s_per_m / (
        2 * math.sqrt(spring_n_per_m * mass_kg)
    )
    damped_frequency = natural_frequency * math.sqrt(1 - damping_ratio**2)
    assert natural_frequency == pytest.approx(2)
    assert damping_ratio == pytest.approx(0.375)
    assert damped_frequency == pytest.approx(1.854, abs=0.001)

    m2, k2, c2 = 2, 50, 3
    wn2 = math.sqrt(k2 / m2)
    zeta2 = c2 / (2 * math.sqrt(k2 * m2))
    assert wn2 == pytest.approx(5)
    assert zeta2 == pytest.approx(0.15)
    assert wn2 * math.sqrt(1 - zeta2**2) == pytest.approx(4.943, abs=0.001)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["differential-equations-2:check"]["solution_spec"][
        "answer"
    ] == pytest.approx(5)
    assert items["differential-equations-2:force-balance-model"][
        "solution_spec"
    ]["answer"] == 3


def test_coupled_system_jacobian_eigenvalues_and_local_claims():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "differential-equations-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "equilibrium",
        "Taylor expansion",
        "Jacobian",
        "eigenvalue",
        "nullcline",
        "hyperbolic",
        "local",
        "global behavior",
    ):
        assert concept.lower() in text.lower()

    trace_node, determinant_node = -3, 2
    discriminant_node = trace_node**2 - 4 * determinant_node
    node_eigenvalues = (
        (trace_node + math.sqrt(discriminant_node)) / 2,
        (trace_node - math.sqrt(discriminant_node)) / 2,
    )
    trace_spiral, determinant_spiral = -2, 5
    discriminant_spiral = trace_spiral**2 - 4 * determinant_spiral
    spiral_real_part = trace_spiral / 2
    spiral_imaginary_part = math.sqrt(-discriminant_spiral) / 2
    assert node_eigenvalues == pytest.approx((-1, -2))
    assert spiral_real_part == pytest.approx(-1)
    assert spiral_imaginary_part == pytest.approx(2)
    assert max((-2, 0.1)) > 0  # one growing mode is sufficient for instability

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["differential-equations-3:check"]["solution_spec"]["answer"] == 1
    assert items["differential-equations-3:eigenvalue-stability"]["solution_spec"][
        "answer"
    ] == 0


def test_euler_step_stability_boundary_positivity_and_refinement():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "differential-equations-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "forward Euler",
        "global error",
        "stability boundary",
        "strict interval",
        "positivity interval",
        "step refinement",
        "stiff",
    ):
        assert concept.lower() in text.lower()

    one_step = 3 + 0.25 * 2
    decay_rate = 50
    stability_boundary = 2 / decay_rate
    positivity_boundary = 1 / decay_rate
    factor_at_stability_boundary = 1 - decay_rate * stability_boundary
    factor_at_positivity_boundary = 1 - decay_rate * positivity_boundary
    factor_inside = 1 - decay_rate * 0.01
    assert one_step == pytest.approx(3.5)
    assert stability_boundary == pytest.approx(0.04)
    assert factor_at_stability_boundary == pytest.approx(-1)
    assert positivity_boundary == pytest.approx(0.02)
    assert factor_at_positivity_boundary == pytest.approx(0)
    assert 0 < factor_inside < 1

    euler_h_1 = (1 - 0.1) ** 10
    euler_h_2 = (1 - 0.05) ** 20
    exact_at_1 = math.exp(-1)
    error_h_1 = abs(euler_h_1 - exact_at_1)
    error_h_2 = abs(euler_h_2 - exact_at_1)
    assert euler_h_1 == pytest.approx(0.34867844, abs=1e-8)
    assert euler_h_2 == pytest.approx(0.358486)
    assert error_h_2 / error_h_1 == pytest.approx(0.4892, abs=0.001)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["differential-equations-4:check"]["solution_spec"][
        "answer"
    ] == pytest.approx(one_step)
    boundary_item = items["differential-equations-4:euler-stability-limit"]
    assert boundary_item["solution_spec"]["answer"] == pytest.approx(0.04)
    assert "upper stability boundary" in boundary_item["prompt"]
    assert "supremum" in boundary_item["prompt"]


def test_fourier_periodic_feed_harmonics_and_limits():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "differential-equations-7"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("Fourier harmonics", "midpoint", "overshoot"):
        assert concept.lower() in text.lower()

    coefficient = 4 / (3 * math.pi)
    third_harmonic_gain = 1 / math.sqrt(1 + (3 * 2 * 0.5) ** 2)
    fundamental_amplitude = (4 / math.pi) / math.sqrt(1 + (2 * math.pi / 3) ** 2)
    third_output_amplitude = coefficient / math.sqrt(1 + (2 * math.pi) ** 2)
    assert coefficient == pytest.approx(0.4244, abs=0.0001)
    assert third_harmonic_gain == pytest.approx(0.3162, abs=0.0001)
    assert fundamental_amplitude == pytest.approx(0.5486, abs=0.0001)
    assert third_output_amplitude == pytest.approx(0.0667, abs=0.0001)

    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    items = {item["id"]: item for item in bank["questions"]}
    # Keys are four-decimal display values; compare within each item's grading tolerance.
    for key, exact in (
        ("third-harmonic-coefficient", coefficient),
        ("third-harmonic-gain", third_harmonic_gain),
    ):
        spec = items[f"differential-equations-7:{key}"]["solution_spec"]
        assert spec["answer"] == pytest.approx(exact, abs=spec["tolerance"])
        assert spec["answer"] == pytest.approx(exact, abs=0.0001)
    assert items["differential-equations-7:harmonic-superposition"][
        "solution_spec"
    ]["answer"] == 0
    assert items["differential-equations-7:fourier-jump-limit"][
        "solution_spec"
    ]["answer"] == 0


def test_original_objectives_link_to_outcomes_and_have_direct_evidence():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    expected_links = {
        "differential-equations-1-objective-1": ["differential-equations-outcome-1"],
        "differential-equations-1-objective-2": ["differential-equations-outcome-2"],
        "differential-equations-2-objective-1": ["differential-equations-outcome-2"],
        "differential-equations-2-objective-2": ["differential-equations-outcome-1"],
        "differential-equations-3-objective-1": ["differential-equations-outcome-2"],
        "differential-equations-3-objective-2": ["differential-equations-outcome-2"],
        "differential-equations-4-objective-1": ["differential-equations-outcome-4"],
        "differential-equations-4-objective-2": ["differential-equations-outcome-4"],
        "differential-equations-7-objective-4": ["differential-equations-outcome-1", "differential-equations-outcome-2"],
    }
    for objective_id, outcome_ids in expected_links.items():
        assert objectives[objective_id]["course_outcome_ids"] == outcome_ids

    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    items = {item["id"]: item for item in bank["questions"]}
    assert items["differential-equations-3:check"]["objective_ids"] == [
        "differential-equations-3-objective-2"
    ]
    damping = items["differential-equations-2:damping-regime"]
    linearization = items["differential-equations-3:linearization"]
    assert damping["solution_spec"]["answer"] == 1
    assert damping["objective_ids"] == ["differential-equations-2-objective-1"]
    assert linearization["solution_spec"]["answer"] == 1
    assert linearization["objective_ids"] == ["differential-equations-3-objective-1"]
    assert 8 / (2 * (8 * 2) ** 0.5) == pytest.approx(1)
    assert (1 + 0.01) * (1 - (1 + 0.01)) == pytest.approx(-0.0101)

    for lesson_number, added_question in ((2, damping["id"]), (3, linearization["id"])):
        lesson_id = f"differential-equations-{lesson_number}"
        lesson = next(
            lesson for module in manifest["modules"] for lesson in module["lessons"]
            if lesson["id"] == lesson_id
        )
        assessment = next(
            item for item in manifest["assessments"]
            if item["id"] == f"{lesson_id}-practice"
        )
        assert added_question in lesson["question_ids"]
        assert set(lesson["question_ids"]) == set(assessment["question_ids"])
        assert f"differential-equations-outcome-{2 if lesson_number < 4 else 4}" in assessment["objective_ids"]
