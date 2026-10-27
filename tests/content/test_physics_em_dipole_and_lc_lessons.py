"""Physics II: E&M 0.7.0 dipole and LC/RLC lessons: stated numbers, schedule and comparator boundary.

The numbers each reading states are recomputed here from two-charge superposition and from stepping the
series-loop equation, not read from the lesson. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-em"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
DIPOLE = (COURSE / "modules/24-electric-dipoles-fields-torque-energy-and-force.md").read_text(encoding="utf-8")
LC = (COURSE / "modules/25-lc-oscillation-and-the-undriven-series-rlc-circuit.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
K_E = 9.00e9


def coulomb_field(charge, source, point):
    dx, dy = point[0] - source[0], point[1] - source[1]
    r = math.hypot(dx, dy)
    return K_E * charge * dx / r**3, K_E * charge * dy / r**3


def pair_field(charge, separation, point):
    """Vector sum of the fields of +charge at (+d/2, 0) and -charge at (-d/2, 0)."""
    plus = coulomb_field(charge, (separation / 2, 0.0), point)
    minus = coulomb_field(-charge, (-separation / 2, 0.0), point)
    return plus[0] + minus[0], plus[1] + minus[1]


def pair_potential(charge, separation, point):
    return sum(
        K_E * q / math.hypot(point[0] - x, point[1])
        for q, x in ((charge, separation / 2), (-charge, -separation / 2))
    )


def trajectory(inductance, capacitance, resistance, volts, duration, dt=1e-6):
    """RK4 steps of L q'' + R q' + q/C = 0 from rest; yields (t, q, i)."""

    def rhs(q, i):
        return i, -(resistance * i + q / capacitance) / inductance

    q, i, t = capacitance * volts, 0.0, 0.0
    yield t, q, i
    for _ in range(round(duration / dt)):
        k1 = rhs(q, i)
        k2 = rhs(q + dt * k1[0] / 2, i + dt * k1[1] / 2)
        k3 = rhs(q + dt * k2[0] / 2, i + dt * k2[1] / 2)
        k4 = rhs(q + dt * k3[0], i + dt * k3[1])
        q += dt * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        i += dt * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
        t += dt
        yield t, q, i


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


def test_dipole_reading_states_the_superposed_fields_potentials_and_forces():
    q, d = 2.0e-9, 4.0e-3
    p = q * d
    axis = pair_field(q, d, (0.040, 0.0))[0]
    bisector = pair_field(q, d, (0.0, 0.040))
    assert abs(bisector[1]) < 1e-9 and bisector[0] < 0  # opposite to p, which points along +x
    near = K_E * 5.0e-9 * q / (0.10 - d / 2) ** 2
    far = K_E * 5.0e-9 * q / (0.10 + d / 2) ** 2
    stated(
        DIPOLE,
        f"{round(axis)} N/C", f"{round(2 * K_E * p / 0.040**3)} N/C",
        f"{round(-bisector[0])} N/C exactly", f"{round(K_E * p / 0.040**3)} N/C from the far-field form",
        f"{pair_potential(q, d, (0.040, 0.0)):.1f} V", f"{K_E * p / 0.040**2:.1f} V",
        "pE = 4.0 × 10⁻⁷ N·m", "2pE = 8.0 × 10⁻⁷ J", "F ≈ 7.2 × 10⁻⁷ N",
        f"{(near - far) * 1e7:.2f} × 10⁻⁷ N", f"2kp/r³ = {round(2 * K_E * p / 0.10**3)} N/C",
    )
    assert pair_potential(q, d, (0.0, 0.040)) == pytest.approx(0, abs=1e-12)
    ratios = [pair_field(1.0, 1.0, (n, 0.0))[0] / (2 * K_E / n**3) for n in (10, 5, 2)]
    stated(DIPOLE, f"about {ratios[0]:.3f} at z = 10d, {ratios[1]:.3f} at z = 5d and {ratios[2]:.3f} at z = 2d")


