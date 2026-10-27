"""Independent charge/energy integrals, port identities and wave-boundary checks."""

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
DIRECTORY = ROOT / "content/courses/physics-em"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"physics-em-(1[7-9]|2[0-3]):depth-\d+", q["id"])
}
R = sp.Rational
MU = 4 * sp.pi / R(10**7)
LIGHT = sp.Integer(300000000)
EPS = 1 / (MU * LIGHT**2)
IMPEDANCE = MU * LIGHT


@cache
def cylindrical(k, a, b):
    k, a, b = map(sp.sympify, [k, a, b])
    r, s = sp.symbols("r s", positive=True)
    # Set epsilon to one for this dimensionless/reference integration; K fixes lambda/epsilon.
    line = 2 * sp.pi * k
    rho = 4 * k * r**2 / a**4
    charge = sp.integrate((rho * 2 * sp.pi * r).subs(r, s), (s, 0, r))
    interior = sp.simplify(charge / (2 * sp.pi * r))
    annular = line / (2 * sp.pi * r)
    boundary = sp.integrate(annular, (r, a, b))
    potential = boundary + sp.integrate(interior.subs(r, s), (s, r, a))
    energy = sp.integrate(interior**2 * sp.pi * r, (r, 0, a)) + sp.integrate(
        annular**2 * sp.pi * r, (r, a, b)
    )
    other = sp.integrate(rho * potential * sp.pi * r, (r, 0, a))
    assert sp.simplify(energy - other) == 0
    assert sp.simplify(-sp.diff(potential, r) - interior) == 0
    assert sp.simplify(sp.diff(r * interior, r) / r - rho) == 0
    assert interior.subs(r, a) == annular.subs(r, a)
    return {
        "fraction": sp.simplify(charge.subs(r, a / 2) / line),
        "field": interior.subs(r, a / 2),
        "boundary": boundary,
        "axis": potential.subs(r, 0),
        "before": annular.subs(r, b),
        "surface": -line / (2 * sp.pi * b),
        "energy": sp.simplify(energy / (sp.pi * k**2)),
    }


def mutual(assigned=False):
    inductance = (
        sp.Matrix([[R(3, 100), R(3, 100)], [R(3, 100), R(12, 100)]])
        if assigned
        else sp.Matrix([[R(2, 100), R(2, 100)], [R(2, 100), R(8, 100)]])
    )
    current = sp.Matrix([2, 1] if assigned else [1, -2])
    derivative = sp.Matrix([-1, 2] if assigned else [4, 1])
    voltage = inductance * derivative
    return {
        "coupling": abs(inductance[0, 1])
        / sp.sqrt(inductance[0, 0] * inductance[1, 1]),
        "energy": (current.T * inductance * current)[0] / 2,
        "first_voltage": voltage[0],
        "second_voltage": voltage[1],
        "power": (current.T * voltage)[0],
        "determinant": inductance.det(),
    }


def sheet(amplitude):
    eplus, eminus, hplus, hminus, k = sp.symbols("ep em hp hm k", real=True)
    solved = sp.solve(
        [
            eplus - eminus,
            hplus - eplus / IMPEDANCE,
            hminus + eminus / IMPEDANCE,
            -hplus + hminus - k,
        ],
        [eplus, eminus, hplus, hminus],
        dict=True,
    )[0]
    electric = solved[eplus].subs(k, amplitude)
    theta = sp.symbols("theta", real=True)
    one = sp.integrate(
        (electric * sp.cos(theta)) ** 2 / IMPEDANCE, (theta, 0, 2 * sp.pi)
    ) / (2 * sp.pi)
    source = sp.integrate(
        -electric * amplitude * sp.cos(theta) ** 2, (theta, 0, 2 * sp.pi)
    ) / (2 * sp.pi)
    assert source == 2 * one
    return {"field": -electric, "one_side": one, "total": source}


def reflection(amplitude):
    theta = sp.symbols("theta", real=True)
    incident = sp.integrate(
        amplitude**2 * sp.cos(theta) ** 2 / IMPEDANCE, (theta, 0, 2 * sp.pi)
    ) / (2 * sp.pi)
    # Magnetic wall amplitude comes from adding each traveling wave with its own direction.
    magnetic = (amplitude / LIGHT + amplitude / LIGHT) * 10**9
    return {
        "magnetic": magnetic,
        "incident": incident,
        "pressure": 2 * incident / LIGHT * 10**9,
        "density": EPS * amplitude**2 * 10**9,
    }


