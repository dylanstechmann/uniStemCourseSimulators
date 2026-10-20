"""Recompute the Statics & Mechanics of Materials 0.5.0 beam-project route from its public files."""

from __future__ import annotations

import csv
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statics-materials"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/beam-strength-and-stiffness-project-guide.md").read_text(encoding="utf-8")
REHEARSAL_IDS = LESSONS["statics-materials-project-guide"]["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def candidates(path: Path) -> dict[str, dict[str, Fraction]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["candidate"]: {k: Fraction(v) for k, v in row.items() if k != "candidate"} for row in csv.DictReader(handle)}


def beam(row, span, load, deflection_limit_mm):
    """Exact rational arithmetic in N, mm and MPa (N/mm²), independent of the SI floats used to author the keys."""
    span_mm, width, depth = Fraction(span) * 1000, row["width_mm"], row["depth_mm"]
    modulus = row["elastic_modulus_gpa"] * 1000  # MPa
    moment = Fraction(load) * span_mm / 4  # N·mm
    inertia = width * depth ** 3 / 12  # mm⁴
    stress = moment * (depth / 2) / inertia  # MPa
    deflection = Fraction(load) * span_mm ** 3 / (48 * modulus * inertia)  # mm
    return {
        "moment_nm": moment / 1000, "inertia_e9": inertia / 1000, "stress": stress, "deflection": deflection,
        "strength_load": Fraction(load) * (row["yield_strength_mpa"] / 2) / stress,
        "deflection_load": Fraction(load) * Fraction(deflection_limit_mm) / deflection,
    }


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["statics-materials-project-rehearsal-practice"]
    project = ASSESSMENTS["statics-materials-beam-project"]
    assert "statics-materials-project-guide" in WEEKS[8]["lesson_ids"] and rehearsal["id"] in WEEKS[8]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 8)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[9]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "statics-materials:case"
    milestones = [case for case in cases if case["id"].startswith("statics-materials:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(case["mode"] == "self-assessment" for case in milestones)
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Beam project rehearsal" in GUIDE and rehearsal["title"].startswith("Beam project rehearsal")


def test_rehearsal_keys_recompute_with_exact_arithmetic():
    data = candidates(COURSE / "assignments/beam-rehearsal-candidates.csv")
    p, q = (beam(data[name], "0.250", 20, "0.500") for name in ("P", "Q"))
    assert float(p["moment_nm"]) == key("statics-materials-project:rehearsal-section", "moment")
    assert round(float(p["inertia_e9"]), 2) == key("statics-materials-project:rehearsal-section", "inertia_p")
    assert round(float(q["inertia_e9"]), 1) == key("statics-materials-project:rehearsal-section", "inertia_q")
    assert q["inertia_e9"] / p["inertia_e9"] == Fraction(125, 64) and "cube" in option(
        "statics-materials-project:rehearsal-section", "depth_effect")
    assert round(float(p["stress"]), 2) == key("statics-materials-project:rehearsal-checks", "stress_p")
    assert round(float(p["deflection"]), 3) == key("statics-materials-project:rehearsal-checks", "deflection_p")
    assert round(float(q["deflection"]), 3) == key("statics-materials-project:rehearsal-checks", "deflection_q")
    # P is strong enough but too flexible; Q passes both checks.
    assert p["stress"] <= data["P"]["yield_strength_mpa"] / 2 and p["deflection"] > Fraction("0.500")
    assert q["stress"] <= data["Q"]["yield_strength_mpa"] / 2 and q["deflection"] <= Fraction("0.500")
    assert "passes the strength check but fails the stiffness check" in option("statics-materials-project:rehearsal-checks", "p_outcome")
    assert round(float(p["strength_load"]), 1) == key("statics-materials-project:rehearsal-load-limits", "strength_load_p")
    assert round(float(p["deflection_load"]), 2) == key("statics-materials-project:rehearsal-load-limits", "deflection_load_p")
    assert round(float(q["deflection_load"]), 2) == key("statics-materials-project:rehearsal-load-limits", "deflection_load_q")
    assert all(result["deflection_load"] < result["strength_load"] for result in (p, q))
    raised = beam(data["Q"], "0.250", 24, "0.500")
    assert round(float(raised["deflection"]), 3) == key("statics-materials-project:rehearsal-margin", "deflection_q_raised")
    assert raised["deflection"] > Fraction("0.500")


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/beam-strength-and-stiffness-project-draft.md").read_text(encoding="utf-8")
    for text in ("L=0.300 m", "b=0.020 m", "F=30 N", "δ_max ≤ 0.600 mm"):
        assert text.replace(" ", "") in draft.replace(" ", "").replace("`", "") or text in draft
    for text in ("L = 0.300 m", "F = 30 N", "b = 0.020 m", "δ_max ≤ 0.600 mm", "σ_max ≤ S_y/2"):
        assert text in GUIDE
    x = beam({"width_mm": Fraction(10), "depth_mm": Fraction(10), "elastic_modulus_gpa": Fraction(3),
              "yield_strength_mpa": Fraction(30)}, "0.200", 10, "0.400")
    assert x["moment_nm"] == Fraction(1, 2) and round(float(x["inertia_e9"]), 4) == 0.8333
    assert x["stress"] == 3 and round(float(x["deflection"]), 3) == 0.667
    assert x["strength_load"] == 50 and round(float(x["deflection_load"]), 1) == 6.0
    for text in ("M_max = 10 × 0.200/4 = 0.500 N·m", "= 3.00 MPa", "≈ 0.667 mm", "= 50 N", "≈ 6.0 N"):
        assert text in GUIDE


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + json.dumps([ITEMS[item] for item in REHEARSAL_IDS], ensure_ascii=False)
    for row in candidates(COURSE / "assessment-specs/beam-candidate-comparison.csv").values():
        result = beam(row, "0.300", 30, "0.600")
        reported = {
            f"{float(result['stress']):.3f}", f"{float(result['deflection']):.3f}", f"{float(result['strength_load']):.1f}",
            f"{float(result['deflection_load']):.3f}", f"{float(result['deflection_load']):.2f}",
        }
        for value in sorted(reported):
            assert not re.search(rf"(?<![\d.]){re.escape(value)}(?!\d)", public), value
    assert "2.25" not in public and "0.586" not in public


def test_lab_and_project_data_are_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-fatigue-lives-scatter-and-run-outs.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](fatigue-lives-by-stress-amplitude.csv)" in lab
    assert MANIFEST["learner_resources"] == [
        "labs/fatigue-lives-by-stress-amplitude.csv",
        "assessment-specs/beam-candidate-comparison.csv",
        "assignments/beam-rehearsal-candidates.csv",
    ]

    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/statics-materials/resources/labs/fatigue-lives-by-stress-amplitude.csv" in repository.lesson(
        "statics-materials", "statics-materials-lab-01"
    ).markdown
    guide = repository.lesson("statics-materials", "statics-materials-project-guide").markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "/api/v1/courses/statics-materials/resources/assessment-specs/beam-candidate-comparison.csv" in guide
    assert "#/course/statics-materials/lesson/statics-materials-11" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("statics-materials", path) == (COURSE / path).read_bytes()
