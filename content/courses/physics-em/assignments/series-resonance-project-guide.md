# Series resonance project guide: resonant frequency, quality factor, bandwidth, power and stored energy (optional, ungraded)

**Status:** open, optional and ungraded. Six milestone self-checks in the Case studio save responses privately; nothing is submitted, collected or scored. The separate inactive project draft and its proposed review rubric remain unreviewed and are not served to learners.
**Introduced in:** course package version 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 13 and 14.
**Prerequisite lessons:** [Phasors, loading and measurement inference](../modules/13-phasors-loading-and-measurement-inference.md), [Capacitance, dielectrics and energy boundaries](../modules/08-capacitance-dielectrics-and-energy-boundaries.md) and [Kirchhoff balances, Thevenin models and source loading](../modules/09-kirchhoff-thevenin-and-source-loading.md).

## Purpose

A series RLC circuit driven by a sinusoid responds differently at, above and below one particular frequency. Near that resonance the two reactances nearly cancel, and the current is set almost entirely by the resistor. This project computes the resonant response of three fictional candidates, applies a fictional selection brief, compares average dissipation with the energy shuttling between the inductor and capacitor, and asks what an observed resonance curve alone cannot establish about a physical system.

## The project

All candidates, thresholds and readings are synthetic teaching quantities, not instrument or device specifications. Use an ideal series RLC circuit driven by v_s(t) = V_peak cos(ωt), with peak phasors under the exp(jωt) convention,

\[
Z = R + j\Bigl(\omega L - \frac{1}{\omega C}\Bigr),\qquad
\omega_0 = \frac{1}{\sqrt{LC}},\qquad
Q = \frac{\omega_0 L}{R},\qquad
\Delta\omega = \frac{R}{L},
\]

and the half-power frequencies

\[
\omega_\text{low} = \frac{\sqrt{R^2 + 4L/C} - R}{2L},\qquad
\omega_\text{high} = \frac{\sqrt{R^2 + 4L/C} + R}{2L}.
\]

The three candidates share L = 0.10 H, C = 10 µF and V_peak = 5.0 V and differ only in resistance.

| Candidate | R (Ω) | L (H) | C (µF) | V_peak (V) |
| --- | ---: | ---: | ---: | ---: |
| A | 100 | 0.10 | 10 | 5.0 |
| B | 200 | 0.10 | 10 | 5.0 |
| C | 50 | 0.10 | 10 | 5.0 |

The fictional selection brief requires Q ≥ 1, half-power bandwidth Δω ≤ 1000 rad/s, and peak current at resonance I_peak ≤ 0.080 A. These limits are chosen only to make the paper comparison determinate.

1. Calculate the resonant angular frequency shared by all candidates, and convert it to cycles per second with f₀ = ω₀/(2π).
2. Calculate Q, bandwidth and both half-power frequencies, and the peak and RMS currents at resonance. State which quantities change when only R changes.
3. Calculate the average resistor power at resonance from the RMS current. Compare the maximum magnetic energy L I_peak²/2 with the maximum electric energy C V_C,peak²/2, and state why the two maxima need not occur at the same instant.
4. Apply all three selection limits. Identify the candidate that meets them and the binding failure of each rejected candidate.
5. Calculate the impedance magnitude, source-current peak and phase at ω = 500 rad/s for candidate A. Use the sign of its net reactance to say whether the current leads or lags under the declared convention.
6. Explain which parts of the calculation depend on ideal linear components, and what an observed resonance curve alone cannot establish about a physical system.

## Milestones
Each Case studio milestone lists self-review statements. Responses are saved privately in this application and are never scored.

## Rehearsal circuit

Before the project, work the same steps on a second synthetic series RLC circuit, then check yourself with the open rehearsal practice set, which gives feedback on each value. The rehearsal circuit has R = 64 Ω, L = 0.040 H, C = 4.0 µF and V_peak = 3.0 V. Its responses are not the project candidates' responses.

## Worked example: a third circuit

Take a series RLC circuit with R = 250 Ω, L = 0.010 H, C = 1.0 µF and V_peak = 8.0 V.

