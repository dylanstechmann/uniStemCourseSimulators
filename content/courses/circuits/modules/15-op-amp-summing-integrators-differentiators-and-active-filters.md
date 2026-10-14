# Op-amp signal operations: summing, integrating, differentiating and active filtering

The feedback lesson treated the op amp as a gain block whose feedback network sets the closed-loop gain. The same idea goes further. If the feedback network contains capacitors, or several inputs share one feedback resistor, the stage can add signals, integrate them, differentiate them or filter them, and the op amp's low output impedance keeps the next stage from changing the result. This lesson builds those four operations from one rule and then states the limits that decide whether a real stage behaves as the ideal equations predict. All circuits and values are synthetic teaching models.

The undergraduate [MIT OCW 6.002 Circuits and Electronics (Spring 2007) calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) follows the op-amp abstraction (L21) with multiple inputs and superposition, integrators and differentiators (L22), then feedback stability and oscillators (L23); its recitation R22 covers first- and second-order op-amp filters. This lesson selects the summing, integrating, differentiating and filtering operations for an instrumentation context and leaves oscillators outside. It uses 6.002 as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Analyze an inverting summing amplifier by superposition at the virtual ground and calculate its weighted output.
2. Calculate integrator and differentiator outputs in time and frequency, and explain offset drift, saturation and high-frequency noise gain and the resistor additions that bound them.
3. Design first-order active low-pass and band-pass stages and a unity-gain Sallen–Key low-pass from gain, corner frequency and Q, and check the design against the op amp's gain-bandwidth product.

## One rule for every inverting stage

In an inverting stage the non-inverting input is held at reference, and negative feedback holds the inverting input at nearly the same voltage, a **virtual ground**. No current enters the ideal input, so all current arriving at that node through the input element must leave through the feedback element. Writing input and feedback as impedances Z_in and Z_f gives

**V_out = −(Z_f / Z_in) V_in.**

With two resistors this is the familiar −R_f/R_in. With capacitors, Z = 1/(jωC), and the same rule gives an integrator, a differentiator or a filter. The rule holds only while the output stays inside its range and the loop remains stable; the feedback lesson's checks still apply.

## Summing amplifier

Connect several inputs, each through its own resistor, to the virtual-ground node. Each input current is V_k/R_k, set only by its own voltage and resistor, because the node it feeds is held at reference. The currents add and all flow through R_f:

**V_out = −R_f (V₁/R₁ + V₂/R₂ + …).**

**Synthetic example.** With R_f = 20 kΩ, R₁ = 10 kΩ, R₂ = 40 kΩ, V₁ = +0.20 V and V₂ = −0.40 V, the input currents are 20 μA and −10 μA. Their 10 μA sum gives V_out = −20 kΩ × 10 μA = **−0.20 V**. This is superposition: each input contributes −(R_f/R_k)V_k independently, so the weights are −2 and −0.5. Because the virtual ground isolates the inputs, changing V₁ does not change the current drawn from the V₂ source. That isolation is what makes the summer useful for adding a calibrated offset to a sensor signal or mixing channels with chosen weights. A following inverting stage can restore the sign if needed.

## Integrator

Replace R_f with a capacitor C. The input current V_in/R charges the capacitor, and because one plate sits at virtual ground, the output follows the capacitor voltage with a sign change:

**V_out(t) = V_out(0) − (1/RC) ∫ V_in dt.**

```text
input -- R -- inverting input (virtual ground) -- C -- output
non-inverting input -- reference
```

Description: the input voltage drives a resistor into the inverting input. A capacitor connects that input to the output. The non-inverting input is tied to reference. The text map shows connections, not wiring or pin numbers.

**Synthetic example.** R = 100 kΩ and C = 1 μF give RC = 0.1 s. A constant +0.5 V input produces a ramp of −0.5/0.1 = **−5 V/s**. If the output can swing to −10 V, it saturates after **2.0 s**, after which the integrator equation no longer applies. In frequency terms the gain magnitude is 1/(2πfRC): **0.159** at 10 Hz, unity at **1.59 Hz**, with a +90° phase from the combination of inversion and integration.

**Offset drift.** An ideal integrator has unlimited gain at DC. A tiny constant error, such as a 1 mV input offset, is integrated like a signal: it ramps the output at 1 mV/0.1 s = 10 mV/s and saturates the stage after about 1000 s even with no input. Two common bounds are a reset switch across C and a large resistor R_f in parallel with C. With R_f = 10 MΩ the DC gain is limited to −R_f/R = −100, and the stage integrates only above its corner 1/(2πR_fC) = **0.0159 Hz**. An offset modeled at the non-inverting input then appears at the output multiplied by 1 + R_f/R = 101, about 101 mV, steady rather than ramping. This is a **lossy integrator**, a trade between integration accuracy at low frequency and bounded drift.

## Differentiator

Swap the elements: C at the input and R in feedback. The input current is C dV_in/dt, so

**V_out = −RC dV_in/dt.**

**Synthetic example.** R = 10 kΩ and C = 0.1 μF give RC = 1 ms. A 1 V peak-to-peak triangle wave at 100 Hz has slopes of ±200 V/s, so the output is a square wave of ∓**0.20 V**. In frequency terms the gain magnitude is 2πfRC, which rises without limit: **62.8** at 10 kHz. Wideband noise and fast interference are therefore amplified far more than the wanted signal. The rising gain also meets the op amp's own falling gain, which tends to make the loop ring or oscillate. A practical stage adds a resistor R_s in series with C. With R_s = 1 kΩ, the high-frequency gain is capped at R/R_s = 10 above 1/(2πR_sC) ≈ **1.59 kHz**, and the stage differentiates only below that frequency.

