"""Independent discrete tail, cohort-standardization and lineage-mixture references."""

from __future__ import annotations
import json
import re
from functools import cache
from pathlib import Path
import pytest
import sympy as sp
from courselab.content import ContentRepository
from courselab.grading import grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "content/courses/geroscience"
MANIFEST = json.loads((DIRECTORY / "course.json").read_text())
NEW = {
    q["id"]: q
    for q in json.loads((DIRECTORY / "question-banks/practice.json").read_text())[
        "questions"
    ]
    if re.fullmatch(r"geroscience-(1[89]|2[01]):depth-\d+", q["id"])
}
R = sp.Rational


def trigger(lengths, threshold, loss):
    for n in range(1000):
        if min(lengths) - n * loss <= threshold:
            return n
    raise AssertionError("No trigger in declared search bound")


@cache
def calculations():
    lengths = list(map(R, ["3.2", "4.0", "4.8", "5.6", "6.4", "7.2"]))
    other = list(map(R, ["2.9", "4.1", "4.8", "5.6", "6.4", "7.4"]))
    assigned = list(map(R, ["3.1", "4.1", "5.1", "6.1"]))
    target_control = (R(20, 50) + R(40, 50)) / 2
    target_treated = (R(40, 50) + R(45, 50)) / 2
    fraction = (R(36, 100) - R(1, 10)) / (R(3, 5) - R(1, 10))
    return {
        (18, 1): dict(
            mean=sum(lengths) / len(lengths),
            minimum=min(lengths),
            divisions=trigger(lengths, R(14, 5), R(1, 10)),
        ),
        (18, 2): dict(
            mean=sum(other) / len(other), divisions=trigger(other, R(14, 5), R(1, 10))
        ),
        (18, 3): dict(
            net_shortening=R(1, 20),
            trigger=trigger(lengths, R(14, 5), R(1, 20)),
            population_doublings=sp.log(R(1024, 64), 2),
        ),
        (18, 4): {},
        (19, 1): dict(
            mean=sum(assigned) / 4,
            minimum=min(assigned),
            without=trigger(assigned, R(13, 5), R(1, 10)),
            **{"with": trigger(assigned, R(13, 5), R(1, 20))},
        ),
        (19, 2): dict(doublings=sp.log(R(2048, 64), 2)),
        (20, 1): dict(
            a_difference=R(40 - 20, 50),
            b_difference=R(45 - 40, 50),
            contrast=R(40 - 20, 50) - R(45 - 40, 50),
        ),
        (20, 2): dict(
            control=target_control,
            intervention=target_treated,
            difference=target_treated - target_control,
        ),
        (21, 1): dict(
            fraction=fraction, cells=1000 * fraction, naive=R(36, 100) / R(3, 5)
        ),
        (21, 2): dict(
            scar_change=R(12 - 24, 100),
            relative_reduction=R(24 - 12, 24),
            improvement=R(7 - 5, 10),
            deficit=R(9 - 7, 10),
        ),
    }


@pytest.mark.parametrize("qid", sorted(NEW))
def test_geroscience_fields_and_actual_grader_reject_individual_errors(qid):
    number, item = map(
        int, re.fullmatch(r"geroscience-(\d+):depth-(\d+)", qid).groups()
    )
    question = NEW[qid]
    values = calculations()[number, item]
    specs = question["solution_spec"]["field_specs"]
    assert set(values) == {s["id"] for s in specs if s["type"] == "numeric"}
    response = {}
    for spec in specs:
        if spec["type"] == "single_choice":
            response[spec["id"]] = str(spec["answer"])
        else:
            value = float(values[spec["id"]])
            assert value == pytest.approx(spec["answer"], rel=1e-11, abs=1e-13)
            response[spec["id"]] = (
                format(value, ".2e") if spec["significant_figures"] else str(int(value))
            )
    assert grade(question, AttemptRequest(response=response)).correct
    for spec in specs:
        if spec["type"] == "numeric":
            wrong = (
                format(float(values[spec["id"]]) * 1.2, ".2e")
                if spec["significant_figures"]
                else str(int(values[spec["id"]]) + 1)
            )
        else:
            wrong = str((spec["answer"] + 1) % 3)
        assert not grade(
            question, AttemptRequest(response={**response, spec["id"]: wrong})
        ).correct


