import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "content/courses/biochemistry"


def test_proposed_grade_policy_is_explicit_and_inactive():
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    proposal = (COURSE / "assessment-specs/grading-policy-candidate.md").read_text(
        encoding="utf-8"
    )

    weights = [
        int(value)
        for value in re.findall(
            r"\|\s*(?:Homework|Midterm|Cumulative final|Integrative project)\s*\|\s*(\d+)%",
            proposal,
        )
    ]
    assert weights == [40, 20, 25, 15]
    assert sum(weights) == 100
    assert "Eight homework candidates, weighted equally at 5% each" in proposal
    assert "Status: inactive proposal for review only." in proposal
    assert "course.json` must keep `grading_policy.mode` set to `formative-only`" in proposal

    assert manifest["version"] == manifest["history"][-1]["version"]
    assert manifest["grading_policy"]["mode"] == "formative-only"
    assert manifest["grading_policy"]["categories"] == []
    active_assessments = {item["id"] for item in manifest["assessments"]}
    assert not any("candidate" in assessment_id for assessment_id in active_assessments)
    assert "inactive grading-policy proposal" in (COURSE / "syllabus.md").read_text(
        encoding="utf-8"
    )
