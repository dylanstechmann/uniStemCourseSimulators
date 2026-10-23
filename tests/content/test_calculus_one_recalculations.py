"""Separate numerical checks of authored calculus, not human content review.

No scratchpad imports. Uses numerical differentiation/integration/root finding,
interpolated quadrature and committed CSV values to check public answer keys.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-1"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def derivative(f, x, step=1e-5):
    return (f(x + step) - f(x - step)) / (2 * step)


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


def bisect(f, a, b):
    assert f(a) * f(b) <= 0
    for _ in range(80):
        middle = (a + b) / 2
        if f(a) * f(middle) <= 0:
            b = middle
        else:
            a = middle
    return (a + b) / 2


def inverse_slope(f, b, low, high, step=1e-4):
    """Slope of f's inverse at b from bisection-solved inverse values, not from 1/f'."""

    def inverse(y):
        return bisect(lambda x: f(x) - y, low, high)

    return (inverse(b + step) - inverse(b - step)) / (2 * step)


def compound_limit(n):
    value = 1.0
    for _ in range(n):
        value *= 1 + 1 / n
    return value


def endpoint_rate(first, last, interval):
    # Invert the exponential by root finding, independent of author's log formula.
    return bisect(lambda rate: first * math.exp(-rate * interval) - last, 0, 1)


def lab_groups():
    with (COURSE / "labs/washout-signals.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    groups = {}
    for row in rows:
        groups.setdefault(row["time"], []).append(float(row["signal"]))
    means = {time: math.fsum(values) / len(values) for time, values in groups.items()}
    return rows, groups, means


def expected_answers():
    expected = {}

    def add(lesson, **values):
        expected.update(
            {
                f"calculus-1-{lesson}:{name.replace('_', '-')}": value
                for name, value in values.items()
            }
        )

    add(
        1,
        check=derivative(lambda x: x * x, 3),
        linearization=2 + 0.2 * derivative(math.sqrt, 4),
    )
    add(
        2,
        check=derivative(lambda x: (3 * x + 1) ** 4, 1),
        rate_with_units=derivative(lambda t: 5 * math.exp(-0.2 * t), 2),
    )
    add(3, check=5, constrained_optimization=10 * 10)
    add(
        4,
        check=integral(lambda t: 1.8, 0, 5),
        state_from_rate=2 + integral(lambda t: 3 * t, 0, 4),
    )
    rate = endpoint_rate(1, 0.5, 24)
    # Positive growth is the negative of this same decay magnitude.
    doubling = bisect(lambda t: math.exp(math.log(2.5) / 30 * t) - 2, 0, 100)
    stated_rate = 0.02888

    def logistic(n):
        return stated_rate * n * (1 - n / 1e6)

    peak = bisect(lambda n: derivative(logistic, n, 1), 1, 999999)
    reaching = bisect(
        lambda t: 1e6 / (1 + 9 * math.exp(-stated_rate * t)) - 0.9e6, 0, 300
    )
    add(
        5,
        rate_from_doubling=rate,
        count_at_72h=1e5 * math.exp(stated_rate * 72),
        rate_from_two_counts=doubling,
        max_logistic_rate=logistic(peak),
        time_to_90=reaching,
    )

    def saturation(s):
        return 100 * s / (5 + s)

    add(
        6,
        rate_at_1000=saturation(1000),
        initial_slope=derivative(saturation, 0),
        linear_error=100 * (10 - saturation(0.5)) / saturation(0.5),
        net_change=integral(lambda t: 6 - 2 * t, 0, 5),
        total_moved=integral(lambda t: 6 - 2 * t, 0, 3)
        - integral(lambda t: 6 - 2 * t, 3, 5),
    )
    add(
        7,
        delta=0.1 / 2,
        continuous_hole=4,
        derivative_definition=derivative(lambda x: x * x, 3),
        secant_slope=((3.1) ** 2 - 9) / 0.1,
        sqrt_limit=derivative(math.sqrt, 9),
        slope_step=0.01,
    )

    def response(c):
        return 100 * c / (2 + c)

    def sphere(t):
        return (4 / 3) * math.pi * (2 + 0.1 * t) ** 3

    def cylinder(t):
        return math.pi * (2 + 0.1 * t) ** 2 * (3 - 0.2 * t)

    def circle_branch(x):
        return math.sqrt(25 - x * x)

    add(
        8,
        concentration=1 + 0.5 * 2,
        sensor_time_rate=derivative(lambda t: response(1 + 0.5 * t), 2),
        product_rate=derivative(lambda t: t * t * math.exp(-t), 3),
        implicit_slope=derivative(circle_branch, 3),
        sphere_volume_rate=derivative(sphere, 0),
        cylinder_volume_rate=derivative(cylinder, 0),
    )

    def cubic(x):
        return x**3 - 6 * x * x + 9 * x + 1

    maximum_x = bisect(lambda x: derivative(cubic, x), 0.5, 1.5)

    def surface(r):
        return 2 * math.pi * r * r + 32 * math.pi / r

    radius = bisect(lambda r: derivative(surface, r), 1, 3)
    add(
        9,
        maximum_location=maximum_x,
        maximum_value=max(cubic(0), cubic(maximum_x), cubic(3)),
        inflection=2,
        feasible_cost_minimum=min([0, 1], key=lambda p: 4 * p * p - 12 * p + 15),
        cylinder_radius=radius,
        cylinder_area=surface(radius),
    )

    def flow(t):
        return 6 * t - t * t

    accumulated = integral(flow, 0, 6)

    def upper(t):
        return integral(lambda s: math.exp(-s), 0, t * t)

    def moving(t):
        return integral(lambda s: s * s, t, 2 * t)

    add(
        10,
        accumulation=accumulated,
        average_rate=accumulated / 6,
        moving_upper=derivative(upper, 1),
        moving_both=derivative(moving, 2),
        log_substitution=integral(lambda t: 2 * t / (1 + t * t), 0, 2),
        linear_substitution=integral(lambda s: (2 * s + 1) ** 2, 0, 3),
    )

    def concentration(t):
        return 20 * math.exp(-0.1 * t)

    samples = [(t, concentration(t)) for t in [0, 5, 10, 15, 20]]

    def interpolate(t, degree):
        if degree == 1:
            index = min(int(t / 5), 3)
            pair = samples[index : index + 2]
            (x0, y0), (x1, y1) = pair
            return y0 + (y1 - y0) * (t - x0) / (x1 - x0)
        segment = samples[:3] if t <= 10 else samples[2:]
        result = 0
        for i, (xi, yi) in enumerate(segment):
            product = yi
            for j, (xj, _) in enumerate(segment):
                if i != j:
                    product *= (t - xj) / (xi - xj)
            result += product
        return result

    add(
        11,
        central_h5=integral(lambda t: -2 * math.exp(-0.1 * t), 5, 15) / 10,
        central_h1=integral(lambda t: -2 * math.exp(-0.1 * t), 9, 11) / 2,
        trapezoid=integral(lambda t: interpolate(t, 1), 0, 20),
        simpson=integral(lambda t: interpolate(t, 2), 0, 20),
        trapezoid_bound=20 * 0.2 * 25 / 12,
        noise_bound=(0.02 + 0.02) / 0.2,
    )

    def root_function(x):
        return x * x - 2

    x1 = 1.5 - root_function(1.5) / derivative(root_function, 1.5)
    x2 = x1 - root_function(x1) / derivative(root_function, x1)
    elasticity = 2 / response(2) * derivative(response, 2)
    add(
        12,
        sqrt_linearization=3 + 0.3 * derivative(math.sqrt, 9),
        log_error_bound=0.1 * 0.1 / 2,
        newton_first=x1,
        newton_second=x2,
        elasticity=elasticity,
        relative_response=elasticity * 0.02,
    )

    def sensor(t):
        return concentration(t) + 2

    def mixed(t):
        return 12 * math.exp(-0.2 * t) + 8 * math.exp(-0.05 * t)

    add(
        13,
        log10_slope=abs(
            (math.log10(concentration(10) / 20) - math.log10(concentration(0) / 20))
            / 10
        ),
        half_life=bisect(lambda t: concentration(t) - 10, 0, 20),
        instantaneous_rate=derivative(concentration, 10),
        uncorrected_rate=endpoint_rate(sensor(0), sensor(20), 20),
        corrected_rate=endpoint_rate(sensor(0) - 2, sensor(20) - 2, 20),
        mixed_rate=-derivative(mixed, 10) / mixed(10),
    )
    _, _, means = lab_groups()
    corrected = endpoint_rate(means["t00"] - 2, means["t20"] - 2, 20)
    add(
        "lab-01",
        uncorrected_rate=endpoint_rate(means["t00"], means["t20"], 20),
        corrected_rate=corrected,
        half_life=bisect(lambda t: math.exp(-corrected * t) - 0.5, 0, 20),
        naive_prediction=means["t20"] ** 2 / means["t00"],
    )
    add(14, mvt_c=2, rolle_c=0, rate_bound=0.1)
    add(
        15,
        inverse_slope=inverse_slope(lambda x: x**5 + x, 2, 0, 2),
        arcsine_slope=derivative(math.asin, 0.8),
        general_exponential=derivative(lambda x: 3**x, 2),
        log_chain=derivative(lambda x: math.log(x**3 + 1), 1),
        variable_power=derivative(lambda x: x ** math.sin(x), math.pi / 2),
        log_product_quotient=derivative(
            lambda x: x**2 * (x + 1) ** 3 / math.sqrt(x + 8), 1
        ),
        e_limit_fifty=compound_limit(50),
        ph_sensitivity=0.05 * derivative(lambda c: -math.log10(c), 1.0),
    )
    return expected


EXPECTED = expected_answers()


def test_every_numeric_key_is_recalculated():
    assert set(EXPECTED) == {qid for qid, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 75


@pytest.mark.parametrize("qid,value", sorted(EXPECTED.items()))
def test_numeric_key(qid, value):
    spec = BANK[qid]["solution_spec"]
    tolerance = spec["tolerance"] + spec.get("relative_tolerance", 0) * abs(
        spec["answer"]
    )
    assert abs(value - spec["answer"]) <= tolerance


def lesson_text(number):
    c = load(COURSE / "course.json")
    lesson = next(
        lesson
        for module in c["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == f"calculus-1-{number}"
    )
    return (COURSE / lesson["reading"]).read_text(encoding="utf-8")


def test_inverse_exponential_and_log_lesson_statements_match_numerics():
    text = lesson_text(15)
    assert inverse_slope(lambda x: x**3 + x, 2, 0, 2) == pytest.approx(0.25, abs=1e-6)
    assert round(bisect(lambda x: x**3 + x - 2.001, 0, 2), 6) == 1.00025
    assert round(derivative(lambda x: math.log(x * x + 1), 2), 6) == 0.8
    assert round(derivative(lambda x: 2**x, 3), 3) == 5.545
    assert round(compound_limit(100), 4) == 2.7048
    assert round(math.e - compound_limit(100), 4) == 0.0135 and round(math.e / 200, 4) == 0.0136
    assert round(derivative(math.asin, 0.6), 6) == 1.25 and round(derivative(math.atan, 1), 6) == 0.5
    assert round(derivative(lambda x: x**x, 2), 3) == 6.773

    def y(x):
        return (x + 1) ** 2 * math.sqrt(x + 3) / (x + 2) ** 3

    assert round(y(1), 4) == 0.2963 and round(derivative(y, 1), 4) == 0.037
    assert round(0.10 * derivative(lambda c: -math.log10(c), 1.0), 3) == -0.043
    assert round(-math.log10(1.1), 3) == -0.041
    assert inverse_slope(lambda x: x**3 + 2 * x, 3, 0, 2) == pytest.approx(0.2, abs=1e-6)
    assert round(derivative(lambda x: x**x, 3), 2) == 56.66
    linear, exact = 0.25 * derivative(lambda c: -math.log10(c), 1.0), -math.log10(1.25)
    assert (round(linear, 3), round(exact, 3), round(linear / exact - 1, 2)) == (-0.109, -0.097, 0.12)
    for phrase in (
        "g′(2) = 1/f′(1) = 1/4 = **0.25**",
        "x ≈ 1.000250",
        "which is **0.8** at x = 2",
        "8 ln 2 = **5.545**",
        "the value is **2.7048**, short of e by 0.0135",
        "1/0.8 = **1.25**",
        "4(ln 2 + 1) = **6.773**",
        "0.2963 × 0.125 = **0.0370**",
        "lowers pH by about 0.043",
        "27(1.0986 + 1) = 56.66",
        "overstates the change by about 12%",
    ):
        assert phrase in text, phrase


def test_csv_counts_and_means_against_committed_observations():
    rows, groups, means = lab_groups()
    assert len(rows) == 21 and len(groups) == 7
    assert all(float(row["blank"]) == 2 for row in rows)
    checks = BANK["calculus-1-lab-01:summary"]["solution_spec"]["validation_spec"][
        "checks"
    ]
    assert len(checks) == 14
    for check in checks:
        values = groups[check["row_id"]]
        answer = (
            len(values) if check["column"] == "replicates" else means[check["row_id"]]
        )
        assert check["calculation"]["values"] == values
        assert abs(answer - check["answer"]) <= check["tolerance"]
    assert all(mean > 2 for mean in means.values())


def test_limit_proofs_and_corner_counterexample():
    assert "δ = ε/2" in lesson_text(7)
    for epsilon in [0.1, 0.001, 2]:
        delta = epsilon / 2
        for sign in [-1, 1]:
            x = 3 + sign * 0.9 * delta
            assert abs((2 * x + 1) - 7) < epsilon
    assert abs(-0.1) / (-0.1) == -1 and abs(0.1) / 0.1 == 1
    assert "continuous" in lesson_text(
        7
    ) and "no finite two-sided limit" in lesson_text(7)
    for h in [0.2, -0.2]:
        assert ((3 + h) ** 2 - 9) / h == pytest.approx(6 + h)


def test_intro_limit_table_and_local_approximation_bound():
    text = lesson_text(1)
    assert "punctured neighborhood" in text
    assert "left limit at 2 is 3" in text and "right limit is 6" in text
    assert "|u|\\le25" in text
    for x, expected in [(0.9, 1.9), (0.99, 1.99), (1.01, 2.01), (1.1, 2.1)]:
        assert (x * x - 1) / (x - 1) == pytest.approx(expected)
    second_derivative_bound = 1 / (4 * 75**1.5)
    for h in [4, 20]:
        exact = math.sqrt(100 + h)
        linear = 10 + h / 20
        error = abs(exact - linear)
        assert error <= 0.5 * second_derivative_bound * h**2
    assert 10 + 50 / 20 - math.sqrt(150) == pytest.approx(0.2525512861)


def test_derivative_rules_and_unit_aware_chain_rule():
    text = lesson_text(2)
    assert "(fg)'=f'g+fg'" in text
    assert "Omitting the inner factor" in text
    assert "millimolar units cancel" in text.lower()
    def product(x):
        return x * math.exp(-x)

    assert derivative(product, 1) == pytest.approx(0, abs=1e-9)

    def quotient(x):
        return (x * x + 1) / (x + 1)

    assert derivative(quotient, 2) == pytest.approx(7 / 9, abs=1e-8)
    assert 4 * 4**3 * 3 == 768

    def concentration(t):
        return 4 * math.exp(-0.1 * t)

    def response(t):
        c = concentration(t)
        return 100 * c / (2 + c)

    assert derivative(response, 0) == pytest.approx(-20 / 9, abs=1e-8)
    assert -0.2 * 5 * math.exp(-0.4) == pytest.approx(-0.670320046, abs=1e-9)


def test_optimization_domain_endpoints_and_area_rate():
    text = lesson_text(3)
    assert "open and closed domain matters" in text
    assert "both endpoints" in text and "feasible candidate" in text
    def area(x):
        return x * (10 - x)

    candidates = [area(0), area(5), area(10)]
    assert candidates == [0, 25, 0]
    assert max(candidates) == 25
    # Fixed 10 cm length times a 0.2 cm/s width rate gives cm²/s.
    assert 10 * 0.2 == pytest.approx(2.0)


def test_signed_integral_net_total_change_and_fundamental_theorem():
    text = lesson_text(4)
    assert "Net change and total change answer different questions" in text

    def rate(t):
        return 4 - t

    net_change = integral(rate, 0, 6)
    total_change = integral(lambda t: abs(rate(t)), 0, 4) + integral(
        lambda t: abs(rate(t)), 4, 6
    )
    assert net_change == pytest.approx(6)
    assert total_change == pytest.approx(10)
    assert 12 + net_change == pytest.approx(18)
    def accumulated(t):
        return 4 * t - t * t / 2

    assert derivative(accumulated, 5) == pytest.approx(rate(5), abs=1e-9)
    assert "Any constant added to $A$ cancels" in text


def test_related_rate_worked_numbers_and_vertical_tangent():
    text = lesson_text(8)
    assert "-1.5" in text or "−1.5" in text
    assert "−4.444444" in text and "vertical tangent" in text
    assert derivative(
        lambda t: 100 * (4 * math.exp(-0.2 * t)) / (2 + 4 * math.exp(-0.2 * t)), 0
    ) == pytest.approx(-40 / 9, abs=1e-8)
    assert (3 / 4) * 2 == 1.5
    assert math.sqrt(25 - 5**2) == 0


def test_extrema_inflection_and_feasible_boundary():
    def cubic(x):
        return x**3 - 6 * x * x + 9 * x + 1

    assert [cubic(0), cubic(1), cubic(2), cubic(3)] == [1, 5, 3, 1]
    assert derivative(cubic, 0.5) > 0 and derivative(cubic, 1.5) < 0

    def second(x):
        return (cubic(x + 0.001) - 2 * cubic(x) + cubic(x - 0.001)) / 0.001**2

    assert second(1.5) < 0 and second(2.5) > 0
    assert 2 * math.pi * 4**2 + 2 * math.pi * 4 * 1 == pytest.approx(40 * math.pi)
    assert "both endpoints" in lesson_text(9) and "r ≥ 4" in lesson_text(9)


def test_accumulation_worked_values_and_moving_bounds():
    accumulation = integral(lambda t: 2 * t / (1 + t * t), 0, 2)
    text = lesson_text(10)
    assert f"{4 + accumulation:.6f}" in text and f"{accumulation / 2:.6f}" in text
    assert integral(lambda t: 6 * t - t * t, 0, 3) == pytest.approx(18)
    for t in [1, 2, 3]:
        assert derivative(
            lambda x: integral(lambda s: s * s, x, 2 * x), t
        ) == pytest.approx(7 * t * t, abs=1e-7)


def test_quadrature_bounds_noise_and_example_exactness():
    exact = integral(lambda t: 20 * math.exp(-0.1 * t), 0, 20)
    trap = EXPECTED["calculus-1-11:trapezoid"]
    simpson = EXPECTED["calculus-1-11:simpson"]
    assert 0 < simpson - exact < 0.002 * 20 * 5**4 / 180
    assert 0 < trap - exact < EXPECTED["calculus-1-11:trapezoid-bound"]
    true = -2 / math.e
    assert abs(EXPECTED["calculus-1-11:central-h1"] - true) < abs(
        EXPECTED["calculus-1-11:central-h5"] - true
    )
    # Opposing bounded endpoint errors attain the stated worst-case contribution.
    assert (0.02 - (-0.02)) / (2 * 0.1) == pytest.approx(0.2)
    assert (0 + 4 * 1 + 4) / 3 == pytest.approx(integral(lambda t: t * t, 0, 2))
    text = lesson_text(11)
    for fragment in ["−0.578997", "3.587847", "0.058305", "0.138889"]:
        assert fragment in text


def test_linearization_remainders_newton_and_finite_sensitivity():
    sqrt_error = 3.05 - math.sqrt(9.3)
    assert 0 < sqrt_error < 0.3**2 / 216
    log_error = 0.1 - math.log(1.1)
    assert 0 < log_error < 0.005
    x1, x2 = (
        EXPECTED["calculus-1-12:newton-first"],
        EXPECTED["calculus-1-12:newton-second"],
    )
    assert abs(x2 - math.sqrt(2)) < abs(x1 - math.sqrt(2))
    exact_relative = ((100 * 2.04 / 4.04) - 50) / 50
    assert exact_relative == pytest.approx(0.0099009901)
    assert "0.009901" in lesson_text(12)
    assert any(
        "derivative denominator is zero" in option
        for option in BANK["calculus-1-12:newton-zero"]["options"]
    )


def test_washout_curvature_alternative_model_and_held_out_prediction():
    def signal(t):
        return 20 * math.exp(-0.1 * t) + 2

    def log_signal(t):
        return math.log(signal(t))

    # Positive curvature and flattening can arise from a background alone.
    assert derivative(log_signal, 30) > derivative(log_signal, 10)
    second = (log_signal(10.01) - 2 * log_signal(10) + log_signal(9.99)) / 0.01**2
    assert second > 0
    apparent = EXPECTED["calculus-1-13:uncorrected-rate"]
    predicted = signal(0) * math.exp(-apparent * 40)
    text = lesson_text(13)
    assert f"{predicted:.6f}" in text and f"{signal(40):.6f}" in text
    assert predicted < signal(40)
    assert "Curvature alone does not identify" in text
    assert "no instructor review is claimed" in text


def test_preserved_symbolic_derivative_independently_by_values():
    def function(x):
        return (x * x + 1) / (x + 1)

    def derivative_expression(x):
        return (x * x + 2 * x - 1) / (x + 1) ** 2

    for x in [-3, -0.5, 0, 2, 5]:
        assert derivative(function, x) == pytest.approx(
            derivative_expression(x), abs=1e-7
        )
    spec = BANK["calculus-1-2:symbolic-quotient-derivative"]["solution_spec"]
    assert spec["expression"] == "(x^2 + 2*x - 1)/(x + 1)^2"


def test_schedule_syllabus_and_labels():
    c = load(COURSE / "course.json")
    weeks = c["duration"]["weeks"]
    scheduled = [lid for week in weeks for lid in week["lesson_ids"]]
    lessons = {lesson["id"] for module in c["modules"] for lesson in module["lessons"]}
    # Existing core/lab/project routes plus the new FTC reading and four mixed assignments.
    assert len(weeks) == 14 and len(set(scheduled)) == len(scheduled) == 22
    assert set(scheduled) == lessons
    assert weeks[12]["lesson_ids"] == ["calculus-1-lab-01"]
    assert "calculus-1-case" in weeks[13]["assessment_ids"]
    assert {aid for week in weeks for aid in week["assessment_ids"]} <= {
        a["id"] for a in c["assessments"]
    }
    assert c["maturity"] == "partial" and c["version"] == c["history"][-1]["version"]
    assert (
        c["review"]["status"] == "unreviewed"
        and c["grading_policy"]["mode"] == "formative-only"
    )
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert all(outcome["description"] in syllabus for outcome in c["outcomes"])
    assert f"Version: {c['version']}" in syllabus and "134 public practice items" in syllabus
