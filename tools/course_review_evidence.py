"""Validate a review-evidence register against one exact public course package.

This tool checks public artifact hashes and the structure of reviewer declarations.
It never reads protected answer sources, authenticates a person's identity or
qualifications, changes course maturity, or activates an assessment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import assessment_candidates  # noqa: E402
import course_package_digest  # noqa: E402

COURSE_LEVEL_GATES = (
    "course-scope-review",
    "course-grading-policy-review",
    "measured-workload",
    "institutional-equivalency",
)
COURSE_WIDE_CANDIDATE_GATES = {"measured-workload"}
OPERATOR_GATE = "operator-provisioning-and-release-policy"
REVIEW_STATUSES = {"in_progress", "revise", "signed"}
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def current_packet(root: Path, course_id: str) -> dict[str, Any]:
    """Build the current public inventory without opening private sources."""
    audit = assessment_candidates.audit(root)
    package = next((p for p in audit["packages"] if p["course"] == course_id), None)
    if package is None:
        raise ValueError(f"Unknown course ID: {course_id}")
    digest = course_package_digest.compute_digest(course_id, root)
    if digest["manifest_sha256"] != package["manifest_sha256"]:
        raise ValueError("Candidate audit and package digest read different manifests")
    return {
        "course_id": course_id,
        "course_version": digest["content_version"],
        "public_package_sha256": digest["package_sha256"],
        "manifest_sha256": digest["manifest_sha256"],
        "maturity": package["maturity"],
        "grading_mode": package["grading_mode"],
        "candidate_inventory": [
            {
                "candidate_id": candidate["id"],
                "candidate_version": candidate["version"],
                "metadata_sha256": candidate["metadata_sha256"],
                "public_artifact_sha256": candidate["artifact_sha256"],
                "required_gates": candidate["unresolved_activation_gates"],
            }
            for candidate in package["candidates"]
        ],
    }


def scaffold(root: Path, course_id: str) -> dict[str, Any]:
    """Create an empty, hash-pinned register; no review is implied."""
    packet = current_packet(root, course_id)
    return {
        "schema_version": "1.0",
        "evidence_scope": "review-record-index-only",
        **packet,
        "course_level_gate_ids": list(COURSE_LEVEL_GATES),
        "candidate_reviews": [],
        "course_reviews": [],
        "operator_release_decision": None,
        "notes": "Empty scaffold. No reviewer evidence, approval, or release decision is recorded.",
    }


def _require_text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def _check_sha(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SHA256.fullmatch(value):
        raise ValueError(f"{label} must be a lowercase SHA-256 digest")
    return value


def _check_public_artifact(root: Path, artifact: dict[str, Any]) -> str:
    if not isinstance(artifact, dict):
        raise ValueError("Evidence artifact references must be JSON objects")
    if artifact.get("scope") == "public_repo":
        relative = _require_text(artifact.get("path"), "Public artifact path")
        expected = _check_sha(artifact.get("sha256"), "Public artifact SHA-256")
        if "\\" in relative:
            raise ValueError("Public evidence paths must use forward slashes")
        path = (root / relative).resolve()
        evidence_root = (root / "docs/reviews").resolve()
        if not path.is_relative_to(evidence_root) or not path.is_file():
            raise ValueError(
                f"Public evidence artifact must be a file below docs/reviews: {relative}"
            )
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError(f"Public evidence artifact hash is stale: {relative}")
        if set(artifact) != {"scope", "path", "sha256"}:
            raise ValueError("Public evidence artifact contains unsupported fields")
        return "verified_public"
    if artifact.get("scope") == "external_attestation":
        _require_text(artifact.get("reference"), "External evidence reference")
        _require_text(artifact.get("description"), "External evidence description")
        _check_sha(artifact.get("sha256"), "External evidence SHA-256")
        if set(artifact) != {"scope", "reference", "description", "sha256"}:
            raise ValueError("External evidence artifact contains unsupported fields or paths")
        return "external_hash_unverified"
    raise ValueError("Evidence artifact scope must be public_repo or external_attestation")


def _validate_review(
    record: dict[str, Any],
    *,
    scope: str,
    allowed_gates: set[str],
    root: Path,
    candidate_ids: set[str] | None = None,
) -> tuple[str, str | None, str, str, str]:
    if not isinstance(record, dict):
        raise ValueError("Review records must be JSON objects")
    expected_scope = "candidate" if scope == "candidate" else "course"
    if record.get("scope") != expected_scope:
        raise ValueError(f"Review scope must be {expected_scope}")
    candidate_id = record.get("candidate_id")
    if scope == "candidate":
        if candidate_id not in (candidate_ids or set()):
            raise ValueError("Candidate review references an unknown candidate")
    elif candidate_id is not None:
        raise ValueError("Course-level review must not name a candidate")
    gate = _require_text(record.get("gate"), "Review gate")
    if gate not in allowed_gates:
        raise ValueError(f"Review gate is not allowed in this scope: {gate}")
    status = record.get("status")
    if status not in REVIEW_STATUSES:
        raise ValueError(f"Review status must be one of {sorted(REVIEW_STATUSES)}")

    allowed_fields = {
        "scope",
        "candidate_id",
        "gate",
        "status",
        "reviewer_id",
        "reviewer_qualifications",
        "independence_statement",
        "reviewed_at",
        "method",
        "evidence_id",
        "artifact_refs",
        "blocking_finding_ids",
    }
    if set(record) - allowed_fields:
        raise ValueError("Review record contains unsupported fields")

    artifact_refs = record.get("artifact_refs", [])
    if not isinstance(artifact_refs, list):
        raise ValueError("artifact_refs must be a list")
    artifact_state = "none"
    if artifact_refs:
        states = [_check_public_artifact(root, item) for item in artifact_refs]
        artifact_state = (
            "external_hash_unverified"
            if "external_hash_unverified" in states
            else "verified_public"
        )

    if status == "signed":
        for field in (
            "reviewer_id",
            "reviewer_qualifications",
            "independence_statement",
            "method",
            "evidence_id",
        ):
            _require_text(record.get(field), field)
        reviewed_at = _require_text(record.get("reviewed_at"), "reviewed_at")
        try:
            date.fromisoformat(reviewed_at)
        except ValueError as exc:
            raise ValueError("reviewed_at must use YYYY-MM-DD") from exc
        if not artifact_refs:
            raise ValueError("Signed review records need at least one evidence artifact reference")
        blockers = record.get("blocking_finding_ids", [])
        if not isinstance(blockers, list) or blockers:
            raise ValueError("Signed review records cannot retain blocking findings")
    elif record.get("blocking_finding_ids", []) and not isinstance(
        record.get("blocking_finding_ids"), list
    ):
        raise ValueError("blocking_finding_ids must be a list")
    return expected_scope, candidate_id, gate, status, artifact_state


def _validate_operator_decision(
    decision: Any, *, root: Path, package_sha256: str
) -> tuple[bool, str]:
    if decision is None:
        return False, "not_recorded"
    if not isinstance(decision, dict):
        raise ValueError("operator_release_decision must be an object or null")
    allowed = {
        "decision",
        "operator_id",
        "authority",
        "decided_at",
        "package_sha256",
        "evidence_id",
        "artifact_refs",
    }
    if set(decision) != allowed:
        raise ValueError("Operator decision has missing or unsupported fields")
    choice = decision.get("decision")
    if choice not in {"approve", "decline", "defer"}:
        raise ValueError("Operator decision must be approve, decline, or defer")
    for field in ("operator_id", "authority", "evidence_id"):
        _require_text(decision.get(field), field)
    decided_at = _require_text(decision.get("decided_at"), "decided_at")
    try:
        date.fromisoformat(decided_at)
    except ValueError as exc:
        raise ValueError("decided_at must use YYYY-MM-DD") from exc
    if decision.get("package_sha256") != package_sha256:
        raise ValueError("Operator decision is not bound to the current package digest")
    artifacts = decision.get("artifact_refs")
    if not isinstance(artifacts, list) or not artifacts:
        raise ValueError("Operator decisions need at least one evidence artifact reference")
    states = [_check_public_artifact(root, item) for item in artifacts]
    return choice == "approve", (
        "external_hash_unverified"
        if "external_hash_unverified" in states
        else "recorded_public_evidence"
    )


def audit_register(
    register: dict[str, Any], packet: dict[str, Any], root: Path
) -> dict[str, Any]:
    """Check that declarations are pinned and structurally supported; never approve."""
    if register.get("schema_version") != "1.0":
        raise ValueError("Unsupported review-evidence schema version")
    if register.get("evidence_scope") != "review-record-index-only":
        raise ValueError("Unexpected review-evidence scope")
    allowed_register_fields = {
        "schema_version",
        "evidence_scope",
        "course_id",
        "course_version",
        "public_package_sha256",
        "manifest_sha256",
        "maturity",
        "grading_mode",
        "candidate_inventory",
        "course_level_gate_ids",
        "candidate_reviews",
        "course_reviews",
        "operator_release_decision",
        "notes",
    }
    if set(register) != allowed_register_fields:
        raise ValueError("Review register has missing or unsupported fields")
    if register.get("notes") != (
        "Empty scaffold. No reviewer evidence, approval, or release decision is recorded."
    ):
        raise ValueError("Review-register notes must not be used to store free-form evidence")
    for field in (
        "course_id",
        "course_version",
        "public_package_sha256",
        "manifest_sha256",
    ):
        if register.get(field) != packet[field]:
            raise ValueError(f"Review evidence is stale for {field}")
    for field in ("maturity", "grading_mode"):
        if register.get(field) != packet[field]:
            raise ValueError(f"Review evidence is stale for {field}")
    if register.get("course_level_gate_ids") != list(COURSE_LEVEL_GATES):
        raise ValueError("Course-level review gate inventory changed")

    expected = {c["candidate_id"]: c for c in packet["candidate_inventory"]}
    supplied_list = register.get("candidate_inventory")
    if not isinstance(supplied_list, list):
        raise ValueError("candidate_inventory must be a list")
    supplied = {c.get("candidate_id"): c for c in supplied_list if isinstance(c, dict)}
    if len(supplied) != len(supplied_list) or set(supplied) != set(expected):
        raise ValueError("Candidate inventory does not match the current public audit")
    for candidate_id, current in expected.items():
        if supplied[candidate_id] != current:
            raise ValueError(f"Review evidence is stale for candidate {candidate_id}")

    candidate_ids = set(expected)
    allowed_candidate_gates = {
        candidate_id: set(candidate["required_gates"])
        - COURSE_WIDE_CANDIDATE_GATES
        - {OPERATOR_GATE}
        for candidate_id, candidate in expected.items()
    }
    reviews = register.get("candidate_reviews", [])
    course_reviews = register.get("course_reviews", [])
    if not isinstance(reviews, list) or not isinstance(course_reviews, list):
        raise ValueError("Review entries must be lists")

    candidate_status: dict[tuple[str, str], str] = {}
    external_hash_unverified = 0
    signed_records = 0
    for record in reviews:
        if not isinstance(record, dict):
            raise ValueError("Candidate review records must be objects")
        candidate_id = record.get("candidate_id")
        allowed = allowed_candidate_gates.get(candidate_id)
        if allowed is None:
            raise ValueError("Candidate review references an unknown candidate")
        scope, candidate_id, gate, status, artifact_state = _validate_review(
            record,
            scope="candidate",
            allowed_gates=allowed,
            root=root,
            candidate_ids=candidate_ids,
        )
        key = (candidate_id, gate)
        if key in candidate_status:
            raise ValueError(f"Duplicate review record for {candidate_id}/{gate}")
        candidate_status[key] = status
        signed_records += status == "signed"
        external_hash_unverified += artifact_state == "external_hash_unverified"

    course_status: dict[str, str] = {}
    for record in course_reviews:
        scope, _, gate, status, artifact_state = _validate_review(
            record,
            scope="course",
            allowed_gates=set(COURSE_LEVEL_GATES),
            root=root,
        )
        if gate in course_status:
            raise ValueError(f"Duplicate course-level review record for {gate}")
        course_status[gate] = status
        signed_records += status == "signed"
        external_hash_unverified += artifact_state == "external_hash_unverified"

    operator_approved, operator_artifact_state = _validate_operator_decision(
        register.get("operator_release_decision"),
        root=root,
        package_sha256=packet["public_package_sha256"],
    )
    external_hash_unverified += operator_artifact_state == "external_hash_unverified"
    operator_recorded = register.get("operator_release_decision") is not None

    candidate_results = []
    for candidate_id, candidate in expected.items():
        missing = []
        for gate in candidate["required_gates"]:
            if gate == OPERATOR_GATE:
                complete = operator_approved
            elif gate in COURSE_WIDE_CANDIDATE_GATES:
                complete = course_status.get(gate) == "signed"
            else:
                complete = candidate_status.get((candidate_id, gate)) == "signed"
            if not complete:
                missing.append(gate)
        candidate_results.append(
            {
                "candidate_id": candidate_id,
                "candidate_version": candidate["candidate_version"],
                "required_gate_count": len(candidate["required_gates"]),
                "unresolved_gates": missing,
            }
        )

    unresolved_course_gates = [
        gate for gate in COURSE_LEVEL_GATES if course_status.get(gate) != "signed"
    ]
    unresolved_candidate_gate_count = sum(
        len(candidate["unresolved_gates"]) for candidate in candidate_results
    )
    all_review_records_complete = (
        unresolved_candidate_gate_count == 0 and not unresolved_course_gates
    )
    return {
        "course_id": packet["course_id"],
        "course_version": packet["course_version"],
        "public_package_sha256": packet["public_package_sha256"],
        "maturity": packet["maturity"],
        "grading_mode": packet["grading_mode"],
        "candidate_count": len(candidate_results),
        "candidate_results": candidate_results,
        "unresolved_candidate_gate_count": unresolved_candidate_gate_count,
        "unresolved_course_gates": unresolved_course_gates,
        "signed_review_records_as_declared": signed_records,
        "external_artifact_hashes_not_verified": external_hash_unverified,
        "operator_decision_recorded": operator_recorded,
        "operator_approval_as_declared": operator_approved,
        "all_declared_review_gates_complete": all_review_records_complete,
        "reviewer_identity_or_qualifications_independently_verified": False,
        "private_answer_sources_read": False,
        "release_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--course-id", required=True)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--scaffold", type=Path)
    action.add_argument("--check", type=Path)
    parser.add_argument(
        "--require-all-gates",
        action="store_true",
        help="Exit nonzero unless every declared review and operator gate is recorded complete.",
    )
    args = parser.parse_args()
    path = args.scaffold or args.check
    if not path.is_absolute():
        path = args.root / path
    try:
        if args.scaffold:
            if path.exists():
                raise ValueError(f"Refusing to overwrite review evidence: {path}")
            register = scaffold(args.root, args.course_id)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(register, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        else:
            register = json.loads(path.read_text(encoding="utf-8"))
        packet = current_packet(args.root, args.course_id)
        result = audit_register(register, packet, args.root)
        print(json.dumps(result, indent=2))
        if args.require_all_gates and not result["all_declared_review_gates_complete"]:
            return 2
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, f"Review-evidence check failed: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