def test_dipole_worked_example_matches_superposition_and_newtons_third_law():
    q, d = 3.0e-9, 2.0e-3
    p = q * d
    exact = pair_field(q, d, (0.030, 0.0))[0]
    on_pair = K_E * 4.0e-9 * q * (1 / (0.050 - d / 2) ** 2 - 1 / (0.050 + d / 2) ** 2)
    field_at_source = pair_field(q, d, (0.050, 0.0))[0]
    assert on_pair == pytest.approx(4.0e-9 * field_at_source, rel=1e-12)
    stated(
        DIPOLE,
        "= 4000 N/C", f"{round(exact)} N/C, about 0.2% higher",
        f"{p * 2.0e4 * math.sin(math.radians(60)) * 1e7:.2f} × 10⁻⁷ N·m",
        f"{p * 2.0e4 * (1 - math.cos(math.radians(60))) * 1e8:.1f} × 10⁻⁸ J",
        f"{2 * K_E * 4.0e-9 * p / 0.050**3 * 1e6:.2f} × 10⁻⁶ N", f"2kp/r³ = {round(2 * K_E * p / 0.050**3)} N/C",
    )
    assert on_pair * 1e6 == pytest.approx(3.46, abs=0.005)  # the exact pair force rounds to the stated value too
    worked = next(
        lesson for module in MANIFEST["modules"] for lesson in module["lessons"] if lesson["id"] == "physics-em-24"
    )["worked_example"]
    stated(worked, "4000 N/C", f"{round(exact)} N/C", "1.04 × 10⁻⁷ N·m", "6.0 × 10⁻⁸ J", "3.46 × 10⁻⁶ N")


def test_lc_reading_states_the_integrated_lossless_and_damped_responses():
    inductance, capacitance, volts = 25e-3, 2.5e-6, 12.0
    lossless = list(trajectory(inductance, capacitance, 0, volts, 0.8e-3, dt=1e-7))
    quarter = next(t for t, q, _ in lossless if q <= 0)
    peak = max(abs(i) for _, _, i in lossless)
    split = next(t for t, q, i in lossless if q**2 / (2 * capacitance) <= inductance * i**2 / 2)
    omega0 = math.pi / 2 / quarter
    stated(
        LC,
        f"ω₀ = {omega0:.0f} rad/s", f"f₀ = ω₀/2π = {omega0 / (2 * math.pi):.1f} Hz", f"T = {2 * math.pi / omega0 * 1e3:.3f} ms",
        f"q₀ = {capacitance * volts * 1e6:.0f} µC", f"ω₀q₀ = {peak:.3f} A", f"|di/dt| = V₀/L = {volts / inductance:.0f} A/s",
        f"T/4 = {quarter * 1e3:.3f} ms", f"T/2 = {2 * quarter * 1e3:.3f} ms", f"T/8 = {split * 1e3:.3f} ms",
        f"U = {capacitance * volts**2 / 2 * 1e6:.0f} µJ", f"q₀/√2 = {capacitance * volts / math.sqrt(2) * 1e6:.1f} µC",
        f"√(L/C) = {math.sqrt(inductance / capacitance):.0f} Ω",
    )

    def settle(resistance):
        return max(t for t, q, _ in trajectory(inductance, capacitance, resistance, volts, 15e-3) if abs(q) > 0.01 * capacitance * volts)

    lowest = min(q for _, q, _ in trajectory(inductance, capacitance, 20, volts, 1e-3)) / (capacitance * volts)
    alpha, root = 500 / (2 * inductance), math.sqrt((500 / (2 * inductance)) ** 2 - omega0**2)
    assert lowest < 0  # the underdamped charge reverses sign
    stated(
        LC,
        f"about −{abs(lowest):.2f}q₀", f"about {round(settle(20) * 1e3)} ms", f"about {settle(200) * 1e3:.2f} ms",
        f"about {settle(500) * 1e3:.2f} ms", f"about −{alpha - root:.0f} s⁻¹ and −{alpha + root:,.0f} s⁻¹",
        f"a {1 / (alpha - root) * 1e3:.2f} ms time constant", "R_c\\) = 200 Ω",
    )


