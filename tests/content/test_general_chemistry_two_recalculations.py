"""Separate synthetic chemistry calculations, not independent human review.

No authoring imports. Checks committed keys with conservation, root finding,
ODE integration and reconstructed observations under the declared models.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/general-chemistry-2"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


BANK = {q["id"]: q for q in load(COURSE / "question-banks/practice.json")["questions"]}


def root(function, low, high):
    fl = function(low)
    assert fl * function(high) <= 0
    for _ in range(90):
        mid = (low + high) / 2
        fm = function(mid)
        if fl * fm <= 0:
            high = mid
        else:
            low, fl = mid, fm
    return (low + high) / 2


def integrate(function, initial, time, steps=1200):
    """RK4 on component balances, distinct from author's exponential keys."""
    state = list(initial)
    dt = time / steps
    for _ in range(steps):
        a = function(state)
        b = function([v + dt * k / 2 for v, k in zip(state, a)])
        c = function([v + dt * k / 2 for v, k in zip(state, b)])
        d = function([v + dt * k for v, k in zip(state, c)])
        state = [
            v + dt * (ka + 2 * kb + 2 * kc + kd) / 6
            for v, ka, kb, kc, kd in zip(state, a, b, c, d)
        ]
    return state


def reversible(initial, time):
    def derivative(state):
        net = 0.048 * state[0] - 0.012 * state[1]
        return [-net, net]

    return integrate(derivative, initial, time)


def acid_fractions(h):
    # Successive concentration ratios, normalized by their common total.
    weights = [1, 1e-5 / h, (1e-5 / h) * (1e-8 / h)]
    return [x / math.fsum(weights) for x in weights]


