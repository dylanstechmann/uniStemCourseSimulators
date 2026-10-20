# Slab project guide: steady heat generation, an energy check and the lumped limit (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 13 and 14.
**Prerequisite lessons:** [Control volumes and conservation](../modules/01-control-volumes-and-conservation.md), [Heat transfer and coupled transport](../modules/04-heat-transfer-and-coupled-transport.md) and [Heat transfer: lumped capacitance and the Biot number](../modules/11-heat-transfer-lumped-capacitance-and-the-biot-number.md).

## Purpose

A body that generates heat inside must pass that heat out through its surface, and doing so needs a temperature gradient. This project derives the steady temperature field in a heat-generating slab, checks it against an energy balance and a numerical average, and asks when a single "lumped" temperature is a fair description. The Biot number is the screen for that last question, and the project shows what it does and does not guarantee.

## The project

All dimensions and thermal values are synthetic teaching quantities, not vessel, tissue, equipment or process specifications. A symmetric plane slab occupies −L ≤ x ≤ L with L = 0.010 m, uniform conductivity k = 0.50 W/(m·K) and uniform generation q‴ = 10,000 W/m³. Both faces convect to a fluid at T∞ = 25 °C with h = 20 W/(m²·K). Assume steady one-dimensional conduction, constant properties, symmetry at x = 0, and no radiation or edge effects. On 0 ≤ x ≤ L,

\[
k\frac{d^2T}{dx^2}+q'''=0,\qquad T'(0)=0,\qquad -kT'(L)=h\,[T(L)-T_\infty].
\]

1. Integrate the equation twice and apply the center symmetry and surface convection conditions to derive T(x).
2. Calculate the surface and center temperatures, then verify the surface heat flux against the heat generated per unit area.
3. Derive the half-slab average temperature, and check it independently with composite Simpson's rule at x/L = 0, 0.25, 0.50, 0.75 and 1.00.
4. Compute Bi = hL/k. Compare the exact maximum and average temperatures with the uniform steady energy-balance estimate, and explain why the Biot screening check matters for the lumped approximation.
5. State which boundary conditions and omitted transport modes make this result unsuitable as a real thermal or biological design.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 13 | Work the rehearsal slab, then use the open rehearsal practice set | **Practice gradebook**: Slab project rehearsal |
| M1 | 13 | The temperature profile (task 1) | Case studio: project milestone 1 |
| M2 | 13 | Surface and center temperatures and the energy check (task 2) | Case studio: project milestone 2 |
| M3 | 13 | The average and its Simpson check (task 3) | Case studio: project milestone 3 |
| M4 | 14 | The Biot number and the lumped estimate (task 4) | Case studio: project milestone 4 |
| M5 | 14 | Boundary conditions and omitted modes (task 5) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal slab

Before the project, work the same steps on a second synthetic slab, then check yourself with the open rehearsal practice set, which gives feedback on each value. The rehearsal slab has L = 0.010 m, k = 2.0 W/(m·K), q‴ = 20,000 W/m³, h = 10 W/(m²·K) and T∞ = 22 °C. Its conductivity is high and its surface coefficient low, so its Biot number is small; the project's is not. Its answers are not the project's answers.

## Worked example: a third slab

Take a slab with L = 0.005 m, k = 0.25 W/(m·K), q‴ = 30,000 W/m³, h = 50 W/(m²·K) and T∞ = 30 °C.

1. **Profile.** Integrating once with T′(0) = 0 gives T′(x) = −q‴x/k. The heat generated in the half-slab, q‴L per unit area, must leave the face by convection, so T(L) = T∞ + q‴L/h. Integrating again,

   \[
   T(x)=T_\infty+\frac{q'''L}{h}+\frac{q'''}{2k}\left(L^2-x^2\right).
   \]

2. **Temperatures and the energy check.** T(L) = 30 + 30,000 × 0.005/50 = 33.0 °C and T(0) = 33.0 + 30,000 × 0.005²/(2 × 0.25) = 34.5 °C. The face carries q‴L = 150 W/m², and convection gives 50 × 3.0 = 150 W/m², so the balance closes.
3. **Average.** The parabola's mean excess is two thirds of its center excess, so the average is 33.0 + (2/3) × 1.5 = 34.0 °C. Simpson's rule on the five nodes gives the same value, because it integrates a quadratic exactly.
4. **Lumped limit.** Bi = 50 × 0.005/0.25 = 1.0. A lumped estimate puts the whole slab at T∞ + q‴L/h = 33.0 °C, which matches the surface but misses the center by 1.5 °C, half of the 3 °C rise above the fluid, and the average by 1.0 °C. Here the internal gradient matters.

The Biot number compares internal conduction resistance with surface convection resistance. Below about 0.1 a lumped temperature is usually adequate, but it is a screen, not a proof: compare the internal gradient with the rise above the fluid before relying on it.

## Reporting conventions

- Keep the sign convention for the surface condition fixed: heat leaves the slab when T(L) > T∞.
- Report temperatures in °C, fluxes in W/m² and generation in W/m³, and keep at least four significant figures in intermediate values.
- Show the five nodal temperatures and the Simpson weights, not only the result.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Boundary-value solution | Applies symmetry and convection conditions with consistent signs |
| Energy balance | Matches generated heat per area to the surface convective flux |
| Average check | Derives the average and verifies it by Simpson's rule |
| Model selection | Interprets Biot and the internal temperature gradient correctly |
| Limits | Avoids presenting the synthetic slab as a process or biological design |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The slabs, properties and coefficients are synthetic teaching values. The model assumes steady one-dimensional conduction with constant properties and the same uniform convection on both faces, and ignores radiation, edge effects, temperature-dependent properties and any perfusion heat sink. Nothing here is a thermal design, an equipment specification or a statement about any real tissue, device or process. Original guide and rehearsal values: CC BY 4.0, developed with substantial AI assistance.
