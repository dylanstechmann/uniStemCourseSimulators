"""Laboratory Measurement 0.1.0: recomputed keys, stated numbers, schedule, project route, comparator and grading.

Each numeric key is recomputed here from its formula (C × V × M, C₁V₁ = C₂V₂, the Tanaka water-density formula and
the buoyancy factor Z, the Nernst slope, Henderson–Hasselbalch, Beer–Lambert, least squares), not read from the item.
Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
import re
import statistics
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/lab-measurement"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
CASES = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
READINGS = {lesson["id"]: (COURSE / lesson["reading"]).read_text(encoding="utf-8")
            for module in MANIFEST["modules"] for lesson in module["lessons"]}
SYLLABUS = (COURSE / "syllabus.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


def rho_water(t):
    a1, a2, a3, a4, a5 = -3.983035, 301.797, 522528.9, 69.34881, 999.974950
    return a5 * (1 - (t + a1) ** 2 * (t + a2) / (a3 * (t + a4))) / 1000


def z_factor(t, air=0.0012, weights=8.0):
    return (1 / (rho_water(t) - air)) * (1 - air / weights)


def fit(xs, ys):
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return slope, my - slope * mx


NERNST_25 = 8.314462618 * 298.15 * math.log(10) / 96485.33212 * 1000
CURVE = fit([0, 0.125, 0.25, 0.5, 1.0], [0.000, 0.081, 0.158, 0.322, 0.640])
PROJECT = fit([0, 0.100, 0.200, 0.400], [0.000, 0.061, 0.124, 0.247])

# Recomputed key and one named misconception for every numeric item.
KEYS = {
    "1:nacl-mass": (0.200 * 0.250 * 58.44, 0.200 * 250 * 58.44),  # volume left in mL
    "1:hydrate-mass": (0.0500 * 0.500 * 249.69, 0.0500 * 0.500 * 159.61),  # anhydrous molar mass
    "1:hydrate-error": (3.99 / 249.69 / 0.500, 0.0500),  # the intended concentration
    "1:purity": (0.0250 * 0.500 * 238.30 / 0.990, 0.0250 * 0.500 * 238.30 * 0.990),  # multiplying by the assay
    "1:conc-acid": (1000 * 1.84 * 0.960 / 98.08, 1000 * 0.960 / 98.08),  # ignoring density
    "1:percent-to-molar": (50.0 / 180.16 * 1000, 5.00 / 180.16 * 1000),  # % w/v read as g/L
    "1:small-mass": (25.0e-6 * 0.0200 * 350 * 1000, 25.0e-6 * 20.0 * 350 * 1000),  # volume left in mL
    "2:c1v1": (15.0e-3 * 50.0 / 1.00 * 1000, 15.0e-3 * 50.0 / 1.00),  # answer left in mL
    "2:serial-total": (10 ** 4, 9 ** 4),  # 50 into 450 read as ninefold
    "2:fivefold": (2.00 / 5 ** 3, 2.00 / 4 ** 3),  # 200 into 800 read as fourfold
    "2:back-calc": (83 / (0.100 * 1e-6) / 1e8, 83 / 1e-6 / 1e8),  # forgetting the plated volume
    "2:systematic-compound": ((1.015 ** 6 - 1) * 100, 1.5),  # one step only
    "2:random-compound": (0.80 * math.sqrt(9), 0.80 * 9),  # adding instead of quadrature
    "2:parallel-volume": (0.160 * 250 / 2.00, 0.160 * 250 / 0.200),  # wrong stock
    "3:z-20": (z_factor(20.0), 1 / 0.998207),  # density only, no buoyancy
    "3:mean-volume": (497.6 * 1.0033, 497.6),  # milligrams taken as microlitres
    "3:systematic": ((499.2 - 500) / 500 * 100, 0.16),  # sign dropped
    "3:cv": (0.95 / 499.2 * 100, 0.95),  # absolute instead of relative
    "3:relative-low-end": (0.30 / 5.0 * 100, 0.30 / 100 * 100),  # wrong reference volume
    "4:min-weight": (2 * 0.050 / 0.0010, 0.050 / 0.0010),  # without the factor of 2
    "4:relative-uncertainty": (2 * 0.10 / 5.0 * 100, 0.10 / 5.0 * 100),  # without the factor of 2
    "4:by-difference": ((15.2318 - 14.9874) * 1000, 14.9874 * 1000 - 14000),  # unrelated subtraction
    "4:buoyancy": (2.0000 * (1 - 0.0012 / 8.0) / (1 - 0.0012 / 0.998), 2.0000 * (1 - 0.0012 / 0.998)),  # inverted
    "5:nernst-37": (8.3145 * 310.15 * math.log(10) / 96485 * 1000, NERNST_25),  # 25 °C value
    "5:slope-percent": ((168.0 - 2.5) / (7.00 - 4.01) / 59.16 * 100, (168.0 - 2.5) / 3.00 / 59.16 * 100),
    "5:sample-ph": (7.00 - (110.0 - 2.5) / ((168.0 - 2.5) / 2.99), 7.00 + (110.0 - 2.5) / ((168.0 - 2.5) / 2.99)),
    "5:hh-ratio": (10 ** (5.00 - 4.76), 10 ** (4.76 - 5.00)),  # inverted ratio
    "5:hh-mass": (0.0500 * (10 ** -0.20 / (1 + 10 ** -0.20)) * 141.96, 0.0500 * (1 / (1 + 10 ** -0.20)) * 141.96),
    "5:tris-temp": (7.60 - 0.028 * 12, 7.60 + 0.028 * 12),  # sign of the coefficient
    "6:transmittance": (-math.log10(0.250), -math.log(0.250)),  # natural logarithm
    "6:beer-lambert": (0.467 / 6220 * 1e6, 0.467 * 6220),  # multiplying
    "6:path-length": (0.467 * 0.300, 0.467 / 0.300),  # dividing
    "6:interpolate": ((0.415 - 0.0030) / 0.0124, (0.415 + 0.0030) / 0.0124),  # intercept sign
    "6:dilution-back": (0.315 * 20, 0.315 * 19),  # one-plus-nineteen reading
    "project:rehearsal-mass": (0.0200 * 0.250 * 238.30 / 0.995, 0.0200 * 0.250 * 238.30),  # no purity correction
    "project:rehearsal-pipette": ((99.12 * 1.0035 - 100) / 100 * 100, (99.12 - 100) / 100 * 100),  # no Z
    "project:rehearsal-slope": ((166.9 - 0.8) / 2.99 / 59.16 * 100, (166.9 - 0.8) / 3.00 / 59.16 * 100),
    "project:rehearsal-dilution": ((0.215 + 0.0002) / 0.6183 * 4, (0.215 + 0.0002) / 0.6183 * 5),
}


def item_id(key):
    lesson, slug = key.split(":")
    return f"lab-measurement-{lesson}:{slug}"


def shown(value, sig):
    if not sig:
        return f"{value:g}"
    decimals = max(0, sig - 1 - math.floor(math.log10(abs(value))))
    return f"{value:.{decimals}f}"


def test_every_numeric_item_has_a_recomputed_key():
    numeric = {qid for qid, q in BANK.items() if q["type"] == "numeric"}
    assert numeric == {item_id(key) for key in KEYS}


@pytest.mark.parametrize("key", sorted(KEYS))
def test_numeric_keys_match_recomputation_and_reject_the_misconception(key):
    item = BANK[item_id(key)]
    spec = item["solution_spec"]
    sig = spec["significant_figures"]
    value, wrong = KEYS[key]
    if sig:
        assert float(shown(value, sig)) == pytest.approx(spec["answer"], rel=1e-9), (value, spec["answer"])
        words = {3: "three", 4: "four", 5: "five"}[sig]
        assert item["prompt"].endswith(f"to {words} significant figures."), item["prompt"]
    else:
        assert value == pytest.approx(spec["answer"]) and item["prompt"].endswith("Enter the number only.")
    assert grade(item, AttemptRequest(response=shown(spec["answer"], sig))).correct
    assert not grade(item, AttemptRequest(response=shown(wrong, sig))).correct, shown(wrong, sig)
    if sig:
        # One digit too many is not accepted where significant figures are checked.
        assert not grade(item, AttemptRequest(response=shown(spec["answer"], sig) + "0")).correct


def test_choice_items_accept_only_the_key_and_multiple_select_uses_partial_credit():
    for qid, item in BANK.items():
        if item["type"] == "single_choice":
            accepted = [i for i in range(len(item["options"])) if grade(item, AttemptRequest(response=str(i))).correct]
            assert accepted == [item["solution_spec"]["answer"]], qid
        elif item["type"] == "multiple_select":
            key = item["solution_spec"]["answer"]
            assert item["points"] == 2 and item["solution_spec"]["partial_credit"] == "correct-minus-incorrect-clamped-v1"
            wrong = next(i for i in range(len(item["options"])) if i not in key)
            full = grade(item, AttemptRequest(response=key)).score
            assert full == pytest.approx(2.0)
            assert grade(item, AttemptRequest(response=[*key, wrong])).score < full, qid
            assert grade(item, AttemptRequest(response=[wrong])).score == 0, qid


def test_lesson_one_numbers():
    text = READINGS["lab-measurement-1"]
    assert round(0.150 * 0.500 * 58.44, 2) == 4.38 and round(9 / 58.44 * 1000) == 154
    assert round(0.100 * 0.250 * 147.01, 2) == 3.68 and round(0.100 * 110.98 / 147.01, 4) == 0.0755
    assert round(0.200 * 121.14 / 0.980, 1) == 24.7 and round(1000 * 1.18 * 0.370 / 36.46, 1) == 12.0
    assert round(250 / (1000 * 1.18 * 0.370 / 36.46), 1) == 20.9
    assert round(0.0250 * 0.200 * 246.47 / 0.995, 2) == 1.24
    stated(text, "4.38 g", "154 mM", "3.68 g", "0.0755 M", "24.7 g", "12.0 mol/L", "20.9 mL", "0.200 mg", "4.00 mg", "1.24 g")


def test_lesson_two_numbers():
    text = READINGS["lab-measurement-2"]
    assert 5 ** 4 == 625 and round(47 / (0.1 * 1e-5)) == 47_000_000
    assert round(math.sqrt(6) * 1.0, 1) == 2.4 and round((1.01 ** 6 - 1) * 100, 1) == 6.2
    assert round(98 / 998, 4) == 0.0982 and round(152 / (0.1 * 1e-6)) == 1_520_000_000
    assert [round(v * 2.00 / 200, 4) for v in (5, 10, 20, 40)] == [0.05, 0.1, 0.2, 0.4]
    stated(text, "1/625", "4.7 × 10⁷ CFU/mL", "about 2.4%", "6.2% too concentrated", "98/998 = 0.0982",
           "1.52 × 10⁹ CFU/mL", "0.0500, 0.100, 0.200 and 0.400 mg/mL")


def test_lesson_three_gravimetric_example_and_worked_example():
    text = READINGS["lab-measurement-3"]
    masses = [198.6, 199.1, 198.9, 199.4, 198.7, 199.0, 198.8, 199.2, 198.5, 199.0]
    volumes = [m * z_factor(21.5) for m in masses]
    mean = statistics.fmean(volumes)
    assert round(statistics.fmean(masses), 2) == 198.92 and round(mean, 2) == 199.55
    assert round((mean - 200) / 2, 3) == -0.224 and round(statistics.stdev(volumes) / mean * 100, 3) == 0.140
    assert round((statistics.fmean(masses) - 200) / 2, 2) == -0.54
    v = 992.8 * z_factor(25.0)
    assert round(v, 1) == 996.8 and round((v - 1000) / 10, 2) == -0.32
    assert round(2.10 * z_factor(25.0) / v * 100, 2) == 0.21
    assert round(z_factor(20.0), 4) == 1.0029 and round(z_factor(21.5), 4) == 1.0032 and round(z_factor(25.0), 4) == 1.0040
    assert round(rho_water(20.0) * 1000, 3) == 998.207
    stated(text, "198.92 mg", "199.55 µL", "−0.224%", "0.140%", "−0.540%", "996.8 µL", "−0.32%", "0.21%",
           "1.0029 at 20 °C, 1.0032 at 21.5 °C and 1.0040 at 25 °C", "998.207 kg/m³")


def test_lesson_four_numbers():
    text = READINGS["lab-measurement-4"]
    assert round(2 * 0.08 / 0.0010) == 160 and round(2 * 0.08 / 0.01) == 16 and round(2 * 0.08 / 0.2 * 100) == 80
    assert round((1 - 0.0012 / 8.0) / (1 - 0.0012 / 1.00) * 100 - 100, 3) == 0.105
    assert round(2 * 0.12 / 0.005) == 48 and round(2 * 0.12 / 25 * 100, 2) == 0.96
    assert round((12.3456 - 12.1123) * 1000, 1) == 233.3
    stated(text, "m_min = 2 × 0.08/0.0010 = 160 mg", "m_min = 16 mg", "80%", "+0.105%", "48 mg", "0.96%", "0.2333 g")


def test_lesson_five_numbers():
    text = READINGS["lab-measurement-5"]
    assert round(NERNST_25, 2) == 59.16
    slope = (172.0 - 3.5) / 2.99
    assert round(slope, 2) == 56.35 and round(slope / 59.16 * 100, 1) == 95.3
    assert round(7.00 - (60.0 - 3.5) / slope, 2) == 6.00
    ratio = 10 ** 0.20
    assert round(ratio, 3) == 1.585 and round(0.1 / (1 + ratio) * 137.99, 2) == 5.34
    assert round(0.1 * ratio / (1 + ratio) * 141.96, 2) == 8.70
    assert round(8.00 - 0.028 * (4 - 25), 2) == 8.59
    bad = (-170.6 + 2.0) / 3.01
    assert round(abs(bad) / 59.16 * 100, 1) == 94.7 and round(7.00 + (-120.0 + 2.0) / bad, 2) == 9.11
    stated(text, "59.16 mV per pH unit at 25 °C, 58.17 at 20 °C and 61.54 at 37 °C", "56.35 mV per pH unit", "95.3%",
           "= 6.00", "5.34 g", "8.70 g", "8.59", "94.7%", "9.11")


def test_lesson_six_curve_and_examples():
    text = READINGS["lab-measurement-6"]
    slope, intercept = CURVE
    assert round(slope, 4) == 0.6404 and abs(intercept) < 1e-4
    residuals = [y - (intercept + slope * x) for x, y in zip([0, 0.125, 0.25, 0.5, 1.0], [0.000, 0.081, 0.158, 0.322, 0.640])]
    assert max(abs(r) for r in residuals) <= 0.0022
    assert round((0.254 - intercept) / slope, 3) == 0.397 and round((0.812 - intercept) / slope, 2) == 1.27
    assert round((0.406 - intercept) / slope * 4, 2) == 2.54
    mean = (0.287 + 0.291 + 0.283) / 3
    assert round((mean - intercept) / slope, 3) == 0.448 and round(10 * (mean - intercept) / slope, 2) == 4.48
    assert round(0.311 / 6220 * 1e6, 1) == 50.0
    stated(text, "b = 0.6404", "±0.0022", "0.397 mg/mL", "1.27 mg/mL", "2.54 mg/mL", "0.448 mg/mL", "4.48 mg/mL", "50.0 µM")


def test_project_dataset_curvature_and_results():
    guide = READINGS["lab-measurement-project-guide"]
    xs, ys = [0, 0.100, 0.200, 0.400, 0.600, 0.800], [0.000, 0.061, 0.124, 0.247, 0.352, 0.441]
    slope, intercept = fit(xs, ys)
    residuals = [y - (intercept + slope * x) for x, y in zip(xs, ys)]
    # Negative at both ends and positive in the middle: curvature over the full range.
    assert residuals[0] < 0 and residuals[-1] < 0 and all(r > 0 for r in residuals[2:5])
    low_slope, low_intercept = PROJECT
    assert round(low_slope, 4) == 0.6183 and round(low_intercept, 4) == -0.0002
    assert max(abs(y - (low_intercept + low_slope * x)) for x, y in zip(xs[:4], ys[:4])) < 0.001
    assert round((0.188 - low_intercept) / low_slope, 3) == 0.304
    assert round(5 * (0.139 - low_intercept) / low_slope, 2) == 1.13
    masses = [199.0, 199.5, 198.8, 199.3, 199.6, 198.9, 199.2, 199.4, 199.1, 198.7]
    volumes = [m * z_factor(21.0) for m in masses]
    assert round(z_factor(21.0), 4) == 1.0031
    assert abs((statistics.fmean(volumes) - 200) / 2) < 1.0 and statistics.stdev(volumes) / statistics.fmean(volumes) * 100 < 0.5
    assert round((170.2 - 1.5) / 2.99 / 59.16 * 100, 1) == 95.4
    assert round(0.0500 * 0.500 * 238.30 / 0.995, 2) == 5.99
    stated(guide, "Z = 1.0031 µL/mg", "+1.5 mV", "+170.2 mV", "0.512", "0.139", "1.20 g", "99.47 µL", "−0.53%", "93.9%", "1.39 mg/mL")


def test_schedule_project_route_and_formative_policy():
    weeks = MANIFEST["duration"]["weeks"]
    assert MANIFEST["duration"]["instructional_weeks"] == 6 == len(weeks)
    scheduled = [lesson for week in weeks for lesson in week["lesson_ids"]]
    lessons = [lesson["id"] for module in MANIFEST["modules"] for lesson in module["lessons"]]
    assert sorted(scheduled) == sorted(lessons) and len(set(scheduled)) == 7
    assert MANIFEST["maturity"] == "partial" and MANIFEST["review"]["status"] == "unreviewed"
    assert MANIFEST["grading_policy"]["mode"] == "formative-only"
    milestones = [case for case in CASES if ":project-m" in case["id"]]
    assert len(milestones) == 5 and all(c["points"] == 0 for case in CASES for c in case["rubric"])
    for card in CARDS:
        assert card["lesson_id"] in lessons
    assert f"Version: {MANIFEST['version']}." in SYLLABUS
    numeric = [q for q in BANK.values() if q["type"] == "numeric"]
    sig = sum(1 for q in numeric if q["solution_spec"]["significant_figures"])
    assert f"Of the {len(numeric)} numerical answers, 0 require units, {sig} check significant figures" in " ".join(
        MANIFEST["limitations"])


def test_bench_links_and_comparator():
    assert "#/bench/decimal-dilution-aerobic-plate-count" in READINGS["lab-measurement-2"]
    assert "#/bench/micropipette-gravimetric-verification" in READINGS["lab-measurement-3"]
    stated(CROSSWALK, "MIT OpenCourseWare 5.310 Laboratory Chemistry, Fall 2019", "agent-run comparison",
           "Local extension", "Absent by design")
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    comparator = registry["lab-chemistry-mit-5310"]
    assert comparator["reuse_mode"] == "link-only-comparator" and not comparator["permissions"]["adaptation"]
    assert registry["fda-bam-chapter-3-aerobic-plate-count"]["mapped_courses"] == ["lab-measurement"]
    assert re.search(r"no OCW (text|material)", (SYLLABUS + comparator["third_party_notes"]), re.IGNORECASE)
