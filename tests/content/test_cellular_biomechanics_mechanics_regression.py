"""Independent mechanics checks for the cellular-biomechanics primer."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cellular-biomechanics"


def test_stress_strain_geometry_and_viscoelastic_models():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    assert manifest["version"] == manifest["history"][-1]["version"]
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "cellular-biomechanics-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "engineering stress",
        "engineering strain",
        "stiffness",
        "stress-relaxation",
        "creep",
        "Maxwell element",
        "standard linear solid",
        "observation-time window",
    ):
        assert concept.lower() in text.lower()

    force_n = 10e-6
    area_m2 = 1000e-12
    length_um = 20
    extension_um = 0.4
    stress_pa = force_n / area_m2
    strain = extension_um / length_um
    apparent_modulus_pa = stress_pa / strain
    specimen_stiffness_n_per_m = force_n / (extension_um * 1e-6)
    assert stress_pa == pytest.approx(10_000)
    assert strain == pytest.approx(0.02)
    assert apparent_modulus_pa == pytest.approx(500_000)
    assert specimen_stiffness_n_per_m == pytest.approx(25)

    maxwell_tau_s = (2_000) / 1_000
    maxwell_fraction_after_5s = math.exp(-5 / maxwell_tau_s)
    sls_equilibrium_pa = 400
    sls_transient_pa = 800 * math.exp(-5 / 2)
    assert maxwell_tau_s == pytest.approx(2)
    assert maxwell_fraction_after_5s == pytest.approx(0.082085, abs=1e-6)
    assert sls_equilibrium_pa > 0
    assert sls_equilibrium_pa + sls_transient_pa == pytest.approx(465.668, abs=0.001)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["cellular-biomechanics-1:check"]["solution_spec"]["answer"] == 0
    assert items["cellular-biomechanics-1:constitutive-regime"]["solution_spec"][
        "answer"
    ] == 1

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert "all four original compact prototype readings have expanded instruction" in syllabus


def test_adhesion_geometry_force_path_and_traction_inference():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "cellular-biomechanics-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "extracellular-matrix",
        "integrins",
        "actin",
        "nucleus",
        "ligand density",
        "displacement field",
        "inverse solution",
        "regularization",
    ):
        assert concept.lower() in text.lower()

    one_patch_area = 10 * 10
    sixteen_patch_area_each = 2.5 * 2.5
    sixteen_patch_total = 16 * sixteen_patch_area_each
    assert one_patch_area == pytest.approx(100)
    assert sixteen_patch_total == pytest.approx(one_patch_area)
    assert sixteen_patch_area_each == pytest.approx(6.25)

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["cellular-biomechanics-2:check"]["solution_spec"]["answer"] == 0
    assert items["cellular-biomechanics-2:adhesion-geometry"]["solution_spec"][
        "answer"
    ] == 0

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert "all four original compact prototype readings have expanded instruction" in syllabus


def test_factorial_design_effects_and_nested_replicates():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "cellular-biomechanics-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "2×2 factorial design",
        "experimental unit",
        "independent replication",
        "interaction",
        "randomize",
        "primary endpoint",
        "uncertainty",
    ):
        assert concept.lower() in text.lower()

    soft_low, soft_high = 10, 14
    stiff_low, stiff_high = 16, 28
    stiffness_effect = (stiff_low + stiff_high) / 2 - (soft_low + soft_high) / 2
    ligand_effect = (soft_high + stiff_high) / 2 - (soft_low + stiff_low) / 2
    stiffness_at_high_ligand = stiff_high - soft_high
    stiffness_at_low_ligand = stiff_low - soft_low
    interaction = stiffness_at_high_ligand - stiffness_at_low_ligand
    assert stiffness_effect == pytest.approx(10)
    assert ligand_effect == pytest.approx(8)
    assert interaction == pytest.approx(8)
    assert 3 * 20 == 60  # observations, with only three independently prepared gels

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["cellular-biomechanics-4:check"]["solution_spec"]["answer"] == 0
    assert items["cellular-biomechanics-4:nested-replicates"]["solution_spec"][
        "answer"
    ] == 3

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert "all four original compact prototype readings have expanded instruction" in syllabus


def test_mechanotransduction_perturbation_rescue_and_claim_boundaries():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "cellular-biomechanics-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    for concept in (
        "mechanical input",
        "candidate sensor",
        "functional outcome",
        "necessity",
        "sufficiency",
        "wild-type rescue",
        "orthogonal perturbation",
        "direct interaction evidence",
    ):
        assert concept.lower() in text.lower()

    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    items = {item["id"]: item for item in bank["questions"]}
    assert items["cellular-biomechanics-3:check"]["solution_spec"]["answer"] == 0
    assert items["cellular-biomechanics-3:perturbation-and-rescue"]["solution_spec"][
        "answer"
    ] == 2

    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8").lower()
    assert "all four original compact prototype readings have expanded instruction" in syllabus
