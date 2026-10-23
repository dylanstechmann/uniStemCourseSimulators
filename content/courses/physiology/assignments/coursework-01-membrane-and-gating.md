# Assignment 1: membrane states, gates and observation conditions

Build a mathematical report connecting passive charge balance, a fixed-voltage gate and passive spatial attenuation. Use [passive membrane/cable properties](../modules/15-passive-membrane-and-cable-properties.md) and [the Hodgkin–Huxley reading](../modules/16-voltage-gated-conductances-and-the-hodgkin-huxley-action-potential.md). Retain derivations, any simulation, unit checks and interpretation locally. Browser checkpoints assess selected values, not a full voltage-dependent model or your report. The new parameters are arbitrary teaching values, not measured tissue responses or a stimulation procedure.

## Passive charging in a declared one-compartment model

Use membrane capacitance density Cm=1 microfarad/cm², fixed leak conductance density gL=0.2 millisiemens/cm² and reversal EL=−60 mV. Starting at V=EL, switch the mathematical input-current density to a constant 2 microamperes/cm². The equation is Cm Vdot=I−gL(V−EL), with outward ionic current positive. Derive the steady voltage, time constant and complete voltage solution, converting capacitance/conductance units explicitly.

Evaluate voltage at five milliseconds and verify the initial derivative and final limit. Independently integrate the charge-balance equation numerically, comparing at least three time steps with the exact solution. Keep current density, total current, capacitance density and total capacitance distinct. An area would be required to convert density quantities to total quantities; none is supplied by this model.

Explain why a current-clamp input and an imposed voltage-clamp value are different boundary conditions. At the final passive voltage the input and outward leak currents balance. During charging, their difference supplies capacitive current. A voltage rise alone does not identify a channel's molecular identity or predict a complete action potential under a fixed-conductance model.

## A separate fixed-voltage gating case

For a separate held-voltage example, let a gate n satisfy ndot=alpha(1−n)−beta n with constant alpha=0.1 per millisecond, beta=0.3 per millisecond and n(0)=0.1. Derive n-infinity, its time constant and n(t). Evaluate n after five milliseconds. Show that the solution remains between zero and one for valid initial values and nonnegative opening/closing coefficients.

Let the modeled potassium conductance density be gK=20 n^4 millisiemens/cm². With the voltage held at −20 mV and reversal EK=−80 mV, calculate gK and the potassium-current density after five milliseconds. State its sign under the outward-positive convention. This is one ionic component; it does not give the full clamp current if other ionic or capacitive contributions are present.

Calculate the right-hand initial derivative of gK(t) after the step. Compare the given nonzero n(0) with a hypothetical n(0)=0. Explain why the fourth power does not imply zero initial slope for every starting gate value. A nonlinear power can accentuate the conductance delay without making the first derivative vanish at a nonzero resting activation. Check the derivative by a sufficiently small numerical difference and explain the role of step refinement and rounding.

## Spatial attenuation is a different question

In a distinct uniform passive-cable model, let the steady voltage amplitude decay as A(x)=A0 exp(−x/lambda), with A0=20 mV and lambda=1.5 mm. Calculate the amplitude at x=3 mm and the electrotonic distance x/lambda. Compare this steady attenuation with the temporal charging fraction in the first part. A length constant is not a conduction velocity, and a static exponential decay does not model active regenerative propagation.

Describe what extra voltage dependence and spatial coupling would be required to connect these examples to a propagating action potential. Link the relevant existing readings rather than assuming constant alpha/beta values predict threshold or refractory timing. Distinguish source-derived classic squid-axon parameters in the existing lesson from the invented parameters supplied here. Neither set is a measured response of a human subject in this project.

## Self-review after deriving the results

The passive time constant is five milliseconds and steady voltage −50 mV. At five milliseconds, V=−60+10(1−exp(−1)) mV, about −53.67879 mV. Its initial derivative is +2 mV/ms. For the separate gate, n-infinity is 0.25 and time constant 2.5 ms; n(5)=0.25−0.15 exp(−2), about 0.22969971. Conductance is about 0.05567648 mS/cm² and potassium current about +3.34059 microamperes/cm².

The passive-cable amplitude at three millimeters is 20 exp(−2), about 2.70671 mV. For the given gating initial condition, n-dot initially is 0.06 per millisecond and gK-dot is nonzero; derive its value independently. Retain unit, sign, initial/final-state, derivative and numerical-refinement evidence rather than only the final answers.

This original AI-assisted assignment uses [MIT OCW 6.021J Cells and Tissues Fall 2004 calendar](https://ocw.mit.edu/courses/6-021j-quantitative-physiology-cells-and-tissues-fall-2004/pages/calendar/) as a link-only scope comparator. No source exercise, code, waveform or experimental data was imported. Mathematical checks do not assess reports or establish a biological mechanism, clinical suitability, qualified review or measured workload; the course remains partial and unreviewed.
