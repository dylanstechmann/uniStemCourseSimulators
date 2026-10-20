import json
from pathlib import Path

import pytest

from courselab.content import ContentInvalid, ContentMissing, ContentRepository


def test_percentage_point_unit_is_public_without_exposing_the_answer_key():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    question = next(
        item
        for item in repository.questions("cell-biology")
        if item["id"] == "cell-biology-12:image-quantification-contrast"
    )

    public = repository.public_question(question)

    assert public.unit == "pp"
    assert "solution_spec" not in public.model_dump()


def test_week14_design_studio_is_a_delivered_ungraded_lesson():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("cell-biology")
    week14 = next(week for week in course.weeks if week.week == 14)

    scheduled = {lesson.id: lesson.title for lesson in week14.lessons}
    assert scheduled["cell-biology-review-design-studio"] == (
        "Experimental-design studio: mechanisms, controls, and follow-up"
    )
    assert all(activity.mode in {"practice", "self-assessment"} for activity in week14.assessments)
    assert course.lesson_count == 45

    lesson = repository.lesson("cell-biology", "cell-biology-review-design-studio")
    assert set(lesson.learning_objective_ids) == {
        "cell-biology-20-objective-3",
        "cell-biology-22-objective-3",
        "cell-biology-24-objective-3",
        "cell-biology-26-objective-3",
        "cell-biology-28-objective-2",
    }
    assert "### 1. Variant mechanism and independent controls" in lesson.markdown
    assert "### 4. Distinguish reduced proliferation" in lesson.markdown
    assert lesson.questions == []


def test_final_review_and_project_routes_render_as_ungraded_learner_material():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("cell-biology")
    weeks = {week.week: week for week in course.weeks}
    assert "cell-biology-project-guide" in {lesson.id for lesson in weeks[10].lessons}
    assert "cell-biology-review-14-synthesis" in {lesson.id for lesson in weeks[14].lessons}
    assert all(activity.mode in {"practice", "self-assessment"} for activity in weeks[14].assessments)

    guide = repository.lesson("cell-biology", "cell-biology-project-guide")
    resource_prefix = "/api/v1/courses/cell-biology/resources/"
    assert f"({resource_prefix}assignments/project-rehearsal-cultures.csv)" in guide.markdown
    assert f"({resource_prefix}assessment-specs/integrative-project-candidate-cultures.csv)" in guide.markdown
    assert "(#/course/cell-biology/lesson/cell-biology-28)" in guide.markdown
    assert len(guide.questions) == 4
    assert all("solution_spec" not in question.model_dump() for question in guide.questions)

    synthesis = repository.lesson("cell-biology", "cell-biology-review-14-synthesis")
    assert f"({resource_prefix}assignments/final-review-feedback-variant-clones.csv)" in synthesis.markdown
    assert "(#/course/cell-biology/lesson/cell-biology-review-8-quantitative)" in synthesis.markdown
    assert synthesis.questions == []
    assert repository.learner_resource(
        "cell-biology", "assignments/final-review-feedback-variant-clones.csv"
    ).startswith(b"genotype,clone,")
    with pytest.raises(ContentMissing, match="Learner resource not found"):
        repository.learner_resource(
            "cell-biology", "assessment-specs/integrative-project-candidate-observations.csv"
        )

    milestones = [case for case in repository.case_studies("cell-biology") if case.id.startswith("cell-biology:project-m")]
    assert [case.id for case in milestones] == [
        "cell-biology:project-m1-question",
        "cell-biology:project-m2-plan",
        "cell-biology:project-m3-evidence",
        "cell-biology:project-m4-interpretation",
        "cell-biology:project-m5-methods",
    ]
    assert all(case.mode == "self-assessment" and case.criteria for case in milestones)


