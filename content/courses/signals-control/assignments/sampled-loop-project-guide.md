# Sampled-loop portfolio project guide (optional, ungraded)

**Status:** open, optional practice. You can save milestone responses privately in the Case studio; this route is ungraded.
**Introduced in:** course package 0.5.0.
**Suggested time (unvalidated author estimate):** 2–4 hours across weeks 13–14.

## Start here

Sampling, filtering, controller arithmetic and physical state evolution are different operations. This portfolio connects them without hiding their interfaces: a continuous disturbance reaches an analog filter before sampling, the controller forms a candidate command, a bound changes what is applied, and the plant evolves under that held applied value. A timing heuristic and a nominal margin calculation remain conditional checks, not substitutes for an identified model.

Work through the supplied project after the related course readings. First close the model or evidence ledger on paper, then use the separate rehearsal to test your method. The worked example uses different inputs and is a demonstration of the reasoning, not a response to the project. Keep definitions, units, denominators, signs and assumptions visible in your own response. If a check fails, return to the model rather than adjusting a number to match an option.

## Project brief and supplied information

The portfolio deliberately combines separate synthetic pieces rather than asserting that one physical plant has been identified. A disturbance at 3 cycles/min is sampled with Ts = 0.25 min. An analog first-order low-pass has corner 1 cycle/min; also evaluate its response at a desired 0.25 cycles/min.

A separate loop has crossover 1/3 rad/min, stipulated unheld phase margin 70.9 degrees and closed-loop time constant 3 min. Apply the declared ten-samples-per-time-constant heuristic, and approximate hold phase cost as ω_gc Ts/2. This phase cost is an approximation to the zero-order hold below its first frequency-response zero, not a model of all digital implementation delays.

The incremental PI equation is u_candidate[k] = u[k−1] + Kp(e[k]−e[k−1]) + Kp(Ts/Ti)e[k]. Use Kp = 6.667, Ti = 10 min, previous applied output 19.9, previous error 0.9 and current error 1.2. Apply the abstract bound [0,20] and retain the clamped applied output for this exercise’s tracking convention.

For the plant step, use tau = 10 min, gain K = 0.5, Ts = 0.25 min and y[k] = 0. Its exact held-input recurrence is y[k+1] = a y[k] + K(1−a)u_applied[k], where a = exp(−Ts/tau). Sampling and plant quantities use minutes consistently. No command, limit or timing input specifies a real device.

## Milestones and self-review

### Milestone 1: Sampling and aliases

For the project’s 3 cycles/min disturbance and Ts = 0.25 min, calculate sampling, Nyquist and apparent frequency. Demonstrate the ambiguity with a few sampled cosine values and explain why the analog filtering boundary matters.

- Keeps cycles/min distinct from rad/min.
- Checks the alias in the principal interval from zero to Nyquist.
- Explains indistinguishable sampled sequences rather than claiming a digital filter restores lost information.

### Milestone 2: Analog attenuation trade-off

For fc = 1 cycle/min, evaluate the project disturbance at 3 cycles/min and desired component at 0.25 cycles/min. Report amplitude ratios, distinguish them from powers, and explain why the two checks are not a complete anti-alias design.

- Uses the same corner-frequency convention for both components.
- Distinguishes dimensionless amplitude ratio from decibels, power and absolute error.
- States what additional spectrum and tolerance information is missing.

### Milestone 3: Sample-period and hold phase

Check the project’s Ts = 0.25 min against the 3 min closed-loop time constant. At crossover 1/3 rad/min, compute the hold cost in radians and degrees and its effect on the supplied 70.9-degree margin. List timing and modeling omissions.

- Labels the ten-sample criterion as a heuristic rather than a theorem.
- Converts the same phase consistently between radians and degrees.
- Subtracts the phase cost once and keeps the result conditional on omitted delays.

### Milestone 4: Incremental PI and a bounded command

Apply the project’s incremental PI update with Kp = 6.667, Ti = 10 min, Ts = 0.25 min, previous command 19.9 and errors 0.9 then 1.2. Show the candidate, the [0,20] clamp and the value retained under the stated tracking convention.

- Uses both the proportional difference and integral increment.
- Shows candidate, applied and retained values as separate quantities.
- Does not generalize this one-step arithmetic into a validated anti-windup controller.

### Milestone 5: Exact held-input plant and scope

For the project plant with tau = 10 min, gain 0.5 and initial output zero, advance one Ts = 0.25 min interval using the applied PI command. Give an independent limiting-case check and state why the portfolio’s separate stipulated pieces do not identify one real process.

- Uses the exact exponential and applied held command.
- Checks the update against the old state and held-input equilibrium.
- Identifies timing, quantization, actuator and uncertainty evidence the paper model omits.

## Worked example: a separate case

