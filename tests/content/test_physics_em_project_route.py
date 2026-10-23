"""Independently check the learner-facing series-resonance rehearsal and routes."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-em"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
QUESTIONS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
PREFIX = "physics-em-project:rehearsal-"


def half_power_frequency(target_reactance: float, inductance=0.040, capacitance=4e-6) -> float:
    """Solve X(ω) = ±R by bisection instead of the guide's quadratic formula."""
    low, high = 1.0, 1e6
    for _ in range(80):
        middle = (low + high) / 2
        reactance = middle * inductance - 1 / (middle * capacitance)
        if reactance < target_reactance:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def rehearsal_answers() -> dict[str, dict[str, float]]:
    r, inductance, capacitance, voltage_peak = 64, 0.040, 4e-6, 3.0
    omega0 = 1 / math.sqrt(inductance * capacitance)
    current_peak = voltage_peak / r
    current_rms = current_peak / math.sqrt(2)
    impedance = complex(r, 800 * inductance - 1 / (800 * capacitance))
    return {
        "resonance": {"omega0": omega0, "f0": omega0 / math.tau},
        "q-bandwidth": {
            "quality": math.sqrt(inductance / capacitance) / r,
            "bandwidth": half_power_frequency(r) - half_power_frequency(-r),
            "low": half_power_frequency(-r),
            "high": half_power_frequency(r),
        },
        "power-energy": {
            "i_rms": current_rms,
            "power": current_rms**2 * r,
            "w_max": inductance * current_peak**2 / 2 * 1e6,
            "v_c_peak": current_peak / (omega0 * capacitance),
        },
        "off-resonance": {
            "reactance": impedance.imag,
            "impedance": abs(impedance),
            "current": abs(voltage_peak / impedance),
        },
    }


@pytest.mark.parametrize("suffix,answers", rehearsal_answers().items())
def test_independently_computed_answers_earn_credit_at_the_requested_precision(suffix, answers):
    question = QUESTIONS[PREFIX + suffix]
    assert "three significant figures" in question["prompt"]
    # Choice reasoning is checked below; numeric responses come only from the independent model.
    response = {
        field["id"]: str(field["answer"])
        for field in question["solution_spec"]["field_specs"]
        if field["type"] == "single_choice"
    }
    response.update({field: format(value, ".2e") for field, value in answers.items()})
    result = grade(question, AttemptRequest(response=response))
    assert result.correct, [(field.field_id, field.diagnosis) for field in result.feedback.components]
    for field in question["solution_spec"]["field_specs"]:
        if field["type"] != "numeric":
            continue
        assert field["significant_figures"] == 3
        wrong = {**response, field["id"]: format(answers[field["id"]] * 1.2, ".2e")}
        assert not grade(question, AttemptRequest(response=wrong)).correct


def selected(suffix: str, field_id: str) -> str:
    question = QUESTIONS[PREFIX + suffix]
    field = next(item for item in question["response_fields"] if item["id"] == field_id)
    key = next(item for item in question["solution_spec"]["field_specs"] if item["id"] == field_id)
    return field["options"][key["answer"]]


def test_rehearsal_selection_and_phase_match_the_model():
    answers = rehearsal_answers()
    assert answers["q-bandwidth"]["quality"] >= 1
    assert answers["q-bandwidth"]["bandwidth"] > 1000
    assert 3 / 64 <= 0.080
    assert selected("selection", "q_check").startswith("Yes:")
    assert selected("selection", "bw_check").startswith("No:")
    assert selected("selection", "i_check").startswith("Yes:")
    assert selected("selection", "binding").startswith("The bandwidth:")
    assert answers["off-resonance"]["reactance"] < 0
    assert "current leads" in selected("off-resonance", "lead_lag")
    phase = math.degrees(math.atan2(-answers["off-resonance"]["reactance"], 64))
    assert round(phase, 1) == 77.1
    assert "quarter-cycle" in selected("power-energy", "simultaneity")
    assert "2π radians" in selected("resonance", "conversion")
    assert "Only ω₀ and f₀" in selected("q-bandwidth", "r_change")
    assert "constant L and R" in selected("scope", "linearity")
    assert "cannot establish that the system is an ideal linear series RLC" in selected("scope", "curve_limits")
    assert "Only the response of this synthetic circuit" in selected("scope", "scope")


@pytest.mark.parametrize("reactance", ["-2.80e2", "-2.81e2"])
def test_halfway_reactance_accepts_both_three_figure_rounding_conventions(reactance):
    # -280.5 Ω is exactly halfway; the prompt does not prescribe a tie-breaking convention.
    question = QUESTIONS[PREFIX + "off-resonance"]
    response = {"reactance": reactance, "impedance": "288", "current": "0.0104", "lead_lag": "0"}
    assert grade(question, AttemptRequest(response=response)).correct


def test_worked_example_matches_the_guide_and_lesson_summary():
    r, inductance, capacitance, voltage_peak = 250, 0.010, 1e-6, 8.0
    omega0 = 1 / math.sqrt(inductance * capacitance)
    low = half_power_frequency(-r, inductance, capacitance)
    high = half_power_frequency(r, inductance, capacitance)
    current = voltage_peak / complex(r, 50000 * inductance - 1 / (50000 * capacitance))
    assert round(low) == 3508 and round(high) == 28508
    assert math.isclose(high - low, r / inductance)
    peak = voltage_peak / r
    capacitor_peak = peak / (omega0 * capacitance)
    assert math.isclose((peak / math.sqrt(2)) ** 2 * r, 0.128)
    assert math.isclose(inductance * peak**2 / 2, capacitance * capacitor_peak**2 / 2)
    assert round(abs(current), 4) == 0.0148
    assert round(math.degrees(math.atan2(current.imag, current.real)), 1) == -62.5
    guide = (COURSE / "assignments/series-resonance-project-guide.md").read_text(encoding="utf-8")
    lesson = next(
        lesson for module in MANIFEST["modules"] for lesson in module["lessons"]
        if lesson["id"] == "physics-em-project-guide"
    )
    frequency = f"{omega0 / math.tau:.1f}"
    assert f"{frequency} Hz" in guide
    assert f"{frequency} Hz" in lesson["worked_example"]


def test_project_has_a_scheduled_guide_practice_and_ungraded_milestones():
    lessons = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
    assessments = {item["id"]: item for item in MANIFEST["assessments"]}
    weeks = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
    guide = lessons["physics-em-project-guide"]
    rehearsal = assessments["physics-em-project-rehearsal-practice"]
    project = assessments["physics-em-rlc-project"]
    assert MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert (COURSE / guide["reading"]).is_file()
    assert guide["id"] in weeks[13]["lesson_ids"]
    assert rehearsal["id"] in weeks[13]["assessment_ids"]
    assert rehearsal["mode"] == "practice"
    assert set(rehearsal["question_ids"]) == set(guide["question_ids"])
    assert len(rehearsal["question_ids"]) == 6
    assert project["id"] in weeks[14]["assessment_ids"]
    assert (project["mode"], project["points"], project["question_ids"]) == ("self-assessment", 0, [])
    cases = json.loads((COURSE / MANIFEST["case_rubrics"]).read_text(encoding="utf-8"))["cases"]
    milestones = [case for case in cases if ":project-m" in case["id"]]
    assert len(milestones) == 6
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "labs/loading-reports.csv" in MANIFEST["learner_resources"]
    lab = (COURSE / "labs/01-calibration-loading-and-time-constants.md").read_text(encoding="utf-8")
    assert "](loading-reports.csv)" in lab
