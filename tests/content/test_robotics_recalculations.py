"""Separate geometry/dynamics checks; same AI, not qualified human review."""

from __future__ import annotations

import cmath
import csv
import json
import math
from fractions import Fraction
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/robotics"
BANK = {
    q["id"]: q
    for q in json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )[
        "questions"
    ]
}
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))


def position(q1, q2, l1=0.3, l2=0.2):
    return [
        l1 * math.cos(q1) + l2 * math.cos(q1 + q2),
        l1 * math.sin(q1) + l2 * math.sin(q1 + q2),
    ]


def jacobian(q1, q2):
    return [
        [-0.3 * math.sin(q1) - 0.2 * math.sin(q1 + q2), -0.2 * math.sin(q1 + q2)],
        [0.3 * math.cos(q1) + 0.2 * math.cos(q1 + q2), 0.2 * math.cos(q1 + q2)],
    ]


def product(matrix, vector):
    return [math.fsum(a * b for a, b in zip(row, vector)) for row in matrix]


def solve(matrix, rhs):
    a, b = matrix[0]
    c, d = matrix[1]
    det = a * d - b * c
    assert abs(det) > 1e-12
    return [(d * rhs[0] - b * rhs[1]) / det, (-c * rhs[0] + a * rhs[1]) / det]


def motion(angle, task):
    matrix = jacobian(0, math.radians(angle))
    desired = [-0.01, 0] if task == "inward" else [0, 0.01]
    rates = solve(matrix, desired)
    scale = min(1, 0.5 / max(map(abs, rates)))
    command = [scale * rate for rate in rates]
    return rates, scale, command, product(matrix, command)


def bisect(function, low, high):
    for _ in range(100):
        middle = (low + high) / 2
        if (function(low) > 0) == (function(middle) > 0):
            low = middle
        else:
            high = middle
    return (low + high) / 2


def root_damping(kd, kp=64.0):
    """Damping ratio read from a root of s^2 + kd s + kp."""
    root = (-kd + cmath.sqrt(kd * kd - 4 * kp)) / 2
    return -root.real / abs(root)


def point_mass_torques(q, rates, accelerations, tool_mass=0.5, gravity=9.81):
    """Newton-Euler for the two point masses (elbow 1 kg, tool) on 0.30 m and 0.20 m massless links."""
    (q1, q2), (w1, w2), (a1, a2) = q, rates, accelerations
    theta, omega, alpha = q1 + q2, w1 + w2, a1 + a2
    elbow = (0.3 * math.cos(q1), 0.3 * math.sin(q1))
    tool = (elbow[0] + 0.2 * math.cos(theta), elbow[1] + 0.2 * math.sin(theta))
    elbow_acc = (
        -0.3 * a1 * math.sin(q1) - 0.3 * w1 * w1 * math.cos(q1),
        0.3 * a1 * math.cos(q1) - 0.3 * w1 * w1 * math.sin(q1),
    )
    tool_acc = (
        elbow_acc[0] - 0.2 * alpha * math.sin(theta) - 0.2 * omega * omega * math.cos(theta),
        elbow_acc[1] + 0.2 * alpha * math.cos(theta) - 0.2 * omega * omega * math.sin(theta),
    )
    elbow_force = (1.0 * elbow_acc[0], 1.0 * (elbow_acc[1] + gravity))
    tool_force = (tool_mass * tool_acc[0], tool_mass * (tool_acc[1] + gravity))

    def cross(r, f):
        return r[0] * f[1] - r[1] * f[0]

    arm = (tool[0] - elbow[0], tool[1] - elbow[1])
    return [cross(elbow, elbow_force) + cross(tool, tool_force), cross(arm, tool_force)]


def inertia_columns(q, tool_mass=0.5):
    """Mass matrix from Newton-Euler torques for unit accelerations with no gravity or velocity."""
    columns = [point_mass_torques(q, (0, 0), unit, tool_mass, 0) for unit in ((1, 0), (0, 1))]
    return [[columns[0][0], columns[1][0]], [columns[0][1], columns[1][1]]]


