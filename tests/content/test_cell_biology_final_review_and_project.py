"""Cell Biology 0.62.0 learner routes for the cumulative final review and the integrative project.

These tests recompute every new key from the committed CSV files and stated prompt values, and check
that the new activities stay ungraded and separate from the inactive assessment candidates. Passing
them is author-side consistency evidence only; it is not review of the science or of the teaching.
"""

from __future__ import annotations

import csv
import json
import math
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cell-biology"
CLONES = COURSE / "assignments/final-review-feedback-variant-clones.csv"
REHEARSAL = COURSE / "assignments/project-rehearsal-cultures.csv"
SYNTHESIS = COURSE / "modules/13d-course-synthesis-and-final-review.md"
GUIDE = COURSE / "assignments/integrative-project-guide.md"
GENOTYPES = ("reference", "knock_in", "corrected")
TIMES = (0, 10, 30, 60)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def rows(path):
    with path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def bank():
    return {q["id"]: q for q in read_json(COURSE / "question-banks/practice.json")["questions"]}


def manifest():
    return read_json(COURSE / "course.json")


def assessment(assessment_id):
    return next(a for a in manifest()["assessments"] if a["id"] == assessment_id)


def clone_values(genotype, column):
    return [float(row[column]) for row in rows(CLONES) if row["genotype"] == genotype]


def mean(values):
    return math.fsum(values) / len(values)


def field_answers(question):
    return {spec["id"]: spec for spec in question["solution_spec"]["field_specs"]}


def trapezoid(values, times=TIMES):
    return math.fsum((values[i] + values[i + 1]) / 2 * (times[i + 1] - times[i]) for i in range(len(times) - 1))


def test_final_review_set_combines_new_integrative_items_with_one_earlier_item_per_late_lesson():
    final = assessment("cell-biology-week14-final-review-practice")
    questions = bank()
    assert final["type"] == "practice" and final["mode"] == "practice" and final["week"] == 14
    assert "not a final exam" in final["title"]
    new_ids = [qid for qid in final["question_ids"] if qid.startswith("cell-biology-final:")]
    earlier = [qid for qid in final["question_ids"] if not qid.startswith("cell-biology-final:")]
    assert len(new_ids) == 13 and len(earlier) == 12 and len(final["question_ids"]) == 25
    assert final["points"] == sum(questions[qid]["points"] for qid in final["question_ids"]) == 53
    assert sorted(int(qid.split(":")[0].rsplit("-", 1)[1]) for qid in earlier) == list(range(17, 29))
    lesson_items = {qid for module in manifest()["modules"] for lesson in module["lessons"] for qid in lesson["question_ids"]}
    assert not set(new_ids) & lesson_items, "new cumulative items are delivered through the review set only"
    for qid in new_ids:
        question = questions[qid]
        assert question["visibility"] == "public-practice-authoring"
        assert question["prompt"].startswith("Final review open practice")
        assert "cell-biology-review-14-synthesis" in question["feedback"]["lesson_ids"] or qid in {
            "cell-biology-final:penetrance-with-phenocopy", "cell-biology-final:gel-modulus"}


def test_clone_dataset_has_four_independent_clones_per_genotype_and_matches_the_reading_table():
    data = rows(CLONES)
    assert len(data) == 12
    for genotype in GENOTYPES:
        clones = [row["clone"] for row in data if row["genotype"] == genotype]
        assert len(clones) == len(set(clones)) == 4
    synthesis = SYNTHESIS.read_text(encoding="utf-8")
    table = {
        cells[0]: cells[1:]
        for line in synthesis.splitlines()
        if line.startswith("| ") and len(cells := [c.strip() for c in line.strip("|").split("|")]) == 4
    }
    expected_rows = {
        "F mRNA, relative units": "f_mrna_rel",
        "Short-pulse F synthesis, relative units": "f_nascent_rel",
        "F half-life (h)": "f_half_life_h",
        "Steady-state F protein, relative units": "f_protein_rel",
        "pERK at 60 min (fold over vehicle)": "perk_60_fold",
        "EdU-positive recovered viable cells (%)": "edu_positive_pct",
        "Viable recovery (%)": "viable_recovery_pct",
    }
    for label, column in expected_rows.items():
        shown = [float(value) for value in table[label]]
        recomputed = [mean(clone_values(g, column)) for g in GENOTYPES]
        assert all(math.isclose(a, b, abs_tol=1e-9) for a, b in zip(shown, recomputed)), label


