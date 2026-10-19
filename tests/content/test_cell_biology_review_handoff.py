"""Ensure the Cell Biology review packet names the exact public package."""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_cell_biology_review_handoff_matches_pinned_public_package():
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/course_package_digest.py"),
            "--course-id",
            "cell-biology",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    actual = json.loads(result.stdout)
    snapshot = (ROOT / "docs/CELL_BIOLOGY_REVIEW_SNAPSHOT.md").read_text(
        encoding="utf-8"
    )
    handoff = (ROOT / "docs/CELL_BIOLOGY_REVIEW_HANDOFF.md").read_text(
        encoding="utf-8"
    )
    embedded_handoff = (
        ROOT / "content/courses/cell-biology/independent-review-handoff.md"
    ).read_text(encoding="utf-8")
    review_register = (
        ROOT / "docs/reviews/cell-biology-assessment-review-register-0.35.0.md"
    ).read_text(encoding="utf-8")
    workload_protocol = (
        ROOT / "docs/reviews/cell-biology-workload-pilot-0.62.0.md"
    ).read_text(encoding="utf-8")
    historical_061_workload_protocol = (
        ROOT / "docs/reviews/cell-biology-workload-pilot-0.61.0.md"
    ).read_text(encoding="utf-8")
    historical_060_workload_protocol = (
        ROOT / "docs/reviews/cell-biology-workload-pilot-0.60.0.md"
    ).read_text(encoding="utf-8")
    historical_workload_protocol = (
        ROOT / "docs/reviews/cell-biology-workload-pilot-0.56.0.md"
    ).read_text(encoding="utf-8")
    historical_057_workload_protocol = (
        ROOT / "docs/reviews/cell-biology-workload-pilot-0.57.0.md"
    ).read_text(encoding="utf-8")
    historical_snapshot = (
        ROOT / "docs/CELL_BIOLOGY_REVIEW_SNAPSHOT-0.56.0.md"
    ).read_text(encoding="utf-8")
    workload_log = ROOT / "docs/reviews/cell-biology-workload-log-template-0.62.0.csv"
    manifest = json.loads(
        (ROOT / "content/courses/cell-biology/course.json").read_text(
            encoding="utf-8"
        )
    )

    assert actual["course_id"] == "cell-biology"
    assert actual["content_version"] == "0.62.0"
    assert "targets Cell Biology package version 0.62.0" in handoff
    assert "Foundations of Cell and Molecular Biology 0.62.0" in embedded_handoff
    assert "45 lesson records, 69 lesson objectives, 183 public formative questions" in embedded_handoff
    assert "142 candidate-gate instances and four course-level gates" in embedded_handoff
    assert re.search(
        r"Public package archive SHA-256:\*\*\s*`([0-9a-f]{64})`", snapshot
    ).group(1) == actual["package_sha256"]
    assert re.search(
        r"Manifest SHA-256:\*\*\s*`([0-9a-f]{64})`", snapshot
    ).group(1) == actual["manifest_sha256"]
    assert "[review snapshot](CELL_BIOLOGY_REVIEW_SNAPSHOT.md)" in handoff
    assert "15 artifacts for 14 intended components" in handoff
    assert (
        "[machine-readable review-evidence index]"
        "(reviews/cell-biology-review-evidence.json)"
    ) in handoff
    assert "142 unresolved candidate-gate instances" in handoff
    assert "four unresolved course-level gates" in handoff
    assert "[numeric-key report](reviews/cell-biology-public-numeric-recalculation.json)" in handoff
    assert "[table reconciliation](reviews/cell-biology-public-table-recalculation.json)" in handoff
    assert "No reviewer sign-off or release decision" in handoff
    assert "Current register state: **no reviewers assigned; no sign-offs" in review_register
    assert "[0.62.0 workload-pilot protocol]" in handoff
    assert "homework and lab packet headers and syllabus week-5 and week-11 descriptions label the 2–3 hour values as unvalidated author estimates" in handoff
    assert "[blank log template]" in handoff
    assert "No participant recruitment, approved weekly time targets, learner logs, or workload results" in handoff

    # 0.62.0 repins the prospective protocol to the current digest; the 0.61.0 protocol stays historical.
    assert actual["package_sha256"] in workload_protocol
    assert actual["manifest_sha256"] in workload_protocol
    assert "Public package pin:** archive SHA-256" in workload_protocol
    assert "pinned to the 0.62.0 package digest" in handoff
    assert "version 0.62.0" in workload_protocol
    assert "version 0.61.0" in historical_061_workload_protocol
    assert actual["package_sha256"] not in historical_061_workload_protocol
    assert "No learners have been recruited" in workload_protocol
    assert "deliberately blank" in workload_protocol
    assert "not a midterm" in workload_protocol
    assert "cell-biology-workload-log-template-0.62.0.csv" in workload_protocol
    assert "version 0.60.0" in historical_060_workload_protocol
    assert "version 0.57.0" in historical_057_workload_protocol
    assert "a731447f4eb6d6bf596199480007484d152522b6ff4915654a8fdd501e1ad79e" in historical_057_workload_protocol
    assert "`cell-biology` 0.56.0" in historical_snapshot
    assert "6e07c8c49282fabfdbc3761e8eec4a0afbddf52b939b02133ec1e151deb4a5eb" in historical_snapshot
    assert "87255c6be323bf955096261532b35476f0206802b14186c7a99f7f24c80e70cd" in historical_snapshot
    assert "CELL_BIOLOGY_REVIEW_SNAPSHOT-0.56.0.md" in historical_workload_protocol

    duration_weeks = manifest["duration"]["weeks"]
    target_table = workload_protocol.split(
        "| Week | Proposed focus |", maxsplit=1
    )[1].split("\n\n", maxsplit=1)[0]
    inventory_table = workload_protocol.split(
        "| Week | Available lesson IDs (not assignments) |", maxsplit=1
    )[1].split("\n\n", maxsplit=1)[0]
    for week in duration_weeks:
        # The repinned protocol lists the current week titles and every available activity ID.
        assert f"| {week['week']} | {week['title']} |" in target_table
        lesson_ids = ", ".join(f"`{value}`" for value in week["lesson_ids"])
        assessment_ids = ", ".join(
            f"`{value}`" for value in week["assessment_ids"]
        )
        inventory_row = (
            f"| {week['week']} | {lesson_ids} | {assessment_ids} |"
        )
        assert inventory_row in inventory_table

    with workload_log.open(encoding="utf-8", newline="") as log_file:
        log_rows = list(csv.reader(log_file))
    assert len(log_rows) == 1
    assert len(log_rows[0]) == 13
    assert log_rows[0][0] == "participant_code"
