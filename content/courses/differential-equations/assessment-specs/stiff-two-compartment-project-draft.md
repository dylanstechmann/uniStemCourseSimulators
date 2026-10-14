# Stiff two-compartment system: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded and is not a protected assessment. The state variables and rate constants are normalized mathematical constructs, not quantities or parameters for any real organism, chamber, device or process.

## Purpose and outcomes

Analyze one coupled linear ODE system from its exact solution through its numerical behavior. The project connects equilibrium/stability, eigenvalues, integrating factors, stiffness, explicit Euler stability, positivity constraints, and an implicit Euler comparison.

## Model

For dimensionless `t ≥ 0`, consider

\[
x'=-x,\qquad y'=x-100y,\qquad x(0)=1,\quad y(0)=0.
\]

The model is deliberately small and exact. It is not a fit to data and its two state labels have no biological or engineering interpretation.

## Work sequence

1. Solve for `x(t)` and then use an integrating factor to find `y(t)`. Check both initial conditions and substitute the formulas back into the ODEs.
2. Find the system eigenvalues and explain why the two time scales make the system stiff. Determine the explicit-Euler stability restriction from the fast eigenvalue.
3. Use `y'=0` and the exact solution to find when `y` reaches its maximum. Verify that the result is a maximum and calculate the peak value.
4. Write the forward-Euler recurrence. Starting from `(1,0)`, take four steps of size `h=0.025` to `t=0.1`. Compare the result with the exact solution and explain any negative component.
5. Derive the backward-Euler recurrence. Repeat at `h=0.025` and compare positivity and error with the exact state at `t=0.1`. Explain why positivity alone does not establish accuracy.
6. Repeat explicit Euler with ten steps of size `h=0.01`. Compare errors and connect the step size with both the stability threshold and the positivity bound for the fast component.
7. State what evidence would be needed before this type of simplified model could be used to describe a real system; do not invent experimental parameters or procedures.

## Author calculation key

The exact solution is

\[
x(t)=e^{-t},\qquad y(t)=\frac{e^{-t}-e^{-100t}}{99}.
\]

The eigenvalues are `−1` and `−100`. Forward Euler requires `0<h<0.02` for strict linear stability of the fast mode, and `h≤0.01` keeps the coefficient `1−100h` nonnegative in the explicit update for `y`. At the peak, `x=100y`, so `e^{-t}=100e^{-100t}` and `t*=ln(100)/99≈0.0465169`; `y(t*)=e^{-t*}/100≈0.00954548`.

Forward Euler uses

\[
x_{n+1}=(1-h)x_n,\qquad y_{n+1}=h x_n+(1-100h)y_n.
\]

At `h=0.025`, four steps give `(x₄,y₄)≈(0.90368789,−0.04200820)`, while the exact state is `(0.90483742,0.00913931)`. The negative component is a numerical failure of this step, not a property of the exact model. Backward Euler gives

\[
x_{n+1}=\frac{x_n}{1+h},\qquad y_{n+1}=\frac{y_n+h x_{n+1}}{1+100h}.
\]

At `h=0.025` and `t=0.1`, it gives `(0.90595064,0.00908370)`: nonnegative, with a small but nonzero error. At `h=0.01`, ten forward-Euler steps give `(0.90438208,0.00913517)`, close to but not identical to the exact state. For this recurrence, positive initial states remain nonnegative under backward Euler for any `h>0`; that structural property does not remove time-discretization error.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Exact solution | Uses the initial conditions and verifies both equations |
| Stability | Finds both eigenvalues and derives the strict explicit-Euler bound |
| Positivity | Distinguishes stability from the nonnegative-update condition |
| Numerical comparison | Recomputes explicit/implicit steps and checks against the exact solution |
| Limits | Separates synthetic mathematics from claims about a real system |

The rubric has no point weights or automatic prose grader. Workload, accessibility, mathematical accuracy and instructional design need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and normalized synthetic parameters, CC BY 4.0, developed with substantial AI assistance. No external dataset or real-world procedure is included.
