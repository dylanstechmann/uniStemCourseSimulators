"""Separate trusted-author checks; same AI, not human or learner-code review."""

from __future__ import annotations

import ast
import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/programming"
BANK = {
    q["id"]: q
    for q in json.loads((COURSE / "question-banks/practice.json").read_text())[
        "questions"
    ]
}
MANIFEST = json.loads((COURSE / "course.json").read_text())


def example(number):
    lesson = next(
        lesson
        for m in MANIFEST["modules"]
        for lesson in m["lessons"]
        if lesson["id"] == f"programming-{number}"
    )
    text = (COURSE / lesson["reading"]).read_text()
    return text.split("```python", 1)[1].split("```", 1)[0]


def expected_answers():
    old = {
        "programming-2:check": 2 + 3 * 0.4,
        "programming-2:euler-amplification": abs(1 - 4 * 0.6),
        "programming-3:residual-standard-error": math.sqrt(
            sum(v * v for v in [0.1, -0.2, 0.1, 0, 0]) / (5 - 2)
        ),
        "programming-5:three-doublings": 30 / math.log2(8),
        "programming-5:culture-doubling-time": 24 / math.log2(1.28e6 / 2e5),
        "programming-5:float-gap": 0.1 + 0.2 - 0.3,
        "programming-6:pair-count": sum(range(10000)),
        "programming-6:pair-time": sum(range(10000)) / 1e7,
        "programming-6:scaling-factor": 3 * (60000 / 20000) ** 2,
        "programming-6:binary-steps": math.ceil(math.log2(1_000_000)),
        # Preserved approximate scale, explicitly distinguished from exact spacing below.
        "programming-7:spacing": 1e8 * math.ulp(1.0),
        "programming-7:true-variance": sum(v * v for v in [-1, 0, 1]) / 3,
        "programming-7:digits-lost": math.log10(100000002**2 / 0.6667),
        "programming-7:cancellation-error": 1e-12 * 1.0000001 / (1.0000001 - 1),
    }
    values = {
        8: {
            "concentration": 1.5 / (500 / 1000),
            "scaled-inputs": 3 / 1,
            "accepted": 6 - 4,
            "quarantined": 6 - 2,
            "calibrated": (2.4 - 0.4) / 2,
            "unit-factor": 1000,
        },
        9: {
            "broadcast-size": 4 * 3,
            "channel-mean": sum([0, 4, 8]) / 3,
            "sample-mean": sum([8, 8]) / 2,
            "paired-change": sum(b - a for a, b in zip([1, 2, 3], [2, 4, 8])) / 3,
            "memory-mb": 2000 * 3000 * 8 / 1_000_000,
            "sample-correction": 10 - 1,
        },
        10: {
            "retained-midpoint": (1.25 + 1.5) / 2,
            "retained-bound": (1.5 - 1.25) / 2,
            "width-eight": 4 / 2**8,
            "minimum-halvings": math.ceil(math.log2(4 / (2 * 0.001))),
            "newton-first": 1 - (1 - 2) / 2,
            "newton-domain": 10 - (1 / 3) / (1 / 72),
        },
        11: {
            "trapezoid-coarse": 0.5 * (0.25 + 0.5),
            "trapezoid-fine": 0.25 * (0.0625 + 0.25 + 0.5625 + 0.5),
            "simpson": 0.5 / 3 * (4 * 0.25 + 1),
            "fine-error": (0.375 - 0.34375) / 3,
            "irregular-area": 1 * (0 + 2) / 2 + 2 * (2 + 2) / 2,
            "euler-end": (1 - 2 * 0.25) ** 4,
        },
        12: {
            "centered-intercept": sum([2, 3, 5]) / 3,
            "slope": (5 - 2) / 2,
            "sse": sum(v * v for v in [1 / 6, -1 / 3, 1 / 6]),
            "residual-df": 3 - 2,
            "rse": math.sqrt(1 / 6),
            "exact-spacing": math.nextafter(1e8, math.inf) - 1e8,
        },
        14: {
            "matrix-norm": max(abs(1) + abs(1), abs(1) + abs(1.0001)),
            "inverse-norm": max(abs(1.0001) + abs(-1), abs(-1) + abs(1)) / (1 * 1.0001 - 1 * 1),
            "condition-number": max(2, 2.0001)
            * max(abs(1.0001) + abs(-1), abs(-1) + abs(1))
            / (1.0001 - 1),
            "forward-error": max(abs(0.5 - 1), abs(1.5 - 1)) / 1,
            "residual-norm": max(abs(2 - (0.5 + 1.5)), abs(2.0001 - (0.5 + 1.0001 * 1.5))),
            "rhs-relative-perturbation": abs(2.00015 - 2.0001) / 2.0001,
        },
        15: {
            "true-value": 1 / (1 + 0.5**2),
            # Lagrange form built from the table, independent of the stated coefficients.
            "interpolated-value": sum(
                fy * math.prod((0.5 - xj) / (xi - xj) for xj in (0, 1, 2) if xj != xi)
                for xi, fy in ((0, 1), (1, 0.5), (2, 0.2))
            ),
            "signed-error": sum(
                fy * math.prod((0.5 - xj) / (xi - xj) for xj in (0, 1, 2) if xj != xi)
                for xi, fy in ((0, 1), (1, 0.5), (2, 0.2))
            )
            - 1 / (1 + 0.5**2),
            "basis-value": (0.5 - 0) * (0.5 - 1) / ((2 - 0) * (2 - 1)),
            "extrapolated-value": sum(
                fy * math.prod((4 - xj) / (xi - xj) for xj in (0, 1, 2) if xj != xi)
                for xi, fy in ((0, 1), (1, 0.5), (2, 0.2))
            ),
        },
        13: {
            "sensitivity": 2 / 3,
            "precision": 2 / 5,
            "specificity": 2 / 5,
            "accuracy": 4 / 8,
            "higher-threshold": 6 / 8,
            "donor-overlap": len(set(range(4)) & set(range(4))),
        },
    }
    old.update(
        {
            f"programming-{n}:{key}": value
            for n, items in values.items()
            for key, value in items.items()
        }
    )
    old.update(
        {
            "programming-lab-01:accepted": 16,
            "programming-lab-01:excluded": 4,
            "programming-lab-01:precision": 2 / 5,
            "programming-lab-01:sensitivity": 2 / 3,
        }
    )
    return old