Use different inputs: Ts = 0.1 min and a disturbance at 7 cycles/min. Sampling frequency is 10 cycles/min, Nyquist is 5 cycles/min and the observed alias is |7−10| = 3 cycles/min. The cosine samples agree because their phases differ by whole turns at integer sample times. An analog corner of 2 cycles/min gives disturbance magnitude 1/√(1+3.5²) ≈ 0.2747; a desired 0.5 cycles/min component has magnitude about 0.9701. Neither a later digital filter nor a different label can identify which pre-sampling frequency generated an already aliased record.

For a separate loop with crossover 0.4 rad/min, margin 55 degrees and closed-loop time constant 2 min, the ten-sample bound is Ts ≤ 0.2 min. The chosen step meets it. The hold’s approximate 0.05 min delay costs 0.0200 rad = 1.14592 degrees at crossover, leaving about 53.8541 degrees from the stipulated margin. That subtraction is not a stability certificate when other delays are unknown.

Let the PI inputs be Kp = 3, Ti = 6 min, previous applied command 4.8, previous error 0.2 and current error 0.5, bounded to [0,5]. The candidate is 4.8 + 3(0.3) + 3(0.1/6)(0.5) = 5.725. The plant receives 5 and this specified tracking implementation retains 5. The candidate remains useful as a diagnostic but must not be substituted for the applied value.

For a plant with tau = 3 min, gain 0.4 and old output 0.3, the exact factor is exp(−0.1/3) ≈ 0.967216. The next state is 0.967216×0.3 + 0.4(1−0.967216)×5 ≈ 0.355733. Check independently that it lies between 0.3 and the held-input equilibrium 0.4×5 = 2, moving only a small fraction of that gap in a short interval. This combines the implemented command with the plant model while keeping the sampling, margin and identification assumptions explicit.

## Rehearsal: practice before the project

The [rehearsal parameters](sampled-loop-rehearsal.csv) define a new portfolio. Ts is 0.2 min; disturbance and desired frequencies are 4 and 0.4 cycles/min with an analog corner of 0.8 cycles/min. The separate loop has crossover 0.5 rad/min, stipulated unheld margin 60 degrees and closed-loop time constant 2.5 min. PI values are Kp = 4, Ti = 5 min, prior applied output 7.8 and errors 0.5 then 0.8, bounded to [0,8]. The exact sampled plant has tau = 4 min, K = 0.6 and old output 1. Keep the distinct loop and plant pieces labelled; the file is not an identification record.

Open **Practice gradebook** and choose **Sampled-loop portfolio rehearsal**. Each numeric field names its reporting unit. Enter continuous quantities as bare numbers to three significant figures, using scientific notation when trailing zeros would otherwise hide the intended precision; enter exact counts as whole numbers. Keep extra digits in intermediate calculations. Interpretation choices test the declared model and evidence limits; a correct choice does not demonstrate a complete written argument. The public feedback explains each field and permits unlimited retries.

## Finish and check your report

Include the supplied inputs, your equations or evidence map, intermediate quantities with units, a final table with clearly labelled rows and a short interpretation. For every numerical result, include a second check: substitute into the original relation, verify a conservation balance, compare a limiting case or independently recompute it. For evidence interpretations, name the comparison, design, endpoint, uncertainty and the conclusion that remains unsupported. A diagram or plot needs a plain-text description that preserves its scientific meaning; colour alone must not carry a distinction.

Use the Case studio checklist only after finding the corresponding evidence in your response. Marking a box records your own review; it does not score prose, certify mastery or establish an institutional grade. Disclose spreadsheets, code, references and AI assistance so another reader can distinguish your reasoning from external calculations. Keep a copy of your report and review any discrepancy between your calculation and the public rehearsal feedback before moving on.

| Stage | Focus | Where to work |
| --- | --- | --- |
| Rehearsal | Separate synthetic inputs and public feedback | Practice gradebook: Sampled-loop portfolio rehearsal |
| M1 | Sampling and aliases | Case studio: project milestone 1 |
| M2 | Analog attenuation trade-off | Case studio: project milestone 2 |
| M3 | Sample-period and hold phase | Case studio: project milestone 3 |
| M4 | Incremental PI and a bounded command | Case studio: project milestone 4 |
| M5 | Exact held-input plant and scope | Case studio: project milestone 5 |

## Scope and provenance

Scope comparators: MIT OCW 6.003 Signals and Systems, Fall 2011 syllabus, https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/syllabus/, and 2.004 Dynamics and Control II, Spring 2008 calendar, https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/pages/calendar/. The local readings develop selected sampling, frequency-response, difference-equation and feedback foundations. This portfolio integrates those pieces; full Fourier/discrete-frequency breadth, compensator synthesis and physical implementation remain outside its scope.

The original authoring draft remains a separate proposal for future qualified review; this guide supplies an open practice route without activating that draft as a graded assessment. Workload, scientific quality, assessment design and accessibility have not received independent approval. Original guide, synthetic inputs and rehearsal problems: CC BY 4.0, developed with substantial AI assistance as part of this personal hobby and learning project. No third-party prose, exercise, figure or dataset is reproduced.
