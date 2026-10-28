"""Calculus I 0.7.0 trigonometric limits and derivatives lesson: stated numbers, schedule and comparator boundary.

Each number the reading states is recomputed here with central differences and direct evaluation, not read from the
lesson. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-1"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
READING = (COURSE / "modules/21-trigonometric-limits-and-derivatives-of-sine-and-cosine.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")


def slope(f, x, step=1e-5):
    return (f(x + step) - f(x - step)) / (2 * step)


def curvature(f, x, step=1e-4):
    return (f(x + step) - 2 * f(x) + f(x - step)) / step**2


def stated(*phrases):
    missing = [phrase for phrase in phrases if phrase not in READING]
    assert not missing, missing


def minus(value, digits):
    """Format with the typographic minus the reading uses."""
    return f"{value:.{digits}f}".replace("-", "−")


def test_the_limit_table_and_the_squeeze_bounds():
    for h, sine_digits, cosine_digits in ((0.5, 4, 4), (0.1, 4, 4), (0.01, 5, 4), (0.001, 7, 4)):
        assert math.sin(h) < h < math.tan(h) and math.cos(h) < math.sin(h) / h < 1
        stated(f"| {h} | {math.sin(h) / h:.{sine_digits}f} | {minus((math.cos(h) - 1) / h, cosine_digits)} |")
    assert (math.sin(1e-6) / 1e-6, (math.cos(1e-6) - 1) / 1e-6) == pytest.approx((1.0, 0.0), abs=1e-6)
    stated(f"cos 0.5 = {math.cos(0.5):.4f}", f"(sin 0.5)/0.5 = {math.sin(0.5) / 0.5:.4f}")


def test_related_limits_and_the_difference_quotient_identity():
    assert math.sin(3e-5) / 1e-5 == pytest.approx(3.0, abs=1e-6)
    assert (1 - math.cos(1e-3)) / 1e-6 == pytest.approx(0.5, abs=1e-6)
    for x, h in ((0.7, 0.01), (2.0, 0.003)):
        lhs = (math.sin(x + h) - math.sin(x)) / h
        rhs = math.sin(x) * (math.cos(h) - 1) / h + math.cos(x) * math.sin(h) / h
        assert lhs == pytest.approx(rhs, rel=1e-12)
    stated(f"at x = 0.1 the quotient is already {(1 - math.cos(0.1)) / 0.01:.4f}", "sin(3x)/x = 3·sin(3x)/(3x) → 3·1 = 3")


def test_derivatives_of_sine_cosine_and_tangent():
    assert slope(math.sin, 1.0) == pytest.approx(math.cos(1.0), abs=1e-9) and slope(math.cos, 1.0) == pytest.approx(-math.sin(1.0), abs=1e-9)
    assert slope(math.tan, math.pi / 4) == pytest.approx(2.0, abs=1e-8)
    stated(f"slope of the sine of {slope(math.sin, 1.0):.6f}, which equals cos 1", "which is 2 at x = π/4")


def test_pulsatile_flow_slope_and_oscillator_relation():
    flow = lambda t: 5 + 2 * math.sin(2 * math.pi * t / 0.8)  # noqa: E731
    largest = max(slope(flow, i * 0.001) for i in range(800))
    assert largest == pytest.approx(4 * math.pi / 0.8, abs=1e-6)
    peak_time = max(range(800), key=lambda i: flow(i * 0.001)) * 0.001
    assert peak_time == pytest.approx(0.2, abs=1e-9) and slope(flow, peak_time) == pytest.approx(0, abs=1e-6)
    assert slope(flow, 0.0) == pytest.approx(largest, abs=1e-6) and flow(0.0) == pytest.approx(5.0)
    stated(
        "= 15.71 cos(7.854t) mL/s²", f"Aω = {largest:.2f} mL/s²", f"the flow is {flow(0.1):.2f} mL/s and still rising at {slope(flow, 0.1):.2f} mL/s²",
        "(7 mL/s, at t = 0.2 s)",
    )
    signal = lambda t: 3 * math.sin(2 * t)  # noqa: E731
    assert curvature(signal, 0.7) == pytest.approx(-4 * signal(0.7), abs=1e-5)
    stated("x″ = −12 sin 2t = −4x")


def test_degrees_and_small_angle_statements():
    degrees = lambda x: math.sin(math.radians(x))  # noqa: E731
    assert slope(degrees, 0.0) == pytest.approx(math.pi / 180, abs=1e-9)
    at_thirty = slope(degrees, 30.0)
    assert at_thirty == pytest.approx(math.pi / 180 * math.cos(math.radians(30)), abs=1e-9) and 180 / math.pi == pytest.approx(57.3, abs=0.05)
    stated(f"At x = 30° the slope is {at_thirty:.5f} per degree, not 0.866", "factor of 57.3", "\\approx 0.01745\\cos(x^\\circ)")
    errors = [(x, 100 * (x - math.sin(x)) / math.sin(x)) for x in (0.2, 0.5, 1.0)]
    stated(f"{errors[0][1]:.2f}% at x = 0.2, {errors[1][1]:.2f}% at x = 0.5 and {errors[2][1]:.1f}% at x = 1.0")


def test_worked_example_signal():
    signal = lambda t: 10 + 4 * math.sin(0.5 * t - 0.6)  # noqa: E731
    assert slope(signal, 1.2) == pytest.approx(2.0, abs=1e-8) and signal(1.2) == pytest.approx(10.0)
    assert max(slope(signal, i * 0.01) for i in range(1300)) == pytest.approx(2.0, abs=1e-6)
    peak = 2 * (math.pi / 2 + 0.6)
    assert signal(peak) == pytest.approx(14.0) and slope(signal, peak) == pytest.approx(0, abs=1e-7)
    assert curvature(signal, 2.0) == pytest.approx(-0.25 * (signal(2.0) - 10), abs=1e-6)
    stated(
        "S′(t) = 4·0.5·cos(0.5t − 0.6) = 2 cos(0.5t − 0.6)", "so t = 1.2 s", f"S′(2) = 2 cos 0.4 = {slope(signal, 2.0):.3f}",
        f"S″(2) = −sin 0.4 = {minus(curvature(signal, 2.0), 3)}", f"S(2) = 10 + 4 sin 0.4 = {signal(2.0):.3f}",
        f"gives −0.25 × {signal(2.0) - 10:.3f} = {minus(curvature(signal, 2.0), 3)}", f"gives {slope(signal, 2.0):.4f}", "S = 14", f"t = 2(π/2 + 0.6) = {peak:.2f} s",
    )
    worked = next(lesson for module in MANIFEST["modules"] for lesson in module["lessons"] if lesson["id"] == "calculus-1-21")["worked_example"]
    for phrase in ("S′(2) = 2 cos 0.4 = 1.842", "S″(2) = −sin 0.4 = −0.389", "4.34 s"):
        assert phrase in worked


def test_lesson_is_scheduled_after_the_derivative_rules():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[3]["lesson_ids"] == ["calculus-1-2", "calculus-1-21", "calculus-1-17"]
    assert weeks[3]["assessment_ids"][1] == "calculus-1-21-practice"
    for target in ("02-derivative-rules-and-chain-rule.md", "07-limits-continuity-and-derivative-definition.md", "12-local-approximations-newton-and-sensitivity.md"):
        assert f"]({target})" in READING
    assert "](../../differential-equations/modules/02-second-order-systems-and-mechanical-response.md)" in READING
    assert "link-only scope comparators" in READING and "partial, unreviewed and formative-only" in READING and "synthetic" in READING.lower()
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == ("partial", "unreviewed", "formative-only")
    lesson = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == "calculus-1-21")
    covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
    assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == 13 and len(lesson["card_ids"]) == 4


def test_crosswalk_records_both_comparators_and_its_limits():
    for phrase in (
        "https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/syllabus/", "https://abel.math.harvard.edu/archive/1a_spring_05/calendar_mwf.html",
        "compiled with AI assistance", "not a review by the owner", "Unit 1 Part A sessions 7–8", "Covered in 0.7.0; previously absent",
        "Elsewhere: the Calculus II course", "Elsewhere: the Differential Equations course", "Prerequisite review, outside the package", "Absent by policy",
    ):
        assert phrase in CROSSWALK, phrase
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    links = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    assert {link for link in links if not link.startswith("https://")} <= readings
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for sid in ("calc1-harvard-math1a-2005", "calc1-unit1-parta-derivatives"):
        assert registry[sid]["reuse_mode"] == "link-only-comparator" and not registry[sid]["permissions"]["quotation"], sid
    assert "calculus-1-module-21" in registry["calc1-harvard-math1a-2005"]["mapped_modules"]


MISCONCEPTIONS = {
    "sine-multiple-limit": 1.0,  # forgot the factor 5
    "cosine-quadratic-limit": 1.0,  # the wrong power in the denominator
    "trig-derivative-value": -0.232,  # d/dx cos x = +sin x
    "chain-rule-slope": 0.283,  # forgot the inner factor 3
    "tangent-slope": 2.0,  # sec instead of sec squared
    "product-rule-slope": 0.5236,  # only x cos x
    "peak-slope": 1.5,  # the amplitude without omega
    "oscillator-acceleration": 11.6,  # sign dropped
    "degree-slope": 1.0,  # radian formula used for degrees
    "small-angle-error": 0.0429,  # a fraction instead of a percentage
}


@pytest.mark.parametrize("slug,wrong", MISCONCEPTIONS.items(), ids=list(MISCONCEPTIONS))
def test_numeric_keys_reject_the_named_misconception(slug, wrong):
    item = BANK[f"calculus-1-21:{slug}"]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct
