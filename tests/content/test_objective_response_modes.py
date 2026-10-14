"""The response-format report stays tied to public course mappings."""

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "objective_response_modes", ROOT / "tools/objective_response_modes.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_generated_report_is_current_and_reports_are_not_maturity_evidence():
    report = MODULE.audit()
    rendered = MODULE.render(report)

    assert report["course_id"] == "cell-biology"
    assert report["version"] == json.loads((ROOT / "content/courses/cell-biology/course.json").read_text(encoding="utf-8"))["version"]
    assert report["maturity"] == "partial"
    assert report["review"] == "unreviewed"
    assert report["grading_mode"] == "formative-only"
    assert report["evidence_scope"] == "public-practice-format-and-ungraded-writing-resource-inventory-only"
    assert len(report["objectives"]) == 69
    assert report["questions"] == 166
    assert len(report["ungraded_written_response_lessons"]) == 2
    assert rendered == (ROOT / "docs/CELL_BIOLOGY_RESPONSE_MODE_AUDIT.md").read_text(encoding="utf-8")
    assert "does not score question quality" in rendered
    assert "not a free-response performance audit" in rendered
    assert "does not assess prompt quality, learner work, or human scoring" in rendered
    assert "Ungraded written-response practice resources" in rendered
    assert "solution_spec" not in rendered


def test_explanation_objectives_show_their_structured_and_single_choice_formats():
    report = MODULE.audit()
    objectives = {item["id"]: item for item in report["objectives"]}
    for objective_id in (
        "cell-biology-13-objective-1",
        "cell-biology-15-objective-1",
        "cell-biology-17-objective-1",
    ):
        objective = objectives[objective_id]
        assert objective["question_count"] == 3
        assert objective["formats"]["single_choice"] == 2
        assert objective["formats"]["structured[single_choice×3]"] == 1


def test_ungraded_writing_inventory_maps_both_rehearsals_without_claiming_scoring():
    report = MODULE.audit()
    resources = {item["lesson_id"]: item for item in report["ungraded_written_response_lessons"]}

    assert set(resources) == {
        "cell-biology-review-early-written",
        "cell-biology-review-design-studio",
    }
    assert resources["cell-biology-review-early-written"]["objective_ids"] == [
        "cell-biology-5-objective-1",
        "cell-biology-2-objective-1",
        "cell-biology-2-objective-2",
    ]
    assert set(resources["cell-biology-review-design-studio"]["objective_ids"]) == {
        "cell-biology-20-objective-3",
        "cell-biology-22-objective-3",
        "cell-biology-24-objective-3",
        "cell-biology-26-objective-3",
        "cell-biology-28-objective-2",
    }
    assert all("ungraded-written-response" in item["relationship"] for item in resources.values())
