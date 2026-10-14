# Historical graded-assessment archive triage

This runbook covers records created before graded-source archiving was available, and records the read-only audit classifies as unverifiable or inconsistent. It does not restore source bytes, regrade a submission, decide an appeal, or authorize a change to learner records.

## 1. Preserve the current record

Before investigating production data, follow the [deployment backup procedure](DEPLOYMENT.md) and verify the backup. Record the application and migration versions, date, operator, and incident or appeal reference in the institution's protected case system. Keep names, learner IDs, responses, scores, keys, and source documents out of this runbook and ordinary logs.

Run the privacy-preserving aggregate report:

```sh
docker compose exec -T api python -m courselab.audit_graded_archives
```

For production, use the production Compose file and environment arguments from `DEPLOYMENT.md`. This command is report-only. Save its aggregate output with the incident record; do not edit the database based on the report.

## 2. Interpret the status conservatively

| Audit status | What the report establishes | Operator response |
| --- | --- | --- |
| `source_archive_verified` | The saved enrollment/plan/instance links and archived source bytes match the stored source SHA-256. | Treat this as source-provenance evidence only. It does not validate the answer key, grader, score, or academic quality. Continue the appeal or quality process under institutional policy. |
| `archive_missing` | No archived source row was found for the linked assessment and version. | Check for a trusted, access-controlled historical release artifact and deployment record. If exact source bytes and their digest cannot be independently established, record the submission as unverifiable and refer it for a human academic decision. |
| `archive_digest_mismatch` | An archive exists for the assessment/version, but not with the digest pinned to this submission. | Preserve both records and escalate as a source-integrity incident. Do not choose whichever archive seems plausible. |
| `archive_ambiguous` | More than one archive row matches the same course/version/assessment/digest. | Escalate for database-integrity review; do not delete or merge rows as part of appeal handling. |
| `archive_bytes_corrupt` | The stored bytes fail their recorded digest. | Preserve the database and backup, restrict ordinary access under incident policy, and escalate. Do not overwrite the bytes with current files. |
| `snapshot_link_mismatch`, `snapshot_source_digest_mismatch`, `enrollment_missing`, `plan_missing`, `assessment_instance_missing` | The submission's saved relationships are incomplete or inconsistent. | Escalate as a data-integrity issue. The aggregate count does not identify a particular learner or justify a score change. |

Counts are grouped by course, pinned version, assessment, and status. They intentionally omit learner/submission identifiers and response or score data. Use the institution's authorized case-management process for any individual appeal; do not try to infer an individual's state from aggregate counts.

## 3. Establish historical source evidence

An assessment can be treated as historically source-verifiable only when the institution can independently establish the exact protected source bytes that governed that submission and match them to the stored course, version, assessment, form, and digest metadata. A version string, current course package, similarly named file, current answer key, or author recollection is insufficient by itself.

Migration 0010 archives graded-source bytes for newly pinned assessment plans; it did not backfill earlier submissions. The public course-package backfill command in `DEPLOYMENT.md` archives learner-facing package files only. It does not recover private assessment sources, answer keys, grader implementations, or historical grading rules. There is currently no supported private-source backfill command. Do not write archive rows directly or reconstruct historical source from the current package.

If a trusted, exact historical source package is found, preserve its provenance and digest and submit a separate engineering change for review before any import or regrade. That change must preserve the original submission and decision history and be tested against appeals and access controls. A verified source still does not prove that the original score was correct.

## 4. Decide the case under institutional policy

The audit does not change grades or determine whether a learner should receive credit, a regrade, an extension, or an appeal remedy. A qualified human decision-maker must consider the available evidence, applicable policy, fairness to affected learners, and the limits of the historical record. Preserve the original grade and source state until the authorized process records a decision; document the rationale and evidence in the protected case system.

Do not label an unverifiable submission correct or incorrect solely because its archive is missing. If no exact source evidence exists, state that historical grading cannot be independently reconstructed from this system. Any remedy belongs to the institution's academic process, not an automated archive repair.

## 5. Close and prevent recurrence

Record the audit date and aggregate status, backup reference, evidence reviewed, decision authority, final disposition, and any follow-up engineering issue in the protected case system. Retain or dispose of that record under institutional privacy policy. After the incident, confirm that current plans pin the intended source and grader digests and that the routine archive audit remains part of operations.

The platform's source-archive audit and public-package backfill are technical evidence tools. They do not authenticate reviewer qualifications, establish grading correctness, or substitute for institutional appeal, retention, and release policies.
