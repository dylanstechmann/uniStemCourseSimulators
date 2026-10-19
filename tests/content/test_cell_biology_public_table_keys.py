import csv
import json
import math
import re
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cell-biology"
QUESTION_BANK = COURSE / "question-banks/practice.json"

SOURCES = {
    "cell-biology-11:image-quantification-summary": (
        "labs/image-counts.csv", "condition", "batch", None,
    ),
    "cell-biology-hw1:sorting-summary": (
        "assignments/homework-01-m6p-sorting.csv", "condition", "batch", None,
    ),
    "cell-biology-lab2:summary-table": (
        "labs/signaling-timecourse.csv", "condition", "biological_preparation", "time_min",
    ),
    "cell-biology-hw2:rate-summary": (
        "assignments/homework-02-inhibition-rates.csv", "condition", "assay_day", "substrate_uM",
    ),
    "cell-biology-hw3:lesion-summary": (
        "assignments/homework-03-lesion-removal.csv", "condition", "culture", None,
    ),
    "cell-biology-hw4:chip-reporter-summary": (
        "assignments/homework-04-chip-reporter.csv", "condition", "culture", None,
    ),
    "cell-biology-hw5:layer-summary": (
        "assignments/homework-05-rna-protein.csv", "condition", "culture", None,
    ),
    "cell-biology-hw6:clone-summary": (
        "assignments/homework-06-isogenic-clones.csv", "condition", "clone", None,
    ),
    "cell-biology-hw7:coverslip-summary": (
        "assignments/homework-07-matrix-spreading.csv", "condition", "coverslip", None,
    ),
    "cell-biology-hw8:state-summary": (
        "assignments/homework-08-cell-state.csv", "condition", "culture", None,
    ),
    "cell-biology-lab3:summary-table": (
        "labs/lineage-timecourse.csv", "condition", "culture", "day",
    ),
    "cell-biology-final:clone-summary-table": (
        "assignments/final-review-feedback-variant-clones.csv", "genotype", "clone", None,
    ),
    "cell-biology-project:rehearsal-summary": (
        "assignments/project-rehearsal-cultures.csv", "condition", "culture", None,
    ),
}

OUTPUT_TO_SOURCE_COLUMN = {
    "mean_marker_positive_percent": None,
    "mean_lysosomal_delivery_pct": "lysosomal_delivery_pct",
    "mean_conditioned_medium_pct": "conditioned_medium_pct",
    "mean_perk_relative": "perk_totalerk_relative",
    "mean_rate_nm_per_s": "initial_rate_nm_per_s",
    "mean_lesion_remaining_pct": "lesion_remaining_pct_4h",
    "mean_s_phase_pct": "s_phase_pct",
    "mean_specific_pct_input": "chip_specific_pct_input",
    "mean_igg_pct_input": "chip_igg_pct_input",
    "mean_reporter_wt": "reporter_wt_rel",
    "mean_reporter_mut": "reporter_mut_rel",
    "mean_mrna": "mrna_rel",
    "mean_protein": "protein_rel",
    "mean_labeling": "nascent_labeling_rel",
    "mean_remaining_4h": "protein_remaining_4h_pct",
    "mean_assay_score": "assay_score",
    "mean_spread_area_um2": "spread_area_um2",
    "mean_cell_density": "cell_density_per_mm2",
    "mean_ligand_density": "ligand_density_rel",
    "mean_edu_pct": "edu_pct",
    "mean_sabgal_pct": "sabgal_pct",
    "mean_reentry_edu_pct": "reentry_edu_pct",
    "mean_lineage_pct": "lineage_marker_pct",
    "mean_pluripotency_pct": "pluripotency_marker_pct",
    "mean_cells_thousands": "cells_per_well_thousands",
    "mean_f_half_life_h": "f_half_life_h",
    "mean_perk_60_fold": "perk_60_fold",
}


def _rehearsal_value(row, column):
    """Recompute the project-guide transformations from the CSV strings with exact arithmetic."""
    value = {name: Fraction(text) for name, text in row.items() if name not in {"form", "condition", "culture"}}
    per_thousand = value["viable_cells"] / 1000
    if column == "mean_rna_per_1000_viable":
        corrected = (value["rna_signal_eq"] - value["rna_background_eq"]) * value["spike_input_eq"] / value["spike_recovered_eq"]
        return float(corrected / per_thousand)
    if column == "mean_protein_ug_per_1000_viable":
        corrected = (value["protein_signal_ug"] - value["protein_background_ug"]) / value["protein_recovery_fraction"]
        return float(corrected / per_thousand)
    if column == "mean_marker_pct":
        return float(100 * value["marker_positive_viable"] / value["viable_cells"])
    if column == "mean_function_pct":
        return float(100 * value["functional_events_viable"] / value["viable_cells"])
    raise AssertionError(f"No rehearsal transformation for {column}")


def _load_csv(path):
    with path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def _prompt_values(prompt, row_id):
    match = re.search(rf"\b{re.escape(row_id)}\s*=\s*([0-9., ]+?)(?:;|\.(?=\s|$))", prompt)
    assert match, f"Could not find the {row_id} replicate values in the prompt"
    return [float(value.strip()) for value in match.group(1).split(",")]


def _source_rows(question_id, row_id, rows, row_field, replicate_field, time_field):
    if question_id == "cell-biology-4:csv-summary-table":
        return None
    if time_field == "time_min":
        condition, time = row_id.rsplit("_", 1)
    else:
        condition = row_id
        time = {"day": "8", "substrate_uM": "40"}.get(time_field)
    selected = [row for row in rows if row[row_field] == condition]
    if time_field:
        selected = [row for row in selected if row[time_field] == time]
    assert selected, f"No source rows for {question_id}/{row_id}"
    replicate_ids = [row[replicate_field] for row in selected]
    assert len(replicate_ids) == len(set(replicate_ids)), f"Repeated replicate in {question_id}/{row_id}"
    return selected


