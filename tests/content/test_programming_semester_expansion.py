"""Independent arithmetic and algorithm checks for the deeper numerical coursework.

These are agent-run checks, not independent human review or learner-code grading.
"""

from __future__ import annotations

import ast
import csv
import json
import math
import re
import sys
from fractions import Fraction
from pathlib import Path
from statistics import mean, variance

import pytest
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/programming"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())["questions"]}
NEW = {qid: q for qid, q in BANK.items() if re.fullmatch(r"programming-(?:1[6-9]|2[0-6]):method-\d+", qid)}


def multiply(matrix, vector):
    return [sum(a * x for a, x in zip(row, vector, strict=True)) for row in matrix]


def independent_values():
    def cubic(x):
        return x * x * x
    def central(x, h):
        return (cubic(x + h) - cubic(x - h)) / (2 * h)
    fine, coarse = central(1, .1), central(1, .2)
    h = (.000032 / 4) ** (1 / 3)
    outputs = [1, 2, 3, 4, 5]
    second, fourth = Fraction(1, 3), Fraction(1, 5)
    mc_variance = fourth - second * second
    # E[(u²-u+1/2)²] by integrating its expanded polynomial exactly.
    paired_second = Fraction(1, 5) - Fraction(1, 2) + Fraction(2, 3) - Fraction(1, 2) + Fraction(1, 4)
    paired_variance = paired_second - second * second
    a = [[Fraction(4), Fraction(1)], [Fraction(2), Fraction(3)]]
    b = [Fraction(6), Fraction(8)]
    multiplier = a[1][0] / a[0][0]
    x2 = (b[1] - multiplier * b[0]) / (a[1][1] - multiplier * a[0][1])
    x1 = (b[0] - a[0][1] * x2) / a[0][0]
    first_jacobi = [Fraction(2, 4), Fraction(1, 4)]
    second_jacobi = [(2 + first_jacobi[1]) / 4, (1 + first_jacobi[0]) / 4]
    change = max(abs(x - y) for x, y in zip(first_jacobi, second_jacobi, strict=True))
    matrix = [[4, 1], [1, 4]]
    power1 = multiply(matrix, [1, 0])
    power2 = multiply(matrix, power1)
    power3 = multiply(matrix, power2)
    rayleigh = sum(x * y for x, y in zip(power2, power3, strict=True)) / sum(x*x for x in power2)
    # Derive the Newton correction via elimination from the rehearsal equations.
    dx = Fraction(1, 6)
    dy = dx + 1
    xnew, ynew = 3 + dx, dy
    residual = xnew*xnew + ynew*ynew - 10
    full_point = [2 + .25, 1.25]
    half_point = [2 + .125, .625]
    def norm_f(point):
        x, y = point
        return max(abs(x*x + y*y - 5), abs(x-y-1))
    start, step = 2, .1
    euler = start + step * (-3 * start)
    heun = start + step / 2 * (-3 * start - 3 * euler)
    backward = start / (1 + 3 * step)
    normalized = (.82 - .8) / (.001 + .01 * max(1, .82))
    with (DIRECTORY / "assignments/semester-observations.csv").open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    seen, accepted = set(), []
    for row in rows:
        value = float(row["length"])
        if row["record_id"] in seen:
            continue
        seen.add(row["record_id"])
        if not math.isfinite(value) or value <= 0 or row["unit"] not in {"um", "mm"}:
            continue
        accepted.append((row["specimen_id"], value / 1000 if row["unit"] == "um" else value))
    grouped = {name: mean(value for specimen, value in accepted if specimen == name)
               for name, _ in accepted}
    states_a = math.exp(-1)
    states_b = math.exp(-1) * (-math.expm1(-1))
    # Simpson integration independently checks the uniform-parameter expectation.
    intervals = 1000
    expectation = .4 / intervals / 3 * sum(
        (1 if i in {0, intervals} else 4 if i % 2 else 2) * math.exp(-(.8 + .4*i/intervals))
        for i in range(intervals + 1)) / .4
    return {
        (16, 1): {"forward": (cubic(1.2)-cubic(1))/.2, "central": coarse},
        (16, 2): {"extrapolated": (4*fine-coarse)/3, "fine_error": abs(fine-coarse)/3},
        (16, 3): {"step": h, "bound": 2*h*h+.000032/h},
        (16, 4): {"sd": math.sqrt(2*.02**2/(2*.1)**2)},
        (17, 1): {"mean": mean(outputs), "variance": variance(outputs), "se": math.sqrt(variance(outputs)/len(outputs))},
        (17, 2): {"target": float(second), "se": math.sqrt(float(mc_variance)/10000), "count": 10000*3**2},
        (17, 3): {"upper": 1-pow(.05, Fraction(1, 500))},
        (17, 4): {"variance": float(paired_variance), "factor": float(mc_variance / 2 / paired_variance)},
        (18, 1): {"multiplier": float(multiplier), "x1": float(x1), "x2": float(x2)},
        (18, 2): {"first_x": float(second_jacobi[0]), "second_x": float(second_jacobi[1]), "bound": float(change/3)},
        (18, 3): {"entries": sum(1 for i in range(1000) for j in range(max(0,i-1), min(1000,i+2))), "bytes": 8*(1000+999+999)},
        (18, 4): {},
        (19, 1): {"first": power2[0], "second": power2[1], "ratio": 3/5},
        (19, 2): {"quotient": rayleigh},
        (19, 3): {"residual": max(abs(x-y) for x,y in zip(multiply(matrix,[1,0]),[4,0],strict=True)), "relative": 1/5},
        (19, 4): {"first": 1/(2-1), "second": 1/(5-1)},
        (20, 1): {"dx": float(dx), "dy": float(dy), "residual": float(residual)},
        (20, 2): dict(zip(["first", "second"], multiply([[6,2],[1,-1]], [1,-1]), strict=True)),
        (20, 3): {"full": norm_f(full_point), "half": norm_f(half_point)},
        (20, 4): {},
        (21, 1): {"euler": euler, "heun": heun, "backward": backward},
        (21, 2): {"error": normalized, "next": .2*.9/math.sqrt(normalized)},
        (21, 3): {"multiplier": 1-1000*.01, "bound": 2/1000},
        (21, 4): {},
        (22, 1): {"accepted": len(accepted), "excluded": len(rows)-len(accepted), "specimens": len(grouped)},
        (22, 2): {"s1": grouped["S1"], "s2": grouped["S2"], "overall": mean(grouped.values())},
        (23, 1): {"value": .25**2+.25+1, "integral": float(Fraction(1,3)+Fraction(1,2)+1)},
        (23, 2): {"error": .34375-1/3, "extrapolated": (4*.34375-.375)/3},
        (24, 1): {"mean": float(second), "probability": 1-math.sqrt(.64)},
        (24, 2): {"expectation": float(second)+.01, "bias": .01},
        (25, 1): {"center": multiply([[2,-1,0],[-1,2,-1],[0,-1,2]],[1,2,1])[1]},
        (25, 2): {"small": 2-2*math.cos(math.pi/4), "large": 2-2*math.cos(3*math.pi/4)},
        (26, 1): {"a": states_a, "b": states_b, "c": 1-states_a-states_b},
        (26, 2): {"equal": states_a, "mean": expectation},
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_new_checkpoint_numeric_answers_recompute_and_grade(qid):
    number, item = map(int, re.fullmatch(r"programming-(\d+):method-(\d+)", qid).groups())
    values = independent_values()[(number, item)]
    question = NEW[qid]
    numeric = {spec["id"]: spec for spec in question["solution_spec"]["field_specs"] if spec["type"] == "numeric"}
    assert set(values) == set(numeric)
    response = {}
    for spec in question["solution_spec"]["field_specs"]:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        elif spec["significant_figures"] is None:
            assert float(values[spec["id"]]).is_integer()
            response[spec["id"]] = str(int(values[spec["id"]]))
        else:
            assert values[spec["id"]] == pytest.approx(spec["answer"], rel=1e-8, abs=1e-12)
            response[spec["id"]] = format(values[spec["id"]], ".2e")
    result = grade(question, AttemptRequest(response=response))
    assert result.correct, result.feedback
    for fid, value in values.items():
        assert not grade(question, AttemptRequest(response={**response, fid: format(value*1.2, ".2e")})).correct


def test_new_coursework_is_scheduled_and_delivered_without_activating_grades():
    assert len(NEW) == 34
    assert MANIFEST["version"] == "0.6.0"
    assert MANIFEST["review"]["status"] == "unreviewed" and MANIFEST["maturity"] == "partial"
    weeks = MANIFEST["duration"]["weeks"]
    assert len(weeks) == 14
    scheduled = [lid for week in weeks for lid in week["lesson_ids"]]
    assert len(scheduled) == len(set(scheduled)) == 28
    assert all(a["mode"] in {"practice", "self-assessment"} for a in MANIFEST["assessments"])
    content = ContentRepository(ROOT / "content")
    for number in range(16, 27):
        lesson = content.lesson("programming", f"programming-{number}")
        assert len(lesson.questions) == (4 if number < 22 else 2)
        assert len(lesson.retrieval_cards) == len(lesson.questions)
        assert len(lesson.markdown.split()) >= 700
    resource = "assignments/semester-observations.csv"
    assert content.learner_resource("programming", resource) == (DIRECTORY / resource).read_bytes()


@pytest.mark.parametrize("slug,name", [("differentiation", "central_difference"), ("monte-carlo", "estimate_square_mean")])
def test_original_reference_functions_have_independent_contract_checks(slug, name):
    text = (DIRECTORY / f"modules/{slug}.md").read_text()
    source = text.split("```python",1)[1].split("```",1)[0]
    tree = ast.parse(source)
    namespace = {}
    exec(compile(tree, f"original-{slug}", "exec"), namespace)
    function = namespace[name]
    if slug == "differentiation":
        assert function(lambda x: 3*x+4, 2, .01) == pytest.approx(3)
        assert function(lambda x: x**3, 1, .1) == pytest.approx(3.01)
        with pytest.raises(ValueError):
            function(lambda x: x, 1e20, 1e-10)
        with pytest.raises(ValueError):
            function(lambda x: math.inf, 1, .1)
    else:
        first = function(10000, 812)
        assert first == function(10000, 812)
        assert first != function(10000, 813)
        # Deterministic stream check; no probabilistic flaky test against one random mean.
        import random
        rng = random.Random(812)
        values = [rng.random()**2 for _ in range(10000)]
        assert first == pytest.approx((mean(values), math.sqrt(variance(values)/len(values))))
        with pytest.raises(ValueError):
            function(True, 812)


def test_current_package_snapshot_pins_version_and_hashes():
    sys.path.insert(0, str(ROOT / "tools"))
    from course_package_digest import compute_digest
    actual = compute_digest("programming")
    snapshot = (ROOT / "docs/PROGRAMMING_REVIEW_SNAPSHOT.md").read_text()
    assert actual["content_version"] == "0.6.0"
    assert actual["package_sha256"] in snapshot
    assert actual["manifest_sha256"] in snapshot
    assert (ROOT / "docs/PROGRAMMING_REVIEW_SNAPSHOT-0.5.0.md").is_file()