def test_steady_state_model_accounts_for_the_measured_knock_in_protein():
    half_life = {g: mean(clone_values(g, "f_half_life_h")) for g in GENOTYPES}
    synthesis = {g: mean(clone_values(g, "f_nascent_rel")) for g in GENOTYPES}
    protein = {g: mean(clone_values(g, "f_protein_rel")) for g in GENOTYPES}
    predicted = 100 * (synthesis["knock_in"] / synthesis["reference"]) * (half_life["knock_in"] / half_life["reference"])
    assert math.isclose(predicted, 32.6667, abs_tol=1e-3)
    assert abs(predicted - protein["knock_in"]) < 1  # the constructed data follow the stated model
    question = bank()["cell-biology-final:turnover-steady-state"]
    answers = field_answers(question)
    k_knock_in = math.log(2) / half_life["knock_in"]
    assert abs(answers["k_deg_knock_in"]["answer"] - k_knock_in) <= answers["k_deg_knock_in"]["tolerance"]
    assert answers["k_deg_knock_in"]["unit"] == "h^-1" and answers["k_deg_knock_in"]["significant_figures"] == 3
    assert abs(answers["predicted_ratio_pct"]["answer"] - predicted) <= answers["predicted_ratio_pct"]["tolerance"]
    assert answers["interpretation"]["answer"] == 1


def test_clone_summary_upload_and_trajectory_plot_recalculate_from_the_csv():
    questions = bank()
    upload = questions["cell-biology-final:clone-summary-table"]
    checks = upload["solution_spec"]["validation_spec"]["checks"]
    assert upload["solution_spec"]["validation_spec"]["columns"] == [
        "genotype", "clone_count", "mean_f_half_life_h", "mean_perk_60_fold"]
    assert len(checks) == 9 and upload["points"] == 9
    source = {"mean_f_half_life_h": "f_half_life_h", "mean_perk_60_fold": "perk_60_fold"}
    for check in checks:
        if check["column"] == "clone_count":
            assert check["answer"] == len(clone_values(check["row_id"], "f_half_life_h")) == 4
        else:
            values = clone_values(check["row_id"], source[check["column"]])
            assert check["calculation"]["values"] == values
            assert abs(check["answer"] - mean(values)) <= check["tolerance"]

    plot = questions["cell-biology-final:knock-in-perk-trajectory"]
    observations = {item["x"]: item["values"] for item in plot["graph_spec"]["observations"]}
    expected = {point["x"]: point["y"] for point in plot["solution_spec"]["points"]}
    for time in (10, 30, 60):
        values = clone_values("knock_in", f"perk_{time}_fold")
        assert observations[time] == values
        assert math.isclose(expected[time], mean(values), abs_tol=1e-9)


