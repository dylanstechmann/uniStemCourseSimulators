"""Keep the cumulative Biochemistry final packet inactive and answer-free."""

from __future__ import annotations

import csv
import importlib.util
import json
import math
from pathlib import Path

from courselab.units import parse_unit

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
CANDIDATE_PATH = COURSE / "assessment-specs/final-candidate.json"
SPEC = importlib.util.spec_from_file_location(
    "assessment_candidates", ROOT / "tools/assessment_candidates.py"
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)
# Open homework, review and project lessons added in 0.5.0 revisit existing objectives; the inactive
# candidate stays mapped to the topic lessons it was drafted against.
OPEN_PRACTICE_LESSON_PREFIXES = ("biochemistry-hw", "biochemistry-review-", "biochemistry-project-")


def test_cumulative_final_candidate_is_inactive_answer_free_and_mapped():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    known_objectives = {item["id"] for item in manifest["lesson_objectives"]}

    assert candidate["candidate_id"] == "biochemistry-final-candidate-v1"
    history_versions = {entry["version"] for entry in manifest["history"]}
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert candidate["content_version"] == "0.4.85"
    assert candidate["content_version"] in history_versions
    assert candidate["state"] == "inactive-review-candidate"
    assert candidate["review"]["status"] == "unreviewed"
    assert candidate["key_status"].startswith("An unreviewed private key/grader draft")
    assert candidate["candidate_id"] not in {a["id"] for a in manifest["assessments"]}
    assert len(candidate["questions"]) == 52
    assert candidate["points"] == 520
    assert sum(item["points"] for item in candidate["questions"]) == 520
    assert set(candidate["objective_ids"]) <= known_objectives
    assert set(candidate["objective_ids"]) == {
        objective
        for item in candidate["questions"]
        for objective in item["learning_objective_ids"]
    }
    assert candidate["objective_link_occurrences"] == sum(
        len(entry["objective_ids"]) for entry in candidate["objective_evidence"]
    )
    manifest_lesson_ids = {
        lesson["id"]
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if not lesson["id"].startswith(OPEN_PRACTICE_LESSON_PREFIXES)
    }
    assert len(candidate["lesson_ids"]) == 27
    assert set(candidate["lesson_ids"]) == manifest_lesson_ids
    assert candidate["prerequisite_sha256"]
    palmitate = next(item for item in candidate["questions"] if item["id"].endswith(":case-08"))
    assert "biochemistry-fatty-acid-objective-2" in palmitate["learning_objective_ids"]
    evidence = next(
        item for item in candidate["objective_evidence"]
        if item["question_id"] == palmitate["id"] and item["field_id"] == "palmitate-net-atp"
    )
    assert "biochemistry-fatty-acid-objective-2" in evidence["objective_ids"]

    # Public prompts and choices contain no protected grader structures or values.
    assert AUDIT.FORBIDDEN.isdisjoint(AUDIT.keys(candidate["questions"]))
    for item in candidate["questions"]:
        assert item["type"] == "structured"
        assert item["points"] == 10
        if item["id"].endswith(":case-42"):
            assert len(item["response_fields"]) == 5
            assert [field["points"] for field in item["response_fields"]] == [2, 2, 2, 2, 2]
        else:
            assert len(item["response_fields"]) == 2
            assert [field["points"] for field in item["response_fields"]] == [5, 5]
        assert sum(field["points"] for field in item["response_fields"]) == item["points"]
        assert AUDIT.FORBIDDEN.isdisjoint(AUDIT.keys(item["response_fields"]))
        for field in item["response_fields"]:
            if field["type"] == "numeric":
                parse_unit(field.get("unit") or "")
                assert isinstance(field["significant_figures"], int)
                assert 1 <= field["significant_figures"] <= 12