def test_markdown_lesson_links_resolve_to_current_and_archived_routes():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    lesson = repository.lesson("cell-biology", "cell-biology-review-design-studio")

    assert (
        "[Variant mechanism and isogenic evidence](#/course/cell-biology/lesson/cell-biology-20)"
        in lesson.markdown
    )
    assert (
        "[Integrative regenerative-biology study design](#/course/cell-biology/lesson/cell-biology-28)"
        in lesson.markdown
    )
    course = repository.course("cell-biology")
    assert (
        "[ungraded written-design studio](#/course/cell-biology/lesson/cell-biology-review-design-studio)"
        in course.syllabus_markdown
    )
    homework_datasets = {
        "cell-biology-hw1": "assignments/homework-01-m6p-sorting.csv",
        "cell-biology-hw2": "assignments/homework-02-inhibition-rates.csv",
        "cell-biology-hw3": "assignments/homework-03-lesion-removal.csv",
        "cell-biology-hw4": "assignments/homework-04-chip-reporter.csv",
        "cell-biology-hw5": "assignments/homework-05-rna-protein.csv",
        "cell-biology-hw6": "assignments/homework-06-isogenic-clones.csv",
        "cell-biology-hw7": "assignments/homework-07-matrix-spreading.csv",
        "cell-biology-hw8": "assignments/homework-08-cell-state.csv",
    }
    for lesson_id, dataset_path in homework_datasets.items():
        assert f"/lesson/{lesson_id})" in course.syllabus_markdown
        assignment = repository.lesson("cell-biology", lesson_id)
        assert f"/api/v1/courses/cell-biology/resources/{dataset_path}" in assignment.markdown

    linked_reading = repository.lesson("cell-biology", "cell-biology-2")
    assert "https://www.nist.gov/pml/special-publication-330/sp-330-section-2" in linked_reading.markdown
    # The source map is a repository file the app does not serve, so the reading shows its text without a dead link.
    assert "See the package source map and the repository source registry." in linked_reading.markdown
    assert "../source-map.json" not in linked_reading.markdown
    image_lab = repository.lesson("cell-biology", "cell-biology-lab-01")
    assert (
        "[CSV file](/api/v1/courses/cell-biology/resources/labs/image-counts.csv)"
        in image_lab.markdown
    )
    asset_path = "labs/image-counts.csv"
    asset_bytes = repository.learner_resource("cell-biology", asset_path)
    assert asset_bytes == (content_root / "courses/cell-biology" / asset_path).read_bytes()
    with pytest.raises(ContentMissing, match="Learner resource not found"):
        repository.learner_resource(
            "cell-biology", "assessment-specs/lab-01-candidate-observations.csv"
        )

    version = repository.manifest("cell-biology")["version"]
    archived_repository = ContentRepository(
        content_root,
        package_snapshot=("cell-biology", repository.package_files("cell-biology")),
        archived_version=version,
    )
    archived_lesson = archived_repository.lesson(
        "cell-biology", "cell-biology-review-design-studio"
    )
    assert (
        f"[Variant mechanism and isogenic evidence](#/course/cell-biology/version/{version}/lesson/cell-biology-20)"
        in archived_lesson.markdown
    )
    archived_course = archived_repository.course("cell-biology")
    assert (
        f"[ungraded written-design studio](#/course/cell-biology/version/{version}/lesson/cell-biology-review-design-studio)"
        in archived_course.syllabus_markdown
    )
    for lesson_id, dataset_path in homework_datasets.items():
        assert f"/version/{version}/lesson/{lesson_id})" in archived_course.syllabus_markdown
        archived_assignment = archived_repository.lesson("cell-biology", lesson_id)
        assert (
            f"/api/v1/courses/cell-biology/versions/{version}/resources/{dataset_path}"
            in archived_assignment.markdown
        )
    archived_lab = archived_repository.lesson(
        "cell-biology", "cell-biology-lab-01"
    )
    assert (
        "[CSV file](/api/v1/courses/cell-biology/versions/"
        f"{version}/resources/labs/image-counts.csv)"
    ) in archived_lab.markdown
    assert archived_repository.learner_resource(
        "cell-biology", asset_path
    ) == asset_bytes


