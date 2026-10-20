"""Recompute the Calculus I 0.5.0 washout-project route from its public files with independent numerics."""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-1"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/washout-model-project-guide.md").read_text(encoding="utf-8")
REHEARSAL_IDS = LESSONS["calculus-1-project-guide"]["question_ids"]
TWO_TERMS = re.compile(r"S\(t\) = (\d+)e\^\(−([\d.]+)t\) \+ (\d+)e\^\(−([\d.]+)t\)")


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def model(text: str):
    a, alpha, b, beta = (float(value) for value in TWO_TERMS.search(text).groups())
    return lambda t: a * math.exp(-alpha * t) + b * math.exp(-beta * t)


def rows(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        return [(float(row["time_hours"]), float(row["observed_signal"]), float(row["known_blank"]))
                for row in csv.DictReader(handle)]


def derivative(f, t: float, step: float = 1e-5) -> float:
    return (f(t + step) - f(t - step)) / (2 * step)


def second_derivative(f, t: float, step: float = 1e-3) -> float:
    return (f(t + step) - 2 * f(t) + f(t - step)) / step ** 2


def fine_integral(f, low: float, high: float, panels: int = 4000) -> float:
    step = (high - low) / panels
    return step / 3 * sum(
        (1 if i in (0, panels) else 4 if i % 2 else 2) * f(low + i * step) for i in range(panels + 1)
    )


def simpson(values, step: float) -> float:
    weights = [1] + [4 if i % 2 else 2 for i in range(1, len(values) - 1)] + [1]
    return step / 3 * math.fsum(w * v for w, v in zip(weights, values))


def bisect(f, low: float, high: float) -> float:
    for _ in range(200):
        middle = (low + high) / 2
        low, high = (middle, high) if f(low) * f(middle) > 0 else (low, middle)
    return (low + high) / 2


def newton(f, start: float, steps: int):
    estimates, t = [], start
    for _ in range(steps):
        t = t - f(t) / derivative(f, t)
        estimates.append(t)
    return estimates


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["calculus-1-project-rehearsal-practice"]
    project = ASSESSMENTS["calculus-1-washout-project"]
    assert "calculus-1-project-guide" in WEEKS[12]["lesson_ids"] and rehearsal["id"] in WEEKS[12]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 12)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[14]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "calculus-1:case"
    milestones = [case for case in cases if case["id"].startswith("calculus-1:project-m")]
    assert [case["id"].split("-")[2] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(case["mode"] == "self-assessment" for case in milestones)
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Washout project rehearsal" in GUIDE
    assert rehearsal["title"].startswith("Washout project rehearsal")


def test_rehearsal_keys_recompute_with_independent_numerics():
    signal = model(ITEMS["calculus-1-project:rehearsal-derivatives"]["prompt"])
    data = rows(COURSE / "assignments/washout-rehearsal-signals.csv")
    assert all(blank == 1.5 for _, _, blank in data)
    assert all(observed == pytest.approx(signal(t) + blank, abs=5.1e-7) for t, observed, blank in data)

    assert derivative(signal, 0) == pytest.approx(key("calculus-1-project:rehearsal-derivatives", "s_prime_0"), abs=0.005)
    assert second_derivative(signal, 0) == pytest.approx(key("calculus-1-project:rehearsal-derivatives", "s_double_prime_0"), abs=0.0005)
    assert all(derivative(signal, t) < 0 < second_derivative(signal, t) for t in range(0, 21))

    target = lambda t: signal(t) - 5  # noqa: E731
    assert target(15) > 0 > target(20)
    first, second = newton(target, 15.0, 2)
    assert round(first, 2) == key("calculus-1-project:rehearsal-newton", "t1")
    assert round(second, 2) == key("calculus-1-project:rehearsal-newton", "t2")
    assert abs(second - bisect(target, 15, 20)) < 0.002

    exact = fine_integral(signal, 0, 20)
    assert round(exact, 1) == key("calculus-1-project:rehearsal-accumulation", "exact_integral")
    assert round(exact / 20, 3) == key("calculus-1-project:rehearsal-accumulation", "average")
    assert round(exact + 1.5 * 20, 1) == key("calculus-1-project:rehearsal-accumulation", "observed_integral")

    estimate = simpson([observed - blank for _, observed, blank in data], 5.0)
    assert round(estimate, 2) == key("calculus-1-project:rehearsal-simpson", "simpson")
    assert round(estimate - exact, 3) == key("calculus-1-project:rehearsal-simpson", "abs_error")
    assert -(1.6 - 1.5) * 20 == pytest.approx(key("calculus-1-project:rehearsal-blank", "integral_change"))


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/washout-model-project-draft.md").read_text(encoding="utf-8")
    assert "S(t)=18e^{-0.08t}+6e^{-0.015t}" in draft.replace(" ", "")
    project = model(GUIDE)
    data = rows(COURSE / "assessment-specs/washout-capstone-signals.csv")
    assert all(observed == pytest.approx(project(t) + 3, abs=5.1e-7) for t, observed, _ in data)

    lab_signal = lambda t: 20 * math.exp(-0.1 * t)  # noqa: E731
    assert derivative(lab_signal, 10) == pytest.approx(-0.736, abs=0.0005) and "C′(10) = −2e^(−1) ≈ −0.736" in GUIDE
    first, second = newton(lambda t: lab_signal(t) - 4, 15.0, 2)
    assert (round(first, 4), round(second, 4)) == (16.0366, 16.0942) and "16.0366" in GUIDE and "16.0942" in GUIDE
    assert round(10 * math.log(5), 4) == 16.0944 and "10 ln 5 ≈ 16.0944 h" in GUIDE
    exact = fine_integral(lab_signal, 0, 20)
    assert round(exact, 3) == 172.933 and "200(1 − e^(−2)) ≈ 172.933" in GUIDE
    estimate = simpson([lab_signal(t) for t in (0, 5, 10, 15, 20)], 5.0)
    assert round(estimate, 3) == 172.991 and round(estimate - exact, 3) == 0.058 and "≈ 172.991, about 0.058 above" in GUIDE


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    project = model(GUIDE)
    target = lambda t: project(t) - 8  # noqa: E731
    first, second = newton(target, 20.0, 2)
    exact = fine_integral(project, 0, 24)
    data = rows(COURSE / "assessment-specs/washout-capstone-signals.csv")
    estimate = simpson([observed - blank for _, observed, blank in data], 4.0)
    public = GUIDE + json.dumps([ITEMS[item] for item in REHEARSAL_IDS], ensure_ascii=False)
    reported = {
        f"{derivative(project, 0):.2f}", f"{first:.2f}", f"{second:.4f}", f"{exact:.1f}", f"{exact:.2f}",
        f"{exact / 24:.2f}", f"{exact + 72:.1f}", f"{estimate:.2f}", f"{estimate - exact:.3f}",
        f"{100 * (estimate - exact) / exact:.4f}",
    }
    for value in sorted(reported):
        for form in {value, value.replace("-", "−")}:
            assert not re.search(rf"(?<![\d.]){re.escape(form)}(?!\d)", public), form


def test_lab_and_project_data_are_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-washout-background.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "[Download the synthetic CSV](washout-signals.csv)" in lab
    assert "inactive, unscheduled and ungraded" in lab
    assert MANIFEST["learner_resources"] == [
        "labs/washout-signals.csv",
        "assessment-specs/washout-capstone-signals.csv",
        "assignments/washout-rehearsal-signals.csv",
    ]

    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/calculus-1/resources/labs/washout-signals.csv" in repository.lesson(
        "calculus-1", "calculus-1-lab-01"
    ).markdown
    guide = repository.lesson("calculus-1", "calculus-1-project-guide").markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "/api/v1/courses/calculus-1/resources/assessment-specs/washout-capstone-signals.csv" in guide
    assert "#/course/calculus-1/lesson/calculus-1-11" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("calculus-1", path) == (COURSE / path).read_bytes()