def test_cumulative_final_candidate_observations_are_synthetic_and_well_formed():
    with (COURSE / "assessment-specs/final-candidate-observations.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))

    assert rows
    assert {row["case_id"] for row in rows} == {"case-02", "case-03", "case-14", "case-15", "case-16", "case-17", "case-18", "case-19", "case-21", "case-22", "case-26", "case-28", "case-29", "case-30", "case-31", "case-32", "case-33", "case-34", "case-35", "case-36", "case-37", "case-38", "case-39", "case-40", "case-41", "case-42", "case-43", "case-44", "case-45", "case-50", "case-51", "case-52"}
    assert all(row["notes"] is not None for row in rows)
    kinetics = [row for row in rows if row["case_id"] == "case-02"]
    assert {row["condition"] for row in kinetics} == {"control", "inhibitor"}
    assert all(
        sum(row["measurement"] == name for row in kinetics if row["condition"] == group)
        == 3
        for group in ("control", "inhibitor")
        for name in ("substrate concentration", "initial rate")
    )
    purification = [row for row in rows if row["case_id"] == "case-03"]
    assert {row["condition"] for row in purification} == {"crude", "final fraction"}
    assert {row["measurement"] for row in purification} == {
        "total protein",
        "total activity",
    }
    cholesterol = {
        row["measurement"]: float(row["value"])
        for row in rows
        if row["case_id"] == "case-14"
    }
    pool_change = (
        cholesterol["cholesterol synthesis"]
        + cholesterol["LDL receptor uptake"]
        - cholesterol["bile-acid conversion"]
        - cholesterol["VLDL export"]
    )
    assert pool_change == 22


def test_final_case_17_maps_glycolytic_products_and_uncoupling_separately():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-17"))
    assert case["learning_objective_ids"] == [
        "biochemistry-3-objective-1", "biochemistry-3-objective-2"
    ]
    assert [field["id"] for field in case["response_fields"]] == [
        "glycolysis-products", "uncoupling-readout"
    ]
    assert all(field["type"] == "single_choice" for field in case["response_fields"])
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "glycolysis-products": ["biochemistry-3-objective-1"],
        "uncoupling-readout": ["biochemistry-3-objective-2"],
    }
    with (COURSE / "assessment-specs/final-candidate-observations.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        row = next(item for item in csv.DictReader(handle) if item["case_id"] == "case-17")
    assert row["measurement"] == "glucose input" and float(row["value"]) == 3


def test_final_case_18_bounds_conditional_ketone_yield_and_hepatic_evidence():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-18"))
    assert case["learning_objective_ids"] == [
        "biochemistry-ketone-objective-3", "biochemistry-ketone-objective-4"
    ]
    assert [field["id"] for field in case["response_fields"]] == [
        "acetoacetate-yield", "hepatic-fate-evidence"
    ]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-18"]
    values = {row["measurement"]: float(row["value"]) for row in rows}
    acetyl_coa = values["acetoacetate input"] * values["acetyl-CoA per ketone"]
    nadh = acetyl_coa * values["TCA NADH per acetyl-CoA"]
    fadh2 = acetyl_coa * values["TCA FADH2 per acetyl-CoA"]
    net_gtp = acetyl_coa * values["TCA GTP per acetyl-CoA"] - values["SCOT-bypassed GTP"] * values["acetoacetate input"]
    conditional_yield = nadh * values["P/O NADH"] + fadh2 * values["P/O FADH2"] + net_gtp
    assert abs(conditional_yield - 30.4) < 1e-9
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "acetoacetate-yield": ["biochemistry-ketone-objective-3"],
        "hepatic-fate-evidence": ["biochemistry-ketone-objective-4"],
    }


def test_final_case_19_calculates_citrate_label_change_without_claiming_flux():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-19"))
    assert case["learning_objective_ids"] == ["biochemistry-tca-cycle-objective-3"]
    assert [field["id"] for field in case["response_fields"]] == [
        "labeled-fraction-change", "flux-inference-boundary"
    ]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-19"]
    fractions = {
        condition: {
            row["measurement"].replace("citrate ", "").replace(" fraction", ""): float(row["value"])
            for row in rows if row["condition"] == condition
        }
        for condition in ("early", "late")
    }
    assert all(abs(sum(values.values()) - 1) < 1e-12 for values in fractions.values())
    change = (
        fractions["late"]["M+2"] + fractions["late"]["M+3"]
        - fractions["early"]["M+2"] - fractions["early"]["M+3"]
    )
    assert abs(change - 0.40) < 1e-12
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "labeled-fraction-change": ["biochemistry-tca-cycle-objective-3"],
        "flux-inference-boundary": ["biochemistry-tca-cycle-objective-3"],
    }


def test_final_case_20_covers_gluconeogenic_cost_and_carbon_source_boundary():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-20"))
    assert case["learning_objective_ids"] == [
        "biochemistry-gluconeogenesis-objective-1",
        "biochemistry-gluconeogenesis-objective-2",
    ]
    assert [field["id"] for field in case["response_fields"]] == [
        "atp-gtp-cost", "gluconeogenic-carbon-boundary"
    ]
    numeric = case["response_fields"][0]
    assert numeric["unit"] == "mol/mol" and numeric["significant_figures"] == 3
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "atp-gtp-cost": ["biochemistry-gluconeogenesis-objective-1"],
        "gluconeogenic-carbon-boundary": [
            "biochemistry-gluconeogenesis-objective-1",
            "biochemistry-gluconeogenesis-objective-2",
        ],
    }


def test_final_case_21_separates_intermediate_pool_balance_from_tca_flux():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-21"))
    assert case["learning_objective_ids"] == ["biochemistry-tca-cycle-objective-2"]
    assert [field["id"] for field in case["response_fields"]] == [
        "net-intermediate-balance", "redox-demand-interpretation"
    ]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-21"]
    values = {row["condition"] + ":" + row["measurement"]: float(row["value"]) for row in rows}
    net_pool_rate = (
        values["perturbed:anaplerotic replenishment rate"]
        - values["perturbed:cataplerotic withdrawal rate"]
    )
    assert abs(net_pool_rate - 0.50) < 1e-12
    assert values["perturbed:NADH/NAD+ ratio"] > values["reference:NADH/NAD+ ratio"]
    assert values["perturbed:ATP/ADP ratio"] > values["reference:ATP/ADP ratio"]
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "net-intermediate-balance": ["biochemistry-tca-cycle-objective-2"],
        "redox-demand-interpretation": ["biochemistry-tca-cycle-objective-2"],
    }


