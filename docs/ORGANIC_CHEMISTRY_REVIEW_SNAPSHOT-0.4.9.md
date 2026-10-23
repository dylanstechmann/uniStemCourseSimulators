# Organic Chemistry I review snapshot

This record pins the current public course package for independent review. It does not imply acceptance or release.

- **Course package:** `organic-chemistry` 0.4.9
- **Public package archive SHA-256:** `9f9640d5f3743028486e33c13c01c93fbab8c4cf55aad41a3ed6ee6c92b8b67c`
- **Manifest SHA-256:** `148ca3c3b3e28cc565aeb8eca521f47463db35be89cdeb0dad1a12ef6fba3375`
- **Archive inventory:** 26 files, 403,130 bytes
- **Calculated:** 2026-10-13
- **Reproduce:** `uv run --project backend --locked python -B tools/course_package_digest.py --course-id organic-chemistry`

Version 0.4.9 adds a nucleophilic aromatic substitution (SNAr) strand to the existing aromaticity lesson rather than a new week. MIT OCW [5.12 Spring 2005 calendar](https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2005/pages/calendar/) pairs electrophilic and nucleophilic aromatic substitution in week 11. The lesson explains the Meisenheimer-complex addition–elimination mechanism, why ortho/para but not meta electron-withdrawing groups activate, the activated-ring leaving-group trend and the nitro group's opposite roles in EAS and SNAr. It includes one new objective, seven mapped formative items and three cards. OpenStax Organic Chemistry 16.6 is a link-only reference; no source asset or exercise was imported. Benzyne chemistry and multistep synthesis remain absent.

The independent recalculation test now covers every numeric key in the package, including the lesson 14–16 items, and the repository content validator and Organic Chemistry tests were run for this version. The 0.4.8 snapshot is archived separately. This digest establishes package identity only, not chemical review or release approval. The course remains partial, unreviewed and formative-only.
