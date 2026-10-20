"""Recompute the Physics I 0.5.0 rotor-project route from its public files."""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-mechanics"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/rotor-tradeoff-project-guide.md").read_text(encoding="utf-8")
REHEARSAL_IDS = LESSONS["physics-mechanics-project-guide"]["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def candidates(path: Path) -> dict[str, dict[str, float]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["candidate"]: {k: float(v) for k, v in row.items() if k != "candidate"} for row in csv.DictReader(handle)}


def rotor(row: dict[str, float]) -> dict[str, float]:
    """Ideal uniform-disk rotor at the target ratio; the speed comes from ω²r = target × g, solved by bisection."""
    radius, target, gravity = row["radius_m"], row["target_rcf"], row["g_m_per_s2"]
    low, high = 0.0, 10_000.0
    for _ in range(200):
        middle = (low + high) / 2
        low, high = (middle, high) if middle ** 2 * radius < target * gravity else (low, middle)
    omega = (low + high) / 2
    inertia = row["disk_mass_kg"] * radius ** 2 / 2
    return {"omega": omega, "rpm": omega * 60 / (2 * math.pi), "inertia": inertia, "energy": inertia * omega ** 2 / 2,
            "force": row["imbalance_mass_kg"] * omega ** 2 * radius}


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["physics-mechanics-project-rehearsal-practice"]
    project = ASSESSMENTS["physics-mechanics-rotor-project"]
    assert "physics-mechanics-project-guide" in WEEKS[11]["lesson_ids"] and rehearsal["id"] in WEEKS[11]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 11)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[12]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "physics-mechanics:case"
    milestones = [case for case in cases if case["id"].startswith("physics-mechanics:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(case["mode"] == "self-assessment" for case in milestones)
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Rotor project rehearsal" in GUIDE and rehearsal["title"].startswith("Rotor project rehearsal")


def test_rehearsal_keys_recompute_from_the_csv():
    data = candidates(COURSE / "assignments/rotor-rehearsal-candidates.csv")
    assert set(data) == {"P", "Q"} and {row["target_rcf"] for row in data.values()} == {400}
    p, q = rotor(data["P"]), rotor(data["Q"])
    assert round(p["omega"], 1) == key("physics-mechanics-project:rehearsal-speed", "omega_p")
    assert round(p["rpm"]) == key("physics-mechanics-project:rehearsal-speed", "rpm_p")
    halved = rotor({**data["P"], "radius_m": data["P"]["radius_m"] / 2})
    assert halved["omega"] / p["omega"] == pytest.approx(math.sqrt(2))
    assert "√2" in option("physics-mechanics-project:rehearsal-speed", "radius_scaling")
    assert round(q["inertia"], 4) == key("physics-mechanics-project:rehearsal-energy", "inertia_q")
    assert round(q["energy"], 1) == key("physics-mechanics-project:rehearsal-energy", "energy_q")
    for row, result in ((data["P"], p), (data["Q"], q)):
        assert result["energy"] == pytest.approx(row["disk_mass_kg"] * row["radius_m"] * row["target_rcf"] * row["g_m_per_s2"] / 4)
    assert round(p["force"], 3) == key("physics-mechanics-project:rehearsal-imbalance", "force_p")
    assert round(q["force"], 3) == key("physics-mechanics-project:rehearsal-imbalance", "force_q")
    assert q["energy"] > p["energy"] and option("physics-mechanics-project:rehearsal-comparison", "larger_energy") == "Candidate Q"


def test_draft_table_matches_its_csv_and_the_guide_restates_it():
    project = candidates(COURSE / "assessment-specs/fictional-rotor-candidates.csv")
    draft = (COURSE / "assessment-specs/fictional-rotor-tradeoff-project-draft.md").read_text(encoding="utf-8")
    for text in (draft, GUIDE):
        table = {
            name: (float(mass), float(radius), float(imbalance))
            for name, mass, radius, imbalance in re.findall(r"^\| ([ABC]) \| ([\d.]+) \| ([\d.]+) \| ([\d.]+) \|$", text, re.MULTILINE)
        }
        assert table == {
            name: (row["disk_mass_kg"], row["radius_m"], row["imbalance_mass_kg"]) for name, row in project.items()
        }
    # The draft's reference results follow from the CSV, including candidate C's 0.6 kg disk.
    c = rotor(project["C"])
    assert round(c["inertia"], 5) == 0.003 and round(c["energy"], 1) == 88.3

    x = rotor({"disk_mass_kg": 2.0, "radius_m": 0.050, "imbalance_mass_kg": 0.0002, "target_rcf": 1000, "g_m_per_s2": 9.81})
    assert (round(x["omega"], 1), round(x["rpm"], -1), round(x["inertia"], 4)) == (442.9, 4230, 0.0025)
    assert (round(x["energy"], 2), round(x["force"], 3)) == (245.25, 1.962)
    for text in ("ω ≈ 442.9 rad/s, about 4,230 rpm", "= 0.0025 kg·m²", "= 245.25 J", "≈ 1.962 N"):
        assert text in GUIDE


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + json.dumps([ITEMS[item] for item in REHEARSAL_IDS], ensure_ascii=False)
    for row in candidates(COURSE / "assessment-specs/fictional-rotor-candidates.csv").values():
        result = rotor(row)
        reported = {
            f"{result['omega']:.2f}", f"{result['omega']:.1f}", f"{round(result['rpm']):,}", f"{round(result['rpm'])}",
            f"{result['inertia']:.5f}", f"{result['energy']:.1f}", f"{result['force']:.3f}",
        }
        for value in sorted(reported):
            assert not re.search(rf"(?<![\d.,]){re.escape(value)}(?![\d,])", public), value


def test_lab_and_project_data_are_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-machine-compliance-and-orientation.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "[Download the synthetic CSV](compliance-reports.csv)" in lab
    assert MANIFEST["learner_resources"] == [
        "labs/compliance-reports.csv",
        "assessment-specs/fictional-rotor-candidates.csv",
        "assignments/rotor-rehearsal-candidates.csv",
    ]

    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/physics-mechanics/resources/labs/compliance-reports.csv" in repository.lesson(
        "physics-mechanics", "physics-mechanics-lab-01"
    ).markdown
    guide = repository.lesson("physics-mechanics", "physics-mechanics-project-guide").markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "/api/v1/courses/physics-mechanics/resources/assessment-specs/fictional-rotor-candidates.csv" in guide
    assert "#/course/physics-mechanics/lesson/physics-mechanics-6" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("physics-mechanics", path) == (COURSE / path).read_bytes()
