"""The reviewer-facing table audit stays reproducible and scope-limited."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "docs/reviews/cell-biology-public-table-recalculation.json"
SPEC = importlib.util.spec_from_file_location(
    "cell_biology_public_table_evidence",
    ROOT / "tools/cell_biology_public_table_evidence.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_public_table_evidence_report_is_current_and_limited_to_formative_data():
    expected = MODULE._canonical_json(MODULE.build_evidence())
    assert REPORT.read_text(encoding="utf-8") == expected

    report = json.loads(expected)
    assert report["course_version"] == json.loads((ROOT / "content/courses/cell-biology/course.json").read_text(encoding="utf-8"))["version"]
    assert report["evidence_scope"] == "author-side-public-formative-source-reconciliation"
    assert report["question_count"] == 14
    assert report["check_count"] == report["passed_check_count"] == 133
    assert all(result["passed"] for result in report["results"])
    assert report["scope_limits"] == {
        "protected_assessment_sources_read": False,
        "independent_review_established": False,
        "qualified_reviewer_identity_verified": False,
        "release_authorized": False,
    }


def test_public_table_evidence_check_detects_drift(tmp_path):
    stale = tmp_path / "evidence.json"
    stale.write_text("{}\n", encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/cell_biology_public_table_evidence.py"),
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
