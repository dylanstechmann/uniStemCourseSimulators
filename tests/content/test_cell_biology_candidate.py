"""Public inactive-candidate integrity; no protected answers belong in these tests."""

import csv
import hashlib
import json
import math
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cell-biology"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))


@pytest.fixture(
    params=sorted((COURSE / "assessment-specs").glob("*-candidate.json")),
    ids=lambda path: path.stem,
)
def candidate(request):
    return json.loads(request.param.read_text(encoding="utf-8"))


def nested_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from nested_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from nested_keys(item)


def test_candidate_is_version_bound_and_blocked_on_real_review(candidate):
    CANDIDATE = candidate
    assert CANDIDATE["content_version"] in {
        entry["version"] for entry in MANIFEST["history"]
    }
    assert tuple(map(int, CANDIDATE["content_version"].split("."))) <= tuple(
        map(int, MANIFEST["version"].split("."))
    )
    for name, digest in CANDIDATE.get("prerequisite_sha256", {}).items():
        assert hashlib.sha256((COURSE / name).read_bytes()).hexdigest() == digest
    assert CANDIDATE["state"] == "inactive-review-candidate"
    assert CANDIDATE["review"] == {"status": "unreviewed", "reviewers": []}
    assert {
        "independent-recalculation",
        "subject-matter-review",
        "assessment-review",
        "accessibility-review",
        "measured-workload",
        "operator-provisioning-and-release-policy",
    }.issubset(CANDIDATE["activation_gates"])
    assert re.fullmatch(r"[a-f0-9]{64}", CANDIDATE["private_source_sha256"])
    assert CANDIDATE["private_source_ref"].startswith("private://assignments/")


def test_public_candidate_has_only_answer_free_item_fields(candidate):
    CANDIDATE = candidate
    assert not {
        "solution_spec",
        "answer",
        "feedback",
        "field_specs",
        "rubric",
        "checks",
    }.intersection(nested_keys(CANDIDATE["questions"]))
    allowed = {
        "id",
        "type",
        "prompt",
        "options",
        "unit",
        "significant_figures",
        "points",
        "selection",
        "partial_credit_policy",
        "response_fields",
        "graph_spec",
        "accepted_media_types",
        "max_upload_bytes",
        "variant_id",
        "variant_token",
        "learning_objective_ids",
        "assessment_role",
    }
    questions = CANDIDATE["questions"]
    assert len({q["id"] for q in questions}) == len(questions)
    assert sum(q["points"] for q in questions) == CANDIDATE["points"]
    assert all(set(q) <= allowed for q in questions)


def test_candidate_maps_to_existing_instruction_and_actual_outcome_links(candidate):
    CANDIDATE = candidate
    lessons = {
        lesson["id"] for module in MANIFEST["modules"] for lesson in module["lessons"]
    }
    objectives = {o["id"]: o for o in MANIFEST["lesson_objectives"]}
    assert set(CANDIDATE["lesson_ids"]) <= lessons
    assert set(CANDIDATE["objective_ids"]) <= set(objectives)
    expected = {
        outcome
        for key in CANDIDATE["objective_ids"]
        for outcome in objectives[key].get("course_outcome_ids", [])
    }
    assert set(CANDIDATE["course_outcome_ids"]) == expected
    assert all(
        set(q["learning_objective_ids"]) <= set(CANDIDATE["objective_ids"])
        for q in CANDIDATE["questions"]
    )


