"""Recompute the Calculus III 0.5.0 concentration-and-flux field route from its public files."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-3"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/integrative-field-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["calculus-3-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def field_checks(c0, a, radius, diffusivity, n=4000):
    """Numerical routes separate from the closed forms: a Cartesian midpoint sum for the total, a parameterized
    boundary sum with central-difference gradients for the outward flux, and a numerical divergence over the disk."""
    c = lambda x, y: c0 - a * (x * x + y * y)  # noqa: E731
    h = 1e-5

    def flux(x, y):
        return (-diffusivity * (c(x + h, y) - c(x - h, y)) / (2 * h),
                -diffusivity * (c(x, y + h) - c(x, y - h)) / (2 * h))

    step = 2 * radius / 600
    total = divergence_total = 0.0
    for i in range(600):
        for j in range(600):
            x, y = -radius + (i + 0.5) * step, -radius + (j + 0.5) * step
            if x * x + y * y <= radius * radius:
                total += c(x, y) * step * step
                dx = (flux(x + h, y)[0] - flux(x - h, y)[0]) / (2 * h)
                dy = (flux(x, y + h)[1] - flux(x, y - h)[1]) / (2 * h)
                divergence_total += (dx + dy) * step * step
    boundary = 0.0
    for k in range(n):
        theta = (k + 0.5) * 2 * math.pi / n
        x, y = radius * math.cos(theta), radius * math.sin(theta)
        jx, jy = flux(x, y)
        boundary += (jx * math.cos(theta) + jy * math.sin(theta)) * radius * 2 * math.pi / n
    return c(radius, 0), total, boundary, divergence_total


def test_route_is_scheduled_optional_and_ungraded():
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 6, 0)
    assert MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["calculus-3-project-rehearsal-practice"]
    project = ASSESSMENTS["calculus-3-field-project"]
    assert LESSON["id"] in WEEKS[13]["lesson_ids"] and rehearsal["id"] in WEEKS[13]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 13)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[14]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "calculus-3:case"
    milestones = [case for case in cases if case["id"].startswith("calculus-3:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Field project rehearsal" in GUIDE and rehearsal["title"].startswith("Field project rehearsal")


def test_rehearsal_keys_recompute_numerically():
    boundary_value, total, boundary, divergence_total = field_checks(9.0, 2.0, 1.5, 0.4)
    field, flux, check = ("calculus-3-project:rehearsal-field", "calculus-3-project:rehearsal-flux",
                          "calculus-3-project:rehearsal-theorem-check")
    assert round(boundary_value, 2) == key(field, "boundary_value")
    assert abs(total - key(field, "total_amount")) < 0.05
    assert option(field, "measure").startswith("dA = r dr dθ, with 0 ≤ r ≤ 1.5")
    assert abs(boundary / (2 * math.pi * 1.5) - key(flux, "normal_flux")) < 1e-4
    assert abs(boundary - key(flux, "boundary_transfer")) < 0.006 and abs(divergence_total - key(check, "divergence_integral")) < 0.05
    assert abs(divergence_total / (math.pi * 2.25) - key(flux, "divergence")) < 0.01
    assert option(flux, "normal").startswith("n = (x, y)/1.5")
    _, _, boundary_high_d, _ = field_checks(9.0, 2.0, 1.5, 0.6)
    assert abs(boundary_high_d - key(check, "transfer_high_d")) < 0.006


def test_guide_restates_the_draft_and_its_checks_recompute():
    draft = (COURSE / "assessment-specs/integrative-field-project-draft.md").read_text(encoding="utf-8")
    assert "$D=0.5\\;\\mathrm{m^2/s}$" in draft and "D=0.75" in draft and "These values are visible self-checks" in draft
    for text in ("D = 0.5 m²/s", "x² + y² ≤ 4 m²", "D to 0.75 m²/s", "12-(x^2+y^2)"):
        assert text in GUIDE, text
    boundary_value, total, boundary, divergence_total = field_checks(12.0, 1.0, 2.0, 0.5)
    assert round(boundary_value) == 8 and abs(total - 40 * math.pi) < 0.1
    assert abs(boundary - 8 * math.pi) < 0.01 and abs(divergence_total - 8 * math.pi) < 0.1
    assert abs(field_checks(12.0, 1.0, 2.0, 0.75)[2] - 12 * math.pi) < 0.01
    for text in ("polar total is 40π amount", "equal 8π amount/s", "the transfer is 12π amount/s", "boundary value 8 amount/m²"):
        assert text in GUIDE, text
    boundary_value, total, boundary, divergence_total = field_checks(5.0, 1.0, 1.0, 1.0)
    assert boundary_value == 4 and abs(total - 4.5 * math.pi) < 0.02 and abs(boundary - 4 * math.pi) < 0.01
    for text in ("4.5π ≈ 14.14 amount", "4π ≈ 12.57 amount/s"):
        assert text in GUIDE
    assert "14.14" in LESSON["worked_example"]


def test_cross_course_link_and_lab_dataset_resolve_in_the_application():
    lab = (COURSE / "labs/01-boundary-flux-and-balance.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](boundary-flux.csv)" in lab
    assert MANIFEST["learner_resources"] == ["labs/boundary-flux.csv"]
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/calculus-3/resources/labs/boundary-flux.csv" in repository.lesson(
        "calculus-3", "calculus-3-lab-01").markdown
    assert "#/course/linear-algebra/lesson/linear-algebra-2" in repository.lesson("calculus-3", "calculus-3-13").markdown
    guide = repository.lesson("calculus-3", LESSON["id"]).markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "#/course/calculus-3/lesson/calculus-3-12" in guide
    assert repository.learner_resource("calculus-3", "labs/boundary-flux.csv") == (COURSE / "labs/boundary-flux.csv").read_bytes()
