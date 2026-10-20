"""Separate numerical checks of synthetic fields and public formative keys.

No authoring-script imports. Uses finite differences, root finding, numerical
line/surface/volume integration and the committed boundary observations.
The same AI assistant authored content and checks; this is not human review.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/calculus-3"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def integral(f, a, b, panels=1000):
    h = (b - a) / panels
    return (
        h
        / 3
        * math.fsum(
            (1 if i in (0, panels) else 4 if i % 2 else 2) * f(a + i * h)
            for i in range(panels + 1)
        )
    )


def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)


def partial(f, point, coordinate, h=1e-5):
    before, after = list(point), list(point)
    before[coordinate] -= h
    after[coordinate] += h
    return (f(*after) - f(*before)) / (2 * h)


def gradient(f, point):
    return [partial(f, point, i) for i in range(len(point))]


def hessian(f, point):
    return [
        [
            partial(lambda *p: partial(f, p, i, h=1e-3), point, j, h=1e-3)
            for j in range(2)
        ]
        for i in range(2)
    ]


def bisect(f, a, b):
    assert f(a) * f(b) <= 0
    for _ in range(70):
        middle = (a + b) / 2
        if f(a) * f(middle) <= 0:
            b = middle
        else:
            a = middle
    return (a + b) / 2


def squared_error(points):
    return lambda a, b: math.fsum((y - a * x - b) ** 2 for x, y in points)


def centred_line(points):
    mean_x = math.fsum(x for x, _ in points) / len(points)
    mean_y = math.fsum(y for _, y in points) / len(points)
    slope = math.fsum((x - mean_x) * (y - mean_y) for x, y in points) / math.fsum(
        (x - mean_x) ** 2 for x, _ in points
    )
    return slope, mean_y - slope * mean_x


def best_exponential(points):
    """Direct least squares in y: closed-form c for each k, golden search on k."""

    def error(k):
        e = [math.exp(k * x) for x, _ in points]
        c = math.fsum(y * v for (_, y), v in zip(points, e)) / math.fsum(
            v * v for v in e
        )
        return math.fsum((y - c * v) ** 2 for (_, y), v in zip(points, e)), c

    low, high = -2.0, 0.0
    ratio = (math.sqrt(5) - 1) / 2
    for _ in range(200):
        a, b = high - ratio * (high - low), low + ratio * (high - low)
        if error(a)[0] < error(b)[0]:
            high = b
        else:
            low = a
    k = (low + high) / 2
    sse, c = error(k)
    return c, k, sse


def dot(a, b):
    return math.fsum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def segment_work(field, start, end):
    displacement = [b - a for a, b in zip(start, end)]
    return integral(
        lambda t: dot(
            field(*[a + t * d for a, d in zip(start, displacement)]), displacement
        ),
        0,
        1,
    )


def boundary_work(field, vertices):
    return math.fsum(
        segment_work(field, a, b) for a, b in zip(vertices, vertices[1:] + vertices[:1])
    )


def sphere_flux(field, radius):
    def angular(phi, theta):
        point = (
            radius * math.sin(phi) * math.cos(theta),
            radius * math.sin(phi) * math.sin(theta),
            radius * math.cos(phi),
        )
        normal = [p / radius for p in point]
        return dot(field(*point), normal) * radius**2 * math.sin(phi)

    return integral(
        lambda theta: integral(lambda phi: angular(phi, theta), 0, math.pi, panels=100),
        0,
        2 * math.pi,
        panels=20,
    )


def box_flux(field, lengths):
    total = 0
    for coordinate, width in enumerate(lengths):
        others = [i for i in range(3) if i != coordinate]
        for position, sign in [(0, -1), (width, 1)]:

            def density(a, b):
                point = [0, 0, 0]
                point[coordinate] = position
                point[others[0]] = a
                point[others[1]] = b
                return sign * field(*point)[coordinate]

            total += integral(
                lambda a: integral(
                    lambda b: density(a, b), 0, lengths[others[1]], panels=20
                ),
                0,
                lengths[others[0]],
                panels=20,
            )
    return total


def quadratic(x, y):
    return x * x + 2 * x * y + 3 * y * y - 4 * x - 8 * y


def stationary_quadratic(function=quadratic):
    x, y = 0.0, 0.0
    for _ in range(3):
        g = gradient(function, (x, y))
        h = hessian(function, (x, y))
        determinant = h[0][0] * h[1][1] - h[0][1] * h[1][0]
        x -= (h[1][1] * g[0] - h[0][1] * g[1]) / determinant
        y -= (-h[1][0] * g[0] + h[0][0] * g[1]) / determinant
    return x, y


def feasible_edge_minimum():
    candidates = [(x, y) for x in (0, 0.5) for y in (0, 2)]
    for x in (0, 0.5):

        def edge_rate(y):
            return partial(quadratic, (x, y), 1)

        if edge_rate(0) * edge_rate(2) <= 0:
            candidates.append((x, bisect(edge_rate, 0, 2)))
    for y in (0, 2):

        def edge_rate(x):
            return partial(quadratic, (x, y), 0)

        if edge_rate(0) * edge_rate(0.5) <= 0:
            candidates.append((bisect(edge_rate, 0, 0.5), y))
    return min(candidates, key=lambda point: quadratic(*point))


def lab_data():
    with (COURSE / "labs/boundary-flux.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["face"], []).append(float(row["normal_flux"]))
    means = {key: math.fsum(values) / len(values) for key, values in groups.items()}
    areas = {row["face"]: float(row["area_m2"]) for row in rows}
    return rows, groups, means, areas


def expected_answers():
    answers = {}

    def add(lesson, **values):
        answers.update(
            {
                f"calculus-3-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    add(
        1,
        check=partial(lambda x, y: x * x + 3 * y * y, (1, -1), 1),
        directional_derivative=derivative(
            lambda t: (1 + 0.6 * t) ** 2 * (2 + 0.8 * t), 0
        ),
    )
    add(
        2,
        check=max(
            math.cos(t * 2 * math.pi / 10000) + math.sin(t * 2 * math.pi / 10000)
            for t in range(10000)
        ),
        lagrange_multiplier=max(x / 1000 * (10 - x / 1000) for x in range(10001)),
    )
    add(
        3,
        check=integral(lambda theta: integral(lambda r: r, 0, 1), 0, 2 * math.pi),
        jacobian_polar_area=integral(
            lambda theta: integral(lambda r: r, 0, 3), 0, 2 * math.pi
        ),
    )

    def field(x, y):
        return 100 * math.exp(-(x * x + y * y) / 5000)

    gx = partial(field, (30, 40), 0)
    add(
        5,
        partial_x=gx,
        gradient_magnitude=math.hypot(0.7278, 0.9704),
        directional=derivative(
            lambda t: field(30 + t / math.sqrt(2), 40 + t / math.sqrt(2)), 0
        ),
        fick_flux=10 * 1.213,
        fractional_difference=100 * 10 * 1.213 / 60.65,
    )
    radius = bisect(
        lambda r: derivative(lambda v: 2 * math.pi * v * v + 200 / v, r), 1, 5
    )

    def density(r):
        return 100 * math.exp(-r * r / 5000)

    disk = integral(lambda r: 2 * math.pi * r * density(r), 0, 50)
    whole = integral(lambda r: 2 * math.pi * r * density(r), 0, 500, panels=10000)

    def old_quadratic(x, y):
        return x * x + x * y + y * y - 3 * x

    add(
        6,
        critical_value=old_quadratic(*stationary_quadratic(old_quadratic)),
        vessel_radius=radius,
        multiplier=2 / 2.515,
        polar_total=disk,
        disk_fraction=100 * disk / whole,
    )

    def helix(t):
        return (3 * math.cos(t), 3 * math.sin(t), 4 * t)

    tangent = [derivative(lambda t: helix(t)[i], 0.7) for i in range(3)]
    speed = math.sqrt(dot(tangent, tangent))
    add(
        7,
        vector_length=math.hypot(1, 2, 2),
        cross_z=cross((1, 0, 0), (0, 2, 0))[2],
        helix_speed=speed,
        helix_length=integral(
            lambda t: math.sqrt(
                math.fsum(derivative(lambda u: helix(u)[i], t) ** 2 for i in range(3))
            ),
            0,
            2,
        ),
        plane_distance=abs(dot((2, -1, 2), (0, 0, 0)) - 6) / math.hypot(2, -1, 2),
        tangent_z=tangent[2] / speed,
    )

    def f(x, y):
        return x * x * y + math.sin(y)

    g = gradient(f, (2, 0))
    center = (1, 2)
    delta = (0.1, -0.2)

    def q(x, y):
        return x * x + y * y

    remainder = (
        q(center[0] + delta[0], center[1] + delta[1])
        - q(*center)
        - dot(gradient(q, center), delta)
    )
    add(
        8,
        partial_x=g[0],
        partial_y=g[1],
        mixed=partial(lambda x, y: partial(f, (x, y), 0), (2, 0), 1, h=1e-3),
        path_rate=derivative(lambda t: f(1 + t, t * t), 1),
        tangent_prediction=f(2, 0) + dot(g, (0.1, 0.02)),
        quadratic_error=remainder,
    )
    sx, sy = stationary_quadratic()
    h = hessian(quadratic, (sx, sy))
    boundary_x, boundary_y = feasible_edge_minimum()
    add(
        9,
        stationary_x=sx,
        stationary_y=sy,
        hessian_determinant=h[0][0] * h[1][1] - h[0][1] * h[1][0],
        circle_maximum=max(
            math.cos(t * 2 * math.pi / 10000) * math.sin(t * 2 * math.pi / 10000)
            for t in range(10000)
        ),
        boundary_x=boundary_x,
        boundary_value=quadratic(boundary_x, boundary_y),
    )
    add(
        10,
        triangle_area=integral(
            lambda x: integral(lambda y: 1, 0, 1 - x, panels=20), 0, 1
        ),
        triangle_total=integral(
            lambda x: integral(lambda y: x + y, 0, 1 - x, panels=20), 0, 1
        ),
        ellipse_area=integral(
            lambda t: 0.5
            * (2 * math.cos(t) * 3 * math.cos(t) + 3 * math.sin(t) * 2 * math.sin(t)),
            0,
            2 * math.pi,
        ),
        annular_total=integral(lambda r: 2 * math.pi * r**3, 1, 2),
        ball_volume=integral(lambda z: math.pi * (4 - z * z), -2, 2),
        ball_density_total=integral(
            lambda z: integral(
                lambda r: (r * r + z * z) * 2 * math.pi * r,
                0,
                math.sqrt(max(0, 4 - z * z)),
                panels=20,
            ),
            -2,
            2,
        ),
    )

    def potential_field(x, y):
        return (2 * x * y, x * x)

    def rotation(x, y):
        return (-y, x)

    def vortex(x, y):
        return (-y / (x * x + y * y), x / (x * x + y * y))

    add(
        11,
        potential_work=segment_work(potential_field, (0, 0), (2, 1)),
        curved_work=integral(
            lambda t: dot(potential_field(t, t * t), (1, 2 * t)), 0, 1
        ),
        scalar_length=integral(lambda t: 3 * t * math.hypot(3, 4), 0, 1),
        circle_circulation=integral(
            lambda t: dot(
                rotation(math.cos(t), math.sin(t)), (-math.sin(t), math.cos(t))
            ),
            0,
            2 * math.pi,
        ),
        rectangle_circulation=boundary_work(rotation, [(0, 0), (2, 0), (2, 1), (0, 1)]),
        vortex_circulation=integral(
            lambda t: dot(
                vortex(math.cos(t), math.sin(t)), (-math.sin(t), math.cos(t))
            ),
            0,
            2 * math.pi,
        ),
    )
    area_vector = cross((1, 0, 1), (0, 1, 1))
    add(
        12,
        graph_area=math.sqrt(dot(area_vector, area_vector)),
        vertical_flux=integral(
            lambda x: integral(
                lambda y: dot((0, 0, x + y), area_vector), 0, 1, panels=20
            ),
            0,
            1,
        ),
        constant_flux=dot((2, 0, 5), area_vector),
        sphere_flux=sphere_flux(lambda x, y, z: (x, y, z), 1),
        box_flux=box_flux(lambda x, y, z: (x * x, y, z), (2, 1, 1)),
        diffusion_flux=sphere_flux(lambda x, y, z: (-x, -y, -z), 2),
    )

    def stokes_field(x, y, z):
        return (-y / 2, x / 2, z)

    def inward(x, y, z):
        return (-2 * x, -3 * y, -4 * z)

    transfer = box_flux(inward, (2, 1, 1))
    add(
        13,
        stokes_circle=integral(
            lambda t: dot(
                stokes_field(math.cos(t), math.sin(t), 0),
                (-math.sin(t), math.cos(t), 0),
            ),
            0,
            2 * math.pi,
        ),
        stokes_disk=integral(
            lambda t: dot(
                stokes_field(2 * math.cos(t), 2 * math.sin(t), 0),
                (-2 * math.sin(t), 2 * math.cos(t), 0),
            ),
            0,
            2 * math.pi,
        ),
        tilted_triangle=boundary_work(stokes_field, [(0, 0, 0), (1, 0, 0), (0, 1, 1)]),
        balance_transfer=transfer,
        steady_sink=-transfer / 2,
        storage_rate=-12 * 2 - transfer,
    )
    # Lesson 13: direct surface flux (no divergence theorem) and a clockwise line integral.
    lateral = (2**2 / 3) / 2 * (2 * math.pi * 2 * 3)  # H.n = r^2/(3r) on r=2
    top = (3 / 3) * (math.pi * 2**2)  # H.n = z/3 on z=3; the z=0 face contributes 0
    add(
        13,
        cylinder_flux=lateral + top,
        reverse_circulation=integral(
            lambda t: dot(
                (2 * math.sin(t) / 2, 2 * math.cos(t) / 2, 0),
                (-2 * math.sin(t), -2 * math.cos(t), 0),
            ),
            0,
            2 * math.pi,
        ),
    )
    fit_points = [(1, 3), (2, 4), (3, 4), (4, 6), (5, 8)]
    fit = squared_error(fit_points)
    slope, intercept = centred_line(fit_points)
    rate, _ = centred_line([(0, math.log(6)), (1, math.log(3)), (2, math.log(1.8))])
    curvature = hessian(fit, (slope, intercept))
    add(
        14,
        line_slope=slope,
        line_intercept=intercept,
        minimum_squared_error=fit(slope, intercept),
        squared_error_hessian=curvature[0][0] * curvature[1][1]
        - curvature[0][1] * curvature[1][0],
        log_fit_rate=rate,
        held_y_derivative=derivative(lambda x: x * x + 1 * (2 * x + 1), 1),
        held_z_derivative=derivative(lambda x: x * x + (3 - 2 * x) * 3, 1),
        triple_product_factor=derivative(lambda t: 10 * t / 4, 2),
    )
    _, _, means, areas = lab_data()
    raw = math.fsum(means[k] * areas[k] for k in means)
    corrected = math.fsum((means[k] - 1) * areas[k] for k in means)
    add(
        "lab-01",
        raw_transfer=raw,
        corrected_transfer=corrected,
        steady_sink=-corrected / 2,
        rescaled_box=box_flux(inward, (3, 1, 1)),
    )
    return answers


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_all_numeric_keys_with_separate_methods(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(
        EXPECTED[question_id], abs=max(spec["tolerance"], 1e-8), rel=2e-6
    )


def test_numeric_inventory_is_exhaustive():
    assert set(EXPECTED) == {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert len(EXPECTED) == 72


def test_gradient_directional_derivative_and_local_linearization():
    manifest = load(COURSE / "course.json")
    lesson = next(
        lesson
        for module in manifest["modules"]
        for lesson in module["lessons"]
        if lesson["id"] == "calculus-3-1"
    )
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert "A non-unit vector scales the rate" in text
    assert "The exact change is about" in text

    def field(x, y):
        return x**2 * y + math.sin(y)

    point = (1.0, 0.0)
    grad = gradient(field, point)
    direction = (3 / 5, 4 / 5)
    assert grad == pytest.approx([0, 2], abs=1e-8)
    assert math.hypot(*direction) == pytest.approx(1)
    assert dot(grad, direction) == pytest.approx(1.6)
    h = 1e-5
    directional_difference = (
        field(point[0] + h * direction[0], point[1] + h * direction[1])
        - field(point[0] - h * direction[0], point[1] - h * direction[1])
    ) / (2 * h)
    assert directional_difference == pytest.approx(1.6, abs=1e-8)

    displacement = (0.02, 0.03)
    predicted = dot(grad, displacement)
    actual = field(point[0] + displacement[0], point[1] + displacement[1]) - field(
        *point
    )
    assert predicted == pytest.approx(0.06)
    assert actual == pytest.approx(0.061207, abs=1e-6)
    assert abs(actual - predicted) < 0.002


def test_integrative_field_project_draft_reconciles_area_and_flux_integrals():
    radius = 2.0
    diffusivities = (0.5, 0.75)

    total_amount = 2 * math.pi * (12 * radius**2 / 2 - radius**4 / 4)
    assert total_amount == pytest.approx(40 * math.pi)

    for diffusivity, expected_flux in zip(diffusivities, (8 * math.pi, 12 * math.pi)):
        divergence = 4 * diffusivity
        boundary_density = 2 * diffusivity * radius
        boundary_flux = 2 * math.pi * radius * boundary_density
        volume_flux = divergence * math.pi * radius**2
        assert boundary_flux == pytest.approx(expected_flux)
        assert volume_flux == pytest.approx(expected_flux)

    project = (COURSE / "assessment-specs/integrative-field-project-draft.md").read_text(
        encoding="utf-8"
    )
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    manifest = load(COURSE / "course.json")
    assert manifest["version"] == manifest["history"][-1]["version"]
    assert all("integrative-field-project" not in item["id"] for item in manifest["assessments"])
    assert "Inactive authoring draft" in project
    assert "not a biological measurement or engineering specification" in project
    assert "not scheduled, submitted or graded" in syllabus


def test_directional_derivative_is_invariant_under_consistent_frame_rotation():
    gradient_world = (3.0, 4.0)
    direction_world = (3 / 5, 4 / 5)
    x_axis_rotated = (0.0, 1.0)
    y_axis_rotated = (-1.0, 0.0)

    gradient_rotated = (
        dot(gradient_world, x_axis_rotated),
        dot(gradient_world, y_axis_rotated),
    )
    direction_rotated = (
        dot(direction_world, x_axis_rotated),
        dot(direction_world, y_axis_rotated),
    )

    assert gradient_rotated == pytest.approx((4.0, -3.0))
    assert direction_rotated == pytest.approx((4 / 5, -3 / 5))
    assert dot(gradient_world, direction_world) == pytest.approx(5.0)
    assert dot(gradient_rotated, direction_rotated) == pytest.approx(5.0)
    assert dot(gradient_world, direction_rotated) == pytest.approx(0.0)

    reading = (COURSE / "modules/01-vectors-partial-derivatives-and-gradients.md").read_text(
        encoding="utf-8"
    )
    assert "The dot product is still" in reading
    assert "Mixing the old gradient components" in reading


def test_hessian_classification_and_constrained_global_bound():
    def maximum(x, y):
        return 4 - (x - 1) ** 2 - 2 * (y + 2) ** 2

    stationary = (1.0, -2.0)
    assert gradient(maximum, stationary) == pytest.approx([0, 0], abs=1e-8)
    h_max = hessian(maximum, stationary)
    assert h_max[0] == pytest.approx([-2, 0], abs=1e-6)
    assert h_max[1] == pytest.approx([0, -4], abs=1e-6)
    assert h_max[0][0] < 0 and h_max[1][1] < 0
    assert h_max[0][0] * h_max[1][1] - h_max[0][1] * h_max[1][0] > 0
    assert maximum(*stationary) == pytest.approx(4)

    def product(x, y):
        return x * y

    constrained_gradient = gradient(product, (5.0, 5.0))
    constraint_gradient = (1.0, 1.0)
    multiplier = constrained_gradient[0] / constraint_gradient[0]
    assert constrained_gradient == pytest.approx([5, 5])
    assert constrained_gradient == pytest.approx(
        [multiplier * value for value in constraint_gradient]
    )
    assert product(5, 5) == pytest.approx(25)
    for x in (-10, 0, 3.5, 10, 25):
        assert product(x, 10 - x) == pytest.approx(25 - (x - 5) ** 2)
        assert product(x, 10 - x) <= 25
    text = (COURSE / "modules/02-multivariable-optimization-and-constraints.md").read_text(
        encoding="utf-8"
    )
    assert "makes this second-derivative test inconclusive" in text
    assert "Check feasible boundaries" in text


def test_multiple_integral_jacobians_and_density_units():
    text = (COURSE / "modules/03-multiple-integrals-and-coordinate-transforms.md").read_text(
        encoding="utf-8"
    )
    assert "absolute value $|J|$" in text
    assert "Multiplying the center value by the area" in text

    radius = 3.0
    polar_area = 2 * math.pi * integral(lambda r: r, 0, radius)
    cartesian_area = integral(
        lambda theta: 18 * math.cos(theta) ** 2,
        -math.pi / 2,
        math.pi / 2,
    )
    assert polar_area == pytest.approx(9 * math.pi)
    assert cartesian_area == pytest.approx(polar_area, abs=1e-9)

    # The linear map (u,v) -> (2u,v) stretches unit-disk area by |det J|=2.
    ellipse_jacobian = 2 * 1 - 0 * 0
    assert ellipse_jacobian == pytest.approx(2)
    assert ellipse_jacobian * math.pi == pytest.approx(2 * math.pi)

    total = 2 * math.pi * integral(lambda r: (2 + r) * r, 0, 2)
    area = math.pi * 2**2
    assert total == pytest.approx(40 * math.pi / 3)
    assert total / area == pytest.approx(10 / 3)


def test_line_integral_and_green_theorem_orientation_checks():
    text = (COURSE / "modules/04-line-integrals-flux-and-integral-theorems.md").read_text(
        encoding="utf-8"
    )
    assert "Reversing the path reverses this integral" in text
    assert "Green's flux form" in text
    assert "right-hand rule" in text

    def circle_line_integral(direction):
        def integrand(parameter):
            theta = direction * parameter
            tangent = (-direction * math.sin(theta), direction * math.cos(theta))
            field = (-math.sin(theta), math.cos(theta))
            return dot(field, tangent)

        return integral(integrand, 0, 2 * math.pi)

    parameterized = circle_line_integral(1)
    reversed_parameterization = circle_line_integral(-1)
    green_circulation = 2 * math.pi * integral(lambda r: 2 * r, 0, 1)
    assert parameterized == pytest.approx(2 * math.pi)
    assert green_circulation == pytest.approx(parameterized)
    assert reversed_parameterization == pytest.approx(-2 * math.pi)

    outward_flux = integral(lambda theta: 1.0, 0, 2 * math.pi)
    divergence_flux = 2 * math.pi * integral(lambda r: 2 * r, 0, 1)
    assert outward_flux == pytest.approx(2 * math.pi)
    assert divergence_flux == pytest.approx(outward_flux)
    assert 3 * (4 * math.pi / 3) == pytest.approx(4 * math.pi)


CHECKS = BANK["calculus-3-lab-01:summary"]["solution_spec"]["validation_spec"]["checks"]


@pytest.mark.parametrize("check", CHECKS, ids=lambda check: check["id"])
def test_csv_keys_recompute_supplied_rows(check):
    _, groups, means, _ = lab_data()
    values = groups[check["row_id"]]
    expected = (
        len(values) if check["column"] == "replicates" else means[check["row_id"]]
    )
    assert check["answer"] == pytest.approx(expected, abs=check["tolerance"])
    assert check["calculation"]["values"] == values


def option(key):
    q = BANK[key]
    return q["options"][q["solution_spec"]["answer"]]


def test_normalization_cross_orientation_and_parameter_scale():
    a, b = (1, 0, 0), (0, 2, 0)
    assert cross(a, b) == tuple(-v for v in cross(b, a))
    assert dot(a, cross(a, b)) == dot(b, cross(a, b)) == 0
    assert integral(lambda s: 10, 0, 1) == pytest.approx(
        EXPECTED["calculus-3-7:helix-length"], abs=1e-8
    )
    assert "nonzero length" in option("calculus-3-7:zero-direction")


def test_partial_counterexample_and_chain_rule():
    for h in (1e-3, 1e-5, 1e-7):
        assert h * h / (h * h + h * h) == 0.5
        assert 0 * h / (0 + h * h) == 0
    assert "do not guarantee continuity" in option("calculus-3-8:partials-only")
    assert "f_x x′+f_y y′+f_t" in option("calculus-3-8:explicit-time")
    actual = (2.1) ** 2 * 0.02 + math.sin(0.02)
    assert actual > EXPECTED["calculus-3-8:tangent-prediction"]


def test_hessian_degeneracy_and_feasible_edges():
    for h in (0.01, 0.1):
        assert h**4 + 0 > 0
        assert h**4 - 0 > 0 and 0 - h**4 < 0
    assert "inconclusive" in option("calculus-3-9:degenerate")
    candidates = [
        quadratic(0.5, 7 / 6),
        quadratic(0, 4 / 3),
        quadratic(0.5, 0),
        quadratic(0, 2),
    ]
    assert min(candidates) == pytest.approx(EXPECTED["calculus-3-9:boundary-value"])
    assert min(candidates) > quadratic(1, 1)
    # The circle has two maximum points when coordinates can have both signs.
    for sign in (-1, 1):
        x = y = sign / math.sqrt(2)
        assert x * x + y * y == pytest.approx(1) and x * y == pytest.approx(0.5)
    assert "constraint gradient is nonzero" in option("calculus-3-9:regularity")


def test_coordinate_bounds_and_density_averages():
    reversed_triangle = integral(
        lambda y: integral(lambda x: x + y, 0, 1 - y, panels=20), 0, 1
    )
    assert reversed_triangle == pytest.approx(EXPECTED["calculus-3-10:triangle-total"])
    assert 1 < EXPECTED["calculus-3-10:annular-total"] / (3 * math.pi) < 4
    assert EXPECTED["calculus-3-10:ball-density-total"] / EXPECTED[
        "calculus-3-10:ball-volume"
    ] == pytest.approx(12 / 5)
    assert "absolute Jacobian determinant" in option("calculus-3-10:absolute-jacobian")
    assert "ρ²sinφ" in option("calculus-3-10:spherical-angle")


def test_path_reversal_potential_and_hole():
    def f(x, y):
        return (2 * x * y, x * x)

    assert segment_work(f, (2, 1), (0, 0)) == -EXPECTED["calculus-3-11:potential-work"]
    assert segment_work(f, (0, 0), (2, 0)) + segment_work(
        f, (2, 0), (2, 1)
    ) == pytest.approx(4)
    assert "simply connected" in option("calculus-3-11:potential-domain")
    assert "singular at the enclosed origin" in option("calculus-3-11:vortex-hole")
    # A clockwise inner vortex circle cancels the outer circulation on an annulus.
    inner = integral(lambda t: -1, 0, 2 * math.pi)
    assert inner + EXPECTED["calculus-3-11:vortex-circulation"] == pytest.approx(
        0, abs=1e-12
    )


def test_surface_graph_sign_and_divergence():
    upward = cross((1, 0, 1), (0, 1, 1))
    downward = tuple(-x for x in upward)
    assert dot((2, 0, 5), downward) == -dot((2, 0, 5), upward)
    volume_flux = integral(lambda x: 2 * x + 2, 0, 2)
    assert volume_flux == pytest.approx(EXPECTED["calculus-3-12:box-flux"])
    assert "entire closed outward-oriented" in option("calculus-3-12:closed")
    assert "Include derivatives of D" in option("calculus-3-12:variable-diffusion")


def test_stokes_triangle_and_singular_shell():
    area_vector = tuple(v / 2 for v in cross((1, 0, 0), (0, 1, 1)))
    assert dot((0, 0, 1), area_vector) == pytest.approx(
        EXPECTED["calculus-3-13:tilted-triangle"]
    )

    def stokes(x, y, z):
        return (-y / 2, x / 2, z)

    assert boundary_work(stokes, [(0, 0, 0), (0, 1, 1), (1, 0, 0)]) == pytest.approx(
        -0.5
    )

    def radial(x, y, z):
        return tuple(c / (x * x + y * y + z * z) ** 1.5 for c in (x, y, z))

    outer = sphere_flux(radial, 1)
    inner = -sphere_flux(radial, 0.5)
    assert outer == pytest.approx(4 * math.pi, abs=1e-6)
    assert outer + inner == pytest.approx(0, abs=1e-10)
    assert "adds an inner boundary" in option("calculus-3-13:singularity")


def test_storage_and_source_assumptions():
    q = EXPECTED["calculus-3-13:balance-transfer"]
    assert -9 * 2 - q == pytest.approx(0)
    assert -12 * 2 - q == EXPECTED["calculus-3-13:storage-rate"]
    assert (2 - 9) * 2 == -14
    assert "source, storage, geometry" in option("calculus-3-13:inference")


def test_lab_normals_areas_balanced_rows_and_offset():
    rows, groups, means, areas = lab_data()
    expected = {
        "x0": ((-1, 0, 0), 1, 0),
        "x2": ((1, 0, 0), 1, -4),
        "y0": ((0, -1, 0), 2, 0),
        "y1": ((0, 1, 0), 2, -3),
        "z0": ((0, 0, -1), 2, 0),
        "z1": ((0, 0, 1), 2, -4),
    }
    assert len(rows) == 18 and all(len(v) == 3 for v in groups.values())
    for row in rows:
        normal, area, density = expected[row["face"]]
        assert tuple(float(row[k]) for k in ("nx", "ny", "nz")) == normal
        assert float(row["area_m2"]) == area
        assert float(row["normal_flux"]) == pytest.approx(
            density + 1 + (int(row["replicate"]) - 2) * 0.1
        )
        assert float(row["offset"]) == 1
    assert sum(areas.values()) == 10
    assert (
        EXPECTED["calculus-3-lab-01:raw-transfer"]
        - EXPECTED["calculus-3-lab-01:corrected-transfer"]
        == 10
    )
    assert math.fsum((means[k] - 1) * areas[k] for k in means) == pytest.approx(-9 * 2)


def test_least_squares_and_held_variable_lesson_statements():
    text = (
        COURSE / "modules/14-least-squares-and-constrained-partial-derivatives.md"
    ).read_text(encoding="utf-8")
    lesson_points = [(1, 2), (2, 3), (3, 5), (4, 6)]
    fit = squared_error(lesson_points)
    a, b = centred_line(lesson_points)
    assert (round(a, 6), round(b, 6), round(fit(a, b), 6)) == (1.4, 0.5, 0.2)
    assert all(
        partial(fit, (a, b), i) == pytest.approx(0, abs=1e-6) for i in range(2)
    )
    assert math.fsum(x * (y - a * x - b) for x, y in lesson_points) == pytest.approx(0)
    h = hessian(fit, (a, b))
    assert h[0][0] * h[1][1] - h[0][1] ** 2 == pytest.approx(80, rel=1e-4)
    decay = [(0, 5), (1, 3), (2, 2)]
    k, log_c = centred_line([(x, math.log(y)) for x, y in decay])
    assert (round(k, 3), round(math.exp(log_c), 2)) == (-0.458, 4.91)
    c_direct, k_direct, sse_direct = best_exponential(decay)
    sse_log = math.fsum((y - math.exp(log_c + k * x)) ** 2 for x, y in decay)
    assert (round(c_direct, 2), round(k_direct, 3)) == (4.97, -0.474)
    assert (round(sse_direct, 4), round(sse_log, 4)) == (0.0152, 0.0203)
    assert derivative(lambda x: x * 2 * (x + 2), 1) == pytest.approx(8)
    assert derivative(lambda x: x * (3 - x) * 3, 1) == pytest.approx(3)
    factors = (
        derivative(lambda v: 10 * 1 / v, 5),
        derivative(lambda t: 10 * t / 2, 1),
        derivative(lambda p: p * 5 / 10, 2),
    )
    assert factors[0] * factors[1] * factors[2] == pytest.approx(-1)
    worked = [(0, 1), (1, 3), (2, 4), (3, 6)]
    wa, wb = centred_line(worked)
    shift = squared_error(worked)(wa, wb + 0.1) - squared_error(worked)(wa, wb)
    assert (round(wa, 6), round(wb, 6), round(shift, 6)) == (1.6, 1.1, 0.04)
    for phrase in (
        "**a = 1.4**",
        "**b = 0.5**",
        "**D = 0.20**",
        "**80**",
        "k = **−0.458**",
        "**4.91**",
        "c ≈ 4.97 and k ≈ −0.474",
        "0.0152 in y against 0.0203",
        "**8** and **3**",
        "(∂V/∂T)_P = 10/P = **5**",
        "a = 1.6 and b = 1.1",
    ):
        assert phrase in text


def test_schedule_and_conservative_labels():
    c = load(COURSE / "course.json")
    assert c["version"] == c["history"][-1]["version"] and c["maturity"] == "partial"
    assert (
        c["review"]["status"] == "unreviewed"
        and c["grading_policy"]["mode"] == "formative-only"
    )
    lessons = {lesson["id"] for module in c["modules"] for lesson in module["lessons"]}
    weeks = c["duration"]["weeks"]
    assert [w["week"] for w in weeks] == list(range(1, 15))
    assert {lid for w in weeks for lid in w["lesson_ids"]} == lessons
    assert weeks[-1]["assessment_ids"] == [
        "calculus-3-week14-flux-lab",
        "calculus-3-case",
        "calculus-3-field-project",  # 0.5.0: the optional project's milestone record
    ]
    # 15 topic and lab lessons plus the optional field project guide added in 0.5.0.
    assert len(lessons) == 16 and len(BANK) == 115
    cards = len(load(COURSE / "question-banks/retrieval-cards.json")["cards"])
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert (
        f"There are {len(lessons)} readings, {len(BANK)} public practice items and {cards} retrieval cards"
        in syllabus
    )
    assert "Weeks 1, 5, 8, 10 and 13 now have expanded" in syllabus
    assert "No compact prototype readings remain" in syllabus