def test_public_data_keep_observation_units_and_series_consistent(candidate):
    CANDIDATE = candidate
    with (COURSE / CANDIDATE["dataset_path"]).open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    if "case_id" in rows[0]:
        assert {r["form"] for r in rows} == {"A", "B"}
        assert all(math.isfinite(float(r["value"])) for r in rows)
        assert len({(r["case_id"], r["form"], r["metric"]) for r in rows}) == len(rows)
        metrics_by_case_form = {}
        units_by_case_metric = {}
        for row in rows:
            assert row["case_id"] and row["metric"] and row["unit"]
            metrics_by_case_form.setdefault((row["case_id"], row["form"]), set()).add(
                row["metric"]
            )
            units_by_case_metric.setdefault(
                (row["case_id"], row["metric"]), set()
            ).add(row["unit"])
        cases = {row["case_id"] for row in rows}
        assert set(metrics_by_case_form) == {
            (case_id, form) for case_id in cases for form in ("A", "B")
        }
        for case_id in cases:
            assert metrics_by_case_form[(case_id, "A")] == metrics_by_case_form[
                (case_id, "B")
            ]
        assert all(len(units) == 1 for units in units_by_case_metric.values())
        if CANDIDATE["candidate_id"] == "cell-biology-lab-01-review-v1":
            expected_metrics = {
                f"culture_{culture}_{channel}"
                for culture in range(1, 5)
                for channel in ("input", "fraction")
            }
            values = {
                (row["form"], row["metric"]): float(row["value"]) for row in rows
            }
            assert all(
                metrics_by_case_form[(case_id, form)] == expected_metrics
                for case_id in cases
                for form in ("A", "B")
            )
            for culture in range(1, 5):
                input_metric = f"culture_{culture}_input"
                fraction_metric = f"culture_{culture}_fraction"
                assert values[("A", input_metric)] == values[("B", input_metric)]
                for form in ("A", "B"):
                    assert values[(form, input_metric)] > 0
                    assert 0 <= values[(form, fraction_metric)] <= values[
                        (form, input_metric)
                    ]
        if CANDIDATE["candidate_id"] == "cell-biology-lab-02-review-v1":
            expected_metrics = {
                f"culture_{culture}_t{time_min}"
                for culture in range(1, 5)
                for time_min in (10, 30)
            }
            values = {
                (row["form"], row["metric"]): float(row["value"]) for row in rows
            }
            assert cases == {"lab-02-02"}
            assert all(
                metrics_by_case_form[(case_id, form)] == expected_metrics
                for case_id in cases
                for form in ("A", "B")
            )
            for form in ("A", "B"):
                for culture in range(1, 5):
                    at_10 = values[(form, f"culture_{culture}_t10")]
                    at_30 = values[(form, f"culture_{culture}_t30")]
                    assert at_10 > at_30 > 0
        if CANDIDATE["candidate_id"] == "cell-biology-lab-03-review-v1":
            expected_metrics = {
                f"culture_{culture}_{channel}"
                for culture in range(1, 5)
                for channel in ("viable", "positive")
            }
            values = {
                (row["form"], row["metric"]): float(row["value"]) for row in rows
            }
            assert cases == {"lab-03-03"}
            assert all(
                metrics_by_case_form[(case_id, form)] == expected_metrics
                for case_id in cases
                for form in ("A", "B")
            )
            for culture in range(1, 5):
                viable_metric = f"culture_{culture}_viable"
                positive_metric = f"culture_{culture}_positive"
                assert values[("A", viable_metric)] == values[("B", viable_metric)]
                for form in ("A", "B"):
                    viable = values[(form, viable_metric)]
                    positive = values[(form, positive_metric)]
                    assert viable > 0
                    assert 0 <= positive <= viable
        if CANDIDATE["candidate_id"] == "cell-biology-final-review-v1":
            measured_cases = {
                *(f"final-{case:02d}" for case in range(2, 13)),
                *(f"final-{case:02d}" for case in range(14, 29)),
            }
            assert len(rows) == 138
            assert cases == measured_cases
        if CANDIDATE["candidate_id"] == "cell-biology-integrative-project-review-v1":
            assert len(rows) == 26
            assert cases == {
                "integrative-project-17",
                "integrative-project-22",
                "integrative-project-28",
            }
        if CANDIDATE["candidate_id"] == "cell-biology-integrative-project-review-v1":
            with (COURSE / CANDIDATE["additional_dataset_paths"][0]).open(
                newline=""
            ) as stream:
                cultures = list(csv.DictReader(stream))
            conditions = {
                "control",
                "signal_low",
                "signal_high",
                "matrix_high",
                "both",
                "rescue",
            }
            forms = {"A", "B"}
            groups = {}
            cultures_by_form_condition = {}
            numeric_fields = (
                "time_h",
                "seeded_cells",
                "viable_cells",
                "rna_signal_eq",
                "rna_background_eq",
                "spike_input_eq",
                "spike_recovered_eq",
                "protein_signal_ug",
                "protein_background_ug",
                "protein_recovery_fraction",
                "marker_positive_viable",
                "functional_events_viable",
                "perk_0_au",
                "perk_10_au",
                "perk_30_au",
                "matrix_modulus_pa",
                "accessible_ligand_relative",
            )
            assert len(cultures) == 96
            for row in cultures:
                key = (row["form"], row["condition"], row["culture"])
                groups.setdefault(key, []).append(row)
                cultures_by_form_condition.setdefault(
                    (row["form"], row["condition"]), set()
                ).add(row["culture"])
                assert all(math.isfinite(float(row[field])) for field in numeric_fields)
                assert float(row["seeded_cells"]) > 0
                assert float(row["viable_cells"]) > 0
                assert (
                    0
                    < float(row["spike_recovered_eq"])
                    <= float(row["spike_input_eq"])
                )
                assert float(row["rna_signal_eq"]) > float(row["rna_background_eq"])
                assert float(row["protein_signal_ug"]) > float(
                    row["protein_background_ug"]
                )
                assert 0 < float(row["protein_recovery_fraction"]) <= 1
                assert (
                    0
                    <= int(row["marker_positive_viable"])
                    <= int(row["viable_cells"])
                )
                assert (
                    0
                    <= int(row["functional_events_viable"])
                    <= int(row["viable_cells"])
                )
                assert float(row["matrix_modulus_pa"]) > 0
                assert float(row["accessible_ligand_relative"]) > 0
            assert set(cultures_by_form_condition) == {
                (form, condition) for form in forms for condition in conditions
            }
            for form in forms:
                for condition in conditions:
                    assert cultures_by_form_condition[(form, condition)] == {
                        f"{form}-{condition}-{replicate:02d}"
                        for replicate in range(1, 5)
                    }
            assert len(groups) == 48
            for observations in groups.values():
                assert {float(row["time_h"]) for row in observations} == {0, 48}
        return
    if "clone" in rows[0]:
        assert len(rows) == 24
        groups = {}
        clones_by_condition = {}
        condition_by_clone = {}
        numeric_fields = (
            "viable_cells_thousands",
            "recovery_fraction",
            "protein_signal_ug",
            "protein_background_ug",
            "activity_signal_nmol_min",
            "activity_background_nmol_min",
            "response_positive_cells",
            "response_cells_assayed",
        )
        for row in rows:
            groups.setdefault(row["clone"], []).append(row)
            clones_by_condition.setdefault(row["condition"], set()).add(row["clone"])
            condition_by_clone[row["clone"]] = row["condition"]
            assert all(math.isfinite(float(row[key])) for key in numeric_fields)
            assert 0 < float(row["recovery_fraction"]) <= 1
            assert float(row["viable_cells_thousands"]) > 0
            assert float(row["protein_signal_ug"]) > float(row["protein_background_ug"])
            assert float(row["activity_signal_nmol_min"]) > float(
                row["activity_background_nmol_min"]
            )
            assert (
                0
                <= int(row["response_positive_cells"])
                <= int(row["response_cells_assayed"])
            )
        assert clones_by_condition == {
            "reference": {"q01", "q02", "q03", "q04"},
            "knockin": {"v01", "v02", "v03", "v04"},
            "corrected": {"z01", "z02", "z03", "z04"},
        }
        assert len(groups) == 12 and all(len(v) == 2 for v in groups.values())
        for clone, observations in groups.items():
            assert {row["culture"] for row in observations} == {
                f"{clone}a",
                f"{clone}b",
            }
            assert {row["condition"] for row in observations} == {
                condition_by_clone[clone]
            }
        return
    if "original_area_mm2" in rows[0]:
        assert len(rows) == 24
        groups = {}
        numeric_fields = (
            "original_area_mm2",
            "initial_length_mm",
            "extension_mm",
            "force_signal_n",
            "force_background_n",
            "accessible_ligand_au",
            "seeded_cells",
            "viable_attached_cells",
            "nuclear_marker_positive_cells",
            "summed_cell_area_um2",
        )
        for row in rows:
            groups.setdefault(row["preparation"], []).append(row)
            assert all(math.isfinite(float(row[key])) for key in numeric_fields)
            assert all(
                float(row[k]) > 0
                for k in ("original_area_mm2", "initial_length_mm", "extension_mm")
            )
            assert float(row["force_signal_n"]) > float(row["force_background_n"])
            assert (
                0
                <= int(row["nuclear_marker_positive_cells"])
                <= int(row["viable_attached_cells"])
                <= int(row["seeded_cells"])
            )
        expected_conditions = {
            "soft_low",
            "soft_high",
            "stiff_low",
            "stiff_high",
            "stiff_high_block",
            "stiff_high_rescue",
        }
        assert set(groups) == {"b01", "b02", "b03", "b04"}
        for observations in groups.values():
            assert len(observations) == 6
            assert {row["condition"] for row in observations} == expected_conditions
            assert len({row["seeded_cells"] for row in observations}) == 1
            by_condition = {row["condition"]: row for row in observations}
            low_ligand = {
                float(by_condition[condition]["accessible_ligand_au"])
                for condition in ("soft_low", "stiff_low")
            }
            high_ligand = {
                float(by_condition[condition]["accessible_ligand_au"])
                for condition in (
                    "soft_high",
                    "stiff_high",
                    "stiff_high_block",
                    "stiff_high_rescue",
                )
            }
            assert len(low_ligand) == len(high_ligand) == 1
            assert next(iter(high_ligand)) > next(iter(low_ligand))
        return
    if "viable_singlets" in rows[0]:
        assert len(rows) == 36
        groups = {}
        cultures_by_condition = {}
        for row in rows:
            groups.setdefault(row["culture"], []).append(row)
            cultures_by_condition.setdefault(row["condition"], set()).add(
                row["culture"]
            )
            live = int(row["viable_singlets"])
            assert live > 0 and live <= int(row["all_recovered_cells"])
            assert (
                sum(
                    int(row[k]) for k in ("dna_2n_cells", "dna_s_cells", "dna_4n_cells")
                )
                == live
            )
            assert all(
                0 <= int(row[k]) <= live
                for k in (
                    "edu_positive_viable",
                    "p21_high_viable",
                    "beta_gal_high_viable",
                    "mitotic_marker_positive_viable",
                )
            )
            assert (
                0
                <= int(row["caspase_positive_all_recovered"])
                <= int(row["all_recovered_cells"])
            )
        assert len(groups) == 12
        assert cultures_by_condition == {
            "vehicle": {"c01", "c02", "c03", "c04"},
            "withdrawal_refeed": {"w01", "w02", "w03", "w04"},
            "damage_challenge": {"g01", "g02", "g03", "g04"},
        }
        for observations in groups.values():
            assert {int(row["time_h"]) for row in observations} == {0, 24, 72}
            assert len({row["condition"] for row in observations}) == 1
        return
    if "rna_spike_input_eq" in rows[0]:
        assert len(rows) == 12 and len({row["culture"] for row in rows}) == 12
        preparations_by_condition = {}
        condition_by_culture = {}
        for row in rows:
            preparations_by_condition.setdefault(row["condition"], set()).add(
                row["culture"]
            )
            condition_by_culture[row["culture"]] = row["condition"]
            assert float(row["viable_cells_thousands"]) > 0
            assert (
                0
                < float(row["rna_spike_recovered_eq"])
                <= float(row["rna_spike_input_eq"])
            )
            for channel in ("included", "skipped", "shared", "precursor"):
                assert float(row[f"{channel}_signal_eq"]) > float(
                    row[f"{channel}_background_eq"]
                )
        assert preparations_by_condition == {
            "control": {"c01", "c02", "c03", "c04"},
            "depleted": {"d01", "d02", "d03", "d04"},
            "restored": {"r01", "r02", "r03", "r04"},
        }
        with (COURSE / CANDIDATE["additional_dataset_paths"][0]).open(
            newline=""
        ) as stream:
            chase = list(csv.DictReader(stream))
        assert len(chase) == 48
        assert {row["culture"] for row in chase} == {row["culture"] for row in rows}
        assert all(
            condition_by_culture[row["culture"]] == row["condition"] for row in chase
        )
        for culture in {row["culture"] for row in rows}:
            assert {
                float(row["time_h"]) for row in chase if row["culture"] == culture
            } == {0, 2, 4, 6}
        for row in chase:
            assert all(
                math.isfinite(float(row[key]))
                for key in (
                    "time_h",
                    "labeled_target_signal_au",
                    "labeled_target_background_au",
                    "recovery_reference_au",
                )
            )
            assert float(row["recovery_reference_au"]) > 0
            assert float(row["labeled_target_signal_au"]) > float(
                row["labeled_target_background_au"]
            )
        return
    if "amplification_factor" in rows[0]:
        assert len(rows) == 72
        groups = {}
        cultures_by_condition = {}
        for row in rows:
            groups.setdefault((row["culture"], row["locus"]), []).append(row)
            cultures_by_condition.setdefault(row["condition"], set()).add(
                row["culture"]
            )
            assert 0 < float(row["input_fraction"]) <= 1
            assert 1 < float(row["amplification_factor"]) <= 2
            assert all(
                math.isfinite(float(row[key]))
                for key in ("cq_input", "cq_specific", "cq_igg")
            )
        assert len(groups) == 36
        for observations in groups.values():
            assert {row["technical_well"] for row in observations} == {"1", "2"}
            assert (
                len(
                    {
                        (
                            row["condition"],
                            row["input_fraction"],
                            row["amplification_factor"],
                        )
                        for row in observations
                    }
                )
                == 1
            )
        assert cultures_by_condition == {
            "control": {"c01", "c02", "c03", "c04"},
            "knockdown": {"k01", "k02", "k03", "k04"},
            "restored": {"s01", "s02", "s03", "s04"},
        }
        assert len(CANDIDATE["additional_dataset_paths"]) == 1
        with (COURSE / CANDIDATE["additional_dataset_paths"][0]).open(
            newline=""
        ) as stream:
            reporters = list(csv.DictReader(stream))
        assert len(reporters) == 12
        assert len({row["preparation"] for row in reporters}) == 12
        reporter_preparations_by_condition = {}
        for row in reporters:
            reporter_preparations_by_condition.setdefault(row["condition"], set()).add(
                row["preparation"]
            )
        assert reporter_preparations_by_condition == {
            "control": {"rc01", "rc02", "rc03", "rc04"},
            "knockdown": {"rk01", "rk02", "rk03", "rk04"},
            "restored": {"rs01", "rs02", "rs03", "rs04"},
        }
        assert not {row["preparation"] for row in reporters}.intersection(
            row["culture"] for row in rows
        )
        for row in reporters:
            for construct in ("promoter", "wt", "mutant", "positive"):
                for channel in ("firefly", "renilla"):
                    assert float(row[f"{construct}_{channel}_au"]) > float(
                        row[f"{construct}_{channel}_background_au"]
                    )
        return
    if "dna_reference_au" in rows[0]:
        assert len(rows) == 36
        groups = {}
        cultures_by_condition = {}
        numeric_fields = (
            "loaded_dna_ng",
            "lesion_signal_au",
            "lesion_background_au",
            "dna_reference_au",
            "viable_cells_thousands",
            "dna_synthesis_label_pct",
        )
        for row in rows:
            groups.setdefault(row["culture"], []).append(row)
            cultures_by_condition.setdefault(row["condition"], set()).add(
                row["culture"]
            )
            assert all(math.isfinite(float(row[key])) for key in numeric_fields)
            assert float(row["dna_reference_au"]) > 0
            assert float(row["lesion_signal_au"]) >= float(row["lesion_background_au"])
            assert float(row["loaded_dna_ng"]) > 0
            assert float(row["viable_cells_thousands"]) >= 0
            assert 0 <= float(row["dna_synthesis_label_pct"]) <= 100
        assert len(groups) == 12
        assert cultures_by_condition == {
            "wt": {"w01", "w02", "w03", "w04"},
            "factor_depleted": {"d01", "d02", "d03", "d04"},
            "factor_restored": {"r01", "r02", "r03", "r04"},
        }
        for observations in groups.values():
            assert {float(row["time_h"]) for row in observations} == {0, 2, 6}
            assert len({row["condition"] for row in observations}) == 1
        return
    if "series" in rows[0]:
        assert len(rows) == 420
        assert len({tuple(row.values())[:-1] for row in rows}) == len(rows)
        days = {"d01", "d02", "d03", "d04"}
        conditions = {"vehicle", "compound_a", "compound_b"}
        assert {row["day"] for row in rows} == days
        assert {row["condition"] for row in rows} == conditions
        blocks = {}
        for row in rows:
            assert math.isfinite(float(row["signal_au"]))
            blocks.setdefault((row["day"], row["condition"]), []).append(row)
        assert set(blocks) == {(day, condition) for day in days for condition in conditions}
        for observations in blocks.values():
            standards = [row for row in observations if row["series"] == "standard"]
            assert {float(row["product_standard_nm"]) for row in standards} == {
                0,
                500,
                1000,
            }
            for series in ("blank", "reaction"):
                selected = [row for row in observations if row["series"] == series]
                assert len(selected) == 16
                assert {float(row["substrate_um"]) for row in selected} == {
                    5,
                    15,
                    45,
                    135,
                }
                assert {float(row["time_s"]) for row in selected} == {0, 2, 4, 10}
        return
    groups = {}
    preparations_by_condition = {}
    numeric_fields = (
        "pulse_input_nmol",
        "lysosome_intact_nmol",
        "medium_intact_nmol",
        "other_intact_nmol",
        "fragments_nmol",
        "lysosome_marker_recovery_pct",
        "binding_index",
        "receptor_abundance_index",
        "viability_pct",
    )
    for row in rows:
        groups.setdefault(row["preparation"], []).append(row)
        preparations_by_condition.setdefault(row["condition"], set()).add(
            row["preparation"]
        )
        assert all(math.isfinite(float(row[key])) for key in numeric_fields)
        assert float(row["pulse_input_nmol"]) > 0
        assert 0 < float(row["lysosome_marker_recovery_pct"]) <= 100
        assert float(row["binding_index"]) > 0
        assert float(row["receptor_abundance_index"]) > 0
        assert 0 <= float(row["viability_pct"]) <= 100
        amounts = [
            float(row[key])
            for key in (
                "lysosome_intact_nmol",
                "medium_intact_nmol",
                "other_intact_nmol",
                "fragments_nmol",
            )
        ]
        assert all(value >= 0 for value in amounts)
        assert sum(amounts) <= float(row["pulse_input_nmol"])
    assert len(rows) == 36 and len(groups) == 12
    assert preparations_by_condition == {
        "wt": {"w01", "w02", "w03", "w04"},
        "motif_mutant": {"m01", "m02", "m03", "m04"},
        "motif_repaired": {"r01", "r02", "r03", "r04"},
    }
    for observations in groups.values():
        assert {int(r["chase_min"]) for r in observations} == {0, 30, 90}
        assert len({r["condition"] for r in observations}) == 1
        assert len({r["pulse_input_nmol"] for r in observations}) == 1


