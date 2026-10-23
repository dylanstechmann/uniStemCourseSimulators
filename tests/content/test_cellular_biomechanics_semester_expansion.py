"""Independent tensor,membrane and force-history evidence for the original packets."""

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
DIRECTORY = ROOT / "content/courses/cellular-biomechanics"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"cellular-biomechanics-(1[6-9]|2[0-2]):depth-\d+", q["id"])
}
R = sp.Rational


def continuum_reference(normal, shear, gradient, unit_normal):
    b = sp.Matrix(gradient)
    strain = (b + b.T) / 2
    engineering = sp.Matrix([strain[0, 0], strain[1, 1], 2 * strain[0, 1]])
    c = sp.Matrix([[*normal[0], 0], [*normal[1], 0], [0, 0, shear]])
    vector = c * engineering
    stress = sp.Matrix([[vector[0], vector[2]], [vector[2], vector[1]]])
    work = sum(stress[i, j] * strain[i, j] for i in range(2) for j in range(2)) / 2
    return engineering, vector, stress, 1000 * work, stress * sp.Matrix(unit_normal), c


def membrane_reference(kappa, sigma):
    radius = sp.symbols("radius", positive=True)
    energy = sp.pi * kappa / radius + 2 * sp.pi * sigma * radius
    optimum = sp.solve(sp.diff(energy, radius), radius)[0]
    assert sp.diff(energy, radius, 2).subs(radius, optimum) > 0
    return optimum, sp.simplify(energy.subs(radius, optimum))


def inverse_membrane_reference(force, radius):
    kappa, sigma = sp.symbols("kappa sigma", real=True)
    # Solve the original stationary-energy and force equations together.
    equations = [
        -sp.pi * kappa / radius**2 + 2 * sp.pi * sigma,
        sp.pi * kappa / radius + 2 * sp.pi * sigma * radius - force,
    ]
    solution = sp.solve(equations, (kappa, sigma))
    return solution[kappa], solution[sigma]


def history_reference(k0, scale, ramp, force, probability=0.5):
    time = sp.symbols("time", nonnegative=True)
    hazard = sp.integrate(k0 * sp.exp(ramp * time / scale), (time, 0, force / ramp))
    target = 1 - probability
    left, right = 0.0, float(scale) * 20

    # Independent quantile root from the survivor;author used the closed-form quantile.
    def survivor(value):
        return math.exp(
            -float(k0) * float(scale) / float(ramp) * math.expm1(value / float(scale))
        )

    for _ in range(100):
        middle = (left + right) / 2
        if survivor(middle) > target:
            left = middle
        else:
            right = middle
    f = sp.symbols("force", real=True)
    stationary = sp.solve(1 / scale - k0 * sp.exp(f / scale) / ramp, f)[0]
    mode = max(0.0, float(stationary))
    return hazard, sp.exp(-hazard), mode, (left + right) / 2