def test_discrete_end_trigger_checks_both_sides_of_first_integer():
    for lengths, threshold, loss in [
        ([R(16, 5)], R(14, 5), R(1, 10)),
        ([R(29, 10)], R(14, 5), R(1, 10)),
        ([R(31, 10)], R(13, 5), R(1, 20)),
        ([R(31, 10)], R(13, 5), R(3, 20)),
    ]:
        n = trigger(lengths, threshold, loss)
        assert min(lengths) - (n - 1) * loss > threshold >= min(lengths) - n * loss
    assert trigger([R(31, 10)], R(13, 5), R(3, 20)) == 4
    assert calculations()[18, 1]["mean"] == calculations()[18, 2]["mean"]
    assert calculations()[18, 1]["divisions"] != calculations()[18, 2]["divisions"]


def test_net_population_doublings_do_not_identify_individual_histories():
    # Two original cells may each divide twice,or one may divide three times while the other is lost.
    assert 2 * 2**2 == 2**3
    assert sp.log(R(8, 2), 2) == 2
    # Equal endpoint counts do not identify the lineage division count or loss mechanism.
    assert 3 != 2


def test_target_standardization_preserves_within_setting_and_changes_with_weights():
    for weight in [R(1, 4), R(1, 2), R(3, 4)]:
        control = weight * R(2, 5) + (1 - weight) * R(4, 5)
        treated = weight * R(4, 5) + (1 - weight) * R(9, 10)
        assert treated - control == weight * R(2, 5) + (1 - weight) * R(1, 10)
    assert calculations()[20, 2]["difference"] == R(1, 4)
    # The same horizon total can have early or late deaths,so event timing is not identified.
    assert sum(t > 5 for t in [1, 1, 9, 9]) == sum(t > 5 for t in [4, 4, 9, 9]) == 2
    assert sum(t > 2 for t in [1, 1, 9, 9]) != sum(t > 2 for t in [4, 4, 9, 9])


def test_lineage_mixture_domains_background_and_nonidentifiable_equal_detection():
    f, e, q = sp.symbols("f e q")
    p = f * e + (1 - f) * q
    assert sp.simplify((p - q) / (e - q) - f) == 0
    assert sp.diff(p, f).subs(e, q) == 0
    result = calculations()[21, 1]["fraction"]
    assert result == R(13, 25) and result * R(3, 5) + (1 - result) * R(1, 10) == R(
        9, 25
    )
    assert (R(8, 10) - R(1, 10)) / (R(3, 5) - R(1, 10)) > 1


def test_geroscience_delivery_source_chronology_and_access_boundaries():
    assert len(NEW) == 10 and MANIFEST["version"] == "0.7.0"
    assert (
        MANIFEST["maturity"] == "partial"
        and MANIFEST["review"]["status"] == "unreviewed"
    )
    repository = ContentRepository(ROOT / "content")
    ids = [x for w in MANIFEST["duration"]["weeks"] for x in w["lesson_ids"]]
    assert len(ids) == len(set(ids)) == 23
    for n in range(18, 22):
        lesson = repository.lesson("geroscience", f"geroscience-{n}")
        assert len(lesson.markdown.split()) >= 700
        assert (
            len(lesson.questions)
            == len(lesson.retrieval_cards)
            == (4 if n == 18 else 2)
        )
    nutrient = (
        DIRECTORY / "modules/07-nutrient-sensing-and-lifespan-interventions.md"
    ).read_text()
    assert (
        "https://pubmed.ncbi.nlm.nih.gov/22932268/" in nutrient
        and "https://www.nature.com/articles/ncomms14063" in nutrient
    )
    assert "2012,not2017" in nutrient
    regeneration = (DIRECTORY / "modules/08-regeneration-across-species.md").read_text()
    assert (
        "https://pubmed.ncbi.nlm.nih.gov/12481136/" in regeneration
        and "https://pubmed.ncbi.nlm.nih.gov/20336145/" in regeneration
    )
    foundation = repository.lesson("geroscience", "geroscience-18").markdown
    assert "full-text retrieval was blocked" in foundation
