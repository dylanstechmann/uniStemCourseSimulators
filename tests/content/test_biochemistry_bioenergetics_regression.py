"""Independent equation checks for the biochemistry bioenergetics primer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def test_carbon_redox_and_coupling_bookkeeping():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert tuple(int(part) for part in manifest["version"].split(".")) >= (0, 4, 0)
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biochemistry-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("six-carbon", "NADH", "uncoupler"):
        assert concept.lower() in text.lower()
    # The overview defers quantitative mitochondrial accounting to lesson 11.
    detail = (COURSE / "modules/11-mitochondrial-bioenergetics-and-atp-yield.md").read_text(encoding="utf-8")
    for concept in ("proton-motive force", "uncoupler", "one ATP-per-glucose number without the stoichiometry"):
        assert concept.lower() in detail.lower()

    glucose_mol = 5
    net_atp_per_glucose = 2
    direct_atp_mol = glucose_mol * net_atp_per_glucose
    cytosolic_nadh_per_glucose = 2
    assumed_atp_equiv_per_nadh = 3
    partial_accounting_per_glucose = net_atp_per_glucose + (
        cytosolic_nadh_per_glucose * assumed_atp_equiv_per_nadh
    )
    assert direct_atp_mol == pytest.approx(10)
    assert partial_accounting_per_glucose == pytest.approx(8)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["biochemistry-3:check"]["solution_spec"]["answer"] == pytest.approx(10)
    assert items["biochemistry-3:uncoupler-and-pmf"]["solution_spec"]["answer"] == 1
    assert items["biochemistry-3:pool-change"]["solution_spec"]["answer"] == 12
    assert items["biochemistry-3:pool-vs-turnover"]["solution_spec"]["answer"] == 0
    assert "Calculate net ATP-pool change" in next(
        objective["description"] for objective in manifest["lesson_objectives"]
        if objective["id"] == "biochemistry-3-objective-3"
    )

