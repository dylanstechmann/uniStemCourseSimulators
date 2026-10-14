"""Audit private machine-check keys with the production deterministic grader."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal
from pathlib import Path

from courselab.grading import count_significant_figures, grade
from courselab.schemas import AttemptRequest

ROOT = Path(__file__).resolve().parents[1]


def _number_text(value: Decimal, significant_figures: int | None, unit: str | None) -> str:
    if significant_figures is None:
        number = str(value)
    elif value == 0:
        number = f"{0:.{significant_figures}f}"
    else:
        decimal_places = significant_figures - 1 - value.copy_abs().adjusted()
        number = (
            format(value, f".{decimal_places}f")
            if decimal_places >= 0
            else format(value, f".{significant_figures - 1}e")
        )
        if count_significant_figures(number) != significant_figures:
            number = format(value, f".{significant_figures - 1}e")
    return f"{number} {unit}" if unit else number


def _responses(question: dict) -> tuple[dict[str, str], dict[str, dict], dict[str, dict]]:
    fields = {field["id"]: field for field in question["response_fields"]}
    specs = {spec["id"]: spec for spec in question["solution_spec"]["field_specs"]}
    if fields.keys() != specs.keys():
        raise ValueError("field IDs do not match")
    response: dict[str, str] = {}
    for field_id, field in fields.items():
        spec = specs[field_id]
        if field["type"] == "numeric":
            response[field_id] = _number_text(
                Decimal(str(spec["answer"])),
                spec.get("significant_figures"),
                spec.get("unit"),
            )
        elif field["type"] == "single_choice":
            response[field_id] = str(spec["answer"])
        else:
            raise ValueError("unsupported private response field type")
    return response, fields, specs


def _wrong_value(field: dict, spec: dict) -> str:
    if field["type"] == "single_choice":
        answer = spec["answer"]
        wrong = next(index for index in range(len(field["options"])) if index != answer)
        return str(wrong)
    answer = Decimal(str(spec["answer"]))
    absolute_tolerance = Decimal(str(spec.get("tolerance", 0)))
    relative_tolerance = Decimal(str(spec.get("relative_tolerance", 0)))
    delta = max(
        absolute_tolerance * 10,
        abs(answer) * max(relative_tolerance * 10, Decimal("0.25")),
        Decimal(1),
    )
    return _number_text(
        answer + delta, spec.get("significant_figures"), spec.get("unit")
    )


def audit(private_root: Path, course_id: str) -> tuple[int, int]:
    assignment_root = private_root / "courses" / course_id / "assignments"
    if not assignment_root.is_dir():
        raise FileNotFoundError(f"Private assignment directory not found: {assignment_root}")

    question_count = 0
    field_count = 0
    for path in sorted(assignment_root.glob("*-review-draft.json")):
        candidate = json.loads(path.read_text(encoding="utf-8"))
        for question in candidate.get("questions", []):
            if not question.get("solution_spec", {}).get("field_specs"):
                continue
            response, fields, specs = _responses(question)
            result = grade(question, AttemptRequest(response=response))
            points = float(question["points"])
            if not result.correct or result.score != points:
                raise ValueError(f"Full-credit response failed for {question['id']}")
            question_count += 1
            field_count += len(fields)
            for field_id, field in fields.items():
                mutated = response.copy()
                mutated[field_id] = _wrong_value(field, specs[field_id])
                mutation_result = grade(
                    question, AttemptRequest(response=mutated)
                )
                expected = points - float(field["points"])
                if mutation_result.score != expected:
                    raise ValueError(
                        f"One-field mutation did not lose only its field points for {question['id']}"
                    )

    if question_count == 0:
        raise ValueError("No private machine-check questions were audited")
    return question_count, field_count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--private-assessments-root",
        type=Path,
        default=ROOT / ".local/private-assessments",
    )
    parser.add_argument("--course-id", default="biochemistry")
    args = parser.parse_args()
    questions, fields = audit(args.private_assessments_root, args.course_id)
    print(
        f"Private grader audit PASS: {questions} questions, {fields} response fields; "
        f"{fields} one-field mutations each lost exactly their field points."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
