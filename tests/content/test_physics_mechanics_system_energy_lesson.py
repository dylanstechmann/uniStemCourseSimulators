"""Physics: Mechanics 0.7.0 center-of-mass, parallel-axis and system-energy lesson: stated numbers, schedule, comparators.

Each number the reading states is recomputed here from mass-weighted sums, thin-slice sums and a time-stepped swing, not
read from the lesson. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-mechanics"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
READING = (COURSE / "modules/22-center-of-mass-parallel-axes-and-system-energy.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
G = 9.81


def stated(*phrases):
    missing = [phrase for phrase in phrases if phrase not in READING]
    assert not missing, missing


def slices(function, lower, upper, pieces=4000):
    step = (upper - lower) / pieces
    return math.fsum(function(lower + (i + 0.5) * step) * step for i in range(pieces))


def test_center_of_mass_of_discrete_and_continuous_systems():
    masses, positions = [2.0, 1.2, 0.4], [0.15, 0.40, 0.60]
    limb = sum(m * x for m, x in zip(masses, positions)) / sum(masses)
    density = lambda x: 1.5 + 2 * x  # noqa: E731
    total = slices(density, 0, 1.0)
    rod = slices(lambda x: x * density(x), 0, 1.0) / total
    assert limb == pytest.approx(0.28333, abs=1e-5) and total == pytest.approx(2.5) and rod == pytest.approx(0.56667, abs=1e-5) and rod > 0.5
    stated(f"x_cm = (2.0·0.15 + 1.2·0.40 + 0.4·0.60)/3.6 = 1.02/3.6 = {limb:.3f} m", f"M = 1.5 + 1.0 = {total:.1f} kg", f"x_cm = (0.75 + 0.667)/2.5 = {rod:.3f} m")


def test_motion_of_the_center_of_mass_with_a_spring_and_with_skaters():
    # Two blocks and a spring: integrate the coupled motion and read the center-of-mass acceleration from v_cm.
    def derivative(state):
        x1, v1, x2, v2 = state
        spring = 50.0 * (x2 - x1 - 1.0)
        return [v1, spring / 2.0, v2, (16.0 - spring) / 6.0]

    state, dt = [0.0, 0.0, 1.0, 0.0], 1e-4
    for _ in range(5000):
        k1 = derivative(state)
        k2 = derivative([s + dt * k / 2 for s, k in zip(state, k1)])
        k3 = derivative([s + dt * k / 2 for s, k in zip(state, k2)])
        k4 = derivative([s + dt * k for s, k in zip(state, k3)])
        state = [s + dt * (a + 2 * b + 2 * c + d) / 6 for s, a, b, c, d in zip(state, k1, k2, k3, k4)]
    assert (2.0 * state[1] + 6.0 * state[3]) / 8.0 / 0.5 == pytest.approx(2.0, abs=1e-6)
    v2 = -60.0 * -2.0 / 40.0
    after = (60.0 * (0.0 - 2.0) + 40.0 * (1.0 + v2)) / 100.0
    assert v2 == pytest.approx(3.0) and after == pytest.approx(0.4) and (40.0 * 1.0) / 100.0 == pytest.approx(0.4)
    stated("a_cm = 16/8.0 = 2.0 m/s²", "x_cm = 40/100 = 0.40 m", "+3.0 m/s", "−2.0 m and 4.0 m", "(60·(−2.0) + 40·4.0)/100 = 0.40 m")


def test_center_of_mass_frame_energy_split_and_collision():
    m1, m2, u1 = 2.0, 1.0, 3.0
    vcm = m1 * u1 / (m1 + m2)
    total, moving, relative = 0.5 * m1 * u1**2, 0.5 * (m1 + m2) * vcm**2, 0.5 * (m1 * m2 / (m1 + m2)) * u1**2
    after_elastic = (2 * vcm - u1, 2 * vcm - 0.0)
    assert (vcm, total, moving, relative) == pytest.approx((2.0, 9.0, 6.0, 3.0)) and total == pytest.approx(moving + relative)
    assert after_elastic == pytest.approx((1.0, 4.0)) and m1 * after_elastic[0] + m2 * after_elastic[1] == pytest.approx(6.0)
    assert 0.5 * m1 * after_elastic[0] ** 2 + 0.5 * m2 * after_elastic[1] ** 2 == pytest.approx(9.0)
    stated("v_cm = 6.0/3.0 = 2.0 m/s", "½·2.0·3.0² = 9.0 J", "½·3.0·2.0² = 6.0 J", "K_rel = ½(2/3)(3.0²) = 3.0 J", "v₁′ = 2v_cm − v₁ = 1.0 m/s", "v₂′ = 2v_cm − 0 = 4.0 m/s", "6.0 kg·m/s", "9.0 J")


def test_parallel_axis_theorem_by_direct_summation():
    mass, length, pieces = 0.80, 0.50, 4000
    positions = [(i + 0.5) * length / pieces for i in range(pieces)]
    element = mass / pieces
    center = math.fsum(element * x for x in positions) / mass
    about_center = math.fsum(element * (x - center) ** 2 for x in positions)
    about_end = math.fsum(element * x * x for x in positions)
    assert about_center == pytest.approx(mass * length**2 / 12, rel=1e-6) and about_end == pytest.approx(about_center + mass * (length / 2) ** 2, rel=1e-6)
    assert about_end == pytest.approx(4 * about_center, rel=1e-6)
    # a two-mass body checks I = I_cm + M d^2 with the axis shifted perpendicular to the line of the masses
    a, d = math.sqrt(0.30 / 4.0), 0.25
    assert 2 * 2.0 * a * a == pytest.approx(0.30) and 2 * 2.0 * (a * a + d * d) == pytest.approx(0.30 + 4.0 * d * d)
    assert (round(about_center, 5), round(about_end, 5)) == (0.01667, 0.06667)
    stated("I_cm = 0.01667 kg·m² and I_end = 0.06667 kg·m²", "four times the center value", "I = ML²/12 + M(L/2)² = ML²/3", "(3/2)MR²",
           "summing 4000 thin slices numerically gives the same two values")


def test_rolling_energy_and_the_contact_point_check():
    mass, radius, speed = 2.0, 0.10, 1.5
    omega = speed / radius
    density = mass / (math.pi * radius**2)
    rings = 400
    kinetic = 0.0
    for i in range(rings):
        r = (i + 0.5) * radius / rings
        for j in range(rings):
            angle = (j + 0.5) * 2 * math.pi / rings
            x, y = r * math.cos(angle), r * math.sin(angle)
            vx, vy = speed + omega * y, -omega * x  # clockwise spin about the center for rolling to the right
            kinetic += 0.5 * density * (vx * vx + vy * vy) * r * (radius / rings) * (2 * math.pi / rings)
    assert kinetic == pytest.approx(3.375, rel=1e-5) and 0.75 * mass * speed**2 == pytest.approx(3.375)
    assert 0.5 * (1.5 * mass * radius**2) * omega**2 == pytest.approx(3.375)
    stated("½·2.0·1.5² = 2.25 J", "½(½MR²)ω² = ½(0.0100)(225) = 1.125 J", "K = 3.375 J = ¾Mv_cm²", "One third of the energy is rotational", "I_contact = ½MR² + MR² = (3/2)MR²")


def test_pivoted_rod_worked_example_with_a_time_stepped_swing():
    mass, length = 0.80, 0.50
    about_end = mass * length**2 / 3
    released = mass * G * length / 2
    omega = math.sqrt(2 * released / about_end)
    angle, rate, dt = 0.0, 0.0, 1e-5
    while angle < math.pi / 2:
        rate += mass * G * (length / 2) * math.cos(angle) / about_end * dt
        angle += rate * dt
    assert rate == pytest.approx(omega, rel=2e-4)
    split = 0.5 * mass * (omega * length / 2) ** 2 + 0.5 * (mass * length**2 / 12) * omega**2
    assert split == pytest.approx(released)
    stated(
        "I_cm = ML²/12 = 0.01667 kg·m²", "I_pivot = 0.01667 + 0.80·(0.25)² = 0.06667 kg·m²", f"Mg(L/2) = 0.80·9.81·0.25 = {released:.3f} J",
        f"ω = √(2·1.962/0.06667) = {omega:.3f} rad/s", f"v_cm = ωL/2 = {omega * length / 2:.3f} m/s", f"ωL = {omega * length:.3f} m/s",
        f"½·0.80·1.918² = {0.5 * mass * (omega * length / 2) ** 2:.4f} J", f"½·0.01667·7.672² = {0.5 * (mass * length**2 / 12) * omega**2:.4f} J",
    )
    worked = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == "physics-mechanics-22")["worked_example"]
    for phrase in ("ω = 7.672 rad/s", "1.918 m/s", "3.836 m/s", "1.4715 + 0.4905 = 1.962 J"):
        assert phrase in worked


def test_lesson_is_scheduled_after_torque_and_rolling_and_links_prerequisites():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[8]["lesson_ids"] == ["physics-mechanics-10", "physics-mechanics-22", "physics-mechanics-16", "physics-mechanics-17"]
    assert weeks[8]["assessment_ids"][1] == "physics-mechanics-22-practice"
    for target in ("03-momentum-collisions-and-impulse.md", "09-work-momentum-and-system-boundaries.md", "10-torque-angular-momentum-and-rolling.md"):
        assert f"]({target})" in READING
    for target in ("calculus-2/modules/22-averages-weighted-averages-and-probability-densities.md", "calculus-3/modules/23-mass-average-value-and-moments-of-inertia.md"):
        assert f"](../../{target})" in READING
    assert "link-only scope comparators" in READING and "partial, unreviewed and formative-only" in READING and "synthetic" in READING.lower()
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == ("partial", "unreviewed", "formative-only")
    lesson = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == "physics-mechanics-22")
    covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
    assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == 13 and len(lesson["card_ids"]) == 4


def test_crosswalk_records_both_comparators_and_its_limits():
    for phrase in (
        "https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/", "https://oyc.yale.edu/physics/phys-200", "compiled with AI assistance", "not a review by the owner",
        "Week 5 Lesson 17 (\"Center of Mass and Motion of the Center of Mass\")", "Lecture 8 (chapter \"The Center of Mass\")", "Covered in 0.7.0; previously absent",
        "| Gyroscopes | Week 12 deep dive | — | — | Absent; named only by MIT |", "| Waves | — | Lecture 18 (introduction) | — | Absent; named only by Yale |",
        "Elsewhere: the Thermodynamics & Transport course", "Outside this package's boundary", "Local extension", "Absent by policy",
    ):
        assert phrase in CROSSWALK, phrase
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    links = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    assert {link for link in links if not link.startswith("https://")} <= readings | {"labs/01-machine-compliance-and-orientation.md"}
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for sid in ("mech-yale-phys200", "mech-mit-801sc-week5-momentum", "mech-mit-801sc-week10-rotation"):
        assert registry[sid]["reuse_mode"] == "link-only-comparator" and not registry[sid]["permissions"]["quotation"], sid
    assert "physics-mechanics-module-22" in registry["mech-yale-phys200"]["mapped_modules"]


MISCONCEPTIONS = {
    "cm-three-masses": 0.4333,  # the unweighted mean position
    "cm-rod-density": 1.0,  # the geometric midpoint
    "cm-acceleration": 2.667,  # the force on the heavier block alone
    "skater-displacement": 4.9,  # the displacement scaled the wrong way
    "inelastic-loss": 24.0,  # all of the initial energy
    "rod-end-inertia": 0.036,  # the value about the center
    "disk-rim-inertia": 0.05,  # the value about the center
    "parallel-axis-offset": 0.30,  # the center-of-mass value alone
    "rolling-kinetic-energy": 2.25,  # translation only
    "sphere-rotational-fraction": 0.4,  # the inertia coefficient mistaken for the fraction
}


@pytest.mark.parametrize("slug,wrong", MISCONCEPTIONS.items(), ids=list(MISCONCEPTIONS))
def test_numeric_keys_reject_the_named_misconception(slug, wrong):
    item = BANK[f"physics-mechanics-22:{slug}"]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct
