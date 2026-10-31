"""Statistics 0.7.0 lessons 26 (categorical outcomes) and 27 (one-way ANOVA): recomputed numbers, schedule and grading.

2 × 2 measures, χ² and Fisher probabilities are recomputed from counts and binomial coefficients; the ANOVA table from the
raw values; p-values from the regularized incomplete beta function. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
from math import comb
from pathlib import Path

import mpmath
import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/statistics"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
R26 = (COURSE / "modules/26-categorical-outcomes-two-by-two-tables.md").read_text(encoding="utf-8")
R27 = (COURSE / "modules/27-one-way-analysis-of-variance.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")


def stated(text, *phrases):
    missing = [p for p in phrases if p not in text]
    assert not missing, missing


def chi2(table):
    (a, b), (c, d) = table
    n = a + b + c + d
    rows, cols = (a + b, c + d), (a + c, b + d)
    return sum((o - rows[i] * cols[j] / n) ** 2 / (rows[i] * cols[j] / n)
               for i, row in enumerate(table) for j, o in enumerate(row))


def p_f(f, d1, d2):
    return float(mpmath.betainc(d2 / 2, d1 / 2, 0, d2 / (d2 + d1 * f), regularized=True))


def p_t(t, df):
    return float(mpmath.betainc(df / 2, 0.5, 0, df / (df + t * t), regularized=True))


def test_lesson_26_two_by_two_numbers():
    a, b, c, d = 12, 28, 24, 16
    odds_ratio = a * d / (b * c)
    se = math.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    x2 = chi2(((a, b), (c, d)))
    assert (a / 40) / (c / 40) == pytest.approx(0.5) and round(odds_ratio, 3) == 0.286
    assert round(se, 3) == 0.472
    assert round(math.exp(math.log(odds_ratio) - 1.96 * se), 3) == 0.113 and round(math.exp(math.log(odds_ratio) + 1.96 * se), 3) == 0.721
    assert round(x2, 2) == 7.27 and round(math.erfc(math.sqrt(x2 / 2)), 4) == 0.0070
    assert round(math.sqrt(0.3 * 0.7 / 40 + 0.6 * 0.4 / 40), 3) == 0.106
    stated(R26, "= 0.286", "0.113 to 0.721", "= 7.27", "p = 0.0070", "= 0.106, giving −0.51 to −0.09")


def test_lesson_26_fisher_and_simpson():
    probs = {x: comb(7, x) * comb(9, 8 - x) / comb(16, 8) for x in range(0, 8)}
    observed = probs[1]
    assert round(observed, 4) == 0.0196 and round(probs[0] + probs[1], 4) == 0.0203
    assert round(sum(p for p in probs.values() if p <= observed + 1e-12), 4) == 0.0406
    strata = [(81, 6, 234, 36), (192, 71, 55, 25)]
    for a, b, c, d in strata:
        assert a / (a + b) > c / (c + d)
    pooled = [sum(s[i] for s in strata) for i in range(4)]
    assert pooled[0] / (pooled[0] + pooled[1]) < pooled[2] / (pooled[2] + pooled[3])
    mh = sum(a * d / sum(s) for (a, b, c, d), s in zip(strata, strata)) / sum(b * c / sum(s) for (a, b, c, d), s in zip(strata, strata))
    assert round(mh, 2) == 1.45
    stated(R26, "7 × 36/12,870 = 0.0196", "1 × 9/12,870 = 0.0007", "0.0203", "p = 0.0406", "= 1.45", "78.0%", "82.6%")
    x2 = chi2(((9, 51), (21, 39)))
    assert round(x2, 2) == 6.40 and round(math.erfc(math.sqrt(x2 / 2)), 3) == 0.011
    stated(R26, "= 6.40", "p = 0.011", "0.328", "0.429")


def test_lesson_27_anova_table_and_comparisons():
    groups = [[48, 52, 50, 55, 47, 48], [53, 58, 51, 57, 55, 56], [60, 57, 63, 59, 62, 59]]
    values = [x for g in groups for x in g]
    grand = sum(values) / len(values)
    means = [sum(g) / len(g) for g in groups]
    ssb = sum(len(g) * (m - grand) ** 2 for g, m in zip(groups, means))
    ssw = sum((x - m) ** 2 for g, m in zip(groups, means) for x in g)
    f = (ssb / 2) / (ssw / 15)
    assert (ssb, ssw) == (300, 104) and round(f, 1) == 21.6 and round(ssb / (ssb + ssw), 3) == 0.743
    assert f"{p_f(f, 2, 15):.1e}" == "3.8e-05"
    se = math.sqrt(ssw / 15 * 2 / 6)
    assert round(se, 2) == 1.52
    assert round(10 / se, 2) == 6.58 and round(5 / se, 2) == 3.29 and round(p_t(5 / se, 15), 4) == 0.0050
    assert round(3 * p_t(5 / se, 15), 3) == 0.015 and round(1 - 0.95 ** 3, 3) == 0.143
    stated(R27, "SS_B = Σ nⱼ(ȳⱼ − ȳ)² = 6(−5)² + 6(0)² + 6(5)² = 300", "F = 150.0/6.93 = 21.6", "p = 3.8 × 10⁻⁵", "0.743",
           "t = 5.0/1.52 = 3.29, p = 0.0050", "0.015", "1 − 0.95³ = 0.143")
    means4, var4 = [10.0, 12.0, 13.0, 15.0], [4.0, 5.0, 3.0, 4.0]
    ssb4 = 5 * sum((m - 12.5) ** 2 for m in means4)
    ssw4 = 4 * sum(var4)
    f4 = (ssb4 / 3) / (ssw4 / 16)
    assert (ssb4, ssw4) == (65.0, 64.0) and round(f4, 2) == 5.42 and round(p_f(f4, 3, 16), 4) == 0.0092
    stated(R27, "= 65.0", "SS_W = 4 × (4.0 + 5.0 + 3.0 + 4.0) = 64.0", "F = 21.7/4.00 = 5.42", "p = 0.0092")


KEYS = {
    "26:risk-ratio": (0.36 / 0.60, 0.60 / 0.36), "26:odds-ratio": (18 * 20 / (32 * 30), 0.36 / 0.60),
    "26:risk-difference": (0.36 - 0.60, 0.60 - 0.36), "26:expected": (24, 18),
    "26:chi-square": (chi2(((18, 32), (30, 20))), 36 / 24 + 36 / 26), "26:log-or-se": (math.sqrt(1 / 18 + 1 / 32 + 1 / 30 + 1 / 20), 1 / 18 + 1 / 32 + 1 / 30 + 1 / 20),
    "26:fisher-point": (7 * 36 / 12870, 7 * 9 / 12870),
    "27:ssb": (5 * ((14 - 44 / 3) ** 2 + (18 - 44 / 3) ** 2 + (12 - 44 / 3) ** 2), (14 - 44 / 3) ** 2 + (18 - 44 / 3) ** 2 + (12 - 44 / 3) ** 2),
    "27:ssw": (30, 7.5), "27:f-stat": ((280 / 3 / 2) / (30 / 12), (280 / 3) / 30), "27:df-within": (20, 23),
    "27:eta-squared": (0.3, 120 / 280), "27:fwer": (1 - 0.95 ** 5, 0.25), "27:pairwise-se": (1.0, math.sqrt(2.5 / 5)),
}


def shown(value, sig):
    if not sig:
        return f"{value:g}"
    return f"{value:.{max(0, sig - 1 - math.floor(math.log10(abs(value))))}f}"


def test_every_new_numeric_item_has_a_key():
    new = {qid for qid, q in BANK.items() if q["type"] == "numeric" and qid.startswith(("statistics-26:", "statistics-27:"))}
    assert new == {f"statistics-{k}" for k in KEYS}


@pytest.mark.parametrize("key", sorted(KEYS))
def test_new_numeric_keys(key):
    item = BANK[f"statistics-{key}"]
    spec = item["solution_spec"]
    value, wrong = KEYS[key]
    sig = spec["significant_figures"]
    assert float(shown(value, sig)) == pytest.approx(spec["answer"])
    assert grade(item, AttemptRequest(response=shown(spec["answer"], sig))).correct
    assert not grade(item, AttemptRequest(response=shown(wrong, sig))).correct


def test_new_choice_items_accept_only_the_key():
    for qid, item in BANK.items():
        if not qid.startswith(("statistics-26:", "statistics-27:")) or item["type"] == "numeric":
            continue
        if item["type"] == "single_choice":
            assert [i for i in range(len(item["options"])) if grade(item, AttemptRequest(response=str(i))).correct] == [item["solution_spec"]["answer"]]
        else:
            assert grade(item, AttemptRequest(response=item["solution_spec"]["answer"])).score == pytest.approx(2.0)


def test_schedule_version_and_crosswalk():
    assert MANIFEST["version"] == "0.7.0"
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[5]["lesson_ids"].index("statistics-26") == weeks[5]["lesson_ids"].index("statistics-10") + 1
    assert weeks[6]["lesson_ids"].index("statistics-27") == weeks[6]["lesson_ids"].index("statistics-7") + 1
    stated(CROSSWALK, "USC STAT 205", "agent-run comparison", "Logistic regression", "Absent")
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    assert "Version: 0.7.0." in syllabus and "scope-crosswalk.md" in syllabus
