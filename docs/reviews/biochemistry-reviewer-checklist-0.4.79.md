# Biochemistry 0.4.79 external-review checklist

**Purpose:** prepare and record qualified review of an inactive course package. This checklist is not evidence that a review occurred, a course approval, or authorization to assign or grade work.

## Package to review

| Identifier | Pinned value |
| --- | --- |
| Course | Biochemistry I: Proteins, Enzymes & Metabolism (`biochemistry`) |
| Version | `0.4.79` |
| Public package SHA-256 | `2a3e4df695f46db6ef54426db20e0594420815ef3adda0dece17c83bfb86ff61` |
| Manifest SHA-256 | `f9f3fac07002318bf85ecd13324ca5cdbb4e2d2d544c90a3407544cdd14b7aa2` |
| Current state | `partial`, `unreviewed`, `formative-only`; no candidates active |

Start from the generated [assessment-candidate report](../ASSESSMENT_CANDIDATE_REPORT.md), which names the exact candidates, artifacts, and hashes. Confirm its hashes against the current [public-package snapshot](../BIOCHEMISTRY_REVIEW_SNAPSHOT.md) before reviewing. If any package or candidate hash differs, stop and regenerate this packet for the new version. The private assessment sources are not part of the public snapshot; use the institution's protected review process for them.

## Candidate-level gates

There are 11 inactive candidates. The candidate report currently lists eight unresolved gate types for each candidate (88 candidate-gate instances total). Review each candidate separately where its content or grading behavior differs. Course-wide evidence, especially one measured-workload study, may support multiple candidate records when the method and exact version scope justify it; do not duplicate a study merely to create more records.

| Gate | Reviewer evidence to provide |
| --- | --- |
| `independent-recalculation` | Independently recompute numeric answers from the authored prompt and source data, record equations, units, assumptions, tolerances, and discrepancies. Do not begin by copying the private key. |
| `grader-mutation-review` | Review expected, partial, missing, malformed, and boundary responses against the rubric and actual grader. The author-side one-field mutation audit is supporting evidence, not an independent sign-off. |
| `qualified-biochemical-review` | State relevant biochemical qualifications; check mechanism, stoichiometry, terminology, evidence limits, and whether each answer is scientifically defensible. Cite candidate and lesson artifact hashes. |
| `assessment-blueprint-review` | Check level, cognitive demand, objective links, coverage, point allocation, and whether the fixed candidate form supports the intended assessment claim. |
| `accessibility-and-fairness-review` | Review accessible formats and interactions, language and time demands, accommodations, and foreseeable construct-irrelevant barriers or bias. Record limitations and remediation. |
| `measured-workload` | Use the version-bound [workload-pilot protocol](biochemistry-workload-pilot-0.4.79.md) only after a required learner plan is frozen and other prerequisites are met. No pilot data currently exist. |
| `candidate-specific-protected-delivery-verification` | Have an authorized operator verify the exact protected source and grader are confined, access-controlled, and delivered only under the approved assessment plan. Do not put keys or protected-source paths in this public register. |
| `operator-release-and-retake-policy` | Have the responsible operator approve the release, timing, retake, review, appeal, and recovery rules for this candidate. The candidate is not live until that decision is recorded in the applicable system. |

## Course-level gates and separate approvals

The evidence register tracks four course-level gates:

| Gate | Review evidence to provide |
| --- | --- |
| `course-scope-review` | Qualified review of course outcomes, sequence, prerequisites, depth, and the boundary of the course claim. |
| `course-grading-policy-review` | Review of a proposed grading policy and its consequences. No graded assignments or approved grading policy are currently active. |
| `measured-workload` | A version-pinned workload study of the owner-approved required learner plan. The prospective protocol is not pilot data. |
| `institutional-equivalency` | A determination by the receiving institution against its own curriculum, credit, contact-time, and assessment requirements. |

The proposed potato-catalase activity and its [blank instructor pilot log](biochemistry-physical-lab-pilot-log-0.4.79.md) sit outside the course package. They do not close any physical-laboratory, safety, accessibility, or training requirement. Local laboratory-supervisor and EHS approval, a successful local pilot, and institutionally required review remain necessary before student use.

## Record each review

For each gate, submit a separate record to the version-bound [evidence register](biochemistry-review-evidence-0.4.79-finalized.json). Identify the reviewer, qualifications, independence, date, method, decision (`in_progress`, `revise`, or `signed`), and evidence artifacts. Public evidence must be stored under `docs/reviews/` and referenced by SHA-256. External evidence must be cited by stable reference and digest, while the institution retains the actual document.

The evidence tool checks package and public-evidence hashes and validates the record structure. It cannot authenticate a person's identity or qualifications, verify an external document's contents, or approve a course. The institution must establish reviewer identity, conflict handling, and secure evidence retention outside the tool.

```text
Candidate ID or course scope:
Gate:
Reviewer name / institutional identifier:
Relevant qualifications:
Independence / conflict statement:
Date and method:
Decision: in_progress | revise | signed
Evidence references and SHA-256 digests:
Findings, limitations, and required corrections:
Reviewer attestation / institutional record reference:
```

`Signed` records acceptance of the named gate by the recorded reviewer; it does not activate a candidate or certify the whole course. A release decision belongs to the authorized operator after applicable candidate and course gates are resolved. Keep the package partial, unreviewed, and formative-only until the institution's complete review and release process supports a different state.