## First-order active filters

Put a capacitor C_f in parallel with R_f. Then Z_f = R_f/(1 + jωR_fC_f), and

**H(jω) = −(R_f/R_in) / (1 + jω R_f C_f),**

an inverting low-pass with DC gain −R_f/R_in and corner f_c = 1/(2πR_fC_f). **Synthetic example:** R_in = 10 kΩ, R_f = 100 kΩ and C_f = 1 nF give DC gain −10 and f_c = **1.59 kHz**. At f_c the magnitude is 10/√2 = 7.07 and the output lags the inverted input by 45°. At 10 kHz it is 10/√(1 + (10/1.59)²) = **1.57**.

Add a capacitor C_in in series with R_in and the input path blocks DC, adding a high-pass corner 1/(2πR_inC_in). With C_in = 10 μF and C_f = 10 nF in the same stage, the corners are **1.59 Hz** and **159 Hz**. Between them the gain is close to −10; at 15.9 Hz, a decade from each corner, it is 10/1.01 = 9.90. Such a band-pass removes a slow baseline and fast noise in one stage.

Unlike a passive RC network, the stage's ideal output impedance is near zero. A load drawing current from the output does not change the network that sets H, so stages can be cascaded without the loading shifts of the [filter-loading lesson](10-filter-loading-baseline-and-recovery.md), provided the output current and swing stay within range.

## A second-order stage without an inductor

A first-order stage falls at 20 dB per decade. The unity-gain **Sallen–Key low-pass** reaches 40 dB per decade with two resistors, two capacitors and a follower. The input passes through R₁ and R₂ in series to the follower's input. C₁ runs from the junction of the resistors to the output, and C₂ runs from the follower input to reference. With R₁ = R₂ = R:

**f₀ = 1/(2πR√(C₁C₂)), Q = ½√(C₁/C₂).**

**Synthetic example:** R = 10 kΩ, C₁ = 20 nF and C₂ = 10 nF give f₀ = **1.13 kHz** and Q = **0.707**, the maximally flat (Butterworth) response. At ten times f₀ the magnitude is about 0.010, a hundredfold reduction, against tenfold for a first-order stage. Q plays the same role as in the [series RLC lesson](14-second-order-rlc-transients-resonance-and-impedance.md): raising C₁/C₂ raises Q, which brings peaking near f₀ and ringing in the step response. Feedback through C₁ supplies the resonance that an inductor would otherwise provide.

## Gain-bandwidth limits

A real op amp's open-loop gain falls with frequency. A common single-pole model gives a nearly constant **gain-bandwidth product** (GBW). The closed-loop bandwidth is then about GBW divided by the **noise gain** 1 + R_f/R_in, not by the signal gain. An inverting gain of −10 has noise gain 11, so with GBW = 1 MHz its bandwidth is about **91 kHz**. A filter designed at 1.59 kHz sits far below that limit, and the ideal equations hold. A filter or differentiator that needs gain near GBW does not. Slew rate, output current and the stability margin of capacitive feedback set further limits that this lesson does not quantify.

## Common mistakes

- Forgetting the inversion: summers, integrators, differentiators and inverting filters all carry a minus sign.
- Assuming one input of a summer changes the current from another; the virtual ground isolates them.
- Building a pure integrator with no DC path and expecting it to hold zero with no input; offsets ramp it into saturation.
- Using a pure differentiator on a noisy sensor signal; its gain rises without bound with frequency.
- Computing closed-loop bandwidth from the signal gain rather than the noise gain.
- Applying the ideal transfer function when the output has saturated or the loop is unstable.

## Worked example

**Problem.** A synthetic sensor signal of a few tens of millivolts contains useful content below 20 Hz and unwanted noise above 1 kHz. Design an inverting active low-pass with DC gain −20 and a corner near 100 Hz using R_in = 10 kΩ, and check it against an op amp with GBW = 1 MHz.

**Step 1: gain.** R_f = 20 × 10 kΩ = 200 kΩ.

**Step 2: corner.** C_f = 1/(2π × 200 kΩ × 100 Hz) = 7.96 nF. Choosing an 8.2 nF standard value gives f_c = 1/(2π × 200 kΩ × 8.2 nF) = **97.0 Hz**.

**Step 3: attenuation.** At 1 kHz the magnitude is 20/√(1 + (1000/97.0)²) = **1.93**, compared with 20 in the passband, about a tenfold relative reduction.

**Step 4: gain-bandwidth check.** The noise gain is 1 + 200/10 = 21, so the closed-loop bandwidth is about 1 MHz/21 = 47.6 kHz, far above the 97 Hz corner. The ideal design holds if the output stays within range: a 50 mV input becomes −1.0 V in the passband.

## Limits of this lesson

All values are synthetic. The analysis assumes an ideal op amp in its linear range with a stable loop, ideal components and a single-pole gain-bandwidth model where stated. Component tolerances, capacitor leakage and dielectric absorption, input bias current through large resistors, slew rate, output current limits and layout parasitics are omitted. Differentiator and capacitive-feedback stability are described qualitatively; phase-margin analysis and oscillator design are not developed. Nothing here is a hardware design, component recommendation or patient-connected circuit. The text maps describe connections and have not had assistive-technology review. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
