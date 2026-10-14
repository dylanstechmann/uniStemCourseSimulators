"""Check the kinetics lab's displayed means and reciprocal fits against its CSV."""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def _table_means(text: str, heading: str, next_heading: str) -> dict[float, float]:
    section = text.split(heading, maxsplit=1)[1].split(next_heading, maxsplit=1)[0]
    means = {}
    for line in section.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        try:
            means[float(cells[0])] = float(cells[-1])
        except (ValueError, IndexError):
            continue
    return means


def _lineweaver_burk_fit(points: list[tuple[float, float]]) -> tuple[float, float]:
    reciprocal_substrate = [1 / substrate for substrate, _ in points]
    reciprocal_rate = [1 / rate for _, rate in points]
    mean_x = mean(reciprocal_substrate)
    mean_y = mean(reciprocal_rate)
    slope = sum(
        (x - mean_x) * (y - mean_y)
        for x, y in zip(reciprocal_substrate, reciprocal_rate, strict=True)
    ) / sum((x - mean_x) ** 2 for x in reciprocal_substrate)
    intercept = mean_y - slope * mean_x
    return intercept, slope


def test_kinetics_lab_means_and_worked_fit_match_the_linked_csv():
    manifest = json.loads(
        (COURSE / "course.json").read_text(encoding="utf-8")
    )
    lab_path = COURSE / "labs/01-enzyme-kinetics-and-inhibition-from-data.md"
    lab = lab_path.read_text(encoding="utf-8")
    # The label is frozen inside the 0.4.85 assessment candidates' prerequisite digests; it names an
    # earlier released version (0.4.84) and needs a deliberate candidate re-binding to correct.
    label = re.search(r"Metabolism, version (\d+\.\d+\.\d+)\.", lab).group(1)
    assert label in {entry["version"] for entry in manifest["history"]}

    groups: dict[tuple[str, float], list[float]] = defaultdict(list)
    with (COURSE / "labs/enzyme-kinetics-rates.csv").open(
        newline="", encoding="utf-8"
    ) as dataset:
        for row in csv.DictReader(dataset):
            groups[(row["condition"], float(row["substrate_um"]))].append(
                float(row["rate_um_per_min"])
            )

    points_by_condition = {}
    for condition, heading, next_heading in (
        ("control", "**Control**", "**Inhibitor**"),
        ("inhibitor", "**Inhibitor**", "## Work sequence"),
    ):
        points = sorted(
            (
                substrate,
                mean(groups[(condition, substrate)]),
            )
            for group_condition, substrate in groups
            if group_condition == condition
        )
        displayed = _table_means(lab, heading, next_heading)
        assert len(points) == 6
        assert all(len(groups[(condition, substrate)]) == 3 for substrate, _ in points)
        assert displayed == {
            substrate: pytest.approx(round(rate, 2)) for substrate, rate in points
        }
        points_by_condition[condition] = points

    control_intercept, control_slope = _lineweaver_burk_fit(
        points_by_condition["control"]
    )
    inhibitor_intercept, inhibitor_slope = _lineweaver_burk_fit(
        points_by_condition["inhibitor"]
    )
    control_vmax = 1 / control_intercept
    control_km = control_slope / control_intercept
    inhibitor_vmax = 1 / inhibitor_intercept
    inhibitor_km = inhibitor_slope / inhibitor_intercept
    alpha = inhibitor_km / control_km
    inhibition_constant = 4 / (alpha - 1)

    assert control_intercept == pytest.approx(0.01000, abs=3e-6)
    assert control_slope == pytest.approx(0.0500, abs=3e-5)
    assert control_vmax == pytest.approx(100.0, abs=0.1)
    assert control_km == pytest.approx(5.00, abs=0.01)
    assert inhibitor_vmax == pytest.approx(control_vmax, abs=0.1)
    assert inhibitor_km == pytest.approx(15.0, abs=0.01)
    assert alpha == pytest.approx(3.0, abs=0.01)
    assert inhibition_constant == pytest.approx(2.0, abs=0.01)
    assert "K_I = 4/(3.00 − 1) = 2.00 μM" in lab
