"""Recompute the Bioreactors 0.5.0 oxygen-project route from its public files."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/bioreactors"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/oxygen-capacity-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["bioreactors-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def integrate(k, our0, mu, until, steps=20000):
    """RK4 on dC/dt = k(1 − C) − OUR₀e^(μt) from C(0) = 1, independent of the closed-form deficit."""
    c, t, h = 1.0, 0.0, until / steps
    rate = lambda time, value: k * (1 - value) - our0 * math.exp(mu * time)  # noqa: E731
    for _ in range(steps):
        a = rate(t, c)
        b = rate(t + h / 2, c + h * a / 2)
        d = rate(t + h / 2, c + h * b / 2)
        e = rate(t + h, c + h * d)
        c, t = c + h * (a + 2 * b + 2 * d + e) / 6, t + h
    return c


def crossing(k, our0, mu, ccrit):
    """First time the integrated state reaches the threshold, found by bisection on the RK4 solution."""
    low, high = 0.0, 1.0
    while integrate(k, our0, mu, high, 4000) > ccrit:
        low, high = high, high * 2
    for _ in range(40):
        middle = (low + high) / 2
        low, high = (middle, high) if integrate(k, our0, mu, middle, 4000) > ccrit else (low, middle)
    return (low + high) / 2


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["bioreactors-project-rehearsal-practice"]
    project = ASSESSMENTS["bioreactors-oxygen-project"]
    assert LESSON["id"] in WEEKS[8]["lesson_ids"] and rehearsal["id"] in WEEKS[8]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 8)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[9]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "bioreactors:case"
    milestones = [case for case in cases if case["id"].startswith("bioreactors:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Oxygen project rehearsal" in GUIDE and rehearsal["title"].startswith("Oxygen project rehearsal")


def test_rehearsal_keys_recompute_from_the_ode_itself():
    k, our0, mu, ccrit = 0.5, 0.08, 0.25, 0.5
    capacity_item, crossing_item = "bioreactors-project:rehearsal-capacity", "bioreactors-project:rehearsal-crossing"
    capacity = k * (1 - ccrit)
    quasi_steady = math.log(capacity / our0) / mu
    assert key(capacity_item, "capacity") == round(capacity, 3) and key(capacity_item, "margin") == round(capacity - our0, 3)
    assert key(capacity_item, "quasi_steady_time") == round(quasi_steady, 3)
    # Demand at the quasi-steady time equals threshold capacity.
    assert math.isclose(our0 * math.exp(mu * key(capacity_item, "quasi_steady_time")), capacity, rel_tol=2e-4)
    assert round(1 - integrate(k, our0, mu, 6), 3) == key(crossing_item, "d_at_6")
    assert round(1 - integrate(k, our0, mu, 7), 3) == key(crossing_item, "d_at_7")
    assert key(crossing_item, "d_at_6") < 1 - ccrit < key(crossing_item, "d_at_7")
    assert round(crossing(k, our0, mu, ccrit), 3) == key(crossing_item, "crossing_time")
    assert round(integrate(k, our0, mu, quasi_steady), 3) == key(crossing_item, "c_at_quasi_steady") > ccrit
    assert option("bioreactors-project:rehearsal-deficit", "solution") == "D(t) = OUR₀/(k + μ) × (e^(μt) − e^(−kt))"
    assert "always positive" in option("bioreactors-project:rehearsal-deficit", "monotone")


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/oxygen-capacity-project-draft.md").read_text(encoding="utf-8")
    for text in ("`k=0.8`", "`OUR₀=0.1`", "`μ=0.2`", "`Ccrit=0.4`"):
        assert text in draft
    for text in ("k = 0.8", "OUR₀ = 0.1", "μ = 0.2", "Ccrit = 0.4", "C(0) = 1"):
        assert text in GUIDE
    k, our0, mu, ccrit = 1.0, 0.2, 0.5, 0.5
    quasi_steady = math.log(k * (1 - ccrit) / our0) / mu
    assert round(quasi_steady, 3) == 1.833 and round(crossing(k, our0, mu, ccrit), 3) == 2.680
    assert round(1 - integrate(k, our0, mu, 2), 3) == 0.344 and round(1 - integrate(k, our0, mu, 3), 3) == 0.591
    assert round(integrate(k, our0, mu, quasi_steady), 3) == 0.688
    for text in ("≈ 1.833", "≈ 2.680", "D(2) ≈ 0.344", "D(3) ≈ 0.591", "C ≈ 0.688"):
        assert text in GUIDE
    assert "1.833" in LESSON["worked_example"] and "2.680" in LESSON["worked_example"]


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + LESSON["worked_example"] + json.dumps(
        [ITEMS[item] for item in REHEARSAL_IDS] + [card for card in CARDS if card["lesson_id"] == LESSON["id"]],
        ensure_ascii=False)
    k, our0, mu, ccrit = 0.8, 0.1, 0.2, 0.4
    quasi_steady = math.log(k * (1 - ccrit) / our0) / mu
    values = {k * (1 - ccrit), k * (1 - ccrit) - our0, quasi_steady, crossing(k, our0, mu, ccrit),
              integrate(k, our0, mu, quasi_steady), 1 - integrate(k, our0, mu, 8), 1 - integrate(k, our0, mu, 9)}
    for value in values:
        for text in {f"{value:.2f}", f"{value:.3f}", f"{value:.4f}"}:
            assert not re.search(rf"(?<![\d.]){re.escape(text)}(?!\d)", public), text
    assert "0.1(e^" not in public.replace(" ", "")


def test_lab_dataset_is_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-measuring-kla-by-dynamic-gassing-out.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](gassing-out-do-curves.csv)" in lab
    assert MANIFEST["learner_resources"] == ["labs/gassing-out-do-curves.csv", "assignments/probe-response-reference.csv", "assignments/process-evidence-factorial.csv"]
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/bioreactors/resources/labs/gassing-out-do-curves.csv" in repository.lesson(
        "bioreactors", "bioreactors-lab-01").markdown
    guide = repository.lesson("bioreactors", LESSON["id"]).markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "#/course/bioreactors/lesson/bioreactors-11" in guide
    assert repository.learner_resource("bioreactors", "labs/gassing-out-do-curves.csv") == (
        COURSE / "labs/gassing-out-do-curves.csv").read_bytes()
