"""Independent calculations and learner routes for the final eight planned projects."""
from __future__ import annotations

import cmath
import csv
import json
import math
import re
from pathlib import Path
from statistics import NormalDist

import pytest
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSES = ROOT / "content/courses"
PLANS = {
    "circuits": ("sensor-channel", 13),
    "physiology": ("renal-clearance", 11),
    "signals-control": ("sampled-loop", 13),
    "general-chemistry-1": ("gas-equilibrium", 10),
    "organic-chemistry": ("aldol-identity", 11),
    "statistics": ("confirmatory-protocol", 14),
    "robotics": ("trajectory-margin", 13),
    "geroscience": ("surrogate-evidence", 14),
}


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def parameters(cid, slug):
    with (COURSES / cid / f"assignments/{slug}-rehearsal.csv").open(encoding="utf-8", newline="") as stream:
        return {row["parameter"]: float(row["value"]) for row in csv.DictReader(stream)}


def circuits_answers():
    p = parameters("circuits", "sensor-channel")
    differential = p["gain"] * p["terminal_differential_peak"]
    ratio = math.exp(math.log(10) * p["cmrr"] / 20)
    output_error = p["gain"] * p["common_mode_peak"] / ratio
    rc = p["filter_resistance"] * p["filter_capacitance"]
    def gain(f):
        return abs(1 / complex(1, math.tau * f * rc))
    step = p["adc_span"] / (1 << int(p["adc_bits"]))
    return {
        1: {"loading": 1 / (1 + p["source_resistance"] / p["input_resistance"]),
            "low": p["reference"] - differential, "high": p["reference"] + differential},
        2: {"cmrr": ratio, "error_output": output_error, "error_input": output_error / p["gain"] * 1e6},
        3: {"corner": 1 / (math.tau * rc), "signal_gain": gain(p["signal_frequency"]),
            "disturbance_gain": gain(p["disturbance_frequency"]), "nyquist": p["sample_rate"] / 2},
        4: {"lsb": step * 1000, "input_step": step / p["gain"] * 1e6},
    }


def physiology_answers():
    with (COURSES / "physiology/assignments/renal-clearance-rehearsal.csv").open(encoding="utf-8", newline="") as stream:
        rows = {row["substance"]: row for row in csv.DictReader(stream)}
    def ledger(name):
        row = rows[name]
        plasma = float(row["plasma_mg_per_ml"])
        excretion = float(row["urine_mg_per_ml"]) * float(row["flow_ml_per_min"])
        return plasma, excretion, excretion / plasma
    _, reference_excretion, gfr = ledger("reference")
    pa, ea, ca = ledger("A")
    pc, ec, cc = ledger("C")
    pg, eg, _ = ledger("glucose")
    tm = float(rows["glucose"]["tm_mg_per_min"])
    assert eg == pytest.approx(max(gfr * pg - tm, 0))
    return {
        1: {"gfr": gfr, "reference_rate": reference_excretion},
        2: {"clearance_a": ca, "filtered_a": gfr * pa, "excreted_a": ea, "fraction_a": ca / gfr},
        3: {"clearance_c": cc, "net_c": ec - gfr * pc, "fraction_c": cc / gfr},
        4: {"filtered_glucose": gfr * pg, "excreted_glucose": eg, "threshold": tm / gfr},
    }


