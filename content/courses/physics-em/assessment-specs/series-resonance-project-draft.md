# Series resonance and energy: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. The RLC candidates and selection thresholds are fictional mathematical inputs, not an instrument specification or device recommendation.

## Declared model

Use an ideal series `RLC` circuit driven by `v_s(t)=V_peak cos(omega t)`, with peak phasors under the `exp(j omega t)` convention. Candidate component values are listed in the [candidate table](series-rlc-candidates.csv). Use

`Z = R + j(omega L - 1/(omega C))`,
`omega_0 = 1/sqrt(LC)`,
`Q = omega_0 L/R`,
`Delta omega = R/L`,

and the half-power frequencies

`omega_low = [sqrt(R^2+4L/C)-R]/(2L)`,
`omega_high = [sqrt(R^2+4L/C)+R]/(2L)`.

For the fictional selection brief, require `Q >= 1`, half-power bandwidth `Delta omega <= 1000 rad/s`, and peak current at resonance `I_peak <= 0.080 A`. These limits are chosen only to make the paper comparison determinate.

## Work sequence

1. Calculate the resonant angular frequency for all candidates and convert it to cycles per second using `f_0=omega_0/(2 pi)`.
2. Calculate `Q`, bandwidth, both half-power frequencies, and the peak and RMS currents at resonance. State which variables change when only `R` changes.
3. Calculate average resistor power at resonance from RMS current. At resonance, compare the maximum magnetic energy `L I_peak^2/2` with the maximum electric energy `C V_C,peak^2/2`; state why the maxima need not occur at the same instant.
4. Apply all three selection limits. Identify the candidate that meets them and the binding failure for each rejected candidate.
5. Calculate impedance magnitude, source-current peak and phase at `omega=500 rad/s` for candidate A. Use the sign of its net reactance to identify whether the current leads or lags under the declared convention.
6. Explain which parts of the calculation depend on ideal linear components and what an observed resonance curve alone cannot establish about a physical system.

## Author calculation key

All candidates have `omega_0=1000 rad/s` and `f_0≈159.155 Hz`. Their resonance results are:

| Candidate | `Q` | Bandwidth (rad/s) | `omega_low` (rad/s) | `omega_high` (rad/s) | `I_peak` at resonance (A) | Average resistor power (W) | Maximum stored energy in either reactive element (J) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 1.0 | 1000 | 618.034 | 1618.034 | 0.050 | 0.125 | 0.000125 |
| B | 0.5 | 2000 | 414.214 | 2414.214 | 0.025 | 0.0625 | 0.00003125 |
| C | 2.0 | 500 | 780.776 | 1280.776 | 0.100 | 0.250 | 0.000500 |

Only A meets all three stipulated limits. B fails the minimum `Q` and maximum bandwidth; C exceeds the peak-current limit. At `omega=500 rad/s` for A, the net reactance is `-150 ohm`, so `|Z|=sqrt(100^2+150^2)≈180.278 ohm`. The source-current peak is about `0.027735 A`, and current leads voltage by `atan(1.5)≈56.310 degrees` under the stated convention.

At resonance, candidate A has `I_RMS=0.050/sqrt(2)≈0.035355 A`. Average resistor power is `I_RMS^2 R=0.125 W`. The inductor's maximum energy is `0.5(0.1)(0.05)^2=125 microjoules`. The capacitor peak voltage is `I_peak/(omega_0 C)=5.0 V`, giving the same maximum electric energy, `0.5(10 microfarad)(5.0)^2=125 microjoules`. These two maximum stored energies are equal for the stipulated ideal series resonance, while the resistor dissipates energy over cycles.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Resonance | Computes `omega_0`, `Q` and bandwidth from the declared components |
| Frequency response | Calculates half-power points, impedance magnitude and lead/lag consistently |
| AC power | Distinguishes peak from RMS current and computes average resistor power |
| Energy | Compares electric and magnetic energy maxima without treating them as simultaneous |
| Scope | Keeps the ideal circuit separate from claims about real devices or instruments |

The rubric has no point weights or automatic prose grader. Mathematical accuracy, instructional design, accessibility and workload need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and complete laboratory sequence are addressed.

## Provenance

Original authoring and fictional parameters, CC BY 4.0, developed with substantial AI assistance. No third-party data or laboratory procedures are included.
