"""Keep early Biochemistry homework drafts inactive, answer-free and mapped."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
SPEC = importlib.util.spec_from_file_location(
    "assessment_candidates", ROOT / "tools/assessment_candidates.py"
)
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)
# Version 0.5.0 schedules open homework, review and project lessons beside the topic lessons. They revisit
# existing objectives; the inactive candidates stay mapped to the topic lessons they were drafted against.
# The inactive 0.4.85 candidates also predate the five 0.6.0 mechanism/bridge lessons.
# Their original coverage contract stays frozen; new public objectives are not certified by these candidates.
POST_CANDIDATE_LESSON_PREFIXES = (
    "biochemistry-hw", "biochemistry-review-", "biochemistry-project-",
    *(f"biochemistry-{number}" for number in range(28, 33)),
)


def _candidate(number: int) -> dict:
    path = COURSE / f"assessment-specs/homework-{number:02d}-candidate.json"
    return json.loads(path.read_text(encoding="utf-8"))


def test_homework_candidates_cover_their_scheduled_objectives_without_live_policy():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lessons = {
        lesson["id"]: lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
    }
    for number, weeks in (
        (1, (1, 2)),
        (2, (3, 4)),
        (3, (5, 6)),
        (4, (7,)),
        (5, (8, 9)),
        (6, (10,)),
        (7, (11, 12)),
        (8, (13, 14)),
    ):
        candidate = _candidate(number)
        scheduled = [
            week
            for week in manifest["duration"]["weeks"]
            if week["week"] in weeks
        ]
        expected_lessons = [
            lesson_id
            for week in scheduled
            for lesson_id in week["lesson_ids"]
            if not lesson_id.startswith(POST_CANDIDATE_LESSON_PREFIXES)
        ]
        expected_objectives = {
            objective_id
            for lesson_id in expected_lessons
            for objective_id in lessons[lesson_id]["objectives"]
        }
        question_objectives = {
            objective_id
            for question in candidate["questions"]
            for objective_id in question["learning_objective_ids"]
        }
        evidence_objectives = {
            objective_id
            for entry in candidate["objective_evidence"]
            for objective_id in entry["objective_ids"]
        }

        assert (
            candidate["candidate_id"]
            == f"biochemistry-homework-{number:02d}-candidate-v1"
        )
        # Candidates stay bound to the released version they were drafted against.
        assert candidate["content_version"] == "0.4.85"
        assert candidate["content_version"] in {entry["version"] for entry in manifest["history"]}
        assert candidate["state"] == "inactive-review-candidate"
        assert candidate["review"] == {"status": "unreviewed", "reviewers": []}
        assert candidate["candidate_id"] not in {
            assessment["id"] for assessment in manifest["assessments"]
        }
        assert candidate["lesson_ids"] == expected_lessons
        assert set(candidate["objective_ids"]) == expected_objectives
        assert question_objectives == evidence_objectives == expected_objectives
        assert candidate["objective_link_occurrences"] == sum(
            len(entry["objective_ids"]) for entry in candidate["objective_evidence"]
        )
        assert candidate["points"] == sum(
            question["points"] for question in candidate["questions"]
        )
        assert len(candidate["questions"]) >= 5
        brief = (COURSE / candidate["instruction_path"]).read_text(encoding="utf-8")
        assert len(brief.split()) >= 250
        assert AUDIT.FORBIDDEN.isdisjoint(AUDIT.keys(candidate["questions"]))
        assert all(
            question["points"] == 10
            and len(question["response_fields"]) == 2
            and [field["points"] for field in question["response_fields"]] == [5, 5]
            for question in candidate["questions"]
        )
        assert all(
            re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", field["id"])
            for question in candidate["questions"]
            for field in question["response_fields"]
        )
        assert all(
            field.get("unit") != "none"
            for question in candidate["questions"]
            for field in question["response_fields"]
            if field["type"] == "numeric"
        )


def test_homework_candidate_datasets_are_synthetic_and_key_free():
    for number in (1, 2):
        candidate = _candidate(number)
        dataset = COURSE / candidate["dataset_path"]
        with dataset.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        assert rows
        assert {row["case_id"] for row in rows} >= {
            f"case-{index:02d}" for index in range(1, len(candidate["questions"]) + 1)
        }
        assert all(row["notes"] for row in rows)
        assert not any(
            token in column.lower()
            for row in rows
            for column in row
            for token in ("answer", "solution", "key")
        )


def test_homework_candidate_artifact_hashes_validate():
    report = AUDIT.audit(ROOT)
    biochemistry = next(
        package for package in report["packages"] if package["course"] == "biochemistry"
    )
    assert {candidate["id"] for candidate in biochemistry["candidates"]} >= {
        f"biochemistry-homework-{number:02d}-candidate-v1" for number in range(1, 9)
    }
    assert all(
        candidate["declared_review_status"] == "unreviewed"
        and candidate["unresolved_activation_gates"]
        for candidate in biochemistry["candidates"]
    )


def test_week_seven_rate_dataset_has_matched_synthetic_replicates():
    path = COURSE / "assessment-specs/homework-04-candidate-data.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    observations = [row for row in rows if row["case_id"] == "case-04"]
    assert {row["condition"] for row in observations} == {"control", "inhibitor"}
    for condition in ("control", "inhibitor"):
        condition_rows = [row for row in observations if row["condition"] == condition]
        assert {float(row["substrate_uM"]) for row in condition_rows} == {
            10.0,
            20.0,
            40.0,
            80.0,
            160.0,
        }
        for substrate in {row["substrate_uM"] for row in condition_rows}:
            matched = [row for row in condition_rows if row["substrate_uM"] == substrate]
            assert {row["replicate"] for row in matched} == {"1", "2", "3"}
            assert all(float(row["initial_rate_umol_min"]) > 0 for row in matched)


def test_homework_kinetic_calculations_have_dimensionally_complete_inputs():
    h3 = _candidate(3)
    h3_data = COURSE / h3["dataset_path"]
    with h3_data.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    enzyme = next(
        row for row in rows
        if row["case_id"] == "case-02" and row["variable"] == "active_enzyme"
    )
    assert enzyme["unit"] == "µmol"
    assert "amount" in enzyme["notes"]
    turnover = next(
        field for question in h3["questions"]
        for field in question["response_fields"]
        if field["id"] == "turnover-number"
    )
    assert "amount" in turnover["prompt"]
    assert turnover["unit"] == "1/min"
    efficiency = next(
        field for question in h3["questions"]
        for field in question["response_fields"]
        if field["id"] == "catalytic-efficiency"
    )
    assert efficiency["unit"] == "L/(µmol·min)"

    h4 = _candidate(4)
    h4_data = COURSE / h4["dataset_path"]
    with h4_data.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert "inhibitor_concentration_uM" in rows[0]
    inhibitor_rows = [
        row for row in rows
        if row["case_id"] == "case-03" and row["condition"] == "inhibitor"
    ]
    assert inhibitor_rows
    assert {row["inhibitor_concentration_uM"] for row in inhibitor_rows} == {"10"}


def test_homework_08_tracer_case_is_synthetic_and_maps_both_fields():
    candidate = _candidate(8)
    tracer = next(
        question
        for question in candidate["questions"]
        if question["id"].endswith(":case-10")
    )
    assert candidate["points"] == 100
    assert len(candidate["questions"]) == 10
    assert tracer["learning_objective_ids"] == ["biochemistry-ppp-objective-3"]
    assert [field["id"] for field in tracer["response_fields"]] == [
        "labeled-ribose-fraction",
        "tracer-inference-limit",
    ]
    with (COURSE / candidate["dataset_path"]).open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-10"]
    distribution = {
        row["variable"]: float(row["value"])
        for row in rows
        if row["variable"].startswith("ribose_m")
    }
    assert sum(distribution.values()) == 100
    assert distribution["ribose_m1"] + distribution["ribose_m2"] == 60


def test_homework_01_urea_case_recomputes_closed_nitrogen_and_energy_balance():
    candidate = _candidate(1)
    assert candidate["points"] == 80
    assert len(candidate["questions"]) == 8
    case = next(
        question
        for question in candidate["questions"]
        if question["id"].endswith(":case-08")
    )
    assert case["learning_objective_ids"] == ["biochemistry-urea-cycle-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-08"]
    values = {row["variable"]: float(row["value"]) for row in rows}
    urea_amount = values["urea_nitrogen_input"] / values["nitrogen_atoms_per_urea"]
    phosphate_demand = urea_amount * values["high_energy_phosphate_equivalents_per_urea"]
    assert urea_amount == 2.5
    assert phosphate_demand == 10


def test_homework_07_cholesterol_case_recomputes_hepatocyte_pool_balance():
    candidate = _candidate(7)
    assert candidate["points"] == 90
    assert len(candidate["questions"]) == 9
    case = next(
        question
        for question in candidate["questions"]
        if question["id"].endswith(":case-09")
    )
    assert case["learning_objective_ids"] == ["biochemistry-cholesterol-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-09"]
    rates = {row["variable"]: float(row["value"]) for row in rows}
    pool_change = (
        rates["synthesis_rate"]
        + rates["ldlr_uptake_rate"]
        - rates["bile_acid_conversion_rate"]
        - rates["vldl_export_rate"]
    )
    assert pool_change == 30


def test_private_machine_candidates_cover_public_questions_without_exposing_keys():
    private_root = ROOT / ".local/private-assessments/courses/biochemistry/assignments"
    if not private_root.is_dir():
        pytest.skip("private assessment root is not provisioned in this checkout")
    candidate_pairs = [
        (f"homework-{number:02d}-candidate.json", f"homework-{number:02d}-review-draft.json")
        for number in range(1, 9)
    ] + [
        ("midterm-candidate.json", "midterm-review-draft.json"),
        ("final-candidate.json", "final-review-draft.json"),
    ]
    private_paths = [private_root / private_name for _, private_name in candidate_pairs]
    if any(not path.is_file() or path.stat().st_size == 0 for path in private_paths):
        pytest.skip("protected answer fixtures are incomplete in this checkout")

    for public_name, private_name in candidate_pairs:
        public_path = COURSE / "assessment-specs" / public_name
        public = json.loads(public_path.read_text(encoding="utf-8"))
        private_path = private_root / private_name
        private = json.loads(private_path.read_text(encoding="utf-8"))
        public_ids = {question["id"] for question in public["questions"]}
        private_ids = {question["id"] for question in private["questions"]}

        assert private["candidate_id"] == public["candidate_id"]
        assert private["candidate_version"] == public["content_version"]
        assert private["public_candidate_sha256"] == hashlib.sha256(
            public_path.read_bytes()
        ).hexdigest()
        assert private["instruction_sha256"] == hashlib.sha256(
            (COURSE / public["instruction_path"]).read_bytes()
        ).hexdigest()
        assert private["dataset_sha256"] == hashlib.sha256(
            (COURSE / public["dataset_path"]).read_bytes()
        ).hexdigest()
        assert public_ids == private_ids


def test_homework_05_nucleotide_route_accounting_case():
    candidate = _candidate(5)
    assert candidate["points"] == 90
    assert len(candidate["questions"]) == 9
    case = next(q for q in candidate["questions"] if q["id"].endswith(":case-08"))
    assert case["learning_objective_ids"] == ["biochemistry-nucleotide-objective-3"]
    assert [field["id"] for field in case["response_fields"]] == ["prpp-total", "branch-currencies"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-08"]
    values = {row["variable"]: float(row["value"]) for row in rows}
    assert values["de_novo_imp"] + values["hypoxanthine_salvaged_to_imp"] == 7
    assert values["imp_to_amp"] == 2
    assert values["imp_to_gmp"] == 1


def test_final_nucleotide_route_accounting_case_uses_distinct_synthetic_values():
    candidate = json.loads((COURSE / "assessment-specs/final-candidate.json").read_text(encoding="utf-8"))
    assert candidate["points"] == 520
    assert len(candidate["questions"]) == 52
    case = next(q for q in candidate["questions"] if q["id"].endswith(":case-15"))
    assert case["learning_objective_ids"] == ["biochemistry-nucleotide-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-15"]
    values = {row["measurement"]: float(row["value"]) for row in rows}
    assert values["de novo IMP"] + values["hypoxanthine salvaged to IMP"] == 9
    assert values["IMP converted to AMP"] == 3
    assert values["IMP converted to GMP"] == 2


def test_homework_05_atp_pool_balance_case():
    candidate = _candidate(5)
    assert candidate["points"] == 90
    assert len(candidate["questions"]) == 9
    case = next(q for q in candidate["questions"] if q["id"].endswith(":case-09"))
    assert case["learning_objective_ids"] == ["biochemistry-3-objective-3"]
    assert [field["id"] for field in case["response_fields"]] == ["net-pool-change", "pool-interpretation"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-09"]
    values = {row["variable"]: float(row["value"]) for row in rows}
    assert values["atp_synthesis_rate"] - values["atp_utilization_rate"] == 12


def test_final_atp_pool_balance_case_uses_distinct_rates():
    candidate = json.loads((COURSE / "assessment-specs/final-candidate.json").read_text(encoding="utf-8"))
    assert candidate["points"] == 520
    assert len(candidate["questions"]) == 52
    case = next(q for q in candidate["questions"] if q["id"].endswith(":case-16"))
    assert case["learning_objective_ids"] == ["biochemistry-3-objective-3"]
    with (COURSE / candidate["dataset_path"]).open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["case_id"] == "case-16"]
    values = {row["measurement"]: float(row["value"]) for row in rows}
    assert values["ATP synthesis rate"] - values["ATP utilization rate"] == 15
