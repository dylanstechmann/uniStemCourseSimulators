"""Read authoring packages on the server, publish only explicit learner DTOs.

The legacy practice specifications are intentionally open authoring resources.
They are not restricted production examinations. They still never ship as a
frontend static asset or through a learner content response.
"""

import hashlib
import json
import posixpath
import re
from collections.abc import Callable
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

from pydantic import ValidationError

from .schemas import (
    CourseSummary,
    CourseWeek,
    LessonSummary,
    ModuleSummary,
    Objective,
    Prerequisites,
    PublicCaseStudy,
    PublicCourse,
    PublicCurriculum,
    PublicLesson,
    PublicQuestion,
    PublicRetrievalCard,
)


class ContentMissing(LookupError):
    pass


class ContentInvalid(ValueError):
    pass


class ContentRepository:
    def __init__(
        self,
        root: Path,
        private_assessments_root: Path | None = None,
        *,
        package_snapshot: tuple[str, dict[str, bytes]] | None = None,
        archived_version: str | None = None,
    ):
        self.root = root.resolve()
        self.package_snapshot = package_snapshot
        self.archived_version = archived_version
        self.private_assessments_root = (
            private_assessments_root.resolve() if private_assessments_root else None
        )
        if package_snapshot is not None and self.private_assessments_root is not None:
            raise ValueError("Archived public content cannot access private assessment sources")
        if self.private_assessments_root and (
            self.private_assessments_root == self.root
            or self.private_assessments_root.is_relative_to(self.root)
            or self.root.is_relative_to(self.private_assessments_root)
        ):
            raise ValueError("Private assessments and public course content must use separate roots")

    def _file(self, course_id: str, relative: str) -> Path:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", course_id):
            raise ContentMissing("Course not found")
        directory = (self.root / "courses" / course_id).resolve()
        course_root = (self.root / "courses").resolve()
        if not directory.is_relative_to(course_root):
            raise ContentInvalid("Unsafe content directory")
        candidate = (directory / relative).resolve()
        if not candidate.is_relative_to(directory):
            raise ContentInvalid("Unsafe content reference")
        if not candidate.is_file():
            raise ContentMissing("Content not found")
        return candidate

    def manifest(self, course_id: str) -> dict:
        item = json.loads(self._read(course_id, "course.json"))
        if item.get("id") != course_id:
            raise ContentInvalid("Manifest ID mismatch")
        return item

    def package_files(self, course_id: str) -> dict[str, bytes]:
        """Read every regular file in one public package without following links."""
        directory = self._file(course_id, "course.json").parent
        files: dict[str, bytes] = {}
        total_bytes = 0
        for path in sorted(directory.rglob("*")):
            if path.is_symlink():
                raise ContentInvalid("Course packages cannot contain symbolic links")
            if not path.is_file():
                continue
            resolved = path.resolve()
            if not resolved.is_relative_to(directory):
                raise ContentInvalid("Unsafe content package path")
            relative = path.relative_to(directory).as_posix()
            parts = relative.split("/")
            if (
                not relative
                or "\\" in relative
                or ":" in relative
                or any(part in {"", ".", ".."} for part in parts)
            ):
                raise ContentInvalid("Unsafe content package path")
            payload = path.read_bytes()
            total_bytes += len(payload)
            if len(files) >= 10_000 or total_bytes > 64 * 1024 * 1024:
                raise ContentInvalid("Course package exceeds the archive limit")
            files[relative] = payload
        if "course.json" not in files:
            raise ContentMissing("Course manifest not found")
        return files

    def _read(self, course_id: str, relative: str) -> str:
        if self.package_snapshot is not None:
            snapshot_course_id, files = self.package_snapshot
            if (
                course_id != snapshot_course_id
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", course_id)
                or not isinstance(relative, str)
                or not relative
                or relative.startswith("/")
                or "\\" in relative
                or ":" in relative
                or any(part in {"", ".", ".."} for part in relative.split("/"))
            ):
                raise ContentInvalid("Unsafe archived content reference")
            try:
                return files[relative].decode("utf-8")
            except KeyError as exc:
                raise ContentMissing("Archived content not found") from exc
            except UnicodeDecodeError as exc:
                raise ContentInvalid("Archived text content is not UTF-8") from exc
        return self._file(course_id, relative).read_text(encoding="utf-8")

    def assessment_source_file(self, course_id: str, relative: str) -> Path:
        """Resolve public package sources or keys from a separate private mount.

        A `private://` source maps below
        `<private-root>/courses/<course-id>/...`; it can never fall back to the
        public content directory. Missing private configuration or files fail
        closed when the assessment plan is created or checked.
        """
        if relative.startswith("private://"):
            if self.private_assessments_root is None:
                raise ContentMissing("Private assessment content is unavailable")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", course_id):
                raise ContentMissing("Course not found")
            private_relative = relative.removeprefix("private://")
            parts = private_relative.split("/")
            if (
                not private_relative
                or private_relative.startswith("/")
                or "\\" in private_relative
                or ":" in private_relative
                or any(part in {"", ".", ".."} for part in parts)
            ):
                raise ContentInvalid("Unsafe private assessment reference")
            courses_root = (self.private_assessments_root / "courses").resolve()
            if not courses_root.is_relative_to(self.private_assessments_root):
                raise ContentInvalid("Unsafe private assessment reference")
            directory = (courses_root / course_id).resolve()
            if not directory.is_relative_to(courses_root):
                raise ContentInvalid("Unsafe private assessment reference")
            candidate = (directory / Path(*parts)).resolve()
            if not candidate.is_relative_to(directory):
                raise ContentInvalid("Unsafe private assessment reference")
            if not candidate.is_file():
                raise ContentMissing("Private assessment content not found")
            return candidate
        return self._file(course_id, relative)

    def _summary(self, manifest: dict) -> CourseSummary:
        return CourseSummary(
            **{name: manifest[name] for name in (
                "id", "title", "description", "domain", "level", "maturity", "version", "limitations"
            )},
            lesson_count=sum(len(module["lessons"]) for module in manifest["modules"]),
        )

    def catalog(self) -> list[CourseSummary]:
        items = []
        for path in sorted((self.root / "courses").glob("*/course.json")):
            items.append(self._summary(self.manifest(path.parent.name)))
        return items

    def curriculum(self) -> PublicCurriculum:
        """Return a prerequisite/pathway map with explicit course maturity."""
        map_path = self.root / "curriculum-map.json"
        if not map_path.is_file():
            raise ContentInvalid("Curriculum map is unavailable")
        source = json.loads(map_path.read_text(encoding="utf-8"))
        nodes = []
        for path in sorted((self.root / "courses").glob("*/course.json")):
            manifest = self.manifest(path.parent.name)
            nodes.append({
                "id": manifest["id"], "title": manifest["title"],
                "domain": manifest["domain"], "level": manifest["level"],
                "maturity": manifest["maturity"], "description": manifest["description"],
                "prerequisites": manifest["prerequisites"], "package_id": manifest["id"],
                "related_package_ids": [], "relation_note": None,
            })
        for item in source["catalog_only"]:
            nodes.append({
                **item, "package_id": None,
            })
        return PublicCurriculum(
            schema_version=source["schema_version"], description=source["description"],
            nodes=nodes, pathways=source["pathways"], alignment_maps=source["alignment_maps"],
        )

    def sources(self) -> list[dict]:
        registry = self.root / "sources" / "registry.json"
        if not registry.is_file():
            return []
        data = json.loads(registry.read_text(encoding="utf-8"))
        entries = data if isinstance(data, list) else data.get("sources", [])
        return [{key: entry.get(key) for key in ("id", "title", "url", "institution", "license")}
                for entry in entries]

    def course(self, course_id: str) -> PublicCourse:
        manifest = self.manifest(course_id)
        modules = [ModuleSummary(
            id=module["id"], title=module["title"], source_ids=module.get("source_ids", []),
            lessons=[LessonSummary(id=lesson["id"], title=lesson["title"],
                                   learning_objective_ids=lesson.get("objectives", []))
                     for lesson in module["lessons"]],
        ) for module in manifest["modules"]]
        lessons_by_id = {
            lesson["id"]: lesson
            for module in manifest["modules"]
            for lesson in module["lessons"]
        }
        assessments_by_id = {
            assessment["id"]: assessment
            for assessment in manifest.get("assessments", [])
        }
        duration = manifest.get("duration") or {}
        if not isinstance(duration, dict):
            raise ContentInvalid("Course duration must be an object")
        authored_weeks = duration.get("weeks", [])
        if not isinstance(authored_weeks, list):
            raise ContentInvalid("Course week schedule must be a list")
        weeks = []
        previous_week = 0
        for item in authored_weeks:
            if not isinstance(item, dict):
                raise ContentInvalid("Course week schedule entry is invalid")
            week_number = item.get("week")
            title = item.get("title")
            lesson_ids = item.get("lesson_ids", [])
            assessment_ids = item.get("assessment_ids", [])
            if (
                not isinstance(week_number, int)
                or isinstance(week_number, bool)
                or not 1 <= week_number <= 52
                or not isinstance(title, str)
                or not title.strip()
            ):
                raise ContentInvalid("Course week schedule entry is invalid")
            if week_number <= previous_week:
                raise ContentInvalid("Course week numbers must be strictly increasing")
            if not isinstance(lesson_ids, list) or not isinstance(assessment_ids, list):
                raise ContentInvalid("Course week content IDs must be lists")
            if any(not isinstance(lesson_id, str) for lesson_id in lesson_ids) or any(
                not isinstance(assessment_id, str) for assessment_id in assessment_ids
            ):
                raise ContentInvalid("Course week content IDs must be strings")
            if len(set(lesson_ids)) != len(lesson_ids) or len(set(assessment_ids)) != len(assessment_ids):
                raise ContentInvalid("Course week schedule cannot repeat a lesson or activity")
            if any(lesson_id not in lessons_by_id for lesson_id in lesson_ids) or any(
                assessment_id not in assessments_by_id for assessment_id in assessment_ids
            ):
                raise ContentInvalid("Course week schedule references unknown content")
            previous_week = week_number
            weeks.append(CourseWeek(
                week=week_number, title=title,
                lessons=[{"id": lesson_id, "title": lessons_by_id[lesson_id]["title"]}
                         for lesson_id in lesson_ids],
                assessments=[{
                    "id": assessment_id,
                    "title": assessments_by_id[assessment_id].get("title") or assessment_id,
                    "type": assessments_by_id[assessment_id]["type"],
                    "mode": assessments_by_id[assessment_id]["mode"],
                } for assessment_id in assessment_ids],
            ))
        return PublicCourse(
            **self._summary(manifest).model_dump(),
            prerequisites=Prerequisites.model_validate(manifest["prerequisites"]),
            outcomes=[Objective.model_validate(item) for item in manifest["outcomes"]],
            lesson_objectives=[Objective.model_validate(item) for item in manifest.get("lesson_objectives", [])],
            modules=modules, weeks=weeks, case_studies=self.case_studies(course_id),
            syllabus_markdown=self._linked_markdown(
                course_id, manifest["syllabus"], self._read(course_id, manifest["syllabus"])
            ),
            license=manifest["license"], review_status=manifest["review"]["status"],
        )

    def case_studies(self, course_id: str) -> list[PublicCaseStudy]:
        """Expose only authored, zero-point self-assessment prompts and checklists."""
        manifest = self.manifest(course_id)
        source_path = manifest.get("case_rubrics")
        if not source_path:
            return []
        try:
            source = json.loads(self._read(course_id, source_path))
            if source["course_id"] != course_id or not isinstance(source["cases"], list):
                raise ContentInvalid("Invalid case-studio package")
            cases = []
            for item in source["cases"]:
                if item["mode"] != "self-assessment" or any(
                    criterion["points"] != 0 for criterion in item["rubric"]
                ):
                    raise ContentInvalid("Case studio supports ungraded self-assessment only")
                visible = {
                    "id": item["id"], "prompt": item["prompt"], "mode": item["mode"],
                    "objective_ids": item.get("objective_ids", []),
                    "criteria": [{"id": criterion["id"], "criterion": criterion["criterion"]}
                                 for criterion in item["rubric"]],
                    "limitations": item.get("limitations", []),
                }
                digest = hashlib.sha256(json.dumps(
                    {"course_id": course_id, **visible}, sort_keys=True, separators=(",", ":"),
                    ensure_ascii=False,
                ).encode()).hexdigest()
                case = PublicCaseStudy.model_validate({**visible, "case_sha256": digest})
                if len({criterion.id for criterion in case.criteria}) != len(case.criteria):
                    raise ContentInvalid("Duplicate case criterion ID")
                cases.append(case)
            if len({case.id for case in cases}) != len(cases):
                raise ContentInvalid("Duplicate case ID")
            return cases
        except (KeyError, TypeError, ValueError, ValidationError) as exc:
            raise ContentInvalid("Invalid case-studio package") from exc

    def lesson_record(self, course_id: str, lesson_id: str) -> tuple[dict, dict]:
        for module in self.manifest(course_id)["modules"]:
            for lesson in module["lessons"]:
                if lesson["id"] == lesson_id:
                    return module, lesson
        raise ContentMissing("Lesson not found")

    def _linked_markdown(self, course_id: str, source_path: str, markdown: str) -> str:
        manifest = self.manifest(course_id)
        learner_resources = self._learner_resource_paths(course_id, manifest)
        reading_to_id = {
            posixpath.normpath(item["reading"]): item["id"]
            for module in manifest["modules"]
            for item in module["lessons"]
        }
        route_prefix = f"#/course/{quote(course_id, safe='')}"
        if self.archived_version:
            route_prefix += f"/version/{quote(self.archived_version, safe='')}"

        def rewrite_link(match: re.Match[str]) -> str:
            raw_destination = match.group(1)
            destination_match = re.match(r"^(?:<([^>]*)>|([^\s]+))(.*)$", raw_destination)
            if destination_match is None:
                return match.group(0)
            destination = destination_match.group(1) or destination_match.group(2)
            suffix = destination_match.group(3)
            parsed = urlsplit(destination)
            path_extension = posixpath.splitext(parsed.path.lower())[1]
            if (
                parsed.scheme
                or parsed.netloc
                or parsed.path.startswith("/")
                or path_extension not in {".md", ".csv"}
                or parsed.query
                or parsed.fragment
            ):
                return match.group(0)
            target_path = posixpath.normpath(
                posixpath.join(posixpath.dirname(source_path), unquote(parsed.path))
            )
            target_id = reading_to_id.get(target_path)
            if target_id is not None:
                target = f"{route_prefix}/lesson/{quote(target_id, safe='')}"
                return f"]({target}{suffix})"
            if target_path not in learner_resources:
                return match.group(0)
            resource_prefix = f"/api/v1/courses/{quote(course_id, safe='')}"
            if self.archived_version:
                resource_prefix += (
                    f"/versions/{quote(self.archived_version, safe='')}"
                )
            target = f"{resource_prefix}/resources/{quote(target_path, safe='/')}"
            return f"]({target}{suffix})"

        return re.sub(r"(?<!!)\]\(([^)]+)\)", rewrite_link, markdown)

    def _learner_resource_paths(
        self, course_id: str, manifest: dict | None = None
    ) -> set[str]:
        manifest = manifest or self.manifest(course_id)
        references = manifest.get("learner_resources", [])
        if (
            not isinstance(references, list)
            or any(not isinstance(reference, str) for reference in references)
            or len(set(references)) != len(references)
        ):
            raise ContentInvalid("Learner resource references must be a unique list")
        resources: set[str] = set()
        for relative in references:
            if (
                not isinstance(relative, str)
                or not relative
                or relative.startswith("/")
                or "\\" in relative
                or ":" in relative
                or not relative.lower().endswith(".csv")
                or any(part in {"", ".", ".."} for part in relative.split("/"))
            ):
                raise ContentInvalid("Unsafe learner resource reference")
            if self.package_snapshot is not None:
                snapshot_course_id, files = self.package_snapshot
                if course_id != snapshot_course_id or relative not in files:
                    raise ContentMissing("Archived learner resource not found")
            else:
                self._file(course_id, relative)
            resources.add(relative)
        return resources

    def learner_resource(self, course_id: str, relative: str) -> bytes:
        """Return CSV files explicitly exposed as learner resources."""
        manifest = self.manifest(course_id)
        if (
            not relative.lower().endswith(".csv")
            or relative not in self._learner_resource_paths(course_id, manifest)
        ):
            raise ContentMissing("Learner resource not found")
        if self.package_snapshot is not None:
            snapshot_course_id, files = self.package_snapshot
            if course_id != snapshot_course_id:
                raise ContentMissing("Learner resource not found")
            try:
                return files[relative]
            except KeyError as exc:
                raise ContentMissing("Learner resource not found") from exc
        return self._file(course_id, relative).read_bytes()

    def _lesson_markdown(self, course_id: str, lesson: dict) -> str:
        source_path = lesson["reading"]
        return self._linked_markdown(
            course_id, source_path, self._read(course_id, source_path)
        )

    def questions(self, course_id: str) -> list[dict]:
        manifest = self.manifest(course_id)
        reference = manifest.get("practice_question_bank", "question-banks/practice.json")
        if not isinstance(reference, str) or not reference or "\\" in reference:
            raise ContentInvalid("Unsafe practice question-bank reference")
        package = json.loads(self._read(course_id, reference))
        if package.get("course_id") != course_id:
            raise ContentInvalid("Question-bank course mismatch")
        # Fail closed: the unrestricted retry route only serves the explicitly
        # public seed practice bank. Restricted/untagged records are not gradeable
        # or readable through this repository interface.
        return [question for question in package["questions"]
                if question.get("visibility") == "public-practice-authoring"]

    def question(self, course_id: str, question_id: str) -> dict:
        for item in self.questions(course_id):
            if item["id"] == question_id:
                return item
        raise ContentMissing("Question not found")

    def _cards_by_id(self, course_id: str, manifest: dict) -> dict[str, dict]:
        if not manifest.get("retrieval_cards"):
            return {}
        package = json.loads(self._read(course_id, manifest["retrieval_cards"]))
        if package.get("course_id") != course_id:
            raise ContentInvalid("Retrieval-card course mismatch")
        cards_by_id = {}
        for card in package["cards"]:
            if card["id"] in cards_by_id:
                raise ContentInvalid("Retrieval-card IDs must be unique")
            cards_by_id[card["id"]] = card
        return cards_by_id

    @staticmethod
    def _assigned_card(cards_by_id: dict[str, dict], card_id: str, lesson_id: str) -> dict:
        card = cards_by_id.get(card_id)
        if card is None or card.get("lesson_id") != lesson_id:
            raise ContentInvalid("Lesson retrieval-card reference is invalid")
        return card

    def retrieval_cards(self, course_id: str, lesson_id: str) -> list[PublicRetrievalCard]:
        """Publish only the learner-facing fields for cards assigned to this lesson."""
        manifest = self.manifest(course_id)
        _, lesson = self.lesson_record(course_id, lesson_id)
        cards_by_id = self._cards_by_id(course_id, manifest)
        selected = []
        for card_id in lesson.get("card_ids", []):
            card = self._assigned_card(cards_by_id, card_id, lesson_id)
            selected.append(PublicRetrievalCard(
                id=card["id"], front=card["front"], back=card["back"],
                learning_objective_ids=card.get("objective_ids", []),
            ))
        return selected

    def course_retrieval_cards(self, course_id: str) -> list[dict]:
        """Every lesson-assigned card in syllabus order, with learner-visible fields only.

        Cards that no lesson assigns are not published, matching the lesson DTO boundary.
        """
        manifest = self.manifest(course_id)
        cards_by_id = self._cards_by_id(course_id, manifest)
        published = []
        seen = set()
        for module in manifest["modules"]:
            for lesson in module["lessons"]:
                for card_id in lesson.get("card_ids", []):
                    card = self._assigned_card(cards_by_id, card_id, lesson["id"])
                    if card_id in seen:
                        raise ContentInvalid("A retrieval card is assigned to more than one lesson")
                    seen.add(card_id)
                    published.append({
                        "id": card["id"], "lesson_id": lesson["id"], "lesson_title": lesson["title"],
                        "front": card["front"], "back": card["back"],
                        "learning_objective_ids": card.get("objective_ids", []),
                    })
        return published

    def public_question(
        self, question: dict, variant_id: str | None = None, variant_token: str | None = None
    ) -> PublicQuestion:
        """Build a whitelisted learner DTO; never return the authored grader spec."""
        return PublicQuestion(
            id=question["id"], type=question["type"], prompt=question["prompt"],
            options=question.get("options", []), unit=question.get("solution_spec", {}).get("unit"),
            significant_figures=question.get("solution_spec", {}).get("significant_figures"),
            points=question.get("points", 1), learning_objective_ids=question.get("objective_ids", []),
            selection="multiple" if question["type"] == "multiple_select" else "single",
            partial_credit_policy=(question.get("solution_spec", {}).get("partial_credit")
                                   if question["type"] == "multiple_select" else None),
            response_fields=[
                {
                    "id": field["id"], "type": field["type"], "prompt": field["prompt"],
                    "options": field.get("options", []), "unit": field.get("unit"),
                    "points": field["points"],
                }
                for field in question.get("response_fields", [])
            ],
            graph_spec=(
                {
                    "x_axis": {
                        "label": question["graph_spec"]["x_axis"]["label"],
                        "minimum": question["graph_spec"]["x_axis"]["minimum"],
                        "maximum": question["graph_spec"]["x_axis"]["maximum"],
                    },
                    "y_axis": {
                        "label": question["graph_spec"]["y_axis"]["label"],
                        "minimum": question["graph_spec"]["y_axis"]["minimum"],
                        "maximum": question["graph_spec"]["y_axis"]["maximum"],
                    },
                    "points": [
                        {"id": point["id"], "label": point["label"]}
                        for point in question["graph_spec"]["points"]
                    ],
                    "observations": [
                        {
                            "id": observation["id"],
                            "x": observation["x"],
                            "values": observation["values"],
                        }
                        for observation in question["graph_spec"]["observations"]
                    ],
                }
                if question["type"] == "graph" else None
            ),
            accepted_media_types=(
                question.get("solution_spec", {}).get("accepted_media_types", [])
                if question["type"] == "file_upload" else []
            ),
            max_upload_bytes=(
                question.get("solution_spec", {}).get("max_bytes")
                if question["type"] == "file_upload" else None
            ),
            variant_id=variant_id, variant_token=variant_token,
        )

    def lesson(
        self, course_id: str, lesson_id: str,
        public_question_factory: Callable[[dict], PublicQuestion] | None = None,
    ) -> PublicLesson:
        module, lesson = self.lesson_record(course_id, lesson_id)
        available = {question["id"]: question for question in self.questions(course_id)}
        questions = [available[question_id] for question_id in lesson.get("question_ids", [])
                     if question_id in available]
        return PublicLesson(
            id=lesson["id"], title=lesson["title"], markdown=self._lesson_markdown(course_id, lesson),
            learning_objective_ids=lesson.get("objectives", []), worked_example=lesson.get("worked_example"),
            source_ids=module.get("source_ids", []),
            retrieval_cards=self.retrieval_cards(course_id, lesson["id"]),
            questions=[public_question_factory(question) if public_question_factory else
                       self.public_question(question, "base" if question.get("randomization") else None)
                       for question in questions],
        )
