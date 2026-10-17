"""Regression checks for the Genetics ordered-tetrad and centromere-distance reading."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/genetics"
LESSON = "genetics-18"


def _manifest() -> dict:
    return json.loads((COURSE / "course.json").read_text(encoding="utf-8"))


def _practice() -> dict[str, dict]:
    bank = json.loads((COURSE / "question-banks/practice.json").read_text(encoding="utf-8"))
    return {question["id"]: question for question in bank["questions"]}


def _centromere_cm(sds: int, asci: int) -> Fraction:
    # Single-exchange model: recombination frequency is half the SDS fraction; cM = 100 r.
    return Fraction(100, 2) * Fraction(sds, asci)


def _expected_sds(distance_cm: Fraction, asci: int) -> Fraction:
    # A recombination frequency r makes the SDS fraction 2r.
    return asci * 2 * distance_cm / 100


# Each key is recalculated here from the counts in the prompt, not copied from the bank.
NUMERIC_KEYS = {
    "genetics-18:sds-distance-300": _centromere_cm(42, 300),
    "genetics-18:four-spore-sds-400": _centromere_cm(60, 400),
    "genetics-18:expected-sds-12cm": _expected_sds(Fraction(12), 500),
    "genetics-18:expected-sds-15cm": _expected_sds(Fraction(15), 600),
    "genetics-18:expected-fds-20cm": 200 - _expected_sds(Fraction(20), 200),
    # Rule of three: with no SDS ascus among n, the SDS fraction is below about 3/n.
    "genetics-18:zero-sds-bound-600": _centromere_cm(3, 600),
}

CHOICE_KEYS = {
    "genetics-18:sister-products": "Spores 1 and 2, and spores 3 and 4",
    "genetics-18:four-spore-pattern": "A a A a",
    "genetics-18:eight-spore-fds": "A A A A a a a a",
    "genetics-18:zero-sds": "point estimate is 0 cM",
    "genetics-18:sds-underestimate": "multiple exchanges",
    "genetics-18:sds-plateau": "ceiling",
}


def test_ordered_tetrad_reading_is_delivered_and_bounded():
    manifest = _manifest()
    assert manifest["maturity"] == "partial"
    assert manifest["review"]["status"] == "unreviewed"
    assert manifest["grading_policy"]["mode"] == "formative-only"

    module = next(module for module in manifest["modules"] if module["id"] == "genetics-module-18")
    assert [lesson["id"] for lesson in module["lessons"]] == [LESSON]
    week5 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 5)
    assert week5["lesson_ids"] == ["genetics-7", LESSON]
    assert week5["assessment_ids"] == ["genetics-7-practice", f"{LESSON}-practice"]
    lesson = module["lessons"][0]
    text = (COURSE / lesson["reading"]).read_text(encoding="utf-8")
    assert len(text.split()) >= 800
    for phrase in (
        "First-division segregation (FDS)",
        "Second-division segregation (SDS)",
        "r = ½ × (SDS asci ÷ total asci)",
        "d = 50 × (SDS asci ÷ total asci)",
        "rule of three",
        "exchanges involving the same pair of non-sister chromatids leave both dyads homozygous",
        "levels off near two-thirds",
        "In budding yeast the four spores lie in no fixed order",
        "gene conversion",
        "Limits of this lesson",
    ):
        assert phrase in text, phrase


def test_ordered_tetrad_numeric_keys_match_independent_recalculation():
    practice = _practice()
    numeric = {key for key, item in practice.items() if key.startswith(LESSON + ":") and item["type"] == "numeric"}
    assert numeric == set(NUMERIC_KEYS)
    for key, expected in NUMERIC_KEYS.items():
        spec = practice[key]["solution_spec"]
        assert abs(Fraction(str(spec["answer"])) - expected) <= Fraction(str(spec["tolerance"])), key
        assert spec["tolerance"] <= 0.5, key


def test_rule_of_three_bound_is_close_to_the_exact_binomial_bound():
    # The exact 95% upper bound for zero events in 600 trials is 1 - 0.05 ** (1 / 600).
    exact_cm = 50 * (1 - 0.05 ** (1 / 600))
    spec = _practice()["genetics-18:zero-sds-bound-600"]["solution_spec"]
    assert abs(spec["answer"] - exact_cm) <= spec["tolerance"]


def test_ordered_tetrad_choice_keys_point_at_the_correct_option():
    practice = _practice()
    choice = {key for key, item in practice.items() if key.startswith(LESSON + ":") and item["type"] == "single_choice"}
    assert choice == set(CHOICE_KEYS)
    for key, phrase in CHOICE_KEYS.items():
        options = practice[key]["options"]
        assert phrase in options[practice[key]["solution_spec"]["answer"]], key
        assert sum(phrase in option for option in options) == 1, key


def test_ordered_tetrad_practice_assessment_lists_every_item():
    manifest = _manifest()
    practice = _practice()
    items = [key for key in practice if key.startswith(LESSON + ":")]
    assessment = next(item for item in manifest["assessments"] if item["id"] == f"{LESSON}-practice")
    assert assessment["question_ids"] == items
    assert assessment["points"] == sum(practice[key]["points"] for key in items)
    lesson = next(lesson for module in manifest["modules"] for lesson in module["lessons"] if lesson["id"] == LESSON)
    assert lesson["question_ids"] == items


def test_ordered_tetrad_cards_are_linked_to_the_reading_and_its_objectives():
    manifest = _manifest()
    objectives = {objective["id"] for objective in manifest["lesson_objectives"]}
    cards = json.loads((COURSE / "question-banks/retrieval-cards.json").read_text(encoding="utf-8"))["cards"]
    new_cards = [card for card in cards if card["lesson_id"] == LESSON]
    assert len(new_cards) == 5
    for card in new_cards:
        assert set(card["objective_ids"]) <= objectives
    covered = {objective for card in new_cards for objective in card["objective_ids"]}
    assert covered == {f"{LESSON}-objective-{n}" for n in range(1, 5)}
