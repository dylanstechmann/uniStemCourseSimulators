"""Recompute the Linear Algebra 0.4.0 hidden-state reconstruction route from its public files."""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/linear-algebra"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/hidden-state-reconstruction-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["linear-algebra-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def readouts(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    weights = [[Fraction(row[name]) for name in row if name.startswith("weight_")] for row in rows]
    return weights, [Fraction(row["observed_readout"]) for row in rows]


def householder_least_squares(A, b):
    """Least squares by Householder QR in floating point, a route separate from the normal equations."""
    m, n = len(A), len(A[0])
    R = [[float(v) for v in row] for row in A]
    y = [float(v) for v in b]
    for k in range(n):
        column = [R[i][k] for i in range(k, m)]
        alpha = -math.copysign(math.sqrt(sum(v * v for v in column)), column[0])
        v = column[:]
        v[0] -= alpha
        norm = math.sqrt(sum(t * t for t in v))
        v = [t / norm for t in v]
        for j in range(k, n):
            dot = sum(v[i - k] * R[i][j] for i in range(k, m))
            for i in range(k, m):
                R[i][j] -= 2 * v[i - k] * dot
        dot = sum(v[i - k] * y[i] for i in range(k, m))
        for i in range(k, m):
            y[i] -= 2 * v[i - k] * dot
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(R[i][j] * x[j] for j in range(i + 1, n))) / R[i][i]
    return x


