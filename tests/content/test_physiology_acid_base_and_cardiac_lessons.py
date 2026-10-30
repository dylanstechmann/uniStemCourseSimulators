"""Physiology 0.7.0 lessons 24 (acid-base balance) and 25 (cardiac cycle and ECG): stated numbers, schedule, comparators, grading.

pH and compensation come from the Henderson-Hasselbalch relation, the daily ledger from a day-by-day loop, ventricular filling by
integrating its rate equation, the heart-rate optimum by scanning, and the lead amplitudes by projecting explicit vectors, not from
the readings. Same-AI checks, not human review.
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
COURSE = ROOT / "content/courses/physiology"
MANIFEST = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
BANK = {q["id"]: q for q in json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))["questions"]}
CARDS = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
R24 = (COURSE / "modules/acid-base-balance-bicarbonate-buffer-and-compensation.md").read_text(encoding="utf-8")
R25 = (COURSE / "modules/cardiac-cycle-conduction-and-the-ecg.md").read_text(encoding="utf-8")
CROSSWALK = (COURSE / "scope-crosswalk.md").read_text(encoding="utf-8")


def stated(text, *phrases):
    missing = [phrase for phrase in phrases if phrase not in text]
    assert not missing, missing


def ph(bicarbonate, pco2):
    return 6.1 + math.log10(bicarbonate / (0.03 * pco2))


def filling(rate, tau=0.25, v_inf=130.0, esv=50.0, steps=40000):
    """Integrate dV/dt = (V_inf - V)/tau over the stipulated diastole; returns diastole, EDV, SV and CO."""
    period = 60 / rate
    diastole = period - (0.15 + 0.2 * period)
    volume = esv
    for _ in range(steps):
        volume += (v_inf - volume) / tau * diastole / steps
    return diastole, volume, volume - esv, rate * (volume - esv) / 1000


def closed_form_output(rate, tau=0.25):
    period = 60 / rate
    diastole = period - (0.15 + 0.2 * period)
    return rate * (130 - 80 * math.exp(-diastole / tau) - 50) / 1000


def lead(p, theta_deg, axis_deg):
    return p * math.cos(math.radians(theta_deg - axis_deg))


def phase(p_lv, p_la, p_ao, falling):
    mitral, aortic = p_la > p_lv, p_lv > p_ao
    if mitral:
        return "filling"
    if aortic:
        return "ejection"
    return "isovolumic relaxation" if falling else "isovolumic contraction"


def test_acid_base_reading_numbers_recompute():
    assert ph(24, 40) == pytest.approx(7.401, abs=5e-4) and 10 ** (9 - ph(24, 40)) == pytest.approx(39.7, abs=0.05)
    assert ph(24, 40) - ph(24, 80) == pytest.approx(math.log10(2), abs=1e-12) and ph(48, 80) == pytest.approx(ph(24, 40))
    assert ph(24, 40 / 0.6) == pytest.approx(7.18, abs=0.005) and 40 / 0.6 == pytest.approx(66.7, abs=0.05)
    assert ph(24, 80) == pytest.approx(7.10, abs=0.005) and ph(12, 40) == pytest.approx(7.10, abs=0.005)
    assert ph(12, 28) == pytest.approx(7.255, abs=5e-4) and 12 / (0.03 * 28) == pytest.approx(14.3, abs=0.05)
    d, e = ph(24, 40) - ph(12, 40), ph(24, 40) - ph(12, 28)
    assert d == pytest.approx(0.301, abs=5e-4) and e == pytest.approx(0.146, abs=5e-4)
    assert d / e - 1 == pytest.approx(1.06, abs=0.005) and 1 - e / d == pytest.approx(0.51, abs=0.005)
    assert 0.863 * 200 / 40 == pytest.approx(4.32, abs=0.0051) and 0.863 * 200 / 28 == pytest.approx(6.16, abs=0.005)
    assert (0.863 * 200 / 28) / (0.863 * 200 / 40) - 1 == pytest.approx(0.43, abs=0.005)
    assert ph(30, 60) == pytest.approx(7.32, abs=0.005) and ph(24, 60) == pytest.approx(7.22, abs=0.005)
    stated(R24, "pH = 6.1 + log₁₀ 20 = 7.40", "about 39.7 nmol/L", "log₁₀ 2 = 0.30", "ratio is 24/2.0 = 12 and pH = 6.1 + log₁₀ 12 = 7.18",
           "pH = 6.1 + log₁₀ 14.3 = 7.255", "6.16 L/min", "an increase of 43%", "G = d/e − 1 = 1.06", "removed 1 − e/d = 51%",
           "ratio of 30/1.8 = 16.7 and pH = 7.32", "7.22 that the acute case would show")


def test_daily_ledger_and_filtered_load_by_simulation():
    bicarbonate = 24.0
    for _ in range(7):
        bicarbonate -= (70 - 60) / 14
    assert bicarbonate == pytest.approx(19.0) and ph(bicarbonate, 40) == pytest.approx(7.30, abs=0.005)
    assert 10 / 14 == pytest.approx(0.71, abs=0.005)
    assert 180 * 24 == 4320 and 0.01 * 180 * 24 == pytest.approx(43.2)
    stated(R24, "180 × 24 = 4320 mmol/day", "loses 43.2 mmol/day", "10/14 = 0.71 mmol/L per day", "24 − 5 = 19 mmol/L", "pH would be 6.1 + log₁₀(19/1.2) = 7.30")


def test_anion_gap_and_co2_fick_numbers():
    assert 140 - 104 - 24 == 12 and 140 - 104 - 12 == 24 and 140 - 116 - 12 == 12
    assert 200 / 5 == 40 and 250 / 5 == 50
    stated(R24, "AG = 12", "AG = 140 − 104 − 12 = 24", "AG = 140 − 116 − 12 = 12", "200/5 = 40 mL/L", "50 mL/L")


def test_acid_base_worked_example_recomputes():
    uncompensated, compensated = ph(15, 40), ph(15, 30)
    assert uncompensated == pytest.approx(7.197, abs=5e-4) and compensated == pytest.approx(7.322, abs=5e-4)
    d, e = 7.401 - uncompensated, 7.401 - compensated
    assert d == pytest.approx(0.204, abs=5e-4) and e == pytest.approx(0.079, abs=5e-4)
    assert d / e - 1 == pytest.approx(1.58, abs=0.01) and 1 - e / d == pytest.approx(0.61, abs=0.005)
    stated(R24, "pH = 6.1 + log₁₀ 12.5 = 7.197", "d = 7.401 − 7.197 = 0.204", "pH = 6.1 + 1.222 = 7.322", "e = 7.401 − 7.322 = 0.079",
           "G = d/e − 1 = 0.204/0.079 − 1 = 1.58", "removed 1 − 0.079/0.204 = 61%")


def test_cardiac_timing_table_and_optimum_by_integration():
    rows = {60: (0.650, 124.1, 74.1, 4.44), 75: (0.490, 118.7, 68.7, 5.15), 120: (0.250, 100.6, 50.6, 6.07),
            150: (0.170, 89.5, 39.5, 5.92), 180: (0.117, 79.8, 29.8, 5.37)}
    for rate, (diastole, edv, sv, co) in rows.items():
        got = filling(rate)
        assert got[0] == pytest.approx(diastole, abs=5e-4) and got[1] == pytest.approx(edv, abs=0.05)
        assert got[2] == pytest.approx(sv, abs=0.05) and got[3] == pytest.approx(co, abs=0.005), rate
        stated(R25, f"| {rate} | {diastole:.3f} | {edv:.1f} | {sv:.1f} | {co:.2f} |")
    assert all(closed_form_output(rate) == pytest.approx(filling(rate)[3], abs=2e-3) for rate in (60, 90, 126, 180))
    best = max(range(40, 221), key=closed_form_output)
    assert best == 126 and closed_form_output(best) == pytest.approx(6.08, abs=0.005)
    outputs = {rate: filling(rate)[3] for rate in (60, 75, 120, 150, 180)}
    assert outputs[60] < outputs[75] < outputs[120] and outputs[120] > outputs[150] > outputs[180]
    assert all(filling(rate)[2] > filling(rate + 15)[2] for rate in (60, 75, 120, 150))  # stroke volume falls steadily with rate
    # diastole absorbs most of the shortening when the rate doubles
    t60, t120 = (0.15 + 0.2 * 1.0, 1.0 - 0.35), (0.15 + 0.2 * 0.5, 0.5 - 0.25)
    assert 1 - t120[0] / t60[0] == pytest.approx(0.29, abs=0.005) and 1 - t120[1] / t60[1] == pytest.approx(0.62, abs=0.005)
    stated(R25, "cut systole by 29% and diastole by 62%", "peaks near 126 beats per minute at about 6.08 L/min")


def test_stiffer_ventricle_and_worked_example():
    assert filling(75, tau=0.40)[2] == pytest.approx(56.5, abs=0.05) and filling(75, tau=0.40)[3] == pytest.approx(4.24, abs=0.005)
    assert filling(120, tau=0.40)[3] == pytest.approx(4.46, abs=0.005)
    assert filling(75)[2] == pytest.approx(68.7, abs=0.05)
    diastole, edv, sv, co = filling(90)
    assert diastole == pytest.approx(0.383, abs=5e-4) and edv == pytest.approx(112.7, abs=0.05)
    assert sv == pytest.approx(62.7, abs=0.05) and co == pytest.approx(5.65, abs=0.005)
    stiff = filling(90, tau=0.40)
    assert stiff[1] == pytest.approx(99.3, abs=0.05) and stiff[2] == pytest.approx(49.3, abs=0.05) and stiff[3] == pytest.approx(4.44, abs=0.005)
    assert 1 - stiff[3] / co == pytest.approx(0.21, abs=0.005)
    stated(R25, "= 130 − 80 × 0.216 = 112.7 mL", "so SV = 62.7 mL", "CO = 90 × 62.7 = 5.65 L/min", "EDV = 130 − 80 × 0.384 = 99.3 mL",
           "SV = 49.3 mL and CO = 4.44 L/min, a loss of about 21%", "SV becomes 56.5 mL and CO 4.24 L/min", "CO is 4.46 L/min against 6.07")


def test_valve_logic_assigns_the_phases_stated_in_the_reading():
    assert phase(5, 8, 80, falling=True) == "filling"
    assert phase(60, 8, 100, falling=True) == "isovolumic relaxation" and phase(60, 8, 100, falling=False) == "isovolumic contraction"
    assert phase(118, 8, 116, falling=False) == "ejection"
    assert (120 - 50, (120 - 50) / 120) == (70, pytest.approx(0.583, abs=5e-4))
    stated(R25, "EF = 70/120 = 0.583", "volume cannot change", "this is isovolumic relaxation", "the aortic valve is open and the ventricle is ejecting")


def test_conduction_and_pacemaker_numbers():
    atrial, node, purkinje = 0.05 / 1.0, 0.005 / 0.05, 0.04 / 3.0
    assert (atrial, node) == pytest.approx((0.050, 0.100)) and purkinje == pytest.approx(0.0133, abs=5e-5)
    assert atrial + node + purkinje == pytest.approx(0.163, abs=5e-4) and node > atrial > purkinje
    slow = 0.005 / 0.04
    assert slow == pytest.approx(0.125) and atrial + slow + purkinje == pytest.approx(0.188, abs=5e-4)
    assert 60 / ((-40 - -60) / 25) == pytest.approx(75) and 60 / ((-40 - -60) / 30) == pytest.approx(90)
    assert (-40 - -60) / (60 / 100) == pytest.approx(33.3, abs=0.05) and (-40 - -60) / 30 == pytest.approx(0.667, abs=5e-4)
    assert 60 / 0.75 == pytest.approx(80)
    stated(R25, "0.163 s", "0.125 s and the total rises to 0.188 s", "20/25 = 0.80 s, or 75 beats per minute", "raises the rate to 90",
           "20/0.60 = 33.3 mV/s", "R–R = 0.75 s gives 80 per minute")


def test_lead_projections_and_einthoven_law():
    for theta in range(-180, 181, 15):
        i, ii, iii = (lead(1.0, theta, axis) for axis in (0, 60, 120))
        assert ii == pytest.approx(i + iii, abs=1e-12), theta
    i, ii, iii = (lead(1.2, 60, axis) for axis in (0, 60, 120))
    assert (i, ii, iii) == pytest.approx((0.6, 1.2, 0.6))
    i, ii, iii = (lead(1.0, 90, axis) for axis in (0, 60, 120))
    assert abs(i) < 1e-12 and ii == pytest.approx(0.866, abs=5e-4) and iii == pytest.approx(0.866, abs=5e-4)
    theta = math.degrees(math.atan2((2 * 1.0 - 0.8) / math.sqrt(3), 0.8))
    p = math.hypot(0.8, (2 * 1.0 - 0.8) / math.sqrt(3))
    assert theta == pytest.approx(40.9, abs=0.05) and p == pytest.approx(1.06, abs=0.005)
    assert (lead(p, theta, 0), lead(p, theta, 60), lead(p, theta, 120)) == pytest.approx((0.8, 1.0, 0.2), abs=1e-9)
    assert lead(p, theta, 120) == pytest.approx(1.06 * math.cos(math.radians(-79.1)), abs=5e-3)
    stated(R25, "II = I + III", "I = 0.6, II = 1.2 and III = 0.6 mV", "θ = 40.9° and p = 1.06 mV", "lead III is II − I = 0.2 mV", "0.866 p")


def test_lessons_are_scheduled_where_the_comparators_place_the_topics():
    weeks = {w["week"]: w for w in MANIFEST["duration"]["weeks"]}
    assert weeks[5]["lesson_ids"] == ["physiology-3", "physiology-25"]
    assert weeks[5]["assessment_ids"] == ["physiology-3-practice", "physiology-25-practice"]
    assert weeks[7]["lesson_ids"] == ["physiology-11", "physiology-24"]
    assert weeks[7]["assessment_ids"] == ["physiology-11-practice", "physiology-24-practice"]
    for text, targets in ((R24, ("11-respiratory-mechanics-and-gas-exchange.md", "08-homeostasis-balance-and-feedback-gain.md",
                                 "06-renal-clearance-and-tubular-handling.md", "14-compensation-and-reserve.md",
                                 "../../general-chemistry-2/modules/01-acid-base-equilibria-and-buffers.md",
                                 "../../biochemistry/modules/07-binding-equilibria-and-cooperativity.md")),
                          (R25, ("10-hemodynamics-pressure-flow-resistance-compliance.md", "15-passive-membrane-and-cable-properties.md",
                                 "14-compensation-and-reserve.md", "../../physics-em/modules/24-electric-dipoles-fields-torque-energy-and-force.md",
                                 "../../linear-algebra/modules/08-orthogonality-projections-and-qr.md"))):
        for target in targets:
            assert f"]({target})" in text and (COURSE / "modules" / target).resolve().exists(), target
        assert "gives no medical advice" in text and "synthetic" in text
    assert (MANIFEST["version"], MANIFEST["maturity"], MANIFEST["review"]["status"], MANIFEST["grading_policy"]["mode"]) == (
        "0.7.0", "partial", "unreviewed", "formative-only")
    objectives = {o["id"]: o for o in MANIFEST["lesson_objectives"]}
    outcomes = {o["id"] for o in MANIFEST["outcomes"]}
    lessons = {x["id"]: x for m in MANIFEST["modules"] for x in m["lessons"]}
    for lesson_id, text, cards in (("physiology-24", R24, 5), ("physiology-25", R25, 4)):
        lesson = lessons[lesson_id]
        covered = {o for q in lesson["question_ids"] for o in BANK[q]["objective_ids"]}
        assert covered == set(lesson["objectives"]) and len(lesson["question_ids"]) == 12 and len(lesson["card_ids"]) == cards
        assert {c["id"] for c in CARDS if c["lesson_id"] == lesson_id} == set(lesson["card_ids"])
        assert len(text.split()) >= 1400
        for objective_id in lesson["objectives"]:
            assert objectives[objective_id]["description"] in text
            assert set(objectives[objective_id]["course_outcome_ids"]) <= outcomes
        practice = next(a for a in MANIFEST["assessments"] if a["id"] == f"{lesson_id}-practice")
        assert practice["mode"] == "practice" and practice["points"] == sum(BANK[q]["points"] for q in lesson["question_ids"]) == 14


def test_crosswalk_records_all_comparators_and_its_limits():
    stated(CROSSWALK, "https://ocw.mit.edu/courses/hst-542j-quantitative-physiology-organ-transport-systems-spring-2004/pages/calendar/",
           "https://www.physiology.arizona.edu/sites/default/files/2023-09/BME_PSIO%20511%20Syllabus%202023.pdf",
           "https://www.colorado.edu/lab/tan/sites/default/files/attached-files/mcen4171.pdf", "compiled with AI assistance", "not a review by the owner",
           "| Cardiac electrophysiology and the ECG | Lec 5–7 | Cardiac Electrophysiology – ECG | Unit 5b |",
           "| Acid–base physiology | — (no lecture title names it) | pH and Acid Base Regulation; Pulmonary regulation of acid-base balance | Units 6b and 7a |",
           "Covered in 0.7.0; previously absent", "Covered in 0.7.0; previously shallow", "Absent by design", "year is not printed")
    readings = {lesson["reading"] for module in MANIFEST["modules"] for lesson in module["lessons"]}
    local = {part.split(")")[0] for part in CROSSWALK.split("](")[1:]}
    local = {link for link in local if not link.startswith("https://")}
    assert all((COURSE / link).resolve().exists() for link in local)
    assert {link for link in local if link.startswith(("modules/", "labs/"))} <= readings
    registry = {s["id"]: s for s in json.loads((ROOT / "content/sources/registry.json").read_text(encoding="utf-8"))["sources"]}
    for sid in ("physiology-arizona-psio511", "physiology-colorado-mcen4117"):
        assert registry[sid]["reuse_mode"] == "link-only-comparator" and not registry[sid]["permissions"]["quotation"], sid
        assert registry[sid]["accessed_at"] == "2026-10-30" and registry[sid]["imported_assets"] == [], sid
        assert {"physiology-module-24", "physiology-module-25"} <= set(registry[sid]["mapped_modules"]), sid
    assert "physiology-module-25" in registry["physiology-semester-organ-calendar"]["mapped_modules"]
    modules = {m["id"]: m for m in MANIFEST["modules"]}
    assert all("physiology-arizona-psio511" in modules[f"physiology-module-{n}"]["source_ids"] for n in (24, 25))
    assert "physiology-semester-organ-calendar" in modules["physiology-module-25"]["source_ids"]


# Topics the crosswalk labels absent are named in no local reading; the chloride shift is absent although carbamino compounds are named.
ABSENT_TERMS = (r"\bbaroreflex", r"\bbaroreceptor", r"\bautoregulation", r"\bthyroid", r"\bparathyroid", r"\bgastrointestinal", r"\barrhythmia",
                r"chloride shift", r"neuromuscular junction")


def test_topics_the_crosswalk_labels_absent_appear_in_no_local_reading():
    for module in MANIFEST["modules"]:
        for lesson in module["lessons"]:
            text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
            for term in ABSENT_TERMS:
                assert not re.search(term, text, re.IGNORECASE), (lesson["id"], term)


def shown(value, sig):
    if sig == 3:
        return f"{value:.{max(0, 2 - math.floor(math.log10(abs(value))))}f}"
    return f"{value:g}"


MISCONCEPTIONS = {
    "24": {
        "chronic-respiratory-ph": 6.1 + math.log10(30 / 60),  # forgetting the CO2 solubility
        "ventilation-fall-ph": 6.1 + math.log10(24 / (0.03 * 40 * 0.6)),  # scaling P_CO2 instead of dividing by the fraction
        "compensated-ph": 6.1 + math.log10(12 / (0.03 * 40)),  # the uncompensated value
        "compensation-ventilation": 0.863 * 200 / 40 * 28 / 40,  # multiplying by the pressure ratio
        "loop-gain": (7.401 - 7.100) / (7.401 - 7.255),  # forgetting the minus one
        "daily-ledger-ph": 6.1 + math.log10((24 - 10 / 14) / (0.03 * 40)),  # one day, not seven
        "filtered-shortfall": 180 * 0.01,  # omitting the concentration
        "anion-gap": 142 - 108,  # omitting bicarbonate
        "co2-fick": 250 * 5,  # multiplying instead of dividing
    },
    "25": {
        "ejection-fraction": (130 - 50) / 50,  # dividing by the end-systolic volume
        "diastolic-time-100": 0.15 + 0.2 * 0.6,  # systole
        "stroke-volume-120": 130 - 80 * math.exp(-1),  # end-diastolic volume
        "output-150": filling(120)[3],  # expecting output to keep rising
        "stiff-output-90": filling(90)[3],  # keeping the earlier time constant
        "av-node-delay": 0.005 / 0.05,  # the earlier velocity
        "pacemaker-slope": 20 * 0.6,  # multiplying by the interval
        "lead-three": 0.4 + 0.9,  # adding instead of subtracting
        "axis-angle": math.degrees(math.atan2(1.0, 0.8)),  # II over I
    },
}
CASES = [(lesson, slug, wrong) for lesson, group in MISCONCEPTIONS.items() for slug, wrong in group.items()]


@pytest.mark.parametrize("lesson,slug,wrong", CASES, ids=[f"{lesson}-{slug}" for lesson, slug, _ in CASES])
def test_numeric_keys_accept_the_key_and_reject_the_named_misconception(lesson, slug, wrong):
    item = BANK[f"physiology-{lesson}:{slug}"]
    spec = item["solution_spec"]
    sig = spec["significant_figures"]
    assert grade(item, AttemptRequest(response=shown(spec["answer"], sig))).correct, shown(spec["answer"], sig)
    assert not grade(item, AttemptRequest(response=shown(wrong, sig))).correct, shown(wrong, sig)


def test_every_new_numeric_item_has_a_named_misconception_and_three_figure_items_say_so():
    numeric = {qid for qid, q in BANK.items() if q["type"] == "numeric" and re.match(r"physiology-2[45]:", qid)}
    assert numeric == {f"physiology-{lesson}:{slug}" for lesson, group in MISCONCEPTIONS.items() for slug in group}
    for qid in numeric:
        spec = BANK[qid]["solution_spec"]
        if spec["significant_figures"] == 3:
            assert BANK[qid]["prompt"].endswith("to three significant figures."), qid
            assert not grade(BANK[qid], AttemptRequest(response=shown(spec["answer"], 3) + "0")).correct, qid  # a fourth figure
        else:
            assert BANK[qid]["prompt"].endswith("Enter the number only."), qid


@pytest.mark.parametrize("item_id", ["24:same-ph-different-cause", "25:phase-from-pressures"])
def test_single_choice_items_accept_only_the_key(item_id):
    item = BANK[f"physiology-{item_id}"]
    key = item["solution_spec"]["answer"]
    accepted = [index for index in range(len(item["options"])) if grade(item, AttemptRequest(response=str(index))).correct]
    assert accepted == [key]


def test_choice_keys_follow_from_the_models():
    same = BANK["physiology-24:same-ph-different-cause"]
    assert ph(24, 80) == pytest.approx(ph(12, 40)) and "differ in which term moved" in same["options"][same["solution_spec"]["answer"]]
    pressures = BANK["physiology-25:phase-from-pressures"]
    assert pressures["options"][pressures["solution_spec"]["answer"]] == "Isovolumic relaxation" == phase(60, 8, 100, falling=True).capitalize()
    lowers = BANK["physiology-24:which-changes-lower-ph"]
    # (bicarbonate factor, P_CO2 factor): rising P_CO2, falling bicarbonate, falling P_CO2, both doubled, half and +50%
    factors = [(1.0, 1.5), (0.5, 1.0), (1.0, 0.5), (2.0, 2.0), (0.5, 1.5)]
    expected = [index for index, (b, p) in enumerate(factors) if ph(24 * b, 40 * p) < ph(24, 40) - 1e-12]
    assert expected == lowers["solution_spec"]["answer"] == [0, 1, 4]


@pytest.mark.parametrize("item_id,key", [("24:which-changes-lower-ph", [0, 1, 4]), ("24:anion-gap-statements", [0, 1, 2]),
                                         ("25:filling-model-statements", [0, 1, 3]), ("25:dipole-statements", [0, 1])])
def test_multiple_select_items_give_partial_credit_for_correct_minus_incorrect(item_id, key):
    item = BANK[f"physiology-{item_id}"]
    assert item["solution_spec"]["answer"] == key and item["points"] == 2
    assert item["solution_spec"]["partial_credit"] == "correct-minus-incorrect-clamped-v1"
    options = range(len(item["options"]))
    wrong = next(index for index in options if index not in key)
    full = grade(item, AttemptRequest(response=key)).score
    assert full == pytest.approx(2.0)
    assert grade(item, AttemptRequest(response=[*key, wrong])).score < full
    assert grade(item, AttemptRequest(response=[wrong])).score == 0
    assert grade(item, AttemptRequest(response=list(options))).score < full
