"""Public package boundaries and reproducibility; no protected answer expectations."""

import csv
import json
import math
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cell-biology"
PACKETS = COURSE / "assessment-specs"


def test_cumulative_forms_use_actual_lesson_objectives_including_reused_water_objective():
    course = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lessons = {
        lesson["id"]: lesson
        for module in course["modules"]
        for lesson in module["lessons"]
    }
    for name, count, points in [("midterm", 16, 100), ("final", 28, 150)]:
        candidate = json.loads(
            (PACKETS / f"{name}-candidate.json").read_text(encoding="utf-8")
        )
        assert len(candidate["lesson_ids"]) == count
        expected = {
            o for lid in candidate["lesson_ids"] for o in lessons[lid]["objectives"]
        }
        occurrences = sum(
            len(lessons[lid]["objectives"]) for lid in candidate["lesson_ids"]
        )
        assert expected == set(candidate["objective_ids"])
        assert candidate["objective_link_occurrences"] == occurrences
        assert len(expected) == occurrences - 1
        assert candidate["points"] == points
        assert len(candidate["questions"]) == count
        assert "cell-biology-5-objective-2" not in expected


def test_final_case_stems_are_distinct_from_midterm_stems():
    packets = [
        json.loads(
            (PACKETS / f"{name}-candidate.json").read_text(encoding="utf-8")
        )
        for name in ("midterm", "final")
    ]
    stems = []
    for packet in packets:
        forms = [*packet["questions"], *packet["variant_questions"].values()]
        stems.append({re.sub(r"\W+", " ", q["prompt"]).lower() for q in forms})
    assert not stems[0].intersection(stems[1])


def test_project_generator_reproduces_tables_and_retains_culture_time_units(tmp_path):
    generated = subprocess.run(
        [
            sys.executable,
            str(PACKETS / "generate_project_dataset.py"),
            "--output",
            str(tmp_path),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert "integrative-project-candidate-cultures.csv" in generated.stdout
    assert (tmp_path / "integrative-project-candidate-cultures.csv").read_bytes() == (
        PACKETS / "integrative-project-candidate-cultures.csv"
    ).read_bytes()
    with (PACKETS / "integrative-project-candidate-cultures.csv").open(
        newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 96
    groups = defaultdict(list)
    for r in rows:
        groups[(r["form"], r["condition"], r["culture"])].append(r)
        live = int(r["viable_cells"])
        assert 0 < live <= int(r["seeded_cells"])
        assert 0 <= int(r["marker_positive_viable"]) <= live
        assert 0 <= int(r["functional_events_viable"]) <= live
        assert float(r["rna_signal_eq"]) > float(r["rna_background_eq"])
        assert float(r["protein_signal_ug"]) > float(r["protein_background_ug"])
        assert 0 < float(r["spike_recovered_eq"]) <= float(r["spike_input_eq"])
        assert 0 < float(r["protein_recovery_fraction"]) <= 1
    assert len(groups) == 48
    assert all({r["time_h"] for r in v} == {"0", "48"} for v in groups.values())
    assert all(len(v) == 2 for v in groups.values())
    for v in groups.values():
        assert (
            len(
                {
                    tuple(r[k] for k in ("perk_0_au", "perk_10_au", "perk_30_au"))
                    for r in v
                }
            )
            == 1
        )
    candidate = json.loads(
        (PACKETS / "integrative-project-candidate.json").read_text(encoding="utf-8")
    )
    assert candidate["machine_score_is_project_grade"] is False
    assert (COURSE / candidate["human_portfolio_path"]).is_file()


def test_membrane_example_temperature_matches_si_constant_derivation():
    # Exact defining SI constants; this is independent of the lesson's rounded coefficient.
    k = 1.380649e-23
    charge = 1.602176634e-19
    coefficients = [1000 * math.log(10) * k * t / charge for t in (298.15, 310.15)]
    assert math.isclose(coefficients[0], 59.159, abs_tol=0.001)
    assert math.isclose(coefficients[1], 61.540, abs_tol=0.001)
    text = (
        COURSE / "modules/02-membranes-transport-and-compartmentalization.md"
    ).read_text(encoding="utf-8")
    assert "59.16 mV" in text and "61.54 mV" in text
    assert "37 °C" in text
    assert "61.5 / z" not in text or "25 °C" not in text.split("61.5 / z")[0][-30:]


def test_remaining_cell_biology_numeric_keys_are_recalculated():
    questions = {
        q["id"]: q
        for q in json.loads(
            (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
        )["questions"]
    }

    vmax, km, substrate = 120.0, 3.0, 6.0
    predicted_rate = vmax * substrate / (km + substrate)
    rate = questions["cell-biology-3:check"]["solution_spec"]
    assert predicted_rate == 80.0
    assert abs(rate["answer"] - predicted_rate) <= rate["tolerance"]
    assert rate["unit"] == "μmol/min"

    gas_constant, temperature, equilibrium_constant = 8.314, 298.0, 10.0
    standard_delta_g = -gas_constant * temperature * math.log(equilibrium_constant) / 1000
    energy = questions["cell-biology-3:delta-g-from-k"]["solution_spec"]
    assert math.isclose(standard_delta_g, -5.7048204, abs_tol=1e-6)
    assert abs(energy["answer"] - standard_delta_g) <= energy["tolerance"]
    assert energy["unit"] == "kJ/mol"


def test_cell_biology_numeric_recalculation_inventory_is_complete():
    # The week-specific calculations live mainly in test_content_validation.py;
    # the two week-3 calculations above were added here. Pin the audited key set
    # so a new numeric practice item requires an explicit recalculation check.
    expected_ids = {
        "cell-biology-3:check",
        "cell-biology-3:delta-g-from-k",
        "cell-biology-9:coupling-energy",
        "cell-biology-9:rate-at-km",
        "cell-biology-9:rate-at-twice-km",
        "cell-biology-10:rate-prediction",
        "cell-biology-11:resolution-estimate",
        "cell-biology-12:er-marker-recovery",
        "cell-biology-12:image-quantification-contrast",
        "cell-biology-13:hybrid-fraction",
        "cell-biology-16:chip-percent-input",
        "cell-biology-17:isoform-fraction",
        "cell-biology-18:protein-half-life",
        "cell-biology-19:affected-child-risk",
        "cell-biology-21:occupancy-model",
        "cell-biology-21:relative-response",
        "cell-biology-24:uniform-stress",
        "cell-biology-24:yap-relative-increase",
        "cell-biology-25:phase-snapshot",
        "cell-biology-25:edu-relative-reduction",
        "cell-biology-27:functional-fraction",
        # 0.62.0 final review and project rehearsal; recalculated in
        # test_cell_biology_final_review_and_project.py.
        "cell-biology-final:gel-modulus",
        "cell-biology-project:rehearsal-perk-area",
    }
    bank = json.loads(
        (COURSE / "question-banks/practice.json").read_text(encoding="utf-8")
    )
    actual_ids = {
        q["id"] for q in bank["questions"] if q["type"] == "numeric"
    }
    assert actual_ids == expected_ids
