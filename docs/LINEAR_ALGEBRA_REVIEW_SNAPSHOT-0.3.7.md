# Linear Algebra review snapshot

This record pins the current public course package for independent review. It is regenerated with the read-only command below and does not imply acceptance or release.

- **Course package:** `linear-algebra` 0.3.7
- **Public package archive SHA-256:** `f98849cf30202bac6f0bed0bb7ccc07b7172544f54b95b3f573ec3a5208b02d6`
- **Manifest SHA-256:** `8af2263c70b37a12dd2e2cac20fb2bed7ffa289548972a5add57ee3baadc0734`
- **Archive inventory:** 24 files, 324,010 bytes
- **Calculated:** 2026-10-13
- **Reproduce:** `uv run --project backend python tools/course_package_digest.py --course-id linear-algebra`

Version 0.3.7 adds an original determinants reading grouped with eigenvalues in week 7. MIT OCW [18.06SC Fall 2011 Unit II](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/) places three determinant sessions between Gram–Schmidt and eigenvalues. The reading covers volume scaling, row-operation rules, elimination and cofactor computation, invertibility, det(A − λI) = 0 and why determinant size is not a conditioning measure, with eleven formative items and four cards. Every numeric key is recomputed by exact cofactor expansion in the course recalculation test. The digest proves package identity only; it is not mathematical review, instructional approval or release evidence. The course remains partial, unreviewed and formative-only.
