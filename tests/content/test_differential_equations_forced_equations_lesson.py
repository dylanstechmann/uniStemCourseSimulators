"""Differential Equations 0.7.0 forced-linear-equations lesson: stated numbers, schedule and comparator boundary.

Particular solutions are checked by substituting them back with finite differences, and the worked example by
integrating the equation from rest, not by reading the lesson. Same-AI checks, not human review.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/differential-equations"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
READING = (COURSE / "modules/23-forced-linear-equations-exponential-response-and-undetermined-coefficients.md").read_text(encoding="utf-8")
RESONANCE = (COURSE / "modules/08-resonance-and-damping-of-a-spring-mass-damper.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")


def operator(coefficients, x, t, h=1e-4):
    a2, a1, a0 = coefficients
    return a2 * (x(t + h) - 2 * x(t) + x(t - h)) / h**2 + a1 * (x(t + h) - x(t - h)) / (2 * h) + a0 * x(t)


def from_rest(m, c, k, force, omega, t_end, dt=1e-4):
    """RK4 states of m x'' + c x' + k x = force cos(omega t) from rest."""
    def rhs(t, s):
        return s[1], (force * math.cos(omega * t) - c * s[1] - k * s[0]) / m

    t, s, out = 0.0, (0.0, 0.0), [(0.0, 0.0, 0.0)]
    for _ in range(round(t_end / dt)):
        k1 = rhs(t, s)
        k2 = rhs(t + dt / 2, (s[0] + dt * k1[0] / 2, s[1] + dt * k1[1] / 2))
        k3 = rhs(t + dt / 2, (s[0] + dt * k2[0] / 2, s[1] + dt * k2[1] / 2))
        k4 = rhs(t + dt, (s[0] + dt * k3[0], s[1] + dt * k3[1]))
        s = (s[0] + dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6, s[1] + dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6)
        t += dt
        out.append((t, s[0], s[1]))
    return out


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


@pytest.mark.parametrize(
    "coefficients,solution,forcing",
    [
        ([1, 3, 2], lambda t: 3 * math.exp(-3 * t), lambda t: 6 * math.exp(-3 * t)),
        ([1, 3, 2], lambda t: 2 * t - 2, lambda t: 4 * t + 2),
        ([1, 3, 2], lambda t: 5 * t * math.exp(-t), lambda t: 5 * math.exp(-t)),
        ([1, 3, 2], lambda t: 3 * math.exp(-3 * t) + 3 * math.exp(-t) - 6 * math.exp(-2 * t), lambda t: 6 * math.exp(-3 * t)),
        ([1, 0, 16], lambda t: 0.1 * t * math.sin(4 * t), lambda t: 0.8 * math.cos(4 * t)),
    ],
    ids=["exponential", "polynomial", "resonant", "initial-fit", "pure-resonance"],
)
def test_each_stated_solution_satisfies_its_equation(coefficients, solution, forcing):
    for t in (0.3, 1.1, 2.7):
        assert operator(coefficients, solution, t) == pytest.approx(forcing(t), abs=1e-5)


def test_initial_fit_and_stated_particular_solutions_appear():
    full = lambda t: 3 * math.exp(-3 * t) + 3 * math.exp(-t) - 6 * math.exp(-2 * t)  # noqa: E731
    assert full(0) == pytest.approx(0, abs=1e-12)
    assert (full(1e-6) - full(-1e-6)) / 2e-6 == pytest.approx(0, abs=1e-6)
    stated(READING, "p(−3) = 9 − 9 + 2 = 2, so x_p = 3e^(−3t)", "c₁ = 3 and c₂ = −6", "a = 2, b = −2, and x_p = 2t − 2",
           "x_p = 5t e^(−t)", "= 0.1 t sin 4t")


def test_complex_replacement_reproduces_the_resonance_lesson_values():
    at_resonance = complex(80 - 0.2 * 20**2, 1.2 * 20)
    off_resonance = complex(80 - 0.2 * 10**2, 1.2 * 10)
    assert at_resonance == pytest.approx(24j)
    stated(READING, f"0.5/24 m = {0.5 / abs(at_resonance) * 1000:.2f} mm with a {math.degrees(cmath.phase(at_resonance)):.0f}° lag",
           f"giving {0.5 / abs(off_resonance) * 1000:.2f} mm and an {math.degrees(cmath.phase(off_resonance)):.1f}° lag")
    assert f"**{0.5 / abs(at_resonance) * 1000:.2f} mm**" in RESONANCE  # the value the resonance lesson states