def lab_data():
    with (COURSE / "labs/relaxation-reports.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    groups = {}
    for row in rows:
        groups.setdefault(row["sample"], []).append(float(row["reported_a_mm"]))
    means = {key: math.fsum(values) / len(values) for key, values in groups.items()}
    return rows, groups, means


def titration_ph(acid_ml, acid_m, base_ml, base_m=0.1, pkas=(), strong=False):
    """Exact charge balance Na + h = (acid anion charge) + Kw/h for an acid titrated with NaOH."""
    volume = acid_ml + base_ml
    total, sodium = acid_m * acid_ml / volume, base_m * base_ml / volume
    constants = [10 ** -pka for pka in pkas]

    def residual(log_h):
        h = 10**log_h
        if strong:
            anion = total
        else:
            terms = [1.0]
            for k in constants:
                terms.append(terms[-1] * k / h)
            anion = total * sum(i * t for i, t in enumerate(terms)) / sum(terms)
        return sodium + h - anion - 1e-14 / h

    return -root(residual, -14, 0)


def steepest_volume(curve, low, high, points=4001):
    """Volume of maximum slope of a computed titration curve (the inflection used as the endpoint)."""
    step = (high - low) / (points - 1)
    volumes = [low + i * step for i in range(points)]
    slopes = [(curve(v + 1e-4) - curve(v - 1e-4)) / 2e-4 for v in volumes]
    return volumes[max(range(points), key=slopes.__getitem__)]


def expected_answers():
    answers = {}

    def add(lesson, **values):
        answers.update(
            {
                f"general-chemistry-2-{lesson}:{key.replace('_', '-')}": value
                for key, value in values.items()
            }
        )

    add(
        1,
        check=7.2 + math.log10(10),
        henderson_hasselbalch=4.76 + math.log10(0.2 / 0.1),
    )
    add(
        2,
        check=root(lambda t: math.exp(-0.35 * t) - 0.5, 0, 10),
        arrhenius_ratio=math.exp(50000 / 8.314 * (1 / 298 - 1 / 308)),
    )
    add(3, check=-2 * 96485 * 0.30 / 1000, cell_potential=0.34 - (-0.76))
    ratio = 10 ** (7.4 - 6.86)
    acid = 0.1 / (1 + ratio)
    base = 0.1 - acid
    add(
        5,
        ratio=ratio,
        base_concentration=100 * 3.467 / (1 + 3.467),
        ph_after_acid=6.86 + math.log10(0.0676 / 0.0324),
        capacity=2.303 * 0.1 * ratio / (1 + ratio) ** 2 * 1000,
        unionized_fraction=100 / (1 + 10 ** (9 - 7.4)),
    )
    assert acid + base == pytest.approx(0.1)
    ea = root(
        lambda energy: math.exp(energy / 8.314 * (1 / 298.15 - 1 / 310.15)) - 2.6,
        0,
        100000,
    )
    add(
        6,
        first_order_remaining=100 * math.exp(-0.0231 * 60),
        second_order_halflife=root(
            lambda t: 0.02 / (1 + 0.5 * 0.02 * t) - 0.01, 0, 200
        ),
        activation_energy=ea / 1000,
        cold_rate=0.001 * math.exp(-61200 / 8.314 * (1 / 277.15 - 1 / 298.15)),
    )
    add(
        7,
        nernst=-0.32 + 0.06155 / 2 * math.log10(10),
        delta_g=-2 * 96485 * (0.045 - (-0.2892)) / 1000,
        free_calcium=(0.001 / (1e7 * 0.001)) * 1e6,
    )
    rt = 8.314 * 300
    k = root(lambda value: rt * math.log(value) - 3000, 1, 10)
    b_eq = root(lambda b: b / (1 - b) - k, 0, 0.99)
    add(
        8,
        standard_g=(12000 - 300 * 50) / 1000,
        crossing=root(lambda t: 12000 - 50 * t, 0, 400),
        equilibrium_constant=k,
        current_g=rt * math.log(10 / k) / 1000,
        equilibrium_b=b_eq,
        coupled_k=math.exp(math.log(4) + math.log(0.5)),
    )
    fractions = acid_fractions(1e-6)
    charge = fractions[1] + 2 * fractions[2]
    add(
        9,
        neutral_fraction=fractions[0],
        mono_fraction=fractions[1],
        di_fraction=fractions[2],
        mean_charge=charge,
        spectator_difference=0.01 * charge + 1e-14 / 1e-6 - 1e-6,
        amphiprotic_ph=-math.log10(math.sqrt(1e-5 * 1e-8)),
    )
    m = math.log(0.008 / 0.002) / math.log(2)
    n = math.log(0.004 / 0.002) / math.log(2)
    kc = 0.002 / (0.1**m * 0.2**n)
    intermediate = root(lambda value: value / (0.1 * 0.2) - 5, 0, 0.2)
    add(
        10,
        a_order=m,
        b_order=n,
        rate_constant=kc,
        predicted_rate=kc * 0.15**m * 0.30**n,
        pre_equilibrium_rate=0.2 * intermediate,
        pseudo_first=0.5 * 0.2,
    )
    a20, _ = reversible([1, 0], 20)
    add(
        11,
        relaxation=0.048 + 0.012,
        plateau=root(lambda a: 0.048 * a - 0.012 * (1 - a), 0, 1),
        twenty=a20,
        displacement_half=root(lambda t: reversible([1, 0], t)[0] - 0.6, 0, 30),
        actual_half=root(lambda t: reversible([1, 0], t)[0] - 0.5, 0, 30),
        intermediate_peak=root(
            lambda t: 2 * math.exp(-0.1 * t) - math.exp(-0.05 * t), 0, 30
        ),
    )
    e0 = 0.4 - (-0.1)
    g0 = -2 * 96485 * e0
    g_current = g0 + rt * math.log(100)
    add(
        12,
        standard_potential=e0,
        standard_g=g0 / 1000,
        nernst_potential=-g_current / (2 * 96485),
        ln_k=-g0 / rt,
        charge=0.5 * 120,
        target_amount=(0.8 * 0.5 * 120) / (2 * 96485),
    )
    # Solve in free metal rather than author's complex-concentration quadratic.
    free_metal = root(
        lambda free: (0.001 - free) - 1e4 * free * (0.0015 - (0.001 - free)), 0, 0.001
    )
    bound = 0.001 - free_metal
    add(
        13,
        donor_count=3 * 2,
        complex_charge=2 - 2,
        bound_metal=bound,
        free_metal=free_metal,
        fixed_ligand_fraction=root(lambda f: f / (1 - f) - 1, 0, 0.99),
        spin_energy=((-2.4 * 200 + 3 * 150) - (-0.4 * 200 + 150)),
    )
    simple = root(lambda s: s * s - 1e-8, 0, 0.001)
    common = root(lambda s: s * (0.01 + s) - 1e-8, 0, 0.001)
    complex_total = root(lambda s: s * (s / 101) - 1e-8, 0, 0.01)
    add(
        14,
        pure_solubility=simple,
        common_ion=common,
        two_anions=root(lambda s: s * (2 * s) ** 2 - 4e-12, 0, 0.001),
        saturation_ratio=0.001 * 0.00002 / 1e-8,
        complexed_total=complex_total,
        complexed_free=complex_total / 101,
    )
    # Lesson 15: every pH from the exact charge balance; volumes from the steepest point of the curve.
    add(
        15,
        equivalence_concentration=0.1
        * steepest_volume(lambda v: titration_ph(20, 0.082, v, 0.1, (4.5,)), 15, 18)
        / 20,
        initial_weak_acid_ph=titration_ph(25, 0.05, 0, 0.1, (3.86,)),
        buffer_region_ph=titration_ph(25, 0.1, 10, 0.1, (4.76,)),
        half_equivalence_pka=titration_ph(25, 0.0736, 9.2, 0.1, (5.12,)),
        equivalence_ph=titration_ph(20, 0.08, 16, 0.1, (4.2,)),
        past_equivalence_ph=titration_ph(25, 0.1, 27, 0.1, (4.76,)),
        strong_acid_before_equivalence=titration_ph(25, 0.1, 24.5, strong=True),
        diprotic_second_equivalence=steepest_volume(
            lambda v: titration_ph(20, 0.05, v, 0.1, (3.0, 7.0)), 17, 23
        ),
    )
    _, _, means = lab_data()
    offset = means["blank"]
    d0 = means["t00"] - offset - 0.2
    d20 = means["t20"] - offset - 0.2
    fitted = root(lambda value: d0 * math.exp(-value * 20) - d20, 0, 0.1)
    forward = root(lambda kf: kf / (fitted - kf) - 4, 0, fitted * 0.99)
    add(
        "lab-01",
        background=offset,
        relaxation=fitted,
        forward=forward,
        reserved_prediction=0.2 + d0 * math.exp(-fitted * 60),
    )
    return answers


EXPECTED = expected_answers()


@pytest.mark.parametrize("item_id,expected", EXPECTED.items(), ids=list(EXPECTED))
def test_numeric_key_matches_separate_calculation(item_id, expected):
    spec = BANK[item_id]["solution_spec"]
    allowed = spec["tolerance"] + abs(expected) * spec.get("relative_tolerance", 0)
    assert abs(spec["answer"] - expected) <= allowed + 1e-12


def test_all_numeric_items_are_covered_without_silent_new_keys():
    numeric = {key for key, q in BANK.items() if q["type"] == "numeric"}
    assert numeric == set(EXPECTED)
    assert len(numeric) == 72
    assert (
        sum(q["solution_spec"].get("unit_required", False) for q in BANK.values()) == 10
    )


CSV_CHECKS = BANK["general-chemistry-2-lab-01:summary"]["solution_spec"][
    "validation_spec"
]["checks"]


@pytest.mark.parametrize("check", CSV_CHECKS, ids=[c["id"] for c in CSV_CHECKS])
def test_csv_checks_recompute_from_committed_reports(check):
    _, groups, means = lab_data()
    values = groups[check["row_id"]]
    assert check["calculation"]["values"] == pytest.approx(values)
    expected = (
        len(values)
        if check["column"] == "replicates"
        else round(means[check["row_id"]], 4)
    )
    assert check["answer"] == pytest.approx(expected, abs=1e-12)


@pytest.mark.parametrize("time", [0, 10, 20, 30, 40, 60])
def test_lab_reconstruction_and_reversible_conservation(time):
    rows, groups, means = lab_data()
    sample = f"t{time:02d}"
    a, b = reversible([1, 0], time)
    assert a >= 0 and b >= 0
    assert a + b == pytest.approx(1, abs=1e-12)
    assert means[sample] == pytest.approx(round(a + 0.05, 4), abs=1e-12)
    assert groups[sample] == pytest.approx(
        [means[sample] - 0.005, means[sample], means[sample] + 0.005]
    )
    assert {int(r["time_min"]) for r in rows if r["sample"] == sample} == {time}


@pytest.mark.parametrize("h", [1e-3, 1e-5, 1e-6, 1e-8, 1e-10])
def test_acid_normalization_mass_equilibrium_and_charge(h):
    f = acid_fractions(h)
    species = [0.01 * x for x in f]
    assert all(x > 0 for x in species)
    assert math.fsum(species) == pytest.approx(0.01)
    assert h * species[1] / species[0] == pytest.approx(1e-5)
    assert h * species[2] / species[1] == pytest.approx(1e-8)
    spectator = species[1] + 2 * species[2] + 1e-14 / h - h
    assert h + spectator == pytest.approx(species[1] + 2 * species[2] + 1e-14 / h)


def test_ligand_conservation_and_invalid_quadratic_root():
    x = EXPECTED["general-chemistry-2-13:bound-metal"]
    metal, ligand = 0.001 - x, 0.0015 - x
    assert 0 < x < 0.001 and metal > 0 and ligand > 0
    assert x / (metal * ligand) == pytest.approx(1e4)
    assert metal + x == pytest.approx(0.001) and ligand + x == pytest.approx(0.0015)
    other_root = 0.001 + 0.0015 + 1e-4 - x
    assert other_root > min(0.001, 0.0015)
    assert x < 0.001 * (1e4 * 0.0015) / (1 + 1e4 * 0.0015)


def test_octahedral_d_six_counts_pairing_and_energies():
    high, low = [2, 1, 1, 1, 1], [2, 2, 2, 0, 0]
    energies = [-0.4 * 200] * 3 + [0.6 * 200] * 2
    totals = [
        sum(n * e for n, e in zip(occ, energies)) + sum(n == 2 for n in occ) * 150
        for occ in [high, low]
    ]
    assert sum(high) == sum(low) == 6
    assert sum(n == 1 for n in high) == 4 and sum(n == 1 for n in low) == 0
    assert totals[1] - totals[0] == -100


def test_solubility_complexation_amount_charge_and_common_ion():
    s = EXPECTED["general-chemistry-2-14:complexed-total"]
    m = EXPECTED["general-chemistry-2-14:complexed-free"]
    ml = s - m
    assert m * s == pytest.approx(1e-8, rel=1e-10, abs=1e-16)
    assert ml / (m * 0.01) == pytest.approx(1e4)
    assert m + ml == pytest.approx(s)
    assert s > EXPECTED["general-chemistry-2-14:pure-solubility"]
    common = EXPECTED["general-chemistry-2-14:common-ion"]
    assert common < 1e-6
    assert (1e-4 / 0.01) / (1e-6 / 0.01) == pytest.approx(100)


def test_free_energy_direction_equation_scaling_and_charge_efficiency():
    rt, f = 8.314 * 300, 96485
    assert (
        EXPECTED["general-chemistry-2-8:standard-g"]
        < 0
        < EXPECTED["general-chemistry-2-8:current-g"]
    )
    q, n, e0 = 100, 2, 0.5
    e = e0 - rt * math.log(q) / (n * f)
    assert e == pytest.approx(e0 - rt * math.log(q**2) / (2 * n * f))
    target = EXPECTED["general-chemistry-2-12:target-amount"]
    assert target * n * f == pytest.approx(0.8 * 60)
    assert e > 0


def test_reversible_equilibrium_flux_and_target_domains():
    assert 0.048 * 0.2 == pytest.approx(0.012 * 0.8)
    a, b = reversible([0.1, 0.9], 20)
    assert 0.1 < a < 0.2 and a + b == pytest.approx(1)
    displaced_half = EXPECTED["general-chemistry-2-11:displacement-half"]
    actual_half = EXPECTED["general-chemistry-2-11:actual-half"]
    assert displaced_half < actual_half
    assert reversible([1, 0], displaced_half)[0] == pytest.approx(0.6)
    assert reversible([1, 0], actual_half)[0] == pytest.approx(0.5)


def test_sequential_intermediate_peak_conserves_total_and_balances_rates():
    def derivative(s):
        return [-0.1 * s[0], 0.1 * s[0] - 0.05 * s[1], 0.05 * s[1]]

    peak = EXPECTED["general-chemistry-2-11:intermediate-peak"]
    a, intermediate, product = integrate(derivative, [1, 0, 0], peak)
    assert [a, intermediate, product] == pytest.approx([0.25, 0.5, 0.25], abs=1e-10)
    assert a + intermediate + product == pytest.approx(1)
    assert 0.1 * a == pytest.approx(0.05 * intermediate)


def test_lab_reference_plateau_naive_rate_and_reserved_point():
    rows, groups, means = lab_data()
    assert len(rows) == 21 and len(groups) == 7
    assert all(not r["time_min"] for r in rows if r["sample"] == "blank")
    offset = means["blank"]
    assert offset == pytest.approx(0.05)
    corrected40 = means["t40"] - offset
    fitted = EXPECTED["general-chemistry-2-lab-01:relaxation"]
    naive = -math.log(corrected40 / (means["t00"] - offset)) / 40
    assert naive < fitted and corrected40 > 0.2
    assert fitted == pytest.approx(0.06, abs=2e-5)
    predicted = EXPECTED["general-chemistry-2-lab-01:reserved-prediction"]
    assert predicted == pytest.approx(means["t60"] - offset, abs=0.0001)


@pytest.mark.parametrize("n", [8, 10, 13])
def test_primary_source_records_preserve_link_only_rights(n):
    manifest = load(COURSE / "course.json")
    module = next(
        m for m in manifest["modules"] if m["id"] == f"general-chemistry-2-module-{n}"
    )
    sources = {
        s["id"]: s for s in load(ROOT / "content/sources/registry.json")["sources"]
    }
    record = next(
        sources[sid]
        for sid in module["source_ids"]
        if sid.startswith("openstax-chem2-")
    )
    assert record["permissions"] == dict(
        linking=True, quotation=False, adaptation=False, redistribution=False
    )
    assert record["imported_assets"] == [] and record["accessed_at"] == ("2026-10-22" if record["id"] == "openstax-chem2-coordination-properties" else "2026-10-09")


def test_proposed_schedule_and_formative_limits():
    manifest = load(COURSE / "course.json")
    lessons = {
        lesson["id"] for module in manifest["modules"] for lesson in module["lessons"]
    }
    weeks = manifest["duration"]["weeks"]
    syllabus = (COURSE / manifest["syllabus"]).read_text(encoding="utf-8")
    assert f"Version: {manifest['version']}." in syllabus and manifest["maturity"] == "partial"
    # Existing core/lab/project plus three foundations and three connected reports.
    assert len(weeks) == 11 and len(lessons) == 23
    assert sorted(lid for week in weeks for lid in week["lesson_ids"]) == sorted(
        lessons
    )
    # Four compact primers share a week with their expanded treatment; week 3 pairs speciation with titration,
    # and week 8 adds the project guide.
    assert [len(week["lesson_ids"]) for week in weeks] == [2, 1, 3, 2, 2, 1, 2, 2, 3, 2, 3]
    assert weeks[2]["lesson_ids"] == ["general-chemistry-2-9", "general-chemistry-2-15", "general-chemistry-2-16"]
    assert weeks[7]["lesson_ids"] == ["general-chemistry-2-12", "general-chemistry-2-project-guide"]
    assert "The 11-week sequence contains 23 reading/activity routes, 132 public practice items and 77 retrieval cards" in syllabus
    assert len(BANK) == 132
    assert len(load(COURSE / "question-banks/retrieval-cards.json")["cards"]) == 77
    assert all(
        a["mode"] in ("practice", "self-assessment") for a in manifest["assessments"]
    )


def test_titration_lesson_statements_match_exact_charge_balance():
    text = (COURSE / "modules/15-acid-base-titration-curves-and-equivalence.md").read_text(encoding="utf-8")
    weak = [titration_ph(25, 0.1, v, 0.1, (4.76,)) for v in (0, 12.5, 20, 25, 26)]
    assert "pH 2.883, 4.761, 5.362, 8.730 and 11.292 at 0, 12.50, 20.00, 25.00 and 26.00 mL" in text
    assert weak == pytest.approx([2.883, 4.761, 5.362, 8.730, 11.292], abs=6e-4)
    for fragment, value in {"**pH 2.88**": weak[0], "**5.36**": weak[2], "**pH 8.73**": weak[3], "**pH 11.29**": weak[4]}.items():
        assert fragment in text and float(fragment.strip("*").split()[-1]) == pytest.approx(value, abs=0.006)
    assert "**pH 2.69**" in text and titration_ph(25, 0.1, 24, strong=True) == pytest.approx(2.69, abs=0.005)
    assert titration_ph(25, 0.1, 25, strong=True) == pytest.approx(7.0, abs=1e-6)
    # Indicator ranges 4-10 on the strong-acid curve span less than 0.1 mL around equivalence.
    low = root(lambda v: titration_ph(25, 0.1, v, strong=True) - 4, 24, 25)
    high = root(lambda v: titration_ph(25, 0.1, v, strong=True) - 10, 25, 26)
    assert high - low < 0.11
    assert "pH = **8.42**" in text and titration_ph(20, 0.08, 16, 0.1, (4.2,)) == pytest.approx(8.42, abs=0.005)
    assert "**10.00 mL** and **20.00 mL**" in text
    first = steepest_volume(lambda v: titration_ph(20, 0.05, v, 0.1, (3.0, 7.0)), 7, 13)
    assert first == pytest.approx(10.0, abs=0.1)
    for volume, pka in ((5.0, 3.0), (15.0, 7.0)):
        assert titration_ph(20, 0.05, volume, 0.1, (3.0, 7.0)) == pytest.approx(pka, abs=0.35)
