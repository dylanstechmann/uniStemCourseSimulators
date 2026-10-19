"""Recompute and report public Cell Biology formative table checks.

This audit is limited to the learner-visible formative question bank and its
public CSV or prompt inputs. It never reads protected assessment sources and
does not establish independent review, course quality, or release readiness.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import course_package_digest  # noqa: E402

COURSE = ROOT / "content/courses/cell-biology"
QUESTION_BANK = COURSE / "question-banks/practice.json"
QUESTION_SOURCES = {
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
def _fraction(row: dict[str, str], column: str) -> Fraction:
    return Fraction(row[column])


def _per_1000_viable(row: dict[str, str], amount: Fraction) -> Fraction:
    return amount / (_fraction(row, "viable_cells") / 1000)


# Project-rehearsal outputs are per-culture transformations defined in the integrative project guide.
DERIVED_OUTPUTS = {
    "mean_rna_per_1000_viable": lambda row: _per_1000_viable(
        row,
        (_fraction(row, "rna_signal_eq") - _fraction(row, "rna_background_eq"))
        * _fraction(row, "spike_input_eq") / _fraction(row, "spike_recovered_eq"),
    ),
    "mean_protein_ug_per_1000_viable": lambda row: _per_1000_viable(
        row,
        (_fraction(row, "protein_signal_ug") - _fraction(row, "protein_background_ug"))
        / _fraction(row, "protein_recovery_fraction"),
    ),
    "mean_marker_pct": lambda row: 100 * _fraction(row, "marker_positive_viable") / _fraction(row, "viable_cells"),
    "mean_function_pct": lambda row: 100 * _fraction(row, "functional_events_viable") / _fraction(row, "viable_cells"),
}
PROMPT_VALUES = re.compile(
    r"\b(?P<row>[A-Za-z0-9_-]+)\s*=\s*(?P<values>[0-9., ]+?)(?:;|\.(?=\s|$))"
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def _prompt_rows(prompt: str) -> dict[str, list[float]]:
    return {
        match.group("row"): [float(value.strip()) for value in match.group("values").split(",")]
        for match in PROMPT_VALUES.finditer(prompt)
    }


def _source_rows(
    question_id: str,
    row_id: str,
    rows: list[dict[str, str]],
    row_field: str,
    replicate_field: str,
    time_field: str | None,
) -> list[dict[str, str]]:
    if time_field == "time_min":
        condition, time = row_id.rsplit("_", 1)
    else:
        condition = row_id
        time = {"day": "8", "substrate_uM": "40"}.get(time_field)
    selected = [row for row in rows if row[row_field] == condition]
    if time_field:
        selected = [row for row in selected if row[time_field] == time]
    if not selected:
        raise ValueError(f"No source rows for {question_id}/{row_id}")
    replicate_ids = [row[replicate_field] for row in selected]
    if len(replicate_ids) != len(set(replicate_ids)):
        raise ValueError(f"Repeated replicate in {question_id}/{row_id}")
    return selected


def _close(actual: float, expected: float, *, atol: float = 1e-12) -> bool:
    return math.isclose(actual, expected, rel_tol=0, abs_tol=atol)


def build_evidence(root: Path = ROOT) -> dict[str, Any]:
    """Return a deterministic, hash-bound audit of every public table check."""
    course_dir = root / "content/courses/cell-biology"
    bank_path = course_dir / "question-banks/practice.json"
    bank = json.loads(bank_path.read_text(encoding="utf-8"))
    questions = bank["questions"]
    table_questions = [
        question for question in questions
        if question.get("solution_spec", {}).get("validation_spec", {}).get("checks")
    ]
    question_by_id = {question["id"]: question for question in table_questions}
    expected_ids = set(QUESTION_SOURCES) | {"cell-biology-4:csv-summary-table"}
    if set(question_by_id) != expected_ids:
        raise ValueError("Public table question inventory differs from the audit allowlist")

    source_paths = {question_id: data[0] for question_id, data in QUESTION_SOURCES.items()}
    source_path_list = sorted({course_dir / value for value in source_paths.values()})
    source_records = [
        {"path": path.relative_to(root).as_posix(), "sha256": _sha256(path)}
        for path in source_path_list
    ]
    package = course_package_digest.compute_digest("cell-biology", root)
    results: list[dict[str, Any]] = []

    for question_id in sorted(question_by_id):
        question = question_by_id[question_id]
        if question_id == "cell-biology-4:csv-summary-table":
            rows = None
            row_field = replicate_field = time_field = None
            question_source = "embedded-prompt"
            prompt_rows = _prompt_rows(question["prompt"])
        else:
            source_path, row_field, replicate_field, time_field = QUESTION_SOURCES[question_id]
            rows = _load_csv(course_dir / source_path)
            question_source = (course_dir / source_path).relative_to(root).as_posix()
            prompt_rows = {}

        checks = question["solution_spec"]["validation_spec"]["checks"]
        selected_by_row = {
            row_id: _source_rows(
                question_id, row_id, rows, row_field, replicate_field, time_field,
            ) if rows is not None else None
            for row_id in {check["row_id"] for check in checks}
        }
        computed_values: dict[str, list[float]] = {}
        values_by_row: dict[str, list[list[float]]] = {}
        for check in checks:
            calculation = check["calculation"]
            if calculation["operation"] != "mean":
                continue
            row_id = check["row_id"]
            selected = selected_by_row[row_id]
            if selected is None:
                source_values = prompt_rows[row_id]
            elif check["column"] == "mean_marker_positive_percent":
                source_values = [
                    100 * float(row["marker_positive_nuclei"]) / float(row["viable_nuclei"])
                    for row in selected
                ]
            elif check["column"] in DERIVED_OUTPUTS:
                source_values = [float(DERIVED_OUTPUTS[check["column"]](row)) for row in selected]
            else:
                source_column = OUTPUT_TO_SOURCE_COLUMN.get(check["column"])
                if source_column is None:
                    raise ValueError(f"No public source column for {question_id}:{check['id']}")
                source_values = [float(row[source_column]) for row in selected]

            authored_values = calculation["values"]
            if len(authored_values) != len(source_values) or not all(
                _close(float(actual), expected)
                for actual, expected in zip(authored_values, source_values)
            ):
                raise ValueError(f"Authored replicate values differ from source for {question_id}:{check['id']}")
            computed_values[check["id"]] = source_values
            values_by_row.setdefault(row_id, []).append(source_values)

        for check in checks:
            calculation = check["calculation"]
            row_id = check["row_id"]
            if calculation["operation"] == "count":
                matches = [values for values in values_by_row[row_id] if values == calculation["values"]]
                if not matches:
                    raise ValueError(f"Count input has no matching public data for {question_id}:{check['id']}")
                source_values = matches[0]
                computed = len(source_values) if selected_by_row[row_id] is None else len(selected_by_row[row_id])
            elif calculation["operation"] == "mean":
                source_values = computed_values[check["id"]]
                computed = math.fsum(source_values) / len(source_values)
            else:
                raise ValueError(f"Unsupported public table operation: {calculation['operation']}")

            expected = float(check["answer"])
            absolute_tolerance = float(check.get("tolerance", 0))
            relative_tolerance = float(check.get("relative_tolerance", 0))
            allowed_error = absolute_tolerance + relative_tolerance * abs(expected)
            absolute_error = abs(computed - expected)
            if absolute_error > allowed_error:
                raise ValueError(
                    f"Recalculation failed for {question_id}:{check['id']}: "
                    f"computed {computed}, expected {expected}, allowed error {allowed_error}"
                )
            results.append({
                "question_id": question_id,
                "check_id": check["id"],
                "source": question_source,
                "row_id": row_id,
                "operation": calculation["operation"],
                "replicate_values": source_values,
                "replicate_count": len(source_values),
                "computed": computed,
                "authored_answer": expected,
                "absolute_error": absolute_error,
                "absolute_tolerance": absolute_tolerance,
                "relative_tolerance": relative_tolerance,
                "maximum_allowed_error": allowed_error,
                "passed": True,
            })

    if len(results) != 133:
        raise ValueError(f"Expected 133 public table checks, found {len(results)}")

    return {
        "schema_version": "1.0",
        "evidence_scope": "author-side-public-formative-source-reconciliation",
        "course_id": "cell-biology",
        "course_version": package["content_version"],
        "public_package_sha256": package["package_sha256"],
        "question_bank": {
            "path": bank_path.relative_to(root).as_posix(),
            "sha256": _sha256(bank_path),
        },
        "public_sources": source_records,
        "scope_limits": {
            "protected_assessment_sources_read": False,
            "independent_review_established": False,
            "qualified_reviewer_identity_verified": False,
            "release_authorized": False,
        },
        "question_count": len(table_questions),
        "check_count": len(results),
        "passed_check_count": len(results),
        "results": results,
    }


def _canonical_json(value: dict[str, Any]) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", metavar="PATH", help="write the evidence JSON to PATH")
    mode.add_argument("--check", metavar="PATH", help="fail if PATH differs from current evidence")
    args = parser.parse_args()
    path = Path(args.write or args.check)
    if not path.is_absolute():
        path = ROOT / path
    try:
        evidence = build_evidence()
        rendered = _canonical_json(evidence)
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(rendered, encoding="utf-8", newline="\n")
            action = "wrote"
        else:
            if not path.is_file() or path.read_text(encoding="utf-8") != rendered:
                raise ValueError(f"Evidence report is missing or stale: {path}")
            action = "checked"
    except (OSError, ValueError, KeyError, TypeError, ZeroDivisionError) as exc:
        parser.exit(1, f"Public table evidence {args.check or args.write} failed: {exc}\n")
    print(json.dumps({
        "action": action,
        "course_version": evidence["course_version"],
        "question_count": evidence["question_count"],
        "check_count": evidence["check_count"],
        "passed_check_count": evidence["passed_check_count"],
        "protected_assessment_sources_read": False,
        "release_authorized": False,
        "path": path.as_posix(),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