def test_worked_example_matches_an_integration_from_rest():
    m, c, k, force, omega = 0.5, 2.0, 50.0, 1.0, 8.0
    gain = complex(k - m * omega**2, c * omega)
    amplitude, lag = force / abs(gain), cmath.phase(gain)
    alpha, damped = c / (2 * m), math.sqrt(k / m - (c / (2 * m)) ** 2)
    a = -amplitude * math.cos(lag)
    b = (alpha * a - amplitude * omega * math.sin(lag)) / damped
    closed = lambda t: amplitude * math.cos(omega * t - lag) + math.exp(-alpha * t) * (a * math.cos(damped * t) + b * math.sin(damped * t))  # noqa: E731
    trajectory = from_rest(m, c, k, force, omega, 4.0)
    for t, x, _ in trajectory[::5000]:
        assert x == pytest.approx(closed(t), abs=1e-8)
    late = max(abs(x) for t, x, _ in trajectory if t > 3.2)
    assert late == pytest.approx(amplitude, rel=1e-3)
    zeta, ratio = c / (2 * math.sqrt(k * m)), omega / math.sqrt(k / m)
    assert (force / k) / math.sqrt((1 - ratio**2) ** 2 + (2 * zeta * ratio) ** 2) == pytest.approx(amplitude)
    stated(
        READING,
        f"= 18 + j16, so |p(j8)| = √580 = {abs(gain):.2f} N/m and the lag is arctan(16/18) = {math.degrees(lag):.1f}°",
        f"an amplitude of {amplitude * 1000:.1f} mm", "ζ = 2.0/(2√(50 × 0.5)) = 0.2 and r = 0.8",
        f"roots are −2 ± j{damped:.2f}", f"A = −{abs(a) * 1000:.1f} mm and B = −{abs(b) * 1000:.1f} mm",
        f"falls to {100 * math.exp(-alpha * 2.5):.1f}% of its starting size by 2.5 s",
    )


def test_lesson_is_scheduled_between_the_characteristic_equation_and_resonance():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[4]["lesson_ids"] == ["differential-equations-2", "differential-equations-23"]
    assert "differential-equations-23-practice" in weeks[4]["assessment_ids"]
    assert weeks[5]["lesson_ids"] == ["differential-equations-8"]
    for target in ("02-second-order-systems-and-mechanical-response.md", "08-resonance-and-damping-of-a-spring-mass-damper.md",
                   "14-laplace-transform-initial-value-problems.md"):
        assert f"]({target})" in READING
    assert "j" in READING and "e^(jθ) = cos θ + j sin θ" in READING
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == (
        "partial", "unreviewed", "formative-only")


def test_crosswalk_records_both_comparators_and_its_title_level_limits():
    stated(
        CROSSWALK,
        "https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/",
        "https://people.math.harvard.edu/archive/21b_spring_15/syllabus.html", "compiled with AI assistance",
        "not a review by the owner", "first 24 lectures on linear algebra",
        "| Exponential response, undetermined coefficients, operators and pure resonance | II: Exponential Response, Undetermined Coefficients, Linear Operators, Pure Resonance | 29 |",
        "| Partial differential equations (heat and wave) | — | 32–33 | — | Absent; named only by Harvard 21b |",
        "Absent by policy",
    )
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    links = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    assert {link for link in links if not link.startswith("https://")} <= readings
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    harvard = registry["de-harvard-math21b-2015"]
    assert harvard["reuse_mode"] == "link-only-comparator" and not harvard["permissions"]["quotation"]
    assert "differential-equations-module-23" in harvard["mapped_modules"]


MISCONCEPTIONS = {
    "erf-coefficient": 10,  # forcing amplitude without dividing by p(r)
    "complex-amplitude": 2.0,  # dividing by the constant term only
    "complex-phase": 14.04,  # the complement of the lag angle
    "polynomial-constant": 1,  # sign of b
    "resonant-coefficient": 10,  # forcing amplitude without p'(r)
    "pure-resonance-envelope": 8.0,  # 6t/3 instead of 6t/(2·3)
    "initial-condition-constant": -2,  # the other constant
    "steady-amplitude": 20.0,  # static deflection F/k
}


@pytest.mark.parametrize("slug,wrong", MISCONCEPTIONS.items(), ids=list(MISCONCEPTIONS))
def test_numeric_keys_reject_the_named_misconception(slug, wrong):
    item = BANK[f"differential-equations-23:{slug}"]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct
