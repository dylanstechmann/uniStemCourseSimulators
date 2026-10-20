"""Recompute the Calculus II 0.5.0 exponential-tail project route from its public files."""

from __future__ import annotations

import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-2"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/exponential-tail-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["calculus-2-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    return h / 3 * (f(a) + f(b) + sum((4 if i % 2 else 2) * f(a + i * h) for i in range(1, n)))


def maclaurin(rate: Fraction, degree: int) -> list[Fraction]:
    """Coefficients of e^(−rate·x) built from derivatives at 0, (−rate)ⁿ/n!, rather than typed by hand."""
    return [(-rate) ** n / math.factorial(n) for n in range(degree + 1)]


def integrate_polynomial(coefficients, upper):
    return sum(Fraction(c) * Fraction(upper) ** (n + 1) / (n + 1) for n, c in enumerate(coefficients))


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["calculus-2-project-rehearsal-practice"]
    project = ASSESSMENTS["calculus-2-tail-project"]
    assert LESSON["id"] in WEEKS[13]["lesson_ids"] and rehearsal["id"] in WEEKS[13]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 13)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[14]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "calculus-2:case"
    milestones = [case for case in cases if case["id"].startswith("calculus-2:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Tail project rehearsal" in GUIDE and rehearsal["title"].startswith("Tail project rehearsal")


def test_rehearsal_keys_recompute_numerically_and_exactly():
    q = lambda x: math.exp(-x / 2)  # noqa: E731
    improper = "calculus-2-project:rehearsal-improper"
    # Numerical quadrature on a long finite interval plus a negligible remainder approximates the improper integral.
    assert round(simpson(q, 0, 80), 2) == key(improper, "total")
    assert round(simpson(q, 4, 84), 3) == key(improper, "tail_at_4")
    low, high = 0.0, 50.0
    for _ in range(80):
        middle = (low + high) / 2
        low, high = (low, middle) if simpson(q, middle, middle + 80, 400) <= 0.01 else (middle, high)
    assert round(high, 2) == key(improper, "cutoff")
    assert option(improper, "direction").startswith("Because the tail shrinks")

    coefficients = maclaurin(Fraction(1, 2), 3)
    assert coefficients == [1, Fraction(-1, 2), Fraction(1, 8), Fraction(-1, 48)]
    polynomial = integrate_polynomial(coefficients, 1)
    assert polynomial == Fraction(151, 192)
    taylor = "calculus-2-project:rehearsal-taylor"
    exact = simpson(q, 0, 1)
    assert round(float(polynomial), 4) == key(taylor, "polynomial_integral") and round(exact, 4) == key(taylor, "exact_integral")
    assert round(float(polynomial) - exact, 6) == key(taylor, "signed_error") < 0
    assert option(taylor, "sign").startswith("Because the first omitted term")

    certificate = "calculus-2-project:rehearsal-certificate"
    bound = Fraction(1, 16)  # |d⁴/dx⁴ e^(−x/2)| = e^(−x/2)/16 ≤ 1/16 on [0, 1]
    integrated = bound * integrate_polynomial([0, 0, 0, 0, Fraction(1, 24)], 1)
    assert integrated == Fraction(1, 1920)
    assert float(bound) == key(certificate, "derivative_bound") and round(float(integrated), 6) == key(certificate, "integrated_bound")
    assert abs(float(polynomial) - exact) < float(integrated)
    assert round(float(polynomial) + simpson(q, 1, 81), 4) == key(certificate, "combined")


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/exponential-tail-project-draft.md").read_text(encoding="utf-8")
    for text in ("`T=3`", "`0.01`", "`P₄(x)=1−x+x²/2−x³/6+x⁴/24`"):
        assert text in draft
    for text in ("T = 3", "at most 0.01", "P_4(x)=1-x+\\frac{x^2}{2}-\\frac{x^3}{6}+\\frac{x^4}{24}"):
        assert text in GUIDE, text
    coefficients = maclaurin(Fraction(2), 2)
    polynomial = integrate_polynomial(coefficients, Fraction(1, 2))
    exact = (1 - math.exp(-1)) / 2
    bound = Fraction(8, 6) * Fraction(1, 2) ** 4 / 4
    assert polynomial == Fraction(1, 3) and round(exact, 4) == 0.3161 and round(float(polynomial) - exact, 4) == 0.0173
    assert round(float(bound), 4) == 0.0208 and float(bound) > float(polynomial) - exact
    assert round(math.log(500) / 2, 3) == 3.107 and round(float(polynomial) + math.exp(-1) / 2, 4) == 0.5173
    for text in ("≈ 3.107", "≈ 0.3333", "≈ 0.3161", "about 0.0173", "≈ 0.0208", "≈ 0.5173"):
        assert text in GUIDE, text
    assert "3.107" in LESSON["worked_example"] and "0.0208" in LESSON["worked_example"]


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + LESSON["worked_example"] + json.dumps(
        [ITEMS[item] for item in REHEARSAL_IDS] + [card for card in CARDS if card["lesson_id"] == LESSON["id"]],
        ensure_ascii=False)
    polynomial = integrate_polynomial(maclaurin(Fraction(1), 4), 1)
    assert polynomial == Fraction(19, 30)
    values = {math.exp(-3), math.log(100), float(polynomial), 1 / 720, math.exp(-1) - 11 / 30,
              float(polynomial) + math.exp(-1)}
    for value in values:
        # Small values are compared at higher precision, so 1/720 rounding to 0.001 does not match a stated tolerance.
        formats = {f"{value:.5f}", f"{value:.7f}"} if value < 0.01 else {f"{value:.3f}", f"{value:.4f}", f"{value:.7f}"}
        for text in formats:
            assert not re.search(rf"(?<![\d.]){re.escape(text)}(?!\d)", public), text
    assert "19/30" not in public and "1/720" not in public


def test_lab_dataset_is_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-force-work-and-series.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](force-samples.csv)" in lab
    assert MANIFEST["learner_resources"] == ["labs/force-samples.csv"]
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/calculus-2/resources/labs/force-samples.csv" in repository.lesson(
        "calculus-2", "calculus-2-lab-01").markdown
    guide = repository.lesson("calculus-2", LESSON["id"]).markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "#/course/calculus-2/lesson/calculus-2-12" in guide
    assert repository.learner_resource("calculus-2", "labs/force-samples.csv") == (
        COURSE / "labs/force-samples.csv").read_bytes()