def singular_values_2x2(A):
    """Power iteration on AᵀA for the largest eigenvalue; the trace gives the other."""
    ata = [[sum(row[i] * row[j] for row in A) for j in range(2)] for i in range(2)]
    v = [1.0, 0.3]
    for _ in range(200):
        w = [ata[0][0] * v[0] + ata[0][1] * v[1], ata[1][0] * v[0] + ata[1][1] * v[1]]
        norm = math.hypot(*w)
        v = [w[0] / norm, w[1] / norm]
    largest = v[0] * (ata[0][0] * v[0] + ata[0][1] * v[1]) + v[1] * (ata[1][0] * v[0] + ata[1][1] * v[1])
    smallest = float(ata[0][0] + ata[1][1]) - largest
    return math.sqrt(largest), math.sqrt(smallest)


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["linear-algebra-project-rehearsal-practice"]
    project = ASSESSMENTS["linear-algebra-hidden-state-project"]
    assert LESSON["id"] in WEEKS[12]["lesson_ids"] and rehearsal["id"] in WEEKS[12]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 12)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[13]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "linear-algebra:case"
    milestones = [case for case in cases if case["id"].startswith("linear-algebra:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Hidden-state project rehearsal" in GUIDE
    assert rehearsal["title"].startswith("Hidden-state project rehearsal")


def test_rehearsal_keys_recompute_independently():
    A, b = readouts(COURSE / "assignments/rehearsal-readouts.csv")
    x = householder_least_squares(A, b)
    ls = "linear-algebra-project:rehearsal-least-squares"
    assert (round(x[0], 3), round(x[1], 3)) == (key(ls, "x_p"), key(ls, "x_q"))
    residual = [float(bi) - sum(float(a) * xi for a, xi in zip(row, x)) for row, bi in zip(A, b)]
    assert all(abs(sum(float(row[j]) * r for row, r in zip(A, residual))) < 1e-12 for j in range(2))
    assert round(sum(r * r for r in residual), 6) == key(ls, "residual_sq")
    assert option(ls, "orthogonal").startswith("Aᵀ(b − A x̂) = 0")
    sigma_max, sigma_min = singular_values_2x2(A)
    cond = "linear-algebra-project:rehearsal-conditioning"
    assert round(sigma_max, 3) == key(cond, "sigma_max") and round(sigma_min, 3) == key(cond, "sigma_min")
    assert round(sigma_max / sigma_min, 3) == key(cond, "condition") and abs(sigma_max / sigma_min - (1 + math.sqrt(5)) / 2) < 1e-9
    # A chain iterated many times converges to its stationary vector; the gap ratio gives the second eigenvalue.
    T = [[Fraction("0.85"), Fraction("0.30")], [Fraction("0.15"), Fraction("0.70")]]
    p = [Fraction("0.40"), Fraction("0.60")]
    history = []
    for _ in range(60):
        p = [T[0][0] * p[0] + T[0][1] * p[1], T[1][0] * p[0] + T[1][1] * p[1]]
        history.append(p)
    dynamics = "linear-algebra-project:rehearsal-dynamics"
    assert (float(history[0][0]), float(history[0][1])) == (key(dynamics, "p1_first"), key(dynamics, "p1_second"))
    stationary = Fraction(2, 3)
    assert round(float(history[-1][0]), 3) == key(dynamics, "stationary_first") and abs(history[-1][0] - stationary) < 1e-12
    ratio = (history[5][0] - stationary) / (history[4][0] - stationary)
    assert ratio == Fraction(11, 20) and float(ratio) == key(dynamics, "second_eigenvalue")
    assert all(sum(T[i][j] for i in range(2)) == 1 for j in range(2))
    assert option("linear-algebra-project:rehearsal-rank", "rank").startswith("Rank 2 and nullity 0")


def test_guide_restates_the_draft_and_its_worked_example_recomputes():
    draft = (COURSE / "assessment-specs/hidden-state-reconstruction-project-draft.md").read_text(encoding="utf-8")
    for text in ("0.8&0.1&0.1", "b=\\begin{bmatrix}0.21\\\\0.49\\\\0.30\\\\0.19\\\\0.51\\end{bmatrix}", "q_1=(1,-1,0)/\\sqrt2"):
        assert text in draft, text
    for text in ("0.8&0.1&0.1", "b=\\begin{bmatrix}0.21\\\\0.49\\\\0.30\\\\0.19\\\\0.51\\end{bmatrix}", "q₁ = (1, −1, 0)/√2"):
        assert text in GUIDE, text
    A = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)], [Fraction(1), Fraction(-1)]]
    b = [Fraction("0.5"), Fraction("0.3"), Fraction("0.25")]
    x = householder_least_squares(A, b)
    assert (round(x[0], 4), round(x[1], 4)) == (0.5167, 0.2833)
    sigma_max, sigma_min = singular_values_2x2(A)
    assert round(sigma_max / sigma_min, 3) == 1.732
    for text in ("x̂ = ((2 × 0.75 + 0.05)/3, (0.75 + 2 × 0.05)/3) ≈ (0.5167, 0.2833)", "κ₂(A) = √3 ≈ 1.732",
                 "p₁ = (0.9, 0.1)", "π = (0.8, 0.2)"):
        assert text in GUIDE, text
    assert "0.5167" in LESSON["worked_example"]


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    public = GUIDE + LESSON["worked_example"] + json.dumps(
        [ITEMS[item] for item in REHEARSAL_IDS] + [card for card in CARDS if card["lesson_id"] == LESSON["id"]],
        ensure_ascii=False)
    A, b = readouts(COURSE / "assessment-specs/state-readouts.csv")
    x = householder_least_squares(A, b)
    assert [round(v, 6) for v in x] == [0.2, 0.5, 0.3]
    for text in ("(0.20, 0.50, 0.30)", "(0.24, 0.45, 0.31)", "0.0004", "1.4142", "1/3, 1/3", "0.7 per step",
                 "multiplied by 0.7", "eigenvalues are 1, 0.7"):
        assert text not in public, text
    assert not re.search(r"(?<![\d.])0\.7(?![\d])", GUIDE)


def test_lab_and_project_data_are_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-sensor-geometry.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab and "](sensor-pairs.csv)" in lab
    assert MANIFEST["learner_resources"] == [
        "labs/sensor-pairs.csv", "assessment-specs/state-readouts.csv", "assignments/rehearsal-readouts.csv"]
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    assert "/api/v1/courses/linear-algebra/resources/labs/sensor-pairs.csv" in repository.lesson(
        "linear-algebra", "linear-algebra-lab-01").markdown
    guide = repository.lesson("linear-algebra", LESSON["id"]).markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "#/course/linear-algebra/lesson/linear-algebra-11" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("linear-algebra", path) == (COURSE / path).read_bytes()
