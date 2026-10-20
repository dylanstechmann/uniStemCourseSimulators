"""Integrity checks for the cell-biology package and the generated gap report.

These tests read committed files only. They do not judge teaching quality, and passing them does not
mean any component was reviewed. They exist so the homework, lab and specification files cannot drift
away from the question bank, from their own example tables, or from the rule that no answer key for a
protected component is committed.
"""

from __future__ import annotations

import csv
import io
import json
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content" / "courses" / "cell-biology"
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def bank():
    return json.loads((COURSE / "question-banks" / "practice.json").read_text(encoding="utf-8"))["questions"]


def markdown_files():
    return sorted(p for p in COURSE.rglob("*.md"))


def test_relative_links_in_cell_biology_markdown_resolve():
    broken = []
    for path in markdown_files():
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in LINK.findall(text):
            if re.match(r"[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            if file_part and not (path.parent / file_part).resolve().exists():
                broken.append(f"{path.relative_to(COURSE)} -> {target}")
    assert not broken, broken


def test_every_homework_and_lab_dataset_link_names_a_committed_file():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    learner_resources = set(manifest["learner_resources"])
    missing = []
    for path in list((COURSE / "assignments").glob("*.md")) + list((COURSE / "labs").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for destination in LINK.findall(text):
            if re.match(r"[a-z][a-z0-9+.-]*:", destination):
                continue
            file_part = destination.split("#", 1)[0].split("?", 1)[0]
            if not file_part.lower().endswith(".csv"):
                continue
            target = (path.parent / file_part).resolve()
            if not target.is_file():
                missing.append(f"{path.name}: {file_part} does not exist")
                continue
            resource_path = target.relative_to(COURSE).as_posix()
            if path.parent.name == "assignments" and resource_path not in learner_resources:
                missing.append(f"{path.name}: {resource_path} is not allowlisted")
    assert not missing, missing


def test_open_homework_and_lab_package_labels_name_a_released_version():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    packets = sorted((COURSE / "assignments").glob("homework-0[1-8]-*.md"))
    packets.extend(sorted((COURSE / "labs").glob("0[1-3]-*.md")))
    assert len(packets) == 11
    for path in packets:
        text = path.read_text(encoding="utf-8")
        match = re.search(r"^\*\*Course package:\*\*.*?version (\d+(?:\.\d+)+)", text, re.M)
        assert match is not None, path.name
        # Lab labels are frozen inside lab-candidate prerequisite digests; they must name a released
        # version, and relabelling them needs a deliberate candidate re-binding.
        assert match.group(1) in {entry["version"] for entry in manifest["history"]}, (path.name, match.group(1))
        time_label = re.search(
            r"^\*\*(?:Suggested time|Estimated learner time) \(unvalidated author estimate\):\*\* 2–3 hours$",
            text,
            re.M,
        )
        assert time_label is not None, path.name
    assert syllabus.count("unvalidated author-estimated time: 2–3 hours") == 2
    assert "Week 5 includes a virtual fluorescence-count data lab" in syllabus
    assert "Week 11 includes a synthetic signaling time-course lab" in syllabus


def test_every_csv_summary_check_carries_an_independent_recalculation():
    unchecked = []
    for question in bank():
        if question["type"] != "file_upload":
            continue
        for check in question["solution_spec"]["validation_spec"]["checks"]:
            calculation = check.get("calculation")
            if not isinstance(calculation, dict) or calculation.get("operation") not in {"count", "mean"}:
                unchecked.append(f"{question['id']}:{check['id']}")
    assert not unchecked, unchecked


def parse_example_blocks(markdown: str):
    for block in re.findall(r"```csv\n(.*?)```", markdown, flags=re.S):
        yield list(csv.reader(io.StringIO(block.strip())))


def load_csv(path):
    with path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def test_homework_example_means_recalculate_from_linked_datasets():
    source_columns = {
        "01": {
            "mean_lysosomal_delivery_pct": "lysosomal_delivery_pct",
            "mean_conditioned_medium_pct": "conditioned_medium_pct",
        },
        "02": {"mean_rate_nm_per_s": "initial_rate_nm_per_s"},
        "03": {
            "mean_lesion_remaining_pct": "lesion_remaining_pct_4h",
            "mean_s_phase_pct": "s_phase_pct",
        },
        "04": {
            "mean_specific_pct_input": "chip_specific_pct_input",
            "mean_igg_pct_input": "chip_igg_pct_input",
            "mean_reporter_wt": "reporter_wt_rel",
            "mean_reporter_mut": "reporter_mut_rel",
        },
        "05": {
            "mean_mrna": "mrna_rel",
            "mean_protein": "protein_rel",
            "mean_labeling": "nascent_labeling_rel",
            "mean_remaining_4h": "protein_remaining_4h_pct",
        },
        "06": {"mean_assay_score": "assay_score"},
        "07": {
            "mean_spread_area_um2": "spread_area_um2",
            "mean_cell_density": "cell_density_per_mm2",
            "mean_ligand_density": "ligand_density_rel",
        },
        "08": {
            "mean_edu_pct": "edu_pct",
            "mean_sabgal_pct": "sabgal_pct",
            "mean_reentry_edu_pct": "reentry_edu_pct",
        },
    }
    for packet_path in sorted((COURSE / "assignments").glob("homework-0[1-8]-*.md")):
        packet = packet_path.read_text(encoding="utf-8")
        homework_number = re.search(r"homework-(\d\d)-", packet_path.name).group(1)
        dataset_link = re.search(
            r"\*\*Dataset:\*\*.*?\]\(([^)]+\.csv)\)", packet
        ).group(1)
        with (packet_path.parent / dataset_link).open(
            encoding="utf-8", newline=""
        ) as dataset_file:
            dataset = list(csv.DictReader(dataset_file))
        if homework_number == "02":
            dataset = [row for row in dataset if row["substrate_uM"] == "40"]

        grouped = {}
        for row in dataset:
            grouped.setdefault(row["condition"], []).append(row)
        example_tables = list(parse_example_blocks(packet))
        assert len(example_tables) == 1, packet_path.name
        example = example_tables[0]
        assert example[0][0:2] == ["condition", "batch_count"], packet_path.name
        assert example[0][2:] == list(source_columns[homework_number]), packet_path.name

        means = {}
        for example_row in example[1:]:
            condition, batch_count, *shown_means = example_row
            observations = grouped[condition]
            assert int(batch_count) == len(observations) == 4, packet_path.name
            condition_means = {}
            for shown_column, shown_value in zip(example[0][2:], shown_means):
                source_column = source_columns[homework_number][shown_column]
                observed_mean = sum(float(row[source_column]) for row in observations) / len(observations)
                assert abs(float(shown_value) - observed_mean) < 1e-9, (
                    packet_path.name,
                    condition,
                    shown_column,
                    shown_value,
                    observed_mean,
                )
                condition_means[shown_column] = observed_mean
            means[condition] = condition_means
        assert set(means) == set(grouped), packet_path.name

        if homework_number == "01":
            wt = means["wt"]["mean_lysosomal_delivery_pct"]
            mutant = means["tail_mutant"]["mean_lysosomal_delivery_pct"]
            contrast = mutant - wt
            contrast_text = f"−{abs(contrast):.2f}" if contrast < 0 else f"{contrast:.2f}"
            assert (
                f"{mutant:.2f}% − {wt:.2f}% = {contrast_text} percentage points"
            ) in packet


def test_virtual_lab_worked_examples_recalculate_from_linked_datasets():
    image_rows = load_csv(COURSE / "labs/image-counts.csv")
    image_lab = (COURSE / "labs/01-fluorescence-image-quantification.md").read_text(
        encoding="utf-8"
    )
    image_means = {}
    for condition in {row["condition"] for row in image_rows}:
        rows = [row for row in image_rows if row["condition"] == condition]
        image_means[condition] = math.fsum(
            100 * float(row["marker_positive_nuclei"]) / float(row["viable_nuclei"])
            for row in rows
        ) / len(rows)
    image_difference = image_means["cue"] - image_means["vehicle"]
    assert image_means == {"vehicle": 13.0, "cue": 22.0}
    assert (
        "The expected descriptive means are 13% for vehicle and 22% for cue, "
        "a difference of 9 percentage points."
    ) in image_lab
    assert image_difference == 9

    signaling_rows = load_csv(COURSE / "labs/signaling-timecourse.csv")
    signaling_lab = (
        COURSE / "labs/02-signaling-dynamics-inhibitor-rescue.md"
    ).read_text(encoding="utf-8")
    label_to_condition = {
        "Vehicle": "vehicle",
        "Ligand pulse": "ligand_pulse",
        "Continuous ligand": "ligand_continuous",
        "Ligand + MEK inhibitor": "continuous_meki",
        "Ligand + receptor inhibitor": "ligand_egfri",
        "Receptor inhibitor + active MEK": "egfri_active_mek",
    }
    table_match = re.search(
        r"(?ms)^\| Condition \| Perturbation schedule \| 2-min mean \| 60-min mean \|\n"
        r"(?P<table>(?:^\|[^\n]*\n)+)",
        signaling_lab,
    )
    assert table_match is not None
    shown_rows = [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in table_match.group("table").splitlines()
        if line.strip().startswith("|") and not re.search(r"\|\s*:?-+", line)
    ]
    assert len(shown_rows) == 6
    for label, _, shown_2min, shown_60min in shown_rows:
        condition = label_to_condition[label]
        for time_text, shown in (("2", shown_2min), ("60", shown_60min)):
            observations = [
                float(row["perk_totalerk_relative"])
                for row in signaling_rows
                if row["condition"] == condition and row["time_min"] == time_text
            ]
            expected = math.fsum(observations) / len(observations)
            assert len(observations) == 4
            assert math.isclose(float(shown), expected, rel_tol=0, abs_tol=0.005)

    def signal_mean(condition):
        values = [
            float(row["perk_totalerk_relative"])
            for row in signaling_rows
            if row["condition"] == condition and row["time_min"] == "2"
        ]
        return math.fsum(values) / len(values)

    vehicle = signal_mean("vehicle")
    ligand = signal_mean("ligand_continuous")
    inhibitor = signal_mean("continuous_meki")
    suppression = 100 * (1 - (inhibitor - vehicle) / (ligand - vehicle))
    worked = re.search(
        r"## Worked calculation\s*\n(.*?)(?=\n## )", signaling_lab, re.S
    ).group(1)
    assert math.isclose(suppression, 96.15, rel_tol=0, abs_tol=0.005)
    assert "= 96.15%, or 96.2% to three significant figures" in worked

    lineage_rows = load_csv(COURSE / "labs/lineage-timecourse.csv")
    lineage_lab = (
        COURSE / "labs/03-lineage-time-course-and-state-inference.md"
    ).read_text(encoding="utf-8")
    summary_blocks = list(parse_example_blocks(lineage_lab))
    assert len(summary_blocks) == 1
    summary = summary_blocks[0]
    assert summary[0] == [
        "condition",
        "batch_count",
        "mean_lineage_pct",
        "mean_pluripotency_pct",
        "mean_cells_thousands",
    ]
    summary_columns = {
        "mean_lineage_pct": "lineage_marker_pct",
        "mean_pluripotency_pct": "pluripotency_marker_pct",
        "mean_cells_thousands": "cells_per_well_thousands",
    }
    lineage_means = {}
    for condition, batch_count, *shown_means in summary[1:]:
        rows = [
            row
            for row in lineage_rows
            if row["condition"] == condition and row["day"] == "8"
        ]
        assert len(rows) == int(batch_count) == 4
        values_by_column = {}
        for shown, (output_column, source_column) in zip(
            shown_means, summary_columns.items()
        ):
            mean = math.fsum(float(row[source_column]) for row in rows) / len(rows)
            assert math.isclose(float(shown), mean, rel_tol=0, abs_tol=1e-9)
            values_by_column[output_column] = mean
        lineage_means[condition] = values_by_column

    control_lineage = lineage_means["control"]["mean_lineage_pct"]
    factor_lineage = lineage_means["factor"]["mean_lineage_pct"]
    difference = factor_lineage - control_lineage
    control_cells = lineage_means["control"]["mean_cells_thousands"]
    factor_cells = lineage_means["factor"]["mean_cells_thousands"]
    worked = re.search(
        r"## Worked calculation\s*\n(.*?)(?=\n## )", lineage_lab, re.S
    ).group(1)
    assert difference == 51
    assert control_cells == 451 and factor_cells == 241
    assert (
        "58.5% lineage-marker-positive cells against 7.5% in control, "
        "a 51 percentage-point difference."
    ) in worked
    assert "241 thousand with the factor and 451 thousand in control" in worked


def test_homework_worked_calculations_recalculate_from_source_data():
    """Key worked rates, contrasts, ratios and half-life must track their source data."""
    assignment_dir = COURSE / "assignments"

    def packet_and_dataset(number):
        packet_path = next(assignment_dir.glob(f"homework-{number}-*.md"))
        packet = packet_path.read_text(encoding="utf-8")
        link = re.search(r"\*\*Dataset:\*\*.*?\]\(([^)]+\.csv)\)", packet).group(1)
        with (packet_path.parent / link).open(encoding="utf-8", newline="") as source:
            rows = list(csv.DictReader(source))
        worked = re.search(r"## Worked calculation\s*\n(.*?)(?=\n## )", packet, re.S).group(1)
        return packet, rows, worked

    def mean(rows, column):
        return sum(float(row[column]) for row in rows) / len(rows)

    # Homework 2's printed model table and worked cross-point use different
    # apparent constants for the competitive and uncompetitive models.
    packet, rows, worked = packet_and_dataset("02")
    model_table = re.search(r"Curve values [^\n]*\n\n((?:\|[^\n]*\n)+)", packet).group(1)
    model_rows = [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in model_table.splitlines()
        if line.strip().startswith("|") and not re.search(r"\|\s*:?-+", line)
    ]
    assert len(model_rows) == 7
    for substrate_text, vehicle_text, a_text, b_text in model_rows[1:]:
        substrate = float(substrate_text)
        expected = (
            120 * substrate / (20 + substrate),
            120 * substrate / (60 + substrate),
            60 * substrate / (10 + substrate),
        )
        for shown, computed in zip((vehicle_text, a_text, b_text), expected):
            assert float(shown) == round(computed, 2), (substrate, shown, computed)
    at_40 = [row for row in rows if row["substrate_uM"] == "40"]
    inhibitor_a = mean([row for row in at_40 if row["condition"] == "inhibitor_a"], "initial_rate_nm_per_s")
    inhibitor_b = mean([row for row in at_40 if row["condition"] == "inhibitor_b"], "initial_rate_nm_per_s")
    assert inhibitor_a == inhibitor_b == 48
    assert worked.count("= 48 nM·s⁻¹") == 3
    assert "At `[S] = 5 µM` A gives 9.23 and B gives 20.00" in worked
    assert "at `[S] = 160 µM` A gives 87.27 and B gives 56.47" in worked

    # Homework 3: the signed percentage-point difference uses the two source means.
    _, rows, worked = packet_and_dataset("03")
    wt = mean([row for row in rows if row["condition"] == "wt"], "lesion_remaining_pct_4h")
    deficient = mean([row for row in rows if row["condition"] == "repair_deficient"], "lesion_remaining_pct_4h")
    assert (wt, deficient, deficient - wt) == (40, 85, 45)
    assert "= 40%" in worked and "averages 85%" in worked and "45 percentage points" in worked

    # Homework 4: enrichment is the ratio of the two control-condition means.
    _, rows, worked = packet_and_dataset("04")
    control = [row for row in rows if row["condition"] == "control"]
    knockdown = [row for row in rows if row["condition"] == "knockdown"]
    specific = mean(control, "chip_specific_pct_input")
    igg = mean(control, "chip_igg_pct_input")
    enrichment = specific / igg
    assert (specific, igg, round(enrichment, 2), mean(knockdown, "chip_specific_pct_input")) == (6.1, 0.45, 13.56, 2.2)
    assert "6.1 / 0.45 = 13.56-fold" in worked

    # Homework 5: the mean wild-type remaining fraction gives a 4-hour half-life.
    _, rows, worked = packet_and_dataset("05")
    wt_rows = [row for row in rows if row["condition"] == "wt"]
    remaining_fraction = mean(wt_rows, "protein_remaining_4h_pct") / 100
    half_life = -4 * math.log(2) / math.log(remaining_fraction)
    assert remaining_fraction == 0.5 and half_life == 4
    assert "half-life is 4 h in both" in worked

    # Homework 6: derive penetrance from the authored table and check clone means.
    packet, rows, worked = packet_and_dataset("06")
    carrier_count, affected_carriers = map(int, re.search(r"\| Variant carriers \| (\d+) \| (\d+) \|", packet).groups())
    noncarrier_count, affected_noncarriers = map(int, re.search(r"\| Non-carriers \| (\d+) \| (\d+) \|", packet).groups())
    carrier_rate = affected_carriers / carrier_count
    noncarrier_rate = affected_noncarriers / noncarrier_count
    ratio = carrier_rate / noncarrier_rate
    clone_means = {condition: mean([row for row in rows if row["condition"] == condition], "assay_score")
                   for condition in {row["condition"] for row in rows}}
    assert (carrier_rate, noncarrier_rate, round(ratio, 12)) == (0.6, 0.1, 6)
    assert clone_means == {"parental_variant": 41, "corrected": 78.5, "reintroduced": 42}
    assert "18 / 30 = 60%" in worked and "7 / 70 = 10%" in worked and "six times" in worked
    assert "= 41" in worked and "78.5" in worked and "variant 42" in worked

    # Homework 7: compute the stiff-to-soft ratio from the culture-level values.
    _, rows, worked = packet_and_dataset("07")
    soft = mean([row for row in rows if row["condition"] == "soft"], "spread_area_um2")
    stiff = mean([row for row in rows if row["condition"] == "stiff"], "spread_area_um2")
    assert (soft, stiff, round(stiff / soft, 2)) == (425, 1490, 3.51)
    assert "= 425 µm²" in worked and "1490 µm² on stiff" in worked and "1490 / 425 = 3.51" in worked

    # Homework 8: summarize the source markers and the post-stimulation contrast.
    _, rows, worked = packet_and_dataset("08")
    quiescent = [row for row in rows if row["condition"] == "quiescent"]
    damage = [row for row in rows if row["condition"] == "damage_induced"]
    q_reentry = mean(quiescent, "reentry_edu_pct")
    d_reentry = mean(damage, "reentry_edu_pct")
    assert (mean(quiescent, "edu_pct"), mean(damage, "edu_pct")) == (5, 4)
    assert (mean(quiescent, "sabgal_pct"), mean(damage, "sabgal_pct")) == (9, 65)
    assert (q_reentry, d_reentry, q_reentry - d_reentry) == (34, 6, 28)
    assert "5% and 4% against 40%" in worked
    assert "9% in the serum-withdrawn cultures and 65%" in worked
    assert "34% for the quiescent cultures and 6%" in worked and "28 percentage-point difference" in worked


def test_example_summary_tables_in_packets_equal_the_authored_keys():
    """The tables a learner is shown as the required format must agree with the grader's answers."""
    keys = {}
    for question in bank():
        if question["type"] == "file_upload":
            spec = question["solution_spec"]["validation_spec"]
            for check in spec["checks"]:
                keys.setdefault((tuple(spec["columns"]), check["row_id"], check["column"]), check["answer"])
    mismatches, compared = [], 0
    for path in list((COURSE / "assignments").glob("homework-0[2-8]-*.md")) + list((COURSE / "labs").glob("03-*.md")):
        for table in parse_example_blocks(path.read_text(encoding="utf-8")):
            header = tuple(table[0])
            for row in table[1:]:
                for column, value in zip(header[1:], row[1:]):
                    key = (header, row[0], column)
                    assert key in keys, f"{path.name}: example cell {key} has no authored check"
                    compared += 1
                    if abs(float(value) - float(keys[key])) > 1e-9:
                        mismatches.append(f"{path.name}: {key} shows {value}, key is {keys[key]}")
    assert compared >= 60
    assert not mismatches, mismatches


def test_assessment_specifications_contain_no_keys_and_describe_inactive_drafts():
    folder = COURSE / "assessment-specs"
    documents = sorted(folder.glob("*.md"))
    assert {p.name for p in documents} >= {"midterm-specification.md", "final-specification.md",
                                           "integrative-project-specification.md"}
    for path in documents:
        text = path.read_text(encoding="utf-8")
        assert '"solution_spec"' not in text and '"answer"' not in text, path.name
        if path.name.endswith("-specification.md"):
            assert "inactive" in text.lower()
            assert "no protected answer package is committed" in text.lower()
            assert "No reviewer has examined this specification" in text
    other = [p for p in folder.iterdir() if p.is_file() and p.suffix not in {".md"}]
    assert {path.name for path in other} == {
        "homework-01-candidate-pulse-chase.csv", "homework-01-candidate.json",
        "homework-02-candidate-fluorescence.csv", "homework-02-candidate.json",
        "homework-03-candidate-lesion-reference.csv", "homework-03-candidate.json",
        "homework-04-candidate-chip.csv", "homework-04-candidate-reporter.csv", "homework-04-candidate.json",
        "homework-05-candidate-baseline.csv", "homework-05-candidate-chase.csv", "homework-05-candidate.json",
        "homework-06-candidate-clones.csv", "homework-06-candidate.json",
        "homework-07-candidate-matrix.csv", "homework-07-candidate.json",
        "homework-08-candidate-fate.csv", "homework-08-candidate.json",
        "midterm-candidate.json", "midterm-candidate-observations.csv",
        "final-candidate.json", "final-candidate-observations.csv", "final-v2-candidate.json",
        "lab-01-candidate.json", "lab-01-candidate-observations.csv",
        "lab-02-candidate.json", "lab-02-candidate-observations.csv",
        "lab-03-candidate.json", "lab-03-candidate-observations.csv",
        "integrative-project-candidate.json", "integrative-project-candidate-observations.csv",
        "integrative-project-candidate-cultures.csv", "generate_project_dataset.py"
    }, f"unexpected non-document files beside the specifications: {other}"


def test_no_answer_package_files_are_committed_anywhere_in_the_course_tree():
    offenders = [str(p.relative_to(ROOT)) for p in (ROOT / "content").rglob("*.json")
                 if "private" in p.parts or p.name.startswith("answer-package")]
    assert not offenders, offenders


def test_course_labels_are_unchanged_by_the_new_material():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert course["maturity"] == "partial"
    assert course["review"] == {"status": "unreviewed", "reviewed_version": None, "reviewers": []}
    assert course["grading_policy"]["mode"] == "formative-only"
    assert course["grading_policy"]["categories"] == []
    for assessment in course["assessments"]:
        assert assessment["mode"] in {"practice", "self-assessment"}, assessment["id"]


def test_homework_points_equal_the_sum_of_their_items():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    points = {q["id"]: q["points"] for q in bank()}
    for assessment in course["assessments"]:
        if assessment["type"] in {"homework", "lab"}:
            assert assessment["points"] == sum(points[i] for i in assessment["question_ids"]), assessment["id"]


def test_gap_report_is_current():
    result = subprocess.run([sys.executable, "-B", str(ROOT / "tools" / "objective_coverage.py"), "--check",
                             str(ROOT / "docs" / "COURSE_GAP_REPORT.md")], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_review_snapshot_matches_deterministic_public_package_digest():
    snapshot = (ROOT / "docs/CELL_BIOLOGY_REVIEW_SNAPSHOT.md").read_text(encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools/course_package_digest.py"), "--course-id", "cell-biology"],
        check=True,
        capture_output=True,
        text=True,
    )
    digest = json.loads(result.stdout)
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))

    assert digest["content_version"] == course["version"] == "0.62.1"
    assert f'Public package archive SHA-256:** `{digest["package_sha256"]}`' in snapshot
    assert f'Manifest SHA-256:** `{digest["manifest_sha256"]}`' in snapshot
    assert f'{digest["file_count"]} files, {digest["archive_bytes"]:,} bytes' in snapshot
