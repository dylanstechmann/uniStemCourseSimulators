# Biochemistry I review snapshot

This record pins the current public package for independent review. It does not imply acceptance or release.

- **Course package:** `biochemistry` 0.4.85
- **Public package archive SHA-256:** `11e44547cc09947f07291f11d7f20547e1e184b9699a1e946272c1deaf3f9fda`
- **Manifest SHA-256:** `03c8a96b4f96b12796db521cac14a382a967703b8eaeeec80b2877cb93840ec3`
- **Archive inventory:** 70 files, 1,111,975 bytes
- **Calculated:** 2026-10-11
- **Reproduce:** `uv run --project backend --locked python -B tools/course_package_digest.py --course-id biochemistry`

Version 0.4.85 consolidates overlapping explanations while preserving the lesson IDs and formative questions. The central-metabolism primer now introduces the ledgers and points to dedicated free-energy and mitochondrial treatments; the network lesson frames perturbation evidence and refers quantitative control coefficients to their later lesson. The proposed scope focuses on heterotrophic animal-cell metabolism and explicitly defers photosynthesis, membrane transport and translation. The official [MIT OCW 7.05 Spring 2020 calendar](https://ocw.mit.edu/courses/7-05-general-biochemistry-spring-2020/pages/calendar/) includes those topics; the [syllabus](https://ocw.mit.edu/courses/7-05-general-biochemistry-spring-2020/pages/syllabus/) states that its OCW materials cover primarily the metabolism half. The local sequence is a narrower comparator, not an equivalent course.

The public package contains 11 inactive assessment candidates and two synthetic-data virtual labs. Candidate prerequisite hashes now point to the 0.4.85 readings; their questions, answer keys and inactive status were not changed. The package remains partial, unreviewed and formative-only. Historical review and workload artifacts for 0.4.84 remain pinned to that earlier version; the digest establishes package identity only, not scientific review, instructional approval or release readiness.
