# Calculus I 0.4.2 — derivative rules and units

Date: 2026-10-10. Codex expanded the original week-3 reading and wrote separate numerical regressions. The checks derive the reported slopes from the functions, but the same AI assistant authored the lesson and tests; this is not independent academic or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The compact derivative-rules reading now explains product, quotient and chain rules; exponential decay; and unit tracking through a concentration-dependent response. It distinguishes differentiating a function of concentration from differentiating that concentration over time, and states the inverse-hour unit needed to keep the exponential argument dimensionless. Implicit differentiation and extended related-rate problems remain in the later lesson. Existing questions, answer keys, objectives, points and assessment policy are unchanged. The package advances from 0.4.1 to 0.4.2; two compact legacy readings remain.

## Numerical checks

For \(p(x)=xe^{-x}\), a central difference at 1 gives slope 0, matching \(p'(1)=0\). For \(q(x)=(x^2+1)/(x+1)\), a central difference at 2 gives \(7/9\), matching the quotient-rule expression. The chain-rule example \((3x+1)^4\) has derivative 768 at 1. For \(C(t)=5e^{-0.2t}\) mM, the rate at two hours is \(-0.670320\) mM/h. For \(R(c)=100c/(2\,\mathrm{mM}+c)\) and \(c(t)=4e^{-0.1t}\) mM, the initial response rate is \(-20/9\) percentage points per hour; concentration units cancel.

The expanded Calculus I regression file passed 77 tests; Ruff passed for that file. Full content validation passed for 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases, with zero errors and 94 disclosed legacy-depth warnings. These checks do not validate workload, accessibility or biological interpretation.
