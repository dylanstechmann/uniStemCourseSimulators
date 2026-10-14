"""PID action, windup, sampled implementation, and source regressions."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/signals-control"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_controller_reading_maps_objectives_and_preserves_pid_items():
    manifest = load(COURSE / "course.json")
    assert manifest["version"].startswith("0.4.")
    module = next(
        item
        for item in manifest["modules"]
        if item["id"] == "signals-control-module-4"
    )
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) > 1_000
    for concept in (
        "u(t) = Kp e(t) + Ki ∫ e(τ) dτ + Kd de(t)/dt",
        "Proportional action responds to the error that exists now",
        "Integral action responds to accumulated error",
        "Derivative action responds to the error's rate of change",
        "integrator windup",
        "zero-order hold",
        "quantize measurements and commands",
    ):
        assert concept.lower() in text.lower()

    objectives = {item["id"]: item for item in manifest["lesson_objectives"]}
    expected_outcomes = [
        "signals-control-outcome-3",
        "signals-control-outcome-4",
    ]
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["course_outcome_ids"] == expected_outcomes
    assessment = next(
        item
        for item in manifest["assessments"]
        if item["id"] == "signals-control-4-practice"
    )
    assert set(expected_outcomes).issubset(set(assessment["objective_ids"]))

    bank = load(COURSE / "question-banks/practice.json")
    items = {item["id"]: item for item in bank["questions"]}
    integral = items["signals-control-4:check"]
    windup = items["signals-control-4:integrator-windup"]
    assert integral["prompt"] == (
        "Which PID term is most directly responsible for eliminating a constant "
        "steady-state error in many systems?"
    )
    assert integral["options"][integral["solution_spec"]["answer"]] == "Integral"
    assert windup["prompt"] == (
        "A PI controller's actuator saturates for several seconds during a large "
        "setpoint step. After the step, the output overshoots badly. What is the "
        "most likely cause?"
    )
    assert windup["solution_spec"]["answer"] == 0
    assert {integral["id"], windup["id"]} == set(lesson["question_ids"])


def test_pid_and_digital_control_sources_are_link_only_and_mapped():
    expected = {"mit-ocw-pid-windup", "mit-ocw-digital-control"}
    registry = load(ROOT / "content/sources/registry.json")
    sources = {item["id"]: item for item in registry["sources"]}
    for source_id in expected:
        source = sources[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }
        assert "signals-control-module-4" in source["mapped_modules"]

    source_map = load(COURSE / "source-map.json")
    mapping = next(
        item
        for item in source_map["modules"]
        if item["module_id"] == "signals-control-module-4"
    )
    assert expected.issubset(set(mapping["source_ids"]))