def signals_answers():
    p = parameters("signals-control", "sampled-loop")
    ts = p["sample_period"]
    fs = 1 / ts
    alias = min(abs(p["disturbance_frequency"] - k * fs) for k in range(-10, 11))
    def transfer(f):
        return abs(1 / complex(1, f / p["filter_corner"]))
    omega_ts = p["crossover"] * ts
    hold = (1 - cmath.exp(-1j * omega_ts)) / (1j * omega_ts)
    phase = -cmath.phase(hold)
    proportional_change = p["kp"] * (p["error"] - p["previous_error"])
    integral_change = p["kp"] / p["ti"] * ts * p["error"]
    candidate = p["previous_output"] + proportional_change + integral_change
    applied = max(0, min(p["command_max"], candidate))
    decay = math.exp(-ts / p["plant_tau"])
    equilibrium = p["plant_gain"] * applied
    next_state = equilibrium + (p["old_state"] - equilibrium) * decay
    return {
        1: {"sample_frequency": fs, "nyquist": fs / 2, "alias": alias},
        2: {"disturbance_gain": transfer(p["disturbance_frequency"]), "signal_gain": transfer(p["signal_frequency"])},
        3: {"period_bound": p["closed_loop_tau"] / 10, "hold_radians": phase,
            "hold_degrees": math.degrees(phase), "remaining_margin": p["margin"] - math.degrees(phase)},
        4: {"candidate": candidate, "applied": applied},
        5: {"decay": decay, "next_state": next_state},
    }


def chemistry_answers():
    p = parameters("general-chemistry-1", "gas-equilibrium")
    initial_a, initial_b = p["initial_a"], p["initial_b"]
    beta, target = p["beta"], p["equilibrium_constant"]
    lo, hi = -initial_b / 2, initial_a
    # Solve the original mass-action expression, rather than the author's factored quadratic.
    for _ in range(100):
        extent = (lo + hi) / 2
        quotient = beta * (initial_b + 2 * extent) ** 2 / (initial_a - extent)
        if quotient < target:
            lo = extent
        else:
            hi = extent
    extent = (lo + hi) / 2
    a, b = initial_a - extent, initial_b + 2 * extent
    return {
        1: {"extent_max": initial_a, "conserved": 2 * initial_a + initial_b},
        2: {"activity_a": beta * initial_a},
        3: {"extent": extent, "amount_a": a, "amount_b": b},
        4: {"enthalpy": extent * p["reaction_enthalpy"], "equilibrium_q": beta * b * b / a,
            "unit_total": 2 * a + b},
        5: {"perturbed_q": beta * (b / 2) ** 2 / a},
    }


def organic_answers():
    guide = (COURSES / "organic-chemistry/assignments/aldol-identity-project-guide.md").read_text(encoding="utf-8")
    rehearsal = guide.split("## Rehearsal: practice before the project", 1)[1]
    formulas = re.findall(r"\((C\d+H\d+O\d*)\)", rehearsal)
    assert formulas == ["C4H8O", "C8H8O"]
    def atoms(formula):
        return {element: int(count or 1) for element, count in re.findall(r"([A-Z][a-z]?)(\d*)", formula)}
    left, right = map(atoms, formulas)
    added = {element: left.get(element, 0) + right.get(element, 0) for element in left.keys() | right.keys()}
    dehydrated = {**added, "H": added["H"] - 2, "O": added["O"] - 1}
    def dbe(molecule):
        return molecule["C"] + 1 - molecule["H"] / 2
    with (COURSES / "organic-chemistry/assignments/aldol-identity-rehearsal.csv").open(encoding="utf-8", newline="") as stream:
        totals = {row["card"]: sum(int(value) for column, value in row.items() if column.endswith("_H"))
                  for row in csv.DictReader(stream)}
    tetrahedral_neighbors = [("CHO", "ethyl", "carbinol", "H"), ("aryl", "OH", "alpha", "H")]
    centers = sum(len(set(neighbors)) == 4 for neighbors in tetrahedral_neighbors)
    return {
        2: {"carbon": added["C"], "hydrogen_addition": added["H"], "oxygen_addition": added["O"],
            "hydrogen_dehydrated": dehydrated["H"]},
        3: {"dbe_addition": dbe(added), "dbe_dehydrated": dbe(dehydrated)},
        4: {"card_x_total": totals["X"], "card_y_total": totals["Y"]},
        5: {"centers": centers},
    }


