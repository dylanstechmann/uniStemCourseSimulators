"""Keep the proposed Biochemistry midterm answer-free, inactive and mapped."""

from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

from courselab.units import parse_unit

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
PACKET = COURSE / "assessment-specs/midterm-candidate.json"
SPEC = importlib.util.spec_from_file_location(
    "assessment_candidates", ROOT / "tools/assessment_candidates.py"
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)
# Open homework, review and project lessons added in 0.5.0 revisit existing objectives; the inactive
# candidate stays mapped to the topic lessons it was drafted against.
# The inactive 0.4.85 candidates also predate the five 0.6.0 mechanism/bridge lessons.
# Their original coverage contract stays frozen; new public objectives are not certified by these candidates.
POST_CANDIDATE_LESSON_PREFIXES = (
    "biochemistry-hw", "biochemistry-review-", "biochemistry-project-",
    *(f"biochemistry-{number}" for number in range(28, 33)),
)


def test_midterm_candidate_is_answer_free_inactive_and_covers_first_seven_weeks():
    candidate = json.loads(PACKET.read_text(encoding="utf-8"))
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    scheduled = {
        lesson_id
        for week in manifest["duration"]["weeks"]
        if week["week"] <= 7
        for lesson_id in week["lesson_ids"]
        if not lesson_id.startswith(POST_CANDIDATE_LESSON_PREFIXES)
    }
    lessons = {
        lesson["id"]: lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
    }
    expected_objectives = {
        objective
        for lesson_id in scheduled
        for objective in lessons[lesson_id]["objectives"]
    }

    assert candidate["candidate_id"] == "biochemistry-midterm-candidate-v1"
    assert candidate["content_version"] == "0.4.85"
    assert candidate["content_version"] in {entry["version"] for entry in manifest["history"]}
    assert candidate["state"] == "inactive-review-candidate"
    assert candidate["review"]["status"] == "unreviewed"
    assert candidate["candidate_id"] not in {item["id"] for item in manifest["assessments"]}
    assert set(candidate["lesson_ids"]) == scheduled
    assert set(candidate["objective_ids"]) == expected_objectives
    assert candidate["points"] == 120
    assert len(candidate["questions"]) == 12
    assert sum(item["points"] for item in candidate["questions"]) == 120
    assert AUDIT.FORBIDDEN.isdisjoint(AUDIT.keys(candidate["questions"]))
    assert {
        objective
        for item in candidate["questions"]
        for objective in item["learning_objective_ids"]
    } == expected_objectives
    assert {
        objective
        for evidence in candidate["objective_evidence"]
        for objective in evidence["objective_ids"]
    } == expected_objectives
    assert candidate["objective_link_occurrences"] == sum(
        len(evidence["objective_ids"]) for evidence in candidate["objective_evidence"]
    )
    assert candidate["key_status"].startswith("An unreviewed private key/grader draft")
    for item in candidate["questions"]:
        assert item["points"] == 10
        assert item["type"] == "structured"
        assert len(item["response_fields"]) == 2
        assert [field["points"] for field in item["response_fields"]] == [5, 5]
        assert AUDIT.FORBIDDEN.isdisjoint(AUDIT.keys(item["response_fields"]))
        for field in item["response_fields"]:
            if field["type"] == "numeric":
                parse_unit(field.get("unit") or "")
                assert field["significant_figures"] == 3


def test_midterm_synthetic_observations_have_replicates_and_no_derived_keys():
    with (COURSE / "assessment-specs/midterm-candidate-observations.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))

    assert rows
    assert all(row["notes"] for row in rows)
    urea = {
        row["measurement"]: float(row["value"])
        for row in rows
        if row["case_id"] == "case-12"
    }
    assert urea["available nitrogen atoms"] / urea["nitrogen atoms per urea"] == 4
    assert 4 * urea["high-energy phosphate equivalents per urea"] == 16
    kinetics = [row for row in rows if row["case_id"] in {"case-07", "case-08"}]
    assert {row["condition"] for row in kinetics} == {"control", "inhibitor"}
    for condition in ("control", "inhibitor"):
        condition_rows = [row for row in kinetics if row["condition"] == condition]
        assert len(condition_rows) % 2 == 0
        paired_observations = {}
        for index in range(0, len(condition_rows), 2):
            setting, rate = condition_rows[index : index + 2]
            assert setting["measurement"] == "substrate concentration"
            assert rate["measurement"] == "initial rate"
            assert setting["replicate"] == rate["replicate"]
            paired_observations.setdefault(float(setting["value"]), []).append(
                setting["replicate"]
            )
        assert len(paired_observations) >= 3
        assert all(len(replicates) == 3 for replicates in paired_observations.values())
    purification = [row for row in rows if row["case_id"] == "case-09"]
    assert {row["condition"] for row in purification} == {"crude", "later fraction"}
    assert {row["measurement"] for row in purification} == {
        "total protein",
        "total activity",
    }
