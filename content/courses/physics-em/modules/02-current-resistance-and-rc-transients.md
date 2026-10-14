# Current, resistance, and RC transients

## Learning objectives

By the end of this reading, you should be able to:

1. Calculate the time constant of a series resistor-capacitor circuit from R and C, using consistent units.
2. Predict ideal capacitor charging and discharging voltages from an initial value and the circuit time constant.

## Current and resistance

Electric current measures how quickly charge crosses a chosen surface. For a steady current, **I = ΔQ/Δt**; more generally, current is the rate of charge transfer. One ampere is one coulomb per second. By convention, current points in the direction positive charge would move. In a metal wire, electrons drift in the opposite direction, even though circuit diagrams continue to use conventional current.

A potential difference across a conducting component can drive charge flow. Resistance summarizes how much voltage is needed to sustain a given current through that component. For an ohmic resistor in its stated operating regime, **V = IR**, where V is the voltage drop across it, I is the current through it, and R is measured in ohms. One ohm equals one volt per ampere. Ohm's relation is a useful model for resistors, not a universal equation for every device: a diode, for example, does not generally have a constant resistance across its operating range.

In a series branch there is one path, so the same current passes through each element. The resistor and capacitor can have different voltage drops that change over time. Kirchhoff's current and voltage rules express charge conservation at a junction and energy conservation around a loop; week 6 develops those network balances and source-loading analysis in more detail.

## What the time constant measures

An ideal capacitor stores charge and energy in its electric field. Current changes its charge, so its voltage cannot jump instantaneously in a finite-resistance circuit with finite current. When a resistor and capacitor are connected in series, the resistor limits the rate at which charge can move. Their product defines the time constant:

**τ = RC.**

The units confirm that τ is a time: Ω·F = (V/A)(C/V) = C/A = s. Convert prefixes before multiplying. For R = 2 kΩ and C = 5 μF, τ = (2,000 Ω)(5×10⁻⁶ F) = 0.010 s = 10 ms. If R is doubled while C stays fixed, the ideal time constant doubles; if C is halved, the time constant is halved.

The time constant describes the speed of a response in a particular circuit model, not the final voltage. In a simple unloaded series RC circuit, changing R changes how fast the capacitor approaches the same source voltage. Adding a parallel load may change both the time constant and final value because the circuit seen by the capacitor has changed.

## Charging after a voltage step

Consider an ideal source that changes from 0 to a constant Vₛ at t = 0, with a capacitor initially uncharged and a resistor in series. Applying the loop relation and the capacitor relation Q = CV gives the first-order response

**V꜀(t) = Vₛ(1 − e⁻ᵗ⁄τ),** with **τ = RC**.

The voltage starts at zero and approaches Vₛ. At t = τ, it has completed a fraction 1 − e⁻¹ ≈ 0.632 of the total change. At t = 2τ, the completed fraction is 1 − e⁻² ≈ 0.865. At t = 5τ, the remaining difference from the final value is e⁻⁵ ≈ 0.0067 of the initial step, so the capacitor is within about 1% of Vₛ.

For a 5.0 V step, R = 1.0 kΩ and C = 1.0 μF give τ = 1.0 ms. At t = 2.0 ms, t/τ = 2, so V꜀ = 5.0(1 − e⁻²) V ≈ 4.323 V. The exponent must be dimensionless: divide elapsed time by τ in the same time units. Notice also what the 63% statement means: after one time constant, the capacitor has completed about 63% of the change from its initial voltage toward its final voltage. If the capacitor starts at a nonzero value, its voltage is not necessarily 63% of the final voltage.

The charging current is initially Vₛ/R and decays as i(t) = (Vₛ/R)e⁻ᵗ⁄τ in this ideal model. Initially most of the source voltage is across the resistor; as the capacitor charges, its voltage rises and the resistor drop and current fall. At long times the ideal capacitor current approaches zero and its voltage approaches the source voltage. These endpoints are useful checks on both the equation and a sketch.

## Discharging from an initial voltage

If a capacitor begins at V₀ and discharges through a resistor with no source in the loop, its voltage follows **V꜀(t) = V₀e⁻ᵗ⁄τ**. It starts at V₀ and decays toward zero. After one time constant, it retains e⁻¹ ≈ 0.368 of its starting voltage; this is the same response described as completing about 63% of the change from V₀ to zero. The resistor converts electrical energy to thermal energy during the ideal discharge. A detailed balance of source work, stored energy, and resistor loss appears in a later switching lesson.

For charging from an arbitrary initial voltage V₀ toward a constant final value Vꜰ, the same one-mode model is **V꜀(t) = Vꜰ + (V₀ − Vꜰ)e⁻ᵗ⁄τ**. The exponential describes the remaining difference from the final value. This form makes clear that τ characterizes the transition, while initial and final conditions set its amplitude and offset.

## Scope and measurement limits

These formulas assume a single ideal resistor, a single ideal capacitor, a step-like source, and fixed component values. Real capacitors leak, resistors vary with temperature, sources have internal resistance, and instruments have finite input impedance. A voltmeter connected across a high-impedance circuit can create an additional load; the resistance relevant to τ is then the effective resistance seen by the capacitor under the circuit's source conditions. The week-6 lesson and week-14 lab study such loading explicitly.

RC models are also used as simplified descriptions of membrane charging. A fitted exponential time constant constrains a circuit-level combination of resistance and capacitance, but an observed biological trace does not by itself identify a unique biological mechanism. Real membranes can have multiple conductances and nonideal dynamics. The ideal response is a useful baseline, not a complete physiological model.

## Common checks

- Convert kΩ, MΩ, μF and ms consistently before evaluating τ = RC.
- Keep current, charge, voltage, resistance and time constant in their own units: A, C, V, Ω and s.
- Use the exponential's dimensionless ratio t/τ, not t or τ alone.
- For charging, check V꜀(0) = 0 and V꜀(∞) = Vₛ when the capacitor starts uncharged; for discharging, check V꜀(0) = V₀ and V꜀(∞) = 0.
- Apply the 63% rule to the fraction of the total voltage change completed after one τ, not automatically to the absolute voltage.
- Treat V = IR as an operating-regime model for an ohmic resistor, not a universal component law.

## Further study

These link-only OpenStax University Physics Volume 2 sections provide additional background: [9.3 Resistivity and Resistance](https://openstax.org/books/university-physics-volume-2/pages/9-3-resistivity-and-resistance), [9.4 Ohm's Law](https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law), and [10.5 RC Circuits](https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits). This lesson uses original wording and calculations; no source prose, figures, examples, problem wording, or datasets are reproduced.
