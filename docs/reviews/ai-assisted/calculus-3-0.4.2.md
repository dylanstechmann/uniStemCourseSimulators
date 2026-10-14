# Calculus III 0.4.2 — multivariable optimization

Date: 2026-10-10. Codex expanded the week-5 optimization reading and added separate numerical checks. The same AI assistant authored the lesson and regression, so these checks are not independent mathematical or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The reading distinguishes critical-point conditions from classification, explains positive/negative-definite and indefinite Hessians, and states when the second-derivative test is inconclusive. It derives a regular equality-constrained Lagrange condition, then verifies a global maximum by substitution along the feasible set. It also identifies boundary and inequality cases that need additional checks. Existing questions, keys, objectives and item counts are unchanged; two compact prototype readings remain.

## Numerical checks

For $F(x,y)=4-(x-1)^2-2(y+2)^2$, the stationary point $(1,-2)$ has gradient zero and Hessian $\operatorname{diag}(-2,-4)$, with determinant 8 and global maximum 4. For $xy$ subject to $x+y=10$, the multiplier is 5 at $(5,5)$ and the objective is 25. Substitution gives $x(10-x)=25-(x-5)^2\le25$ for every real $x$. These checks verify the constructed examples and selected conditions, not every theorem or design application.
