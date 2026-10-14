# Integrative project draft: low-frequency differential sensor channel

**Inactive authoring draft for Electrical Circuits & Instrumentation 0.4.6.** This is a paper-design exercise, not a hardware build or scheduled assignment. It has no points, course grade or submission path. All values are constructed specifications; no real sensor, device or subject is represented. Qualified circuit review, workload measurement, accessibility review and activation decisions remain open.

## Design brief

Propose an idealized front end that carries a low-frequency differential sensor signal through an amplifier, one-pole low-pass filter and ADC. The aim is to show how gain, common-mode rejection, source loading, output headroom, filter response, sampling and quantization interact. State any limitation that cannot be resolved from the supplied parameters instead of filling it with an assumed component specification.

Use these fixed classroom assumptions:

| Quantity | Supplied value |
| --- | ---: |
| Differential signal | ±5 mV, bandwidth 0–5 Hz |
| Common-mode input | ±0.5 V |
| Differential source resistance | 1 kΩ |
| Amplifier differential input resistance | 1 MΩ |
| Differential gain and reference | 200 V/V, 2.5 V |
| Common-mode rejection | 80 dB at the stated frequencies |
| Amplifier/ADC output span | 0–5 V, idealized |
| First-order filter | 8.2 kΩ and 1 μF |
| ADC and sample rate | 12 bits over 0–5 V; 100 samples/s |
| Interference check frequency | 50 Hz |

Use $V_{out}=V_{ref}+A_dV_d+A_{cm}V_{cm}$ before the filter, with $A_d=200$ and $A_d/A_{cm}=10^{80/20}$. Treat the filter as $|H(f)|=[1+(f/f_c)^2]^{-1/2}$ with $f_c=(2\pi RC)^{-1}$. Use ADC step size $5/2^{12}$ V. These are ideal model statements, not guaranteed performance for a real part.

## Milestones and deliverables

1. **Loading and gain:** compute the voltage fraction delivered to the 1 MΩ input by a 1 kΩ source. Map the differential range through gain and reference, then include the supplied common-mode error when checking the ideal 0–5 V span.
2. **Common-mode error:** convert 80 dB CMRR to a linear ratio. Calculate common-mode output at the supplied limit and refer that error back to the sensor input; state the comparison basis used.
3. **Filter and sampling:** calculate the RC corner, gain at 5 and 50 Hz, and the Nyquist frequency at 100 samples/s. Explain what the one-pole response does and does not establish about alias rejection.
4. **ADC scale:** calculate the ADC step in volts and the ideal input-referred step through gain 200. Distinguish quantization step from a measured noise floor or effective number of bits.
5. **Design note:** show the signal path and reference levels in a labelled diagram or table with a text alternative. Provide unit-checked equations, a small independent calculation test, and a bounded discussion of unmodeled input range, offset/bias, component tolerances, noise spectrum, output swing, stability and real anti-alias requirements.

## Reviewer-side arithmetic checks

The source-loading factor is $1{,}000{,}000/(1{,}001{,}000)\approx0.9990$. The 80 dB CMRR implies $A_{cm}=0.02$; a ±0.5 V common-mode input contributes up to ±10 mV at the output, equivalent to ±50 μV differential input. The ideal differential output before common-mode error spans 1.5–3.5 V; including that error gives 1.49–3.51 V, still within the assumed 0–5 V range. The filter corner is about 19.4 Hz, with magnitude about 0.968 at 5 Hz and 0.362 at 50 Hz. Nyquist is 50 Hz. One ADC LSB is about 1.221 mV, or 6.10 μV referred through gain 200. These checks are visible because the project is inactive and ungraded; they are not a protected answer key or performance guarantee.

## Draft human rubric

Weights, points, pass thresholds and delivery rules are unset.

| Criterion | Strong evidence | Developing evidence | Little or no evidence |
| --- | --- | --- | --- |
| Signal and loading model | Differential/common-mode variables, source loading and units are applied consistently. | Main model is correct with one loading or unit gap. | Differential and common-mode quantities are conflated. |
| Gain and headroom | Output range includes the specified reference, signal and common-mode contribution. | Nominal gain is correct but a range contribution is omitted. | Clipping/headroom conclusion is wrong or unsupported. |
| CMRR reasoning | Decibels convert to the correct linear ratio and error is referred to a stated basis. | Conversion is mostly correct but the error basis is unclear. | CMRR is treated as a percent or gain is inverted. |
| Filter/sampling | Corner, passband, interference attenuation and Nyquist are calculated with limits stated. | Core calculations are present but alias claims exceed the one-pole evidence. | Sampling or frequency response is materially incorrect. |
| ADC scale | Code step and input-referred step use the stated range, resolution and gain. | A minor scale or terminology gap remains. | Step size is confused with measured noise or effective resolution. |
| Diagram and communication | A readable signal path labels units, reference, filter and sampling, with a text alternative. | Most stages are shown but a label or alternative is missing. | The signal path or ranges cannot be followed. |
| Uncertainty and limits | Missing device/noise/tolerance specifications are identified without inventing a real-world guarantee. | Most limits are bounded, with one unsupported component claim. | The ideal calculation is presented as validated hardware performance. |

Before activation, a qualified reviewer must assess circuit correctness and the rubric; course owners must measure workload and review accessible diagram alternatives and delivery policy. This draft does not authorize component selection, patient connection or a physical experiment. It is not part of the course manifest's scheduled assessments and creates no grade.
