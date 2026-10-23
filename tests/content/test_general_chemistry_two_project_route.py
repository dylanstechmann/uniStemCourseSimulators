"""Recompute the General Chemistry II 0.5.0 redox-project route from its public files."""

from __future__ import annotations

import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-2"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/redox-cell-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["general-chemistry-2-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]
GAS, TEMPERATURE, FARADAY = Fraction("8.314"), Fraction("298.15"), Fraction(96485)


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def cell(cathode: tuple[str, int], anode: tuple[str, int]):
    """Exact electron bookkeeping and E°cell from (E°, electrons) reductions; potentials are never scaled."""
    electrons = math.lcm(cathode[1], anode[1])
    return electrons, electrons // cathode[1], electrons // anode[1], Fraction(cathode[0]) - Fraction(anode[0])


def nernst_by_bisection(standard_potential, electrons, quotient):
    """Solve -nFE = -nFE° + RT ln Q for E by bisection rather than rearranging the Nernst equation."""
    def residual(potential):
        return -electrons * float(FARADAY) * potential - (
            -electrons * float(FARADAY) * float(standard_potential) + float(GAS * TEMPERATURE) * math.log(quotient))
    low, high = -2.0, 2.0
    for _ in range(100):
        middle = (low + high) / 2
        if residual(low) * residual(middle) <= 0:
            high = middle
        else:
            low = middle
    return (low + high) / 2


