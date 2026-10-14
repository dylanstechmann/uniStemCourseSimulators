# Calculus II 0.4.1 — integration methods and improper limits

Date: 2026-10-10. Codex expanded the original week-1 reading and added separate numerical regressions. The same AI assistant authored the reading and tests, so these checks are not independent academic or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The introductory reading now presents substitution, integration by parts and partial fractions through representative examples, emphasizing primitive checks and interval domains. It derives the convergence threshold for power integrals on infinite intervals and near finite endpoint singularities, then connects the infinite-interval limit to a constructed exponential exposure. The more extensive method practice remains in the later course readings. Existing questions, keys and objectives are unchanged. The package advances from 0.4.0 to 0.4.1; three compact legacy readings remain.

## Numerical checks

The substitution example evaluates to \(\ln(7/3)\). The by-parts primitive differentiates to \(x\ln x\) on positive sample points, and the boundary term \(x^2\ln x\) tends to zero at the origin. The partial-fraction example evaluates to \(\tfrac12\ln(3/2)\). The \(p=2\) tail \(\int_1^\infty x^{-2}dx\) equals 1 after the substitution \(u=1/x\); the harmonic cutoff \(\int_1^B dx/x=\ln B\) grows without bound. The exponential practice integral approaches 2.

The regression checks course and syllabus versions, formative/unreviewed status, and the numerical identities. These calculations do not establish comprehensive course coverage, workload, accessibility or physical interpretation.
