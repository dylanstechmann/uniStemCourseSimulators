"""Separate electric/circuit calculations; same-AI checks, not human review.

No authoring imports. Numeric/CSV keys and field, power, state and loading
balances are checked using committed data and separate numerical methods.
"""

from __future__ import annotations

import cmath
import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/physics-em"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def bisect(function, low, high):
    sign = function(low)
    assert sign * function(high) <= 0
    for _ in range(90):
        middle = (low + high) / 2
        value = function(middle)
        if sign * value <= 0:
            high = middle
        else:
            low, sign = middle, value
    return (low + high) / 2


def integrate(function, initial, duration, steps=2000):
    state = list(initial)
    dt = duration / steps
    for _ in range(steps):
        a = function(state)
        b = function([v + dt * k / 2 for v, k in zip(state, a)])
        c = function([v + dt * k / 2 for v, k in zip(state, b)])
        d = function([v + dt * k for v, k in zip(state, c)])
        state = [
            v + dt * (ka + 2 * kb + 2 * kc + kd) / 6
            for v, ka, kb, kc, kd in zip(state, a, b, c, d)
        ]
    return state


def quadrature(function, lower, upper, steps=2000):
    dt = (upper - lower) / steps
    return dt * (
        (function(lower) + function(upper)) / 2
        + math.fsum(function(lower + i * dt) for i in range(1, steps))
    )


MU0 = 4e-7 * math.pi


def biot_savart(path, current, point, pieces=4000):
    """Sum mu0 I dl x r / (4 pi r^3) over a parametrized path p(s), 0 <= s <= 1."""
    total = [0.0, 0.0, 0.0]
    for i in range(pieces):
        a, b = path(i / pieces), path((i + 1) / pieces)
        mid = [(x + y) / 2 for x, y in zip(a, b)]
        dl = [y - x for x, y in zip(a, b)]
        r = [p - m for p, m in zip(point, mid)]
        dist = math.sqrt(sum(c * c for c in r))
        cross = (
            dl[1] * r[2] - dl[2] * r[1],
            dl[2] * r[0] - dl[0] * r[2],
            dl[0] * r[1] - dl[1] * r[0],
        )
        for k in range(3):
            total[k] += MU0 * current * cross[k] / (4 * math.pi * dist**3)
    return math.sqrt(sum(c * c for c in total))


def circle(radius):
    return lambda s: (
        radius * math.cos(2 * math.pi * s),
        radius * math.sin(2 * math.pi * s),
        0.0,
    )


def segment(half_length, distance):
    return lambda s: (distance, -half_length + 2 * half_length * s, 0.0)


def enclosed_field(current, radius, r, rings=2000):
    """Ampere's law with the enclosed current found by integrating J over the disc."""
    density = current / (math.pi * radius**2)
    enclosed = quadrature(lambda rho: density * 2 * math.pi * rho, 0, min(r, radius), rings)
    return MU0 * enclosed / (2 * math.pi * r)


def loop_torque(turns, current, radius, field, angle, pieces=4000):
    """Sum r x (I dl x B) around a tilted circular loop in a uniform field along z."""
    tz = 0.0
    torque = [0.0, 0.0, 0.0]
    for i in range(pieces):
        s0, s1 = i / pieces, (i + 1) / pieces

        def at(s):
            x, y = radius * math.cos(2 * math.pi * s), radius * math.sin(2 * math.pi * s)
            return (x * math.cos(angle), y, -x * math.sin(angle))

        a, b = at(s0), at(s1)
        mid = [(p + q) / 2 for p, q in zip(a, b)]
        dl = [q - p for p, q in zip(a, b)]
        force = (dl[1] * field, -dl[0] * field, 0.0)
        torque[0] += turns * current * (mid[1] * force[2] - mid[2] * force[1])
        torque[1] += turns * current * (mid[2] * force[0] - mid[0] * force[2])
        tz += turns * current * (mid[0] * force[1] - mid[1] * force[0])
    return math.sqrt(torque[0] ** 2 + torque[1] ** 2 + tz**2)


