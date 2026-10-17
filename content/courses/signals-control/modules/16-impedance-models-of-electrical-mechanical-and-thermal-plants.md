# From components to transfer functions: impedance models of electrical, mechanical and thermal plants

The earlier lessons began from a model that was simply given: a first-order lag for the incubator and the standard second-order form for a sensor that rings. This lesson derives such models from the physical components. Each element is described by its **impedance**, the ratio of an effort to a flow in the Laplace domain, and the elements combine by the same rules whether they are resistors and capacitors, springs and dampers, or chamber walls and air. The transfer function then follows by algebra, and the component values give the time constants, natural frequencies and damping ratios directly. All components and numbers are synthetic.

The [MIT OCW 2.004 Dynamics and Control II (Spring 2008) calendar](https://www.ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/pages/calendar/) gives component modeling a long block, lectures 5–16, from the impedance of electrical components to mechanical, rotational and two-port systems, before it turns to system responses. This lesson gives a compact version of its electrical and translational-mechanical impedance lectures (5–7 and 9–10), adds thermal elements for the course's incubator, and sits beside the local second-order lesson so that the response measures are already available. It uses 2.004 as a scope comparator only and reproduces no MIT material. Circuit fundamentals themselves belong to the Circuits & Instrumentation course.

## Learning objectives

By the end of this lesson, you should be able to:

1. Write the Laplace-domain impedances of resistors, capacitors and inductors and of dampers, springs and masses, and combine elements that share a flow or an effort.
2. Derive a transfer function by impedance division or a force balance, read its time constant, natural frequency and damping ratio from component values, and check it at s = 0, at large s and by units.
3. Represent a thermal or mechanical plant by an electrical analog and explain why a passive thermal network cannot ring on its own.

## Impedance: effort over flow

For an electrical element the effort is the voltage across it and the flow is the current through it. With zero initial conditions:

- a resistor has V = RI, so **Z = R**;
- a capacitor has I = C dV/dt, so V = I/(sC) and **Z = 1/(sC)**;
- an inductor has V = L dI/dt, so **Z = sL**.

Elements that carry the same current (in series) add their impedances; elements that share the same voltage (in parallel) add the reciprocals of their impedances. The limits are worth remembering: at s = 0, the steady state, a capacitor is an open circuit and an inductor a short circuit, and at very large s the roles reverse.

For translational mechanics, take the effort as force and the flow as velocity:

- a damper has F = bv, so **Z = b**;
- a spring has F = kx, and x = v/s, so **Z = k/s**;
- a mass has F = m dv/dt, so **Z = ms**, with v measured relative to the ground.

Elements attached to the same moving point share its velocity, and the force needed to drive that point is the sum of their forces, so their impedances add. This is the **force–voltage analogy**: force corresponds to voltage and velocity to current, so a damper behaves like a resistor (R = b), a mass like an inductor (L = m) and a spring like a capacitor with **C = 1/k**. Elements that share a velocity behave like series elements that share a current. The catheter of the second-order lesson is the hydraulic version of the same structure: the inertia of the fluid column plays the part of the mass, the compliance of the tubing and diaphragm the spring, and viscous friction the damper.

For heat flow, the effort is a temperature difference and the flow is the heat flow in watts. A **thermal resistance** R_th (K/W) passes q = ΔT/R_th, and a **thermal capacitance** C_th (J/K) stores heat, q = C_th dT/dt, so its impedance is 1/(sC_th). There is no thermal counterpart to a mass or an inductor, because heat has no inertia.

## Transfer functions by impedance division

When the output is the effort across one element of a series chain, the transfer function is that element's impedance divided by the total. For an **RC low-pass filter** with the output across the capacitor,

**Vout/Vin = (1/(sC)) / (R + 1/(sC)) = 1/(RCs + 1),**

a first-order lag with time constant τ = RC. With R = 10 kΩ and C = 10 µF, τ = 0.1 s and the corner frequency is 1/τ = 10 rad/s, or 1.59 Hz. The result agrees with the limits above: at s = 0 the gain is 1, because the capacitor draws no current, and at large s the gain falls toward zero, because the capacitor shorts the output.

For a **series RLC circuit** with the output across the capacitor,

**Vout/Vin = 1/(LCs² + RCs + 1).**

Matching this to the standard second-order form gives **ωn = 1/√(LC)** and **ζ = (R/2)√(C/L)**. With L = 10 mH, C = 1 µF and R = 50 Ω, ωn = 10,000 rad/s and ζ = 0.25.

A **mass–spring–damper** driven by a force F, with the spring and damper connecting the mass to the ground, needs F = (ms + b + k/s)V. Because V = sX, the displacement response is

**X/F = 1/(ms² + bs + k),**

so **ωn = √(k/m)**, **ζ = b/(2√(km))** and the static deflection per unit force is 1/k. With m = 2 kg, k = 800 N/m and b = 16 N·s/m, ωn = 20 rad/s, ζ = 0.2 and the static gain is 1.25 mm/N. Under the force–voltage analogy this system is the series RLC circuit with L = m, R = b and C = 1/k, which is why the two denominators have the same form: the capacitor voltage plays the part of the spring force kx.

## The incubator as a thermal RC circuit

Model a chamber as one well-mixed thermal capacitance C_th, heated by u watts and losing heat to the room through R_th. The energy balance C_th dT/dt = u − (T − T_room)/R_th gives, for the temperature rise ΔT above the room,

**ΔT/U = R_th/(R_th C_th s + 1).**

The DC gain is the thermal resistance and the time constant is R_th C_th. The incubator of the Laplace lesson, with K = 0.5 °C/W and τ = 10 min, therefore corresponds to R_th = 0.5 K/W and C_th = 600 s ÷ 0.5 K/W = 1,200 J/K. The component view also says what each change would do: better insulation raises R_th, and so both the gain and the time constant, while a heavier chamber raises only the time constant.

Adding a heater block, a wall or a sensor adds another capacitance joined through another resistance, and each adds a real pole. In a lumped thermal network every capacitance is referenced to a fixed temperature and heat flows only from hot to cold, so all the poles are real and negative, and a heater step makes every node temperature rise without overshoot. A temperature loop that overshoots is showing the effect of feedback, which the later feedback lessons examine, not a property of the plant alone.

## Checking a derived model

Three checks catch most derivation errors. First, set **s = 0**: the result should be the static behaviour, such as 1/k for a spring or R_th for a chamber. Second, let **s grow large**: the highest power of s should belong to the element that dominates fast changes, as the mass does in X/F ≈ 1/(ms²). Third, check **units**: every term in a denominator must carry the same units, as ms², bs and k all do in newtons per metre. The order of the denominator usually equals the number of independent energy-storing elements (capacitors, inductors, masses, springs and thermal capacitances), which gives a fourth quick check.

## Common mistakes

- Writing a capacitor's impedance as sC or a spring's as ks, instead of 1/(sC) and k/s.
- Mapping a spring to a capacitor with C = k instead of C = 1/k in the force–voltage analogy.
- Putting the total impedance in the numerator of an impedance divider.
- Expecting a passive thermal model to overshoot after a heater step.
- Mixing prefixes and time units, such as kΩ with µF, or minutes with seconds.

## Worked example

**Problem.** A synthetic sensor mount is modeled as a mass on a spring with damping: m = 0.5 kg, k = 50 N/m and b = 3 N·s/m. Find X/F, the static deflection per newton, ωn, ζ, the step overshoot and the electrical analog.

**Step 1: transfer function.** X/F = 1/(0.5s² + 3s + 50).

**Step 2: static gain.** At s = 0, X/F = 1/50 = 0.02 m/N, or **20 mm/N**.

**Step 3: natural frequency and damping.** ωn = √(50/0.5) = **10 rad/s** and ζ = 3/(2√(50 × 0.5)) = 3/10 = **0.3**.

**Step 4: overshoot.** From the second-order lesson, the overshoot is exp(−πζ/√(1 − ζ²)) = exp(−0.988) ≈ **37.2%**.

**Step 5: analog.** Under the force–voltage analogy the mount is a series RLC circuit with L = 0.5 H, R = 3 Ω and C = 1/50 = 0.02 F. Its denominator 0.01s² + 0.06s + 1 is the mount's 0.5s² + 3s + 50 divided by 50, so the circuit and the mount have the same poles.

## Limits of this lesson

All components and numbers are synthetic. The models are ideal, linear and lumped, start at rest, and ignore friction nonlinearity, saturation, distributed effects such as waves and conduction delay, and the dependence of parameters on temperature. Rotational systems, gears and other two-port elements, motors, operational amplifiers and parameter estimation from data, all part of 2.004's modeling block, are not covered here; the virtual lab fits a first-order model from step data. Nothing here is a design, a component choice or a statement about any real device.
