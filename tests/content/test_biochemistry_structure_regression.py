"""Independent equation checks for the biochemistry structure primer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def test_binding_occupancy_and_property_distinctions():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert tuple(int(part) for part in manifest["version"].split(".")) >= (0, 4, 0)
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biochemistry-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("primary structure", "quaternary structure", "specificity", "cooperativity"):
        assert concept.lower() in text.lower()

    kd_um = 4
    free_ligand_um = 12
    occupancy = free_ligand_um / (kd_um + free_ligand_um)
    assert occupancy == pytest.approx(0.75)
    assert kd_um / (kd_um + kd_um) == pytest.approx(0.5)

    x_occupancy_at_5_um = 5 / (1 + 5)
    y_occupancy_at_5_um = 5**3 / (10**3 + 5**3)
    assert x_occupancy_at_5_um == pytest.approx(0.8333333333)
    assert y_occupancy_at_5_um == pytest.approx(0.1111111111)
    assert x_occupancy_at_5_um > y_occupancy_at_5_um

    apo_closed = 0.30
    ligand_condition_closed = 0.90
    closed_open_odds_shift = (ligand_condition_closed / (1 - ligand_condition_closed)) / (
        apo_closed / (1 - apo_closed)
    )
    assert closed_open_odds_shift == pytest.approx(21)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["biochemistry-1:check"]["solution_spec"]["answer"] == pytest.approx(0.75)
    assert items["biochemistry-1:affinity-specificity-cooperativity"]["solution_spec"]["answer"] == 0


def test_structure_ensemble_primary_references_are_link_only_and_mapped():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    module = next(item for item in manifest["modules"] if item["id"] == "biochemistry-module-1")
    expected_sources = {"biochem-koshland-induced-fit-1958", "biochem-gbp-unione-2016"}
    assert expected_sources <= set(module["source_ids"])

    source_map = json.loads((COURSE / "source-map.json").read_text(encoding="utf-8"))
    mapped = next(item for item in source_map["modules"] if item["module_id"] == module["id"])
    assert expected_sources <= set(mapped["source_ids"])

    registry = json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))
    records = {item["id"]: item for item in registry["sources"]}
    for source_id in expected_sources:
        record = records[source_id]
        assert record["reuse_mode"] == "link-only-reference"
        assert record["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }

    text = (COURSE / "modules/01-protein-structure-and-molecular-recognition.md").read_text(
        encoding="utf-8"
    )
    assert "about 68% and 32%" in text
    assert "factor of $21$" in text

