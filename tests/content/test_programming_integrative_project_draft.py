"""Construction and release-boundary checks for the inactive Programming capstone draft."""

from __future__ import annotations

import csv
import json
import math
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/programming"
PROJECT = COURSE / "assessment-specs/integrative-sensor-calibration-project.md"
DATA = COURSE / "assessment-specs/sensor-calibration-records.csv"
GENERATOR = COURSE / "assessment-specs/generate_sensor_calibration_records.py"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def test_project_dataset_is_deterministic_and_has_the_declared_contract(tmp_path):
    output = tmp_path / "rerun" / "records.csv"
    subprocess.run(
        [sys.executable, str(GENERATOR), "--output", str(output)],
        check=True,
        capture_output=True,
        text=True,
    )

    assert output.read_bytes() == DATA.read_bytes()
    rows = read_rows(DATA)
    assert len(rows) == 90
    assert len({row["record_id"] for row in rows}) == 90
    assert set(rows[0]) == {
        "record_id",
        "batch_id",
        "split",
        "standard_mM",
        "signal_mV",
        "replicate_id",
    }
    assert {row["split"] for row in rows} == {"train", "held_out"}


def test_project_calibration_and_held_out_batch_errors_recalculate():
    rows = read_rows(DATA)
    training = [row for row in rows if row["split"] == "train"]
    levels = [float(row["standard_mM"]) for row in training]
    signals = [float(row["signal_mV"]) for row in training]
    mean_level = math.fsum(levels) / len(levels)
    mean_signal = math.fsum(signals) / len(signals)
    slope = math.fsum(
        (level - mean_level) * (signal - mean_signal)
        for level, signal in zip(levels, signals)
    ) / math.fsum((level - mean_level) ** 2 for level in levels)
    intercept = mean_signal - slope * mean_level

    assert intercept == pytest.approx(20.0)
    assert slope == pytest.approx(3.0)

    residuals_by_batch: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        if row["split"] != "held_out":
            continue
        level = float(row["standard_mM"])
        observed = float(row["signal_mV"])
        residuals_by_batch[row["batch_id"]].append(observed - (intercept + slope * level))

    expected = {"B05": (4.0, 4.003331), "B06": (-3.0, 3.004441)}
    assert set(residuals_by_batch) == set(expected)
    for batch_id, (mean_error, rmse) in expected.items():
        residuals = residuals_by_batch[batch_id]
        assert math.fsum(residuals) / len(residuals) == pytest.approx(mean_error)
        actual_rmse = math.sqrt(math.fsum(error**2 for error in residuals) / len(residuals))
        assert actual_rmse == pytest.approx(rmse, abs=1e-6)


def test_capstone_remains_an_inactive_ungraded_authoring_draft():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    project = PROJECT.read_text(encoding="utf-8")
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert all("integrative-project" not in item["id"] for item in manifest["assessments"])
    assert "Inactive authoring draft" in project
    assert "carries no points or course grade" in project
    assert "assessment-specs/integrative-sensor-calibration-project.md" in syllabus
    assert "inactive, ungraded draft" in syllabus and "not part of the assessment schedule" in syllabus


def test_programming_review_snapshot_matches_the_public_package():
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/course_package_digest.py"),
            "--course-id",
            "programming",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    actual = json.loads(result.stdout)
    snapshot = (ROOT / "docs/PROGRAMMING_REVIEW_SNAPSHOT.md").read_text(encoding="utf-8")

    assert actual["course_id"] == "programming"
    assert actual["content_version"] == "0.5.0"
    assert re.search(
        r"Public package archive SHA-256:\*\*\s*`([0-9a-f]{64})`", snapshot
    ).group(1) == actual["package_sha256"]
    assert re.search(r"Manifest SHA-256:\*\*\s*`([0-9a-f]{64})`", snapshot).group(1) == actual[
        "manifest_sha256"
    ]
    assert re.search(
        r"Archive inventory:\*\*\s*(\d+) files, ([\d,]+) bytes", snapshot
    ).groups() == (
        str(actual["file_count"]),
        f"{actual['archive_bytes']:,}",
    )
