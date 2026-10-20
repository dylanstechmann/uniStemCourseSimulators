"""Recompute the Transport 0.5.0 heat-generation slab route from its public files."""

from __future__ import annotations

import json
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/transport"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/heat-generation-slab-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["transport-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def finite_difference(L, k, q, h, t_inf, cells=200):
    """Solve k T'' + q = 0 with T'(0) = 0 and −kT'(L) = h(T(L) − T∞) by an exact rational tridiagonal sweep.

    Second-order central differences with ghost nodes reproduce a quadratic profile exactly, so this is an independent
    check on the closed form used to author the keys, not an approximation to it.
    """
    L, k, q, h, t_inf = (Fraction(value) for value in (L, k, q, h, t_inf))
    dx = L / cells
    n = cells + 1
    lower, diag, upper, rhs = [Fraction(0)] * n, [Fraction(0)] * n, [Fraction(0)] * n, [Fraction(0)] * n
    for i in range(n):
        lower[i], diag[i], upper[i], rhs[i] = Fraction(1), Fraction(-2), Fraction(1), -q * dx * dx / k
    upper[0] = Fraction(2)  # symmetry: ghost node T(−dx) = T(dx)
    # convection: ghost node T(L + dx) = T(L − dx) − 2 dx h (T(L) − T∞)/k
    lower[-1] = Fraction(2)
    diag[-1] = Fraction(-2) - 2 * dx * h / k
    rhs[-1] = -q * dx * dx / k - 2 * dx * h * t_inf / k
    for i in range(1, n):
        factor = lower[i] / diag[i - 1]
        diag[i] -= factor * upper[i - 1]
        rhs[i] -= factor * rhs[i - 1]
    temps = [Fraction(0)] * n
    temps[-1] = rhs[-1] / diag[-1]
    for i in range(n - 2, -1, -1):
        temps[i] = (rhs[i] - upper[i] * temps[i + 1]) / diag[i]
    return temps


def summary(L, k, q, h, t_inf, cells=200):
    temps = finite_difference(L, k, q, h, t_inf, cells)
    L, k, h, t_inf = (Fraction(value) for value in (L, k, h, t_inf))
    dx = L / cells
    trapezoid = sum((temps[i] + temps[i + 1]) / 2 for i in range(cells)) * dx
    # Euler–Maclaurin end correction, exact for a quadratic: subtract dx²/12 × (T′(L) − T′(0)), with T′(0) = 0 and
    # T′(L) = −h(T(L) − T∞)/k taken from the boundary condition.
    slope_at_surface = -h * (temps[-1] - t_inf) / k
    average = (trapezoid - dx * dx / 12 * slope_at_surface) / L
    nodes = [temps[i * cells // 4] for i in range(5)]
    return temps[-1], temps[0], average, nodes


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["transport-project-rehearsal-practice"]
    project = ASSESSMENTS["transport-slab-project"]
    assert LESSON["id"] in WEEKS[13]["lesson_ids"] and rehearsal["id"] in WEEKS[13]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 13)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[14]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "transport:case"
    milestones = [case for case in cases if case["id"].startswith("transport:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Slab project rehearsal" in GUIDE and rehearsal["title"].startswith("Slab project rehearsal")


def test_rehearsal_keys_recompute_from_a_finite_difference_solution():
    surface, center, average, nodes = summary("0.010", "2.0", 20000, 10, 22)
    temps = "transport-project:rehearsal-temperatures"
    assert round(float(surface), 1) == key(temps, "surface_temperature")
    assert round(float(center), 1) == key(temps, "center_temperature")
    flux = 10 * (surface - 22)  # convective flux at the face, W/m²
    assert flux == Fraction(20000) * Fraction("0.010") and float(flux) / 1000 == key(temps, "surface_flux")
    mean = "transport-project:rehearsal-average"
    simpson = (Fraction(1, 12)) * (nodes[0] + 4 * nodes[1] + 2 * nodes[2] + 4 * nodes[3] + nodes[4])
    assert round(float(average), 2) == key(mean, "exact_average") and round(float(simpson), 2) == key(mean, "simpson_average")
    assert simpson == average
    biot = "transport-project:rehearsal-biot"
    lumped = 22 + Fraction(20000) * Fraction("0.010") / 10
    assert key(biot, "biot") == 0.05 and round(float(center - lumped), 3) == key(biot, "center_error")
    assert option(biot, "screen").startswith("Lumped is adequate")
    assert option("transport-project:rehearsal-profile", "profile") == "T(x) = T∞ + q‴L/h + q‴(L² − x²)/(2k)"


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/heat-generation-slab-project-draft.md").read_text(encoding="utf-8")
    for text in ("`L=0.010 m`", "`k=0.50 W/(m·K)`", "`q'''=10,000 W/m³`", "`T∞=25 °C`", "`h=20 W/(m²·K)`"):
        assert text in draft
    for text in ("L = 0.010 m", "k = 0.50 W/(m·K)", "q‴ = 10,000 W/m³", "T∞ = 25 °C", "h = 20 W/(m²·K)"):
        assert text in GUIDE
    surface, center, average, nodes = summary("0.005", "0.25", 30000, 50, 30)
    assert (surface, center, average) == (33, Fraction(69, 2), 34)
    assert Fraction(50) * Fraction("0.005") / Fraction("0.25") == 1
    for text in ("= 33.0 °C", "= 34.5 °C", "q‴L = 150 W/m²", "= 34.0 °C", "Bi = 50 × 0.005/0.25 = 1.0", "center by 1.5 °C"):
        assert text in GUIDE, text
    assert "34.5 °C" in LESSON["worked_example"] and "Bi = 1.0" in LESSON["worked_example"]


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + LESSON["worked_example"] + json.dumps(
        [ITEMS[item] for item in REHEARSAL_IDS] + [card for card in CARDS if card["lesson_id"] == LESSON["id"]],
        ensure_ascii=False)
    surface, center, average, nodes = summary("0.010", "0.50", 10000, 20, 25)
    assert (surface, center) == (30, 31)
    for value in [average, *nodes[1:4]]:
        for text in {f"{float(value):.2f}", f"{float(value):.4f}", f"{float(value):.6f}"}:
            assert not re.search(rf"(?<![\d.]){re.escape(text)}(?!\d)", public), text
    for text in ("31 °C", "100 W/m²", "Bi = 0.4", "0.667", "31 − (x/L)²", "31-(x/L)"):
        assert text not in public, text


def test_lab_dataset_is_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-oxygen-depth-profiles-in-cell-laden-slabs.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](oxygen-depth-profiles.csv)" in lab
    assert MANIFEST["learner_resources"] == ["labs/oxygen-depth-profiles.csv"]
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/transport/resources/labs/oxygen-depth-profiles.csv" in repository.lesson(
        "transport", "transport-lab-01").markdown
    guide = repository.lesson("transport", LESSON["id"]).markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "#/course/transport/lesson/transport-11" in guide
    assert repository.learner_resource("transport", "labs/oxygen-depth-profiles.csv") == (
        COURSE / "labs/oxygen-depth-profiles.csv").read_bytes()
