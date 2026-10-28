"""Calculus II 0.7.0 averages, density and probability lesson: stated numbers, schedule and comparator boundary.

Each number the reading states is recomputed here with Simpson quadrature and bisection, not read from the lesson.
Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-2"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
READING = (COURSE / "modules/22-averages-weighted-averages-and-probability-densities.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")


def simpson(f, a, b, n=4000):
    h = (b - a) / n
    return h / 3 * math.fsum((1 if i in (0, n) else 4 if i % 2 else 2) * f(a + i * h) for i in range(n + 1))


def bisection(f, lo, hi):
    flo = f(lo)
    assert flo * f(hi) <= 0
    for _ in range(80):
        mid = (lo + hi) / 2
        if flo * f(mid) <= 0:
            hi = mid
        else:
            lo, flo = mid, f(mid)
    return (lo + hi) / 2


def stated(*phrases):
    missing = [phrase for phrase in phrases if phrase not in READING]
    assert not missing, missing


def test_average_value_and_average_rate_statements():
    f = lambda x: x * x + 1  # noqa: E731
    total = simpson(f, 0, 3)
    average = total / 3
    point = bisection(lambda x: f(x) - average, 0, 3)
    assert total == pytest.approx(12) and average == pytest.approx(4) and point == pytest.approx(math.sqrt(3)) and point != 1.5
    rate = lambda t: 6 * math.exp(-0.5 * t)  # noqa: E731
    uptake = simpson(rate, 0, 4)
    mean_rate = uptake / 4
    crossing = bisection(lambda t: rate(t) - mean_rate, 0, 4)
    assert rate(4) < mean_rate < rate(0) and rate(2) < mean_rate < (rate(0) + rate(4)) / 2
    stated(
        "The integral is 9 + 3 = 12, so f̄ = 12/3 = 4", f"c = √3 = {point:.2f}",
        f"= 12(1 − e^(−2)) = {uptake:.2f} µmol", f"average rate is {uptake:.2f}/4 = {mean_rate:.2f} µmol/min",
        f"6e^(−2) = {rate(4):.2f}", f"t = −2 ln(2.594/6) = {crossing:.2f} min", f"r(2) = {rate(2):.2f}", f"{(rate(0) + rate(4)) / 2:.2f}",
    )


def test_density_totals_and_weighted_position_statements():
    rod = lambda x: 2 + x  # noqa: E731
    mass = simpson(rod, 0, 3)
    weighted = simpson(lambda x: x * rod(x), 0, 3)
    assert mass == pytest.approx(10.5) and weighted == pytest.approx(18) and weighted / mass > 1.5
    cells = simpson(lambda x: 400 * math.exp(-x / 2), 0, 6)
    stated(
        f"M = 6 + 4.5 = {mass:.1f} kg", f"{mass / 3:.1f} kg/m", f"N = 800(1 − e^(−3)) = {cells:.0f} cells",
        "= 9 + 9 = 18", f"x̄ = 18/10.5 = {weighted / mass:.2f} m",
    )


def test_probability_density_statements():
    waiting = lambda t: 0.25 * math.exp(-t / 4)  # noqa: E731
    total = simpson(waiting, 0, 120, 12000)
    below, above = simpson(waiting, 0, 2), 1 - simpson(waiting, 0, 8)
    mean = simpson(lambda t: t * waiting(t), 0, 160, 16000)
    median = bisection(lambda m: simpson(waiting, 0, m, 800) - 0.5, 0.1, 20)
    assert total == pytest.approx(1, abs=1e-8) and mean == pytest.approx(4, abs=1e-5) and median < mean
    assert simpson(lambda x: x * x, 0, 3) == pytest.approx(9)
    stated(
        "∫₀³ kx² dx = 9k, so k = 1/9", f"P(T ≤ 2) = 1 − e^(−0.5) = {below:.3f}", f"P(T > 8) = e^(−2) = {above:.3f}",
        f"m = 4 ln 2 = {median:.2f} min", "total area 2 × 0.5 = 1", "μ = ∫₀^∞ (t/4)e^(−t/4) dt = 4 min",
    )


def test_heavy_tail_examples_diverge_or_converge_as_stated():
    cutoffs = [10.0**k for k in (3, 6, 9)]
    for bound in cutoffs:
        assert 1 - 1 / bound == pytest.approx(1, abs=2e-3)  # the total of 1/x^2 on [1, B]
    means = [math.log(bound) for bound in cutoffs]  # the exact integral of 1/x from 1 to B
    assert means == sorted(means) and means[-1] > 20  # grows without bound
    assert simpson(lambda x: 2 / x**2, 1, 1000, 200000) == pytest.approx(2, abs=2e-3)  # 2/x^3: finite mean 2
    stated("lim (1 − 1/B) = 1", "ln B", "∫₁^∞ 2/x² dx = 2", "p = 1")


def test_bell_curve_values():
    phi = lambda z: math.exp(-z * z / 2) / math.sqrt(2 * math.pi)  # noqa: E731
    values = [simpson(phi, -k, k) for k in (1, 2, 3)]
    assert simpson(phi, -8, 8, 8000) == pytest.approx(1, abs=1e-11)
    stated(
        f"P(−1 ≤ Z ≤ 1) = {values[0]:.4f}, P(−2 ≤ Z ≤ 2) = {values[1]:.4f} and P(−3 ≤ Z ≤ 3) = {values[2]:.4f}",
        f"1/√(2π) = {1 / math.sqrt(2 * math.pi):.3f}",
    )


def test_worked_example_density():
    g = lambda x: (3 / 32) * x * (4 - x)  # noqa: E731
    assert simpson(g, 0, 4) == pytest.approx(1) and simpson(g, 1, 3) == pytest.approx(22 / 32) and simpson(lambda x: x * g(x), 0, 4) == pytest.approx(2)
    median = bisection(lambda m: simpson(g, 0, m, 800) - 0.5, 0.1, 3.9)
    assert median == pytest.approx(2, abs=1e-8) and g(2) == pytest.approx(0.375)
    average = simpson(g, 0, 4) / 4
    assert average == pytest.approx(0.25) and average < g(2)
    stated(
        "= 32 − 64/3 = 32/3", f"(3/32)(9 − 5/3) = 22/32 = {22 / 32:.4f}", "256/3 − 64 = 64/3", f"f(2) = 3·2·2/32 = {g(2):.3f}", "average value of f on [0, 4] is (1/4)∫f = 0.25",
    )
    worked = next(lesson for module in MANIFEST["modules"] for lesson in module["lessons"] if lesson["id"] == "calculus-2-22")["worked_example"]
    assert "22/32 = 0.6875" in worked and "f(2) = 0.375" in worked and "0.25 = 1/4" in worked


def test_lesson_is_scheduled_after_accumulation_and_before_assignment_two():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[6]["lesson_ids"] == ["calculus-2-5", "calculus-2-22", "calculus-2-19"]
    assert weeks[6]["assessment_ids"][1] == "calculus-2-22-practice"
    for target in ("05-integrals-as-accumulation-and-numerical-error.md", "08-improper-integrals-and-comparison.md"):
        assert f"]({target})" in READING
    assert "](../../calculus-3/modules/23-mass-average-value-and-moments-of-inertia.md)" in READING
    assert "](../../statistics/modules/01-probability-distributions-and-sampling.md)" in READING
    assert "link-only scope comparators" in READING and "partial, unreviewed and formative-only" in READING and "synthetic" in READING.lower()
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == ("partial", "unreviewed", "formative-only")
    lesson = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == "calculus-2-22")
    covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
    assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == 13 and len(lesson["card_ids"]) == 4


def test_crosswalk_records_both_comparators_and_its_limits():
    for phrase in (
        "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/syllabus/", "https://abel.math.harvard.edu/archive/1b_spring_04/syllabus.html",
        "compiled with AI assistance", "not a review by the owner", "Unit 3 Part C sessions 60–61", "Covered in 0.7.0; previously absent",
        "| Binomial series | — | Series block, week 9 | — | Absent; named only by Harvard |", "Elsewhere: the Differential Equations course",
        "Elsewhere: the Calculus I course", "Absent by policy",
    ):
        assert phrase in CROSSWALK, phrase
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    links = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    assert {link for link in links if not link.startswith("https://")} <= readings
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for sid in ("calc2-harvard-math1b-2004", "calc2-unit3-averages-probability"):
        assert registry[sid]["reuse_mode"] == "link-only-comparator" and not registry[sid]["permissions"]["quotation"], sid
    assert "calculus-2-module-22" in registry["calc2-harvard-math1b-2004"]["mapped_modules"]


MISCONCEPTIONS = {
    "average-value": 18,  # the integral without dividing by the length
    "average-rate": 24.86,  # the total instead of the average
    "rod-mass": 30,  # the largest density times the length
    "rod-weighted-position": 1.5,  # the midpoint
    "cell-count": 3000,  # the initial density times the length
    "normalizing-constant": 0.3333,  # an integral of x^2 taken as 3
    "interval-probability": 0.6321,  # P(T <= 5), forgetting the lower part
    "density-mean": 1.0,  # the midpoint
    "exponential-median": 5.0,  # the mean 1/rate
    "bell-curve-interval": 0.9332,  # one-sided P(Z <= 1.5)
}


@pytest.mark.parametrize("slug,wrong", MISCONCEPTIONS.items(), ids=list(MISCONCEPTIONS))
def test_numeric_keys_reject_the_named_misconception(slug, wrong):
    item = BANK[f"calculus-2-22:{slug}"]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct
