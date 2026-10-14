"""The public numeric-key artifact is reproducible and excludes protected sources."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "docs/reviews/cell-biology-public-numeric-recalculation.json"
SPEC = importlib.util.spec_from_file_location(
    "cell_biology_numeric_key_evidence",
    ROOT / "tools/cell_biology_numeric_key_evidence.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_numeric_key_evidence_report_matches_every_public_numeric_practice_item():
    expected = MODULE._canonical_json(MODULE.build_evidence())
    assert REPORT.read_text(encoding="utf-8") == expected

    report = json.loads(expected)
    bank = json.loads(
        (ROOT / "content/courses/cell-biology/question-banks/practice.json").read_text(encoding="utf-8")
    )
    expected_ids = {question["id"] for question in bank["questions"] if question["type"] == "numeric"}
    results = {result["question_id"]: result for result in report["results"]}

    assert report["course_version"] == json.loads((ROOT / "content/courses/cell-biology/course.json").read_text(encoding="utf-8"))["version"]
    assert report["numeric_item_count"] == report["passed_check_count"] == 21
    assert set(results) == expected_ids
    assert all(result["passed"] for result in results.values())
    assert all(result["prompt_anchor"] for result in results.values())
    assert report["scope_limits"] == {
        "inactive_candidate_answer_sources_read": False,
        "independent_review_established": False,
        "qualified_reviewer_identity_verified": False,
        "release_authorized": False,
    }


def test_numeric_key_evidence_check_detects_stale_report(tmp_path):
    stale = tmp_path / "evidence.json"
    stale.write_text("{}\n", encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/cell_biology_numeric_key_evidence.py"),
            "--check",
            str(stale),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "missing or stale" in result.stderr
