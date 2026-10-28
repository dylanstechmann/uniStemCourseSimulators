"""Transport 0.7.0 closed-system first-law lesson: stated numbers, schedule, comparators, and the crosswalk's absent topics.

Each number the reading states is recomputed here from quadrature of P dV, an RK4 integration of the adiabat and a staged
expansion, not read from the lesson. Same-AI checks, not human review.
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import pytest

from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/transport"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
READING = (COURSE / "modules/23-closed-system-first-law-work-heat-and-ideal-gas-processes.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")
R = 8.314
N, T, V1, V2 = 0.0500, 300.0, 1.0e-3, 3.0e-3


def stated(*phrases):
    missing = [phrase for phrase in phrases if phrase not in READING]
    assert not missing, missing


def simpson(function, lower, upper, pieces=20000):
    step = (upper - lower) / pieces
    return step / 3 * math.fsum((1 if i in (0, pieces) else 4 if i % 2 else 2) * function(lower + i * step) for i in range(pieces + 1))


def adiabat(temperature, v_start, v_end, c_v, moles, steps=40000):
    """RK4 for dT/dV = -(R/C_v) T/V (first law with Q = 0 for an ideal gas), with the work from trapezoid sums of P dV."""
    volume, work, dv = v_start, 0.0, (v_end - v_start) / steps
    rate = lambda temp, vol: -(R / c_v) * temp / vol  # noqa: E731
    for _ in range(steps):
        k1 = rate(temperature, volume)
        k2 = rate(temperature + dv * k1 / 2, volume + dv / 2)
        k3 = rate(temperature + dv * k2 / 2, volume + dv / 2)
        k4 = rate(temperature + dv * k3, volume + dv)
        following = temperature + dv * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        work += 0.5 * (moles * R * temperature / volume + moles * R * following / (volume + dv)) * dv
        temperature, volume = following, volume + dv
    return temperature, work


def test_four_processes_of_one_gas_by_quadrature_and_an_integrated_adiabat():
    c_v, c_p = 1.5 * R, 2.5 * R
    work_iso = simpson(lambda v: N * R * T / v, V1, V2)
    t_ad, work_ad = adiabat(T, V1, V2, c_v, N)
    p1, p_iso, p_ad = N * R * T / V1, N * R * T / V2, N * R * t_ad / V2
    assert work_iso == pytest.approx(N * R * T * math.log(3), rel=1e-9) and work_iso == pytest.approx(137.0, abs=0.05)
    assert t_ad == pytest.approx(T * 3 ** (-2 / 3), rel=1e-8) and t_ad == pytest.approx(144.2, abs=0.05)
    assert work_ad == pytest.approx(N * c_v * (T - t_ad), rel=1e-6) and work_ad == pytest.approx(97.1, abs=0.05)
    assert p1 * V1 ** (5 / 3) == pytest.approx(p_ad * V2 ** (5 / 3), rel=1e-7)
    assert (round(p1 / 1e3, 1), round(p_iso / 1e3, 2), round(p_ad / 1e3, 2)) == (124.7, 41.57, 19.98)
    # constant pressure 300 -> 350 K: Q = dU + W, and the work equals P dV from V proportional to T
    heat_p, d_u, work_p = N * c_p * 50, N * c_v * 50, N * R * 50
    assert heat_p == pytest.approx(d_u + work_p) and work_p == pytest.approx(p1 * (V1 * 350 / 300 - V1))
    assert c_v == pytest.approx(12.47, abs=0.006) and c_p == pytest.approx(20.79, abs=0.006)
    assert heat_p == pytest.approx(51.96, abs=0.006) and d_u == pytest.approx(31.18, abs=0.006) and work_p == pytest.approx(20.79, abs=0.006)
    stated("P₁ = nRT/V₁ = 124.7 kPa", "0.0500·8.314·300·ln 3 = **137.0 J**", "The final pressure is 41.57 kPa.", "T₂ = 300·(1/3)^(2/3) = 144.2 K",
           "0.0500·12.47·155.8 = **97.1 J**", "Its final pressure is only 19.98 kPa.", "C_v = (3/2)R = 12.47 J/(mol·K), C_p = (5/2)R = 20.79 J/(mol·K) and γ = 5/3",
           "Q = nC_pΔT = 0.0500·20.79·50 = 51.96 J", "ΔU = nC_vΔT = 31.18 J", "W = nRΔT = 20.79 J", "takes only 31.18 J, all of it ΔU")
    # an ideal gas has H = U + nRT, so the constant-volume enthalpy change uses C_p as well
    assert N * c_v * 60 + N * R * 60 == pytest.approx(N * c_p * 60)


def test_irreversible_expansion_loses_work_and_generates_entropy():
    p_final = N * R * T / V2
    work_irr = p_final * (V2 - V1)
    work_rev = simpson(lambda v: N * R * T / v, V1, V2)
    delta_s = simpson(lambda v: N * R / v, V1, V2)  # entropy is a state function: integrate dQ_rev/T = P dV/T
    heat_irr = work_irr  # dU = 0 for an isothermal ideal gas
    generated = delta_s - heat_irr / T
    assert work_irr == pytest.approx(83.14, abs=0.01) and work_irr / work_rev == pytest.approx(0.607, abs=0.001)
    assert delta_s == pytest.approx(0.4567, abs=1e-4) and heat_irr / T == pytest.approx(0.2771, abs=1e-4) and generated == pytest.approx(0.1796, abs=1e-4)
    assert T * generated == pytest.approx(work_rev - work_irr, rel=1e-9) and T * generated == pytest.approx(53.9, abs=0.05)
    stated("P_ext = 41.57 kPa", "41.57·2.0 = **83.1 J**", "only 61% of the reversible 137.0 J", "ΔS = nR ln 3 = 0.4567 J/K", "transfers Q/T = 0.4567 J/K",
           "only 83.1 J enters, which transfers 0.2771 J/K", "S_gen = 0.1796 J/K", "0.1796 × 300 = 53.9 J, which equals 137.0 − 83.1")


def test_more_stages_approach_the_reversible_work_and_remove_the_entropy_generation():
    work_rev, delta_s = N * R * T * math.log(3), N * R * math.log(3)
    previous, generated = 0.0, None
    for stages in (1, 2, 4, 16, 256, 4096):
        volumes = [V1 * (V2 / V1) ** (i / stages) for i in range(stages + 1)]
        work = math.fsum((N * R * T / volumes[i]) * (volumes[i] - volumes[i - 1]) for i in range(1, stages + 1))
        assert previous < work < work_rev  # each finer staging delivers more work, never above the reversible value
        previous, generated = work, delta_s - work / T
        assert generated > 0 and generated * T == pytest.approx(work_rev - work, rel=1e-9)
    assert previous == pytest.approx(work_rev, rel=1e-3) and generated < 1e-3


def test_worked_syringe_example_matches_integration_and_the_manifest():
    n, t0, p0 = 0.0200, 300.0, 100e3
    c_v = 2.5 * R
    v_start = n * R * t0 / p0
    t_ad, work_ad = adiabat(t0, v_start, v_start / 2, c_v, n)
    work_on_iso = -simpson(lambda v: n * R * t0 / v, v_start, v_start / 2)
    assert v_start * 1e3 == pytest.approx(0.4988, abs=6e-5) and t_ad == pytest.approx(395.9, abs=0.06)
    assert n * R * t_ad / (v_start / 2) / 1e3 == pytest.approx(263.9, abs=0.06) and p0 * 2**1.4 / 1e3 == pytest.approx(263.9, abs=0.06)
    assert -work_ad == pytest.approx(39.85, abs=0.006) and -work_ad == pytest.approx(n * c_v * (t_ad - t0), rel=1e-6)
    assert work_on_iso == pytest.approx(34.58, abs=0.005) and 2 * p0 / 1e3 == 200.0 and -work_ad > work_on_iso
    stated("0.0200·8.314·300/100,000 = 0.4988 L", "so the final volume is 0.2494 L", "T₂ = 300·2^0.4 = 395.9 K", "P₂ = P₁·2^1.4 = 263.9 kPa",
           "0.0200·20.79·95.85 = 39.85 J", "P₂ = 200 kPa", "nRT ln 2 = 34.58 J", "39.85 against 34.58 J")
    worked = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == "transport-23")["worked_example"]
    for phrase in ("V₁ = 0.4988 L", "395.9 K", "263.9 kPa", "39.85 J", "300 K and 200 kPa", "34.58 J"):
        assert phrase in worked, phrase


def test_lesson_is_scheduled_after_control_volumes_and_links_prerequisites():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[1]["lesson_ids"] == ["transport-1", "transport-23", "transport-14", "transport-15"]
    assert weeks[1]["assessment_ids"][:2] == ["transport-1-practice", "transport-23-practice"]
    for target in ("01-control-volumes-and-conservation.md", "14-entropy-balances-and-irreversibility.md"):
        assert f"]({target})" in READING and (COURSE / "modules" / target).exists()
    assert "work done by the volume is positive" in (COURSE / "modules/01-control-volumes-and-conservation.md").read_text(encoding="utf-8")
    assert "link-only scope comparators" in READING and "partial, unreviewed and formative-only" in READING and "synthetic" in READING.lower()
    assert tuple(int(part) for part in MANIFEST["version"].split(".")) >= (0, 7, 0)
    assert (MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == ("partial", "unreviewed", "formative-only")
    lesson = next(x for m in MANIFEST["modules"] for x in m["lessons"] if x["id"] == "transport-23")
    covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
    assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == 13 and len(lesson["card_ids"]) == 4
    objectives = {o["id"]: o for o in MANIFEST["lesson_objectives"]}
    outcomes = {o["id"] for o in MANIFEST["outcomes"]}
    for objective_id in lesson["objectives"]:
        assert objectives[objective_id]["description"] in READING
        assert set(objectives[objective_id]["course_outcome_ids"]) <= outcomes


def test_crosswalk_records_both_comparators_and_its_limits():
    for phrase in (
        "https://ocw.mit.edu/courses/20-110j-thermodynamics-of-biomolecular-systems-fall-2005/pages/calendar/", "https://oyc.yale.edu/physics/phys-200", "compiled with AI assistance",
        "not a review by the owner", "| Heat engines and the Carnot cycle | — | Lecture 23 (title and a listed chapter); Lecture 24 (chapter 1, a review) | — | Absent; named only by Yale |",
        "Absent: statistical thermodynamics is not developed", "Absent: no reading teaches reaction enthalpy; named only by MIT", "Covered in outline", "Shallow:", "Local extension",
        "Absent by design", "Ten problem sets and three hour exams in the calendar", "Weekly homework, one midterm and a final exam in the syllabus",
    ):
        assert phrase in CROSSWALK, phrase
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    links = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    local = {link for link in links if not link.startswith("https://")}
    assert local - readings == {"../../../docs/COURSE_SCOPE_AUDIT.md"}
    assert all((COURSE / link).resolve().exists() for link in local)
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for sid in ("transport-yale-phys200", "transport-entropy-thermo"):
        assert registry[sid]["reuse_mode"] == "link-only-comparator" and not registry[sid]["permissions"]["quotation"], sid
        assert "transport-module-23" in registry[sid]["mapped_modules"] and "transport" in registry[sid]["mapped_courses"], sid


ABSENT_TERMS = ("Carnot", r"\bheat engine\b", "Clapeyron", "colligative", "Debye", "Archimedes", "Gibbs.Duhem", "Maxwell relation", r"\bHess\b", "Boltzmann distribution", "partition function")


def test_topics_the_crosswalk_labels_absent_appear_in_no_local_reading():
    for module in MANIFEST["modules"]:
        for lesson in module["lessons"]:
            text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
            for term in ABSENT_TERMS:
                assert not re.search(term, text, re.IGNORECASE), (lesson["id"], term)
    assert "Cycles and heat engines are not developed" in READING
    # the foundation terms the crosswalk says were missing before 0.7.0 now appear only in the new reading
    others = "\n".join((COURSE / lesson["reading"]).read_text(encoding="utf-8")
                       for module in MANIFEST["modules"] for lesson in module["lessons"] if lesson["id"] != "transport-23")
    for term in ("state function", "internal energy", "ideal gas"):
        assert term in READING and term not in others.lower(), term


MISCONCEPTIONS = {
    "isothermal-work": 31.76,  # log10 in place of the natural logarithm
    "adiabatic-final-temperature": 229.74,  # gamma = 7/5 used for a monatomic gas
    "adiabatic-work": 100.29,  # C_p in place of C_v
    "isobaric-heat": 41.57,  # C_v in place of C_p
    "adiabatic-pressure": 450.0,  # the isothermal result
    "body-temperature-volume": 0.0304,  # Celsius used as kelvin
    "isochoric-enthalpy": 29.93,  # the internal-energy change
    "internal-energy-change": 50.92,  # the heat absorbed, with C_p
    "irreversible-work": 80.68,  # the reversible work
    "entropy-generation": 0.2305,  # the gas's entropy change alone
}


@pytest.mark.parametrize("slug,wrong", MISCONCEPTIONS.items(), ids=list(MISCONCEPTIONS))
def test_numeric_keys_reject_the_named_misconception(slug, wrong):
    item = BANK[f"transport-23:{slug}"]
    assert grade(item, AttemptRequest(response=str(item["solution_spec"]["answer"]))).correct
    assert not grade(item, AttemptRequest(response=str(wrong))).correct


@pytest.mark.parametrize("slug", ["state-function", "free-expansion"])
def test_single_choice_items_accept_only_the_key(slug):
    item = BANK[f"transport-23:{slug}"]
    key = item["solution_spec"]["answer"]
    assert [grade(item, AttemptRequest(response=str(index))).correct for index in range(len(item["options"]))] == [index == key for index in range(len(item["options"]))]


def test_multiple_select_item_gives_partial_credit_for_correct_minus_incorrect():
    item = BANK["transport-23:process-claims"]
    assert item["solution_spec"]["answer"] == [0, 2, 4] and item["points"] == 2
    scores = {tuple(response): grade(item, AttemptRequest(response=response)).score for response in ([0, 2, 4], [0, 2, 4, 1], [0, 2], [1, 3], [0, 1, 2, 3, 4])}
    assert scores[(0, 2, 4)] == pytest.approx(2.0) and scores[(0, 2, 4, 1)] == pytest.approx(4 / 3) and scores[(0, 2)] == pytest.approx(4 / 3)
    assert scores[(1, 3)] == 0 and scores[(0, 1, 2, 3, 4)] == pytest.approx(2 / 3)
