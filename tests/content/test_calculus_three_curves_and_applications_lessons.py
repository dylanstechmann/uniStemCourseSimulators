"""Calculus III 0.7.0 curve-kinematics and multiple-integral-application lessons: stated numbers, schedule, comparators.

Each number the readings state is recomputed here with finite differences and Simpson quadrature, not read from the
lessons. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-3"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
CURVES = (COURSE / "modules/22-acceleration-curvature-and-swept-area-of-space-curves.md").read_text(encoding="utf-8")
APPLICATIONS = (COURSE / "modules/23-mass-average-value-and-moments-of-inertia.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    return h / 3 * math.fsum((1 if i in (0, n) else 4 if i % 2 else 2) * f(a + i * h) for i in range(n + 1))


def derivative(curve, t, order=1, h=1e-4):
    before, here, after = curve(t - h), curve(t), curve(t + h)
    if order == 1:
        return [(p - m) / (2 * h) for p, m in zip(after, before)]
    return [(p - 2 * c + m) / h**2 for p, c, m in zip(after, here, before)]


def length(vector):
    return math.sqrt(math.fsum(c * c for c in vector))


def dot(u, v):
    return math.fsum(a * b for a, b in zip(u, v))


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])


def kinematics(curve, t):
    v, a = derivative(curve, t), derivative(curve, t, 2)
    tangential = dot(a, v) / length(v)
    normal = math.sqrt(max(length(a) ** 2 - tangential**2, 0.0))
    return v, a, tangential, normal, length(cross(v, a)) / length(v) ** 3


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


def minus(value, digits):
    """Format with the typographic minus the readings use."""
    return f"{value:.{digits}f}".replace("-", "−")


def test_curve_lesson_states_the_computed_kinematics():
    curve = lambda t: (2 * t, t * t, t**3 / 3)  # noqa: E731
    v, a, tangential, normal, kappa = kinematics(curve, 1.0)
    assert length(v) == pytest.approx(3.0) and tangential == pytest.approx(2.0) and normal == pytest.approx(2.0)
    assert simpson(lambda t: length(derivative(curve, t)), 0, 3) == pytest.approx(15.0, abs=1e-6)
    assert [round(c, 3) for c in cross(v, a)] == [2.0, -4.0, 4.0]
    helix = kinematics(lambda t: (3 * math.cos(t), 3 * math.sin(t), 4 * t), 0.4)
    ring = 2.0**2 / 0.5
    stated(
        CURVES,
        "|v|² = 4 + 4t² + t⁴ = (t² + 2)²", "speed is exactly t² + 2 m/s", "= 9 + 6 = 15 m",
        f"speed {length(v):.0f} m/s", f"magnitude 2√2 = {length(a):.2f} m/s²", "d|v|/dt = 2t = 2 m/s² there",
        f"a_N = √(8 − 4) = {normal:.0f} m/s²", f"= (2, {minus(cross(v, a)[1], 0)}, 4), with length {length(cross(v, a)):.0f}",
        f"κ = 6/27 = 2/9 = {kappa:.3f} m⁻¹", f"1/κ = {1 / kappa:.1f} m",
        f"κ = a_N/|v|² = 3/25 = {helix[4]:.2f} m⁻¹", f"a_N = 4/0.5 = {ring:.0f} m/s²",
    )


def test_ellipse_perimeter_curvature_and_bounds():
    ellipse = lambda t: (4 * math.cos(t), 3 * math.sin(t), 0.0)  # noqa: E731
    perimeter = 4 * simpson(lambda t: length(derivative(ellipse, t)), 0, math.pi / 2, 4000)
    ramanujan = math.pi * (3 * 7 - math.sqrt((3 * 4 + 3) * (4 + 3 * 3)))
    assert perimeter == pytest.approx(ramanujan, abs=2e-3) and 2 * math.pi * 3 < perimeter < 2 * math.pi * 4
    long_axis, short_axis = kinematics(ellipse, 0.0)[4], kinematics(ellipse, math.pi / 2)[4]
    assert long_axis == pytest.approx(4 / 9, rel=1e-6) and short_axis == pytest.approx(3 / 16, rel=1e-6)
    constant = {round(cross(derivative(ellipse, t), derivative(ellipse, t, 2))[2], 6) for t in (0.2, 0.9, 2.1)}
    assert constant == {12.0}
    stated(
        CURVES,
        f"**{perimeter:.2f} m**", f"{2 * math.pi * 3:.2f}", f"{2 * math.pi * 4:.2f}", "also gives 22.10",
        f"κ = 12/27 = 4/9 = {long_axis:.3f} m⁻¹", f"radius of curvature is {1 / long_axis:.2f} m",
        f"κ = 12/64 = 3/16 = {short_axis:.4f} m⁻¹", f"radius is {1 / short_axis:.2f} m",
    )


def test_swept_area_is_constant_for_a_central_acceleration():
    orbit = lambda t: (4 * math.cos(2 * t), 3 * math.sin(2 * t), 0.0)  # noqa: E731
    for t in (0.0, 0.4, 1.1):
        r, a = orbit(t), derivative(orbit, t, 2)
        assert [x + 4 * y for x, y in zip(a, r)] == pytest.approx([0, 0, 0], abs=1e-5)
        assert cross(r, derivative(orbit, t))[2] / 2 == pytest.approx(12.0, abs=1e-6)
    assert 12 * math.pi / math.pi == 12
    stated(CURVES, "r × v = (0, 0, 24)", "areal speed is 12 m²/s", "12π/π = 12 m²/s")


def test_cycloid_worked_example_matches_numerical_differentiation():
    radius = 0.3
    cycloid = lambda t: (radius * (t - math.sin(t)), radius * (1 - math.cos(t)), 0.0)  # noqa: E731
    arch = simpson(lambda t: length(derivative(cycloid, t)), 0, 2 * math.pi, 4000)
    quarter, top = kinematics(cycloid, math.pi / 2), kinematics(cycloid, math.pi)
    assert arch == pytest.approx(8 * radius, abs=1e-6)
    assert length(quarter[0]) == pytest.approx(2 * radius * math.sin(math.pi / 4), rel=1e-6)
    assert quarter[2] == pytest.approx(quarter[3], rel=1e-5) and top[2] == pytest.approx(0, abs=1e-6)
    assert 1 / quarter[4] == pytest.approx(4 * radius * math.sin(math.pi / 4), rel=1e-5) and 1 / top[4] == pytest.approx(4 * radius)
    stated(
        CURVES,
        f"8R = {arch:.1f} m", f"The speed is 2R sin(π/4) = {length(quarter[0]):.3f} m/s",
        f"a_T = d|v|/dt = R cos(t/2) = {quarter[2]:.3f} m/s²", f"a_N = √(R² − a_T²) = {quarter[3]:.3f} m/s²",
        f"κ = a_N/|v|² = {quarter[3]:.4f}/0.18 = {quarter[4]:.2f} m⁻¹", f"radius of curvature is {1 / quarter[4]:.3f} m",
        f"speed is 2R = {length(top[0]):.1f} m/s", f"a_N = |a| = {top[3]:.1f} m/s²", f"κ = 0.3/0.36 = {top[4]:.3f} m⁻¹", "radius of curvature is 4R = 1.2 m",
    )


def test_mass_moments_and_average_value_statements():
    rect = lambda x, y: 1 + x / 2  # noqa: E731
    nested = lambda f, x0, x1, y0, y1: simpson(lambda x: simpson(lambda y: f(x, y), y0, y1, 200), x0, x1, 200)  # noqa: E731
    mass = nested(rect, 0, 4, 0, 2)
    xbar = nested(lambda x, y: x * rect(x, y), 0, 4, 0, 2) / mass
    ybar = nested(lambda x, y: y * rect(x, y), 0, 4, 0, 2) / mass
    inertia = nested(lambda x, y: (x * x + y * y) * rect(x, y), 0, 4, 0, 2)
    center_inertia = inertia - mass * (xbar**2 + ybar**2)
    average = simpson(lambda x: simpson(lambda y: x * x + y, 0, x, 200), 0, 2, 200) / 2
    assert mass == pytest.approx(16.0) and xbar == pytest.approx(7 / 3) and ybar == pytest.approx(1.0) and inertia == pytest.approx(128.0, abs=1e-3)
    assert average == pytest.approx(8 / 3, abs=1e-6) and 0 <= average <= 6
    stated(
        APPLICATIONS,
        f"= 2·8 = {mass:.0f} kg", f"x̄ = (112/3)/16 = 7/3 = {xbar:.2f} m", f"ȳ = {ybar:.2f} m", "= 4 + 4/3 = 16/3", f"the average is 8/3 = {average:.2f}",
        f"= 2·(160/3) + 8·(8/3) = {inertia:.0f} kg·m²", "= 49/9 + 1 = 58/9", f"I_cm = 128 − 16·(58/9) = {center_inertia:.1f} kg·m²",
    )


def test_disk_and_solid_statements():
    def polar(fn, radius):
        return simpson(lambda r: simpson(lambda th: fn(r, th) * r, 0, 2 * math.pi, 200), 0, radius, 200)

    k, radius = 12.0, 0.5
    mass, inertia = polar(lambda r, th: k * r, radius), polar(lambda r, th: r * r * k * r, radius)
    assert mass == pytest.approx(math.pi) and inertia == pytest.approx(0.15 * math.pi) and inertia / (mass * radius**2) == pytest.approx(0.6)
    height, cylinder_mass = 0.4, simpson(lambda z: 1000 * (1 + z / 0.4) * math.pi * 0.01, 0, 0.4)
    zbar = simpson(lambda z: z * (1 + z / height), 0, height) / simpson(lambda z: 1 + z / height, 0, height)
    axis_inertia = simpson(lambda z: 1000 * (1 + z / 0.4) * math.pi * 0.1**4 / 2, 0, 0.4)
    assert zbar == pytest.approx(5 * height / 9) and axis_inertia == pytest.approx(0.5 * cylinder_mass * 0.01)
    stated(
        APPLICATIONS,
        f"= π = {mass:.2f} kg", f"0.15π = {inertia:.3f} kg·m²", "I/(MR²) = 0.6", f"1000·π·0.01·0.6 = {cylinder_mass:.2f} kg",
        f"5h/9 = {zbar:.3f} m", f"= {axis_inertia:.4f} kg·m²",
    )


def test_semicircular_plate_worked_example():
    radius, mass = 0.6, 5.0
    density = 2 * mass / (math.pi * radius**2)
    first_moment = simpson(lambda th: simpson(lambda r: r * math.sin(th) * density * r, 0, radius, 200), 0, math.pi, 200)
    ybar = first_moment / mass
    inertia = simpson(lambda th: simpson(lambda r: r * r * density * r, 0, radius, 200), 0, math.pi, 200)
    assert ybar == pytest.approx(4 * radius / (3 * math.pi), rel=1e-9) and inertia == pytest.approx(0.5 * mass * radius**2)
    stated(
        APPLICATIONS,
        f"= 10/(π·0.36) = {density:.2f} kg/m²", f"= 2.4/9.42 = {ybar:.3f} m", f"= {inertia:.2f} kg·m²",
        f"= 0.90 − 5.0·(0.2546)² = 0.90 − 0.324 = {inertia - mass * ybar**2:.3f} kg·m²",
    )
    worked = {lesson["id"]: lesson["worked_example"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    stated(worked["calculus-3-23"], "0.255 m", "0.90 kg·m²", "0.576 kg·m²")
    stated(worked["calculus-3-22"], "8R = 2.4 m", "0.849 m", "4R = 1.2 m")


def test_lessons_are_scheduled_beside_their_prerequisites():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[2]["lesson_ids"] == ["calculus-3-7", "calculus-3-22"]
    assert weeks[9]["lesson_ids"] == ["calculus-3-10", "calculus-3-23", "calculus-3-17"]
    assert "calculus-3-22-practice" in weeks[2]["assessment_ids"] and "calculus-3-23-practice" in weeks[9]["assessment_ids"]
    assert "](07-vectors-planes-and-spatial-curves.md)" in CURVES and "](10-multiple-integrals-and-jacobian-measures.md)" in APPLICATIONS
    for text in (CURVES, APPLICATIONS):
        assert "link-only scope comparators" in text and "https://abel.math.harvard.edu/~knill/teaching/summer2003/syllabus.html" in text
        assert "partial, unreviewed and formative-only" in text and "synthetic" in text.lower()
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == ("partial", "unreviewed", "formative-only")
    for n in (22, 23):
        lesson = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == f"calculus-3-{n}")
        covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
        assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == 13 and len(lesson["card_ids"]) == 4


def test_crosswalk_records_both_comparators_and_its_limits():
    stated(
        CROSSWALK,
        "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/syllabus/",
        "https://abel.math.harvard.edu/~knill/teaching/summer2003/syllabus.html", "compiled with AI assistance", "not a review by the owner",
        "seven-week summer course", "Unit 1 Part C session 19 (acceleration)", "Covered in 0.7.0; previously absent; named only by MIT",
        "| Gravitational attraction | Unit 4 Part A session 78 | — | — | Absent; named only by MIT |", "| Parametric surfaces | — | 6 | — | Absent; named only by Harvard |",
        "Elsewhere: the Linear Algebra course", "Absent by policy",
    )
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    links = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    assert {link for link in links if not link.startswith("https://")} <= readings | {"labs/01-boundary-flux-and-balance.md", "assignments/integrative-field-project-guide.md"}
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for sid in ("calc3-harvard-21a-2003", "calc3-unit1-parametric-curves", "calc3-unit4-triple-integrals"):
        assert registry[sid]["reuse_mode"] == "link-only-comparator" and not registry[sid]["permissions"]["quotation"], sid
    assert {"calculus-3-module-22", "calculus-3-module-23"} <= set(registry["calc3-harvard-21a-2003"]["mapped_modules"])


MISCONCEPTIONS = {
    "acceleration-magnitude": 12.0,  # only the tangential part
    "tangential-acceleration": 6.0,  # the normal part
    "normal-acceleration": 12.0,  # the tangential part
    "curvature-cross-product": 0.6667,  # |v x a|/|v|^2
    "traced-length": 21.17,  # straight-line displacement
    "ellipse-curvature-long-axis": 0.08,  # the short-axis value
    "ellipse-radius-short-axis": 0.08,  # the curvature, not its reciprocal
    "ellipse-perimeter": 21.99,  # circle of the mean radius
    "centripetal-acceleration": 4.0,  # v/R
    "areal-speed": 36.0,  # without the half
    "plate-mass": 12.0,  # density 2 only
    "plate-y-center": 1.0,  # geometric center
    "triangle-average": 0.6667,  # forgot to divide by the area
    "uniform-disk-inertia": 0.48,  # M R^2
    "weighted-disk-inertia": 0.2545,  # forgot the polar Jacobian
    "weighted-disk-ratio": 0.5,  # the uniform disk
    "parallel-axis": 0.24,  # central axis
    "rectangle-inertia": 12.5,  # axis through a corner
    "cylinder-center-height": 0.3,  # mid-height
    "cylinder-mass": 4.712,  # ignoring the density gradient
}


@pytest.mark.parametrize("slug,wrong", MISCONCEPTIONS.items(), ids=list(MISCONCEPTIONS))
def test_numeric_keys_reject_the_named_misconception(slug, wrong):
    n = 22 if slug in list(MISCONCEPTIONS)[:10] else 23
    item = BANK[f"calculus-3-{n}:{slug}"]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct
