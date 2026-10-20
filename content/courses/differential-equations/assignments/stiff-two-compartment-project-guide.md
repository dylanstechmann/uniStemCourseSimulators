# Stiff project guide: one coupled system from its exact solution to its numerical behavior (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 3–5 hours across weeks 12 and 13.
**Prerequisite lessons:** [Forced first-order systems](../modules/07-forced-first-order-systems-in-a-perfused-chamber.md), [Phase portraits of linear systems](../modules/09-phase-portraits-of-linear-systems.md), [Numerical ODEs and error control](../modules/04-numerical-odes-and-error-control.md) and [Stiff equations and implicit methods](../modules/12-stiff-equations-and-implicit-methods.md).

## Purpose

A small linear system can be solved exactly, which makes it a good test bench for numerical methods. This project solves one coupled system by hand, reads its stiffness from the eigenvalues, and then watches what explicit and implicit Euler do with it: where explicit steps lose stability or positivity, why an implicit step stays positive, and why staying positive is not the same as being accurate.

## The project

For dimensionless t ≥ 0, consider the normalized system

\[
x'=-x,\qquad y'=x-100y,\qquad x(0)=1,\quad y(0)=0.
\]

It is deliberately small and exact, not a fit to data, and its two state labels have no biological or engineering interpretation. Forward Euler uses x_{n+1} = (1 − h)x_n and y_{n+1} = h x_n + (1 − 100h)y_n.

1. Solve for x(t), then use an integrating factor to find y(t). Check both initial conditions and substitute the formulas back into the equations.
2. Find the system eigenvalues and explain why the two time scales make the system stiff. Determine the explicit-Euler stability restriction from the fast eigenvalue.
3. Use y′ = 0 and the exact solution to find when y reaches its maximum. Verify that it is a maximum and calculate the peak value.
4. Starting from (1, 0), take four forward-Euler steps of size h = 0.025 to t = 0.1. Compare with the exact solution and explain any negative component.
5. Derive the backward-Euler recurrence. Repeat at h = 0.025 and compare positivity and error with the exact state at t = 0.1. Explain why positivity alone does not establish accuracy.
6. Repeat forward Euler with ten steps of size h = 0.01. Compare the errors and connect the step size with both the stability threshold and the positivity bound for the fast component.
7. State what evidence would be needed before this type of simplified model could describe a real system; do not invent experimental parameters or procedures.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 12 | Work the rehearsal system, then use the open rehearsal practice set | **Practice gradebook**: Stiff project rehearsal |
| M1 | 12 | The exact solution and its checks (task 1) | Case studio: project milestone 1 |
| M2 | 12 | Eigenvalues, stiffness, the step limit and the peak (tasks 2–3) | Case studio: project milestone 2 |
| M3 | 12 | Four forward-Euler steps and any negative value (task 4) | Case studio: project milestone 3 |
| M4 | 13 | Backward Euler and the smaller explicit step (tasks 5–6) | Case studio: project milestone 4 |
| M5 | 13 | The evidence a real system would need (task 7) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal system

Before the project, work the same steps on x′ = −2x, y′ = 2x − 50y with x(0) = 1 and y(0) = 0: four explicit and four implicit steps of size 0.03 to t = 0.12, and twelve explicit steps of size 0.01. Then check yourself with the open rehearsal practice set, which gives feedback on each value. Its rates and step sizes differ from the project's, and its explicit step falls in a different regime, so its answers are not the project's answers.

## Worked example: a third system

Take x′ = −x, y′ = x − 20y with x(0) = 1 and y(0) = 0.

1. **Exact solution.** x = e^(−t). Then y′ + 20y = e^(−t), and the integrating factor e^(20t) gives

   \[
   y(t)=\frac{e^{-t}-e^{-20t}}{19},
   \]

   which is 0 at t = 0 and satisfies the equation on substitution.
2. **Stiffness and step limits.** The matrix is triangular, with eigenvalues −1 and −20. Forward Euler multiplies the fast mode by 1 − 20h, so it is stable for 0 < h < 0.1 and keeps the y update nonnegative only for h ≤ 0.05. The slow mode alone would allow far larger steps.
3. **Peak.** y′ = 0 when x = 20y, which with the exact formulas gives e^(19t) = 20 and t* = ln(20)/19 ≈ 0.1577. There y = e^(−t*)/20 ≈ 0.04271, and y′ changes from positive to negative, so this is a maximum.
4. **One backward-Euler step.** At h = 0.05, x₁ = 1/1.05 ≈ 0.9524 and y₁ = (0 + 0.05 × 0.9524)/(1 + 20 × 0.05) ≈ 0.02381, both positive. The exact state at t = 0.05 is x ≈ 0.9512 and y ≈ 0.03070, so the implicit step stays positive and still misses y by more than 20%.

## Reporting conventions

- Keep eight significant figures in iterates and round only reported values.
- Update x and y together from the previous step's values; do not use a new x in an explicit y update.
- State the step size, the number of steps and the final time with every numerical result.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Exact solution | Uses the initial conditions and verifies both equations |
| Stability | Finds both eigenvalues and derives the strict explicit-Euler bound |
| Positivity | Distinguishes stability from the nonnegative-update condition |
| Numerical comparison | Recomputes explicit and implicit steps and checks against the exact solution |
| Limits | Separates synthetic mathematics from claims about a real system |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The systems are normalized mathematical constructs with no physical, biological or engineering interpretation. Their behavior under Euler's methods illustrates stability, positivity and discretization error; it says nothing about any real compartment, organism or process. Original guide and rehearsal system: CC BY 4.0, developed with substantial AI assistance.