@cache
def calculations():
    field = cylindrical(10, R(1, 25), R(2, 25))
    assigned_field = cylindrical(8, R(1, 20), R(3, 20))
    inductors = mutual()
    assigned = mutual(True)
    wave = sheet(R(1, 100))
    wall = reflection(6)
    source = sp.Matrix([assigned["first_voltage"] + 4, assigned["second_voltage"] + 3])
    return {
        (17, 1): {k: field[k] for k in ["fraction", "field"]},
        (17, 2): {k: field[k] for k in ["boundary", "axis"]},
        (17, 3): {k: field[k] for k in ["before", "surface"]},
        (17, 4): {"energy": field["energy"]},
        (18, 1): {k: inductors[k] for k in ["coupling", "energy"]},
        (18, 2): {
            k: inductors[k] for k in ["first_voltage", "second_voltage", "power"]
        },
        (18, 3): {"determinant": inductors["determinant"]},
        (18, 4): {
            "emf": R(1, 2) * R(1, 5) * 3,
            "current": R(1, 2) * R(1, 5) * 3 / 2,
            "drag": R(3, 20) * R(1, 5) * R(1, 2),
            "power": R(3, 20) ** 2 * 2,
        },
        (19, 1): wave,
        (19, 2): {
            "wavelength": 2 * sp.pi * LIGHT / 10**8,
            "delay": sp.Integer(30) / LIGHT * 10**6,
        },
        (19, 3): {k: wall[k] for k in ["magnetic", "incident", "pressure"]},
        (19, 4): {"density": wall["density"]},
        (20, 1): {k: assigned_field[k] for k in ["field", "boundary", "axis"]},
        (20, 2): {k: assigned_field[k] for k in ["energy", "surface"]},
        (21, 1): {
            "energy": assigned["energy"],
            "first_voltage": assigned["first_voltage"],
            "second_voltage": assigned["second_voltage"],
            "rate": assigned["power"],
        },
        (21, 2): {
            "first_source": source[0],
            "second_source": source[1],
            "loss": 2 * 2**2 + 3 * 1**2,
            "input": (source.T * sp.Matrix([2, 1]))[0],
        },
        (22, 1): sheet(R(3, 100)),
        (22, 2): reflection(R(9, 2)),
        (23, 1): {
            "final": R(2 * 6, 2 + 4),
            "dissipated": R(1, 2) * 2 * 6**2 - R(1, 2) * 6 * 2**2,
            "tau": 2 * R(2 * 4, 2 + 4),
            "current": R(6, 2),
        },
        (23, 2): {},
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_recomputed_em_fields_pass_and_individually_perturbed_fields_fail(qid):
    number, item = map(int, re.fullmatch(r"physics-em-(\d+):depth-(\d+)", qid).groups())
    question, values = NEW[qid], calculations()[number, item]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-12, abs=1e-16)
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


def integrate(rhs, state, end, steps):
    dt = end / steps
    for _ in range(steps):
        a = rhs(state)
        b = rhs([s + dt * k / 2 for s, k in zip(state, a, strict=True)])
        c = rhs([s + dt * k / 2 for s, k in zip(state, b, strict=True)])
        d = rhs([s + dt * k for s, k in zip(state, c, strict=True)])
        state = [
            s + dt * (v + 2 * w + 2 * x + y) / 6
            for s, v, w, x, y in zip(state, a, b, c, d, strict=True)
        ]
    return state


def test_cylindrical_integrals_and_non_equipotential_energy_counterexample():
    field = cylindrical(10, R(1, 25), R(2, 25))
    assert field["axis"] - field["boundary"] == R(5, 2)
    assert field["surface"] == -field["before"]
    # In epsilon=1 reference units, lambda=2*pi*K. Neither selected insulator potential is its weighted mean.
    true = sp.pi * 100 * field["energy"]
    assert sp.simplify(true - sp.pi * 10 * field["axis"]) != 0
    assert sp.simplify(true - sp.pi * 10 * field["boundary"]) != 0