def test_biochemistry_week14_case_studio_is_delivered_as_ungraded_practice():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week14 = next(week for week in course.weeks if week.week == 14)

    case_activity = next(
        activity for activity in week14.assessments if activity.id == "biochemistry-case"
    )
    assert case_activity.mode == "self-assessment"

    lesson = repository.lesson("biochemistry", "biochemistry-13")
    assert lesson.learning_objective_ids == [
        "biochemistry-13-objective-1",
        "biochemistry-13-objective-2",
        "biochemistry-13-objective-3",
    ]
    assert "## Ungraded case studio:" in lesson.markdown
    assert "Nothing is submitted, collected or graded." in lesson.markdown
    assert "0.50 mmol/(L·h)" in lesson.markdown


def test_biochemistry_week4_purification_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week4 = next(week for week in course.weeks if week.week == 4)

    assert "biochemistry-protein-purification" in {lesson.id for lesson in week4.lessons}
    assert "biochemistry-protein-purification-practice" in {
        assessment.id for assessment in week4.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-protein-purification")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-protein-purification-objective-1",
        "biochemistry-protein-purification-objective-2",
    }
    assert len(lesson.questions) == 6
    assert len(lesson.retrieval_cards) == 4
    assert "| Ion-exchange pool | 20 | 0.80 | 210 | 16 | 4,200 | 262.5 | 70 | 4.375 |" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week9_tca_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week9 = next(week for week in course.weeks if week.week == 9)

    assert "biochemistry-tca-cycle" in {lesson.id for lesson in week9.lessons}
    assert "biochemistry-tca-cycle-practice" in {
        assessment.id for assessment in week9.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-tca-cycle")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-tca-cycle-objective-1",
        "biochemistry-tca-cycle-objective-2",
        "biochemistry-tca-cycle-objective-3",
    }
    assert len(lesson.questions) == 8
    assert len(lesson.retrieval_cards) == 5
    assert "3 NADH are produced per turn" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week8_nucleotide_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week8 = next(week for week in course.weeks if week.week == 8)

    assert "biochemistry-nucleotide-biosynthesis" in {
        lesson.id for lesson in week8.lessons
    }
    assert "biochemistry-nucleotide-biosynthesis-practice" in {
        assessment.id for assessment in week8.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-nucleotide-biosynthesis")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-nucleotide-objective-1",
        "biochemistry-nucleotide-objective-2",
        "biochemistry-nucleotide-objective-3",
    }
    assert len(lesson.questions) == 9
    assert len(lesson.retrieval_cards) == 5
    assert "AMP synthesis from IMP uses aspartate and GTP" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week10_gluconeogenesis_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week10 = next(week for week in course.weeks if week.week == 10)

    assert "biochemistry-gluconeogenesis" in {lesson.id for lesson in week10.lessons}
    assert "biochemistry-gluconeogenesis-practice" in {
        assessment.id for assessment in week10.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-gluconeogenesis")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-gluconeogenesis-objective-1",
        "biochemistry-gluconeogenesis-objective-2",
    }
    assert len(lesson.questions) == 7
    assert len(lesson.retrieval_cards) == 4
    assert "4 ATP, 2 GTP and 2 NADH" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week12_glycogen_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week12 = next(week for week in course.weeks if week.week == 12)

    assert "biochemistry-glycogen-metabolism" in {lesson.id for lesson in week12.lessons}
    assert "biochemistry-glycogen-metabolism-practice" in {
        assessment.id for assessment in week12.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-glycogen-metabolism")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-glycogen-objective-1",
        "biochemistry-glycogen-objective-2",
    }
    assert len(lesson.questions) == 7
    assert len(lesson.retrieval_cards) == 4
    assert "two ATP equivalents per residue incorporated" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week12_cholesterol_lipoprotein_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week12 = next(week for week in course.weeks if week.week == 12)

    assert "biochemistry-cholesterol-lipoproteins" in {
        lesson.id for lesson in week12.lessons
    }
    assert "biochemistry-cholesterol-lipoproteins-practice" in {
        assessment.id for assessment in week12.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-cholesterol-lipoproteins")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-cholesterol-objective-1",
        "biochemistry-cholesterol-objective-2",
        "biochemistry-cholesterol-objective-3",
    }
    assert len(lesson.questions) == 9
    assert len(lesson.retrieval_cards) == 5
    assert "SCAP-SREBP system" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week13_pentose_phosphate_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week13 = next(week for week in course.weeks if week.week == 13)

    assert "biochemistry-pentose-phosphate" in {lesson.id for lesson in week13.lessons}
    assert "biochemistry-pentose-phosphate-practice" in {
        assessment.id for assessment in week13.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-pentose-phosphate")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-ppp-objective-1",
        "biochemistry-ppp-objective-2",
        "biochemistry-ppp-objective-3",
    }
    assert len(lesson.questions) == 9
    assert len(lesson.retrieval_cards) == 5
    assert "2 NADPH, 1 CO2" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week13_fatty_acid_synthesis_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week13 = next(week for week in course.weeks if week.week == 13)

    assert "biochemistry-fatty-acid-synthesis" in {lesson.id for lesson in week13.lessons}
    assert "biochemistry-fatty-acid-synthesis-practice" in {
        assessment.id for assessment in week13.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-fatty-acid-synthesis")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-fatty-synthesis-objective-1",
        "biochemistry-fatty-synthesis-objective-2",
        "biochemistry-neutral-lipid-objective-1",
        "biochemistry-neutral-lipid-objective-2",
    }
    assert len(lesson.questions) == 14
    assert len(lesson.retrieval_cards) == 8
    assert "7 ATP at ACC and 14 NADPH" in lesson.markdown
    assert "ATGL converts TAG to diacylglycerol" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week11_fatty_acid_oxidation_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week11 = next(week for week in course.weeks if week.week == 11)

    assert "biochemistry-fatty-acid-oxidation" in {lesson.id for lesson in week11.lessons}
    assert "biochemistry-fatty-acid-oxidation-practice" in {
        assessment.id for assessment in week11.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-fatty-acid-oxidation")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-fatty-acid-objective-1",
        "biochemistry-fatty-acid-objective-2",
    }
    assert len(lesson.questions) == 7
    assert len(lesson.retrieval_cards) == 4
    assert "106 mol ATP equivalents per mol palmitate" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week11_ketone_body_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week11 = next(week for week in course.weeks if week.week == 11)

    assert "biochemistry-ketone-body-metabolism" in {lesson.id for lesson in week11.lessons}
    assert "biochemistry-ketone-body-metabolism-practice" in {
        assessment.id for assessment in week11.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-ketone-body-metabolism")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-ketone-objective-1",
        "biochemistry-ketone-objective-2",
        "biochemistry-ketone-objective-3",
        "biochemistry-ketone-objective-4",
    }
    assert len(lesson.questions) == 9
    assert len(lesson.retrieval_cards) == 6
    assert "Mature hepatocytes generally lack that route" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week2_urea_cycle_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week2 = next(week for week in course.weeks if week.week == 2)

    assert "biochemistry-urea-cycle" in {lesson.id for lesson in week2.lessons}
    assert "biochemistry-urea-cycle-practice" in {
        assessment.id for assessment in week2.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-urea-cycle")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-urea-cycle-objective-1",
        "biochemistry-urea-cycle-objective-2",
        "biochemistry-urea-cycle-objective-3",
    }
    assert len(lesson.questions) == 9
    assert len(lesson.retrieval_cards) == 5
    assert "3 ATP molecules but 4 high-energy phosphate equivalents" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