def test_perk_area_edu_penetrance_and_modulus_keys_are_independently_recalculated():
    questions = bank()
    per_clone_area = {
        g: [trapezoid([float(row[f"perk_{t}_fold"]) for t in TIMES]) for row in rows(CLONES) if row["genotype"] == g]
        for g in GENOTYPES
    }
    mean_trajectory = {g: [mean(clone_values(g, f"perk_{t}_fold")) for t in TIMES] for g in GENOTYPES}
    # The trapezoid is linear, so the mean of per-clone areas equals the area of the mean trajectory.
    for genotype in GENOTYPES:
        assert math.isclose(mean(per_clone_area[genotype]), trapezoid(mean_trajectory[genotype]), abs_tol=1e-9)
    area = field_answers(questions["cell-biology-final:perk-area"])
    assert math.isclose(area["area_knock_in"]["answer"], 315.0) and area["area_knock_in"]["unit"] == "min"
    assert abs(area["area_knock_in"]["answer"] - trapezoid(mean_trajectory["knock_in"])) <= area["area_knock_in"]["tolerance"]
    ratio = trapezoid(mean_trajectory["knock_in"]) / trapezoid(mean_trajectory["reference"])
    assert abs(area["area_ratio"]["answer"] - ratio) <= area["area_ratio"]["tolerance"] + 0.005
    assert area["area_meaning"]["answer"] == 0

    edu = field_answers(questions["cell-biology-final:edu-denominators"])
    reference, knock_in = mean(clone_values("reference", "edu_positive_pct")), mean(clone_values("knock_in", "edu_positive_pct"))
    assert edu["pp_difference"]["answer"] == knock_in - reference == 11 and edu["pp_difference"]["unit"] == "pp"
    assert abs(edu["relative_increase"]["answer"] - 100 * (knock_in - reference) / reference) <= 0.05

    penetrance = field_answers(questions["cell-biology-final:penetrance-with-phenocopy"])
    probability = Fraction(1, 2) * Fraction(60, 100) + Fraction(1, 2) * Fraction(5, 100)
    assert penetrance["phenotype_pct"]["answer"] == float(100 * probability) == 32.5
    assert "0.60" in questions["cell-biology-final:penetrance-with-phenocopy"]["prompt"]
    assert "0.05" in questions["cell-biology-final:penetrance-with-phenocopy"]["prompt"]

    modulus = questions["cell-biology-final:gel-modulus"]
    stress = 1.2e-3 / (2e-3 * 1e-3)
    strain = 0.20 / 10
    assert math.isclose(stress, 600) and math.isclose(strain, 0.02)
    assert abs(modulus["solution_spec"]["answer"] - stress / strain) <= modulus["solution_spec"]["tolerance"]
    assert modulus["solution_spec"]["unit"] == "Pa" and modulus["solution_spec"]["unit_required"] is True


def test_rehearsal_transformations_follow_the_guide_and_differ_from_the_candidate_forms():
    data = rows(REHEARSAL)
    candidate = rows(COURSE / "assessment-specs/integrative-project-candidate-cultures.csv")
    assert list(data[0]) == list(candidate[0]), "the rehearsal uses the project column layout"
    assert {row["form"] for row in data} == {"R"} and not {row["culture"] for row in data} & {row["culture"] for row in candidate}

    def derived(row):
        viable = float(row["viable_cells"])
        rna = (float(row["rna_signal_eq"]) - float(row["rna_background_eq"])) * float(row["spike_input_eq"]) / float(row["spike_recovered_eq"])
        protein = (float(row["protein_signal_ug"]) - float(row["protein_background_ug"])) / float(row["protein_recovery_fraction"])
        return {
            "mean_rna_per_1000_viable": rna / (viable / 1000),
            "mean_protein_ug_per_1000_viable": protein / (viable / 1000),
            "mean_marker_pct": 100 * float(row["marker_positive_viable"]) / viable,
            "mean_function_pct": 100 * float(row["functional_events_viable"]) / viable,
            "area": 5 * float(row["perk_0_au"]) + 15 * float(row["perk_10_au"]) + 10 * float(row["perk_30_au"]),
        }

    questions = bank()
    upload = questions["cell-biology-project:rehearsal-summary"]
    checks = upload["solution_spec"]["validation_spec"]["checks"]
    assert len(checks) == 10 and upload["points"] == 10
    for check in checks:
        selected = [row for row in data if row["condition"] == check["row_id"]]
        if check["column"] == "culture_count":
            assert check["answer"] == len(selected) == 4
            continue
        values = [derived(row)[check["column"]] for row in selected]
        assert all(math.isclose(a, b, abs_tol=1e-9) for a, b in zip(check["calculation"]["values"], values))
        assert abs(check["answer"] - mean(values)) <= check["tolerance"]

    third = next(row for row in data if row["culture"] == "R-signal_high-03")
    area = questions["cell-biology-project:rehearsal-perk-area"]["solution_spec"]
    trapezoid_area = (float(third["perk_0_au"]) + float(third["perk_10_au"])) / 2 * 10 + (float(third["perk_10_au"]) + float(third["perk_30_au"])) / 2 * 20
    assert derived(third)["area"] == trapezoid_area == area["answer"] == 2385

    signal = [row for row in data if row["condition"] == "signal_high"]
    pooled = 100 * sum(float(r["marker_positive_viable"]) for r in signal) / sum(float(r["viable_cells"]) for r in signal)
    equal = mean([derived(r)["mean_marker_pct"] for r in signal])
    answers = field_answers(questions["cell-biology-project:rehearsal-pooled-versus-culture"])
    assert abs(answers["pooled_pct"]["answer"] - pooled) <= 0.05 and abs(answers["equal_culture_pct"]["answer"] - equal) <= 0.05
    assert pooled < equal and answers["summary_choice"]["answer"] == 2

    first = derived(next(row for row in data if row["culture"] == "R-control-01"))
    guide = GUIDE.read_text(encoding="utf-8")
    assert first["mean_rna_per_1000_viable"] == 62.5 and "= 62.5 per 1000 viable cells" in guide
    assert first["mean_marker_pct"] == 20 and "= 20.0%" in guide
    assert first["area"] == 1100 and "= 1100 AU·min" in guide


