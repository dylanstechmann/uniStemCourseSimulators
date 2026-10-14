"""Independent equation checks for the biochemistry pathway-regulation primer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def test_pool_flux_control_and_perturbation_reasoning():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "biochemistry-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("v_{in}", "v_{out}", "isotope tracing", "control is distributed"):
        assert concept.lower() in text.lower()
    # Quantitative control coefficients are developed in lesson 12.
    detail = (COURSE / "modules/12-flux-control-and-layers-of-regulation.md").read_text(encoding="utf-8")
    assert "flux control coefficient" in detail.lower() and "summation" in detail.lower()

    steady_pool_mm = 5
    initial_inflow_mm_per_min = 4
    initial_outflow_mm_per_min = 4
    perturbed_inflow_mm_per_min = 2
    perturbed_outflow_mm_per_min = 2
    assert initial_inflow_mm_per_min - initial_outflow_mm_per_min == pytest.approx(0)
    assert perturbed_inflow_mm_per_min - perturbed_outflow_mm_per_min == pytest.approx(0)
    assert steady_pool_mm == pytest.approx(5)
    assert perturbed_inflow_mm_per_min / initial_inflow_mm_per_min == pytest.approx(0.5)
    local_flux_change_percent = 0.4 * 10
    assert local_flux_change_percent == pytest.approx(4)

    product_label_fraction = (3 * 1 + 2 * 0) / (3 + 2)
    assert product_label_fraction == pytest.approx(0.6)
    assert product_label_fraction / (1 - product_label_fraction) == pytest.approx(1.5)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["biochemistry-4:check"]["solution_spec"]["answer"] == 2
    assert items["biochemistry-4:pathway-block-and-fluxes"]["solution_spec"]["answer"] == 3



def test_primary_research_links_are_registered_for_the_regulation_reading():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    module = next(item for item in manifest["modules"] if item["id"] == "biochemistry-module-4")
    expected_sources = {
        "biochem-mca-heinrich-rapoport-1974",
        "biochem-mfa-sauer-1999",
    }
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

    text = (COURSE / "modules/04-pathway-regulation-and-metabolic-integration.md").read_text(
        encoding="utf-8"
    )
    assert "doi:10.1111/j.1432-1033.1974.tb03318.x" in text
    assert "doi:10.1128/JB.181.21.6679-6688.1999" in text