def test_final_case_22_separates_pfk_regulation_pool_and_measured_flux():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-22"))
    assert case["learning_objective_ids"] == ["biochemistry-10-objective-3"]
    assert [field["id"] for field in case["response_fields"]] == [
        "glucose-uptake-change", "pfk-pool-flux-interpretation"
    ]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-22"]
    values = {
        (row["condition"], row["measurement"]): float(row["value"])
        for row in rows
    }
    uptake_change = (
        values[("energy stress", "glucose uptake rate")]
        - values[("control", "glucose uptake rate")]
    )
    lactate_change = (
        values[("energy stress", "lactate appearance rate")]
        - values[("control", "lactate appearance rate")]
    )
    assert abs(uptake_change - 0.60) < 1e-12
    assert abs(lactate_change - 1.20) < 1e-12
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "glucose-uptake-change": ["biochemistry-10-objective-3"],
        "pfk-pool-flux-interpretation": ["biochemistry-10-objective-3"],
    }


def test_final_case_23_distinguishes_primary_from_quaternary_structure():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-23"))
    assert case["learning_objective_ids"] == ["biochemistry-1-objective-1"]
    assert [field["id"] for field in case["response_fields"]] == [
        "mutation-structure-level", "tetramer-structure-level"
    ]
    assert all(field["type"] == "single_choice" for field in case["response_fields"])
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "mutation-structure-level": ["biochemistry-1-objective-1"],
        "tetramer-structure-level": ["biochemistry-1-objective-1"],
    }


def test_final_case_24_converts_redox_potential_to_free_energy():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-24"))
    assert case["learning_objective_ids"] == ["biochemistry-6-objective-3"]
    numeric = case["response_fields"][0]
    assert numeric["id"] == "redox-delta-g" and numeric["unit"] == "kJ/mol"
    delta_e = 0.815 - 0.220
    delta_g = -1 * 96.485 * delta_e
    assert abs(delta_g - (-57.408575)) < 1e-12
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "redox-delta-g": ["biochemistry-6-objective-3"],
        "electron-transport-coupling": ["biochemistry-6-objective-3"],
    }


def test_final_case_25_uses_exact_quadratic_when_ligand_is_depleted():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-25"))
    assert case["learning_objective_ids"] == ["biochemistry-7-objective-2"]
    assert [field["id"] for field in case["response_fields"]] == [
        "bound-complex-concentration", "depletion-approximation"
    ]
    receptor_total, ligand_total, kd = 20.0, 30.0, 5.0
    exact = (
        receptor_total + ligand_total + kd
        - ((receptor_total + ligand_total + kd) ** 2 - 4 * receptor_total * ligand_total) ** 0.5
    ) / 2
    hyperbolic = receptor_total * ligand_total / (kd + ligand_total)
    assert exact == 15.0
    assert abs(hyperbolic - (120 / 7)) < 1e-12
    assert hyperbolic > exact
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "bound-complex-concentration": ["biochemistry-7-objective-2"],
        "depletion-approximation": ["biochemistry-7-objective-2"],
    }


def test_final_case_26_calculates_atp_turnover_from_oxygen_and_po():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-26"))
    assert case["learning_objective_ids"] == ["biochemistry-11-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-26"]
    values = {
        (row["condition"], row["measurement"]): float(row["value"])
        for row in rows
    }
    coupled = values[("coupled", "oxygen uptake rate")] * values[("coupled", "P/O ratio")]
    uncoupled = values[("uncoupled", "oxygen uptake rate")] * values[("uncoupled", "P/O ratio")]
    assert coupled == 60.0
    assert uncoupled == 45.0
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "uncoupled-atp-rate": ["biochemistry-11-objective-3"],
        "oxygen-turnover-interpretation": ["biochemistry-11-objective-3"],
    }


def test_final_case_27_uses_flux_control_summation_and_local_response():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-27"))
    assert case["learning_objective_ids"] == ["biochemistry-12-objective-2"]
    coefficients = (0.30, 0.20, 0.35)
    c4 = 1 - sum(coefficients)
    flux_change = coefficients[1] * -0.20
    assert abs(c4 - 0.15) < 1e-12
    assert abs(flux_change - (-0.04)) < 1e-12
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "fourth-control-coefficient": ["biochemistry-12-objective-2"],
        "enzyme-perturbation-flux": ["biochemistry-12-objective-2"],
    }