def test_project_milestones_are_ungraded_case_studio_self_checks():
    cases = read_json(COURSE / "rubrics/case-studio.json")["cases"]
    milestones = [case for case in cases if case["id"].startswith("cell-biology:project-m")]
    assert [case["id"].split("-")[2] for case in milestones] == ["m1", "m2", "m3", "m4", "m5"]
    objectives = {o["id"] for o in manifest()["lesson_objectives"]}
    for case in milestones:
        assert case["mode"] == "self-assessment"
        assert case["prompt"].startswith(f"Integrative project milestone {case['id'].split('-')[2][1]}")
        assert all(criterion["points"] == 0 for criterion in case["rubric"]) and len(case["rubric"]) >= 4
        assert set(case["objective_ids"]) <= objectives
        assert any("never submitted, scored or graded" in text for text in case["limitations"])
    project = assessment("cell-biology-integrative-project")
    assert project["type"] == "project" and project["mode"] == "self-assessment"
    assert project["path"] == "rubrics/case-studio.json" and project["points"] == 0 and not project["question_ids"]
    weeks = {week["week"]: week for week in manifest()["duration"]["weeks"]}
    assert "cell-biology-project-guide" in weeks[10]["lesson_ids"]
    assert "cell-biology-project-rehearsal-practice" in weeks[10]["assessment_ids"]
    assert {"cell-biology-week14-final-review-practice", "cell-biology-integrative-project"} <= set(weeks[14]["assessment_ids"])
    guide = GUIDE.read_text(encoding="utf-8")
    assert "never submitted, scored or graded" in guide and "Case studio" in guide


def test_new_items_use_catalogued_misconceptions_and_learner_resources_are_allowlisted():
    catalog = set(re.findall(r"^\| `([a-z0-9-]+)` \|", (COURSE / "misconceptions.md").read_text(encoding="utf-8"), re.M))
    for qid, question in bank().items():
        if qid.startswith(("cell-biology-final:", "cell-biology-project:")):
            assert set(question["feedback"].get("misconception_ids", [])) <= catalog, qid
    resources = set(manifest()["learner_resources"])
    assert {
        "assignments/final-review-feedback-variant-clones.csv",
        "assignments/project-rehearsal-cultures.csv",
        "assessment-specs/integrative-project-candidate-cultures.csv",
    } <= resources
    assert "assessment-specs/integrative-project-candidate-observations.csv" not in resources


def test_syllabus_restores_week8_links_and_describes_the_new_routes_without_claiming_grades():
    syllabus = (COURSE / "syllabus.md").read_text(encoding="utf-8")
    week8 = next(line for line in syllabus.splitlines() if line.startswith("| 8 |"))
    assert "(modules/07c-quantitative-models-and-assumptions.md)" in week8
    assert "(modules/07d-controls-replicates-and-bounded-claims.md)" in week8
    assert "## Cumulative final review (ungraded; not a final exam)" in syllabus
    assert "## Integrative project (optional, ungraded)" in syllabus
    assert "25 questions and 53 practice points" in syllabus
    course = manifest()
    assert course["maturity"] == "partial" and course["grading_policy"]["mode"] == "formative-only"
    assert course["review"]["status"] == "unreviewed"
