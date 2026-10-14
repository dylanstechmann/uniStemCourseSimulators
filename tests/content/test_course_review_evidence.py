"""Review-evidence indexes bind declarations to current public artifacts only."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "course_review_evidence", ROOT / "tools/course_review_evidence.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
REGISTER_PATH = ROOT / "docs/reviews/cell-biology-review-evidence.json"


def _current_register():
    register = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
    packet = MODULE.current_packet(ROOT, "cell-biology")
    return register, packet


def _signed_candidate_review(candidate_id, gate, artifact_path, root=ROOT):
    relative = artifact_path.relative_to(root).as_posix()
    return {
        "scope": "candidate",
        "candidate_id": candidate_id,
        "gate": gate,
        "status": "signed",
        "reviewer_id": "synthetic-reviewer-fixture",
        "reviewer_qualifications": "Fixture only; not an actual reviewer.",
        "independence_statement": "Fixture only; no real review occurred.",
        "reviewed_at": "2026-10-11",
        "method": "Synthetic validator test fixture.",
        "evidence_id": "fixture-evidence-001",
        "artifact_refs": [
            {
                "scope": "public_repo",
                "path": relative,
                "sha256": hashlib.sha256(artifact_path.read_bytes()).hexdigest(),
            }
        ],
        "blocking_finding_ids": [],
    }


def test_cell_biology_scaffold_is_current_unassigned_and_non_authorizing():
    register, packet = _current_register()
    expected = MODULE.scaffold(ROOT, "cell-biology")

    assert "course-grading-policy-review" in MODULE.COURSE_LEVEL_GATES
    assert register == expected
    result = MODULE.audit_register(register, packet, ROOT)
    assert result["candidate_count"] == 15
    assert result["maturity"] == "partial"
    assert result["grading_mode"] == "formative-only"
    assert result["unresolved_candidate_gate_count"] > 0
    assert result["unresolved_course_gates"] == list(MODULE.COURSE_LEVEL_GATES)
    assert result["private_answer_sources_read"] is False
    assert result["reviewer_identity_or_qualifications_independently_verified"] is False
    assert result["release_authorized"] is False
    assert "private://" not in json.dumps(register)


def test_changed_package_or_candidate_hash_invalidates_the_review_register():
    register, packet = _current_register()
    stale_package = copy.deepcopy(register)
    stale_package["public_package_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="stale for public_package_sha256"):
        MODULE.audit_register(stale_package, packet, ROOT)

    stale_candidate = copy.deepcopy(register)
    stale_candidate["candidate_inventory"][0]["metadata_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="stale for candidate"):
        MODULE.audit_register(stale_candidate, packet, ROOT)


def test_signed_review_requires_identity_method_and_hash_bound_evidence():
    register, packet = _current_register()
    candidate_id = register["candidate_inventory"][0]["candidate_id"]
    register["candidate_reviews"] = [
        {
            "scope": "candidate",
            "candidate_id": candidate_id,
            "gate": "subject-matter-review",
            "status": "signed",
            "reviewer_id": "fixture",
        }
    ]
    with pytest.raises(ValueError, match="reviewer_qualifications"):
        MODULE.audit_register(register, packet, ROOT)

    register["candidate_reviews"][0]["reviewer_qualifications"] = "Fixture only"
    with pytest.raises(ValueError, match="independence_statement"):
        MODULE.audit_register(register, packet, ROOT)


def test_public_evidence_hash_is_checked_but_never_grants_release():
    register, packet = _current_register()
    candidate_id = register["candidate_inventory"][0]["candidate_id"]
    artifact = (
        ROOT
        / "docs/reviews/cell-biology-assessment-review-register-0.35.0.md"
    )
    record = _signed_candidate_review(
        candidate_id, "subject-matter-review", artifact
    )
    register["candidate_reviews"] = [record]
    result = MODULE.audit_register(register, packet, ROOT)
    assert result["signed_review_records_as_declared"] == 1
    assert result["unresolved_candidate_gate_count"] > 0
    assert result["release_authorized"] is False

    record["artifact_refs"][0]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="hash is stale"):
        MODULE.audit_register(register, packet, ROOT)


def test_declared_operator_approval_never_authorizes_release():
    register, packet = _current_register()
    artifact = ROOT / "docs/reviews/cell-biology-assessment-review-register-0.35.0.md"
    register["operator_release_decision"] = {
        "decision": "approve",
        "operator_id": "synthetic-operator-fixture",
        "authority": "Fixture only; not a real release authority.",
        "decided_at": "2026-10-11",
        "package_sha256": packet["public_package_sha256"],
        "evidence_id": "operator-fixture-001",
        "artifact_refs": [
            {
                "scope": "public_repo",
                "path": artifact.relative_to(ROOT).as_posix(),
                "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
            }
        ],
    }
    result = MODULE.audit_register(register, packet, ROOT)
    assert result["operator_approval_as_declared"] is True
    assert result["all_declared_review_gates_complete"] is False
    assert result["release_authorized"] is False


def test_cli_checks_current_index_and_strict_mode_reports_unresolved_gates():
    command = [
        sys.executable,
        str(ROOT / "tools/course_review_evidence.py"),
        "--course-id",
        "cell-biology",
        "--check",
        "docs/reviews/cell-biology-review-evidence.json",
    ]
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    report = json.loads(result.stdout)
    assert report["candidate_count"] == 15
    assert report["unresolved_candidate_gate_count"] == 142
    assert report["release_authorized"] is False

    strict = subprocess.run(
        [*command, "--require-all-gates"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert strict.returncode == 2
    assert json.loads(strict.stdout)["unresolved_course_gates"] == list(
        MODULE.COURSE_LEVEL_GATES
    )


def test_external_private_evidence_is_hash_only_and_counted_as_unverified():
    register, packet = _current_register()
    candidate_id = register["candidate_inventory"][0]["candidate_id"]
    register["candidate_reviews"] = [
        {
            "scope": "candidate",
            "candidate_id": candidate_id,
            "gate": "subject-matter-review",
            "status": "signed",
            "reviewer_id": "synthetic-reviewer-fixture",
            "reviewer_qualifications": "Fixture only.",
            "independence_statement": "Fixture only; no review occurred.",
            "reviewed_at": "2026-10-11",
            "method": "Synthetic fixture.",
            "evidence_id": "external-fixture-001",
            "artifact_refs": [
                {
                    "scope": "external_attestation",
                    "reference": "fixture-digest-only",
                    "description": "Fictional protected-source check; not performed.",
                    "sha256": "a" * 64,
                }
            ],
            "blocking_finding_ids": [],
        }
    ]
    result = MODULE.audit_register(register, packet, ROOT)
    assert result["external_artifact_hashes_not_verified"] == 1
    assert result["release_authorized"] is False