def test_final_case_28_interprets_ldh_redox_and_tracer_source_fraction():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-28"))
    assert case["learning_objective_ids"] == ["biochemistry-13-objective-2"]
    assert [field["id"] for field in case["response_fields"]] == [
        "medium-glucose-lactate-fraction", "redox-and-source-interpretation"
    ]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-28"]
    values = {(row["condition"], row["measurement"]): float(row["value"]) for row in rows}
    baseline_ratio = values[("baseline", "lactate concentration")] / values[("baseline", "pyruvate concentration")]
    perturbed_ratio = values[("respiratory-chain inhibitor", "lactate concentration")] / values[("respiratory-chain inhibitor", "pyruvate concentration")]
    source_fraction = (
        values[("respiratory-chain inhibitor", "lactate M+3 fraction")]
        / values[("respiratory-chain inhibitor", "medium uniformly labeled glucose fraction")]
    )
    assert baseline_ratio == 10
    assert perturbed_ratio == 40
    assert source_fraction == 0.96
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "medium-glucose-lactate-fraction": ["biochemistry-13-objective-2"],
        "redox-and-source-interpretation": ["biochemistry-13-objective-2"],
    }



def test_final_case_29_calculates_blocked_glucose_need_and_oxygen_diagnosis():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-29"))
    assert case["learning_objective_ids"] == [
        "biochemistry-13-objective-1", "biochemistry-13-objective-3"
    ]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-29"]
    values = {(row["condition"], row["measurement"]): float(row["value"]) for row in rows}
    uptake = values[("shared", "ATP demand")] / values[("shared", "glycolytic ATP yield per glucose")]
    lactate = uptake * values[("shared", "lactate yield per glucose")]
    assert uptake == 3.2
    assert lactate == 6.4
    assert values[("respiratory-chain inhibition", "oxygen uptake rate")] < values[("baseline", "oxygen uptake rate")] * 0.1
    assert values[("primary glycolytic defect with alternate fuel", "oxygen uptake rate")] > values[("baseline", "oxygen uptake rate")] * 0.8
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "glucose-uptake-after-block": ["biochemistry-13-objective-1"],
        "oxygen-diagnostic-pattern": ["biochemistry-13-objective-1", "biochemistry-13-objective-3"],
    }



def test_final_case_30_calculates_enzyme_turnover_time_and_maps_regulatory_layers():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-30"))
    assert case["learning_objective_ids"] == ["biochemistry-12-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-30"]
    values = {row["measurement"]: float(row["value"]) for row in rows}
    half_life = values["enzyme half-life"]
    t90 = math.log(10) * half_life / math.log(2)
    assert abs(t90 - 59.7947057) < 1e-6
    assert values["fraction of transition completed"] == 0.9
    evidence = {
        item["field_id"]: item["objective_ids"]
        for item in candidate["objective_evidence"]
        if item["question_id"] == case["id"]
    }
    assert evidence == {
        "enzyme-abundance-adjustment-time": ["biochemistry-12-objective-3"],
        "regulatory-layer-time-scales": ["biochemistry-12-objective-3"],
    }