def statistics_answers():
    p = parameters("statistics", "confirmatory-protocol")
    # Recompute quantiles from probabilities rather than the author's rounded critical values.
    critical_sum = NormalDist().inv_cdf(1 - p["alpha"] / 2) + NormalDist().inv_cdf(p["power"])
    def required(sigma):
        return math.ceil(2 * (critical_sum * sigma / p["target_effect"]) ** 2)
    retained = required(p["sigma"])
    sensitive = required(p["sensitivity_sigma"])
    units = 2 * p["pilot_units_per_arm"]
    m, alpha = p["secondary_tests"], p["family_alpha"]
    return {
        1: {"units": units, "observations": units * p["technical_repeats"]},
        3: {"retained": retained, "recruit": math.ceil(retained / (1 - p["attrition"])),
            "sensitive_retained": sensitive, "sensitive_recruit": math.ceil(sensitive / (1 - p["attrition"]))},
        4: {"threshold": alpha / m, "family_probability": -math.expm1(m * math.log1p(-alpha)),
            "expected_false": m * alpha},
    }


def robotics_answers():
    p = parameters("robotics", "trajectory-margin")
    angle, duration = p["displacement"], p["evaluation_duration"]
    # Differentiate the polynomial in normalized time rather than substituting an authored bound.
    def speed_at(s, t):
        return angle * (6 * s - 6 * s * s) / t
    def acceleration_at(s, t):
        return angle * (6 - 12 * s) / (t * t)
    def torque_at(s, t):
        return (p["inertia"] * acceleration_at(s, t)
            + p["mass"] * p["gravity"] * p["radius"] * math.cos(angle * (3 * s * s - 2 * s**3)))
    speed = max(speed_at(i / 1000, duration) for i in range(1001))
    acceleration = max(abs(acceleration_at(i / 1000, duration)) for i in range(1001))
    torque = max(torque_at(i / 1000, duration) for i in range(1001))
    def stopping(v):
        return v * p["latency"] + v * v / (2 * p["braking"]) + p["position_allowance"]
    def feasible(t):
        v = speed_at(.5, t)
        return (v <= p["speed_limit"] and torque_at(0, t) <= p["torque_limit"]
                and stopping(v) <= p["clearance"])
    low, high = .01, 10.0
    for _ in range(100):
        middle = (low + high) / 2
        if feasible(middle):
            high = middle
        else:
            low = middle
    candidates = [p[f"candidate_{i}"] for i in (1, 2, 3)]
    chosen = min(t for t in candidates if feasible(t))
    # Simpson integration of torque times velocity independently closes the work ledger.
    intervals = 2000
    def power(s):
        return torque_at(s, duration) * speed_at(s, duration)
    weighted = power(0) + power(1)
    weighted += sum((4 if i % 2 else 2) * power(i / intervals) for i in range(1, intervals))
    work = weighted * duration / (3 * intervals)
    return {
        1: {"speed": speed, "acceleration": acceleration},
        2: {"gravity": torque_at(.5, duration) / math.cos(angle / 2), "torque": torque},
        3: {"stopping": stopping(speed), "reserve": p["clearance"] - stopping(speed)},
        4: {"continuous": high, "candidate": chosen},
        5: {"work": work},
    }


def geroscience_answers():
    with (COURSES / "geroscience/assignments/surrogate-evidence-rehearsal.csv").open(encoding="utf-8", newline="") as stream:
        rows = {row["study_id"]: row for row in csv.DictReader(stream)}
    def number(row, column):
        return float(rows[row][column])
    def width(row, endpoint):
        return number(row, endpoint + "_ci_high") - number(row, endpoint + "_ci_low")
    return {
        1: {"marker_width": width("X", "marker"), "function_width": width("X", "function")},
        3: {"marker_width": width("Y", "marker"), "hr_distance": abs(number("Y", "survival_hazard_ratio") - 1)},
        4: {"hazard_reduction": 1 - number("Z", "survival_hazard_ratio"),
            "function_margin": number("Z", "function_ci_low")},
        5: {"randomized_contexts": sum(row["design"].startswith("randomized") for row in rows.values())},
    }