def test_biochemistry_week2_amino_acid_carbon_lesson_and_practice_are_delivered():
    content_root = Path(__file__).resolve().parents[2] / "content"
    repository = ContentRepository(content_root)
    course = repository.course("biochemistry")
    week2 = next(week for week in course.weeks if week.week == 2)

    assert "biochemistry-amino-acid-carbon-skeletons" in {
        lesson.id for lesson in week2.lessons
    }
    assert "biochemistry-amino-acid-carbon-skeletons-practice" in {
        assessment.id for assessment in week2.assessments
    }
    lesson = repository.lesson("biochemistry", "biochemistry-amino-acid-carbon-skeletons")
    assert set(lesson.learning_objective_ids) == {
        "biochemistry-amino-carbon-objective-1",
        "biochemistry-amino-carbon-objective-2",
        "biochemistry-amino-carbon-objective-3",
    }
    assert len(lesson.questions) == 9
    assert len(lesson.retrieval_cards) == 5
    assert "not a net glucose precursor in mammals" in lesson.markdown
    assert all("solution_spec" not in question.model_dump() for question in lesson.questions)


@pytest.mark.parametrize(("weeks", "error"), [
    ([{"week": 2, "title": "Later", "lesson_ids": [], "assessment_ids": []},
      {"week": 1, "title": "Earlier", "lesson_ids": [], "assessment_ids": []}],
     "strictly increasing"),
    ([{"week": 1, "title": "First", "lesson_ids": [], "assessment_ids": []},
      {"week": 1, "title": "Repeat", "lesson_ids": [], "assessment_ids": []}],
     "strictly increasing"),
    ([{"week": 1, "title": "Repeated lesson", "lesson_ids": ["lesson-one", "lesson-one"],
       "assessment_ids": []}], "cannot repeat"),
    ([{"week": 1, "title": "Repeated activity", "lesson_ids": [],
       "assessment_ids": ["practice-controls", "practice-controls"]}], "cannot repeat"),
    ([{"week": 0, "title": "Outside range", "lesson_ids": [], "assessment_ids": []}],
     "entry is invalid"),
    ([{"week": 53, "title": "Outside range", "lesson_ids": [], "assessment_ids": []}],
     "entry is invalid"),
])
def test_course_rejects_invalid_week_schedules(content_root, weeks, error):
    manifest_path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["duration"] = {"weeks": weeks}
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    with pytest.raises(ContentInvalid, match=error):
        ContentRepository(content_root).course("test-course")


