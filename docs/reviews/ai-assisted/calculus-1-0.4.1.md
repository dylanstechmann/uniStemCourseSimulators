# Calculus I 0.4.1 — introductory limits reading checks

Date: 2026-10-10. Codex expanded the original week-1 reading and wrote the separate numerical regression check. The arithmetic is independently recalculated in code from the stated function, but the same AI assistant authored both the reading and its test. This is not independent academic or human review. The package remains **partial, unreviewed and formative-only**.

## Scope

The 491-word prototype on limits, continuity and approximation became a substantive foundational reading. It uses a removable-hole example to separate a limit from a point value, a threshold function to show unequal one-sided limits, and a square-root model to illustrate a local tangent and a bounded Taylor remainder. The existing objectives, questions, keys, points, schedule, and practice policy are unchanged. The course advances from 0.4.0 to 0.4.1; three compact prototype units remain.

## Numerical checks

The quotient \((x^2-1)/(x-1)\) was evaluated directly at 0.9, 0.99, 1.01 and 1.1, producing 1.9, 1.99, 2.01 and 2.1. For \(f(u)=\sqrt{100+u}\), the tangent at zero is \(10+u/20\). Direct evaluation gives absolute errors 0.001960973 at \(u=4\) and 0.045548850 at \(u=20\). On \([-25,25]\), \(|f''(u)|\le1/[4(75)^{3/2}]=0.00038490018\), so Taylor's bound at 20 is 0.076980036 and exceeds the actual error. The reading states the bound only on its declared interval.

`tests/content/test_calculus_one_recalculations.py` adds these calculations and checks the schedule/version labels. The targeted file passed 76 tests. Full content validation passed for 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases, with zero errors and 95 disclosed legacy-depth warnings. This narrow verification does not measure workload, accessibility, learner outcomes or the remaining course materials.
