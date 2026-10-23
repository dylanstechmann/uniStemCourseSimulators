# Sensor-channel budget project guide (optional, ungraded)

**Status:** open, optional practice. You can save milestone responses privately in the Case studio; this route is ungraded.
**Introduced in:** course package 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 13–14.

## Start here

A channel can fit a nominal range and still fail as a measurement system. This project makes the bookkeeping explicit: distinguish a source voltage from a loaded terminal voltage, separate differential gain from common-mode gain, and keep amplitude response, sampled representation and code scale in different columns. The useful result is a connected error and range budget with unresolved specifications identified, rather than a list of individually correct but incompatible calculations.

Work through the supplied project after the related course readings. First close the model or evidence ledger on paper, then use the separate rehearsal to test your method. The worked example uses different inputs and is a demonstration of the reasoning, not a response to the project. Keep definitions, units, denominators, signs and assumptions visible in your own response. If a check fails, return to the model rather than adjusting a number to match an option.

## Project brief and supplied information

Use the ideal low-frequency differential channel already proposed by this course. The supplied differential terminal signal is ±5 mV over 0–5 Hz, common mode is ±0.5 V, source resistance is 1 kΩ and differential input resistance is 1 MΩ. Differential gain is 200 V/V about a 2.5 V reference; CMRR is 80 dB over the stated band. The ideal amplifier/ADC span is 0–5 V. An 8.2 kΩ, 1 µF one-pole low-pass precedes a 12-bit ADC sampled at 100 samples/s. Evaluate interference at 50 Hz.

Use V_out = V_ref + A_d V_d + A_cm V_cm, with A_d/A_cm = 10^(CMRR/20). Use f_c = 1/(2πRC), |H(f)| = 1/√(1+(f/f_c)²), and code step = span/2^bits. The terminal differential amplitude is the basis of the nominal headroom calculation; compute the loading factor separately, and show the small change if the quoted amplitude instead describes the open-circuit source. This explicit distinction prevents loading from being silently counted twice. No input-range, current-drive, component-tolerance or noise specification may be invented. The original draft remains ungraded and is not scheduled, submitted or graded.

## Milestones and self-review

### Milestone 1: Loading and gain

For the project, calculate the 1 MΩ/(1 MΩ+1 kΩ) loading fraction. Treat ±5 mV as the declared amplifier-terminal differential range for the nominal gain/reference check. Also report what changes if ±5 mV instead names the open-circuit source.

- Labels open-circuit and terminal voltages separately.
- Calculates loading from both resistances and keeps its factor dimensionless.
- Maps the terminal signal about the 2.5 V reference before adding other errors.

### Milestone 2: Common-mode error and headroom

For gain 200 and 80 dB CMRR, calculate common-mode gain and the output contribution of ±0.5 V. Refer it to the amplifier differential input, then screen the declared 0–5 V output span with worst-case signs.

- Uses 20 log10 for the gain ratio rather than treating decibels as a percentage.
- Divides the output error by differential gain to state its input basis.
- Includes reference, differential signal and common-mode contribution in both extremes.

### Milestone 3: Filter response and sampling

For the project’s 8.2 kΩ, 1 µF filter, compute the corner and amplitude ratios at 5 and 50 Hz. Compare with the 100 samples/s Nyquist frequency. State the additional spectrum and error information needed for an alias budget.

- Uses f in cycles/s consistently with the RC corner formula.
- Reports desired-signal attenuation as well as disturbance attenuation.
- Keeps a finite one-pole attenuation distinct from complete alias prevention.

### Milestone 4: ADC and input-referred scale

For the project’s 12-bit 0–5 V ADC, compute the output step and the step referred through gain 200. State whether the reference point is the amplifier input or the unloaded source, and identify what remains unknown about effective resolution.

- Uses the full span divided by 2^bits under the stated ideal quantizer convention.
- Names the input node and gain used for referral.
- Does not equate a code step with measured noise, accuracy or effective bits.

### Milestone 5: Communicate the channel and its limits

Assemble a labelled signal-path table or diagram with a plain-text alternative. Include loading, gain/reference, common-mode error, filtering, sampling and quantization. List unmodeled offset/bias, noise, swing/current, input range, tolerances and stability, and add one independent numerical check.

- A reader can follow each node’s units, voltage basis and reference.
- An independent check tests a balance or limiting case rather than repeating a calculator display.
- The report keeps its ideal comparison separate from hardware or subject-use claims.

## Worked example: a separate case

Consider a different channel with an **open-circuit** source amplitude of ±4 mV, R_s = 2 kΩ, R_in = 200 kΩ, gain 100, reference 1.65 V and ideal span 0–3.3 V. Its CMRR is 60 dB and common-mode magnitude is 0.3 V. First write the input basis: the divider gives 200/(200+2) = 0.990099, so the amplifier sees ±3.960396 mV. Multiplying that terminal amplitude by gain gives ±0.3960396 V.