def test_questions_use_manifest_bank_and_reject_unsafe_references(content_root):
    manifest_path = content_root / "courses" / "test-course" / "course.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    course_dir = manifest_path.parent
    bank = json.loads((course_dir / "question-banks" / "practice.json").read_text(encoding="utf-8"))
    custom_path = course_dir / "question-banks" / "custom-practice.json"
    custom_bank = {
        "course_id": "test-course",
        "questions": [
            {**bank["questions"][0], "id": "custom-practice-question"},
        ],
    }
    custom_path.write_text(json.dumps(custom_bank), encoding="utf-8")
    manifest["practice_question_bank"] = "question-banks/custom-practice.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    repository = ContentRepository(content_root)
    assert [item["id"] for item in repository.questions("test-course")] == [
        "custom-practice-question"
    ]

    manifest["practice_question_bank"] = "../../outside.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(ContentInvalid, match="Unsafe content reference"):
        repository.questions("test-course")

    manifest["practice_question_bank"] = 42
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(ContentInvalid, match="Unsafe practice question-bank reference"):
        repository.questions("test-course")


def test_links_the_application_cannot_serve_render_as_text(content_root):
    reading = content_root / "courses" / "test-course" / "modules" / "one.md"
    reading.write_text(
        "# Experiment\n\nSee the [source map](../source-map.json), [this lesson](one.md), [data](data.csv) "
        "and [a site](https://example.org/page.md).\n\nCode keeps `handlers[name](event)`, and ![a figure](plot.png) "
        "stays an image.\n",
        encoding="utf-8",
    )
    markdown = ContentRepository(content_root).lesson("test-course", "lesson-one").markdown
    assert (
        "See the source map, [this lesson](#/course/test-course/lesson/lesson-one), data "
        "and [a site](https://example.org/page.md)." in markdown
    )
    assert "`handlers[name](event)`" in markdown and "![a figure](plot.png)" in markdown


