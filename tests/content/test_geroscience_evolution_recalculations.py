"""Separate numerical checks of the synthetic evolutionary-theory lesson and its keys.

Survival and selection strength are recomputed by numerical integration and
cohort bookkeeping rather than the closed forms the lesson states. The same AI
assistant authored content and checks; this is not human or scientific review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/geroscience"
LESSON = COURSE / "modules/13-why-aging-evolves-selection-shadow-and-trade-offs.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def survival(hazard, age, steps=20000):
    """Euler-integrate dl/da = -hazard * l from l(0) = 1."""
    alive, h = 1.0, age / steps
    for _ in range(steps):
        alive -= hazard * alive * h
    return alive


def mean_lifespan(hazard, horizon=400.0, panels=40000):
    """Integrate l(a) over a long horizon with the trapezoid rule."""
    h = horizon / panels
    values = [math.exp(-hazard * i * h) for i in range(panels + 1)]
    return h * (math.fsum(values) - (values[0] + values[-1]) / 2)


def remaining_reproduction(hazard, age, horizon=400.0, panels=40000):
    h = (horizon - age) / panels
    values = [math.exp(-hazard * (age + i * h)) for i in range(panels + 1)]
    return h * (math.fsum(values) - (values[0] + values[-1]) / 2)


def cohort(p, boost=0.0, last_age=None, horizon=2000):
    """Follow one cohort year by year and total its offspring."""
    alive, offspring = 1.0, 0.0
    for age in range(1, horizon):
        alive *= p
        if last_age is not None and age > last_age:
            break
        offspring += alive * (1 + boost if age <= 2 else 1)
    return offspring


def break_even(p, last_age=8):
    low, high = 0.0, 20.0
    target = cohort(p)
    for _ in range(80):
        middle = (low + high) / 2
        if cohort(p, middle, last_age) < target:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def expected_answers():
    return {
        "geroscience-17:extrinsic-survival": survival(0.5, 4),
        "geroscience-17:mean-extrinsic-lifespan": mean_lifespan(0.25),
        "geroscience-17:relative-selection-strength": remaining_reproduction(0.25, 7)
        / remaining_reproduction(0.25, 1),
        "geroscience-17:late-allele-frequency": 2e-5 / (0.02 * 0.1),
        "geroscience-17:baseline-lifetime-reproduction": cohort(0.8),
        "geroscience-17:late-share": (cohort(0.8) - cohort(0.8, last_age=8))
        / cohort(0.8),
        "geroscience-17:pleiotropic-total": cohort(0.8, 0.2, 8),
        "geroscience-17:break-even-boost": break_even(0.8),
    }


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_evolution_keys_with_separate_methods(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(EXPECTED[question_id], abs=spec["tolerance"])


def test_evolution_numeric_inventory_is_exhaustive():
    numeric = {
        key
        for key, q in BANK.items()
        if key.startswith("geroscience-17:") and q["type"] == "numeric"
    }
    assert numeric == set(EXPECTED) and len(EXPECTED) == 8


def test_evolution_lesson_statements_match_cohort_bookkeeping():
    text = LESSON.read_text(encoding="utf-8")
    assert (round(survival(0.3, 5), 3), round(survival(0.3, 10), 3)) == (0.223, 0.05)
    assert mean_lifespan(0.3) == pytest.approx(10 / 3, rel=1e-5)
    strength = remaining_reproduction(0.3, 6) / remaining_reproduction(0.3, 1)
    assert round(strength, 2) == 0.22
    assert 1e-5 / 0.01 == pytest.approx(0.001)
    assert 1e-5 / (0.01 * 0.05) == pytest.approx(0.02)
    high_base, high_allele = cohort(0.7), cohort(0.7, 0.2, 8)
    low_base, low_allele = cohort(0.95), cohort(0.95, 0.2, 8)
    assert (round(high_base, 3), round(high_allele, 3)) == (2.333, 2.437)
    assert round(high_allele / high_base - 1, 2) == 0.04
    assert (round(low_base, 1), round(low_allele, 2)) == (19.0, 6.77)
    assert round(1 - cohort(0.7, last_age=8) / high_base, 3) == 0.058
    assert round(1 - cohort(0.95, last_age=8) / low_base, 2) == 0.66
    assert (round(break_even(0.7), 2), round(break_even(0.95), 1)) == (0.11, 6.8)
    assert round(cohort(0.8, 0.2, 8), 3) == 3.617 and round(break_even(0.8), 3) == 0.466
    for phrase in (
        "l(5) = e^(−1.5) = **0.223**",
        "l(10) = e^(−3) = **0.050**",
        "S(6) = e^(−1.5) = **0.22**",
        "q ≈ 0.02, twenty times",
        "for a total of **2.437**, about 4% more",
        "only **6.77**",
        "11% when p = 0.7 but about 680% when p = 0.95",
        "4.0 − 0.671 + 0.288 = 3.617 < 4.0",
        "b = 0.466",
        "does not show that any intervention will slow aging in people",
    ):
        assert phrase in text, phrase


def test_evolution_lesson_cites_only_resolved_link_only_references():
    manifest = load(COURSE / "course.json")
    module = next(m for m in manifest["modules"] if m["id"] == "geroscience-module-17")
    registry = {
        s["id"]: s for s in load(ROOT / "content/sources/registry.json")["sources"]
    }
    assert module["source_ids"] == [
        "williams-1957-pleiotropy-senescence",
        "hamilton-1966-moulding-senescence",
        "kirkwood-1977-evolution-ageing",
    ]
    for source_id in module["source_ids"]:
        source = registry[source_id]
        assert source["reuse_mode"] == "link-only-reference"
        assert source["url"].startswith("https://doi.org/10.")
        assert "citation-check script on 2026-10-13" in source["version"]
        assert "geroscience-module-17" in source["mapped_modules"]
    week = manifest["duration"]["weeks"][0]
    assert week["lesson_ids"] == ["geroscience-1", "geroscience-17"]