def computed_torque_rest_error(true_tool_mass, kp=100.0, kd=20.0, duration=4.0, steps=8000):
    """Simulate computed torque (model tool 0.5 kg) holding (0, 90 deg) on an arm with another tool mass."""
    target = (0.0, math.pi / 2)

    def derivative(state):
        q, rates = state[:2], state[2:]
        command = [kp * (t - x) - kd * r for t, x, r in zip(target, q, rates)]
        model_bias = point_mass_torques(q, rates, (0, 0))
        torque = [b + t for b, t in zip(model_bias, product(inertia_columns(q), command))]
        true_bias = point_mass_torques(q, rates, (0, 0), true_tool_mass)
        acceleration = solve(inertia_columns(q, true_tool_mass), [t - b for t, b in zip(torque, true_bias)])
        return list(rates) + list(acceleration)

    state, dt = [0.0, math.pi / 2, 0.0, 0.0], duration / steps
    for _ in range(steps):
        k1 = derivative(state)
        k2 = derivative([v + dt * k / 2 for v, k in zip(state, k1)])
        k3 = derivative([v + dt * k / 2 for v, k in zip(state, k2)])
        k4 = derivative([v + dt * k for v, k in zip(state, k3)])
        state = [v + dt * (a + 2 * b + 2 * c + d) / 6 for v, a, b, c, d in zip(state, k1, k2, k3, k4)]
    return [target[0] - state[0], target[1] - state[1]], state[2:]


def pd_sag(gains=(50.0, 20.0), tool_mass=0.5):
    """Exact PD equilibrium K_p e = G(q_d - e) found by fixed-point iteration on Newton-Euler gravity."""
    error = [0.0, 0.0]
    for _ in range(200):
        q = (-error[0], math.pi / 2 - error[1])
        gravity = point_mass_torques(q, (0, 0), (0, 0), tool_mass)
        error = [g / k for g, k in zip(gravity, gains)]
    return error