def test_lc_worked_example_energy_loss_equals_the_resistor_heat():
    inductance, capacitance, volts, resistance = 25e-3, 2.5e-6, 12.0, 20
    alpha = resistance / (2 * inductance)
    omega_d = math.sqrt(1 / (inductance * capacitance) - alpha**2)
    period = 2 * math.pi / omega_d
    steps = list(trajectory(inductance, capacitance, resistance, volts, period, dt=period / 20000))
    heat = math.fsum((a[2] ** 2 + b[2] ** 2) / 2 * resistance * (b[0] - a[0]) for a, b in zip(steps, steps[1:]))
    start = capacitance * volts**2 / 2
    end = steps[-1][1] ** 2 / (2 * capacitance) + inductance * steps[-1][2] ** 2 / 2
    assert heat == pytest.approx(start - end, rel=1e-6)
    assert end / start == pytest.approx(math.exp(-2 * alpha * period), rel=1e-6)
    q_factor = math.sqrt(1 / (inductance * capacitance)) * inductance / resistance
    stated(
        LC,
        f"α = {alpha:.0f} s⁻¹", f"\\(\\omega_d\\) = {omega_d:.0f} rad/s", f"Q = {q_factor:.1f}",
        f"\\(T_d\\) = {period * 1e3:.3f} ms", f"charge ratio is {math.exp(-alpha * period):.3f}",
        f"energy ratio \\(e^{{-2\\alpha T_d}}\\) is {end / start:.3f}", f"About {round(100 * (1 - end / start))}%",
        f"{end * 1e6:.1f} µJ remains", f"{heat * 1e6:.1f} µJ has been dissipated", f"time constant 2L/R = {2 * inductance / resistance * 1e3:.1f} ms",
        f"time constant L/R = {inductance / resistance * 1e3:.2f} ms",
    )
    # The small-loss rule: impossible at Q = 5, close at Q = 100.
    for q_value, rule, exact in ((5, "126%", None), (100, "6.3%", "6.1%")):
        x = (2 * math.pi / q_value) / math.sqrt(1 - 1 / (4 * q_value**2))
        assert f"{100 * 2 * math.pi / q_value:.0f}%" == rule or f"{100 * 2 * math.pi / q_value:.1f}%" == rule
        if exact:
            assert f"{100 * (1 - math.exp(-x)):.1f}%" == exact
        stated(LC, rule)


def test_new_lessons_follow_their_prerequisites_in_the_schedule():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[1]["lesson_ids"][-1] == "physics-em-24" and "physics-em-7" in weeks[1]["lesson_ids"]
    assert weeks[9]["lesson_ids"] == ["physics-em-12", "physics-em-18", "physics-em-25"]
    assert "physics-em-24-practice" in weeks[1]["assessment_ids"] and "physics-em-25-practice" in weeks[9]["assessment_ids"]
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == (
        "partial", "unreviewed", "formative-only")
    for text in (DIPOLE, LC):
        assert "link-only scope comparator" in text and "https://ocw.mit.edu/courses/8-02-" in text
        assert "https://oyc.yale.edu/physics/phys-201" in text
        assert "partial, unreviewed and formative-only" in text


def test_crosswalk_records_both_comparators_and_stays_an_unreviewed_title_level_comparison():
    stated(
        CROSSWALK,
        "https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/",
        "https://oyc.yale.edu/physics/phys-201", "compiled with AI assistance", "not a review by the owner",
        "does not compare lecture content, problem sets, exams or workload",
        "| Electric dipoles | 2 | 2", "| LC oscillation and undriven LRC circuits | 27 | 12",
        "| Driven LRC circuits, impedance and resonance | 28–29 | 13 (impedance, resonance) |", "Shallow:",
        "| Diffraction and gratings | — | 18", "Absent by policy",
    )
    for target in ("modules/24-electric-dipoles-fields-torque-energy-and-force.md", "modules/25-lc-oscillation-and-the-undriven-series-rlc-circuit.md"):
        assert f"]({target})" in CROSSWALK and (COURSE / target).is_file()
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    yale = registry["em-yale-phys201"]
    assert yale["reuse_mode"] == "link-only-comparator" and not yale["permissions"]["quotation"]
    assert {"physics-em-module-24", "physics-em-module-25"} <= set(yale["mapped_modules"])


MISCONCEPTIONS = {
    "physics-em-24:axis-far-field": 375,  # bisector formula
    "physics-em-24:axis-near-exact": 93.75,  # far-field formula at z = 2d
    "physics-em-24:uniform-torque": 3.6,  # sin 90°
    "physics-em-24:rotation-work": 7.2,  # 2pE from alignment
    "physics-em-24:nonuniform-force": 4.75,  # kQp/r³ without the factor 2
    "physics-em-25:lc-frequency": 5000,  # angular frequency reported in hertz
    "physics-em-25:lc-equal-energy-time": 314.2,  # quarter period
    "physics-em-25:critical-resistance": 250,  # √(L/C) without the factor 2
    "physics-em-25:damped-frequency": 5000,  # undamped frequency
    "physics-em-25:energy-per-cycle": 0.372,  # 1 − 2π/Q
}


@pytest.mark.parametrize("item_id,wrong", MISCONCEPTIONS.items(), ids=list(MISCONCEPTIONS))
def test_numeric_keys_reject_the_named_misconception(item_id, wrong):
    item = BANK[item_id]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct
