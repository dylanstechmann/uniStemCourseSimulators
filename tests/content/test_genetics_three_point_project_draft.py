"""Independently recompute the inactive three-point mapping project."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/genetics"
PROJECT = COURSE / "assessment-specs/three-point-mapping-and-penetrance-project-draft.md"
COUNTS = COURSE / "assessment-specs/three-point-testcross-counts.csv"


def load_classes():
    with COUNTS.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    return {row["gamete"]: int(row["count"]) for row in rows}, rows


def test_mapping_interference_and_penetrance_recompute():
    counts, rows = load_classes()
    total = sum(counts.values())
    assert total == 1000
    assert {row["class"] for row in rows} == {
        "parental",
        "single_crossover_A-B",
        "single_crossover_B-C",
        "double_crossover",
    }

    r_ab = (counts["Abc"] + counts["aBC"] + counts["AbC"] + counts["aBc"]) / total
    r_bc = (counts["ABc"] + counts["abC"] + counts["AbC"] + counts["aBc"]) / total
    r_ac = (counts["Abc"] + counts["aBC"] + counts["ABc"] + counts["abC"]) / total
    observed_dco = (counts["AbC"] + counts["aBc"]) / total
    expected_dco = r_ab * r_bc
    coincidence = observed_dco / expected_dco
    interference = 1 - coincidence

    assert math.isclose(r_ab, 0.146, abs_tol=1e-15)
    assert math.isclose(r_bc, 0.100, abs_tol=1e-15)
    assert math.isclose(r_ac, 0.230, abs_tol=1e-15)
    assert math.isclose(r_ab + r_bc - r_ac, 2 * observed_dco, abs_tol=1e-15)
    assert math.isclose(expected_dco * total, 14.6, abs_tol=1e-12)
    assert math.isclose(coincidence, 8 / 14.6, abs_tol=1e-15)
    assert math.isclose(interference, 1 - 8 / 14.6, abs_tol=1e-15)

    prior_heterozygote = 0.5
    penetrance = 0.8
    unaffected_heterozygote = prior_heterozygote * (1 - penetrance)
    unaffected_total = unaffected_heterozygote + (1 - prior_heterozygote)
    assert math.isclose(prior_heterozygote * penetrance, 0.4, abs_tol=1e-15)
    assert math.isclose(unaffected_heterozygote / unaffected_total, 1 / 6, abs_tol=1e-15)


def test_project_is_linked_inactive_and_versioned():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    project = PROJECT.read_text(encoding="utf-8")

    assert manifest["maturity"] == "partial"
    assert manifest["history"][-1]["version"] == manifest["version"]
    assert "assessment-specs/three-point-mapping-and-penetrance-project-draft.md" in syllabus
    assert "not scheduled, assigned, submitted or graded" in syllabus
    assert "not scheduled, assigned, submitted, collected or graded" in project
    assert "no evidence that marker `D` is real" in project