def expected_answers():
    q1, q2 = math.radians(30), math.radians(45)
    x, y = position(q1, q2)
    elbow = math.acos((0.35**2 + 0.15**2 - 0.3**2 - 0.2**2) / (0.12))
    shoulder = math.atan2(0.15, 0.35) - math.atan2(
        0.2 * math.sin(elbow), 0.3 + 0.2 * math.cos(elbow)
    )
    result = {
        "robotics-1:check": math.sin(math.pi / 2),
        "robotics-2:check": 0.5 + 0.5,
        "robotics-3:check": 0.8 * 3,
        "robotics-3:joint-torque-from-inertia": 0.02 * 5,
        "robotics-1:end-effector-position": 1 + 0.5,
        "robotics-3:gear-ratio-torque": 0.1 * 20 * 0.8,
        "robotics-4:combined-sensor-uncertainty": math.hypot(3, 3),
        "robotics-5:forward-x": x,
        "robotics-5:forward-y": y,
        "robotics-5:elbow-angle": math.degrees(elbow),
        "robotics-5:shoulder-angle": math.degrees(shoulder),
        "robotics-5:tool-error": 0.4635 * math.pi / 180 * 1000,
        "robotics-6:output-torque": 0.05 * 50 * 0.8,
        "robotics-6:output-speed": 3000 / 50,
        "robotics-6:gravity-torque": 0.2 * 9.81 * 0.3,
        "robotics-6:margin": 2 / 0.589,
        "robotics-6:tool-resolution": 0.3 * 2 * math.pi / (1024 * 50) * 1000,
    }
    values = {
        7: {
            "base-x": 0.3 - 0.02,
            "base-y": 0.1 + 0.04,
            "inverse-x": 0.14 - 0.1,
            "orientation-mm": 0.1 * 0.002 * 1000,
            "standard-mm": math.sqrt(0.3**2 + 0.2**2),
            "bounded-mm": 0.3 + 0.2,
        },
        8: {
            "determinant": 0.3 * 0.2,
            "elbow-rate": 0.01 / 0.2,
            "force-torque-1": -0.2 * 5,
            "force-torque-2": -0.2 * 5,
            "power": 5 * (-0.06) + 2 * 0.03,
            "damped-rate": 0.01 * 0.1 / (0.01**2 + 0.05**2),
        },
        9: {
            "elbow-cosine": (0.25**2 + 0.25**2 - 2 * 0.25**2) / (2 * 0.25**2),
            "positive-elbow": math.degrees(math.acos(0)),
            "allowed-branches": 1,
            "outer-reach": 2 * 0.25,
            "clearance": 0.1 - 0.05,
            "joint-midpoint-x": 0.5 * math.cos(math.pi / 4),
        },
        10: {
            "kinetic-energy": (0.155 + 2 * 0.02 * 1 * 2 + 0.02 * 2**2) / 2,
            "matrix-determinant": 0.155 * 0.02 - 0.02**2,
            "gravity-shoulder": 1.5 * 9.81 * 0.3,
            "accelerating-shoulder": 1.5 * 9.81 * 0.3 + 0.155,
            "potential-rise": 0.5 * 9.81 * 0.2,
            "straight-mass-determinant": 0.215 * 0.02 - 0.05**2,
        },
        11: {
            "voltage-current": (12 - 0.1 * 100) / 2,
            "motor-torque": 0.1 * 1,
            "low-speed-output": 0.8 * 50 * 0.1 * 2,
            "reflected-inertia": 0.0001 * 50**2,
            "pd-frequency": math.sqrt(2 / 0.02),
            "pd-damping": (0.01 + 0.39) / (2 * math.sqrt(0.02 * 2)),
        },
        12: {
            "cubic-midpoint": 0.4 * (3 * 0.5**2 - 2 * 0.5**3),
            "cubic-peak-speed": 1.5 * 0.4 / 2,
            "cubic-peak-acceleration": 6 * 0.4 / 2**2,
            "duration-speed": float(Fraction(3, 2) * Fraction(2, 5) / Fraction(1, 5)),
            "stop-allowance": 0.2 * 0.05 + 0.2**2 / (2 * 1) + 0.003,
            "clearance-reserve": 0.04 - (0.2 * 0.05 + 0.2**2 / 2 + 0.003),
        },
        13: {
            "following-error": 0.2 - 0.12,
            "jump-speed": 0.1 / 0.01,
            "bounded-change": 2 * 0.01,
            "transmission-gap": 0.01 * 0.3 * 1000,
            "combined-mm": math.sqrt(0.5**2 + 0.8**2),
            "fiducial-bias": sum([2, 2]) / 2,
        },
    }
    result.update(
        {
            f"robotics-{n}:{key}": value
            for n, items in values.items()
            for key, value in items.items()
        }
    )
    # Lesson 4 contact primer: quasistatic spring F = k x, in SI units.
    result.update(
        {
            "robotics-4:contact-position-force": 450 * 2.0e-3,
            "robotics-4:contact-indentation": 0.80 / 400 * 1000,
            "robotics-4:contact-force-limit": max(400, 600) * 2.0e-3,
        }
    )
    # Lesson 14: torques from Newton-Euler point-mass dynamics rather than the Lagrangian M, h and G.
    rest = (0.0, math.pi / 2)
    feedforward = point_mass_torques(rest, (1, 2), (1, 0))
    velocity_only = point_mass_torques(rest, (1, 2), (0, 0), gravity=0)
    gravity_true = point_mass_torques(rest, (0, 0), (0, 0), 0.6)
    gravity_model = point_mass_torques(rest, (0, 0), (0, 0))
    straight = inertia_columns((0.0, 0.0))
    kd_for = bisect(lambda kd: root_damping(kd) - 0.9, 0.1, 15.9)
    result.update(
        {
            "robotics-14:pd-sag-estimate": gravity_model[0] / 50,
            "robotics-14:gravity-mismatch-error": (gravity_true[0] - gravity_model[0]) / 50,
            "robotics-14:pd-natural-frequency-straight": math.sqrt(15.5 / straight[0][0]),
            "robotics-14:computed-torque-damping-gain": kd_for,
            "robotics-14:feedforward-shoulder": feedforward[0],
            "robotics-14:feedforward-elbow": feedforward[1],
            "robotics-14:velocity-term-shoulder": velocity_only[0],
            "robotics-14:computed-torque-mismatch": computed_torque_rest_error(0.6)[0][0],
        }
    )
    rates, scale, _, velocity = motion(2, "inward")
    result.update(
        {
            "robotics-lab-01:in02-demand": rates[1],
            "robotics-lab-01:uniform-scale": scale,
            "robotics-lab-01:achieved-inward": -velocity[0] * 1000,
            "robotics-lab-01:straight-radial-torque": 0,
        }
    )
    return result