def test_public_table_checks_reconcile_to_source_csvs_and_replicate_values():
    questions = json.loads(QUESTION_BANK.read_text(encoding="utf-8"))["questions"]
    table_questions = [
        question for question in questions
        if question.get("solution_spec", {}).get("validation_spec", {}).get("checks")
    ]
    assert len(table_questions) == 14

    verified_checks = 0
    for question in table_questions:
        question_id = question["id"]
        if question_id == "cell-biology-4:csv-summary-table":
            rows = None
            row_field = replicate_field = time_field = None
        else:
            source_path, row_field, replicate_field, time_field = SOURCES[question_id]
            rows = _load_csv(COURSE / source_path)

        checks = question["solution_spec"]["validation_spec"]["checks"]
        selected_by_row = {
            row_id: _source_rows(
                question_id, row_id, rows, row_field, replicate_field, time_field,
            ) if rows is not None else None
            for row_id in {check["row_id"] for check in checks}
        }
        source_values_by_check = {}
        source_values_by_row = {}
        for check in checks:
            calculation = check["calculation"]
            row_id = check["row_id"]
            if calculation["operation"] != "mean":
                continue
            selected = selected_by_row[row_id]
            if question_id == "cell-biology-4:csv-summary-table":
                source_values = _prompt_values(question["prompt"], row_id)
            elif check["column"] == "mean_marker_positive_percent":
                source_values = [
                    100 * float(row["marker_positive_nuclei"]) / float(row["viable_nuclei"])
                    for row in selected
                ]
            elif question_id == "cell-biology-project:rehearsal-summary":
                source_values = [_rehearsal_value(row, check["column"]) for row in selected]
            else:
                source_column = OUTPUT_TO_SOURCE_COLUMN[check["column"]]
                assert source_column is not None
                source_values = [float(row[source_column]) for row in selected]

            expected_values = calculation["values"]
            assert len(expected_values) == len(source_values)
            assert all(math.isclose(float(actual), expected, rel_tol=0, abs_tol=1e-12)
                       for actual, expected in zip(expected_values, source_values))
            source_values_by_check[check["id"]] = source_values
            source_values_by_row.setdefault(row_id, []).append(source_values)

        for check in checks:
            calculation = check["calculation"]
            row_id = check["row_id"]
            values = calculation["values"]
            if calculation["operation"] == "count":
                assert any(values == source_values for source_values in source_values_by_row[row_id])
                computed = len(values) if selected_by_row[row_id] is None else len(selected_by_row[row_id])
            else:
                source_values = source_values_by_check[check["id"]]
                computed = math.fsum(source_values) / len(source_values)

            tolerance = float(check.get("tolerance", 0))
            relative_tolerance = float(check.get("relative_tolerance", 0))
            allowed_error = tolerance + relative_tolerance * abs(float(check["answer"]))
            assert abs(computed - float(check["answer"])) <= allowed_error, (
                question_id, check["id"], computed, check["answer"], allowed_error,
            )
            verified_checks += 1

    assert verified_checks == 133


def test_lineage_lab_distinguishes_culture_records_from_measured_values():
    rows = _load_csv(COURSE / "labs/lineage-timecourse.csv")
    outcomes = (
        "lineage_marker_pct",
        "pluripotency_marker_pct",
        "cells_per_well_thousands",
        "viability_pct",
    )
    assert len(rows) == 40
    assert len(rows) * len(outcomes) == 160
    assert {row["condition"] for row in rows} == {"control", "factor"}
    assert {row["day"] for row in rows} == {"0", "2", "4", "6", "8"}
    for condition in {"control", "factor"}:
        for day in {"0", "2", "4", "6", "8"}:
            replicate_ids = [
                row["culture"]
                for row in rows
                if row["condition"] == condition and row["day"] == day
            ]
            assert len(replicate_ids) == len(set(replicate_ids)) == 4

    lab = (COURSE / "labs/03-lineage-time-course-and-state-inference.md").read_text(
        encoding="utf-8"
    )
    assert "40 culture-level records" in lab
    assert "160 constructed outcome measurements" in lab


def test_virtual_lab_csv_rows_match_documented_replicate_designs():
    image_rows = _load_csv(COURSE / "labs/image-counts.csv")
    image_lab = (COURSE / "labs/01-fluorescence-image-quantification.md").read_text(
        encoding="utf-8"
    )
    assert len(image_rows) == 8
    assert "same eight observations" in image_lab
    for condition in {row["condition"] for row in image_rows}:
        batches = [row["batch"] for row in image_rows if row["condition"] == condition]
        assert len(batches) == len(set(batches)) == 4

    signaling_rows = _load_csv(COURSE / "labs/signaling-timecourse.csv")
    signaling_lab = (
        COURSE / "labs/02-signaling-dynamics-inhibitor-rescue.md"
    ).read_text(encoding="utf-8")
    assert len(signaling_rows) == 120
    assert "all 120 observations" in signaling_lab
    assert len({row["condition"] for row in signaling_rows}) == 6
    assert len({row["time_min"] for row in signaling_rows}) == 5
    for condition in {row["condition"] for row in signaling_rows}:
        for time in {row["time_min"] for row in signaling_rows}:
            preparations = [
                row["biological_preparation"]
                for row in signaling_rows
                if row["condition"] == condition and row["time_min"] == time
            ]
            assert len(preparations) == len(set(preparations)) == 4
