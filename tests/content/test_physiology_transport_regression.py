"""Independent equation checks for the physiology transport primer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physiology"


def test_flow_network_and_exchange_relations():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "physiology-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in ("Poiseuille", "Fick's diffusion relation", "ventilation", "perfusion-limited"):
        assert concept.lower() in text.lower()

    radius_ratio = 2
    flow_ratio = radius_ratio**4
    resistance_ratio = 1 / flow_ratio
    assert flow_ratio == pytest.approx(16)
    assert resistance_ratio == pytest.approx(1 / 16)
    assert 0.50 * flow_ratio == pytest.approx(8.0)

    parallel_resistance = 1 / (1 / 8 + 1 / 8)
    branch_flow = 12 / 8
    assert parallel_resistance == pytest.approx(4)
    assert branch_flow * 2 == pytest.approx(12 / parallel_resistance)

    transfer_index = 0.4 * 50 * 4 / 20
    assert transfer_index == pytest.approx(4)
    assert 0.4 * 100 * 4 / 20 == pytest.approx(8)
    assert 0.4 * 50 * 4 / 40 == pytest.approx(2)
    assert 0.8 / 1.0 == pytest.approx(0.8)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["physiology-3:check"]["solution_spec"]["answer"] == 3
    assert items["physiology-3:perfusion-limited-gas"]["solution_spec"]["answer"] == 3

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "weeks 1, 3, 5 and 11 now have expanded" in syllabus
