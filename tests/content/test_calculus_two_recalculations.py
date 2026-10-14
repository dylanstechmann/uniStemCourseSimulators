"""Separate calculations for public practice keys, not human mathematical review.

Uses numerical quadrature, finite sums, transformed improper integrals and
committed observations. It does not import authoring scripts or their constants.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-2"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def integral(f, a, b, panels=1000):
    h = (b - a) / panels
    return (
        h
        / 3
        * math.fsum(
            (1 if i in (0, panels) else 4 if i % 2 else 2) * f(a + i * h)
            for i in range(panels + 1)
        )
    )


def derivative(f, x, step=1e-5):
    return (f(x + step) - f(x - step)) / (2 * step)


def interpolate(nodes, values, x):
    result = 0
    for j, value in enumerate(values):
        factor = 1
        for k, node in enumerate(nodes):
            if k != j:
                factor *= (x - node) / (nodes[j] - node)
        result += value * factor
    return result


def sampled_integral(nodes, values, degree):
    # Integrate the line/parabola interpolants instead of repeating rule weights.
    return math.fsum(
        integral(
            lambda x: interpolate(
                nodes[j : j + degree + 1], values[j : j + degree + 1], x
            ),
            nodes[j],
            nodes[j + degree],
            panels=20,
        )
        for j in range(0, len(nodes) - 1, degree)
    )


def first_certificate(bound, target, initial=0):
    for n in range(initial, 10000):
        if bound(n) <= target:
            return n
    raise AssertionError("No certificate in search range")


def lab_data():
    with (COURSE / "labs/force-samples.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["position"], []).append(float(row["force_N"]))
    means = {key: math.fsum(values) / len(values) for key, values in groups.items()}
    nodes = [
        float(next(row["metres"] for row in rows if row["position"] == key))
        for key in groups
    ]
    corrected = [means[key] - 1 for key in groups]
    return rows, groups, means, nodes, corrected


def geometric_tail(final_index, ratio=0.4):
    return math.fsum(ratio**k for k in range(final_index + 1, final_index + 101))


def expected_answers():
    answers = {}

    def add(lesson, **values):
        answers.update(
            {
                f"calculus-2-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    # Preserved keys checked without changing the authoring objects.
    add(1, check=integral(lambda t: 4 * math.exp(-2 * t), 0, 20))
    add(2, taylor_remainder=1.6487 * 0.5**3 / math.factorial(3))
    work = integral(lambda x: 4 * x, 0, 3)
    add(3, check=work, variable_force_work=work)
    add(
        4,
        check=math.fsum(0.2**k / math.factorial(k) for k in range(3)),
        alternating_series_error=1 / 25,
    )
    old_nodes = [0, 12, 24, 36, 48]
    old_rates = [0.5, 0.7167, 1.0272, 1.4723, 2.1103]
    add(
        5,
        exact_total=integral(lambda t: 0.5 * math.exp(0.03 * t), 0, 48),
        trapezoid=sampled_integral(old_nodes, old_rates, 1),
        simpson=sampled_integral(old_nodes, old_rates, 2),
        error_bound=48 * 12**2 / 12 * 0.5 * 0.03**2 * math.exp(1.44),
        improper_total=integral(lambda t: 2 * math.exp(-0.1 * t), 0, 300, panels=10000),
    )
    angle = math.radians(10)
    lost = -math.expm1(-0.05)
    add(
        6,
        p2_value=math.fsum((-0.2) ** k / math.factorial(k) for k in range(3)),
        remainder_bound=0.2**3 / math.factorial(3),
        decay_linear_error=100 * (0.05 - lost) / lost,
        small_angle=100 * (angle - math.sin(angle)) / math.sin(angle),
        tolerance_kt=math.sqrt(0.02),
    )

    add(
        7,
        substitution=integral(lambda t: 2 * t / (1 + t * t), 0, 2),
        parts_product=integral(lambda x: x * math.exp(x), 0, 1),
        parts_log=integral(math.log, 1, math.e),
        partial_fractions=integral(lambda x: 1 / ((x + 1) * (x + 2)), 0, 1),
        trig_substitution=integral(
            lambda t: math.sin(t) ** 3 * math.cos(t), 0, math.pi / 2
        ),
        arctangent=integral(lambda x: 1 / (1 + x * x), 0, 1),
    )
    # Substitutions remove improper endpoints: u=1/x, x=u²,
    # u=1/(1+t), and u=1/x for the arctangent tail.
    add(
        8,
        power_tail_total=integral(lambda u: 1, 0, 1),
        endpoint_root=integral(lambda u: 2, 0, 1),
        shifted_total=integral(lambda u: 6, 0, 1),
        shifted_tail=integral(lambda u: 6, 0, 0.25),
        cutoff_tail=integral(lambda u: 1, 0, 0.01),
        comparison_exact=integral(lambda u: 1 / (1 + u * u), 0, 1),
    )
    add(
        9,
        geometric_sum=math.fsum(0.4**k for k in range(100)),
        geometric_partial=math.fsum(0.4**k for k in range(4)),
        geometric_tail=geometric_tail(3),
        geometric_index=first_certificate(geometric_tail, 0.001),
        p_tail_bound=integral(lambda u: 1, 0, 0.01),
        telescoping=math.fsum(1 / (n * n + n) for n in range(1, 10)),
    )
    add(
        10,
        log_partial=math.fsum((-1) ** (n + 1) * 0.5**n / n for n in range(1, 5)),
        log_bound=0.5**5 / 5,
        log_term_count=first_certificate(
            lambda n: 0.5 ** (n + 1) / (n + 1), 0.0001, initial=1
        ),
        arctan_partial=math.fsum(
            (-1) ** n * 0.5 ** (2 * n + 1) / (2 * n + 1) for n in range(3)
        ),
        arctan_bound=0.5**7 / 7,
        endpoint_count=first_certificate(lambda n: 1 / (n + 1), 0.01, initial=1),
    )
    ratio_index = 10**10
    add(
        11,
        radius=3 * (ratio_index + 1) / ratio_index,
        interior_value=math.fsum((1 / 6) ** n / n for n in range(1, 100)),
        geometric_polynomial=math.fsum(0.25**n for n in range(3)),
        geometric_error=geometric_tail(2, 0.25),
        derivative_series=math.fsum(n * 0.5 ** (n - 1) for n in range(1, 100)),
        integrated_series=math.fsum(0.5 ** (n + 1) / (n + 1) for n in range(100)),
    )
    add(
        12,
        decay_cubic=math.fsum((-0.4) ** n / math.factorial(n) for n in range(4)),
        decay_bound=0.4**4 / math.factorial(4),
        growth_bound=max(math.exp(i / 2000) for i in range(1001))
        * 0.5**4
        / math.factorial(4),
        sine_polynomial=math.fsum(
            (-1) ** n * 0.6 ** (2 * n + 1) / math.factorial(2 * n + 1) for n in range(3)
        ),
        integrated_bound=integral(lambda x: x**4 / math.factorial(4), 0, 0.4),
        degree_choice=first_certificate(
            lambda n: 0.8 ** (n + 1) / math.factorial(n + 1), 0.0001
        ),
    )
    radial = integral(lambda r: 6 * (1 - r * r / 4) * 2 * math.pi * r, 0, 2)
    disk_area = integral(lambda r: 2 * math.pi * r, 0, 2)
    add(
        13,
        strip_area=integral(lambda x: x - x * x, 0, 1),
        disk_volume=integral(lambda x: math.pi * (x * x) ** 2, 0, 1),
        parametric_length=integral(lambda t: math.hypot(3, 4), 0, 2),
        polar_area=integral(lambda theta: 0.5 * 2**2, 0, math.pi / 2),
        radial_total=radial,
        radial_average=radial / disk_area,
    )
    # Lesson 14: evaluate each limit numerically near the limit point (no L'Hopital step).
    add(
        14,
        lhopital_exp=(math.exp(2e-6) - 1) / math.sin(3e-6),
        lhopital_rational=(5 * 1e6**2 + 2) / (2 * 1e6**2 - 1),
        lhopital_repeat=(1e-3 - math.sin(1e-3)) / 1e-3**3,
        transform_power=(1 + 1e-9) ** (1 / 1e-9),
        transform_product=1e-12 * math.log(1e-12),
    )
    # Lesson 15: Simpson quadrature of each original integrand (no antiderivative). The secant item's
    # endpoint singularity is removed with x = 3 + t^2 rather than a trigonometric substitution.
    add(
        15,
        odd_power=integral(lambda x: math.sin(x) ** 5, 0, math.pi / 2),
        even_power=integral(lambda x: math.sin(x) ** 4, 0, math.pi / 2),
        tangent_integral=integral(math.tan, 0, math.pi / 3),
        sine_substitution=integral(lambda x: math.sqrt(4 - x * x), 0, 1),
        tangent_substitution=integral(lambda x: (1 + x * x) ** -1.5, 0, math.sqrt(3)),
        secant_substitution=integral(
            lambda t: 2 / ((3 + t * t) * math.sqrt(6 + t * t)), 0, math.sqrt(3)
        ),
        completed_square_arctangent=integral(lambda x: 1 / (x * x - 2 * x + 10), 1, 4),
        completed_square_arcsine=integral(lambda x: (3 + 2 * x - x * x) ** -0.5, 1, 2.5),
    )
    _, _, _, nodes, force = lab_data()
    add(
        "lab-01",
        trapezoid=sampled_integral(nodes, force, 1),
        simpson=sampled_integral(nodes, force, 2),
        series_work=integral(
            lambda x: 10 * x * math.fsum((0.2 * x) ** n for n in range(4)), 0, 2
        ),
        tail_bound=integral(lambda x: 10 * x * (0.2 * x) ** 4 / 0.6, 0, 2),
    )
    return answers


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_all_numeric_keys_with_separate_calculations(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(
        EXPECTED[question_id], abs=max(spec["tolerance"], 1e-8), rel=2e-6
    )


def test_numeric_calculation_inventory_is_exhaustive():
    assert set(EXPECTED) == {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 75


CSV_CHECKS = BANK["calculus-2-lab-01:summary"]["solution_spec"]["validation_spec"][
    "checks"
]


@pytest.mark.parametrize("check", CSV_CHECKS, ids=lambda check: check["id"])
def test_upload_keys_recompute_committed_observations(check):
    _, groups, means, _, _ = lab_data()
    values = groups[check["row_id"]]
    expected = (
        len(values) if check["column"] == "replicates" else means[check["row_id"]]
    )
    assert check["answer"] == pytest.approx(expected, abs=check["tolerance"])
    assert check["calculation"]["values"] == values


def correct_option(key):
    question = BANK[key]
    return question["options"][question["solution_spec"]["answer"]]


def test_method_primitives_and_internal_singularity():
    for x in (0.1, 0.7, 1.4):
        h = 1e-5

        def primitive(u):
            return (u - 1) * math.exp(u)

        assert (primitive(x + h) - primitive(x - h)) / (2 * h) == pytest.approx(
            x * math.exp(x), rel=1e-8
        )
    assert correct_option("calculus-2-7:parts-sign") == "(x−1)eˣ+C."
    assert "internal singularity" in correct_option("calculus-2-7:pole")
    # One-sided log magnitudes grow instead of approaching finite limits.
    assert abs(math.log(1e-8)) > abs(math.log(1e-4))
    assert "ordinary improper integral diverges" in correct_option(
        "calculus-2-8:principal-value"
    )


def test_intro_integration_method_choices_and_improper_limits():
    text = (COURSE / "modules/01-integration-techniques-and-improper-integrals.md").read_text(
        encoding="utf-8"
    )
    assert "converges exactly when $p>1$" in text
    assert "finite limit when $p<1$" in text
    assert "tends to zero is insufficient" in text

    substitution_integral = integral(lambda x: 2 * x / (x * x + 3), 0, 2)
    assert substitution_integral == pytest.approx(math.log(7 / 3), abs=1e-9)

    def parts_primitive(x):
        return x * x * math.log(x) / 2 - x * x / 4

    def parts_integrand(x):
        return x * math.log(x)

    for x in (0.1, 0.5, 1.0):
        assert derivative(parts_primitive, x) == pytest.approx(
            parts_integrand(x), abs=1e-8
        )
    assert math.exp(-200) * -100 == pytest.approx(0, abs=1e-80)
    assert integral(lambda x: 1 / ((x + 1) * (x + 3)), 0, 1) == pytest.approx(
        0.5 * math.log(3 / 2), abs=1e-9
    )

    # x=1/u transforms the convergent p=2 tail to a unit-interval integral.
    assert integral(lambda u: 1, 0, 1) == pytest.approx(1)
    assert math.log(1000) > math.log(10)  # the p=1 cutoff keeps growing
    assert integral(lambda t: 4 * math.exp(-2 * t), 0, 20) == pytest.approx(2)


def test_variable_force_work_accumulation_and_direction():
    text = (COURSE / "modules/03-applications-of-integration-work-and-accumulation.md").read_text(
        encoding="utf-8"
    )
    assert "force component along the displacement" in text
    assert "newtons multiplied by metres are joules" in text
    assert integral(lambda x: 4 * x, 0, 3) == pytest.approx(18)
    assert integral(lambda x: 4 * x, 1, 1.1) == pytest.approx(0.42)
    assert integral(lambda x: -4 * x, 0, 3) == pytest.approx(-18)
    # Multiplying the maximum endpoint force by the full distance overcounts.
    assert 12 * 3 == 36 > integral(lambda x: 4 * x, 0, 3)


def test_sequence_series_distinction_and_geometric_error_bound():
    text = (COURSE / "modules/02-sequences-series-and-approximation-error.md").read_text(
        encoding="utf-8"
    )
    assert "necessary condition is not sufficient" in text
    assert "tail after including terms through index $N$" in text
    assert "not a universal error bound" in text
    partial = math.fsum(0.2**n for n in range(3))
    total = 1 / (1 - 0.2)
    tail = 0.2**3 / (1 - 0.2)
    assert partial == pytest.approx(1.24)
    assert total == pytest.approx(1.25)
    assert total - partial == pytest.approx(tail)
    actual_taylor_error = math.exp(0.5) - (1 + 0.5 + 0.5**2 / 2)
    lagrange_bound = math.exp(0.5) * 0.5**3 / math.factorial(3)
    assert actual_taylor_error == pytest.approx(0.0237212707)
    assert 0 < actual_taylor_error < lagrange_bound < 0.0344


def test_taylor_polynomial_error_bound_is_interval_specific():
    text = (COURSE / "modules/04-power-series-and-taylor-error.md").read_text(
        encoding="utf-8"
    )
    assert "$M$ must bound the derivative everywhere" in text
    assert "separate convergence argument" in text
    def polynomial(x):
        return 1 + x + x * x / 2

    for x in (0.2, 0.5):
        actual_error = abs(math.exp(x) - polynomial(x))
        bound = math.exp(x) * abs(x) ** 3 / math.factorial(3)
        assert actual_error <= bound
    assert polynomial(0.2) == pytest.approx(1.22)
    assert polynomial(0.5) == pytest.approx(1.625)


def test_power_criteria_and_zero_term_limit():
    assert "p>1" in correct_option("calculus-2-8:endpoint-rule")
    assert "p<1" in correct_option("calculus-2-8:endpoint-rule")
    # Each dyadic harmonic block adds at least one half despite shrinking terms.
    for k in range(1, 9):
        assert math.fsum(1 / n for n in range(2 ** (k - 1) + 1, 2**k + 1)) >= 0.5
    assert "harmonic series diverges" in correct_option("calculus-2-9:zero-limit")
    assert "inconclusive" in correct_option("calculus-2-9:ratio-one")


def test_truncation_certificates_are_first_sufficient():
    cases = [
        (geometric_tail, 8, 0.001),
        (lambda n: 0.5 ** (n + 1) / (n + 1), 9, 0.0001),
        (lambda n: 1 / (n + 1), 99, 0.01),
        (lambda n: 0.8 ** (n + 1) / math.factorial(n + 1), 6, 0.0001),
    ]
    for bound, index, tolerance in cases:
        assert bound(index) <= tolerance < bound(index - 1)


def test_alternating_actual_errors_and_signs():
    log_error = math.log1p(0.5) - EXPECTED["calculus-2-10:log-partial"]
    assert 0 < log_error < EXPECTED["calculus-2-10:log-bound"]
    atan_error = math.atan(0.5) - EXPECTED["calculus-2-10:arctan-partial"]
    assert -EXPECTED["calculus-2-10:arctan-bound"] < atan_error < 0
    assert "Conditionally" in correct_option("calculus-2-10:conditional")
    assert "decreasing to zero" in correct_option("calculus-2-10:decrease")


def test_power_series_endpoints_and_operation_domains():
    assert correct_option("calculus-2-11:endpoints").startswith("[−1,5)")
    assert "Inside the radius" in correct_option("calculus-2-11:operation")
    assert "function is finite but this series diverges" in correct_option(
        "calculus-2-11:outside"
    )
    # At x=3 the geometric terms grow, despite the rational value being finite.
    assert (3 / 2) ** 20 > (3 / 2) ** 10
    assert 1 / (1 - 3 / 2) == -2
    # Differentiation changes the integrated logarithm's left endpoint behavior.
    assert abs((-1) ** 1000) == 1
    assert 1 / 1000 < 1 / 100


def test_taylor_bounds_include_actual_and_accumulated_errors():
    assert (
        abs(math.exp(-0.4) - EXPECTED["calculus-2-12:decay-cubic"])
        < EXPECTED["calculus-2-12:decay-bound"]
    )
    growth_cubic = math.fsum(0.5**n / math.factorial(n) for n in range(4))
    assert abs(math.exp(0.5) - growth_cubic) < EXPECTED["calculus-2-12:growth-bound"]
    polynomial_integral = integral(
        lambda x: math.fsum((-x) ** n / math.factorial(n) for n in range(4)), 0, 0.4
    )
    actual_integral = integral(lambda x: math.exp(-x), 0, 0.4)
    assert (
        0
        < actual_integral - polynomial_integral
        < EXPECTED["calculus-2-12:integrated-bound"]
    )
    assert "actual error might still be smaller" in correct_option(
        "calculus-2-12:certificate"
    )


def test_radial_case_and_parameter_multiplicity():
    # A different substitution s=r²/R² gives the same radial half factor.
    transformed = 6 * math.pi * 4 * integral(lambda s: 1 - s, 0, 1)
    assert transformed == pytest.approx(EXPECTED["calculus-2-13:radial-total"])
    assert 6 * math.pi * 4 == pytest.approx(2 * transformed)
    assert integral(lambda t: 2, 0, 4 * math.pi) == pytest.approx(8 * math.pi)
    assert "Two traversals" in correct_option("calculus-2-13:traversal")
    assert "Amount per length" in correct_option("calculus-2-13:density-units")
    assert integral(lambda t: t * 2 * t, 0, 1) == pytest.approx(2 / 3)


def test_lab_data_construction_offset_and_error_separation():
    rows, groups, means, nodes, corrected = lab_data()
    assert len(rows) == 15 and all(len(values) == 3 for values in groups.values())
    for row in rows:
        x = float(row["metres"])
        center = round(10 * x / (1 - 0.2 * x) + 1, 4)
        delta = (int(row["replicate"]) - 2) * 0.05
        assert float(row["force_N"]) == pytest.approx(center + delta, abs=1e-10)
        assert float(row["offset_N"]) == 1
    raw = [means[key] for key in groups]
    for degree in (1, 2):
        assert sampled_integral(nodes, raw, degree) - sampled_integral(
            nodes, corrected, degree
        ) == pytest.approx(2)
    exact = integral(lambda x: 10 * x / (1 - 0.2 * x), 0, 2)
    tail = integral(lambda x: 10 * x * (0.2 * x) ** 4 / (1 - 0.2 * x), 0, 2)
    assert exact - EXPECTED["calculus-2-lab-01:series-work"] == pytest.approx(tail)
    assert 0 < tail < EXPECTED["calculus-2-lab-01:tail-bound"]
    assert EXPECTED["calculus-2-lab-01:trapezoid"] > exact
    assert abs(EXPECTED["calculus-2-lab-01:simpson"] - exact) < 0.006


def test_schedule_and_partial_status():
    manifest = load(COURSE / "course.json")
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert (
        manifest["maturity"] == "partial"
        and manifest["review"]["status"] == "unreviewed"
    )
    assert manifest["grading_policy"]["mode"] == "formative-only"
    lessons = {
        lesson["id"] for module in manifest["modules"] for lesson in module["lessons"]
    }
    weeks = manifest["duration"]["weeks"]
    assert [week["week"] for week in weeks] == list(range(1, 15))
    assert {lesson for week in weeks for lesson in week["lesson_ids"]} == lessons
    assert weeks[-1]["assessment_ids"] == [
        "calculus-2-week14-force-lab",
        "calculus-2-case",
    ]
    assert len(lessons) == 16 and len(BANK) == 113
    cards = len(load(COURSE / "question-banks/retrieval-cards.json")["cards"])
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert (
        f"There are {len(lessons)} readings, {len(BANK)} public practice items and {cards} retrieval cards"
        in syllabus
    )
    assert "Weeks 1, 4, 7 and 10 also have expanded readings" in syllabus


def test_trigonometric_integration_lesson_statements_match_quadrature():
    text = (COURSE / "modules/15-trigonometric-integrals-substitution-and-completing-the-square.md").read_text(
        encoding="utf-8"
    )
    statements = {
        "**2/15 ≈ 0.1333**": integral(lambda x: math.sin(x) ** 3 * math.cos(x) ** 2, 0, math.pi / 2),
        "**π/16 ≈ 0.1963**": integral(lambda x: (math.sin(x) * math.cos(x)) ** 2, 0, math.pi / 2),
        "ln √2 ≈ 0.3466": integral(math.tan, 0, math.pi / 4),
        "ln(1 + √2) ≈ **0.8814**": integral(lambda x: 1 / math.cos(x), 0, math.pi / 4),
        "**9π/4 ≈ 7.069**": integral(lambda x: math.sqrt(max(0.0, 9 - x * x)), 0, 3, panels=200000),
        "**√2/2 ≈ 0.7071**": integral(lambda x: (1 + x * x) ** -1.5, 0, 1),
        "2/√2 ≈ 1.414": integral(lambda x: (1 + x * x) ** -1.5, -1, 1),
        "**π/6 ≈ 0.5236**": integral(lambda t: 2 / ((2 + t * t) * math.sqrt(4 + t * t)), 0, math.sqrt(2)),
        "**π/12 ≈ 0.2618**": integral(lambda x: 1 / (x * x + 4 * x + 13), -2, 1),
        "9 (π/12 − √3/8) ≈ **0.4076**": integral(lambda x: x * x / math.sqrt(9 - x * x), 0, 1.5),
    }
    for fragment, value in statements.items():
        assert fragment in text, fragment
        stated = float(fragment.replace("**", "").split("≈")[-1].strip())
        assert stated == pytest.approx(value, abs=6e-4), (fragment, value)
    assert integral(lambda x: (5 + 4 * x - x * x) ** -0.5, 2, 3.5) == pytest.approx(math.pi / 6, abs=1e-9)
    assert integral(lambda x: math.sin(x) ** 2, 0, math.pi) == pytest.approx(math.pi / 2, abs=1e-9)
    assert integral(lambda x: math.tan(x) / math.cos(x) ** 2, 0, math.pi / 4) == pytest.approx(0.5, abs=1e-9)