EXPECTED = expected_answers()


def test_every_numeric_item_has_separate_calculation():
    assert set(EXPECTED) == {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 74


@pytest.mark.parametrize("key", sorted(EXPECTED))
def test_numeric_keys_against_declared_tolerances(key):
    spec = BANK[key]["solution_spec"]
    allowed = max(
        spec["tolerance"], spec.get("relative_tolerance", 0) * abs(EXPECTED[key])
    )
    assert abs(spec["answer"] - EXPECTED[key]) <= allowed


def test_frame_roundtrip_composition_direction_and_uncertainty():
    def rotate(point):
        return [-point[1], point[0]]

    for point in [[0.04, 0.02], [0, 0], [-0.1, 0.3]]:
        rotated = rotate(point)
        base = [rotated[0] + 0.3, rotated[1] + 0.1]
        shifted = [base[0] - 0.3, base[1] - 0.1]
        recovered = [shifted[1], -shifted[0]]
        assert recovered == pytest.approx(point)
    before = rotate([1 + 0.3, 0 + 0.1])
    after = [rotate([1, 0])[0] + 0.3, rotate([1, 0])[1] + 0.1]
    assert before != after
    angle = 0.002
    chord = 2 * 0.1 * math.sin(angle / 2) * 1000
    assert chord == pytest.approx(0.2, rel=1e-6)
    assert math.hypot(0.3, 0.2) < 0.3 + 0.2


def test_labeled_homogeneous_transform_and_inverse():
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "robotics-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "maps coordinates from frame $B$ into frame $A$" in text
    assert "valid planar rotation preserves lengths" in text
    assert "orthogonal with determinant $+1$" in text

    rotation = [[0, -1], [1, 0]]
    inverse_rotation = [[0, 1], [-1, 0]]
    assert product(rotation, [1, 0]) == [0, 1]
    assert product(inverse_rotation, [0, 1]) == [1, 0]
    for point in ([1, 0], [0, 1]):
        assert product(inverse_rotation, product(rotation, point)) == point
    assert rotation[0][0] * rotation[1][1] - rotation[0][1] * rotation[1][0] == 1

    pose_wb = [[0, -1, 2], [1, 0, 1], [0, 0, 1]]
    point_b = [1, 0, 1]
    point_w = product(pose_wb, point_b)
    assert point_w == pytest.approx([2, 2, 1])
    recovered = product(inverse_rotation, [point_w[0] - 2, point_w[1] - 1])
    assert recovered == pytest.approx(point_b[:2])

    rotate_w = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    translate = [[1, 0, 2], [0, 1, 1], [0, 0, 1]]
    reversed_order = product(rotate_w, product(translate, point_b))
    assert reversed_order == pytest.approx([-1, 3, 1])


def test_two_link_reachability_and_distinct_inverse_branches():
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "robotics-2"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "inner radius is 0.1 m and the outer radius is 0.7 m" in text
    assert "violate a joint limit" in text

    l1, l2 = 0.4, 0.3
    x, y = 0.4, 0.3
    radius = math.hypot(x, y)
    assert abs(l1 - l2) <= radius <= l1 + l2
    cosine = (radius**2 - l1**2 - l2**2) / (2 * l1 * l2)
    assert cosine == pytest.approx(0)
    endpoint_solutions = []
    for theta2 in (math.acos(cosine), -math.acos(cosine)):
        theta1 = math.atan2(y, x) - math.atan2(
            l2 * math.sin(theta2), l1 + l2 * math.cos(theta2)
        )
        endpoint_solutions.append(position(theta1, theta2, l1, l2))
    assert endpoint_solutions[0] == pytest.approx([x, y])
    assert endpoint_solutions[1] == pytest.approx([x, y])
    assert math.sin(0) == pytest.approx(0)
    assert math.sin(math.pi) == pytest.approx(0)


def test_rotational_work_energy_and_gearbox_power_balance():
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "robotics-3"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "Torque and energy share the same base units" in text
    assert "The gearbox increases torque while reducing speed; it does not create power" in text

    inertia, torque, omega0, duration = 0.02, 0.10, 2.0, 0.40
    alpha = torque / inertia
    omega1 = omega0 + alpha * duration
    angle = omega0 * duration + 0.5 * alpha * duration**2
    energy_change = 0.5 * inertia * (omega1**2 - omega0**2)
    assert alpha == pytest.approx(5)
    assert omega1 == pytest.approx(4)
    assert angle == pytest.approx(1.2)
    assert torque * angle == pytest.approx(energy_change)
    assert energy_change == pytest.approx(0.12)


def test_static_feedback_halves_position_error_and_states_its_limits():
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "robotics-4"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "A path describes a geometric route" in text
    assert "A time-scaling function" in text
    assert "It is not a stability proof for a real mechanism" in text

    target, bias, gain, command = 1.0, 0.1, 0.5, 0.0
    residuals = []
    for _ in range(3):
        observed = command + bias
        error = target - observed
        residuals.append(error)
        command += gain * error
    assert residuals == pytest.approx([0.9, 0.45, 0.225])
    assert command == pytest.approx(0.7875)

    ratio, efficiency, motor_torque, motor_speed = 20, 0.8, 0.1, 20
    output_torque = efficiency * ratio * motor_torque
    output_speed = motor_speed / ratio
    assert output_torque == pytest.approx(1.6)
    assert output_speed == pytest.approx(1)
    assert output_torque * output_speed == pytest.approx(
        efficiency * motor_torque * motor_speed
    )


@pytest.mark.parametrize(
    "q1,q2", [(0, math.pi / 2), (0.4, 0.3), (-0.2, math.radians(2))]
)
def test_jacobian_finite_differences_determinant_and_power(q1, q2):
    matrix = jacobian(q1, q2)
    step = 1e-6
    for axis in range(2):
        plus = [q1, q2]
        minus = [q1, q2]
        plus[axis] += step
        minus[axis] -= step
        derivative = [
            (a - b) / (2 * step) for a, b in zip(position(*plus), position(*minus))
        ]
        assert derivative == pytest.approx([row[axis] for row in matrix], abs=1e-10)
    assert matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] == pytest.approx(
        0.06 * math.sin(q2)
    )
    rates, force = [0.1, 0.2], [5, 2]
    velocity = product(matrix, rates)
    torque = product(list(zip(*matrix)), force)
    assert sum(a * b for a, b in zip(velocity, force)) == pytest.approx(
        sum(a * b for a, b in zip(torque, rates))
    )


