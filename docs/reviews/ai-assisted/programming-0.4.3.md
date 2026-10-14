# Programming & Numerical Methods 0.4.3 — regression and validation

Date: 2026-10-10. Codex expanded the week-10 regression reading and added a residual-error check. The same AI assistant authored the reading and regression, so these checks are not independent code, statistical or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson distinguishes training fit, residual scatter, parameter uncertainty and predictive uncertainty. It explains why learned preprocessing must remain inside training folds, why split units should match the prediction target, and how repeated donor measurements can leak information across a row-level split. Existing questions, keys and objectives are unchanged; only the week-12 prototype reading remains compact.

## Numerical checks

For residuals $0.1,-0.2,0.1,0,0$, residual sum of squares is $0.06$. With five observations and two parameters, residual standard error is $\sqrt{0.06/3}\approx0.1414$. The existing item key remains 0.1414, and the regression independently recomputes it.
