"""Print the deterministic public-course archive digest used by the API."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from courselab.content import ContentRepository  # noqa: E402
from courselab.course_archives import CourseContentArchiveService  # noqa: E402


def compute_digest(
    course_id: str, root: Path = ROOT
) -> dict[str, str | int]:
    """Return archive and manifest hashes for one current public package."""
    repository = ContentRepository(root / "content")
    files = repository.package_files(course_id)
    archive, _ = CourseContentArchiveService.build_archive(files)
    manifest_sha256 = hashlib.sha256(files["course.json"]).hexdigest()
    manifest = json.loads(files["course.json"].decode("utf-8"))
    return {
        "course_id": course_id,
        "content_version": manifest["version"],
        "package_sha256": hashlib.sha256(archive).hexdigest(),
        "manifest_sha256": manifest_sha256,
        "file_count": len(files),
        "archive_bytes": len(archive),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--course-id", required=True, help="Course package slug")
    args = parser.parse_args()
    try:
        print(json.dumps(compute_digest(args.course_id), indent=2))
    except (KeyError, OSError, ValueError) as exc:
        parser.exit(1, f"Could not calculate public package digest: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
