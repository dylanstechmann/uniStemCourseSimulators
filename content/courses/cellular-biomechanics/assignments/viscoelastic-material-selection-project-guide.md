# Viscoelastic project guide: choosing a material model across loading time scales (optional, ungraded)

**Status:** open, optional and ungraded. Five milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.4.0.
**Suggested time (unvalidated author estimate):** 3–5 hours across weeks 13 and 14.
**Prerequisite lessons:** [Stress, strain, and constitutive behavior](../modules/01-stress-strain-and-constitutive-behavior.md), [Measuring how stiff a cell is: Hertz indentation and viscoelasticity](../modules/05-hertz-indentation-and-viscoelasticity.md) and [Oscillatory rheology: storage and loss moduli of a viscoelastic gel](../modules/07-oscillatory-rheology-storage-and-loss-moduli.md).
**Data:** the [project candidate table](../assessment-specs/viscoelastic-material-candidates.csv) and the [rehearsal candidate table](viscoelastic-rehearsal-candidates.csv).

## Purpose

A viscoelastic material has no single stiffness. It resists a sudden load more than a slow one, and under oscillation it both stores and dissipates energy, in proportions that depend on frequency. The project compares three fictional material models across those time scales, applies stated thresholds, and keeps a model-based material choice separate from any claim about how cells would respond.

## The project

Candidates A, B and C are mathematical teaching models, not real gels, tissues or cell substrates. Each follows a standard linear solid, with E_inf and E_1 in kPa, τ in seconds and angular frequency ω in rad/s:

\[
E(t)=E_\infty+E_1e^{-t/\tau},\qquad E'(\omega)=E_\infty+E_1\frac{(\omega\tau)^2}{1+(\omega\tau)^2},\qquad E''(\omega)=E_1\frac{\omega\tau}{1+(\omega\tau)^2}.
\]

The candidate table gives each candidate's equilibrium modulus E_inf, relaxing modulus E_1 and relaxation time τ. Assume small-amplitude linear response at a fixed temperature. For this fictional exercise, a candidate should have an equilibrium stress no greater than 0.25 kPa under a held strain of 0.050, a storage modulus of at least 8.0 kPa at ω = 1 rad/s, and a loss tangent E″/E′ no greater than 0.15 at that frequency.

1. Compute each instantaneous modulus E(0) = E_inf + E_1 and equilibrium modulus. Rank the candidates in each limit and explain why a single stiffness label cannot represent both.
2. Under a step strain of 0.050, calculate the stress at t = 5.0 s and as t tends to infinity for each candidate, in kPa.
3. Calculate E′, E″ and tan δ for each candidate at ω = 0.010 rad/s and ω = 1.00 rad/s. Explain the change in the storage-modulus ranking across time scales.
4. Apply the thresholds, identify which candidate or candidates satisfy every requirement, and report the binding criterion for each rejected candidate.
5. At ω = 1 rad/s and strain amplitude ε₀ = 0.030, calculate the dissipated energy density per cycle, W = π E″ ε₀², converting from kPa to J/m³. Compare energy loss with the stored response; do not treat either as a cell outcome.
6. State at least two model assumptions a qualified reviewer would want examined before applying the calculation to measurements, and name a measurement that could test each, without proposing a protocol.
7. Separate the material-model conclusion from a mechanobiology conclusion. The stipulated models cannot establish how any cell would signal, adhere, grow or differentiate.

## Milestones

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 13 | Work the rehearsal candidates, then use the open rehearsal practice set | **Practice gradebook**: Viscoelastic project rehearsal |
| M1 | 13 | Instantaneous and equilibrium moduli, relaxation stresses (tasks 1–2) | Case studio: project milestone 1 |
| M2 | 13 | Storage and loss moduli at two frequencies (task 3) | Case studio: project milestone 2 |
| M3 | 13 | Thresholds and binding criteria (task 4) | Case studio: project milestone 3 |
| M4 | 14 | Dissipated energy density (task 5) | Case studio: project milestone 4 |
| M5 | 14 | Assumptions, tests and scope (tasks 6–7) | Case studio: project milestone 5 |

Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal candidates

The [rehearsal table](viscoelastic-rehearsal-candidates.csv) has the same columns and two candidates, P and Q, examined at different conditions: a step strain of 0.040 read at t = 2.0 s, frequencies of 0.05 and 2.0 rad/s, a strain amplitude of 0.020, and thresholds of at most 0.15 kPa equilibrium stress, at least 6.0 kPa storage modulus at 2.0 rad/s and a loss tangent of at most 0.35 there. Work the same steps on it, then check yourself with the open rehearsal practice set, which gives feedback on each value. Its candidates and conditions differ from the project's, so its answers are not the project's answers.

## Worked example: one more candidate

Take a separate fictional candidate X with E_inf = 0.5 kPa, E_1 = 5 kPa and τ = 2 s.

1. **Two limits.** E(0) = 0.5 + 5 = 5.5 kPa resists a sudden load, but only E_inf = 0.5 kPa remains once the material has relaxed, eleven times less.
2. **Relaxation.** Under a step strain of 0.040, the stress at 2.0 s is 0.040 × (0.5 + 5e^(−1)) ≈ 0.0936 kPa, falling toward 0.040 × 0.5 = 0.0200 kPa.
3. **Two frequencies.** At ω = 0.05 rad/s, ωτ = 0.1, so E′ ≈ 0.5495 kPa and E″ ≈ 0.4950 kPa: X is soft and dissipates almost as much as it stores. At ω = 2.0 rad/s, ωτ = 4, so E′ = 0.5 + 5 × 16/17 ≈ 5.206 kPa and E″ = 5 × 4/17 ≈ 1.176 kPa, a loss tangent of about 0.226.
4. **Energy.** At ω = 2.0 rad/s and ε₀ = 0.020, W = π × 1176 Pa × 0.020² ≈ 1.478 J/m³, using 1 Pa = 1 J/m³.

The same material looks soft or stiff depending on how quickly it is loaded: ωτ, not the moduli alone, decides which regime applies.

## Reporting conventions

- Keep stresses and moduli in kPa and energy densities in J/m³, and say which frequency or time each value belongs to.
- Keep at least four significant figures in intermediate values and round only reported results.
- Report every threshold check separately, and name the binding criterion for each rejected candidate.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Time-scale reasoning | Distinguishes instantaneous, equilibrium and frequency-dependent moduli |
| Calculation | Computes relaxation stress, complex moduli, loss tangent and energy density with units |
| Decision | Applies all thresholds and identifies trade-offs without substituting one modulus for another |
| Assumptions | Names limits of the single-relaxation-time linear model and an appropriate check |
| Scope | Keeps the model-based material choice separate from claims about cell behavior or real materials |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The candidates, thresholds and conditions are synthetic teaching values. The standard linear solid has a single relaxation time and assumes linear, small-strain response at fixed temperature; real gels and tissues can show several relaxation processes, poroelastic flow, nonlinearity and damage. Nothing here is a material specification, a substrate recommendation or a prediction about any cell. Original guide and synthetic rehearsal data: CC BY 4.0, developed with substantial AI assistance.
