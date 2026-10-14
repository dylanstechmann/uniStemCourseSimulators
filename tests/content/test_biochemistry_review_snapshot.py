"""Ensure the Biochemistry review target matches its public archive."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_biochemistry_review_snapshot_matches_public_package():
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/course_package_digest.py"),
            "--course-id",
            "biochemistry",
        ],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    actual = json.loads(result.stdout)
    snapshot = (ROOT / "docs/BIOCHEMISTRY_REVIEW_SNAPSHOT.md").read_text(
        encoding="utf-8"
    )

    assert actual["course_id"] == "biochemistry"
    assert actual["content_version"] == "0.4.85"
    assert re.search(
        r"Public package archive SHA-256:\*\*\s*`([0-9a-f]{64})`", snapshot
    ).group(1) == actual["package_sha256"]
    assert re.search(r"Manifest SHA-256:\*\*\s*`([0-9a-f]{64})`", snapshot).group(
        1
    ) == actual["manifest_sha256"]
    assert re.search(
        r"Archive inventory:\*\*\s*(\d+) files, ([\d,]+) bytes", snapshot
    ).groups() == (str(actual["file_count"]), f"{actual['archive_bytes']:,}")


def test_biochemistry_kinetics_dataset_is_a_package_pinned_learner_resource():
    course_root = ROOT / "content/courses/biochemistry"
    manifest = json.loads((course_root / "course.json").read_text(encoding="utf-8"))
    lesson = (course_root / "labs/01-enzyme-kinetics-and-inhibition-from-data.md").read_text(
        encoding="utf-8"
    )

    assert manifest["learner_resources"] == ["labs/enzyme-kinetics-rates.csv"]
    assert "[synthetic initial rates (CSV)](enzyme-kinetics-rates.csv)" in lesson
    assert "raw.githubusercontent.com" not in lesson
    assert (course_root / manifest["learner_resources"][0]).is_file()
    assert all(
        json.loads(candidate.read_text(encoding="utf-8"))["content_version"]
        == manifest["version"]
        for candidate in (course_root / "assessment-specs").glob("*-candidate.json")
    )

    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    delivered = repository.lesson("biochemistry", "biochemistry-lab-01")
    assert (
        "/api/v1/courses/biochemistry/resources/labs/enzyme-kinetics-rates.csv"
        in delivered.markdown
    )
    assert repository.learner_resource(
        "biochemistry", "labs/enzyme-kinetics-rates.csv"
    ) == (course_root / "labs/enzyme-kinetics-rates.csv").read_bytes()


def test_kinetics_lab_duration_is_labeled_as_an_unvalidated_estimate():
    lesson = (
        ROOT
        / "content/courses/biochemistry/labs/01-enzyme-kinetics-and-inhibition-from-data.md"
    ).read_text(encoding="utf-8")
    assert "**Estimated learner time (unvalidated author estimate):** 2–3 hours" in lesson


def test_binding_equilibrium_worked_example_closes_mass_balance():
    import math

    lesson = (
        ROOT
        / "content/courses/biochemistry/modules/07-binding-equilibria-and-cooperativity.md"
    ).read_text(encoding="utf-8")
    receptor_total, ligand_total, kd = 20.0, 60.0, 15.0
    complex_amount = (
        receptor_total
        + ligand_total
        + kd
        - math.sqrt((receptor_total + ligand_total + kd) ** 2 - 4 * receptor_total * ligand_total)
    ) / 2
    receptor_free = receptor_total - complex_amount
    ligand_free = ligand_total - complex_amount

    assert complex_amount == 15.0
    assert receptor_free * ligand_free / complex_amount == kd
    assert complex_amount <= min(receptor_total, ligand_total)
    assert "(95 − √(95² − 4·20·60))/2 = (95 − 65)/2 = 15 nM" in lesson
    assert "a 1 nM, or 6.7%, overestimate" in lesson
