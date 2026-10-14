# Sampled-loop design portfolio: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. The signals, plant, controller and limits below are synthetic calculations, not recommendations or settings for any real device or process.

## Purpose and outcomes

Connect frequency aliasing, anti-alias filtering, hold delay, sample-period selection, a discrete PI update and a sampled first-order plant. The exercise complements the step-identification lab and the week-14 sensor-filter case, which cover different questions.

## Given synthetic model

- A sampled disturbance has frequency `f_d=3 cycles/min`; the sampler uses `T_s=0.25 min`.
- A first-order analog low-pass filter has corner frequency `f_c=1 cycle/min`.
- A separate loop has gain crossover `ω_gc=1/3 rad/min`, an unheld phase margin of `70.9°`, and a closed-loop time constant of `3 min`.
- A discrete PI controller uses `K_p=6.667`, `T_i=10 min`, and the incremental update
  `u[k]=u[k−1]+K_p(e[k]−e[k−1])+K_p(T_s/T_i)e[k]`.
  Use `u[k−1]=19.9`, `e[k−1]=0.9`, `e[k]=1.2`, and an abstract command bound `0≤u≤20`.
- For the sampled plant, use `τ=10 min`, `K=0.5`, `T_s=0.25 min`, `y[k]=0` and the applied held command from the PI step.

These stipulated pieces form a deliberately compact teaching portfolio; no claim is made that they are one identified or physically validated plant.

## Work sequence

1. Compute the sampling frequency, Nyquist frequency and apparent alias of the 3 cycles/min component. Explain why filtering after sampling cannot recover its original frequency.
2. Calculate the first-order analog filter's amplitude ratio at the disturbance and at a desired 0.25 cycles/min signal. Interpret the two results as a trade-off, not as a complete filter design.
3. Check the ten-samples-per-closed-loop-time-constant rule. Compute the zero-order-hold phase lag at crossover in radians and degrees, then subtract it from the stipulated unheld phase margin.
4. Apply the incremental PI update. Clamp the candidate command to `[0,20]` and state which value must be retained as the actual applied output for anti-windup.
5. Compute `a=exp(−T_s/τ)` and the exact sampled-plant update `y[k+1]=a y[k]+K(1−a)u[k]`.
6. List timing or hardware effects omitted from this arithmetic, and state why no deployment conclusion follows from it.

## Author calculation key

The sampling frequency is `f_s=4/min`, so Nyquist is `2/min` and the apparent frequency is `|3−4|=1/min`. A digital filter cannot distinguish this alias from a true 1/min signal. The analog amplitude ratios are `1/sqrt(1+(3/1)^2)=0.316228` at the disturbance and `1/sqrt(1+(0.25/1)^2)=0.970143` at the desired component.

The rule gives `T_s≤3/10=0.3 min`; the chosen 0.25 min meets it. The hold delay is `T_s/2=0.125 min`, with phase cost `(1/3)(0.125)=0.041667 rad=2.387°`, leaving about `68.513°` from the stipulated 70.9° margin.

The PI candidate is `19.9 + 6.667(0.3) + 6.667(0.025)(1.2)=22.10011`. After clamping, the applied and stored output is `20`. The exact plant factor is `a=e^(−0.025)=0.975310`; from `y[k]=0`, the next state is `0.5(1−a)(20)=0.246901` in the model's output scale.

The answer omits computation delay, jitter, quantization, actuator dynamics, unmodeled poles, uncertainty, saturation duration and validation evidence. Its calculations do not establish a safe sample rate, controller or filter for a real device.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Sampling | Computes Nyquist and alias frequency with consistent cycles/min units |
| Filtering | Computes the two amplitude ratios and respects the analog-before-sampling boundary |
| Margin | Converts the hold phase consistently and updates the stated margin |
| Discrete PI | Uses the incremental equation and stores the clamped applied command |
| Plant update | Uses the exact zero-order-hold recurrence and identifies omitted effects |
| Limits | Avoids presenting the synthetic calculation as device guidance |

The rubric has no point weights or automatic prose grader. Workload, accessibility, mathematical accuracy and instructional design need qualified review. The project remains inactive until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and synthetic values, CC BY 4.0, developed with substantial AI assistance. No third-party dataset or real-world procedure is included.
