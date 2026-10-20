"""Recompute the Cellular Biomechanics 0.4.0 viscoelastic-project route from its public files."""

from __future__ import annotations

import cmath
import csv
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cellular-biomechanics"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/viscoelastic-material-selection-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["cellular-biomechanics-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def candidates(path: Path) -> dict[str, tuple[float, float, float]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["candidate"]: (float(row["equilibrium_modulus_kpa"]), float(row["relaxing_modulus_kpa"]),
                                   float(row["relaxation_time_s"])) for row in csv.DictReader(handle)}


def complex_modulus(model, omega):
    """E*(ω) = E_inf + E_1·iωτ/(1 + iωτ), a complex-arithmetic route separate from the real formulas used for the keys."""
    e_inf, e_1, tau = model
    value = e_inf + e_1 * (1j * omega * tau) / (1 + 1j * omega * tau)
    return value.real, value.imag


def stress(model, strain, t):
    e_inf, e_1, tau = model
    return strain * (e_inf + e_1 * cmath.exp(-t / tau).real)


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.4.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["cellular-biomechanics-project-rehearsal-practice"]
    project = ASSESSMENTS["cellular-biomechanics-viscoelastic-project"]
    assert LESSON["id"] in WEEKS[13]["lesson_ids"] and rehearsal["id"] in WEEKS[13]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 13)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[14]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "cellular-biomechanics:case"
    milestones = [case for case in cases if case["id"].startswith("cellular-biomechanics:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Viscoelastic project rehearsal" in GUIDE
    assert rehearsal["title"].startswith("Viscoelastic project rehearsal")


def test_rehearsal_keys_recompute_independently():
    data = candidates(COURSE / "assignments/viscoelastic-rehearsal-candidates.csv")
    p, q = data["P"], data["Q"]
    relaxation = "cellular-biomechanics-project:rehearsal-relaxation"
    assert round(stress(p, 0.040, 2.0), 3) == key(relaxation, "p_stress_2s")
    assert round(stress(p, 0.040, 1e6), 4) == key(relaxation, "p_stress_eq")
    assert round(stress(q, 0.040, 2.0), 3) == key(relaxation, "q_stress_2s")
    assert "ten of Q's relaxation times" in option(relaxation, "q_relaxed")
    moduli = "cellular-biomechanics-project:rehearsal-moduli"
    for name, model in (("p", p), ("q", q)):
        assert round(complex_modulus(model, 0.05)[0], 2) == key(moduli, f"{name}_storage_low")
        assert round(complex_modulus(model, 2.0)[0], 2) == key(moduli, f"{name}_storage_high")
    storage, loss = complex_modulus(q, 2.0)
    assert round(loss / storage, 3) == key(moduli, "q_tan_high")
    # The storage-modulus ranking reverses between the two frequencies.
    assert complex_modulus(q, 0.05)[0] > complex_modulus(p, 0.05)[0] and complex_modulus(p, 2.0)[0] > storage
    # P passes every rehearsal threshold; Q fails only the storage modulus.
    p_storage, p_loss = complex_modulus(p, 2.0)
    assert stress(p, 0.040, 1e6) <= 0.15 and p_storage >= 6.0 and p_loss / p_storage <= 0.35
    assert stress(q, 0.040, 1e6) <= 0.15 and storage < 6.0 and loss / storage <= 0.35
    decision = "cellular-biomechanics-project:rehearsal-decision"
    assert option(decision, "p_outcome") == "P passes all three thresholds."
    assert option(decision, "q_binding").startswith("Only the storage modulus")
    energy = "cellular-biomechanics-project:rehearsal-energy"
    for name, model in (("p", p), ("q", q)):
        assert round(math.pi * complex_modulus(model, 2.0)[1] * 1000 * 0.020 ** 2, 2) == key(energy, f"{name}_energy")
    assert "1000 J/m³" in option(energy, "conversion")


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/viscoelastic-material-selection-project-draft.md").read_text(encoding="utf-8")
    for text in ("`0.25 kPa`", "`0.050`", "`8.0 kPa`", "`0.15`", "`epsilon_0=0.030`"):
        assert text in draft
    for text in ("0.25 kPa", "held strain of 0.050", "8.0 kPa at ω = 1 rad/s", "no greater than 0.15", "ε₀ = 0.030"):
        assert text in GUIDE
    x = (0.5, 5.0, 2.0)
    assert round(stress(x, 0.040, 2.0), 4) == 0.0936
    storage_low, loss_low = complex_modulus(x, 0.05)
    storage_high, loss_high = complex_modulus(x, 2.0)
    assert (round(storage_low, 4), round(loss_low, 4)) == (0.5495, 0.4950)
    assert (round(storage_high, 3), round(loss_high, 3), round(loss_high / storage_high, 3)) == (5.206, 1.176, 0.226)
    assert round(math.pi * loss_high * 1000 * 0.020 ** 2, 3) == 1.478
    for text in ("≈ 0.0936 kPa", "E′ ≈ 0.5495 kPa", "≈ 5.206 kPa", "≈ 1.176 kPa", "about 0.226", "≈ 1.478 J/m³"):
        assert text in GUIDE
    assert "5.206" in LESSON["worked_example"] and "0.226" in LESSON["worked_example"]


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + LESSON["worked_example"] + json.dumps(
        [ITEMS[item] for item in REHEARSAL_IDS] + [card for card in CARDS if card["lesson_id"] == LESSON["id"]],
        ensure_ascii=False)
    values = set()
    for model in candidates(COURSE / "assessment-specs/viscoelastic-material-candidates.csv").values():
        values |= {stress(model, 0.050, 5.0)}
        for omega in (0.010, 1.00):
            storage, loss = complex_modulus(model, omega)
            values |= {storage, loss, loss / storage}
        values.add(math.pi * complex_modulus(model, 1.00)[1] * 1000 * 0.030 ** 2)
    for value in values:
        # Values below 0.01 (such as B's low-frequency loss tangent) are compared at full precision only, so a
        # three-decimal rounding like 0.001 does not match an unrelated conversion factor in a distractor.
        formats = {f"{value:.6f}"} if abs(value) < 0.01 else {f"{value:.3f}", f"{value:.4f}", f"{value:.6f}"}
        # A rounded result can coincide with a project input the guide must restate, such as C's
        # low-frequency loss modulus 0.049995 rounding to the 0.050 step strain.
        for text in formats - {"0.050", "0.030", "0.010", "0.250", "0.150"}:
            assert not re.search(rf"(?<![\d.]){re.escape(text)}(?!\d)", public), text
    assert "Only A meets" not in public


def test_lab_and_project_data_are_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-stiffness-ligand-density-and-the-unit-of-analysis.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](stiffness-ligand-marker-expression.csv)" in lab
    assert MANIFEST["learner_resources"] == [
        "labs/stiffness-ligand-marker-expression.csv",
        "assessment-specs/viscoelastic-material-candidates.csv",
        "assignments/viscoelastic-rehearsal-candidates.csv",
    ]
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert ("/api/v1/courses/cellular-biomechanics/resources/labs/stiffness-ligand-marker-expression.csv"
            in repository.lesson("cellular-biomechanics", "cellular-biomechanics-lab-01").markdown)
    guide = repository.lesson("cellular-biomechanics", LESSON["id"]).markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "#/course/cellular-biomechanics/lesson/cellular-biomechanics-7" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("cellular-biomechanics", path) == (COURSE / path).read_bytes()