def test_singular_direction_force_map_and_damped_residual():
    matrix = jacobian(0, 0)
    assert matrix == [[0, 0], [0.5, 0.2]]
    assert product(matrix, [1, -2.5]) == pytest.approx([0, 0])
    assert product(list(zip(*matrix)), [5, 0]) == [0, 0]
    with pytest.raises(AssertionError):
        solve(matrix, [-0.01, 0])
    rate = 0.01 * 0.1 / (0.01**2 + 0.05**2)
    assert 0.01 * rate < 0.1
    assert rate < 10


def test_inverse_branches_limits_and_distinct_joint_path_midpoint():
    candidates = []
    for elbow in [math.pi / 2, -math.pi / 2]:
        shoulder = math.pi / 4 - math.atan2(
            0.25 * math.sin(elbow), 0.25 + 0.25 * math.cos(elbow)
        )
        assert position(shoulder, elbow, 0.25, 0.25) == pytest.approx([0.25, 0.25])
        candidates.append((math.degrees(shoulder), math.degrees(elbow)))
    assert sum(-30 <= a <= 60 and -120 <= b <= 120 for a, b in candidates) == 1
    midpoint = position(math.pi / 4, 0, 0.25, 0.25)
    assert midpoint == pytest.approx([0.5 / math.sqrt(2)] * 2)
    assert midpoint != [0.25, 0.25]
    assert (0.6**2 - 0.25**2 - 0.25**2) / (2 * 0.25**2) > 1