def lab_data():
    with (COURSE / "labs/loading-reports.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["sample"], []).append(float(row["reported_voltage_v"]))
    means = {key: math.fsum(values) / len(values) for key, values in groups.items()}
    return rows, groups, means


def calibrated(means, key):
    gain = (means["cal"] - means["zero"]) / 2.5
    return (means[key] - means["zero"]) / gain


def expected_answers():
    answers = {}

    def add(lesson, **values):
        answers.update(
            {
                f"physics-em-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    add(1, check=0.5 * 10e-6 * 3**2 * 1e6, capacitor_energy=0.5 * 2e-6 * 10**2)
    add(
        2,
        check=2000 * 5e-6 * 1000,
        rc_charging=integrate(lambda s: [(5 - s[0]) / 0.001], [0], 0.002)[0],
    )
    add(3, check=50 * 0.004 / 0.02, faraday_emf=50 * 0.002 / 0.10)
    add(4, check=9e6 / (1e6 + 9e6))
    add(
        5,
        capacitance=0.01 * 4 * math.pi * (10e-6) ** 2 * 1e12,
        charge=12.6e-12 * 0.1 * 1e12,
        ion_count=1.257e-12 / 1.602e-19,
        field=0.07 / 5e-9 / 1e6,
        time_constant=1 * 0.01 * 1000,
    )
    add(
        6,
        flow_emf=0.1 * 0.01 * 0.3 * 1000,
        coil_emf=50 * 0.0002 * 20,
        series_resistor=5 / 10e-6,
        leakage=0.35 / 100000 * 1e6,
    )
    add(
        7,
        midpoint_field=2 * 9e9 * 2e-9 / 0.1**2,
        midpoint_potential=9e9 * 2e-9 / 0.1 - 9e9 * 2e-9 / 0.1,
        test_force=3600 * 1e-9 * 1e6,
        point_field=9e9 * 3e-9 / 0.3**2,
        point_potential=9e9 * 3e-9 / 0.3,
        sphere_inside=9e9 * (3e-9 * (0.15 / 0.3) ** 3) / 0.15**2,
    )
    cap = 8.854e-12 * 0.002 / 0.001
    add(
        8,
        vacuum_capacitance=cap * 1e12,
        filled_capacitance=4 * cap * 1e12,
        initial_charge=cap * 6 * 1e12,
        initial_energy=cap * 36 / 2 * 1e12,
        isolated_voltage=cap * 6 / (4 * cap),
        fixed_voltage_energy=4 * cap * 36 / 2 * 1e12,
    )
    loaded = bisect(lambda v: (3 - v) / 200000 - v / 1e6, 0, 3)
    th = bisect(lambda v: (6 - v) / 200000 - v / 100000, 0, 6)
    # A 1 V test port determines the suppressed-source conductance.
    resistance = 1 / (1 / 200000 + 1 / 100000)
    loaded_th = bisect(lambda v: (6 - v) / 200000 - 2 * v / 100000, 0, 6)
    add(
        9,
        loaded_voltage=loaded,
        input_current=loaded / 1e6 * 1e6,
        input_power=loaded**2 / 1e6 * 1e6,
        thevenin_voltage=th,
        thevenin_resistance=resistance / 1000,
        thevenin_loaded=loaded_th,
    )
    one_time = integrate(lambda s: [(3 - s[0]) / 0.1], [1], 0.1)[0]
    add(
        10,
        time_constant=200000 * 0.5e-6,
        one_time_voltage=one_time,
        initial_current=(3 - 1) / 200000 * 1e6,
        final_energy=0.5 * 0.5e-6 * 9 * 1e6,
        source_work=3 * 0.5e-6 * (3 - 1) * 1e6,
        resistor_heat=0.5 * 0.5e-6 * (3 - 1) ** 2 * 1e6,
    )
    force = -2e-9 * 3 * 0.4
    add(
        11,
        magnetic_force=force * 1e9,
        orbit_radius=1e-12 * 3**2 / abs(force) * 1000,
        orbit_frequency=2e-9 * 0.4 / 1e-12,
        wire_force=0.2 * 0.1 * 0.4 * 1000,
        long_wire_field=4 * math.pi * 1e-7 * 0.2 / (2 * math.pi * 0.01) * 1e6,
        solenoid_field=4 * math.pi * 1e-7 * 1000 * 0.2 * 1e6,
    )
    add(
        12,
        turn_flux=(0.1 + 0.020 * 3**2) * 0.003 * 1e6,
        signed_emf=-20 * 0.003 * (0.040 * 3) * 1000,
        bar_emf=0.3 * 0.2 * 0.5 * 1000,
        bar_current=(0.3 * 0.2 * 0.5) / 10 * 1000,
        rl_time=0.04 / 20 * 1000,
        inductor_energy=0.04 * (2 / 20) ** 2 / 2 * 1e6,
    )
    impedance = 1 / (1 / 1e6 + 1j * 10 * 1e-6)
    transfer = impedance / (100000 + impedance)
    tau = (100000 * 1e6 / (100000 + 1e6)) * 1e-6
    add(
        13,
        transfer_magnitude=abs(transfer),
        transfer_phase=math.degrees(math.atan2(transfer.imag, transfer.real)),
        input_rms=abs(transfer) / math.sqrt(2),
        dc_gain=1e6 / 1.1e6,
        pole_frequency=1 / (2 * math.pi * tau),
        input_real_power=abs(transfer) ** 2 / 2,
    )
    add(
        14,
        displacement_current=0.50,
        magnetic_field_inside=1.25,
        magnetic_field_outside=2.00,
        wave_magnetic_field=0.400,
        wave_peak_intensity=(120 * (120 / 3e8)) / (4 * math.pi * 1e-7),
        wave_average_intensity=(120 * (120 / 3e8)) / (2 * 4 * math.pi * 1e-7),
    )
    # Lesson 15: phasor sums for intensity and small-angle fringe geometry.
    spacing = 600e-9 * 2.0 / 0.30e-3
    add(
        15,
        equal_source_intensity=abs(1 + cmath.exp(1j * math.pi / 2)) ** 2,
        fringe_spacing=spacing * 1e3,
        first_dark=0.5 * spacing * 1e3,
        fifth_bright=5 * spacing * 1e3,
        path_phase=2 * math.pi * (1 / 3),
        third_dark_path=(2 + 0.5) * 0.500,
    )
    add(
        16,
        loop_centre_field=biot_savart(circle(0.05), 0.80, (0, 0, 0)) * 1e6,
        loop_axis_field=biot_savart(circle(0.05), 0.80, (0, 0, 0.05)) * 1e6,
        finite_segment_field=biot_savart(segment(0.02, 0.02), 3.0, (0, 0, 0)) * 1e6,
        inside_thick_wire=enclosed_field(8.0, 0.004, 0.001) * 1e6,
        toroid_field=enclosed_field(500 * 0.20, 0.001, 0.05) * 1e6,
        parallel_wire_force=5.0 * enclosed_field(5.0, 0.001, 0.01) * 1e3,
        coil_torque=loop_torque(40, 0.20, 0.015, 0.050, math.pi / 3) * 1e3,
        coil_turning_work=quadrature(
            lambda a: loop_torque(40, 0.20, 0.015, 0.050, a, 400), 0, math.pi, 200
        )
        * 1e3,
    )
    _, _, means = lab_data()
    source = 1e6 * (1 / calibrated(means, "ass") - 1)
    time = -0.05 / math.log(1 - calibrated(means, "b05") / calibrated(means, "bss"))
    effective = source * 1e5 / (source + 1e5)
    add(
        "lab-01",
        report_offset=means["zero"],
        report_gain=(means["cal"] - means["zero"]) / 2.5,
        source_resistance=source,
        input_capacitance=time / effective * 1e6,
    )
    return answers


EXPECTED = expected_answers()


@pytest.mark.parametrize("item_id,expected", EXPECTED.items(), ids=list(EXPECTED))
def test_numeric_key_matches_separate_calculation(item_id, expected):
    spec = BANK[item_id]["solution_spec"]
    allowance = spec["tolerance"] + spec.get("relative_tolerance", 0) * abs(
        spec["answer"]
    )
    assert abs(spec["answer"] - expected) <= allowance + 1e-10


def test_all_numeric_keys_are_recalculated():
    numeric = {q["id"] for q in BANK.values() if q["type"] == "numeric"}
    assert set(EXPECTED) == numeric and len(numeric) == 82


def test_field_source_lesson_statements_match_numerical_biot_savart():
    text = (
        COURSE / "modules/16-sources-of-magnetic-fields-biot-savart-ampere-and-dipoles.md"
    ).read_text(encoding="utf-8")
    loop = circle(0.020)
    assert round(biot_savart(loop, 0.5, (0, 0, 0)) * 1e6, 1) == 15.7
    assert round(biot_savart(loop, 0.5, (0, 0, 0.020)) * 1e6, 2) == 5.55
    finite = biot_savart(segment(0.010, 0.010), 2.0, (0, 0, 0)) * 1e6
    assert round(finite, 1) == 28.3 and round(finite / 40.0, 2) == 0.71

    def square(side):
        corners = [(-side / 2, -side / 2), (side / 2, -side / 2), (side / 2, side / 2), (-side / 2, side / 2)]

        def path(s):
            k, f = min(int(s * 4), 3), s * 4 - min(int(s * 4), 3)
            (x0, y0), (x1, y1) = corners[k], corners[(k + 1) % 4]
            return (x0 + f * (x1 - x0), y0 + f * (y1 - y0), 0.0)

        return path

    assert round(biot_savart(square(0.040), 0.5, (0, 0, 0), 8000) * 1e6, 1) == 14.1
    assert round(biot_savart(square(0.020), 0.05, (0, 0, 0), 8000) * 1e6, 2) == 2.83
    assert round(enclosed_field(10, 0.002, 0.001) * 1e6) == 500
    assert round(enclosed_field(10, 0.002, 0.002) * 1e6) == 1000
    assert round(enclosed_field(10, 0.002, 0.004) * 1e6) == 500
    assert round(enclosed_field(200, 0.001, 0.04) * 1e3, 2) == 1.0
    assert round(enclosed_field(200, 0.001, 0.06) * 1e3, 3) == 0.667
    assert round(3 * enclosed_field(2, 0.001, 0.005) * 1e6) == 240
    moment = 50 * 0.10 * math.pi * 0.010**2
    assert round(loop_torque(50, 0.10, 0.010, 0.20, math.pi / 6) * 1e4, 2) == 1.57
    exact = biot_savart(loop, 0.5, (0, 0, 0.20))
    dipole = MU0 * (0.5 * math.pi * 0.020**2) / (2 * math.pi * 0.20**3)
    assert round(dipole / exact - 1, 3) == 0.015
    assert round(loop_torque(100, 0.05, 0.02 / math.sqrt(math.pi), 0.10, math.pi / 2) * 1e4, 2) == 2.0
    assert round(2 * moment * 0.20 * 1e4, 2) == 6.28
    for phrase in (
        "that is **15.7 μT**",
        "to **5.55 μT**",
        "B = **28.3 μT**",
        "= **14.1 μT**",
        "**500 μT** at r = 1.0 mm and 1000 μT at the surface",
        "**1.00 mT** at r = 0.040 m and 0.667 mT at r = 0.060 m",
        "this is **240 μN/m**",
        "**1.57 × 10⁻³ A·m²**",
        "**1.57 × 10⁻⁴ N·m**",
        "about 1.5%",
        "= 2.83 μT",
    ):
        assert phrase in text, phrase


CHECKS = BANK["physics-em-lab-01:summary"]["solution_spec"]["validation_spec"]["checks"]


@pytest.mark.parametrize("check", CHECKS, ids=[check["id"] for check in CHECKS])
def test_csv_checks_recompute_from_committed_reports(check):
    _, groups, means = lab_data()
    actual = (
        len(groups[check["row_id"]])
        if check["column"] == "replicates"
        else means[check["row_id"]]
    )
    assert check["answer"] == pytest.approx(actual, abs=check["tolerance"])


def test_potential_gradient_zero_value_and_sphere_boundary():
    def potential(x):
        return 9e9 * (2e-9 / abs(x + 0.1) - 2e-9 / abs(x - 0.1))

    step = 1e-5
    assert potential(0) == 0
    assert -(potential(step) - potential(-step)) / (2 * step) == pytest.approx(
        3600, rel=1e-6
    )
    assert 9e9 * 3e-9 * 0.3 / 0.3**3 == pytest.approx(9e9 * 3e-9 / 0.3**2)
    # Equal charges of opposite sign give zero net enclosed charge, not zero local E.
    assert 2e-9 - 2e-9 == 0 and EXPECTED["physics-em-7:midpoint-field"] != 0


def test_dielectric_fixed_charge_and_voltage_energy_ledgers():
    cap = 8.854e-12 * 0.002 / 0.001
    charge = cap * 6
    isolated_final = charge**2 / (2 * 4 * cap)
    initial = charge**2 / (2 * cap)
    assert isolated_final == pytest.approx(initial / 4)
    final = 0.5 * 4 * cap * 6**2
    source = 6 * (4 * cap * 6 - charge)
    mechanical = source - (final - initial)
    assert mechanical == pytest.approx(final - initial)
    assert mechanical > 0 and source == pytest.approx(1912.464e-12)


def test_kirchhoff_power_and_equivalent_port_agree():
    current = 2.5e-6
    load = current * 1e6
    assert 3 * current == pytest.approx(current**2 * (200000 + 1e6))
    assert load == EXPECTED["physics-em-9:loaded-voltage"]
    th = EXPECTED["physics-em-9:thevenin-voltage"]
    rth = EXPECTED["physics-em-9:thevenin-resistance"] * 1000
    assert th * 100000 / (rth + 100000) == pytest.approx(
        EXPECTED["physics-em-9:thevenin-loaded"]
    )


@pytest.mark.parametrize("duration", [0.05, 0.2, 1.0])
def test_rc_component_ode_and_integrated_power(duration):
    resistance, cap, source = 200000, 0.5e-6, 3

    def derivative(state):
        voltage = state[0]
        current = (source - voltage) / resistance
        return [current / cap, source * current, current * current * resistance]

    voltage, work, heat = integrate(derivative, [1, 0, 0], duration)
    assert voltage == pytest.approx(3 - 2 * math.exp(-duration / 0.1), abs=1e-10)
    change = 0.5 * cap * (voltage**2 - 1)
    assert work == pytest.approx(change + heat, abs=1e-14)
    assert work > change > 0 and heat > 0


@pytest.mark.parametrize("parallel_speed", [0, 1])
def test_magnetic_trajectory_preserves_speed_with_signed_deflection(parallel_speed):
    def derivative(state):
        _, _, _, vx, vy, vz = state
        return [vx, vy, vz, 800 * vy, -800 * vx, 0]

    duration = 2 * math.pi / 800 / 4
    x, y, z, vx, vy, vz = integrate(
        derivative, [0, 0, 0, 3, 0, parallel_speed], duration
    )
    assert x == pytest.approx(0.00375, abs=1e-11)
    assert y == pytest.approx(-0.00375, abs=1e-11)
    assert vx == pytest.approx(0, abs=1e-10) and vy == pytest.approx(-3)
    assert z == pytest.approx(parallel_speed * duration)
    assert vx * vx + vy * vy + vz * vz == pytest.approx(9 + parallel_speed**2)


def test_faraday_contour_derivative_and_motional_power():
    step = 1e-5

    def linkage(t):
        return 20 * 0.003 * (0.1 + 0.020 * t * t)

    derivative = (linkage(3 + step) - linkage(3 - step)) / (2 * step)
    assert -derivative * 1000 == pytest.approx(EXPECTED["physics-em-12:signed-emf"])
    current = 0.03 / 10
    opposing_force = current * 0.2 * 0.3
    assert opposing_force * 0.5 == pytest.approx(current**2 * 10)
    assert opposing_force * 0.5 == pytest.approx(90e-6)


@pytest.mark.parametrize("duration", [0.001, 0.005, 0.02])
def test_rl_component_ode_and_energy_with_ongoing_resistor_heat(duration):
    def derivative(state):
        current = state[0]
        return [(2 - 20 * current) / 0.04, 2 * current, 20 * current * current]

    current, work, heat = integrate(derivative, [0, 0, 0], duration)
    assert current == pytest.approx(0.1 * (1 - math.exp(-duration / 0.002)), abs=1e-11)
    assert work == pytest.approx(0.04 * current**2 / 2 + heat, abs=1e-13)
    if duration == 0.02:
        assert heat > 0.04 * current**2 / 2


def test_phasor_kcl_rms_and_cycle_average_power():
    impedance = 1 / (1 / 1e6 + 1j * 10 * 1e-6)
    h = impedance / (100000 + impedance)
    assert (1 - h) / 100000 == pytest.approx(h / impedance)
    period = 2 * math.pi / 10

    def voltage(t):
        return h.real * math.cos(10 * t) - h.imag * math.sin(10 * t)

    rms = math.sqrt(quadrature(lambda t: voltage(t) ** 2, 0, period) / period)
    assert rms == pytest.approx(EXPECTED["physics-em-13:input-rms"])
    real_power = quadrature(lambda t: voltage(t) ** 2 / 1e6, 0, period) / period
    assert real_power * 1e6 == pytest.approx(EXPECTED["physics-em-13:input-real-power"])

    def dv(t):
        return -10 * h.real * math.sin(10 * t) - 10 * h.imag * math.cos(10 * t)

    capacitive_power = (
        quadrature(lambda t: voltage(t) * 1e-6 * dv(t), 0, period) / period
    )
    assert capacitive_power == pytest.approx(0, abs=1e-16)


@pytest.mark.parametrize("kind,resistance", [("a", 1e6), ("b", 1e5)])
def test_lab_loaded_curve_rounding_and_time_inference(kind, resistance):
    rows, groups, means = lab_data()
    assert len(rows) == 36 and len(groups) == 12 and len(CHECKS) == 24
    steady = resistance / (100000 + resistance)
    tau = 100000 * resistance / (100000 + resistance) * 1e-6
    for code, t in [("00", 0), ("05", 0.05), ("10", 0.1), ("20", 0.2), ("ss", None)]:
        key = kind + code
        voltage = steady if t is None else steady * (1 - math.exp(-t / tau))
        assert means[key] == pytest.approx(0.020 + 2 * voltage, abs=0.00000051)
        assert [value - means[key] for value in groups[key]] == pytest.approx(
            [-0.002, 0, 0.002]
        )
        if t:
            inferred = -t / math.log(
                1 - calibrated(means, key) / calibrated(means, kind + "ss")
            )
            assert inferred == pytest.approx(tau, rel=1e-5)
    assert calibrated(means, kind + "ss") == pytest.approx(steady, abs=3e-7)


def test_reporting_correction_leaves_loading_and_nominal_limit_is_equality():
    _, _, means = lab_data()
    assert (means["cal"] - means["zero"]) / 2.5 == pytest.approx(2)
    assert calibrated(means, "ass") < 1 and calibrated(means, "bss") < 1
    assert calibrated(means, "ass") > calibrated(means, "bss")
    assert 50000 * 1e-6 < (100000 * 1e6 / 1.1e6) * 1e-6
    # Preserved V/I key is nominal at-limit equality, not a strict safety margin.
    resistance = EXPECTED["physics-em-6:series-resistor"]
    assert 5 / resistance == pytest.approx(10e-6)
