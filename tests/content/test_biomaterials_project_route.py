"""Recompute the Biomaterials 0.4.0 scaffold-project route from its public files."""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biomaterials"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/scaffold-property-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["biomaterials-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def candidates(path: Path) -> dict[str, dict[str, float]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["candidate"]: {k: float(v) for k, v in row.items() if k != "candidate"} for row in csv.DictReader(handle)}


def modulus(row, day):
    """Count elapsed half-times instead of evaluating the closed form used to author the keys."""
    value, remaining = row["initial_modulus_mpa"], day
    while remaining >= row["modulus_half_time_days"]:
        value, remaining = value / 2, remaining - row["modulus_half_time_days"]
    return value * 2 ** (-remaining / row["modulus_half_time_days"])


def support_time(row, threshold):
    low, high = 0.0, 1000.0
    for _ in range(200):
        middle = (low + high) / 2
        low, high = (middle, high) if modulus(row, middle) > threshold else (low, middle)
    return (low + high) / 2


def passes(row, day, porosity, permeability, initial, threshold):
    return (row["porosity_fraction"] >= porosity and row["permeability_scale_1e-12_m2"] >= permeability
            and row["initial_modulus_mpa"] >= initial and modulus(row, day) >= threshold - 1e-12)


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["biomaterials-project-rehearsal-practice"]
    project = ASSESSMENTS["biomaterials-scaffold-project"]
    assert LESSON["id"] in WEEKS[12]["lesson_ids"] and rehearsal["id"] in WEEKS[12]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 12)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[13]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "biomaterials:case"
    milestones = [case for case in cases if case["id"].startswith("biomaterials:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Scaffold project rehearsal" in GUIDE and rehearsal["title"].startswith("Scaffold project rehearsal")


def test_rehearsal_keys_recompute_independently():
    data = candidates(COURSE / "assignments/scaffold-rehearsal-candidates.csv")
    p, q = data["P"], data["Q"]
    item = "biomaterials-project:rehearsal-modulus"
    assert round(modulus(p, 30), 2) == key(item, "p_day30") and round(modulus(p, 45), 3) == key(item, "p_day45")
    assert round(modulus(q, 30), 2) == key(item, "q_day30")
    assert "halves" in option(item, "half_time")
    item = "biomaterials-project:rehearsal-support-time"
    assert round(support_time(p, 1.0), 1) == key(item, "p_time") and round(support_time(q, 1.0), 1) == key(item, "q_time")
    assert option(item, "formula") == "t = t½ × log₂(E₀ / threshold)"
    criteria = (0.70, 5, 2.0, 1.0)
    assert passes(p, 30, *criteria) and not passes(p, 45, *criteria)
    assert not passes(q, 30, *criteria) and modulus(q, 45) > 1.0 and q["porosity_fraction"] < 0.70
    item = "biomaterials-project:rehearsal-constraints"
    assert option(item, "p_day30").startswith("P passes all four") and option(item, "q_day30").startswith("Q fails on porosity")
    assert option(item, "day45").startswith("Neither")


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/scaffold-property-project-draft.md").read_text(encoding="utf-8")
    for text in ("φ ≥ 0.65", "E₀ ≥ 1.5 MPa", "E(t) ≥ 0.8 MPa", "E(42)", "E(56)"):
        assert text in GUIDE
    for text in ("`φ ≥ 0.65`", "`E₀ ≥ 1.5 MPa`", "`E(t) ≥ 0.8 MPa`"):
        assert text in draft
    x = {"initial_modulus_mpa": 3.0, "modulus_half_time_days": 20.0}
    assert round(modulus(x, 10), 3) == 2.121 and round(support_time(x, 1.2), 2) == 26.44
    for text in ("≈ 2.121 MPa", "≈ 26.44 days"):
        assert text in GUIDE and text.split()[-2] in LESSON["worked_example"]


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + LESSON["worked_example"] + json.dumps(
        [ITEMS[item] for item in REHEARSAL_IDS] + [card for card in CARDS if card["lesson_id"] == LESSON["id"]],
        ensure_ascii=False)
    for row in candidates(COURSE / "assessment-specs/scaffold-property-comparison.csv").values():
        for value in (modulus(row, 42), modulus(row, 56)):
            for text in (f"{value:.3f}", f"{value:.2f}"):
                assert not re.search(rf"(?<![\d.]){re.escape(text)}(?!\d)", public), text
        time = support_time(row, 0.8)
        for text in (f"{time:.1f}", f"{time:.2f}", f"{time:.3f}"):
            assert not re.search(rf"(?<![\d.]){re.escape(text)}(?!\d)", public), text


def test_lab_and_project_data_are_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-degradation-time-course-of-a-synthetic-scaffold.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](scaffold-degradation-time-course.csv)" in lab
    assert MANIFEST["learner_resources"] == [
        "labs/scaffold-degradation-time-course.csv",
        "assessment-specs/scaffold-property-comparison.csv",
        "assignments/scaffold-rehearsal-candidates.csv",
    ]
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/biomaterials/resources/labs/scaffold-degradation-time-course.csv" in repository.lesson(
        "biomaterials", "biomaterials-lab-01").markdown
    guide = repository.lesson("biomaterials", LESSON["id"]).markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "#/course/biomaterials/lesson/biomaterials-lab-01" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("biomaterials", path) == (COURSE / path).read_bytes()
    assert math.isclose(support_time({"initial_modulus_mpa": 1.6, "modulus_half_time_days": 1.0}, 0.8), 1.0, abs_tol=1e-9)
