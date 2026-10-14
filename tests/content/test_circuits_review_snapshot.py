"""Ensure the external Circuits review target matches its public archive."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_circuits_review_snapshot_matches_public_package():
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/course_package_digest.py"),
            "--course-id",
            "circuits",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    actual = json.loads(result.stdout)
    snapshot = (ROOT / "docs/CIRCUITS_REVIEW_SNAPSHOT.md").read_text(encoding="utf-8")

    assert actual["course_id"] == "circuits"
    assert actual["content_version"] == "0.4.8"
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
