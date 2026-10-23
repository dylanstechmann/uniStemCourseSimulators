"""Recompute the Differential Equations 0.5.0 stiff two-compartment route from its public files."""

from __future__ import annotations

import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/differential-equations"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/stiff-two-compartment-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["differential-equations-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def euler(a, b, h, steps, implicit=False):
    """Exact rational Euler iterates for x′ = −a x, y′ = a x − b y from (1, 0)."""
    a, b, h = Fraction(a), Fraction(b), Fraction(h)
    x, y = Fraction(1), Fraction(0)
    path = []
    for _ in range(steps):
        if implicit:
            x = x / (1 + a * h)
            y = (y + a * h * x) / (1 + b * h)
        else:
            x, y = (1 - a * h) * x, a * h * x + (1 - b * h) * y
        path.append((x, y))
    return path


def rk4(a, b, until, steps=20000):
    """A fine RK4 integration of the system, independent of the closed form used to author the keys."""
    x, y, dt = 1.0, 0.0, until / steps
    rate = lambda u, v: (-a * u, a * u - b * v)  # noqa: E731
    for _ in range(steps):
        k1 = rate(x, y)
        k2 = rate(x + dt * k1[0] / 2, y + dt * k1[1] / 2)
        k3 = rate(x + dt * k2[0] / 2, y + dt * k2[1] / 2)
        k4 = rate(x + dt * k3[0], y + dt * k3[1])
        x += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        y += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
    return x, y


def peak(a, b):
    low, high = 0.0, 1.0
    slope = lambda t: a * rk4(a, b, t, 4000)[0] - b * rk4(a, b, t, 4000)[1]  # noqa: E731
    for _ in range(50):
        middle = (low + high) / 2
        low, high = (middle, high) if slope(middle) > 0 else (low, middle)
    return (low + high) / 2


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["differential-equations-project-rehearsal-practice"]
    project = ASSESSMENTS["differential-equations-stiff-project"]
    assert LESSON["id"] in WEEKS[12]["lesson_ids"] and rehearsal["id"] in WEEKS[12]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 12)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[13]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "differential-equations:case"
    milestones = [case for case in cases if case["id"].startswith("differential-equations:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Stiff project rehearsal" in GUIDE and rehearsal["title"].startswith("Stiff project rehearsal")


def test_rehearsal_keys_recompute_independently():
    peak_item, forward, implicit = ("differential-equations-project:rehearsal-peak",
                                    "differential-equations-project:rehearsal-forward",
                                    "differential-equations-project:rehearsal-implicit")
    t_star = peak(2, 50)
    assert round(t_star, 5) == key(peak_item, "peak_time")
    assert round(rk4(2, 50, t_star)[1], 5) == key(peak_item, "peak_value")
    steps = euler(2, 50, "0.03", 4)
    assert round(float(steps[1][1]), 4) == key(forward, "y_two") and round(float(steps[3][1]), 5) == key(forward, "y_four")
    assert all(y > 0 for _, y in steps) and steps[0][1] > steps[1][1] < steps[2][1] > steps[3][1]
    assert abs(1 - 50 * Fraction("0.03")) < 1 and 1 - 50 * Fraction("0.03") < 0  # stable, but the fast factor is negative
    assert round(rk4(2, 50, 0.12)[1], 5) == key(forward, "y_exact")
    assert round(float(euler(2, 50, "0.03", 4, implicit=True)[3][1]), 5) == key(implicit, "backward_y")
    assert round(float(euler(2, 50, "0.01", 12)[-1][1]), 5) == key(implicit, "fine_forward_y")
    assert option("differential-equations-project:rehearsal-exact", "solution") == "y(t) = (e^(−2t) − e^(−50t))/24"
    assert option("differential-equations-project:rehearsal-exact", "limits").startswith("It is stable for 0 < h < 0.04")


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/stiff-two-compartment-project-draft.md").read_text(encoding="utf-8")
    assert "y'=x-100y" in draft and "`h=0.025`" in draft and "`h=0.01`" in draft
    for text in ("y'=x-100y", "h = 0.025", "h = 0.01", "t = 0.1"):
        assert text in GUIDE, text
    t_star = peak(1, 20)
    assert round(t_star, 4) == 0.1577 and round(rk4(1, 20, t_star)[1], 5) == 0.04271
    x1, y1 = euler(1, 20, "0.05", 1, implicit=True)[0]
    exact = rk4(1, 20, 0.05)
    assert (round(float(x1), 4), round(float(y1), 5)) == (0.9524, 0.02381)
    assert (round(exact[0], 4), round(exact[1], 5)) == (0.9512, 0.0307) and (exact[1] - float(y1)) / exact[1] > 0.2
    for text in ("≈ 0.1577", "≈ 0.04271", "≈ 0.9524", "≈ 0.02381", "x ≈ 0.9512 and y ≈ 0.03070"):
        assert text in GUIDE, text
    assert "0.1577" in LESSON["worked_example"]


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + LESSON["worked_example"] + json.dumps(
        [ITEMS[item] for item in REHEARSAL_IDS] + [card for card in CARDS if card["lesson_id"] == LESSON["id"]],
        ensure_ascii=False)
    t_star = peak(1, 100)
    values = [t_star, rk4(1, 100, t_star)[1], *[float(v) for v in euler(1, 100, "0.025", 4)[-1]],
              *rk4(1, 100, 0.1), *[float(v) for v in euler(1, 100, "0.025", 4, implicit=True)[-1]],
              *[float(v) for v in euler(1, 100, "0.01", 10)[-1]]]
    for value in values:
        for text in {f"{abs(value):.4f}", f"{abs(value):.5f}", f"{abs(value):.6f}"}:
            assert not re.search(rf"(?<![\d.]){re.escape(text)}(?!\d)", public), text
    assert "/99" not in public and "ln(100)" not in public


def test_lab_dataset_is_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-fitting-decay-models-and-testing-them-beyond-the-window.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](cell-counts-after-growth-factor-removal.csv)" in lab
    assert MANIFEST["learner_resources"] == ["labs/cell-counts-after-growth-factor-removal.csv"]
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert ("/api/v1/courses/differential-equations/resources/labs/cell-counts-after-growth-factor-removal.csv"
            in repository.lesson("differential-equations", "differential-equations-lab-01").markdown)
    guide = repository.lesson("differential-equations", LESSON["id"]).markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "#/course/differential-equations/lesson/differential-equations-12" in guide
    path = "labs/cell-counts-after-growth-factor-removal.csv"
    assert repository.learner_resource("differential-equations", path) == (COURSE / path).read_bytes()
    assert math.isfinite(len(guide))
