"""Independent body-energy, constraint, swept-geometry and clipped-control references."""

from __future__ import annotations

import json
import math
import re
from functools import cache
from pathlib import Path

import pytest
import sympy as sp
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/robotics"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"robotics-(1[5-9]|2[01]):depth-\d+", q["id"])
}
Q1, Q2, V1, V2, A1, A2 = sp.symbols("q1 q2 v1 v2 a1 a2", real=True)
Q = sp.Matrix([Q1, Q2])
V = sp.Matrix([V1, V2])
A = sp.Matrix([A1, A2])


@cache
def body_reference():
    # Assemble COM translation and absolute body rotation directly from the declared bodies.
    p1 = sp.Matrix([sp.cos(Q1) / 2, sp.sin(Q1) / 2])
    p2 = sp.Matrix([sp.cos(Q1) + sp.cos(Q1 + Q2) / 2, sp.sin(Q1) + sp.sin(Q1 + Q2) / 2])
    c1 = p1.jacobian(Q) * V
    c2 = p2.jacobian(Q) * V
    kinetic = sp.trigsimp((c1.dot(c1) + c2.dot(c2)) / 2 + (V1**2 + (V1 + V2) ** 2) / 24)
    potential = p1[1] + p2[1]
    mass = sp.simplify(sp.hessian(kinetic, (V1, V2)))
    momentum = sp.Matrix([sp.diff(kinetic, v) for v in V])
    # Euler-Lagrange derivatives distinguish the independent q,v,a coordinates.
    force = sp.simplify(
        momentum.jacobian(Q) * V
        + momentum.jacobian(V) * A
        - sp.Matrix([sp.diff(kinetic, q) for q in Q])
        + sp.Matrix([sp.diff(potential, q) for q in Q])
    )
    return kinetic, potential, mass, force


def at(expression, position, velocity=(0, 0), acceleration=(0, 0)):
    return sp.simplify(
        expression.subs(
            dict(zip([Q1, Q2, V1, V2, A1, A2], [*position, *velocity, *acceleration]))
        )
    )


def constraint_reference(mass, input_force):
    normal = sp.Matrix([[1, 0]])
    block = mass.row_join(-normal.T).col_join(normal.row_join(sp.zeros(1)))
    solution = block.inv() * sp.Matrix([*input_force, 0])
    return solution, 1 / (normal * mass.inv() * normal.T)[0]


