# Bioreactors review snapshot

This record pins the current public course package for independent review. It is regenerated with the read-only command below and does not imply acceptance or release.

- **Course package:** `bioreactors` 0.4.9
- **Public package archive SHA-256:** `56053cef00acf0e6ecb290dc777593308b43840767565dac09afa798e88c245a`
- **Manifest SHA-256:** `ba5d45a2f97958bb1fc633cf93260f75f4f062d1a3d93535ab8aae1d5af5b6a3`
- **Archive inventory:** 24 files, 341,955 bytes
- **Calculated:** 2026-10-13
- **Reproduce:** `uv run --project backend python tools/course_package_digest.py --course-id bioreactors`

Version 0.4.9 adds an original fed-batch reading grouped with continuous culture in week 4. It covers changing-volume balances, the dilution term without outflow, an exponential substrate-holding feed, the working-volume limit and retained-product titer, with ten formative items and four cards. MIT OCW [10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) is a link-only comparator. Every numeric key is recomputed by RK4 integration of the amount balances. The digest proves package identity only; it is not bioprocess review, instructional approval or release evidence. The course remains partial, unreviewed and formative-only.
