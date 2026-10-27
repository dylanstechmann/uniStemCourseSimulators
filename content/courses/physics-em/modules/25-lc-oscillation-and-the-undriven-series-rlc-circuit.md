# LC oscillation and the undriven series RLC circuit

The [inductor-energy lesson](12-induction-lenz-and-inductor-energy.md) showed that an inductor stores a current state, and the [RC switching lesson](10-rc-switching-initial-conditions-and-energy.md) that a capacitor stores a voltage state. Connect a charged capacitor to an inductor and the two states trade places. Charge drains from the capacitor into a growing current, the current recharges the capacitor with the opposite polarity, and the exchange repeats. This lesson develops that oscillation, adds resistance, and classifies the three kinds of natural response a series RLC loop can show. All components, voltages and times are synthetic teaching values.

The [MIT OCW 8.02 Physics II: Electricity and Magnetism (Spring 2007) class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) give session 27 to LC and undriven LRC circuits, after RL circuits and before driven LRC circuits, and [Open Yale Courses PHYS 201](https://oyc.yale.edu/physics/phys-201) gives two lectures to LCR circuits, first with DC and then with AC voltage. Both are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Derive the LC equation from the loop rule and the element laws, and calculate the oscillation frequency, period and the charge and current amplitudes from stated initial conditions.
2. Track how energy moves between the capacitor's electric field and the inductor's magnetic field, and use energy conservation to check amplitudes and timing.
3. Classify a series RLC circuit's natural response as underdamped, critically damped or overdamped, and calculate its decay rate, damped frequency, quality factor and the energy left after each period.

## Two storage elements in one loop

A capacitor C is charged to V₀, so it holds q₀ = CV₀, and an ideal inductor L carries no current. An ideal switch joins them at t = 0. Let q be the charge on the plate that starts positive and i = dq/dt the current into that plate. The capacitor contributes q/C around the loop and the inductor L di/dt, so the loop rule gives

\[
L\frac{di}{dt} + \frac{q}{C} = 0 \qquad\Longrightarrow\qquad \frac{d^2q}{dt^2} = -\frac{1}{LC}\,q .
\]

The charge accelerates back toward zero in proportion to how far it is from zero, exactly as a mass on a spring does, so the solutions oscillate at the angular frequency

\[
\omega_0 = \frac{1}{\sqrt{LC}} .
\]

Two continuity rules from earlier lessons fix the constants. The capacitor's charge cannot jump, so q = q₀ just after the switch closes, and the inductor's current cannot jump, so i = 0 then. Therefore

\[
q(t) = q_0\cos\omega_0 t,\qquad i(t) = -\omega_0 q_0\sin\omega_0 t .
\]

Take L = 25 mH, C = 2.5 µF and V₀ = 12 V. Then LC = 6.25 × 10⁻⁸ s², ω₀ = 4000 rad/s, f₀ = ω₀/2π = 636.6 Hz and the period is T = 1.571 ms. The capacitor starts with q₀ = 30 µC, and the current amplitude is ω₀q₀ = 0.120 A. The same amplitude follows from V₀/√(L/C), with √(L/C) = 100 Ω, the ratio of voltage amplitude to current amplitude in this loop.

The timeline is worth tracing. The current starts at zero but not with zero slope: the whole capacitor voltage appears across the inductor, so the current begins changing at |di/dt| = V₀/L = 480 A/s. The current magnitude peaks at T/4 = 0.393 ms, when the capacitor is momentarily uncharged. At T/2 = 0.785 ms the capacitor holds −q₀, the reversed polarity, and the current is zero again. At T the circuit is back in its starting state.

## Energy moves between two fields

The capacitor stores q²/2C in the electric field between its plates, and the inductor stores Li²/2 in the magnetic field of its coil. Substituting the solutions,

\[
U_C = U\cos^2\omega_0 t,\qquad U_L = U\sin^2\omega_0 t,\qquad U = \frac{q_0^2}{2C} = \tfrac12 CV_0^2 .
\]

The coefficients match because Lω₀² = 1/C, so the total stays at U = 180 µJ for the example. As a check, the inductor's energy at the current peak, ½ × 0.025 × 0.120², is also 180 µJ. Each share oscillates at **2ω₀**, since cos² ω₀t = (1 + cos 2ω₀t)/2, and each averages U/2 over a cycle. The shares are first equal at T/8 = 0.196 ms, when |q| = q₀/√2 = 21.2 µC.

In this ideal lumped model no energy leaves the loop: electric-field energy between the plates and magnetic-field energy inside the coil simply take turns. Fields that carry energy away belong to the [radiating-source lesson](radiating-sheet-reflection-and-standing-energy.md); a real circuit loses a little that way, which this model ignores. The mechanical analogy is exact. Inductance plays the role of mass, 1/C of spring stiffness, charge of displacement and current of velocity, so Li²/2 is the counterpart of kinetic energy and q²/2C of spring energy. The [Mechanics oscillations lesson](../../physics-mechanics/modules/11-oscillations-damping-and-energy-balance.md) develops the same mathematics for a physical oscillator.

## Adding resistance

Put a resistor R in the same loop. The loop rule becomes

\[
L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{q}{C} = 0 ,
\]

and the resistor converts stored energy to heat at the rate i²R, so the total stored energy can only fall. Trying \(q = e^{st}\) gives Ls² + Rs + 1/C = 0, whose roots are

\[
s = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2},\qquad \alpha = \frac{R}{2L} .
\]

