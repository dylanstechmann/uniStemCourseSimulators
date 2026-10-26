"""Course package files must hold LF line endings in the working tree as well as in git.

`.gitattributes` normalizes every text file to LF on commit, so CI always checks out LF bytes.
A working copy on a Windows mount can still hold CRLF, and the package digest in each review
snapshot hashes the files as they sit on disk. A snapshot calculated over CRLF bytes therefore
records a hash that CI cannot reproduce, which is a stale-snapshot failure with no visible edit.
This check fails in the working tree instead, where the cause is still obvious.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSES = ROOT / "content/courses"
REGISTRY = ROOT / "content/sources/registry.json"


def package_files():
    """Every file a course package archives, plus the shared source registry."""
    for manifest_path in sorted(COURSES.glob("*/course.json")):
        course = manifest_path.parent
        yield manifest_path
        for pattern in ("modules/*.md", "assignments/*", "labs/*", "question-banks/*.json",
                        "rubrics/*.json", "assessment-specs/*.md"):
            yield from sorted(course.glob(pattern))
        for extra in ("syllabus.md", "source-map.json", "scope-crosswalk.md"):
            if (course / extra).is_file():
                yield course / extra
    yield REGISTRY


def test_no_course_package_file_carries_carriage_returns():
    offenders = sorted(
        str(path.relative_to(ROOT))
        for path in package_files()
        if b"\r" in path.read_bytes()
    )
    assert offenders == [], (
        "These package files hold CRLF line endings in the working tree. Convert them to LF and "
        "recalculate any review snapshot digest that was taken from them: " + ", ".join(offenders)
    )


def test_every_inspected_course_package_is_covered():
    """A renamed content directory must not silently empty the check above."""
    courses = {path.parent.name for path in COURSES.glob("*/course.json")}
    inspected = {
        path.relative_to(COURSES).parts[0]
        for path in package_files()
        if REGISTRY != path and COURSES in path.parents
    }
    assert inspected == courses
    assert json.loads(REGISTRY.read_text(encoding="utf-8"))["sources"], "source registry is empty"