def test_coupled_reference_signs_passivity_and_resistive_energy_integration():
    inductance = sp.Matrix([[R(3, 100), R(3, 100)], [R(3, 100), R(12, 100)]])
    i = sp.Matrix([2, 1])
    reverse = sp.diag(-1, 1)
    assert ((reverse * i).T * (reverse * inductance * reverse) * (reverse * i))[0] == (
        i.T * inductance * i
    )[0]
    invalid = sp.Matrix([[R(3, 100), R(1, 10)], [R(1, 10), R(12, 100)]])
    assert (
        invalid.det() < 0
        and (sp.Matrix([2, -1]).T * invalid * sp.Matrix([2, -1]))[0] < 0
    )
    inverse = inductance.inv()
    u = sp.Matrix([R(403, 100), R(321, 100)])
    resistance = sp.diag(2, 3)
    a = -inverse * resistance
    steady = resistance.inv() * u
    exact = steady + (a / R(10)).exp() * (i - steady)

    def rhs(state):
        first, second, _, _ = state
        b1 = 4.03 - 2 * first
        b2 = 3.21 - 3 * second
        return [
            float(inverse[0, 0]) * b1 + float(inverse[0, 1]) * b2,
            float(inverse[1, 0]) * b1 + float(inverse[1, 1]) * b2,
            4.03 * first + 3.21 * second,
            2 * first**2 + 3 * second**2,
        ]

    result = integrate(rhs, [2.0, 1.0, 0.0, 0.0], 0.1, 1000)
    assert result[:2] == pytest.approx([float(x) for x in exact], abs=1e-10)
    stored = (
        0.5 * 0.03 * result[0] ** 2
        + 0.03 * result[0] * result[1]
        + 0.5 * 0.12 * result[1] ** 2
    )
    assert result[2] - result[3] == pytest.approx(stored - 0.18, abs=1e-10)


def test_source_jump_and_standing_cycle_energy_flux_with_consistent_constants():
    z = float(IMPEDANCE)
    eps = float(EPS)
    c = float(LIGHT)
    samples = 2000
    for phase in [0.0, 0.4, math.pi / 2]:
        electric_energy = magnetic_energy = flux = 0.0
        for j in range(samples):
            t = 2 * math.pi * (j + 0.5) / samples
            electric = 12 * math.sin(phase) * math.sin(t)
            magnetic = 12 / c * math.cos(phase) * math.cos(t)
            electric_energy += eps * electric**2 / 2 / samples
            magnetic_energy += magnetic**2 / (2 * float(MU)) / samples
            flux += electric * magnetic / float(MU) / samples
        assert electric_energy + magnetic_energy == pytest.approx(36 * eps, rel=1e-12)
        assert abs(flux) < 1e-14
    # Source field work and both outward face powers independently averaged from the real fields.
    source = outward = 0.0
    for j in range(samples):
        k = 0.01 * math.cos(2 * math.pi * (j + 0.5) / samples)
        electric = -z * k / 2
        source += -electric * k / samples
        outward += 2 * electric**2 / z / samples
    assert source == pytest.approx(outward, rel=1e-12)
    assert source == pytest.approx(float(sheet(R(1, 100))["total"]), rel=1e-12)


def test_isolated_capacitor_charge_and_integrated_dissipation():
    def rhs(state):
        first, second, _ = state
        current = (first - second) / 2
        return [-current / 2, current / 4, current**2 * 2]  # ms, V, mA and microjoules.

    result = integrate(rhs, [6.0, 0.0, 0.0], 40, 2000)
    assert 2 * result[0] + 4 * result[1] == pytest.approx(12, abs=1e-12)
    energy = 0.5 * 2 * result[0] ** 2 + 0.5 * 4 * result[1] ** 2
    assert 36 - energy == pytest.approx(result[2], abs=1e-7)
    assert result[:2] == pytest.approx([2, 2], abs=3e-6)
    assert result[2] == pytest.approx(24, abs=1e-7)


def test_connected_physics_reports_deliver_with_ungraded_partial_boundary():
    assert len(NEW) == 20
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 6, 0)
    assert MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    # 0.7.0 adds the week-1 dipole and week-9 LC/RLC readings.
    assert len(scheduled) == len(set(scheduled)) == 27
    repository = ContentRepository(ROOT / "content")
    for number in range(17, 24):
        lesson = repository.lesson("physics-em", f"physics-em-{number}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 20 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