The linear CMRR is 1000, so common-mode gain is 100/1000 = 0.1. The worst-case common-mode contribution is ±0.0300 V. Independent signs therefore give extrema 1.65 − 0.3960396 − 0.0300 = 1.2239604 V and 1.65 + 0.3960396 + 0.0300 = 2.0760396 V. Both fit the stipulated span, but this is conditional arithmetic: no real amplifier’s common-mode input range or output-current capability has been supplied. The error referred to the **amplifier input** is 0.0300/100 = 300 µV; referring to the open-circuit source would additionally divide by the loading factor.

For a separate 20 kΩ, 0.5 µF one-pole filter, RC = 0.0100 s and f_c ≈ 15.9 Hz. At 3 Hz the magnitude is about 0.983; at 60 Hz it is about 0.256. A 120 samples/s sampler places Nyquist at 60 Hz, but the filter leaves a finite component there. Without a disturbance amplitude and error allowance, that attenuation cannot be judged sufficient.

A 10-bit converter over 0–3.3 V has a code step of 3.22265625 mV, or 32.2265625 µV referred through gain 100 to the amplifier input. This number is a scale conversion; it does not measure RMS noise. As an independent check, multiplying the input-referred step back by 100 must recover the output step. Label that check separately from the headroom check, since one concerns scale while the other concerns range.

## Rehearsal: practice before the project

The [rehearsal input table](sensor-channel-rehearsal.csv) pins a different channel: terminal differential signal ±8 mV, R_s = 5 kΩ, R_in = 500 kΩ, differential gain 80, reference 2.00 V and common mode ±0.4 V with 66 dB CMRR. The filter is 10 kΩ with 2 µF. Evaluate it at a desired 2 Hz and a 40 Hz disturbance; the 11-bit converter spans 0–4 V at 80 samples/s. Calculate loading, nominal range, common-mode error on two bases, both filter magnitudes, Nyquist and code scale. Then explain which physical performance claims remain unresolved. These are not the project inputs.

Open **Practice gradebook** and choose **Sensor-channel budget rehearsal**. Each numeric field names its reporting unit. Enter continuous quantities as bare numbers to three significant figures, using scientific notation when trailing zeros would otherwise hide the intended precision; enter exact counts as whole numbers. Keep extra digits in intermediate calculations. Interpretation choices test the declared model and evidence limits; a correct choice does not demonstrate a complete written argument. The public feedback explains each field and permits unlimited retries.

## Finish and check your report

Include the supplied inputs, your equations or evidence map, intermediate quantities with units, a final table with clearly labelled rows and a short interpretation. For every numerical result, include a second check: substitute into the original relation, verify a conservation balance, compare a limiting case or independently recompute it. For evidence interpretations, name the comparison, design, endpoint, uncertainty and the conclusion that remains unsupported. A diagram or plot needs a plain-text description that preserves its scientific meaning; colour alone must not carry a distinction.

Use the Case studio checklist only after finding the corresponding evidence in your response. Marking a box records your own review; it does not score prose, certify mastery or establish an institutional grade. Disclose spreadsheets, code, references and AI assistance so another reader can distinguish your reasoning from external calculations. Keep a copy of your report and review any discrepancy between your calculation and the public rehearsal feedback before moving on.

| Stage | Focus | Where to work |
| --- | --- | --- |
| Rehearsal | Separate synthetic inputs and public feedback | Practice gradebook: Sensor-channel budget rehearsal |
| M1 | Loading and gain | Case studio: project milestone 1 |
| M2 | Common-mode error and headroom | Case studio: project milestone 2 |
| M3 | Filter response and sampling | Case studio: project milestone 3 |
| M4 | ADC and input-referred scale | Case studio: project milestone 4 |
| M5 | Communicate the channel and its limits | Case studio: project milestone 5 |

## Scope and provenance

Scope comparator: MIT OCW 6.002 Circuits and Electronics, Spring 2007 calendar, https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/. The local readings cover selected lumped networks, amplification, frequency response and feedback topics corresponding to L1–3 and L18–23. This project integrates those foundations with the local measurement strand. MOS-device, digital-logic and hardware-laboratory depth remain outside this project; it does not complete the broader MIT course.

The original authoring draft remains a separate proposal for future qualified review; this guide supplies an open practice route without activating that draft as a graded assessment. Workload, scientific quality, assessment design and accessibility have not received independent approval. Original guide, synthetic inputs and rehearsal problems: CC BY 4.0, developed with substantial AI assistance as part of this personal hobby and learning project. No third-party prose, exercise, figure or dataset is reproduced.
