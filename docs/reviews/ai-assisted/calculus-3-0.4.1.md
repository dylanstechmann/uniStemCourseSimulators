# Calculus III 0.4.1 — vectors and gradients

Date: 2026-10-10. Codex expanded the week-1 reading and added a separate finite-difference regression. The same AI assistant authored the reading and test, so these checks are not independent mathematical or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson develops coordinate partials, the gradient as a local linear model, directional derivatives along unit vectors, level-curve geometry, and the limits of first-order approximations. A constructed dimensionless field demonstrates the exact and predicted changes for a small displacement. Existing questions, keys, objectives and item counts are unchanged. Three compact prototype readings remain.

## Numerical checks

For $f(x,y)=x^2y+\sin y$ at $(1,0)$, separate centered differences recover gradient $(0,2)$. The unit direction $(3/5,4/5)$ gives directional derivative 1.6. A displacement $(0.02,0.03)$ has linear prediction 0.06 and exact change approximately 0.061207. The regression checks the gradient, unit norm, directional derivative and local approximation error; it does not assess every theorem or physical concentration field.