1. **Resonant frequency.** ω₀ = 1/√(LC) = 1/√(0.010 × 1.0 µF) = 10,000 rad/s, so f₀ = 10,000/(2π) ≈ 1591.5 Hz.
2. **Quality factor and bandwidth.** Q = ω₀L/R = 100/250 = 0.40, and Δω = R/L = 25,000 rad/s. The half-power frequencies are 10,000 × (√(1 + 1/(4Q²)) − 1/(2Q)) ≈ 3508 rad/s and ≈ 28,508 rad/s, whose difference is the bandwidth.
3. **Power and energy.** At resonance I_peak = 8.0/250 = 0.032 A and I_RMS = 0.032/√2, so the average resistor power is I_RMS² R = 0.128 W. The inductor's maximum energy is ½(0.010)(0.032)² = 5.12 µJ; the capacitor's peak voltage is I_peak/(ω₀C) = 3.2 V, giving the same 5.12 µJ electric maximum. The two maxima sit a quarter-cycle apart, while the resistor dissipates energy every cycle.
4. **Off resonance.** At ω = 50,000 rad/s, ωL = 500 Ω and 1/(ωC) = 20 Ω, so the net reactance is +480 Ω: |Z| = √(250² + 480²) ≈ 541 Ω, I_peak = 8.0/541 ≈ 0.0148 A, and the current lags the voltage by atan(480/250) ≈ 62.5° under the declared convention.

The resonant angular frequency depends only on L and C; Q, bandwidth, the half-power frequencies and the currents all change when R alone changes. Below resonance the net reactance is negative and the current leads; above it the net reactance is positive and the current lags.

## Reporting conventions

- Keep the exp(jωt) phasor convention fixed, and state phase as a lead or a lag under that convention.
- Report angular frequencies in rad/s and frequencies in Hz, currents in amperes and power in watts, keeping at least four significant figures in intermediate values.
- Show the resonant, half-power and off-resonance steps separately, not only the final numbers.
- Disclose any software, spreadsheets or AI assistance you used.

## Self-review rubric

The inactive project draft proposes five criteria for a future human reviewer and assigns them no points. For self-review, mark each criterion 0 (absent), 1 (partly correct) or 2 (complete and consistent with the stated model).

| Criterion | Evidence of a complete response |
| --- | --- |
| Resonance | Computes ω₀, f₀, Q and bandwidth from the declared components |
| Frequency response | Calculates half-power frequencies, impedance magnitude and lead/lag consistently |
| AC power | Distinguishes peak from RMS current and computes average resistor power |
| Energy | Compares electric and magnetic maxima without treating them as simultaneous |
| Scope | Keeps the ideal circuit separate from claims about real devices or instruments |

These marks are a self-check. They are not calibrated, carry no grade and do not stand in for an instructor's judgment.

## Limitations and provenance

The candidates, thresholds and readings are synthetic teaching values. The model assumes ideal linear components, a pure single-frequency source and a single mesh; real inductors add core saturation and winding resistance, real capacitors add loss, and real drives are not single-frequency. Nothing here is an instrument specification, a filter design or a device-safety claim, and the fictional selection brief selects a paper candidate only. Original guide and rehearsal values: CC BY 4.0, developed with substantial AI assistance.

| Milestone | Suggested week | Task | Where to check yourself |
| --- | --- | --- | --- |
| Rehearsal | 13 | Work the rehearsal circuit, then use the open rehearsal practice set | **Practice gradebook**: Series-resonance rehearsal |
| M1 | 13 | Resonant frequency, in radians per second and in hertz (task 1) | Case studio: project milestone 1 |
| M2 | 13 | Q, bandwidth, half-power frequencies and currents (task 2) | Case studio: project milestone 2 |
| M3 | 13 | Average power and the two stored-energy maxima (task 3) | Case studio: project milestone 3 |
| M4 | 14 | Applying the fictional selection brief (task 4) | Case studio: project milestone 4 |
| M5 | 14 | Off-resonance impedance and lead/lag (task 5) | Case studio: project milestone 5 |
| M6 | 14 | Ideal-model scope (task 6) | Case studio: project milestone 6 |