@cache
def calculations():
    kinetic, potential, mass, force = body_reference()
    straight = at(mass, (sp.pi / 2, 0))
    tau = at(force, (0, sp.pi / 2), (1, -1), (0, 2))
    active, meff = constraint_reference(sp.Matrix([[3, 1], [1, 2]]), [-4, 2])
    release = sp.Matrix([[3, 1], [1, 2]]).inv() * sp.Matrix([4, 2])
    assigned, assigned_mass = constraint_reference(sp.Matrix([[4, 1], [1, 1]]), [-2, 3])
    released = sp.Matrix([[4, 1], [1, 1]]).inv() * sp.Matrix([5, 1])
    t = sp.symbols("t", real=True)
    path = sp.Matrix([sp.sin(t) / 5, sp.Rational(2, 5) + sp.cos(2 * t) / 10])
    derivative = sp.diff(path, t)
    second = sp.diff(path, t, 2)

    def path_values(time):
        position = path.subs(t, time)
        velocity = derivative.subs(t, time)
        acceleration = second.subs(t, time)
        return (
            at(force, position, velocity, acceleration),
            at(kinetic, position, velocity),
            at(potential, position),
        )

    ft0, kt0, ut0 = path_values(0)
    ft1, _, ut1 = path_values(sp.pi / 2)
    actual_mass = at(mass, (0, sp.pi / 2))
    offset = at(force, (0, sp.pi / 2), (1, 2))
    virtual = (
        sp.Matrix([sp.Rational(1, 5), sp.Rational(3, 10)])
        + 20 * sp.Matrix([sp.Rational(1, 10), -sp.Rational(1, 10)])
        + 100 * sp.Matrix([sp.Rational(1, 100), -sp.Rational(1, 50)])
    )
    requested = actual_mass * virtual + offset
    delivered = sp.Matrix(
        [max(-sp.Rational(1, 2), min(sp.Rational(1, 2), value)) for value in requested]
    )
    actual = actual_mass.inv() * (delivered - offset)
    error_acc = sp.Matrix([sp.Rational(1, 5), sp.Rational(3, 10)]) - actual
    return {
        (15, 1): {"m11": straight[0, 0], "m12": straight[0, 1], "m22": straight[1, 1]},
        (15, 2): {
            "kinetic": at(kinetic, (sp.pi / 2, 0), (1, -1)),
            "potential": at(potential, (sp.pi / 2, 0)),
        },
        (15, 3): {"shoulder": tau[0], "elbow": tau[1]},
        (15, 4): {"determinant": straight.det()},
        (16, 1): {"tangent": active[1], "reaction": active[2]},
        (16, 2): {"mobility": 1 / meff, "effective_mass": meff},
        (16, 3): {"normal": release[0], "tangent": release[1]},
        (16, 4): {"reaction": 4, "acceleration": 4},
        (17, 1): {"speed": 0.32, "motion": 0.032},
        (17, 2): {
            "margin": 0.05 - 0.032 - 0.005,
            "threshold": 2 * (0.05 - 0.005) / 0.32,
        },
        (17, 3): {"endpoint": 0.25 - 0.03 - 0.01, "overlap": 0.03 + 0.01},
        (17, 4): {
            "geometry": 0.5 * 0.01 + 0.2 * 0.02,
            "margin": 0.05 - 0.032 - (0.5 * 0.01 + 0.2 * 0.02),
        },
        (18, 1): {
            "shoulder": ft0[0],
            "elbow": ft0[1],
            "kinetic": kt0,
            "potential": ut0,
        },
        (18, 2): {"shoulder": ft1[0], "elbow": ft1[1], "potential": ut1},
        (19, 1): {
            "tangent": assigned[1],
            "reaction": assigned[2],
            "effective_mass": assigned_mass,
        },
        (19, 2): {"normal": released[0], "tangent": released[1]},
        (20, 1): {
            "speed": 0.55,
            "motion": 0.55 * 0.1 / 2,
            "margin": 0.05 - 0.55 * 0.1 / 2 - 0.01,
        },
        (20, 2): {
            "geometry": 0.75 * 0.01 + 0.25 * 0.02,
            "margin": 0.05 - 0.55 * 0.1 / 2 - (0.75 * 0.01 + 0.25 * 0.02),
            "threshold": 2 * (0.05 - (0.75 * 0.01 + 0.25 * 0.02)) / 0.55,
        },
        (21, 1): {
            "shoulder_request": requested[0],
            "elbow_request": requested[1],
            "shoulder_acceleration": actual[0],
            "elbow_acceleration": actual[1],
        },
        (21, 2): {
            "shoulder_error_acceleration": error_acc[0],
            "elbow_error_acceleration": error_acc[1],
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_body_constraint_geometry_control_fields_and_actual_grader_reject_errors(qid):
    number, item = map(int, re.fullmatch(r"robotics-(\d+):depth-(\d+)", qid).groups())
    question = NEW[qid]
    values = calculations()[number, item]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-11, abs=1e-13)
            response[spec["id"]] = format(value, ".2e")
    assert grade(question, AttemptRequest(response=response)).correct
    for spec in specs:
        wrong = (
            format(float(values[spec["id"]]) * 1.2, ".2e")
            if spec["type"] == "numeric"
            else str((spec["answer"] + 1) % 3)
        )
        assert not grade(
            question, AttemptRequest(response={**response, spec["id"]: wrong})
        ).correct


def simpson(function, left, right, panels):
    step = (right - left) / panels
    return (
        step
        / 3
        * (
            function(left)
            + function(right)
            + 4 * sum(function(left + i * step) for i in range(1, panels, 2))
            + 2 * sum(function(left + i * step) for i in range(2, panels, 2))
        )
    )


def test_energy_derived_rod_matrix_euler_lagrange_and_independent_work_integral():
    kinetic, potential, mass, force = body_reference()
    assert sp.simplify(kinetic - (V.T * mass * V)[0] / 2) == 0
    assert sp.simplify(mass.det() - (sp.Rational(4, 9) - sp.cos(Q2) ** 2 / 4)) == 0
    mdot = mass.diff(Q1) * V1 + mass.diff(Q2) * V2
    gravity = sp.Matrix([sp.diff(potential, q) for q in Q])
    velocity_force = sp.simplify(force - mass * A - gravity)
    assert sp.simplify((V.T * velocity_force)[0] - (V.T * mdot * V)[0] / 2) == 0
    energy = kinetic + potential
    original_derivative = (sp.Matrix([sp.diff(energy, q) for q in Q]).T * V)[0] + (
        sp.Matrix([sp.diff(energy, v) for v in V]).T * A
    )[0]
    assert sp.simplify((force.T * V)[0] - original_derivative) == 0
    t = sp.symbols("t", real=True)
    path = [sp.sin(t) / 5, sp.Rational(2, 5) + sp.cos(2 * t) / 10]
    substitution = {
        Q1: path[0],
        Q2: path[1],
        V1: sp.diff(path[0], t),
        V2: sp.diff(path[1], t),
        A1: sp.diff(path[0], t, 2),
        A2: sp.diff(path[1], t, 2),
    }
    power = sp.lambdify(t, (force.T * V)[0].subs(substitution), "math")
    trajectory_energy = sp.lambdify(t, energy.subs(substitution), "math")
    change = trajectory_energy(1.3) - trajectory_energy(0)
    errors = [abs(simpson(power, 0, 1.3, n) - change) for n in [16, 32, 64]]
    assert errors[2] < errors[1] < errors[0] and errors[2] < 1e-8
    assert simpson(power, 0, 2 * math.pi, 256) == pytest.approx(0, abs=1e-12)
    assert at(energy, (0, sp.pi / 2), (1, 2)) == sp.Rational(8, 3)


def test_constraint_block_reaction_release_rank_and_curved_power():
    for mass, load in [
        (sp.Matrix([[3, 1], [1, 2]]), sp.Matrix([-4, 2])),
        (sp.Matrix([[4, 1], [1, 1]]), sp.Matrix([-2, 3])),
    ]:
        solution, normal_mass = constraint_reference(mass, load)
        acc = solution[:2, 0]
        reaction = solution[2]
        normal = sp.Matrix([[1, 0]])
        assert mass * acc == load + normal.T * reaction and (normal * acc)[0] == 0
        schur = -(normal * mass.inv() * load)[0] / (normal * mass.inv() * normal.T)[0]
        assert schur == reaction > 0 and normal_mass > 0
        redundant = sp.Matrix([[1, 0], [1, 0]])
        assert (redundant * mass.inv() * redundant.T).det() == 0
        assert (normal.T * reaction).dot(sp.Matrix([0, 2])) == 0
    mass = sp.Matrix([[3, 1], [1, 2]])
    separation, _ = constraint_reference(mass, [4, 2])
    assert separation[2] < 0 and (mass.inv() * sp.Matrix([4, 2]))[0] > 0
    t = sp.symbols("t", real=True)
    circle = sp.Matrix([sp.cos(2 * t), sp.sin(2 * t)])
    velocity = sp.diff(circle, t)
    acceleration = sp.diff(velocity, t)
    normal = -circle.T
    assert (normal * velocity)[0].simplify() == 0
    assert sp.simplify((normal * acceleration + sp.diff(normal, t) * velocity)[0]) == 0
    assert sp.simplify(acceleration.dot(velocity)) == 0
    assert acceleration.subs(t, 0) == sp.Matrix([-4, 0])


def segment_distance(point, left, right):
    direction = [b - a for a, b in zip(left, right)]
    length = sum(x * x for x in direction)
    parameter = (
        max(
            0,
            min(
                1, sum((p - a) * d for p, a, d in zip(point, left, direction)) / length
            ),
        )
        if length
        else 0
    )
    nearest = [a + parameter * d for a, d in zip(left, direction)]
    return math.dist(point, nearest)


def test_whole_link_geometry_intervening_collision_and_continuous_bounds():
    center = (0.25, 0.25)

    def clearance(angle):
        elbow = (0.25 * math.cos(angle), 0.25 * math.sin(angle))
        tool = (2 * elbow[0], 2 * elbow[1])
        return (
            min(
                segment_distance(center, (0, 0), elbow),
                segment_distance(center, elbow, tool),
            )
            - 0.04
        )

    assert [clearance(0), clearance(math.pi / 2)] == pytest.approx([0.21, 0.21])
    assert clearance(math.pi / 4) == pytest.approx(-0.04, abs=1e-15)
    assert segment_distance((2, 1), (0, 0), (1, 0)) == pytest.approx(math.sqrt(2))
    assert segment_distance((1, 1), (0, 0), (0, 0)) == pytest.approx(math.sqrt(2))

    # Check the proved all-point bound on an independent smooth path,including interior material points.
    def point(time, material):
        a = 0.2 * math.sin(time)
        b = 0.3 * math.sin(2 * time)
        return (
            0.3 * math.cos(a) + material * 0.2 * math.cos(a + b),
            0.3 * math.sin(a) + material * 0.2 * math.sin(a + b),
        )

    bound = 0.3 * 0.2 + 0.2 * (0.2 + 0.6)
    for material in [0, 0.25, 0.5, 1]:
        for n in range(50):
            time = n / 10
            later = time + 0.07
            assert (
                math.dist(point(time, material), point(later, material))
                <= bound * 0.07 + 1e-15
            )
    assert 0.05 - 0.32 * 0.2 / 2 - 0.005 == pytest.approx(0.013)
    assert 0.05 - 0.55 * 0.1 / 2 - (0.75 * 0.01 + 0.25 * 0.02) == pytest.approx(0.01)
    threshold = 2 * (0.05 - 0.005) / 0.32
    assert 0.05 - 0.32 * threshold / 2 - 0.005 == pytest.approx(0, abs=1e-17)
    assert 0.05 - 0.32 * (threshold * 0.9) / 2 - 0.005 > 0


def test_clipped_control_coupled_acceleration_error_and_exact_unclipped_reference():
    _, _, mass, force = body_reference()
    m = at(mass, (0, sp.pi / 2))
    offset = at(force, (0, sp.pi / 2), (1, 2))
    desired = sp.Matrix([sp.Rational(1, 5), sp.Rational(3, 10)])
    error = sp.Matrix([sp.Rational(1, 100), -sp.Rational(1, 50)])
    rate = sp.Matrix([sp.Rational(1, 10), -sp.Rational(1, 10)])
    virtual = desired + 20 * rate + 100 * error
    requested = m * virtual + offset
    clipped = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 3)])
    actual = m.inv() * (clipped - offset)
    assert m * actual + offset == clipped
    assert actual - virtual == m.inv() * (clipped - requested)
    assert actual[1] != virtual[1] and clipped[1] == requested[1]
    error_acc = desired - actual
    assert error_acc - (-20 * rate - 100 * error) == -m.inv() * (clipped - requested)
    t = sp.symbols("t", real=True)
    for initial, initial_rate in zip(error, rate):
        exact = (initial + (initial_rate + 10 * initial) * t) * sp.exp(-10 * t)
        assert (
            sp.simplify(sp.diff(exact, t, 2) + 20 * sp.diff(exact, t) + 100 * exact)
            == 0
        )
        assert (
            exact.subs(t, 0) == initial and sp.diff(exact, t).subs(t, 0) == initial_rate
        )


def test_robotics_packets_deliver_as_open_partial_coursework():
    assert len(NEW) == 20
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 23
    repository = ContentRepository(ROOT / "content")
    for number in range(15, 22):
        lesson = repository.lesson("robotics", f"robotics-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 18 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