def clearance(start, end, center, radius):
    vector = [b - a for a, b in zip(start, end)]
    norm = sum(v * v for v in vector)
    fraction = (
        0
        if norm == 0
        else max(
            0, min(1, sum((c - a) * v for c, a, v in zip(center, start, vector)) / norm)
        )
    )
    nearest = [a + fraction * v for a, v in zip(start, vector)]
    return math.hypot(*(c - p for c, p in zip(center, nearest))) - radius


@pytest.mark.parametrize(
    "end,center,answer",
    [([1, 0], [0.5, 0.1], 0.05), ([1, 0], [2, 0], 0.95), ([0, 0], [0, 0.1], 0.05)],
)
def test_segment_projection_endpoint_and_degenerate_clearance(end, center, answer):
    assert clearance([0, 0], end, center, 0.05) == pytest.approx(answer)


def mass(q1, q2):
    matrix = jacobian(q1, q2)
    a = 0.09 + 0.5 * sum(row[0] ** 2 for row in matrix)
    b = 0.5 * sum(row[0] * row[1] for row in matrix)
    d = 0.5 * sum(row[1] ** 2 for row in matrix)
    return [[a, b], [b, d]]


def energy(q, rates):
    tool_velocity = product(jacobian(*q), rates)
    kinetic = 0.5 * (0.3 * rates[0]) ** 2 + 0.5 * 0.5 * sum(
        v * v for v in tool_velocity
    )
    potential = 1.5 * 9.81 * 0.3 * math.sin(q[0]) + 0.5 * 9.81 * 0.2 * math.sin(sum(q))
    return kinetic + potential


@pytest.mark.parametrize("q", [[0, 0], [0, math.pi / 2], [0.3, 0.4]])
def test_point_mass_inertia_positive_and_nonzero_rate_energy_balance(q):
    matrix = mass(*q)
    assert matrix[0][0] > 0 and matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2 > 0
    rates, acc = [0.7, -0.4], [0.2, 0.3]
    h = [
        -0.5 * 0.3 * 0.2 * math.sin(q[1]) * (2 * rates[0] * rates[1] + rates[1] ** 2),
        0.5 * 0.3 * 0.2 * math.sin(q[1]) * rates[0] ** 2,
    ]
    gravity = [
        1.5 * 9.81 * 0.3 * math.cos(q[0]) + 0.5 * 9.81 * 0.2 * math.cos(sum(q)),
        0.5 * 9.81 * 0.2 * math.cos(sum(q)),
    ]
    torque = [a + b + c for a, b, c in zip(product(matrix, acc), h, gravity)]
    dt = 1e-6
    plus_q = [a + dt * b for a, b in zip(q, rates)]
    minus_q = [a - dt * b for a, b in zip(q, rates)]
    plus_rate = [a + dt * b for a, b in zip(rates, acc)]
    minus_rate = [a - dt * b for a, b in zip(rates, acc)]
    derivative = (energy(plus_q, plus_rate) - energy(minus_q, minus_rate)) / (2 * dt)
    assert derivative == pytest.approx(
        sum(a * b for a, b in zip(torque, rates)), abs=1e-8
    )


