# Programming & Numerical Methods 0.4.2 — quadrature and Euler stability

Date: 2026-10-10. Codex expanded the week-7 reading and added separate quadrature and recurrence checks. The same AI assistant authored the lesson and regression, so these checks are not independent mathematical or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson compares trapezoid and Simpson approximations, connects integration to accumulated units, derives forward Euler for a first-order ODE, and checks the amplification condition for a scalar decay mode. It distinguishes numerical instability from physical reversal, and numerical tolerance from model validity. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 10 and 12.

## Numerical checks

For $t^2$ on $[0,2]$, the one-panel trapezoid estimate is 4, while Simpson's rule and the exact integral are both $8/3$. For $y'=-4y$, Euler with $h=0.6$ has multiplier $-1.4$ and grows in magnitude; $h=0.4$ has multiplier $-0.6$ and decays in magnitude with sign alternation. Existing public answers, including the preserved 1.4 amplification key, remain unchanged.