What happens depends on R compared with the **critical resistance** \(R_c = 2\sqrt{L/C}\), which is where α = ω₀. For release from rest, with q = q₀ and i = 0 at t = 0:

- **Underdamped**, \(R < R_c\): \(q = q_0 e^{-\alpha t}\left(\cos\omega_d t + \frac{\alpha}{\omega_d}\sin\omega_d t\right)\), with damped angular frequency \(\omega_d = \sqrt{\omega_0^2 - \alpha^2}\). The charge oscillates inside a decaying envelope.
- **Critically damped**, \(R = R_c\): \(q = q_0(1 + \alpha t)e^{-\alpha t}\). The charge returns to zero without crossing it.
- **Overdamped**, \(R > R_c\): both roots s₁ and s₂ are real and negative, and \(q = q_0\,(-s_2 e^{s_1 t} + s_1 e^{s_2 t})/(s_1 - s_2)\). The charge again decays without crossing zero, but the slower root makes the decay sluggish.

With the example L and C, \(R_c\) = 200 Ω. Through R = 20 Ω, α = 400 s⁻¹ and \(\omega_d\) = 3980 rad/s, only 0.5% below ω₀. The charge swings to about −0.73q₀ after half a period and needs about 11 ms before it stays within 1% of zero. Through R = 200 Ω, the critical case, it is within 1% after about 1.66 ms. Through R = 500 Ω, the roots are about −835 s⁻¹ and −19,165 s⁻¹, the slow mode has a 1.20 ms time constant, and the charge is within 1% only after about 5.57 ms. More resistance does not always mean faster settling.

## Quality factor and energy per cycle

The **quality factor** of a series RLC loop is

\[
Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{\omega_0}{2\alpha} .
\]

For R = 20 Ω, Q = 5.0. Critical damping corresponds to Q = 1/2, and any oscillation at all requires Q > 1/2. The amplitude envelope decays as \(e^{-\alpha t}\), with time constant 2L/R = 2.5 ms. For light damping the stored energy, which goes as the square of the amplitude, decays as \(e^{-2\alpha t} = e^{-Rt/L}\), with time constant L/R = 1.25 ms: twice as fast as the amplitude.