def test_handout_contains_all_stems_fields_and_explicit_inactive_scope(candidate):
    CANDIDATE = candidate
    text = (COURSE / CANDIDATE["instruction_path"]).read_text(encoding="utf-8")
    assert "inactive candidate" in text.lower()
    assert "workload has not been measured" in text.lower()
    assert "no live submission route" in text.lower()
    for question in CANDIDATE["questions"]:
        assert question["prompt"] in text
        for option in question["options"]:
            assert option in text
        for field in question["response_fields"]:
            assert field["prompt"] in text
            assert all(option in text for option in field["options"])


def test_candidate_does_not_activate_any_catalog_grade_or_private_source(candidate):
    CANDIDATE = candidate
    assert CANDIDATE["candidate_id"] not in {a["id"] for a in MANIFEST["assessments"]}
    for path in (ROOT / "content/courses").glob("*/course.json"):
        course = json.loads(path.read_text(encoding="utf-8"))
        assert course["maturity"] == "partial"
        assert course["review"]["status"] == "unreviewed"
        assert course["grading_policy"]["mode"] == "formative-only"
        assert all(a["mode"] != "graded" for a in course["assessments"])
        assert all(
            not a["path"].startswith("private://") for a in course["assessments"]
        )


def test_authored_variants_remain_answer_free_and_field_mappings_are_complete(
    candidate,
):
    if "variant_questions" not in candidate:
        return
    questions = {q["id"]: q for q in candidate["questions"]}
    assert set(candidate["variant_questions"]) == set(questions)
    forbidden = {
        "solution_spec",
        "answer",
        "field_specs",
        "feedback",
        "rubric",
        "checks",
    }
    assert not forbidden.intersection(nested_keys(candidate["variant_questions"]))
    for key, variant in candidate["variant_questions"].items():
        assert variant["variant_id"] == "form-b"
        assert variant["prompt"] != questions[key]["prompt"]
        assert variant["response_fields"] == questions[key]["response_fields"]
        assert variant["prompt"] in (
            COURSE / candidate["instruction_path"]
        ).read_text(encoding="utf-8")
    mappings = candidate["objective_evidence"]
    assert {(r["question_id"], r["field_id"]) for r in mappings} == {
        (q["id"], f["id"]) for q in questions.values() for f in q["response_fields"]
    }
    assert {o for r in mappings for o in r["objective_ids"]} == set(
        candidate["objective_ids"]
    )
    assert sum(r["points"] for r in mappings) == candidate["points"]
    for row in mappings:
        field = next(
            f
            for f in questions[row["question_id"]]["response_fields"]
            if f["id"] == row["field_id"]
        )
        assert row["points"] == field["points"]