def test_motor_same_point_power_envelope_and_pd_parameters():
    for speed, current in [(20, 2), (100, 1)]:
        voltage = 2 * current + 0.1 * speed
        assert voltage <= 12
        torque = 0.1 * current
        assert (0.8 * 50 * torque) * (speed / 50) == pytest.approx(0.8 * torque * speed)
    assert 8 * 2 > 0.8 * (0.1 * 1) * 100
    assert 2 * 0.5 > 0.3
    assert math.sqrt(2 / 0.02) == 10 and (0.01 + 0.39) / (2 * math.sqrt(0.02 * 2)) == 1


def test_cubic_extrema_bounds_quintic_endpoints_and_stopping_allowance():
    velocities = [
        0.4 / 2 * (6 * s - 6 * s * s) for s in [i / 2000 for i in range(2001)]
    ]
    assert max(velocities) == pytest.approx(0.3)
    assert 6 * 0.4 / 2**2 == pytest.approx(0.6)
    displacement, speed_limit = Fraction(2, 5), Fraction(1, 5)
    duration = max(Fraction(3, 2) * displacement / speed_limit, math.sqrt(6))
    assert duration == 3
    assert Fraction(3, 2) * displacement / duration <= speed_limit
    assert 6 * displacement / duration**2 <= Fraction(2, 5)
    for s in [0, 1]:
        assert 30 * s * s - 60 * s**3 + 30 * s**4 == 0
        assert 60 * s - 180 * s * s + 120 * s**3 == 0
    assert 0.2 * 0.05 + 0.2**2 / 2 + 0.003 == pytest.approx(0.033)
    assert clearance([0, 0], [1, 0], [0.5, 0], 0.01) < 0
    assert (
        math.hypot(0.5, 0) - 0.01 > 0
    )  # Safe endpoints do not rule out an interior overlap.


def reports():
    with (COURSE / "labs/near-extension-reports.csv").open(newline="") as stream:
        return list(csv.DictReader(stream))


CHECKS = BANK["robotics-lab-01:summary"]["solution_spec"]["validation_spec"]["checks"]


@pytest.mark.parametrize("check", CHECKS, ids=lambda c: c["id"])
def test_csv_cells_recalculated_from_reported_components(check):
    selected = [r for r in reports() if r["sample"] == check["row_id"]]
    value = (
        len(selected)
        if check["column"] == "reports"
        else math.fsum(
            float(
                r[
                    "reported_vx_mm_s"
                    if check["column"] == "mean_vx_mm_s"
                    else "reported_vy_mm_s"
                ]
            )
            for r in selected
        )
        / len(selected)
    )
    assert abs(check["answer"] - value) <= check["tolerance"]


@pytest.mark.parametrize("task", ["inward", "tangent"])
def test_lab_commands_and_report_variants_have_declared_origin(task):
    rows = reports()
    assert len(rows) == 24 and len(CHECKS) == 24
    for row in rows:
        if row["task"] != task:
            continue
        _, scale, command, velocity = motion(float(row["q2_deg"]), task)
        assert float(row["command_q1_rad_s"]) == pytest.approx(command[0], abs=5.1e-10)
        assert float(row["command_q2_rad_s"]) == pytest.approx(command[1], abs=5.1e-10)
        assert max(map(abs, command)) <= 0.5 + 1e-15
        index = int(row["replicate"]) - 2
        assert float(row["reported_vx_mm_s"]) == pytest.approx(
            1000 * velocity[0] + index * 0.02, abs=5.1e-7
        )
        assert float(row["reported_vy_mm_s"]) == pytest.approx(
            1000 * velocity[1] - index * 0.01, abs=5.1e-7
        )
        if task == "tangent":
            assert scale == 1 and command == pytest.approx([1 / 30, -1 / 30])