def project_results():
    electrons, _, _, potential = cell(("0.400", 3), ("-0.200", 2))
    quotient = Fraction("0.100") ** 3 / Fraction("0.0100") ** 2
    charge = Fraction("0.200") * Fraction("30.0") * 60
    extent = charge / FARADAY / electrons
    ln_k = float(electrons * FARADAY * potential / (GAS * TEMPERATURE))
    return {
        "electrons": electrons, "potential": potential, "delta_g": -electrons * FARADAY * potential, "ln_k": ln_k,
        "log_k": ln_k / math.log(10), "quotient": quotient, "nernst": nernst_by_bisection(potential, electrons, quotient),
        "charge": charge, "mol_e": charge / FARADAY, "extent": extent, "a_consumed": 3 * extent, "b_reduced": 2 * extent,
    }


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["general-chemistry-2-project-rehearsal-practice"]
    project = ASSESSMENTS["general-chemistry-2-redox-project"]
    assert "general-chemistry-2-project-guide" in WEEKS[8]["lesson_ids"] and rehearsal["id"] in WEEKS[8]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 8)
    assert rehearsal["question_ids"] == REHEARSAL_IDS and len(REHEARSAL_IDS) == 5
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[9]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "general-chemistry-2:case"
    milestones = [case for case in cases if case["id"].startswith("general-chemistry-2:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(case["mode"] == "self-assessment" for case in milestones)
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Redox project rehearsal" in GUIDE and rehearsal["title"].startswith("Redox project rehearsal")


def test_rehearsal_keys_recompute_independently():
    for text in ("C⁺ + e⁻ ⇌ C(s), E° = +0.250 V", "D²⁺ + 2e⁻ ⇌ D(s), E° = −0.150 V", "a(D²⁺) = 0.0500", "a(C⁺) = 0.0200",
                 "0.250 A for 15.0 min"):
        assert text in GUIDE
        assert any(text in ITEMS[item]["prompt"] for item in REHEARSAL_IDS), text
    electrons, c_coefficient, d_coefficient, potential = cell(("0.250", 1), ("-0.150", 2))
    assert (electrons, c_coefficient, d_coefficient, potential) == (2, 2, 1, Fraction(2, 5))
    balance = "general-chemistry-2-project:rehearsal-balance"
    assert option(balance, "net_reaction") == "D(s) + 2C⁺ → D²⁺ + 2C(s)"
    assert option(balance, "cathode").startswith("The C couple") and option(balance, "electrons").startswith("Two,")

    thermo = "general-chemistry-2-project:rehearsal-thermodynamics"
    assert key(thermo, "e_cell") == float(potential)
    delta_g_kj = -electrons * FARADAY * potential / 1000
    assert delta_g_kj == Fraction("-77.188") and key(thermo, "delta_g") == -77.2
    ln_k = float(electrons * FARADAY * potential / (GAS * TEMPERATURE))
    assert round(ln_k, 2) == key(thermo, "ln_k") == 31.14
    assert math.isclose(math.exp(-float(delta_g_kj) * 1000 / float(GAS * TEMPERATURE)), math.exp(ln_k))
    assert option(thermo, "k_meaning").startswith("Because ΔG° = −RT ln K")

    nernst = "general-chemistry-2-project:rehearsal-nernst"
    quotient = Fraction("0.0500") / Fraction("0.0200") ** 2
    assert quotient == 125 and key(nernst, "quotient") == 125
    potential_now = nernst_by_bisection(potential, electrons, quotient)
    assert round(potential_now, 3) == key(nernst, "e_nonstandard") == 0.338 and 0 < potential_now < potential
    assert option(nernst, "q_effect").startswith("It lowers E")

    charge_item = "general-chemistry-2-project:rehearsal-charge"
    charge = Fraction("0.250") * Fraction("15.0") * 60
    assert charge == 225 and key(charge_item, "charge") == 225
    assert round(float(charge / FARADAY), 5) == key(charge_item, "mol_electrons") == 0.00233
    assert round(float(charge / FARADAY / electrons), 5) == key(charge_item, "d_consumed") == 0.00117
    for field in ("e_cell", "delta_g", "ln_k"):
        assert next(s for s in ITEMS[thermo]["solution_spec"]["field_specs"] if s["id"] == field)["significant_figures"]


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/fictional-redox-cell-project-draft.md").read_text(encoding="utf-8")
    for draft_text, guide_text in (
        ("E_A^\\circ=-0.200", "E°_A = −0.200 V"), ("E_B^\\circ=+0.400", "E°_B = +0.400 V"),
        ("a(A²⁺)=0.100", "a(A²⁺) = 0.100"), ("a(B³⁺)=0.0100", "a(B³⁺) = 0.0100"),
        ("I=0.200 A` for `30.0 min", "I = 0.200 A for 30.0 min"), ("T=298.15 K", "T = 298.15 K"),
    ):
        assert draft_text in draft and guide_text in GUIDE, draft_text
    electrons, y_coefficient, x_coefficient, potential = cell(("0.350", 1), ("-0.100", 3))
    assert (electrons, y_coefficient, x_coefficient, potential) == (3, 3, 1, Fraction(9, 20))
    delta_g = -electrons * FARADAY * potential
    ln_k = float(electrons * FARADAY * potential / (GAS * TEMPERATURE))
    quotient = Fraction("0.0200") / Fraction("0.100") ** 3
    potential_now = nernst_by_bisection(potential, electrons, quotient)
    charge = Fraction("0.300") * Fraction("8.00") * 60
    extent = charge / FARADAY / electrons
    assert round(float(delta_g)) == -130255 and round(float(delta_g) / 1000, 1) == -130.3 and round(ln_k, 2) == 52.55
    assert quotient == 20 and round(potential_now, 4) == 0.4243
    assert charge == 144 and round(float(charge / FARADAY), 6) == 0.001492 and round(float(extent), 7) == 0.0004975
    for text in ("X(s) + 3Y⁺ → X³⁺ + 3Y(s), with n = 3", "= 0.450 V", "≈ −130,255 J/mol", "≈ 52.55", "= 20.0",
                 "≈ 0.4243 V", "= 144 C", "≈ 0.001492 mol e⁻", "about 0.0004975 mol X"):
        assert text in GUIDE, text
    assert "−130.3 kJ/mol" in LESSON["worked_example"] and "52.55" in LESSON["worked_example"]


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + LESSON["worked_example"] + json.dumps(
        [ITEMS[item] for item in REHEARSAL_IDS] + [card for card in CARDS if card["lesson_id"] == LESSON["id"]],
        ensure_ascii=False,
    )
    result = project_results()
    assert result["electrons"] == 6 and result["quotient"] == 10 and result["charge"] == 360
    reported = {
        f"{float(result['potential']):.3f}", f"{float(result['delta_g']):.0f}".lstrip("-"), "347,346",
        f"{float(result['delta_g']) / 1000:.1f}".lstrip("-"), f"{float(result['delta_g']) / 1000:.2f}".lstrip("-"),
        f"{result['ln_k']:.1f}", f"{result['ln_k']:.2f}", f"{result['ln_k']:.3f}",
        f"{result['log_k']:.2f}", f"{result['log_k']:.3f}", f"{result['nernst']:.3f}", f"{result['nernst']:.4f}",
        f"{result['nernst']:.6f}", f"{float(result['charge']):.0f}",
    }
    for amount in ("mol_e", "extent", "a_consumed", "b_reduced"):
        value = float(result[amount])
        reported |= {f"{value:.3g}", f"{value:.4g}", f"{value:.6g}"}
    for value in sorted(reported):
        assert not re.search(rf"(?<![\d.]){re.escape(value)}(?!\d)", public), value
    for text in ("3A(s) + 2B³⁺", "n = 6", "Q = 10", "A²⁺ + 2B(s)"):
        assert text not in public, text


def test_lab_link_is_package_pinned_and_guide_links_resolve():
    lab = (COURSE / "labs/01-reporting-background-and-relaxation.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](relaxation-reports.csv)" in lab
    assert MANIFEST["learner_resources"] == ["labs/relaxation-reports.csv", "assignments/ligand-exchange-reference.csv"]

    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/general-chemistry-2/resources/labs/relaxation-reports.csv" in repository.lesson(
        "general-chemistry-2", "general-chemistry-2-lab-01"
    ).markdown
    guide = repository.lesson("general-chemistry-2", "general-chemistry-2-project-guide").markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    for lesson_id in ("general-chemistry-2-3", "general-chemistry-2-7", "general-chemistry-2-8", "general-chemistry-2-12"):
        assert f"#/course/general-chemistry-2/lesson/{lesson_id}" in guide
    assert repository.learner_resource("general-chemistry-2", "labs/relaxation-reports.csv") == (
        COURSE / "labs/relaxation-reports.csv"
    ).read_bytes()
    # A bracketed concentration followed by a parenthesis, [M](1+K_fl), used to render as a link.
    solubility = repository.lesson("general-chemistry-2", "general-chemistry-2-14").markdown
    assert "S=[M]·(1+K_fl)" in solubility and not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", solubility)
