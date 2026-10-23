"""Keep the Statistics protocol project clearly separate from course grading."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statistics"
PROJECT = COURSE / "assessment-specs/confirmatory-study-protocol-project-draft.md"


def test_confirmatory_project_is_an_inactive_protocol_draft():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    project = PROJECT.read_text(encoding="utf-8")
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assessment_ids = {assessment["id"] for assessment in manifest["assessments"]}

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert "statistics-15-practice" in assessment_ids
    # The review draft stays inactive; the new open rehearsal/self-check route is separate.
    assert all(item["path"] != str(PROJECT.relative_to(COURSE)) for item in manifest["assessments"])
    active = {item["id"]: item for item in manifest["assessments"]}
    assert active["statistics-project-milestones"]["mode"] == "self-assessment"
    assert active["statistics-project-milestones"]["points"] == 0
    assert active["statistics-project-rehearsal-practice"]["mode"] == "practice"
    assert "Inactive authoring draft" in project
    assert "no points or course grade" in project
    assert "not part of the course manifest's assessment schedule" in project
    assert (COURSE / "modules/15-planning-a-confirmatory-study.md").is_file()
    assert "not scheduled, submitted or graded" in syllabus


def test_statistics_review_snapshot_matches_public_package():
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/course_package_digest.py"),
            "--course-id",
            "statistics",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    actual = json.loads(result.stdout)
    snapshot = (ROOT / "docs/STATISTICS_REVIEW_SNAPSHOT.md").read_text(encoding="utf-8")

    assert actual["course_id"] == "statistics"
    assert actual["content_version"] == "0.6.0"
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
