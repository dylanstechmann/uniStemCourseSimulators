"""Exact atom/unit counts need no measured-quantity precision penalty."""
import json
from copy import deepcopy
from pathlib import Path

import pytest
from courselab.grading import grade
from courselab.schemas import AttemptRequest
from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = json.loads((ROOT / "content/schemas/question.schema.json").read_text(encoding="utf-8"))
QUESTION = {
    "id": "count-precision-fixture", "type": "data_interpretation",
    "prompt": "Report the exact atom count and identify its evidence basis.",
    "points": 2, "objective_ids": ["atom-count"], "visibility": "public-practice-authoring",
    "response_fields": [
        {"id": "count", "type": "numeric", "prompt": "Exact carbon atom count.", "unit": "", "points": 1},
        {"id": "basis", "type": "single_choice", "prompt": "What defines this count?",
         "options": ["The supplied formula.", "A measured concentration."], "points": 1},
    ],
    "solution_spec": {"field_specs": [
        {"id": "count", "type": "numeric", "answer": 12, "unit": "", "tolerance": 0,
         "unit_required": False, "significant_figures": None, "dimensions": None},
        {"id": "basis", "type": "single_choice", "answer": 0},
    ]},
    "feedback": {"hint": "Count atoms in the supplied formula.",
                 "solution": "The supplied formula has exactly twelve carbon atoms.", "lesson_ids": []},
}


def test_exact_count_schema_and_grader_accept_a_whole_number_without_false_precision():
    Draft202012Validator(SCHEMA).validate(QUESTION)
    assert grade(QUESTION, AttemptRequest(response={"count": "12", "basis": "0"})).correct
    assert not grade(QUESTION, AttemptRequest(response={"count": "12.1", "basis": "0"})).correct


@pytest.mark.parametrize("invalid", [0, 13, True, 1.5, "3"])
def test_nullable_precision_does_not_accept_invalid_nonnull_precision(invalid):
    question = deepcopy(QUESTION)
    question["solution_spec"]["field_specs"][0]["significant_figures"] = invalid
    with pytest.raises(ValidationError):
        Draft202012Validator(SCHEMA).validate(question)


def test_opted_in_significant_figures_are_still_enforced():
    question = deepcopy(QUESTION)
    question["solution_spec"]["field_specs"][0]["significant_figures"] = 3
    Draft202012Validator(SCHEMA).validate(question)
    assert not grade(question, AttemptRequest(response={"count": "12", "basis": "0"})).correct
    assert grade(question, AttemptRequest(response={"count": "12.0", "basis": "0"})).correct
