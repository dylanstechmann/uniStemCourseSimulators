"""Recompute the Genetics 0.6.0 three-point project route from its public files."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/genetics"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/three-point-mapping-project-guide.md").read_text(encoding="utf-8")
REHEARSAL_IDS = LESSONS["genetics-project-guide"]["question_ids"]


def read_counts(path: Path) -> dict[str, int]:
    with path.open(encoding="utf-8", newline="") as handle:
        return {row["gamete"]: int(row["count"]) for row in csv.DictReader(handle)}


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def analyse(counts: dict):
    """Infer classes, the middle locus and recombination from phase alone, without any class labels."""
    ranked = sorted(counts, key=counts.get)
    double, parental = ranked[:2], ranked[-2:]
    middles = set()
    for gamete in double:
        closest = min(parental, key=lambda haplotype: sum(a != b for a, b in zip(gamete, haplotype)))
        differing = [i for i, (a, b) in enumerate(zip(gamete, closest)) if a != b]
        assert len(differing) == 1
        middles.add(differing[0])
    (middle,) = middles
    outer = [i for i in range(3) if i != middle]
    reference = parental[0]
    total = sum(counts.values())

    def fraction(i: int, j: int) -> float:
        return sum(
            count for gamete, count in counts.items()
            if (gamete[i] == reference[i]) != (gamete[j] == reference[j])
        ) / total

    double_fraction = sum(counts[gamete] for gamete in double) / total
    return set(parental), set(double), middle, outer, total, fraction, double_fraction


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.8.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["genetics-project-rehearsal-practice"]
    project = ASSESSMENTS["genetics-three-point-project"]
    assert "genetics-project-guide" in WEEKS[6]["lesson_ids"] and rehearsal["id"] in WEEKS[6]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 6)
    assert rehearsal["question_ids"] == REHEARSAL_IDS
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[7]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "genetics:case"
    milestones = [case for case in cases if case["id"].startswith("genetics:project-m")]
    assert [case["id"].split("-")[1] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(case["mode"] == "self-assessment" for case in milestones)
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "not scheduled, assigned, submitted, collected or graded" in (
        COURSE / "assessment-specs/three-point-mapping-and-penetrance-project-draft.md"
    ).read_text(encoding="utf-8")
    assert "**Practice gradebook**: Three-point project rehearsal" in GUIDE
    assert rehearsal["title"].startswith("Three-point project rehearsal")


def test_rehearsal_keys_recompute_from_phase_alone():
    counts = read_counts(COURSE / "assignments/three-point-rehearsal-counts.csv")
    parental, double, middle, outer, total, fraction, double_fraction = analyse(counts)
    assert parental == {"EFG", "efg"} and double == {"eFG", "Efg"}
    assert all(gamete in option("genetics-project:rehearsal-order", "parental") for gamete in parental)
    assert all(gamete in option("genetics-project:rehearsal-order", "double") for gamete in double)
    letter = "EFG"[middle]
    assert f"with {letter} in the middle" in option("genetics-project:rehearsal-order", "order")
    # The listed order E, F, G is not the map order, which is the point of the rehearsal.
    assert middle != 1

    first, last = outer
    near, far = fraction(first, middle), fraction(middle, last)
    outer_fraction = fraction(first, last)
    assert round(near, 3) == key("genetics-project:rehearsal-intervals", "r_fe")
    assert round(far, 4) == key("genetics-project:rehearsal-intervals", "r_eg")
    assert round(outer_fraction, 3) == key("genetics-project:rehearsal-interference", "r_fg")
    assert near + far - outer_fraction == pytest.approx(2 * double_fraction)
    expected = near * far * total
    assert round(expected, 1) == key("genetics-project:rehearsal-interference", "expected_dco")
    coincidence = double_fraction * total / expected
    assert round(coincidence, 3) == key("genetics-project:rehearsal-interference", "coincidence")
    assert round(1 - coincidence, 3) == key("genetics-project:rehearsal-interference", "interference")
    assert "double crossovers restore the parental" in option("genetics-project:rehearsal-interference", "outer_shortfall").lower()

    penetrance = 0.60
    unaffected_carrier = 0.5 * (1 - penetrance)
    assert round(0.5 * penetrance, 3) == key("genetics-project:rehearsal-penetrance", "p_affected")
    assert round(unaffected_carrier / (unaffected_carrier + 0.5), 3) == key("genetics-project:rehearsal-penetrance", "p_het_unaffected")
    assert "penetrance 0.60" in ITEMS["genetics-project:rehearsal-penetrance"]["prompt"]


def test_guide_counts_match_the_draft_and_its_worked_example_recomputes():
    draft = read_counts(COURSE / "assessment-specs/three-point-testcross-counts.csv")
    table = dict(re.findall(r"^\| ([ABCabc]{3}) \| (\d+) \|$", GUIDE, flags=re.MULTILINE))
    assert {gamete: int(count) for gamete, count in table.items()} == draft
    assert list(table) == sorted(table), "classes are listed alphabetically, not by type"
    assert f"There are {sum(draft.values()):,} offspring in total." in GUIDE

    lesson = (COURSE / "modules/07-three-point-mapping-and-interference.md").read_text(encoding="utf-8")
    rows = re.findall(r"^\| ([+a] [+b] [+c]) \| (\d+) \|", lesson, flags=re.MULTILINE)
    counts = {tuple(cls.split()): int(count) for cls, count in rows}
    assert len(counts) == 8
    _, double, middle, outer, total, fraction, double_fraction = analyse(counts)
    assert middle == 1 and total == 1000
    near, far, across = fraction(0, 1), fraction(1, 2), fraction(0, 2)
    assert (round(near, 3), round(far, 3), round(across, 3)) == (0.114, 0.112, 0.210)
    assert "r(a–b) = (52 + 54 + 8)/1000 = 0.114" in GUIDE and "r(b–c) = (50 + 54 + 8)/1000 = 0.112" in GUIDE
    assert "r(a–c) = (106 + 104)/1000 = 0.210" in GUIDE
    expected = near * far * total
    assert round(expected, 1) == 12.8 and round(double_fraction * total / expected, 2) == 0.63
    assert "0.114 × 0.112 × 1000 = 12.8" in GUIDE and "8/12.8 = 0.63" in GUIDE
    assert round(0.5 * 0.10 / (0.5 * 0.10 + 0.5), 4) == 0.0909 and "0.05/0.55 = 0.0909" in GUIDE


def test_guide_and_rehearsal_do_not_give_the_project_answers():
    draft = read_counts(COURSE / "assessment-specs/three-point-testcross-counts.csv")
    parental, double, middle, outer, total, fraction, double_fraction = analyse(draft)
    first, last = outer
    near, far, across = fraction(first, middle), fraction(middle, last), fraction(first, last)
    expected = near * far * total
    coincidence = double_fraction * total / expected
    carrier = 0.5 * (1 - 0.80) / (0.5 * (1 - 0.80) + 0.5)
    public = GUIDE + json.dumps([ITEMS[item] for item in REHEARSAL_IDS], ensure_ascii=False)
    for value in (near, far, across, 100 * (near + far), expected, coincidence, 1 - coincidence, carrier, 0.5 * 0.80):
        reported = format(value, "#.3g")
        assert not re.search(rf"(?<![\d.]){re.escape(reported)}(?!\d)", public), reported
    order = "–".join("ABC"[i] for i in (first, middle, last))
    assert order not in public and order.replace("–", "-") not in public
    assert not any(f"{a} and {b}" in public for a in double for b in double if a != b)


def test_lab_dataset_is_package_pinned_and_links_resolve():
    lab = (COURSE / "labs/01-association-study-and-population-structure.md").read_text(encoding="utf-8")
    assert "raw.githubusercontent.com" not in lab
    assert "[synthetic genotypes (CSV)](case-control-genotypes.csv)" in lab
    assert MANIFEST["learner_resources"] == ["labs/case-control-genotypes.csv", "assignments/three-point-rehearsal-counts.csv", "assignments/genome-evidence-counts.csv"]

    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    delivered_lab = repository.lesson("genetics", "genetics-lab-01").markdown
    assert "/api/v1/courses/genetics/resources/labs/case-control-genotypes.csv" in delivered_lab
    guide = repository.lesson("genetics", "genetics-project-guide").markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "/api/v1/courses/genetics/resources/assignments/three-point-rehearsal-counts.csv" in guide
    assert "#/course/genetics/lesson/genetics-7" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("genetics", path) == (COURSE / path).read_bytes()
