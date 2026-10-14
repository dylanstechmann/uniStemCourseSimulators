# Abstract gas equilibrium portfolio: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. `A` and `B` are fictional stoichiometric tokens, not chemical species, and the numerical inputs do not describe a real reaction, apparatus or process.

## Purpose and stipulated model

Connect reaction extent, atom accounting, the reaction quotient, equilibrium and enthalpy at fixed temperature. Consider the abstract relation `A(g) ⇌ 2B(g)`. Each A token contains two conserved units and each B token contains one. The initial amounts are `n_A,0=1.00 mol` and `n_B,0=0.500 mol`. Define the extent `ξ` in mol so

\[
n_A=1.00-\xi,\qquad n_B=0.500+2\xi.
\]

For this mathematical case only, idealized activities are `a_i=β n_i` with stipulated `β=0.200 mol⁻¹`; the dimensionless equilibrium constant at the fixed temperature is `K_p=a_B²/a_A=1.80`. Use an abstract reaction enthalpy `ΔH=+20.0 kJ/mol of extent`. No compound identity, temperature-dependence, or physical vessel is supplied.

## Work sequence

1. State the feasible interval for `ξ` and verify that the conserved-unit count is 2.50 mol before and after reaction.
2. Calculate the initial reaction quotient `Q_p`; use `Q_p` versus `K_p` to predict the direction of net change.
3. Substitute the extent table into the equilibrium expression, rearrange to a quadratic, solve it and reject any root outside the feasible interval.
4. Calculate the equilibrium amounts of A and B and verify both nonnegativity and the conserved-unit count.
5. Calculate the heat absorbed or released at fixed temperature using the stated sign convention, and report sensible significant figures.
6. Explain why equilibrium composition and reaction enthalpy do not determine reaction rate, prove chemical identity or provide a laboratory procedure.

## Author calculation key

The feasible interval is `0≤ξ≤1.00 mol`, set by the initial A amount. Initially, `Q_p=β(0.500)²/1.00=0.0500<K_p`, so the net direction is forward. At equilibrium,

\[
1.80=\frac{0.200(0.500+2\xi)^2}{1.00-\xi},\qquad
4\xi^2+11\xi-8.75=0.
\]

The admissible root is `ξ=(-11+√261)/8=0.6444368 mol`; the other root is negative and infeasible. Thus `n_A=0.355563 mol` and `n_B=1.788874 mol`. The conserved-unit count is `2n_A+n_B=2.500000 mol`, matching the initial total. With heat into the system positive, `q=ξΔH=+12.8887 kJ`, so the stipulated endothermic extent absorbs heat at fixed temperature. These values are checks on the abstract equations only.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Stoichiometric extent | Writes species amounts with correct coefficients and feasible bounds |
| Conservation | Verifies the conserved-unit total before and after reaction |
| Equilibrium | Computes `Q_p`, sets the mass-action expression and selects the admissible root |
| Thermochemistry | Applies the stated extent basis and heat sign convention |
| Scope | Does not infer rate, identity or real chemical handling from the fictional model |

The rubric has no point weights or automatic prose grader. Workload, accessibility, chemical accuracy and instructional design need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and synthetic mathematical inputs, CC BY 4.0, developed with substantial AI assistance. No third-party dataset or real-world procedure is included.
