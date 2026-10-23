"""Independent coupled-equation, impulse, quadrature and oscillator checks."""

from __future__ import annotations

import csv
import json
import math
import re
from fractions import Fraction
from functools import cache
from pathlib import Path

import pytest
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/physics-mechanics"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
BANK = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
}
NEW = {
    qid: q
    for qid, q in BANK.items()
    if re.fullmatch(r"physics-mechanics-(1[6-9]|2[01]):depth-\d+", qid)
}
G = Fraction("9.81")


def solve(matrix, right):
    rows = [
        [Fraction(v) for v in row] + [Fraction(b)]
        for row, b in zip(matrix, right, strict=True)
    ]
    for col in range(len(rows)):
        pivot = next(i for i in range(col, len(rows)) if rows[i][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        rows[col] = [v / scale for v in rows[col]]
        for i in range(len(rows)):
            if i == col:
                continue
            factor = rows[i][col]
            rows[i] = [a - factor * b for a, b in zip(rows[i], rows[col], strict=True)]
    return [row[-1] for row in rows]


def pulley(m1, m2, radius, inertia):
    m1, m2, radius, inertia = map(Fraction, [m1, m2, radius, inertia])
    matrix = [[-m1, 1, 0], [m2, 0, 1], [-inertia / radius**2, -1, 1]]
    right = [m1 * G, m2 * G, 0]
    acceleration, t1, t2 = solve(matrix, right)
    for row, b in zip(matrix, right, strict=True):
        assert sum(x * v for x, v in zip(row, [acceleration, t1, t2], strict=True)) == b
    return acceleration, t1, t2


def slip(mass, beta, u, rim, mu):
    mass, beta, u, rim, mu = map(Fraction, [mass, beta, u, rim, mu])
    # Independent linear impulse/rotation/terminal-constraint equations for v,w,J.
    speed, spin_speed, impulse = solve(
        [[mass, 0, -1], [0, beta * mass, 1], [1, -1, 0]],
        [mass * u, beta * mass * rim, 0],
    )
    assert speed == spin_speed
    time = abs(impulse) / (mu * mass * G)
    initial_energy = mass * (u * u + beta * rim * rim) / 2
    final_energy = mass * (speed * speed + beta * spin_speed * spin_speed) / 2
    return time, speed, initial_energy, final_energy, initial_energy - final_energy


def simpson(function, length, count=4000):
    step = length / count
    return (
        step
        / 3
        * (
            function(0)
            + function(length)
            + math.fsum(
                (4 if i % 2 else 2) * function(i * step) for i in range(1, count)
            )
        )
    )


@cache
def calculations():
    a, t1, t2 = pulley(3, 5, ".1", ".02")
    massless, common, _ = pulley(3, 5, ".1", 0)
    time, speed, initial, final, loss = slip(2, ".5", 3, 0, ".2")
    _, over_speed, _, over_energy, over_loss = slip(2, ".5", 1, 2, ".2")
    b_a, b_t1, b_t2 = pulley(2, 6, ".2", ".08")
    c_time, c_speed, _, _, c_loss = slip("1.5", ".4", "2.8", 0, ".25")
    _, c_over, _, _, c_over_loss = slip("1.5", ".4", ".8", 2, ".25")

    # Direct quadrature of force power and capture-energy flux, not author's log primitive.
    def velocity(t):
        return (6 + 3 * t) / (2 + 0.5 * t)

    work = simpson(lambda t: 3 * velocity(t), 4)
    capture_loss = simpson(lambda t: 0.25 * velocity(t) ** 2, 4)
    assert 9 + work - 40.5 == pytest.approx(capture_loss, abs=1e-11)
    return {
        (16, 1): {"acceleration": a, "tension1": t1, "tension2": t2},
        (16, 2): {
            "angular": a / Fraction(".1"),
            "speed": math.sqrt(2 * float(a) * 0.4),
            "energy": (5 - 3) * G * Fraction(".4"),
        },
        (16, 3): {"acceleration": massless, "tension": common},
        (16, 4): {},
        (17, 1): {"time": time, "speed": speed, "spin": speed / Fraction(".1")},
        (17, 2): {"initial": initial, "final": final, "loss": loss},
        (17, 3): {"speed": over_speed, "final_energy": over_energy, "loss": over_loss},
        (17, 4): {
            "slip": Fraction("2.5") - 1,
            "power": -Fraction(".2") * 2 * G * Fraction("1.5"),
        },
        (18, 1): {
            "collision_speed": (Fraction(".8") * 2 + Fraction("1.2") * -1) / 2,
            "collision_loss": Fraction(".8") * 4 / 2
            + Fraction("1.2") / 2
            - Fraction(".2") ** 2,
            "capture_mass": 2 + Fraction(".5") * 4,
            "capture_speed": Fraction(2 * 3, 4),
            "capture_energy": Fraction(4, 2) * Fraction(3, 2) ** 2,
        },
        (18, 2): {"speed": velocity(4), "work": work, "loss": capture_loss},
        (19, 1): {"acceleration": b_a, "tension1": b_t1, "tension2": b_t2},
        (19, 2): {
            "speed": math.sqrt(2 * float(b_a) * 0.25),
            "time": math.sqrt(0.5 / float(b_a)),
            "release": 4 * G * Fraction(".25"),
            "rotation": Fraction(".08")
            * (2 * b_a * Fraction(".25"))
            / (2 * Fraction(".2") ** 2),
        },
        (20, 1): {
            "time": c_time,
            "speed": c_speed,
            "spin": c_speed / Fraction(".12"),
            "loss": c_loss,
        },
        (20, 2): {"speed": c_over, "loss": c_over_loss},
        (21, 1): {
            "position": Fraction(".1"),
            "velocity": -Fraction(".1") * 4 * Fraction(".1"),
            "energy": Fraction(".04") ** 2 / 2 + 2 * Fraction(".1") ** 2,
        },
        (21, 2): {
            "position": Fraction(".1") - Fraction(".1") * Fraction(".04"),
            "energy": Fraction(".04") ** 2 / 2 + 2 * Fraction(".096") ** 2,
            "damped": math.sqrt(4 - 0.2**2),
        },
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_mechanics_numeric_keys_recompute_and_grader_rejects_each_wrong_field(qid):
    number, item = map(
        int, re.fullmatch(r"physics-mechanics-(\d+):depth-(\d+)", qid).groups()
    )
    values = calculations()[(number, item)]
    question = NEW[qid]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-12, abs=1e-15)
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


def test_pulley_energy_constraint_and_inertia_limits():
    acceleration, t1, t2 = pulley(2, 6, ".2", ".08")
    velocity_squared = 2 * acceleration * Fraction(".25")
    translational = Fraction(2 + 6, 2) * velocity_squared
    rotational = Fraction(".08") / 2 * velocity_squared / Fraction(".2") ** 2
    assert translational + rotational == 4 * G * Fraction(".25")
    assert t2 > t1 > 0
    assert pulley(2, 2, ".2", ".08")[0] == 0
    assert pulley(2, 6, ".2", 0)[0] > acceleration > pulley(2, 6, ".2", ".16")[0]


def test_slip_event_contact_power_and_overspin_limits():
    for u, rim in [(3, 0), (1, 2), (2, 2)]:
        time, speed, initial, final, loss = slip(2, ".5", u, rim, ".2")
        assert loss >= 0 and initial - final == loss
        f = Fraction(".2") * 2 * G
        # Initial slip decays linearly to zero: exact contact-power triangle.
        assert f * abs(u - rim) * time / 2 == loss
        if u == rim:
            assert time == loss == 0 and speed == u
        elif rim > u:
            assert speed > u and final < initial
    assert slip(2, ".5", 3, 0, ".4")[0] == slip(2, ".5", 3, 0, ".2")[0] / 2
    assert slip(2, ".5", 3, 0, ".4")[1] == slip(2, ".5", 3, 0, ".2")[1]


def test_synthetic_oscillator_table_by_rk4_and_energy_dissipation():
    rows = list(
        csv.DictReader((DIRECTORY / "assignments/oscillator-reference.csv").open())
    )
    x, v, lost = 0.1, 0.0, 0.0
    last = 0.0
    for row in rows:
        target = float(row["time_s"])
        steps = 1000
        dt = (target - last) / steps

        def rhs(state):
            px, pv, _ = state
            return pv, -4 * px - 0.4 * pv, 0.4 * pv**2

        for _ in range(steps):
            state = [x, v, lost]
            first = rhs(state)
            second = rhs([s + dt * k / 2 for s, k in zip(state, first, strict=True)])
            third = rhs([s + dt * k / 2 for s, k in zip(state, second, strict=True)])
            fourth = rhs([s + dt * k for s, k in zip(state, third, strict=True)])
            x, v, lost = [
                s + dt * (a + 2 * b + 2 * c + d) / 6
                for s, a, b, c, d in zip(
                    state, first, second, third, fourth, strict=True
                )
            ]
        assert x == pytest.approx(float(row["displacement_m"]), abs=5.1e-9)
        assert v * v / 2 + 2 * x * x + lost == pytest.approx(0.02, abs=1e-12)
        last = target
    # Derive the undamped Euler growth identity at multiple unrelated states.
    for x0, v0, step in [(0.1, 0.0, 0.1), (0.2, -0.3, 0.05), (-0.1, 0.4, 0.2)]:
        initial = v0 * v0 / 2 + 2 * x0 * x0
        xn, vn = x0 + step * v0, v0 - 4 * step * x0
        assert vn * vn / 2 + 2 * xn * xn == pytest.approx(initial * (1 + 4 * step**2))


def test_new_reports_and_resources_deliver_without_graded_activation():
    assert len(NEW) == 16
    assert MANIFEST["version"] == "0.6.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 23
    repository = ContentRepository(ROOT / "content")
    for number in range(16, 22):
        lesson = repository.lesson("physics-mechanics", f"physics-mechanics-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 18 else 2)
        )
    lesson = repository.lesson("physics-mechanics", "physics-mechanics-21")
    assert (
        "/api/v1/courses/physics-mechanics/resources/assignments/oscillator-reference.csv"
        in lesson.markdown
    )
    assert (
        repository.learner_resource(
            "physics-mechanics", "assignments/oscillator-reference.csv"
        )
        == (DIRECTORY / "assignments/oscillator-reference.csv").read_bytes()
    )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