@cache
def calculations():
    e, v, s, w, tr, c = continuum_reference(
        [[6, 2], [2, 5]],
        3,
        [[R(1, 100), R(1, 25)], [-R(1, 50), R(1, 50)]],
        [R(3, 5), R(4, 5)],
    )
    ae, av, ass, aw, atr, ac = continuum_reference(
        [[5, 1], [1, 4]],
        2,
        [[R(1, 50), -R(1, 100)], [R(3, 100), -R(1, 100)]],
        [R(4, 5), R(3, 5)],
    )
    mr, mf = membrane_reference(72, R(1, 50))
    ik, ist = inverse_membrane_reference(12 * sp.pi, 30)
    ar, af = membrane_reference(50, R(1, 25))
    ak, ast = inverse_membrane_reference(8 * sp.pi, 40)
    h, surv, mode, median = history_reference(R(1, 5), 3, R(6, 5), 3)
    _, _, fast_mode, fast_median = history_reference(R(1, 5), 3, R(12, 5), 3)
    _, _, _, q90 = history_reference(R(1, 5), 3, R(6, 5), 3, 0.9)
    ah, asurv, amode, amedian = history_reference(R(1, 20), 4, R(4, 5), 8)
    _, _, twice_mode, _ = history_reference(R(1, 20), 4, R(8, 5), 8)
    ra, fa = membrane_reference(90, R(1, 20))
    rb, fb = membrane_reference(45, R(1, 10))
    assert fa == fb
    return {
        (16, 1): {"gamma": e[2], "stress_xx": v[0], "stress_yy": v[1], "shear": v[2]},
        (16, 2): {"traction_x": tr[0], "traction_y": tr[1]},
        (16, 3): {"energy": w, "determinant": sp.Matrix([[6, 2], [2, 5]]).det()},
        (16, 4): {"unknown": 2},
        (17, 1): {"radius": mr, "force": mf},
        (17, 2): {"tension": ist, "rigidity": ik},
        (17, 3): {
            "thermal": ik / 4,
            "bending": sp.pi * ik / 30,
            "tension": 2 * sp.pi * ist * 30,
        },
        (17, 4): {"radius_ratio": R(1, 2), "force_ratio": 2},
        (18, 1): {"hazard": h, "survival": surv},
        (18, 2): {"mode": mode, "median": median},
        (18, 3): {"mode": fast_mode, "median": fast_median},
        (18, 4): {"percentile": q90},
        (19, 1): {"stress_xx": av[0], "stress_yy": av[1], "shear": av[2], "energy": aw},
        (19, 2): {
            "traction_x": atr[0],
            "traction_y": atr[1],
            "normal": (sp.Matrix([[R(4, 5), R(3, 5)]]) * atr)[0],
            "tangent": (sp.Matrix([[-R(3, 5), R(4, 5)]]) * atr)[0],
        },
        (20, 1): {"radius": ar, "force": af},
        (20, 2): {"tension": ast, "rigidity": ak, "thermal": ak / 4},
        (21, 1): {"mode": amode, "median": amedian},
        (21, 2): {"hazard": ah, "expected": 100 * asurv, "shift": twice_mode - amode},
        (22, 1): {
            "normal_a": R(7, 100),
            "normal_b": R(1, 10),
            "shear_a": R(3, 50),
            "shear_b": R(3, 100),
        },
        (22, 2): {"radius_a": ra, "radius_b": rb, "force": fa},
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_mechanical_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(
        int, re.fullmatch(r"cellular-biomechanics-(\d+):depth-(\d+)", qid).groups()
    )
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
            response[spec["id"]] = (
                format(value, ".2e") if spec["significant_figures"] else str(int(value))
            )
    assert grade(question, AttemptRequest(response=response)).correct
    for spec in specs:
        if spec["type"] == "numeric":
            wrong = (
                format(float(values[spec["id"]]) * 1.2, ".2e")
                if spec["significant_figures"]
                else str(int(values[spec["id"]]) + 1)
            )
        else:
            wrong = str((spec["answer"] + 1) % 3)
        assert not grade(
            question, AttemptRequest(response={**response, spec["id"]: wrong})
        ).correct


def test_tensor_work_traction_rotation_and_unresolved_coefficients():
    e, v, stress, work, traction, c = continuum_reference(
        [[6, 2], [2, 5]],
        3,
        [[R(1, 100), R(1, 25)], [-R(1, 50), R(1, 50)]],
        [R(3, 5), R(4, 5)],
    )
    assert work == 1000 * (e.T * c * e)[0] / 2 and c.is_positive_definite
    strain = sp.Matrix([[e[0], e[2] / 2], [e[2] / 2, e[1]]])
    rotation = sp.Matrix([[R(3, 5), -R(4, 5)], [R(4, 5), R(3, 5)]])
    rotated_stress = rotation * stress * rotation.T
    rotated_strain = rotation * strain * rotation.T
    assert (
        sum(
            rotated_stress[i, j] * rotated_strain[i, j]
            for i in range(2)
            for j in range(2)
        )
        * 500
        == work
    )
    normal = sp.Matrix([R(3, 5), R(4, 5)])
    assert rotated_stress * (rotation * normal) == rotation * traction
    x, y, omega = sp.symbols("x y omega", real=True)
    rigid = sp.Matrix([-omega * y, omega * x]).jacobian([x, y])
    assert rigid + rigid.T == sp.zeros(2)
    a, b, d, g = sp.symbols("a b d g", real=True)
    coefficients = sp.Matrix([[a, b, 0], [b, d, 0], [0, 0, g]])
    output = coefficients * sp.Matrix([R(1, 100), 0, 0])
    sensitivity = output.jacobian([a, b, d, g])
    assert sensitivity.rank() == 2 and len(sensitivity.nullspace()) == 2
    ae, av, ass, aw, atr, _ = continuum_reference(
        [[5, 1], [1, 4]],
        2,
        [[R(1, 50), -R(1, 100)], [R(3, 100), -R(1, 100)]],
        [R(4, 5), R(3, 5)],
    )
    n = sp.Matrix([R(4, 5), R(3, 5)])
    t = sp.Matrix([-R(3, 5), R(4, 5)])
    assert n * n.dot(atr) + t * t.dot(atr) == atr and aw > 0 and av[1] < 0


def test_membrane_original_energy_minimum_scaling_inverse_and_degeneracy():
    k, s, r = sp.symbols("k sigma radius", positive=True)
    energy = sp.pi * k / r + 2 * sp.pi * s * r
    optimum = sp.sqrt(k / (2 * s))
    force = sp.simplify(energy.subs(r, optimum))
    assert sp.simplify(sp.diff(energy, r).subs(r, optimum)) == 0
    assert sp.diff(energy, r, 2).subs(r, optimum) > 0
    assert sp.simplify(force - 4 * sp.pi * s * optimum) == 0
    assert sp.simplify(optimum.subs(s, 4 * s) / optimum) == R(1, 2)
    assert sp.simplify(force.subs(s, 4 * s) / force) == 2
    assert sp.diff(energy.subs(s, 0), r) < 0
    for observed_force, radius in [(12 * sp.pi, 30), (8 * sp.pi, 40)]:
        ik, ist = inverse_membrane_reference(observed_force, radius)
        recomputed_radius, recomputed_force = membrane_reference(ik, ist)
        assert recomputed_radius == radius and recomputed_force == observed_force
        other_radius, other_force = membrane_reference(ik / 2, 2 * ist)
        assert other_force == observed_force and other_radius == radius / sp.Integer(2)


def test_force_history_normalized_density_boundary_quantiles_and_numerical_ode():
    f, t = sp.symbols("force time", nonnegative=True)
    k0 = R(1, 5)
    scale = sp.Integer(3)
    ramp = R(6, 5)
    integrated = sp.integrate(k0 * sp.exp(ramp * t / scale), (t, 0, f / ramp))
    survivor = sp.exp(-integrated)
    density = k0 * sp.exp(f / scale) * survivor / ramp
    assert sp.simplify(sp.diff(survivor, f) + density) == 0
    assert survivor.subs(f, 0) == 1 and sp.limit(survivor, f, sp.oo) == 0
    z = sp.symbols("z", positive=True)
    transformed = sp.exp(-(z - 1) / 2) / 2
    assert sp.integrate(transformed, (z, 1, sp.oo)) == 1
    for probability in [0.1, 0.5, 0.9]:
        _, _, mode, quantile = history_reference(k0, scale, ramp, 3, probability)
        assert float(survivor.subs(f, quantile)) == pytest.approx(
            1 - probability, abs=2e-15
        )
    assert mode > 0
    slow_log_derivative = 1 / scale - k0 * sp.exp(f / scale) / R(3, 10)
    assert slow_log_derivative.subs(f, 0) < 0 and sp.diff(slow_log_derivative, f) < 0

    # Independent RK4 survivor integration uses time-varying hazard without the closed-form survivor.
    def integrate(steps):
        step = 2.5 / steps
        state = 1.0

        def derivative(time, value):
            return -0.2 * math.exp(1.2 * time / 3) * value

        for i in range(steps):
            time = i * step
            k1 = derivative(time, state)
            k2 = derivative(time + step / 2, state + step * k1 / 2)
            k3 = derivative(time + step / 2, state + step * k2 / 2)
            k4 = derivative(time + step, state + step * k3)
            state += step * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return state

    exact = float(survivor.subs(f, 3))
    assert abs(integrate(80) - exact) < abs(integrate(40) - exact) / 10
    assert integrate(80) == pytest.approx(exact, abs=1e-10)
    expected = calculations()[21, 2]["expected"]
    assert 20 < float(expected) < 21 and float(expected) != int(float(expected))
    spec = next(
        s
        for s in NEW["cellular-biomechanics-21:depth-2"]["solution_spec"]["field_specs"]
        if s["id"] == "expected"
    )
    assert spec["significant_figures"] == 3


def test_competing_constitutive_predictions_and_bibliographic_scope():
    a = sp.Matrix([[6, 2, 0], [2, 5, 0], [0, 0, 3]])
    b = sp.Matrix([[6, 2, 0], [2, 8, 0], [0, 0, R(3, 2)]])
    first = sp.Matrix([R(1, 100), 0, 0])
    biaxial = sp.Matrix([R(1, 100), R(1, 100), 0])
    shear = sp.Matrix([0, 0, R(1, 50)])
    assert a.is_positive_definite and b.is_positive_definite and a * first == b * first
    assert (a * biaxial)[1] == R(7, 100) and (b * biaxial)[1] == R(1, 10)
    assert (a * shear)[2] == R(3, 50) and (b * shear)[2] == R(3, 100)
    ra, fa = membrane_reference(90, R(1, 20))
    rb, fb = membrane_reference(45, R(1, 10))
    assert ra == 30 and rb == 15 and fa == fb == 6 * sp.pi
    registry = json.loads((ROOT / "content/sources/registry.json").read_text())[
        "sources"
    ]
    for suffix, identifier in [("helfrich", "4273690"), ("bell", "347575")]:
        source = next(x for x in registry if x["id"] == f"cellmech-semester-{suffix}")
        assert identifier in source["url"] and not source["imported_assets"]
        assert "full paper text was not examined" in source["third_party_notes"]
        assert source["permissions"] == {
            "linking": True,
            "quotation": False,
            "adaptation": False,
            "redistribution": False,
        }


def test_cellular_mechanics_packets_deliver_as_open_partial_coursework():
    assert len(NEW) == 20
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"]["status"] == "unreviewed"
    scheduled = [lid for w in MANIFEST["duration"]["weeks"] for lid in w["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 24
    repository = ContentRepository(ROOT / "content")
    for number in range(16, 23):
        lesson = repository.lesson(
            "cellular-biomechanics", f"cellular-biomechanics-{number}"
        )
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if number < 19 else 2)
        )
    assert all(
        a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"]
    )
