"""The optional design studio is mapped to every create-labeled objective."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/cell-biology"
STUDIO = COURSE / "modules/13c-lineage-to-function-design-practice.md"
OBJECTIVE_ROW = re.compile(r"^\| `(cell-biology-[^`]+)` \|", re.MULTILINE)


def test_ungraded_design_studio_covers_each_create_objective_once():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    text = STUDIO.read_text(encoding="utf-8")
    create_objectives = {
        item["id"] for item in manifest["lesson_objectives"]
        if item["bloom"] == "create"
    }
    linked_objectives = OBJECTIVE_ROW.findall(text)

    assert len(linked_objectives) == 5
    assert set(linked_objectives) == create_objectives
    assert len(linked_objectives) == len(set(linked_objectives))
    assert "The platform does not collect, score, or store a response." in text
    assert "no response is collected, scored, or graded" in text
    assert all(f"### {number}. " in text for number in range(1, 5))
    assert "## Design prompt" in text  # The existing week-14 exercise is objective 28-2.

    lesson = next(
        lesson for module in manifest["modules"] for lesson in module["lessons"]
        if lesson["id"] == "cell-biology-review-design-studio"
    )
    week14 = next(week for week in manifest["duration"]["weeks"] if week["week"] == 14)
    assert set(lesson["objectives"]) == create_objectives
    assert lesson["reading"] == STUDIO.relative_to(COURSE).as_posix()
    assert lesson["question_ids"] == lesson["card_ids"] == []
    assert lesson["id"] in week14["lesson_ids"]


def test_design_studio_lesson_links_resolve():
    for target in re.findall(r"\[[^\]]+\]\(([^)#]+\.md)\)", STUDIO.read_text(encoding="utf-8")):
        assert (STUDIO.parent / target).resolve().is_file(), target
