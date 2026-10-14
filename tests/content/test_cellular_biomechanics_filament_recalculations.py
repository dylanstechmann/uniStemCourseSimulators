"""Separate numerical checks of the cytoskeletal filament-mechanics lesson.

<R^2> comes from double-integrating the tangent correlation along the chain,
buckling loads from a shooting method on kappa y'' + F y = 0 with pinned ends,
and the worm-like-chain force from inverting the extension at that force. The
shared registry in test_ai_assisted_checks.py checks the closed forms. The same
AI assistant authored content and checks; this is not human review.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cellular-biomechanics"
LESSON = COURSE / "modules/15-cytoskeletal-filament-mechanics-persistence-entropy-and-buckling.md"
KT_PN_NM = 4.1
KT_J = 4.1e-21


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def bisect(f, low, high):
    assert f(low) * f(high) <= 0
    for _ in range(60):
        mid = (low + high) / 2
        if f(low) * f(mid) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def mean_square_end_to_end(lp, length):
    """<R^2> = double integral of exp(-|s - s'|/lp) over the contour, done as 2 * integral over separations u of (L - u) exp(-u/lp)."""
    panels = 20000
    h = length / panels
    return 2 * h * (
        (length + 0) / 2
        + math.fsum((length - i * h) * math.exp(-i * h / lp) for i in range(1, panels))
    )


def buckling_force(kappa, length, steps=400):
    """Smallest F for which y'' = -(F/kappa) y with y(0) = 0, y'(0) = 1 returns to y(L) = 0."""

    def end_value(force):
        y, v, h = 0.0, 1.0, length / steps
        w = force / kappa
        for _ in range(steps):
            k1 = (v, -w * y)
            k2 = (v + h / 2 * k1[1], -w * (y + h / 2 * k1[0]))
            k3 = (v + h / 2 * k2[1], -w * (y + h / 2 * k2[0]))
            k4 = (v + h * k3[1], -w * (y + h * k3[0]))
            y += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
            v += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        return y

    guess = math.pi**2 * kappa / length**2
    return bisect(end_value, 0.5 * guess, 1.5 * guess)


def buckling_length(kappa, force, step=1e-9):
    """Integrate y'' = -(F/kappa) y from y(0) = 0, y'(0) = 1 until y first returns to zero."""
    w = force / kappa
    y, v, s = 0.0, 1.0, 0.0
    while True:
        k1 = (v, -w * y)
        k2 = (v + step / 2 * k1[1], -w * (y + step / 2 * k1[0]))
        k3 = (v + step / 2 * k2[1], -w * (y + step / 2 * k2[0]))
        k4 = (v + step * k3[1], -w * (y + step * k3[0]))
        y_new = y + step / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        v += step / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if s > step and y_new <= 0:
            return s + step * y / (y - y_new)
        y, s = y_new, s + step


def wlc_extension(force_pn, lp_nm):
    """Fractional extension at a given force, found by bisection on the Marko-Siggia relation."""
    return bisect(
        lambda x: KT_PN_NM / lp_nm * (1 / (4 * (1 - x) ** 2) - 0.25 + x) - force_pn, 0.0, 0.999
    )


def expected_answers():
    p = "cellular-biomechanics-15:"
    r2_semi = mean_square_end_to_end(1.0, 2.0)
    force80 = bisect(lambda f: wlc_extension(f, 50.0) - 0.8, 0.01, 50.0)
    return {
        p + "persistence-length": 2.0e-26 / KT_J * 1e6,
        p + "tangent-correlation": math.exp(-3.0 / 10.0),
        p + "semiflexible-rms-ratio": math.sqrt(r2_semi) / 2.0,
        p + "entropic-spring": 3 * KT_PN_NM / mean_square_end_to_end(0.40, 100.0),
        p + "wlc-force": force80,
        p + "filament-buckling": buckling_force(3.0e-23, 8.0e-6) * 1e12,
        p + "buckling-length": buckling_length(4.0e-26, 1.0e-12) * 1e6,
        p + "bundle-factor": buckling_force(6**2 * 1.0e-23, 5e-6) / buckling_force(1.0e-23, 5e-6),
    }


EXPECTED = expected_answers()


@pytest.mark.parametrize("question_id", sorted(EXPECTED))
def test_filament_keys_with_separate_methods(question_id):
    spec = BANK[question_id]["solution_spec"]
    assert spec["answer"] == pytest.approx(EXPECTED[question_id], abs=spec["tolerance"])


def test_filament_numeric_inventory_is_exhaustive():
    numeric = {
        key
        for key, q in BANK.items()
        if key.startswith("cellular-biomechanics-15:") and q["type"] == "numeric"
    }
    assert numeric == set(EXPECTED) and len(EXPECTED) == 8


def test_filament_lesson_statements_match_numerical_models():
    text = LESSON.read_text(encoding="utf-8")
    assert KT_J * 10e-6 == pytest.approx(4.1e-26) and KT_J * 5e-3 == pytest.approx(2.05e-23)
    assert round(math.exp(-0.2), 2) == 0.82
    assert round(math.sqrt(mean_square_end_to_end(1.0, 1.0)), 3) == 0.858
    r2 = mean_square_end_to_end(50.0, 1000.0)
    assert round(r2 / 1e4, 1) == 9.5 and round(3 * KT_PN_NM / r2 * 1e4, 2) == 1.29
    assert round(bisect(lambda f: wlc_extension(f, 50.0) - 0.5, 0.001, 50.0), 2) == 0.10
    assert round(bisect(lambda f: wlc_extension(f, 50.0) - 0.9, 0.01, 50.0), 2) == 2.10
    assert round(buckling_force(2.05e-23, 5e-6) * 1e12, 1) == 8.1
    assert round(buckling_force(4.1e-26, 1e-6) * 1e12, 2) == 0.40
    assert round(2.0e-23 / KT_J * 1e3, 1) == 4.9
    f10 = buckling_force(2.0e-23, 1e-5) * 1e12
    assert round(f10, 2) == 1.97
    longest = buckling_length(2.0e-23, 5e-12, step=1e-8)
    assert round(longest * 1e6, 2) == 6.28
    assert round(100 * f10) == 197 and round(10 * f10, 1) == 19.7
    for phrase in (
        "**4.1 × 10⁻²⁶ N·m²**",
        "e^(−0.2) = **0.82**",
        "**2.05 × 10⁻²³ N·m²**",
        "is **0.858 L**",
        "k ≈ 3 × 4.1/95 000 = **1.29 × 10⁻⁴ pN/nm**",
        "half extension needs only **0.10 pN**, while 90% extension needs **2.10 pN**",
        "= **8.1 pN**",
        "buckles at **0.40 pN**",
        "about 4.9 mm",
        "= 1.97 pN",
        "= 6.28 μm",
        "buckles near 197 pN",
    ):
        assert phrase in text, phrase