CALCULATIONS = {"circuits": circuits_answers, "physiology": physiology_answers,
                "signals-control": signals_answers, "general-chemistry-1": chemistry_answers,
                "organic-chemistry": organic_answers, "statistics": statistics_answers,
                "robotics": robotics_answers, "geroscience": geroscience_answers}


@pytest.mark.parametrize("cid", PLANS)
def test_project_routes_are_scheduled_and_open(cid):
    slug, week = PLANS[cid]
    directory = COURSES / cid
    manifest = read(directory / "course.json")
    assert manifest["maturity"] == "partial" and manifest["review"]["status"] == "unreviewed"
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert manifest["grading_policy"]["mode"] == "formative-only"
    lesson = next(lesson for module in manifest["modules"] for lesson in module["lessons"]
                  if lesson["id"] == f"{cid}-project-guide")
    guide = (directory / lesson["reading"]).read_text(encoding="utf-8")
    assert lesson["reading"] == f"assignments/{slug}-project-guide.md"
    assert len(guide.split()) >= 1000
    assert "## Worked example: a separate case" in guide
    assert "## Rehearsal: practice before the project" in guide
    assert "substantial AI assistance" in guide
    weeks = {item["week"]: item for item in manifest["duration"]["weeks"]}
    assessments = {item["id"]: item for item in manifest["assessments"]}
    practice = assessments[f"{cid}-project-rehearsal-practice"]
    project = assessments[f"{cid}-project-milestones"]
    assert lesson["id"] in weeks[week]["lesson_ids"]
    assert practice["id"] in weeks[week]["assessment_ids"]
    assert practice["mode"] == "practice" and len(practice["question_ids"]) == 5
    assert practice["question_ids"] == lesson["question_ids"]
    assert (project["mode"], project["question_ids"], project["points"]) == ("self-assessment", [], 0)
    assert project["id"] in manifest["duration"]["weeks"][-1]["assessment_ids"]
    cases = read(directory / manifest["case_rubrics"])["cases"]
    assert cases[0]["id"] == f"{cid}:case"
    milestones = [case for case in cases if ":project-m" in case["id"]]
    assert len(milestones) == 5
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    bank = {item["id"]: item for item in read(directory / "question-banks/practice.json")["questions"]}
    assert practice["points"] == sum(bank[qid]["points"] for qid in practice["question_ids"])
    content = ContentRepository(ROOT / "content")
    delivered = content.lesson(cid, lesson["id"])
    assert len(delivered.questions) == 5 and len(delivered.retrieval_cards) == 5
    assert "../assignments/" not in delivered.markdown
    for resource in manifest["learner_resources"]:
        assert content.learner_resource(cid, resource) == (directory / resource).read_bytes()


@pytest.mark.parametrize("cid", PLANS)
def test_rehearsal_numeric_answers_recompute_at_the_requested_precision(cid):
    bank = read(COURSES / cid / "question-banks/practice.json")["questions"]
    questions = [q for q in bank if q["id"].startswith(f"{cid}-project:rehearsal-")]
    assert len(questions) == 5
    calculations = CALCULATIONS[cid]()
    for question in questions:
        number = int(question["id"].rsplit("-", 1)[-1])
        numeric = calculations.get(number, {})
        response = {}
        for spec in question["solution_spec"]["field_specs"]:
            fid = spec["id"]
            if spec["type"] == "numeric":
                assert spec.get("significant_figures") in (3, None)
                if spec.get("significant_figures") is None:
                    assert float(numeric[fid]).is_integer()
                    response[fid] = str(int(numeric[fid]))
                else:
                    response[fid] = format(numeric[fid], ".2e")
            else:
                response[fid] = str(spec["answer"])
        result = grade(question, AttemptRequest(response=response))
        assert result.correct, (question["id"], [(c.field_id, c.diagnosis) for c in result.feedback.components])
        assert set(numeric) == {s["id"] for s in question["solution_spec"]["field_specs"] if s["type"] == "numeric"}
        for fid, value in numeric.items():
            wrong = {**response, fid: format(value * 1.2, ".2e")}
            assert not grade(question, AttemptRequest(response=wrong)).correct


