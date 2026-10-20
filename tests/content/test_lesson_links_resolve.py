"""Every link in a delivered lesson must open a lesson, a served learner resource or an external page."""

from __future__ import annotations

import json
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
COURSES = ROOT / "content/courses"
RESOLVED = ("#/course/", "/api/v1/courses/", "https://", "http://", "mailto:")
SOURCE_LINK = re.compile(r"(?<![!\\])\[([^\[\]\n]*)\]\(([^()\s]+)\)")
CELL_BIOLOGY_PROVENANCE = {
    (lesson_id, target)
    for lesson_id in ("cell-biology-1", "cell-biology-2", "cell-biology-5", "cell-biology-6", "cell-biology-7",
                      "cell-biology-8")
    for target in ("../source-map.json", "../../../sources/registry.json")
}

# Links to repository files that the application does not serve. They work when the Markdown is read on GitHub,
# and the app shows their text without a link. The Cell Biology provenance notes sit in readings that inactive
# assessment candidates pin by digest, so they cannot be edited without re-freezing those candidates.
REPOSITORY_ONLY = {("cell-biology", lesson_id, target) for lesson_id, target in CELL_BIOLOGY_PROVENANCE} | {
    ("cell-biology", "cell-biology-3", "03-enzymes-and-cellular-energetics.md"),
    ("cell-biology", "cell-biology-4", "04-gene-expression-and-experimental-logic.md"),
}

# Learner-facing gaps queued for each course's own batch: the dataset or lesson exists but the app cannot open it
# from this link. Remove an entry when its link is fixed; the exact-set comparison fails until the list matches.
QUEUED = {
    ("robotics", "robotics-lab-01", "near-extension-reports.csv"),
}


def manifests():
    for course_dir in sorted(path for path in COURSES.iterdir() if (path / "course.json").is_file()):
        yield course_dir, json.loads((course_dir / "course.json").read_text(encoding="utf-8"))


def repository():
    sys.path.insert(0, str(ROOT / "backend"))
    from courselab.content import ContentRepository

    return ContentRepository(ROOT / "content")


def test_source_links_open_a_lesson_or_learner_resource_unless_listed():
    # A link into another course, such as ../../linear-algebra/modules/02-x.md, opens that course's lesson.
    other_course_readings = {
        f"../{manifest['id']}/{posixpath.normpath(lesson['reading'])}"
        for _, manifest in manifests() for module in manifest["modules"] for lesson in module["lessons"]
    }
    unserved = set()
    for course_dir, manifest in manifests():
        lessons = {lesson["reading"]: lesson["id"] for module in manifest["modules"] for lesson in module["lessons"]}
        resources = set(manifest.get("learner_resources", []))
        for reading, lesson_id in lessons.items():
            for _, destination in SOURCE_LINK.findall((course_dir / reading).read_text(encoding="utf-8")):
                parsed = urlsplit(destination)
                if parsed.scheme or parsed.netloc or parsed.path.startswith("/") or not parsed.path:
                    continue
                target = posixpath.normpath(posixpath.join(posixpath.dirname(reading), unquote(parsed.path)))
                if target not in lessons and target not in resources and target not in other_course_readings:
                    unserved.add((manifest["id"], lesson_id, destination))
    assert unserved == REPOSITORY_ONLY | QUEUED


def test_delivered_lessons_contain_no_link_the_application_cannot_open():
    content = repository()
    dead = set()
    for _, manifest in manifests():
        for lesson_id in (lesson["id"] for module in manifest["modules"] for lesson in module["lessons"]):
            markdown = content.lesson(manifest["id"], lesson_id).markdown
            for destination in re.findall(r"(?<!!)\]\(<?([^)\s>]+)", markdown):
                if not destination.startswith(RESOLVED):
                    dead.add((manifest["id"], lesson_id, destination))
    assert dead == set()


def test_linked_learner_resources_are_served_byte_for_byte():
    content = repository()
    for course_dir, manifest in manifests():
        for path in manifest.get("learner_resources", []):
            assert content.learner_resource(manifest["id"], path) == (course_dir / path).read_bytes(), path
