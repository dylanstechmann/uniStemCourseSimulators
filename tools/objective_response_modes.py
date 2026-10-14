#!/usr/bin/env python3
"""Inventory Cell Biology practice formats and ungraded written-response resources.

This records authored item formats, not the validity, depth, accessibility, or
cognitive demand of an item. It reads only public practice packets.

    python tools/objective_response_modes.py                 # print Markdown
    python tools/objective_response_modes.py --write FILE    # save Markdown
    python tools/objective_response_modes.py --check FILE    # fail on drift
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE_ROOT = ROOT / "content" / "courses" / "cell-biology"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def question_format(question: dict) -> str:
    kind = question.get("type", "unknown")
    if kind != "structured":
        return kind
    fields = Counter(field.get("type", "unknown") for field in question.get("response_fields", []))
    if not fields:
        return "structured"
    detail = ", ".join(f"{name}×{count}" for name, count in sorted(fields.items()))
    return f"structured[{detail}]"


def audit(course_root: Path = COURSE_ROOT) -> dict:
    manifest_path = course_root / "course.json"
    manifest = load(manifest_path)
    package_root = manifest_path.parent.resolve()
    questions: dict[str, dict] = {}

    for assessment in manifest.get("assessments", []):
        if assessment.get("mode") != "practice" or not assessment.get("question_ids"):
            continue
        bank_path = (package_root / assessment["path"]).resolve()
        if not bank_path.is_relative_to(package_root) or not bank_path.is_file():
            raise ValueError(f"Public practice bank is missing or escapes course: {assessment.get('path')}")
        bank_questions = {question["id"]: question for question in load(bank_path).get("questions", [])}
        for question_id in assessment["question_ids"]:
            question = bank_questions.get(question_id)
            if question is None:
                raise ValueError(f"Practice assessment references missing question: {question_id}")
            if question.get("visibility") != "public-practice-authoring":
                continue
            prior = questions.get(question_id)
            if prior is not None and prior != question:
                raise ValueError(f"Conflicting public question definitions: {question_id}")
            questions[question_id] = question

    objective_rows = []
    for objective in manifest.get("lesson_objectives", []):
        linked = sorted(
            (question for question in questions.values() if objective["id"] in question.get("objective_ids", [])),
            key=lambda question: question["id"],
        )
        formats = Counter(question_format(question) for question in linked)
        objective_rows.append({
            "id": objective["id"],
            "bloom": objective.get("bloom", "unspecified"),
            "description": objective["description"],
            "question_count": len(linked),
            "question_ids": [question["id"] for question in linked],
            "formats": dict(sorted(formats.items())),
        })

    source_map_path = (package_root / manifest["source_map"]).resolve()
    if not source_map_path.is_relative_to(package_root) or not source_map_path.is_file():
        raise ValueError("Course source map is missing or escapes the public package")
    source_map = load(source_map_path)
    mapped_by_module = {
        entry.get("module_id"): entry
        for entry in source_map.get("modules", [])
        if isinstance(entry, dict)
    }
    valid_objectives = {objective["id"] for objective in manifest.get("lesson_objectives", [])}
    written_response_lessons = []
    for module in manifest.get("modules", []):
        mapped_module = mapped_by_module.get(module.get("id"), {})
        relationship = mapped_module.get("relationship", "")
        if "ungraded-written-response" not in relationship:
            continue
        for lesson in module.get("lessons", []):
            reading = lesson.get("reading")
            reading_path = (package_root / reading).resolve() if isinstance(reading, str) else None
            if reading_path is None or not reading_path.is_relative_to(package_root) or not reading_path.is_file():
                raise ValueError(f"Ungraded writing resource is missing or escapes course: {reading}")
            if mapped_module.get("reading") != reading or mapped_module.get("lesson_id") != lesson.get("id"):
                raise ValueError(f"Writing resource source map is stale for {lesson.get('id')}")
            objective_ids = lesson.get("objectives", [])
            if not isinstance(objective_ids, list) or not set(objective_ids) <= valid_objectives:
                raise ValueError(f"Writing resource has unknown objective links: {lesson.get('id')}")
            if lesson.get("question_ids", []):
                raise ValueError(f"Ungraded writing resource unexpectedly references question-bank items: {lesson.get('id')}")
            written_response_lessons.append({
                "lesson_id": lesson["id"],
                "title": lesson["title"],
                "reading": reading,
                "objective_ids": objective_ids,
                "relationship": relationship,
            })
    written_response_lessons.sort(key=lambda lesson: lesson["lesson_id"])

    return {
        "course_id": manifest["id"],
        "version": manifest["version"],
        "maturity": manifest.get("maturity", "unspecified"),
        "review": manifest.get("review", {}).get("status", "unspecified"),
        "grading_mode": manifest.get("grading_policy", {}).get("mode", "unspecified"),
        "questions": len(questions),
        "objectives": objective_rows,
        "ungraded_written_response_lessons": written_response_lessons,
        "evidence_scope": "public-practice-format-and-ungraded-writing-resource-inventory-only",
    }


def markdown_cell(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def render(report: dict) -> str:
    objectives = report["objectives"]
    format_counts: Counter[str] = Counter()
    for objective in objectives:
        for format_name in objective["formats"]:
            format_counts[format_name] += 1

    lines = [
        "# Cell Biology objective response-format audit",
        "",
        "Generated by `python tools/objective_response_modes.py`. The response-format table covers public questions",
        "referenced by practice-mode assessments in the named package version. It does not score question quality,",
        "prove that a response format measures the objective verb, or establish depth, mastery, fairness, or accessibility.",
        "A separate inventory lists formal course lessons whose source maps identify ungraded written-response practice.",
        "That list records authored objective links only; it does not assess prompt quality, learner work, or human scoring.",
        "Structured items may contain only selected-response fields. This is not a free-response performance audit.",
        "No maturity, grading, review, or release status is changed by this report.",
        "",
        f"**Package:** `{report['course_id']}` {report['version']} · `{report['maturity']}` · review `{report['review']}` · grading `{report['grading_mode']}`",
        f"**Scope:** {report['questions']} distinct public practice items mapped to {len(objectives)} lesson objectives.",
        "",
        "| Objective | Bloom label | Public items | Mapped response formats | Objective description |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for objective in objectives:
        formats = ", ".join(
            f"`{name}` ({count})" for name, count in objective["formats"].items()
        ) or "—"
        lines.append(
            f"| `{objective['id']}` | {markdown_cell(objective['bloom'])} | {objective['question_count']} | {formats} | "
            f"{markdown_cell(objective['description'])} |"
        )
    lines.extend([
        "",
        "## Format summary",
        "",
        "Counts below are objectives with at least one mapped item of the listed type; an objective can appear in multiple rows.",
        "",
        "| Response format | Objectives linked |",
        "| --- | ---: |",
    ])
    for name, count in sorted(format_counts.items()):
        lines.append(f"| `{name}` | {count} |")
    lines.extend([
        "",
        "## Ungraded written-response practice resources",
        "",
        "These optional course lessons invite written or diagrammed responses but collect no answers and contribute no points.",
        "The objective links are authoring metadata, not evidence that learners demonstrate the linked skill.",
        "",
        "| Lesson | Reading | Linked objectives |",
        "| --- | --- | --- |",
    ])
    for lesson in report["ungraded_written_response_lessons"]:
        reading = "../content/courses/cell-biology/" + lesson["reading"]
        objectives_text = ", ".join(f"`{objective_id}`" for objective_id in lesson["objective_ids"])
        lines.append(
            f"| {markdown_cell(lesson['title'])} | [{lesson['reading']}]({reading}) | {objectives_text} |"
        )
    lines.extend([
        "",
        "This is an authoring inventory for reviewer navigation. Objective verbs such as explain, interpret, or design still need",
        "qualified review against actual prompts, expected reasoning, feedback, and learner work; mapped formats alone cannot establish that alignment.",
        "",
    ])
    return "\n".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=COURSE_ROOT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", type=Path)
    mode.add_argument("--check", type=Path)
    args = parser.parse_args(argv)
    try:
        report = render(audit(args.root))
        if args.write:
            args.write.write_text(report, encoding="utf-8")
        elif args.check:
            if not args.check.is_file() or args.check.read_text(encoding="utf-8") != report:
                parser.exit(1, f"{args.check} is stale; regenerate it with --write.\n")
        else:
            sys.stdout.write(report)
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as exc:
        parser.exit(1, f"Objective response-format audit failed: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