def test_uniform_limiter_preserves_direction_while_independent_clipping_changes_it():
    rates, scale, command, velocity = motion(2, "inward")
    assert scale < 1 and command[1] == pytest.approx(0.5)
    assert velocity == pytest.approx([-0.01 * scale, 0], abs=1e-16)
    clipped = [max(-0.5, min(0.5, r)) for r in rates]
    assert product(jacobian(0, math.radians(2)), clipped) == pytest.approx([0, -0.15])


def test_sensing_bound_and_case_qualifications_are_explicit():
    assert 0.1 / 0.01 > 2 and 0.1 > 2 * 0.01
    assert 0.01 * 0.3 * 1000 == 3
    assert math.hypot(0.5, 0.8) < 0.5 + 0.8
    lesson = next(
        lesson
        for module in MANIFEST["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "robotics-13"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "finite endpoint force mapping alone does not universally diverge" in text
    assert "lacks continuous redundancy" in text


def test_schedule_once_formative_labels_and_all_package_schedules():
    assert MANIFEST["version"] == MANIFEST["history"][-1]["version"]
    weeks = MANIFEST["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    lessons = [
        lesson["id"] for module in MANIFEST["modules"] for lesson in module["lessons"]
    ]
    assert sorted(item for week in weeks for item in week["lesson_ids"]) == sorted(
        lessons
    )
    assessment_ids = {a["id"] for a in MANIFEST["assessments"]}
    assert all(a in assessment_ids for week in weeks for a in week["assessment_ids"])
    assert (
        MANIFEST["maturity"] == "partial"
        and MANIFEST["review"]["status"] == "unreviewed"
    )
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    assert all(a["mode"] != "graded" for a in MANIFEST["assessments"])
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "Weeks 1, 3, 7 and 12 now have expanded" in syllabus
    assert "first three prototype readings remain concise primers" in syllabus
    courses = [
        json.loads(p.read_text(encoding="utf-8"))
        for p in (ROOT / "content/courses").glob("*/course.json")
    ]
    assert len(courses) == 27 and all(c["duration"]["weeks"] for c in courses)


def test_computed_torque_lesson_statements_match_newton_euler_and_simulation():
    text = (COURSE / "modules/14-gravity-compensation-and-computed-torque-control.md").read_text(encoding="utf-8")
    sag = pd_sag()
    error, rates = computed_torque_rest_error(0.6)
    bent, straight = inertia_columns((0.0, math.pi / 2)), inertia_columns((0.0, 0.0))
    assert "e ≈ (0.0898, 0.0046) rad" in text
    assert sag == pytest.approx([0.0898, 0.0046], abs=6e-5)
    assert "**10.0 rad/s**" in text and "**8.49 rad/s**" in text
    assert math.sqrt(15.5 / bent[0][0]) == pytest.approx(10.0, abs=0.005)
    assert math.sqrt(15.5 / straight[0][0]) == pytest.approx(8.49, abs=0.005)
    assert "about **0.022 rad** at the shoulder and an error of similar size and opposite sign at the elbow" in text
    assert error[0] == pytest.approx(0.022, abs=0.0005) and -1.1 < error[1] / error[0] < -0.9
    assert max(abs(r) for r in rates) < 1e-6
    assert "**(4.4145, 0) N·m**" in text and "**τ = (4.3295, 0.050) N·m.**" in text
    assert point_mass_torques((0.0, math.pi / 2), (1, 2), (1, 0)) == pytest.approx([4.3295, 0.050], abs=1e-9)
    assert "1.6 × 9.81 × 0.30 = 4.709 N·m" in text
    assert point_mass_torques((0.0, math.pi / 2), (0, 0), (0, 0), 0.6)[0] == pytest.approx(4.709, abs=5e-4)
    exact_model = computed_torque_rest_error(0.5, duration=1.0, steps=2000)[0]
    assert max(abs(e) for e in exact_model) < 1e-9
