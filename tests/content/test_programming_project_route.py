"""Recompute the Programming & Numerical Methods 0.5.0 sensor-calibration project route from its public files."""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/programming"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
GUIDE = (COURSE / "assignments/sensor-calibration-project-guide.md").read_text(encoding="utf-8")
LESSON = LESSONS["programming-project-guide"]
REHEARSAL_IDS = LESSON["question_ids"]


def key(question_id: str, field_id: str) -> float:
    return next(spec for spec in ITEMS[question_id]["solution_spec"]["field_specs"] if spec["id"] == field_id)["answer"]


def option(question_id: str, field_id: str) -> str:
    field = next(field for field in ITEMS[question_id]["response_fields"] if field["id"] == field_id)
    return field["options"][int(key(question_id, field_id))]


def records(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def contract(rows):
    """The guide's contract: duplicated IDs, non-finite signals and unknown split labels are all rejected."""
    counts = Counter(row["record_id"] for row in rows)
    accepted = [
        row for row in rows
        if counts[row["record_id"]] == 1 and math.isfinite(float(row["signal_mV"]))
        and row["split"] in {"train", "held_out"}
    ]
    return accepted, len(rows) - len(accepted)


def normal_equations(rows):
    """Uncentered normal equations solved exactly by Cramer's rule, unlike the centered formula used to author keys."""
    n = len(rows)
    sx = sum(Fraction(row["standard_mM"]) for row in rows)
    sy = sum(Fraction(row["signal_mV"]) for row in rows)
    sxx = sum(Fraction(row["standard_mM"]) ** 2 for row in rows)
    sxy = sum(Fraction(row["standard_mM"]) * Fraction(row["signal_mV"]) for row in rows)
    determinant = n * sxx - sx * sx
    slope = (n * sxy - sx * sy) / determinant
    return (sy * sxx - sx * sxy) / determinant, slope


def errors(rows, intercept, slope):
    residuals = [Fraction(row["signal_mV"]) - intercept - slope * Fraction(row["standard_mM"]) for row in rows]
    return float(sum(residuals) / len(residuals)), math.sqrt(float(sum(e * e for e in residuals) / len(residuals)))


def test_route_is_scheduled_optional_and_ungraded():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["grading_policy"]["mode"] == "formative-only"
    rehearsal = ASSESSMENTS["programming-project-rehearsal-practice"]
    project = ASSESSMENTS["programming-sensor-calibration-project"]
    assert "programming-project-guide" in WEEKS[13]["lesson_ids"] and rehearsal["id"] in WEEKS[13]["assessment_ids"]
    assert (rehearsal["type"], rehearsal["mode"], rehearsal["week"]) == ("data-analysis", "practice", 13)
    assert rehearsal["question_ids"] == REHEARSAL_IDS and len(REHEARSAL_IDS) == 5
    assert rehearsal["points"] == sum(ITEMS[item]["points"] for item in REHEARSAL_IDS)
    assert project["id"] in WEEKS[14]["assessment_ids"]
    assert (project["type"], project["mode"], project["points"], project["question_ids"]) == ("project", "self-assessment", 0, [])
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    assert cases[0]["id"] == "programming:case"
    milestones = [case for case in cases if case["id"].startswith("programming:project-m")]
    assert [case["id"].split(":project-")[1].split("-")[0] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(case["mode"] == "self-assessment" for case in milestones)
    assert all(criterion["points"] == 0 for case in milestones for criterion in case["rubric"])
    assert "**Practice gradebook**: Calibration project rehearsal" in GUIDE
    assert rehearsal["title"].startswith("Calibration project rehearsal")


def test_rehearsal_keys_recompute_independently():
    rows = records(COURSE / "assignments/calibration-rehearsal-records.csv")
    accepted, rejected = contract(rows)
    training = [row for row in accepted if row["split"] == "train"]
    assert (len(accepted), rejected, len(training)) == (39, 4, 23)
    item = "programming-project:rehearsal-contract"
    assert (key(item, "accepted_rows"), key(item, "rejected_rows"), key(item, "training_rows")) == (39, 4, 23)
    assert option(item, "duplicate_rule").startswith("Because the two rows disagree")

    intercept, slope = normal_equations(training)
    assert slope == Fraction(569, 114) and round(float(slope), 3) == key("programming-project:rehearsal-fit", "slope")
    assert round(float(intercept), 2) == key("programming-project:rehearsal-fit", "intercept")
    bias, training_rmse = errors(training, intercept, slope)
    assert bias == 0 and round(training_rmse, 3) == key("programming-project:rehearsal-fit", "training_rmse")
    assert option("programming-project:rehearsal-fit", "slope_shift").startswith("Rejecting both T1-L2-R2 rows")
    # Keeping the first copy of the duplicated ID restores the balanced design and an exact slope of 5 mV/mM.
    first_copy = [row for row in rows if not (row["record_id"] == "T1-L2-R2" and row["signal_mV"] == "17.7")]
    kept, _ = contract(first_copy)
    assert normal_equations([row for row in kept if row["split"] == "train"])[1] == 5

    transfer = "programming-project:rehearsal-transfer"
    for batch, bias_field, rmse_field in (("H1", "h1_bias", "h1_rmse"), ("H2", "h2_bias", "h2_rmse")):
        bias, rmse = errors([row for row in accepted if row["batch_id"] == batch], intercept, slope)
        assert round(bias, 2) == key(transfer, bias_field) and round(rmse, 2) == key(transfer, rmse_field)
        assert rmse > 2 * training_rmse
    assert option(transfer, "comparison").startswith("Both are well above it")


def test_rehearsal_rows_follow_the_rule_stated_in_the_guide():
    assert "signal_mV = 12 + 5 × standard_mM + batch offset + replicate offset" in GUIDE
    for text in ("T1–T3 (offsets −0.6, +0.3 and +0.9 mV)", "H1 and H2 (+2.5 and −1.5 mV)", "(−0.3 and +0.3 mV)"):
        assert text in GUIDE
    offsets = {"T1": Fraction("-0.6"), "T2": Fraction("0.3"), "T3": Fraction("0.9"), "H1": Fraction("2.5"),
               "H2": Fraction("-1.5")}
    replicates = {"R1": Fraction("-0.3"), "R2": Fraction("0.3")}
    rows = records(COURSE / "assignments/calibration-rehearsal-records.csv")
    accepted, _ = contract(rows)
    for row in accepted:
        expected = 12 + 5 * Fraction(row["standard_mM"]) + offsets[row["batch_id"]] + replicates[row["replicate_id"]]
        assert Fraction(row["signal_mV"]) == expected, row["record_id"]
    project = records(COURSE / "assessment-specs/sensor-calibration-records.csv")
    assert not {row["record_id"] for row in rows} & {row["record_id"] for row in project}
    assert not {row["batch_id"] for row in rows} & {row["batch_id"] for row in project}


def test_guide_restates_the_draft_and_its_checks_recompute():
    draft = (COURSE / "assessment-specs/integrative-sensor-calibration-project.md").read_text(encoding="utf-8")
    assert "20 + 3 * standard_mM + batch_offset_mV + replicate_offset_mV" in draft
    assert "signal_mV = 20 + 3 × standard_mM + batch offset + replicate offset" in GUIDE
    assert "batch offsets −1, 0, 0, 1, 4 and −3 mV for B01 to B06" in GUIDE
    project = records(COURSE / "assessment-specs/sensor-calibration-records.csv")
    accepted, rejected = contract(project)
    assert len(accepted) == len(project) == 90 and rejected == 0
    intercept, slope = normal_equations([row for row in project if row["split"] == "train"])
    assert (intercept, slope) == (20, 3)
    b05 = errors([row for row in project if row["batch_id"] == "B05"], intercept, slope)
    b06 = errors([row for row in project if row["batch_id"] == "B06"], intercept, slope)
    assert b05[0] == pytest.approx(4) and b06[0] == pytest.approx(-3)
    assert round(b05[1], 3) == 4.003 and round(b06[1], 3) == 3.004
    for guide_text, draft_text in (
        ("an intercept of 20 mV and a slope of 3 mV/mM", "an intercept of 20 mV and a slope of 3 mV/mM"),
        ("+4 mV for B05 and −3 mV for B06", "+4 mV for B05 and −3 mV for B06"),
        ("about 4.003 and 3.004 mV", "about 4.003 mV and 3.004 mV"),
    ):
        assert guide_text in GUIDE and draft_text in draft, guide_text

    worked = [{"standard_mM": x, "signal_mV": y} for x, y in (("0", "10.0"), ("2", "14.2"), ("4", "17.8"))]
    intercept, slope = normal_equations(worked)
    assert (intercept, slope) == (Fraction("10.1"), Fraction("1.95"))
    assert round(errors(worked, intercept, slope)[1], 3) == 0.141
    new_batch = [{"standard_mM": "1", "signal_mV": "12.6"}, {"standard_mM": "3", "signal_mV": "16.4"}]
    bias, rmse = errors(new_batch, intercept, slope)
    assert bias == pytest.approx(0.5) and round(rmse, 3) == 0.502
    for text in ("the slope is 15.6/8 = 1.95 mV/mM", "≈ 0.141 mV", "+0.50 mV", "≈ 0.502 mV"):
        assert text in GUIDE

    code = re.search(r"```python\n(.*?)```", GUIDE, re.S).group(1)
    namespace: dict = {}
    exec(compile(code, "sensor-calibration-project-guide.md", "exec"), namespace)
    fitted = namespace["fit_line"]([0, 2, 4], [10.0, 14.2, 17.8])
    assert fitted == pytest.approx((10.1, 1.95))
    with pytest.raises(ValueError):
        namespace["fit_line"]([2, 2, 2], [1.0, 2.0, 3.0])
    with pytest.raises(ValueError):
        namespace["fit_line"]([1], [1.0])


def test_lab_and_project_data_are_package_pinned_and_links_resolve():
    assert MANIFEST["learner_resources"] == [
        "labs/pipeline-records.csv",
        "assessment-specs/sensor-calibration-records.csv",
        "assignments/calibration-rehearsal-records.csv",
    ]

    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    lab = repository.lesson("programming", "programming-lab-01").markdown
    assert "](/api/v1/courses/programming/resources/labs/pipeline-records.csv)" in lab
    guide = repository.lesson("programming", "programming-project-guide").markdown
    assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", guide)
    assert "/api/v1/courses/programming/resources/assessment-specs/sensor-calibration-records.csv" in guide
    assert "/api/v1/courses/programming/resources/assignments/calibration-rehearsal-records.csv" in guide
    assert "#/course/programming/lesson/programming-13" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("programming", path) == (COURSE / path).read_bytes()