def test_final_case_31_calculates_cooperative_oxygen_unloading():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-31"))
    assert case["learning_objective_ids"] == ["biochemistry-7-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-31"]
    values = {(row["condition"], row["measurement"]): float(row["value"]) for row in rows}
    p_lung=values[("shared", "lung oxygen partial pressure")]
    p_tissue=values[("shared", "resting-tissue oxygen partial pressure")]
    def saturation(p, n, p50):
        return p**n / (p50**n + p**n)
    hb_unloading=saturation(p_lung,2.8,26.0)-saturation(p_tissue,2.8,26.0)
    mb_unloading=saturation(p_lung,1.0,2.8)-saturation(p_tissue,1.0,2.8)
    assert abs(hb_unloading-0.20788260481308107)<1e-12
    assert abs(mb_unloading-0.03818320666206032)<1e-12
    assert hb_unloading>mb_unloading
    evidence={item["field_id"]:item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"]==case["id"]}
    assert evidence=={
        "hemoglobin-unloading-fraction":["biochemistry-7-objective-3"],
        "cooperative-unloading-interpretation":["biochemistry-7-objective-3"],
    }



def test_final_case_32_distinguishes_same_pool_from_steady_state_flux():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-32"))
    assert case["learning_objective_ids"] == ["biochemistry-12-objective-1"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-32"]
    values = {(row["condition"],row["measurement"]):float(row["value"]) for row in rows}
    fluxes={}
    for condition in ("enzyme 1 doubled","enzyme 2 halved"):
        supply=values[(condition,"first-step supply rate k1S")]
        k2=values[(condition,"second-step rate constant k2")]
        pool=values[(condition,"intermediate A steady-state pool")]
        outflow=k2*pool
        assert abs(supply-outflow)<1e-12
        fluxes[condition]=supply
    assert values[("enzyme 1 doubled","intermediate A steady-state pool")] == values[("enzyme 2 halved","intermediate A steady-state pool")] == 8.0
    assert fluxes["enzyme 1 doubled"]-fluxes["enzyme 2 halved"] == 2.0
    evidence={item["field_id"]:item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"]==case["id"]}
    assert evidence=={
        "steady-state-flux-difference":["biochemistry-12-objective-1"],
        "same-pool-different-flux":["biochemistry-12-objective-1"],
    }



def test_final_case_33_sums_fractional_acid_base_charges():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-33"))
    assert case["learning_objective_ids"] == ["biochemistry-8-objective-1"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-33"]
    values = {row["measurement"]:float(row["value"]) for row in rows}
    ph=values["solution pH"]
    def base(pka):
        return 1/(1+10**(ph-pka))
    def acid(pka):
        return 1/(1+10**(pka-ph))
    charge=(values["Lys side-chain count"]*base(values["Lys side-chain pKa"])
        +base(values["His side-chain pKa"])+base(values["N-terminus pKa"])
        -values["Asp side-chain count"]*acid(values["Asp side-chain pKa"])
        -acid(values["C-terminus pKa"]))
    assert abs(charge-0.8362731506705152)<1e-12
    evidence={item["field_id"]:item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"]==case["id"]}
    assert evidence=={
        "fractional-net-charge":["biochemistry-8-objective-1"],
        "acid-base-protonation-bookkeeping":["biochemistry-8-objective-1"],
    }



def test_final_case_34_calculates_pi_and_brackets_neutral_form():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-34"))
    assert case["learning_objective_ids"] == ["biochemistry-8-objective-2"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-34"]
    values={(row["condition"],row["measurement"]):float(row["value"]) for row in rows}
    alanine_pi=(values[("alanine","alpha-carboxyl pKa")]+values[("alanine","alpha-amino pKa")])/2
    glutamate_pi=(values[("glutamate","alpha-carboxyl pKa")]+values[("glutamate","side-chain carboxyl pKa")])/2
    lysine_pi=(values[("lysine","alpha-amino pKa")]+values[("lysine","side-chain amino pKa")])/2
    assert alanine_pi==6.015
    assert glutamate_pi==3.225
    assert abs(lysine_pi-9.74)<1e-12
    evidence={item["field_id"]:item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"]==case["id"]}
    assert evidence=={
        "alanine-isoelectric-point":["biochemistry-8-objective-2"],
        "pka-bracketing-rule":["biochemistry-8-objective-2"],
    }



def test_final_case_35_connects_protein_charge_pH_migration_and_resin():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-35"))
    assert case["learning_objective_ids"] == ["biochemistry-8-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-35"]
    values={(row["condition"],row["measurement"]):float(row["value"]) for row in rows}
    charge_change=values[("pH 6.0","net protein charge")]-values[("pH 7.4","net protein charge")]
    assert abs(charge_change-2.2)<1e-12
    pI=values[("shared","protein pI")]
    assert values[("below pI","comparison pH")]<pI<values[("above pI","comparison pH")]
    evidence={item["field_id"]:item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"]==case["id"]}
    assert evidence=={
        "charge-change-on-acidification":["biochemistry-8-objective-3"],
        "charge-migration-resin-interpretation":["biochemistry-8-objective-3"],
    }



def test_final_case_36_uses_efficiency_only_in_low_substrate_regime():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-36"))
    assert case["learning_objective_ids"] == ["biochemistry-2-objective-2"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-36"]
    values={(row["condition"],row["measurement"]):float(row["value"]) for row in rows}
    efficiency_b=values[("enzyme B","kcat")]/(values[("enzyme B","Km")]*1e-6)
    efficiency_a=values[("enzyme A","kcat")]/(values[("enzyme A","Km")]*1e-6)
    assert efficiency_b==4e7 and efficiency_a==2e7
    low=values[("shared","low substrate concentration")]
    high=values[("shared","near-saturating substrate concentration")]
    rate_a_low=values[("enzyme A","kcat")]*low/(values[("enzyme A","Km")]+low)
    rate_b_low=values[("enzyme B","kcat")]*low/(values[("enzyme B","Km")]+low)
    rate_a_high=values[("enzyme A","kcat")]*high/(values[("enzyme A","Km")]+high)
    rate_b_high=values[("enzyme B","kcat")]*high/(values[("enzyme B","Km")]+high)
    assert rate_b_low>rate_a_low and rate_a_high>rate_b_high
    evidence={item["field_id"]:item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"]==case["id"]}
    assert evidence=={
        "enzyme-b-catalytic-efficiency":["biochemistry-2-objective-2"],
        "efficiency-regime-interpretation":["biochemistry-2-objective-2"],
    }



def test_final_case_37_separates_substrate_allosteric_covalent_and_expression_control():
    candidate=json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case=next(item for item in candidate["questions"] if item["id"].endswith(":case-37"))
    assert case["learning_objective_ids"]==["biochemistry-4-objective-1"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8",newline="") as handle:
        rows=[row for row in csv.DictReader(handle) if row["case_id"]=="case-37"]
    values={(r["condition"],r["measurement"]):float(r["value"]) for r in rows}
    percent=100*(values[("substrate-supply intervention","substrate delivery after")]-values[("substrate-supply intervention","substrate delivery before")])/values[("substrate-supply intervention","substrate delivery before")]
    assert percent==-50.0
    assert values[("AMP intervention","PFK activity per enzyme after")]>values[("AMP intervention","PFK activity per enzyme before")]
    assert values[("AMP intervention","phosphorylated PFK fraction")] == values[("AMP intervention","PFK abundance")] * 0.20
    assert values[("kinase intervention","phosphorylated PFK fraction after")]>values[("kinase intervention","phosphorylated PFK fraction before")]
    assert values[("kinase intervention","PFK abundance")] == 1.0
    assert values[("transcription induction","PFK abundance after 24 h")] == 2*values[("transcription induction","PFK abundance before")]
    assert values[("transcription induction","PFK activity per enzyme after 24 h")] == values[("transcription induction","PFK activity per enzyme before")]
    evidence={e["field_id"]:e["objective_ids"] for e in candidate["objective_evidence"] if e["question_id"]==case["id"]}
    assert evidence=={
        "substrate-supply-percent-change":["biochemistry-4-objective-1"],
        "regulatory-layer-classification":["biochemistry-4-objective-1"],
    }



def test_final_case_38_predicts_connected_flux_response_to_partial_block():
    candidate=json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case=next(item for item in candidate["questions"] if item["id"].endswith(":case-38"))
    assert case["learning_objective_ids"]==["biochemistry-4-objective-2"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8",newline="") as handle:
        rows=[r for r in csv.DictReader(handle) if r["case_id"]=="case-38"]
    values={(r["condition"],r["measurement"]):float(r["value"]) for r in rows}
    accumulation=values[("initial interval after block","A→B flux v1")]-values[("initial interval after block","B→C flux v2")]
    assert accumulation==3.0
    assert values[("before block","B→C flux v2")] == values[("before block","C→D flux v3")] == 8.0
    evidence={e["field_id"]:e["objective_ids"] for e in candidate["objective_evidence"] if e["question_id"]==case["id"]}
    assert evidence=={
        "initial-pool-accumulation-rate":["biochemistry-4-objective-2"],
        "connected-pathway-perturbation":["biochemistry-4-objective-2"],
    }



def test_final_case_39_converts_unfolding_free_energy_to_folded_fraction():
    candidate=json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case=next(item for item in candidate["questions"] if item["id"].endswith(":case-39"))
    assert case["learning_objective_ids"]==["biochemistry-9-objective-1"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8",newline="") as handle:
        rows=[r for r in csv.DictReader(handle) if r["case_id"]=="case-39"]
    values={r["measurement"]:float(r["value"]) for r in rows}
    ku=math.exp(-values["free energy of unfolding"]/values["RT at 25 °C"])
    folded=1/(1+ku)
    assert abs(ku-0.03967208)<1e-6
    assert abs(folded-0.96184174)<1e-6
    assert values["free energy of unfolding"]>0 and ku<1 and folded>0.5
    evidence={e["field_id"]:e["objective_ids"] for e in candidate["objective_evidence"] if e["question_id"]==case["id"]}
    assert evidence=={
        "folded-fraction-from-free-energy":["biochemistry-9-objective-1"],
        "two-state-equilibrium-interpretation":["biochemistry-9-objective-1"],
    }



def test_final_case_40_extrapolates_stability_and_denaturation_midpoint():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-40"))
    assert case["learning_objective_ids"] == ["biochemistry-9-objective-2"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-40"]
    values = {(row["condition"], row["measurement"]): float(row["value"]) for row in rows}
    d1, g1 = values[("lower urea point", "urea concentration [D]")], values[("lower urea point", "ΔG_unfold")]
    d2, g2 = values[("higher urea point", "urea concentration [D]")], values[("higher urea point", "ΔG_unfold")]
    m = (g1 - g2) / (d2 - d1)
    stability = g1 + m * d1
    midpoint = stability / m
    assert m == 10.0
    assert stability == 21.0
    assert midpoint == 2.1
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "denaturant-stability-in-water": ["biochemistry-9-objective-2"],
        "denaturant-midpoint": ["biochemistry-9-objective-2"],
    }



def test_final_case_41_connects_destabilizing_mutation_to_unfolded_population():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-41"))
    assert case["learning_objective_ids"] == ["biochemistry-9-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-41"]
    values = {(row["condition"], row["measurement"]): float(row["value"]) for row in rows}
    rt = values[("wild type", "RT at 25 °C")]
    wild_type = values[("wild type", "ΔG_unfold")]
    ddg = values[("destabilizing variant", "mutation-induced ΔΔG_unfold")]
    ku_wt = math.exp(-wild_type / rt)
    ku_mutant = math.exp(-(wild_type + ddg) / rt)
    fold_change = ku_mutant / ku_wt
    folded_mutant = 1 / (1 + ku_mutant)
    unfolded_fold_change = (ku_mutant / (1 + ku_mutant)) / (ku_wt / (1 + ku_wt))
    assert math.isclose(fold_change, 25.2, rel_tol=0.002)
    assert math.isclose(folded_mutant, 0.99896, rel_tol=0.001)
    assert math.isclose(unfolded_fold_change, 25.2, rel_tol=0.01)
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "mutation-ku-fold-change": ["biochemistry-9-objective-3"],
        "mutation-marginal-stability-interpretation": ["biochemistry-9-objective-3"],
    }



def test_final_case_42_summarizes_replicates_by_condition_and_substrate():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-42"))
    assert case["learning_objective_ids"] == ["biochemistry-lab-01-objective-1"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-42"]
    grouped = {}
    for row in rows:
        grouped.setdefault(row["condition"], []).append(float(row["value"]))
    expected = {
        "control at [S]=2.5 μM": 33.33,
        "control at [S]=20 μM": 80.00,
        "inhibitor at [S]=2.5 μM": 14.29,
        "inhibitor at [S]=20 μM": 57.14,
    }
    assert set(grouped) == set(expected)
    assert all(len(values) == 3 for values in grouped.values())
    assert {condition: round(sum(values) / len(values), 2) for condition, values in grouped.items()} == expected
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert set(evidence) == {field["id"] for field in case["response_fields"]}
    assert all(objective_ids == ["biochemistry-lab-01-objective-1"] for objective_ids in evidence.values())



def test_final_case_43_derives_inhibition_constant_from_reciprocal_fits():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-43"))
    assert case["learning_objective_ids"] == ["biochemistry-lab-01-objective-2"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-43"]
    values = {(row["condition"], row["measurement"]): float(row["value"]) for row in rows}
    control_intercept = values[("control fit", "double-reciprocal y-intercept")]
    control_slope = values[("control fit", "double-reciprocal slope")]
    inhibitor_intercept = values[("inhibitor fit", "double-reciprocal y-intercept")]
    inhibitor_slope = values[("inhibitor fit", "double-reciprocal slope")]
    vmax = 1 / control_intercept
    km = control_slope / control_intercept
    vmax_inhibitor = 1 / inhibitor_intercept
    km_app = inhibitor_slope / inhibitor_intercept
    alpha = km_app / km
    ki = values[("inhibitor condition", "inhibitor concentration")] / (alpha - 1)
    assert vmax == vmax_inhibitor == 100
    assert km == 5 and km_app == 15 and alpha == 3 and ki == 2
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "competitive-inhibitor-ki": ["biochemistry-lab-01-objective-2"],
        "lineweaver-burk-parameter-set": ["biochemistry-lab-01-objective-2"],
    }



def test_final_case_44_evaluates_inhibition_fits_and_initial_rate_window():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-44"))
    assert case["learning_objective_ids"] == ["biochemistry-lab-01-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-44"]
    values = {(row["condition"], row["measurement"]): float(row["value"]) for row in rows}
    assert values[("control fit", "double-reciprocal y-intercept")] == values[("inhibitor fit", "double-reciprocal y-intercept")]
    assert values[("inhibitor fit", "double-reciprocal slope")] > values[("control fit", "double-reciprocal slope")]
    assert values[("initial interval", "substrate fraction consumed")] < 0.10
    assert values[("initial interval", "product-inhibition signal")] == 0
    assert values[("late interval", "substrate fraction consumed")] > 0.10
    assert values[("late interval", "product-inhibition signal")] > 0
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "inhibition-pattern-and-fit-limit": ["biochemistry-lab-01-objective-3"],
        "trustworthy-initial-rate-window": ["biochemistry-lab-01-objective-3"],
    }



def test_final_case_45_connects_nonoxidative_carbon_to_ribose_and_nadp():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-45"))
    assert case["learning_objective_ids"] == ["biochemistry-ppp-objective-2"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-45"]
    values = {row["measurement"]: float(row["value"]) for row in rows}
    reaction_sets = min(values["fructose 6-phosphate available"] / 2, values["glyceraldehyde 3-phosphate available"])
    pentose = reaction_sets * 3
    assert reaction_sets == 3
    assert pentose == 9
    assert 6 * values["fructose 6-phosphate available"] + 3 * values["glyceraldehyde 3-phosphate available"] == 5 * pentose
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "ribose-from-glycolytic-intermediates": ["biochemistry-ppp-objective-2"],
        "nadp-availability-and-branch-choice": ["biochemistry-ppp-objective-2"],
    }



def test_final_case_46_maps_amino_acid_skeletons_to_carbon_fates():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-46"))
    assert case["learning_objective_ids"] == ["biochemistry-amino-carbon-objective-1"]
    fields = {field["id"]: field for field in case["response_fields"]}
    assert fields["amino-acid-carbon-entry-map"]["type"] == "single_choice"
    assert fields["amino-acid-carbon-fate-classification"]["type"] == "single_choice"
    assert "Alanine → pyruvate" in fields["amino-acid-carbon-entry-map"]["options"][0]
    assert "phenylalanine → fumarate plus acetoacetate" in fields["amino-acid-carbon-entry-map"]["options"][0]
    assert "leucine is exclusively ketogenic" in fields["amino-acid-carbon-fate-classification"]["options"][0]
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "amino-acid-carbon-entry-map": ["biochemistry-amino-carbon-objective-1"],
        "amino-acid-carbon-fate-classification": ["biochemistry-amino-carbon-objective-1"],
    }



def test_final_case_47_separates_nitrogen_transfer_from_net_carbon_fate():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-47"))
    assert case["learning_objective_ids"] == ["biochemistry-amino-carbon-objective-2"]
    fields = {field["id"]: field for field in case["response_fields"]}
    assert "amino group to α-ketoglutarate" in fields["alanine-nitrogen-carbon-ledgers"]["options"][0]
    assert "net increase in oxaloacetate" in fields["acetyl-coa-net-glucose-boundary"]["options"][0]
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "alanine-nitrogen-carbon-ledgers": ["biochemistry-amino-carbon-objective-2"],
        "acetyl-coa-net-glucose-boundary": ["biochemistry-amino-carbon-objective-2"],
    }



def test_final_case_48_connects_citrate_shuttle_to_acc_malonyl_control():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-48"))
    assert case["learning_objective_ids"] == ["biochemistry-fatty-synthesis-objective-2"]
    fields = {field["id"]: field for field in case["response_fields"]}
    assert "Citrate can leave the mitochondrion" in fields["citrate-shuttle-acetylcoa-supply"]["options"][0]
    assert "inhibits CPT1" in fields["acc-malonyl-cpt1-control"]["options"][0]
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "citrate-shuttle-acetylcoa-supply": ["biochemistry-fatty-synthesis-objective-2"],
        "acc-malonyl-cpt1-control": ["biochemistry-fatty-synthesis-objective-2"],
    }



def test_final_case_49_traces_neutral_lipid_synthesis_to_vldl_export():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-49"))
    assert case["learning_objective_ids"] == ["biochemistry-neutral-lipid-objective-1"]
    fields = {field["id"]: field for field in case["response_fields"]}
    route = fields["glycerolipid-acylation-sequence"]["options"][0]
    assert route.index("lysophosphatidic acid") < route.index("phosphatidic acid") < route.index("diacylglycerol") < route.index("triacylglycerol")
    assert "Hepatocytes" in fields["hepatic-tag-vldl-export"]["options"][0]
    assert "VLDL" in fields["hepatic-tag-vldl-export"]["options"][0]
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "glycerolipid-acylation-sequence": ["biochemistry-neutral-lipid-objective-1"],
        "hepatic-tag-vldl-export": ["biochemistry-neutral-lipid-objective-1"],
    }



def test_final_case_50_bounds_amino_acid_tracer_inference():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-50"))
    assert case["learning_objective_ids"] == ["biochemistry-amino-carbon-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-50"]
    values = {row["condition"]: float(row["value"]) for row in rows}
    assert values["differentiated adipocyte culture"] - values["preadipocyte culture"] == 18
    assert all(row["unit"] == "%" for row in rows)
    choice = case["response_fields"][1]["options"][0]
    assert "18 percentage points" in choice
    assert "whole-body value" in choice
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "bca-derived-acetylcoa-percentage-point-change": ["biochemistry-amino-carbon-objective-3"],
        "bca-tracer-scope-interpretation": ["biochemistry-amino-carbon-objective-3"],
    }



def test_final_case_51_sums_labeled_ribose_and_limits_flux_inference():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-51"))
    assert case["learning_objective_ids"] == ["biochemistry-ppp-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-51"]
    values = {row["measurement"]: float(row["value"]) for row in rows}
    labeled = values["M+1 fraction"] + values["M+2 fraction"]
    assert values["M+0 fraction"] + labeled == 100
    assert labeled == 60
    choice = case["response_fields"][1]["options"][0]
    assert "quantify a rate" in choice
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "labeled-ribose-fraction": ["biochemistry-ppp-objective-3"],
        "ribose-tracer-flux-limit": ["biochemistry-ppp-objective-3"],
    }



def test_final_case_52_balances_nitrogen_to_urea_and_energy():
    candidate = json.loads(CANDIDATE_PATH.read_text(encoding="utf-8"))
    case = next(item for item in candidate["questions"] if item["id"].endswith(":case-52"))
    objective = "biochemistry-urea-cycle-objective-3"
    assert case["learning_objective_ids"] == [objective]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-52"]
    assert len(rows) == 1
    nitrogen_mol = float(rows[0]["value"])
    urea_mol = nitrogen_mol / 2
    atp_mol = urea_mol * 3
    phosphate_equivalents_mol = urea_mol * 4
    assert (nitrogen_mol, urea_mol, atp_mol, phosphate_equivalents_mol) == (5, 2.5, 7.5, 10)
    choice = case["response_fields"][1]["options"][0]
    assert "2.50 mol urea" in choice
    assert "7.50 mol ATP molecules" in choice
    assert "10 mol high-energy phosphate equivalents" in choice
    evidence = {item["field_id"]: item["objective_ids"] for item in candidate["objective_evidence"] if item["question_id"] == case["id"]}
    assert evidence == {
        "stoichiometric-urea-amount": [objective],
        "urea-atp-energy-ledger": [objective],
    }