EXPECTED = expected_answers()


def test_every_numeric_item_has_a_separate_calculation():
    assert set(EXPECTED) == {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 65


@pytest.mark.parametrize("key", sorted(EXPECTED))
def test_numeric_key_matches_declared_tolerance(key):
    spec = BANK[key]["solution_spec"]
    allowed = max(
        spec["tolerance"], spec.get("relative_tolerance", 0) * abs(EXPECTED[key])
    )
    assert abs(spec["answer"] - EXPECTED[key]) <= allowed


@pytest.mark.parametrize("number", [8, 9, 12])
def test_authored_code_is_valid_python_syntax(number):
    ast.parse(example(number))


@pytest.fixture
def concentration():
    namespace = {}
    # Only the trusted, repository-authored instructional snippet is executed.
    exec(compile(example(8), "trusted-concentration-example", "exec"), namespace)
    return namespace["concentration_mg_per_ml"]


@pytest.mark.parametrize(
    "mass,volume,answer", [(0, 0.5, 0), (1.5, 0.5, 3), (3, 1, 3), (2, 4, 0.5)]
)
def test_pure_function_known_answers_and_no_hidden_state(
    concentration, mass, volume, answer
):
    assert concentration(mass, volume) == answer
    assert concentration(mass * 2, volume * 2) == answer


@pytest.mark.parametrize(
    "mass,volume,error",
    [
        (-1, 1, ValueError),
        (1, 0, ValueError),
        (1, -1, ValueError),
        (float("nan"), 1, ValueError),
        (1, float("inf"), ValueError),
        (float("-inf"), 1, ValueError),
        (True, 1, TypeError),
        (1, False, TypeError),
        ("1", 1, TypeError),
        (None, 1, TypeError),
        (1e308, 1e-308, ValueError),
    ],
)
def test_pure_function_rejects_contract_failures(concentration, mass, volume, error):
    with pytest.raises(error):
        concentration(mass, volume)


def test_array_axis_outer_and_chunked_reduction_meanings():
    signal = [[10, 100], [14, 104], [18, 108]]
    original = [row[:] for row in signal]
    corrected = [
        [value - base for value, base in zip(row, [10, 100])] for row in signal
    ]
    assert corrected == [[0, 0], [4, 4], [8, 8]]
    assert [sum(column) / 3 for column in zip(*corrected)] == [4, 4]
    assert [sum(row) / 2 for row in corrected] == [0, 4, 8]
    unequal = [[1, 10], [3, 20], [5, 30]]
    assert [sum(col) / 3 for col in zip(*unequal)] == [3, 20]
    assert [sum(row) / 2 for row in unequal] == [5.5, 11.5, 17.5]
    outer = [[b - a for a in [1, 2, 3]] for b in [2, 4, 8]]
    assert len(outer) == 3 and sum(map(len, outer)) == 9
    # Mean coincidence does not turn the outer grid into paired independent records.
    assert sum(map(sum, outer)) / 9 == pytest.approx(8 / 3)
    assert signal == original


def test_bisection_invariants_width_convention_and_pole_counterexample():
    low, high = 1.0, 2.0
    for k in range(1, 13):
        middle = (low + high) / 2
        if middle * middle > 2:
            high = middle
        else:
            low = middle
        assert low <= math.sqrt(2) <= high
        assert high - low == 2**-k
        assert abs((low + high) / 2 - math.sqrt(2)) <= (high - low) / 2
        if k == 2:
            assert (low, high) == (1.25, 1.5)

    def pole(x):
        return 1 / (x - 1)

    assert pole(0) < 0 < pole(2)
    with pytest.raises(ZeroDivisionError):
        pole(1)
    assert (0 - 2) ** 2 > 0 and (4 - 2) ** 2 > 0 and (2 - 2) ** 2 == 0


def test_newton_domain_and_residual_scale_are_distinct():
    c = 10
    value = c / (2 + c) - 0.5
    derivative = 2 / (2 + c) ** 2
    assert c - value / derivative == pytest.approx(-14)
    assert 0.001 * (3 - 2) == 0.001 and abs(3 - 2) == 1
    assert (3 - 2) == 1000 * (0.001 * (3 - 2))


def trapezoid(function, intervals):
    h = 1 / intervals
    return math.fsum(
        h * (function(i * h) + function((i + 1) * h)) / 2 for i in range(intervals)
    )


def test_quadrature_refinement_order_and_richardson_cancellation():
    coarse, fine, finer = [trapezoid(lambda t: t * t, n) for n in [2, 4, 8]]
    assert (coarse - fine) / (fine - finer) == 4
    assert fine + (fine - coarse) / 3 == pytest.approx(1 / 3)
    assert (coarse - fine) / 3 == pytest.approx(fine - 1 / 3)
    times, rate = [0, 1, 3], [0, 2, 2]
    assert (
        sum((times[i + 1] - times[i]) * (rate[i] + rate[i + 1]) / 2 for i in range(2))
        == 5
    )


@pytest.mark.parametrize(
    "step,stable,positive",
    [(0.25, True, True), (0.75, True, False), (1.1, False, False)],
)
def test_euler_accuracy_stability_and_positivity(step, stable, positive):
    multiplier = 1 - 2 * step
    assert (abs(multiplier) < 1) == stable
    assert (multiplier >= 0) == positive
    state = 1
    for _ in range(4):
        state *= multiplier
    assert state == pytest.approx(multiplier**4)
    if step == 0.25:
        assert state != pytest.approx(math.exp(-2))


def test_affine_residual_orthogonality_rank_and_remote_origin():
    z, y = [-1, 0, 1], [2, 3, 5]
    a = sum(y) / 3
    b = sum(x * v for x, v in zip(z, y)) / sum(x * x for x in z)
    residual = [v - (a + b * x) for x, v in zip(z, y)]
    assert sum(residual) == pytest.approx(0, abs=1e-14)
    assert sum(x * r for x, r in zip(z, residual)) == pytest.approx(0, abs=1e-14)
    assert sum(r * r for r in residual) == pytest.approx(1 / 6)
    uncentered = a - b * 100000002
    assert uncentered == pytest.approx(-149999999.666667)
    for x in [100000001, 100000002, 100000003]:
        assert uncentered + b * x == pytest.approx(a + b * (x - 100000002), abs=1e-7)
    assert [1 + 2 * x for x in [2, 2, 2]] == [5 + 0 * x for x in [2, 2, 2]]
    assert 1 + 2 * 3 != 5 + 0 * 3


def test_exact_binade_spacing_differs_from_preserved_scale_estimate():
    exact = math.ulp(1e8)
    approximate = EXPECTED["programming-7:spacing"]
    assert exact == 2**-26
    assert abs(approximate / exact - 1) > 0.4
    lesson = next(
        lesson
        for m in MANIFEST["modules"]
        for lesson in m["lessons"]
        if lesson["id"] == "programming-12"
    )
    text = (COURSE / lesson["reading"]).read_text()
    assert "scale estimate, not the exact adjacent-float spacing" in text


def lab_records():
    with (COURSE / "labs/pipeline-records.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    accepted, excluded = [], {}
    for row in rows:
        if not row["mass_mg"].strip():
            excluded[row["record_id"]] = "missing mass"
            continue
        mass, volume = float(row["mass_mg"]), float(row["volume"])
        if not math.isfinite(mass) or not math.isfinite(volume):
            excluded[row["record_id"]] = "nonfinite"
        elif mass < 0 or volume <= 0:
            excluded[row["record_id"]] = "domain"
        elif row["volume_unit"] not in ["uL", "mL"]:
            excluded[row["record_id"]] = "unknown unit"
        else:
            converted = volume / 1000 if row["volume_unit"] == "uL" else volume
            accepted.append((row, mass / converted))
    return rows, accepted, excluded


CHECKS = BANK["programming-lab-01:summary"]["solution_spec"]["validation_spec"][
    "checks"
]


@pytest.mark.parametrize("check", CHECKS, ids=lambda c: c["id"])
def test_csv_summary_cell_recalculated_from_raw_tokens(check):
    _, accepted, _ = lab_records()
    values = [value for row, value in accepted if row["donor"] == check["row_id"]]
    answer = (
        len(values)
        if check["column"] == "accepted_records"
        else math.fsum(values) / len(values)
    )
    assert abs(check["answer"] - answer) <= check["tolerance"]


def test_lab_filtering_identity_unit_equivalence_and_disjoint_donors():
    rows, accepted, excluded = lab_records()
    assert len(rows) == 20 and len(accepted) == 16 and len(excluded) == 4
    assert len({r["record_id"] for r in rows}) == 20
    assert excluded == {
        "X01": "missing mass",
        "X02": "domain",
        "X03": "nonfinite",
        "X04": "unknown unit",
    }
    donors = {
        split: {r["donor"] for r, _ in accepted if r["split"] == split}
        for split in ["train", "evaluation"]
    }
    assert donors["train"].isdisjoint(donors["evaluation"])
    assert len(donors["train"]) == len(donors["evaluation"]) == 4
    for row, value in accepted:
        expected = int(row["donor"][1:]) + (2 if row["volume_unit"] == "mL" else 0)
        assert value == expected


@pytest.mark.parametrize(
    "threshold,expected", [(0.5, (2, 3, 1, 2)), (0.7, (2, 1, 1, 4))]
)
def test_frozen_evaluation_confusion_counts_and_equality_rule(threshold, expected):
    _, accepted, _ = lab_records()
    counts = [0, 0, 0, 0]
    evaluation = [r for r, _ in accepted if r["split"] == "evaluation"]
    for row in evaluation:
        truth = int(row["label"]) == 1
        predicted = float(row["score"]) >= threshold
        index = 0 if truth and predicted else 1 if predicted else 2 if truth else 3
        counts[index] += 1
    assert tuple(counts) == expected and sum(counts) == 8
    assert 2 * counts[0] / (2 * counts[0] + counts[1] + counts[2]) == pytest.approx(
        0.5 if threshold == 0.5 else 2 / 3
    )


def test_preprocessing_and_majority_case_counterexamples():
    assert sum([0, 2]) / 2 == 1
    assert sum([0, 2, 100, 102]) / 4 == 51
    assert 990 / 1000 == 0.99 and 0 / (0 + 10) == 0
    with pytest.raises(ZeroDivisionError):
        _ = 0 / (0 + 0)


def test_weekly_sequence_references_and_partial_labels():
    assert MANIFEST["version"] == MANIFEST["history"][-1]["version"]
    weeks = MANIFEST["duration"]["weeks"]
    lessons = [lesson["id"] for m in MANIFEST["modules"] for lesson in m["lessons"]]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    assert sorted(lesson for w in weeks for lesson in w["lesson_ids"]) == sorted(
        lessons
    )
    assessment_ids = {a["id"] for a in MANIFEST["assessments"]}
    assert all(a in assessment_ids for w in weeks for a in w["assessment_ids"])
    assert (
        MANIFEST["maturity"] == "partial"
        and MANIFEST["review"]["status"] == "unreviewed"
    )
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert all(a["mode"] != "graded" for a in MANIFEST["assessments"])
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    cards = len(
        json.loads(
            (COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8")
        )["cards"]
    )
    assert (
        f"The current package contains {len(lessons)} lessons/activity guides, {len(BANK)} public practice items and {cards} retrieval cards"
        in syllabus
    )


def test_unit_conversion_contract_and_provenance_reading():
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "programming-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "Missing is not zero" in text
    assert "A pure function has explicit inputs" in text
    assert "Keep raw input files unchanged" in text

    volume_ml = 500 / 1000
    concentration_mg_per_ml = 1.5 / volume_ml
    assert volume_ml == pytest.approx(0.5)
    assert concentration_mg_per_ml == pytest.approx(3)


def test_quadrature_comparison_and_euler_stability_limits():
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "programming-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "Euler instead multiplies the state at each step" in text
    assert r"0<\lambda h<2" in text

    left, midpoint, right = 0.0, 1.0, 2.0
    def quadratic(t):
        return t**2

    trapezoid = (right - left) * (quadratic(left) + quadratic(right)) / 2
    simpson = (
        (right - left)
        * (quadratic(left) + 4 * quadratic(midpoint) + quadratic(right))
        / 6
    )
    exact_integral = right**3 / 3 - left**3 / 3
    assert trapezoid == pytest.approx(4)
    assert simpson == pytest.approx(8 / 3)
    assert simpson == pytest.approx(exact_integral)

    lam, unstable_step, stable_step, value = 4.0, 0.6, 0.4, 1.0
    unstable_factor = 1 - lam * unstable_step
    next_value = unstable_factor * value
    assert unstable_factor == pytest.approx(-1.4)
    assert abs(next_value) > abs(value)
    stable_factor = 1 - lam * stable_step
    assert stable_factor == pytest.approx(-0.6)
    assert abs(stable_factor) < 1


def test_residual_error_and_group_aware_validation_reading():
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "programming-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "not the standard error of every coefficient" in text
    assert "keep all rows from a donor together" in text

    residuals = [0.1, -0.2, 0.1, 0.0, 0.0]
    residual_sum_squares = sum(value**2 for value in residuals)
    degrees_of_freedom = 5 - 2
    residual_standard_error = math.sqrt(residual_sum_squares / degrees_of_freedom)
    assert residual_sum_squares == pytest.approx(0.06)
    assert degrees_of_freedom == 3
    assert residual_standard_error == pytest.approx(0.1414, abs=0.0001)
    assert BANK["programming-3:residual-standard-error"]["solution_spec"][
        "answer"
    ] == pytest.approx(0.1414)


def test_paired_plot_uncertainty_interval_and_independent_unit():
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "programming-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "The independent sample size is four donors" in text
    assert "A standard error instead describes precision" in text
    assert "does not show where 95% of individual donor responses lie" in text

    changes = [1.0, 0.0, 2.0, 1.0]
    mean = sum(changes) / len(changes)
    sample_sd = math.sqrt(sum((value - mean) ** 2 for value in changes) / 3)
    standard_error = sample_sd / math.sqrt(len(changes))
    margin = 3.182446305 * standard_error
    interval = (mean - margin, mean + margin)
    assert mean == pytest.approx(1)
    assert sample_sd == pytest.approx(math.sqrt(2 / 3))
    assert interval == pytest.approx((-0.299, 2.299), abs=0.001)
    assert BANK["programming-4:check"]["solution_spec"]["answer"] == 0
    assert BANK["programming-4:show-observations"]["solution_spec"]["answer"] == 0


def test_original_lesson_objectives_link_to_matching_course_outcomes():
    expected = {
        "programming-1-objective-1": ["programming-outcome-4"],
        "programming-1-objective-2": ["programming-outcome-1"],
        "programming-2-objective-1": ["programming-outcome-2"],
        "programming-2-objective-2": ["programming-outcome-2"],
        "programming-3-objective-1": ["programming-outcome-3"],
        "programming-3-objective-2": ["programming-outcome-3"],
        "programming-4-objective-1": ["programming-outcome-4"],
        "programming-4-objective-2": ["programming-outcome-4"],
    }
    objectives = {item["id"]: item for item in MANIFEST["lesson_objectives"]}
    for objective_id, outcome_ids in expected.items():
        assert objectives[objective_id]["course_outcome_ids"] == outcome_ids

    for lesson_number, outcome_ids in (
        (1, ["programming-outcome-1", "programming-outcome-4"]),
        (2, ["programming-outcome-2"]),
        (3, ["programming-outcome-3"]),
        (4, ["programming-outcome-4"]),
    ):
        assessment = next(
            item for item in MANIFEST["assessments"]
            if item["id"] == f"programming-{lesson_number}-practice"
        )
        assert set(outcome_ids).issubset(assessment["objective_ids"])
        lesson = next(
            lesson
            for module in MANIFEST["modules"]
            for lesson in module["lessons"]
            if lesson["id"] == f"programming-{lesson_number}"
        )
        assert set(assessment["question_ids"]) == set(lesson["question_ids"])