def test_package_archive_ignores_interpreter_caches(content_root):
    package = content_root / "courses" / "test-course"
    (package / "modules" / "__pycache__").mkdir()
    (package / "modules" / "__pycache__" / "one.cpython-312.pyc").write_bytes(b"\x00bytecode")
    (package / "modules" / "stale.pyc").write_bytes(b"\x00bytecode")

    files = ContentRepository(content_root).package_files("test-course")

    assert "modules/one.md" in files
    assert not [name for name in files if "__pycache__" in name or name.endswith(".pyc")]


def test_private_assessment_paths_are_confined_to_separate_read_root(tmp_path):
    public_root = tmp_path / "content"
    public_course = public_root / "courses" / "cell-biology"
    public_course.mkdir(parents=True)
    public_decoy = public_course / "answers.json"
    public_decoy.write_text('{"answer":"public decoy"}', encoding="utf-8")

    private_root = tmp_path / "private-assessments"
    private_file = private_root / "courses" / "cell-biology" / "assignments" / "homework-2.json"
    private_file.parent.mkdir(parents=True)
    private_file.write_text('{"answer":"private key"}', encoding="utf-8")

    repository = ContentRepository(public_root, private_root)
    assert repository.assessment_source_file(
        "cell-biology", "private://assignments/homework-2.json",
    ) == private_file.resolve()

    # A missing private mount cannot fall back to similarly named public content.
    without_private_root = ContentRepository(public_root)
    with pytest.raises(ContentMissing):
        without_private_root.assessment_source_file("cell-biology", "private://answers.json")

    for unsafe in (
        "private://../answers.json",
        "private:///absolute.json",
        "private://./answers.json",
        "private://assignments/../../answers.json",
        "private://assignments\\answers.json",
        "private://C:/outside.json",
    ):
        with pytest.raises(ContentInvalid):
            repository.assessment_source_file("cell-biology", unsafe)

    with pytest.raises(ValueError, match="separate roots"):
        ContentRepository(public_root, public_root / "private-assessments")


def test_private_assessment_symlink_cannot_escape_mount(tmp_path):
    public_root = tmp_path / "content"
    private_root = tmp_path / "private-assessments"
    course_root = private_root / "courses" / "cell-biology"
    course_root.mkdir(parents=True)
    outside = tmp_path / "outside.json"
    outside.write_text('{"answer":"outside"}', encoding="utf-8")
    link = course_root / "escape.json"
    try:
        link.symlink_to(outside)
    except (OSError, NotImplementedError):
        pytest.skip("Symlink creation is unavailable on this Windows host")

    repository = ContentRepository(public_root, private_root)
    with pytest.raises(ContentInvalid):
        repository.assessment_source_file("cell-biology", "private://escape.json")

    # The course directory itself must stay under the mount as well.
    second_private_root = tmp_path / "second-private-assessments"
    courses_root = second_private_root / "courses"
    courses_root.mkdir(parents=True)
    outside_course = tmp_path / "outside-course"
    outside_course.mkdir()
    (outside_course / "answer.json").write_text("{}", encoding="utf-8")
    try:
        (courses_root / "cell-biology").symlink_to(outside_course, target_is_directory=True)
    except (OSError, NotImplementedError):
        pytest.skip("Directory symlink creation is unavailable on this Windows host")

    repository = ContentRepository(public_root, second_private_root)
    with pytest.raises(ContentInvalid):
        repository.assessment_source_file("cell-biology", "private://answer.json")