An exact per-period statement is also available. At a charge maximum the current is zero, so all the energy is in the capacitor. Successive maxima of the same sign are one damped period \(T_d = 2\pi/\omega_d\) apart, and their charges differ by the factor \(e^{-\alpha T_d}\). For R = 20 Ω, \(T_d\) = 1.579 ms, the charge ratio is 0.532 and the energy ratio \(e^{-2\alpha T_d}\) is 0.283. About 72% of the stored energy turns into heat in each period. The often-quoted rule that a fraction 2π/Q is lost per cycle is a small-loss approximation, valid only when 2π/Q is much less than 1. For Q = 5 it would claim a 126% loss, which is impossible. For Q = 100 it gives 6.3% against an exact 6.1%.

If the circuit is driven sinusoidally instead of released, the same Q measures how sharply its response peaks near ω₀. The optional [series-resonance project guide](../assignments/series-resonance-project-guide.md) develops that driven steady state after the [phasor lesson](13-phasors-loading-and-measurement-inference.md), and the [Circuits second-order lesson](../../circuits/modules/14-second-order-rlc-transients-resonance-and-impedance.md) treats step responses and impedance further.

## Common mistakes

- Reporting 1/√(LC) in hertz; it is an angular frequency in rad/s, and f₀ = ω₀/2π.
- Expecting the current to be largest when the capacitor is fully charged; the charge and current peaks are a quarter period apart.
- Letting the inductor current jump at the switching instant.
- Saying each element's energy oscillates at ω₀; each oscillates at 2ω₀, and only their sum is constant.
- Assuming any resistance stops the oscillation; it stops only when R ≥ 2√(L/C).
- Assuming more resistance always settles faster; beyond critical damping the decay slows again.
- Using the amplitude decay rate α for the energy, which decays at 2α.
- Applying the 2π/Q rule when Q is small.

## Worked example

**Problem.** A synthetic series loop has L = 25 mH and C = 2.5 µF, with the capacitor charged to 12 V and the current zero. It is released through R = 20 Ω. Find ω₀ and f₀, the initial rate of change of current, the current amplitude the loop would reach with no resistance, the damping regime, Q and \(\omega_d\), and the energy left after one damped period.

**Step 1: natural frequency.** ω₀ = 1/√(0.025 × 2.5 × 10⁻⁶) = 4000 rad/s, so f₀ = 636.6 Hz.

**Step 2: initial slope.** The current starts at zero, so the resistor drops no voltage and the full 12 V appears across the inductor: |di/dt| = 12/0.025 = 480 A/s.

**Step 3: lossless amplitude.** q₀ = 30 µC and ω₀q₀ = 0.120 A. Energy check: ½CV₀² = ½LI² = 180 µJ.

**Step 4: regime.** α = 20/(2 × 0.025) = 400 s⁻¹, below ω₀, so the loop is underdamped; \(R_c\) = 200 Ω. Then \(\omega_d = \sqrt{4000^2 - 400^2}\) = 3980 rad/s and Q = 4000 × 0.025/20 = 5.0.

**Step 5: one period later.** \(T_d = 2\pi/3980\) = 1.579 ms, and the energy factor is \(e^{-2\alpha T_d} = e^{-1.263}\) = 0.283. Of the initial 180 µJ, 50.9 µJ remains and 129.1 µJ has been dissipated.

**Step 6: check.** The 129.1 µJ must equal the resistor's heat, the integral of i²R over the same interval. Integrating the underdamped solution numerically reproduces it, which confirms the sign conventions and the energy bookkeeping.

## Limits of this lesson

All components, voltages and times are synthetic. The model uses ideal lumped elements: a linear capacitor, a linear inductor without core loss, connecting wires with no resistance beyond the stated R, an ideal switch and no radiation. Real components add resistance, capacitance and losses that depend on frequency, which can change both the frequency and the damping. Driven response, resonance curves and bandwidth are left to the optional series-resonance guide and the phasor lesson. Nothing here is a circuit design, component specification, switching practice or safety procedure. Original instruction has substantial AI assistance, and the course stays partial, unreviewed and formative-only.