def test_circuits_voltage_basis_and_code_scale_are_consistent():
    answers = circuits_answers()
    assert answers[1]["low"] == pytest.approx(1.36)
    assert answers[1]["high"] == pytest.approx(2.64)
    assert answers[1]["low"] - answers[2]["error_output"] > 0
    assert answers[1]["high"] + answers[2]["error_output"] < 4
    # Independent unit conversion back to the output recovers the ADC step.
    assert answers[4]["input_step"] * 1e-6 * 80 == pytest.approx(answers[4]["lsb"] * 1e-3)
    # The worked example starts from an open-circuit source, unlike the rehearsal terminal input.
    terminal = .004 / (1 + 2000 / 200000)
    assert 1.65 - 100 * terminal - .030 == pytest.approx(1.2239604, abs=1e-7)
    assert 1.65 + 100 * terminal + .030 == pytest.approx(2.0760396, abs=1e-7)


def test_signals_alias_and_applied_command_have_independent_checks():
    p = parameters("signals-control", "sampled-loop")
    values = signals_answers()
    for sample in range(20):
        t = sample * p["sample_period"]
        assert math.cos(math.tau * p["disturbance_frequency"] * t) == pytest.approx(
            math.cos(math.tau * values[1]["alias"] * t), abs=1e-12)
    assert values[4]["candidate"] > values[4]["applied"]
    equilibrium = p["plant_gain"] * values[4]["applied"]
    assert p["old_state"] < values[5]["next_state"] < equilibrium


def test_chemistry_reverse_extent_and_heat_boundary_are_explicit():
    # With initial B present, a small negative extent is inventory-feasible.
    extent = -.1
    assert 1 - extent > 0 and .5 + 2 * extent > 0
    assert 2 * (1 - extent) + .5 + 2 * extent == pytest.approx(2.5)
    draft = (COURSES / "general-chemistry-1/assessment-specs/abstract-gas-equilibrium-project-draft.md").read_text(encoding="utf-8")
    assert "−0.250≤ξ≤1.00" in draft
    assert "fixed temperature alone does not establish" in draft
    values = chemistry_answers()
    assert values[3]["amount_a"] >= 0 and values[3]["amount_b"] >= 0
    assert values[4]["equilibrium_q"] == pytest.approx(1)


def test_geroscience_intervals_and_hazard_scale_preserve_the_evidence_boundary():
    with (COURSES / "geroscience/assignments/surrogate-evidence-rehearsal.csv").open(encoding="utf-8", newline="") as stream:
        rows = {row["study_id"]: row for row in csv.DictReader(stream)}
    def excludes(row, endpoint, null):
        return not (
            float(row[endpoint + "_ci_low"]) <= null <= float(row[endpoint + "_ci_high"]))
    assert rows["X"]["design"].startswith("observational")
    assert excludes(rows["X"], "marker", 0) and excludes(rows["X"], "function", 0)
    assert excludes(rows["Y"], "marker", 0)
    assert not excludes(rows["Y"], "function", 0) and not excludes(rows["Y"], "survival", 1)
    assert not excludes(rows["Z"], "marker", 0)
    assert excludes(rows["Z"], "function", 0) and excludes(rows["Z"], "survival", 1)
    draft = (COURSES / "geroscience/assessment-specs/surrogate-endpoint-evidence-dossier-draft.md").read_text(encoding="utf-8")
    assert "hazard ratio below one" in draft
    assert "negative hazard-ratio contrast" not in draft
