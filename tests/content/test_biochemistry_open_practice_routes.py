"""Recompute the Biochemistry 0.5.0 open homework, review and project practice from its public files."""

from __future__ import annotations

import csv
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
ITEMS = {
    item["id"]: item
    for item in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]
}
ASSESSMENTS = {item["id"]: item for item in MANIFEST["assessments"]}
LESSONS = {lesson["id"]: lesson for module in MANIFEST["modules"] for lesson in module["lessons"]}
WEEKS = {week["week"]: week for week in MANIFEST["duration"]["weeks"]}
HOMEWORK_WEEKS = {1: 2, 2: 4, 3: 6, 4: 7, 5: 9, 6: 10, 7: 12, 8: 14}
RT_25C, RT_37C, FARADAY = 2.479, 2.577, 96.485


def mean(values) -> float:
    values = [float(value) for value in values]
    return math.fsum(values) / len(values)


def rows(name: str) -> list[dict[str, str]]:
    with (COURSE / "assignments" / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def key(question_id: str, field_id: str | None = None) -> float:
    spec = ITEMS[question_id]["solution_spec"]
    if field_id is None:
        return spec["answer"]
    return next(item for item in spec["field_specs"] if item["id"] == field_id)["answer"]


def assert_upload(question_id: str, groups: dict) -> None:
    """Compare every stored CSV-upload check with per-unit values recomputed here from the CSV."""
    checks = ITEMS[question_id]["solution_spec"]["validation_spec"]["checks"]
    assert {check["row_id"] for check in checks} == set(groups)
    for check in checks:
        columns = groups[check["row_id"]]
        if check["calculation"]["operation"] == "count":
            assert check["answer"] == len(next(iter(columns.values())))
            continue
        values = columns[check["column"]]
        assert check["calculation"]["values"] == pytest.approx(values, abs=1e-6)
        assert check["answer"] == pytest.approx(mean(values), abs=1e-6)


def charge(groups, ph: float) -> float:
    return math.fsum(
        -count / (1 + 10 ** (pka - ph)) if kind == "acid" else count / (1 + 10 ** (ph - pka))
        for count, pka, kind in groups
    )


def bound(receptor: float, ligand: float, kd: float) -> float:
    total = receptor + ligand + kd
    return (total - math.sqrt(total * total - 4 * receptor * ligand)) / 2


def fit_hyperbola(substrates, rates):
    """Unweighted least squares in v: for each trial Km the best Vmax is Σvx/Σx², then golden-section search on Km."""

    def profile(km):
        x = [s / (km + s) for s in substrates]
        vmax = math.fsum(v * xi for v, xi in zip(rates, x)) / math.fsum(xi * xi for xi in x)
        return math.fsum((v - vmax * xi) ** 2 for v, xi in zip(rates, x)), vmax

    low, high, ratio = 0.1, 100.0, (math.sqrt(5) - 1) / 2
    for _ in range(200):
        left, right = high - ratio * (high - low), low + ratio * (high - low)
        if profile(left)[0] < profile(right)[0]:
            high = right
        else:
            low = left
    km = (low + high) / 2
    best = profile(km)[0]
    assert all(profile(km * factor)[0] >= best for factor in (0.9, 0.99, 1.01, 1.1))
    return profile(km)[1], km


def fit_reciprocal(substrates, rates):
    x = [1 / s for s in substrates]
    y = [1 / v for v in rates]
    x_bar, y_bar = mean(x), mean(y)
    slope = math.fsum((a - x_bar) * (b - y_bar) for a, b in zip(x, y)) / math.fsum((a - x_bar) ** 2 for a in x)
    vmax = 1 / (y_bar - slope * x_bar)
    return vmax, slope * vmax


def test_open_routes_are_scheduled_ungraded_and_linked():
    assert MANIFEST["version"] == "0.5.0" and MANIFEST["maturity"] == "partial"
    assert MANIFEST["review"] == {"status": "unreviewed", "reviewed_version": None, "reviewers": []}
    assert MANIFEST["grading_policy"]["mode"] == "formative-only" and MANIFEST["grading_policy"]["categories"] == []
    for number, week in HOMEWORK_WEEKS.items():
        assessment = ASSESSMENTS[f"biochemistry-hw{number}-practice"]
        lesson = LESSONS[f"biochemistry-hw{number}"]
        packet = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
        dataset = re.search(r"\*\*Dataset:\*\* \[[^\]]+\]\(([^)]+\.csv)\)", packet).group(1)

        assert (assessment["type"], assessment["mode"], assessment["week"]) == ("homework", "practice", week)
        assert assessment["points"] == sum(ITEMS[item]["points"] for item in assessment["question_ids"])
        assert lesson["id"] in WEEKS[week]["lesson_ids"] and assessment["id"] in WEEKS[week]["assessment_ids"]
        assert lesson["question_ids"] == [] and len(lesson["card_ids"]) == 3
        assert f"select **{assessment['title']}**" in packet
        assert "It does not contribute to a course grade." in packet
        assert "(unvalidated author estimate)" in packet
        assert f"assignments/{dataset}" in MANIFEST["learner_resources"]
        assert all(ITEMS[item]["prompt"].startswith(f"Homework {number} open formative practice") for item in assessment["question_ids"])

    midterm = ASSESSMENTS["biochemistry-week7-midterm-review-practice"]
    final = ASSESSMENTS["biochemistry-week14-final-review-practice"]
    assert midterm["week"] == 7 and "not a midterm exam" in midterm["title"]
    assert final["week"] == 14 and "not a final exam" in final["title"]
    first_half = {lesson for week in range(1, 8) for lesson in WEEKS[week]["lesson_ids"]}
    second_half = {lesson for week in range(8, 15) for lesson in WEEKS[week]["lesson_ids"]}
    reused_from = lambda assessment: {item.split(":")[0] for item in assessment["question_ids"]}  # noqa: E731
    assert reused_from(midterm) - {"biochemistry-midterm"} <= first_half | {"biochemistry-lab2"}
    # The final review is cumulative: it reuses lesson items from both halves of the course.
    assert reused_from(final) & first_half and reused_from(final) & second_half

    rehearsal = ASSESSMENTS["biochemistry-project-rehearsal-practice"]
    project = ASSESSMENTS["biochemistry-protein-state-project"]
    assert rehearsal["week"] == 5 and rehearsal["question_ids"] == LESSONS["biochemistry-project-guide"]["question_ids"]
    assert (project["type"], project["mode"], project["points"], project["week"]) == ("project", "self-assessment", 0, 8)
    cases = json.loads((COURSE / "rubrics/case-studio.json").read_text(encoding="utf-8"))["cases"]
    milestones = [case for case in cases if case["id"].startswith("biochemistry:project-m")]
    assert [case["id"].split("-")[1] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    assert all(case["mode"] == "self-assessment" for case in milestones)
    assert all(item["points"] == 0 for case in milestones for item in case["rubric"])


def test_delivered_lessons_link_to_routes_and_package_resources():
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    repository = ContentRepository(ROOT / "content")
    for lesson_id in [f"biochemistry-hw{number}" for number in HOMEWORK_WEEKS] + [
        "biochemistry-project-guide",
        "biochemistry-review-midterm-synthesis",
        "biochemistry-review-final-synthesis",
    ]:
        markdown = repository.lesson("biochemistry", lesson_id).markdown
        # Every relative reading or dataset link resolves to a lesson route or a pinned learner resource.
        assert not re.search(r"\]\((?!#/course/|/api/v1/|https?://)[^)]+\)", markdown), lesson_id
    guide = repository.lesson("biochemistry", "biochemistry-project-guide").markdown
    assert "/api/v1/courses/biochemistry/resources/assessment-specs/protein-state-binding-conditions.csv" in guide
    assert "#/course/biochemistry/lesson/biochemistry-9" in guide
    for path in MANIFEST["learner_resources"]:
        assert repository.learner_resource("biochemistry", path) == (COURSE / path).read_bytes()


def test_homework_1_charge_and_nitrogen_ledger():
    protein_k = [(10, 4.0, "acid"), (1, 3.5, "acid"), (2, 6.0, "base"), (1, 8.0, "base"), (6, 10.5, "base"), (2, 12.5, "base")]
    assert round(charge(protein_k, 6.0), 2) == key("biochemistry-hw1:charge-profile", "charge_ph6") == -0.91
    assert round(charge(protein_k, 8.0), 2) == key("biochemistry-hw1:charge-profile", "charge_ph8") == -2.50
    assert key("biochemistry-hw1:carbon-fate-tracer", "glucose_label_difference") == 18 - 3

    groups = defaultdict(lambda: defaultdict(list))
    for row in rows("homework-01-nitrogen-ledger.csv"):
        urea = float(row["amino_nitrogen_to_urea_umol"]) / 2
        cells = groups[row["condition"]]
        cells["mean_urea_umol"].append(urea)
        cells["mean_phosphate_equivalents_umol"].append(4 * urea)
        cells["mean_urea_umol_per_million_cells"].append(urea / float(row["viable_cells_million"]))
    assert_upload("biochemistry-hw1:nitrogen-ledger", groups)
    # Averaging per-culture ratios differs from dividing the condition means when cell numbers differ.
    load = groups["amino_load"]
    assert mean(load["mean_urea_umol_per_million_cells"]) == pytest.approx(7.625)
    assert mean(load["mean_urea_umol"]) / 2.0 == pytest.approx(7.5)


def test_homework_2_stability_binding_and_replicate_purification():
    assert key("biochemistry-hw2:stability-profile", "midpoint_variant") == 21 / 12
    assert round(1 / (1 + math.exp(-(21 - 12) / RT_25C)), 3) == key("biochemistry-hw2:stability-profile", "folded_variant_1m")
    assert round(math.exp((30 - 21) / RT_25C), 1) == key("biochemistry-hw2:stability-profile", "unfolded_ratio_water")
    exact = bound(40, 60, 20)
    assert exact * 20 == pytest.approx((40 - exact) * (60 - exact))
    assert round(exact, 1) == key("biochemistry-hw2:ligand-depletion", "complex_exact")
    assert round(100 * (40 * 60 / 80 - exact) / exact, 1) == key("biochemistry-hw2:ligand-depletion", "shortcut_overestimate")
    hill = lambda ligand: ligand**2 / (10**2 + ligand**2)  # noqa: E731
    assert 100 * (hill(20) - hill(5)) == pytest.approx(key("biochemistry-hw2:cooperative-switch"))

    preps = defaultdict(dict)
    for row in rows("homework-02-replicate-purifications.csv"):
        volume = float(row["volume_ml"])
        preps[row["prep"]][row["fraction"]] = (volume * float(row["protein_mg_per_ml"]), volume * float(row["activity_u_per_ml"]))
    groups = defaultdict(lambda: defaultdict(list))
    for fractions in preps.values():
        crude_mg, crude_units = fractions["crude"]
        for fraction, (milligrams, units) in fractions.items():
            groups[fraction]["mean_specific_activity_u_per_mg"].append(units / milligrams)
            groups[fraction]["mean_recovery_pct"].append(100 * units / crude_units)
            groups[fraction]["mean_fold_enrichment"].append((units / milligrams) / (crude_units / crude_mg))
    assert_upload("biochemistry-hw2:replicate-purification", groups)


def test_homework_3_initial_rate_windows_and_models():
    curves = rows("homework-03-progress-curves.csv")
    early = [(float(row["product_4min_um"]) - float(row["product_0min_um"])) / 4 for row in curves]
    late = [(float(row["product_20min_um"]) - float(row["product_0min_um"])) / 20 for row in curves]
    assert_upload(
        "biochemistry-hw3:progress-curve-summary",
        {"window_0_4_min": {"mean_rate_um_per_min": early}, "window_0_20_min": {"mean_rate_um_per_min": late}},
    )
    consumed = mean(100 * float(row["product_4min_um"]) / float(row["substrate_initial_um"]) for row in curves)
    assert round(consumed, 2) == key("biochemistry-hw3:initial-rate-validity", "consumed_4min")
    assert round(100 * (mean(early) - mean(late)) / mean(early), 1) == key("biochemistry-hw3:initial-rate-validity", "endpoint_shortfall")
    assert (60 / 6) / (300 / 150) == key("biochemistry-hw3:efficiency-two-substrates", "efficiency_ratio")
    assert 80 * 40 / (3 * 8 + 40) == key("biochemistry-hw3:inhibition-modes", "competitive_rate")
    assert (80 / 3) * 40 / (8 / 3 + 40) == pytest.approx(key("biochemistry-hw3:inhibition-modes", "uncompetitive_rate"))


def test_homework_4_nonlinear_refit_beats_the_reciprocal_line():
    replicates = defaultdict(lambda: defaultdict(list))
    for row in rows("homework-04-replicate-rates.csv"):
        replicates[row["condition"]][float(row["substrate_um"])].append(float(row["rate_um_per_min"]))
    substrates = sorted(replicates["control"])
    means = {condition: [mean(values[s]) for s in substrates] for condition, values in replicates.items()}
    assert_upload(
        "biochemistry-hw4:replicate-means",
        {
            condition: {f"mean_v_{int(s)}um": values[s] for s in (1.0, 4.0, 32.0)}
            for condition, values in replicates.items()
        },
    )

    # The packet's worked example: at a trial Km of 4.0 μM the best Vmax is Σ(v·x)/Σ(x²) ≈ 60.1 μM/min.
    x = [s / (4.0 + s) for s in substrates]
    trial = math.fsum(v * xi for v, xi in zip(means["control"], x)) / math.fsum(xi * xi for xi in x)
    assert round(trial, 1) == 60.1

    vmax_control, km_control = fit_hyperbola(substrates, means["control"])
    vmax_inhibitor, km_inhibitor = fit_hyperbola(substrates, means["inhibitor"])
    assert round(vmax_control, 1) == key("biochemistry-hw4:nonlinear-fit", "vmax_control")
    assert round(km_control, 2) == key("biochemistry-hw4:nonlinear-fit", "km_control")
    vmax_reciprocal, km_reciprocal = fit_reciprocal(substrates, means["control"])
    assert round(vmax_reciprocal, 1) == key("biochemistry-hw4:reciprocal-comparison", "vmax_reciprocal")
    assert round(km_reciprocal, 2) == key("biochemistry-hw4:reciprocal-comparison", "km_reciprocal")
    alpha = km_inhibitor / km_control
    assert round(alpha, 2) == key("biochemistry-hw4:inhibition-constant", "alpha_nls")
    assert round(6.0 / (alpha - 1), 2) == key("biochemistry-hw4:inhibition-constant", "ki_nls")
    # Competitive pattern: the nonlinear Vmax values agree within 0.5%, while the reciprocal fits disagree.
    assert abs(vmax_inhibitor - vmax_control) / vmax_control < 0.005
    vmax_reciprocal_inhibitor, km_reciprocal_inhibitor = fit_reciprocal(substrates, means["inhibitor"])
    assert vmax_reciprocal_inhibitor < 0.95 * vmax_reciprocal
    assert 6.0 / (km_reciprocal_inhibitor / km_reciprocal - 1) > 1.2 * 6.0 / (alpha - 1)


def test_homework_5_free_energy_redox_and_labeling():
    assert round(7.5 + RT_37C * math.log(0.020), 2) == key("biochemistry-hw5:actual-delta-g", "delta_g_cell")
    assert round(math.exp(-7.5 / RT_37C), 4) == key("biochemistry-hw5:actual-delta-g", "k_eq")
    assert -43.0 + 30.5 == key("biochemistry-hw5:creatine-coupling", "dg0_coupled")
    assert round(math.exp(12.5 / RT_37C)) == key("biochemistry-hw5:creatine-coupling", "k_coupled")
    assert round(-12.5 + RT_37C * math.log((1 / 2.0) * 10), 2) == key("biochemistry-hw5:creatine-coupling", "dg_coupled")
    assert round(-2 * FARADAY * (0.045 - 0.031), 1) == key("biochemistry-hw5:redox-ladder", "dg_succinate_q")
    assert round(-2 * FARADAY * (0.045 + 0.320), 1) == key("biochemistry-hw5:redox-ladder", "dg_nadh_q")

    groups = defaultdict(lambda: defaultdict(list))
    for row in rows("homework-05-citrate-labeling.csv"):
        isotopologues = [float(row[column]) for column in ("m0_pct", "m2_pct", "m3_pct")]
        assert math.fsum(isotopologues) == 100
        time_point = groups[f"minute_{row['minutes_after_pulse']}"]
        time_point["mean_labeled_pct"].append(100 - isotopologues[0])
        time_point["mean_m3_pct"].append(isotopologues[2])
    assert_upload("biochemistry-hw5:citrate-labeling", groups)


def test_homework_6_energy_charge_and_crossover():
    atp, adp = 2.5, 0.75
    amp = adp * adp / atp
    assert amp == pytest.approx(key("biochemistry-hw6:energy-charge", "amp_stressed"))
    assert round((atp + adp / 2) / (atp + adp + amp), 3) == key("biochemistry-hw6:energy-charge", "energy_charge")
    assert (3.0 * 4, 3.0 * 2) == (
        key("biochemistry-hw6:gluconeogenesis-from-lactate", "atp_used"),
        key("biochemistry-hw6:gluconeogenesis-from-lactate", "gtp_used"),
    )

    groups = defaultdict(lambda: defaultdict(list))
    for row in rows("homework-06-crossover.csv"):
        for metabolite in ("f6p", "fbp", "pep"):
            groups[row["condition"]][f"mean_{metabolite}"].append(float(row[f"{metabolite}_umol_per_g"]))
    assert_upload("biochemistry-hw6:crossover-means", groups)
    ratio = {
        metabolite: mean(groups["treated"][f"mean_{metabolite}"]) / mean(groups["control"][f"mean_{metabolite}"])
        for metabolite in ("f6p", "fbp")
    }
    assert ratio["f6p"] == pytest.approx(key("biochemistry-hw6:crossover-step", "f6p_ratio"))
    assert ratio["fbp"] == pytest.approx(key("biochemistry-hw6:crossover-step", "fbp_ratio"))
    assert ratio["f6p"] > 1 > ratio["fbp"]


def test_homework_7_fuel_ledgers_gradient_and_cholesterol_pool():
    turns, acetyl_coa = 18 // 2 - 1, 18 // 2
    atp = (turns + 3 * acetyl_coa) * 2.5 + (turns + acetyl_coa) * 1.5 + acetyl_coa - 2
    assert (acetyl_coa, atp) == (
        key("biochemistry-hw7:stearate-ledger", "acetyl_coa"),
        key("biochemistry-hw7:stearate-ledger", "atp_equivalents"),
    )
    assert round(atp / 26, 2) == key("biochemistry-hw7:stearate-ledger", "atp_per_o2")
    assert round(3.0 * 19 + 2.4 * 21.5) == key("biochemistry-hw7:ketone-ledger", "ketone_atp")
    pmf = 140 + 61.5 * 0.80
    assert round(pmf) == key("biochemistry-hw7:pmf-and-leak", "pmf")
    assert round(FARADAY * pmf / 1000, 1) == key("biochemistry-hw7:pmf-and-leak", "dg_proton")
    assert 4 + 28 * 0.80 == pytest.approx(key("biochemistry-hw7:pmf-and-leak", "atp_leak"))

    groups = defaultdict(lambda: defaultdict(list))
    for row in rows("homework-07-cholesterol-ledger.csv"):
        rates = {column: float(value) for column, value in row.items() if column.endswith("_ug_per_h")}
        net = (rates["synthesis_ug_per_h"] + rates["ldlr_uptake_ug_per_h"]
               - rates["bile_acid_conversion_ug_per_h"] - rates["vldl_export_ug_per_h"])
        groups[row["condition"]]["mean_net_change_ug_per_h"].append(net)
        groups[row["condition"]]["mean_ldlr_uptake_ug_per_h"].append(rates["ldlr_uptake_ug_per_h"])
    assert_upload("biochemistry-hw7:cholesterol-ledger", groups)
    assert mean(groups["inhibitor"]["mean_ldlr_uptake_ug_per_h"]) > mean(groups["control"]["mean_ldlr_uptake_ug_per_h"])


def test_homework_8_control_nadph_and_respiratory_block():
    assert round(1 - 0.40 - 0.35 - 0.15, 2) == key("biochemistry-hw8:control-coefficients", "c4")
    assert round(0.35 * 30, 1) == key("biochemistry-hw8:control-coefficients", "flux_change")
    assert 18 * math.log2(1 / (1 - 0.75)) == key("biochemistry-hw8:enzyme-turnover-time")
    assert (1.5 * 14, 0.60 * 1.5 * 14 / 2) == pytest.approx(
        (key("biochemistry-hw8:nadph-supply", "nadph_total"), key("biochemistry-hw8:nadph-supply", "g6p_oxidized"))
    )

    groups = defaultdict(lambda: defaultdict(list))
    for row in rows("homework-08-respiratory-block.csv"):
        for column, name in (("glucose_uptake", "mean_glucose_uptake"), ("lactate_output", "mean_lactate_output"),
                             ("oxygen_use", "mean_oxygen_use")):
            groups[row["condition"]][name].append(float(row[f"{column}_mmol_per_l_h"]))
    assert_upload("biochemistry-hw8:respiratory-block-means", groups)
    # The packet's model for the controls (ATP demand 8.0, 85% oxidative) sits within 0.01 of the culture means.
    model = {"mean_glucose_uptake": 0.85 * 8.0 / 32 + 0.15 * 8.0 / 2, "mean_lactate_output": 2 * 0.15 * 8.0 / 2,
             "mean_oxygen_use": 6 * 0.85 * 8.0 / 32}
    assert all(abs(mean(groups["control"][name]) - value) < 0.01 for name, value in model.items())
    blocked = groups["inhibitor"]
    assert mean(blocked["mean_lactate_output"]) / mean(blocked["mean_glucose_uptake"]) == pytest.approx(2.0)


def test_midterm_and_final_review_keys_recalculate():
    assert 0.85 * 40 * 25 * 60 / 1000 == pytest.approx(key("biochemistry-midterm:active-enzyme-vmax"))
    complex_ei = bound(50, 50, 5)
    assert round(complex_ei, 1) == key("biochemistry-midterm:tight-binding-inhibitor", "complex_ei")
    assert round(100 * (50 - complex_ei) / 50, 1) == key("biochemistry-midterm:tight-binding-inhibitor", "free_enzyme_pct")
    assert (2.0 / 2, 4 * 2.0 / 2) == (
        key("biochemistry-midterm:alanine-ledger", "urea_mmol"),
        key("biochemistry-midterm:alanine-ledger", "phosphate_equivalents"),
    )
    pure_specific_activity = 1e-3 / 50_000 * 1e9 * 100 * 60 / 1000  # μmol/min per mg of pure 50 kDa sites
    assert 100 * 96 / pure_specific_activity == pytest.approx(key("biochemistry-midterm:active-fraction-from-kcat"))

    palmitate = 7 * 2.5 + 7 * 1.5 + 8 * (3 * 2.5 + 1.5 + 1) - 2
    acetoacetate = 2 * (3 * 2.5 + 1.5 + 1) - 1
    assert (palmitate, acetoacetate, acetoacetate + 2.5) == (106, 19, 21.5)
    assert (8 / 2, 8.0) == (
        key("biochemistry-final:glucose-to-palmitate", "glucose_per_palmitate"),
        key("biochemistry-final:glucose-to-palmitate", "co2_at_pdh"),
    )
    assert round(palmitate / 23, 2) == key("biochemistry-final:atp-per-oxygen", "palmitate_ratio")
    assert round((acetoacetate + 2.5) / 4.5, 2) == key("biochemistry-final:atp-per-oxygen", "bhb_ratio")
    assert (1.92 / 1.20, 0.12 / 1.20) == pytest.approx(
        (key("biochemistry-final:uncoupler-or-inhibitor", "x_fold"), key("biochemistry-final:uncoupler-or-inhibitor", "y_fold"))
    )
    assert (2.0 / 2, 3.0 - 2.0 / 2) == (
        key("biochemistry-final:ppp-modes", "oxidative_g6p"),
        key("biochemistry-final:ppp-modes", "nonoxidative_pentose"),
    )


def test_synthesis_readings_show_consistent_worked_numbers():
    midterm = (COURSE / LESSONS["biochemistry-review-midterm-synthesis"]["reading"]).read_text(encoding="utf-8")
    final = (COURSE / LESSONS["biochemistry-review-final-synthesis"]["reading"]).read_text(encoding="utf-8")

    complex_rl = bound(30, 30, 3)
    assert round(complex_rl, 1) == 21.9 and "[RL] = (63 − 19.21)/2 = 21.9 nM" in midterm
    folded = 1 / (1 + math.exp(-(20 - 10 * 1.5) / RT_25C))
    vmax = 30 * folded * 20 * 60 / 1000
    assert (round(folded, 3), round(vmax, 1)) == (0.883, 31.8)
    assert "f_folded = 1/1.133 = 0.883" in midterm and "= 31.8 μM/min" in midterm
    assert round(31.8 * 6.0 / (14.0 + 6.0), 2) == 9.54 and "9.54 μM/min" in midterm
    assert 4.0 / (14.0 / 6.0 - 1) == pytest.approx(3.0)

    liver = 7 * 2.5 + 7 * 1.5 - 2 + 2 * 10
    exported = 3.0 * 19
    assert (liver, exported, 106 - (liver + exported)) == (46, 57, 3)
    assert "46 + 57 = 103" in final and "46/6 ≈ 7.7" in final


def test_project_rehearsal_and_guide_recalculate_without_project_answers():
    condition = rows("protein-state-rehearsal-condition.csv")[0]
    protein_c = [
        (int(condition["acid_group_count"]), float(condition["acid_pKa"]), "acid"),
        (int(condition["basic_group_count"]), float(condition["basic_pKa"]), "base"),
        (int(condition["histidine_count"]), float(condition["histidine_pKa"]), "base"),
    ]
    rt = 0.008314 * 298.15
    assert round(charge(protein_c, 7.0), 2) == key("biochemistry-project:rehearsal-charge", "charge_ph7")
    assert round(charge(protein_c, 5.0), 2) == key("biochemistry-project:rehearsal-charge", "charge_ph5")

    def staged(denaturant):
        stability = float(condition["deltaG_water_kj_per_mol"]) - float(condition["m_kj_per_mol_M"]) * denaturant
        folded = 1 / (1 + math.exp(-stability / rt))
        active = folded * float(condition["protein_total_nM"])
        complex_rl = bound(active, float(condition["ligand_total_nM"]), float(condition["Kd_nM"]))
        return stability, folded, active, complex_rl

    stability, folded, active, complex_rl = staged(float(condition["denaturant_M"]))
    assert stability == key("biochemistry-project:rehearsal-folding", "dg_unfold")
    assert round(folded, 3) == key("biochemistry-project:rehearsal-folding", "f_folded")
    assert round(active, 1) == key("biochemistry-project:rehearsal-folding", "folded_total")
    assert round(complex_rl, 1) == key("biochemistry-project:rehearsal-binding", "complex_rl")
    assert round(complex_rl / 50, 3) == key("biochemistry-project:rehearsal-binding", "fraction_total")

    guide = (COURSE / "assignments/protein-state-project-guide.md").read_text(encoding="utf-8")
    _, _, active_25, complex_25 = staged(2.5)
    assert round(charge(protein_c, 6.0), 2) == 3.56 and "Net charge = +3.56" in guide
    assert (round(active_25, 1), round(complex_25, 1)) == (34.6, 28.6)
    assert round(complex_25 / 50, 3) == 0.571 < 0.70 and "0.571 < 0.70" in guide

    # The guide and rehearsal items must not reveal results for the project's own conditions A and B.
    with (COURSE / "assessment-specs/protein-state-binding-conditions.csv").open(encoding="utf-8", newline="") as handle:
        project_conditions = list(csv.DictReader(handle))
    public_text = guide + json.dumps(
        [ITEMS[item] for item in LESSONS["biochemistry-project-guide"]["question_ids"]], ensure_ascii=False
    )
    for row in project_conditions:
        groups = [
            (int(row["acid_group_count"]), float(row["acid_pKa"]), "acid"),
            (int(row["basic_group_count"]), float(row["basic_pKa"]), "base"),
            (int(row["histidine_count"]), float(row["histidine_pKa"]), "base"),
        ]
        stability = float(row["deltaG_water_kj_per_mol"]) - float(row["m_kj_per_mol_M"]) * float(row["denaturant_M"])
        folded = 1 / (1 + math.exp(-stability / rt))
        active = folded * float(row["protein_total_nM"])
        complex_rl = bound(active, float(row["ligand_total_nM"]), float(row["Kd_nM"]))
        for value in (charge(groups, float(row["pH"])), folded, active, complex_rl, complex_rl / active,
                      complex_rl / float(row["protein_total_nM"])):
            reported = format(value, "#.3g").replace("-", "−")
            assert not re.search(rf"(?<![\d.]){re.escape(reported)}(?!\d)", public_text), (row["condition"], reported)
            assert not re.search(rf"(?<![\d.]){re.escape(reported.replace('−', '-'))}(?!\d)", public_text)
