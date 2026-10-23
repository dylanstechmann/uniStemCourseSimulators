# Assignment 1: nonlinear port and sensitivity evidence

This open report joins nodal/port balances, nonlinear operating points and local small-signal reasoning. It asks for a solved constitutive model, an admissible branch, an independent power ledger and a quantified perturbation comparison. The circuit and parameters are invented ideal inputs, not a component selection or hardware-build specification. Retain derivations, code and report locally; browser checkpoints assess selected outputs only.

## Part A: a distinct constructed bias point

Use the ideal law $I=I_S[\exp(V_D/V_T)-1]$ with $I_S=10^{-12}$ A and $V_T=0.026$ V. A source drives the junction through R=2000 ohms. Construct a baseline current of 1 mA, giving $V_D=0.026\ln(1+10^9)\approx0.53880491$ V and required source $V_S=V_D+2\approx2.53880491$ V.

Those expressions define the synthetic baseline; they are not measured device data. Start your report from the original network and device equations, then solve the scalar load-line equation numerically using that source. Recover the baseline current without inserting it as a solver constraint. State the root interval, method, residual scale and stopping criterion.

Prove uniqueness within the positive-source bracket using the derivative of the original scalar residual. Compare a bracketed method with Newton iteration from at least two starts. Preserve any failure or out-of-bracket proposal rather than presenting only the successful final value. An optimizer or iteration returning a number does not establish that the constitutive or network equation was actually satisfied.

## Part B: derive a local model

Differentiate the stipulated junction law at the recovered point. The exact incremental resistance is $r_d=0.026/(0.001+10^{-12})$ ohms, approximately 26 ohms. Keep the small $I_S$ term in the full-precision calculation before rounding. Compare this derivative with the finite bias ratio $V_D/I$ and explain why they differ.

Derive source-to-junction sensitivity $H=r_d/(R+r_d)\approx0.01283317$. This is a local voltage gain for a change in source voltage, not the junction's isolated dynamic resistance. Include the source resistor in the incremental network and state which parameters and topology remain fixed.

For a sequence of positive and negative mathematical source offsets, predict the junction change from H and independently re-solve the original nonlinear equation. Compare absolute error and its scaling as the offset is halved. Select a neighborhood satisfying a stated approximation tolerance; do not call that neighborhood a real device rating or a universal allowable signal range.

## Part C: close a separate power ledger

At the baseline, diode power is approximately 0.53880491 mW, resistor dissipation is 2 mW and source input is approximately 2.53880491 mW. Verify $V_SI=V_DI+RI^2$ with the declared passive references. A successful current solve and a power sum are different checks: the latter follows from the network boundary, while the former also tests the nonlinear constitutive law.

Repeat the ledger at one perturbed point using its re-solved current and voltage. Do not reuse the baseline resistance derivative as a global resistor and assume its power represents the nonlinear device. The local derivative model describes deviations; it does not replace the DC bias energy bookkeeping.

## Part D: compare models and boundaries

Construct a clearly labeled constant-drop or piecewise-linear approximation and compare it with the exponential law over the chosen study interval. State the approximation's parameters and intended criterion before judging agreement. A model that matches one point can still have the wrong slope or curvature, so compare all three when relevant.

Identify missing behaviors such as capacitance, self-heating or breakdown without inventing their parameters. If you include one, define a separate constitutive/dynamic model and rerun its balances. The selected exercise does not identify a real junction or supply a laboratory measurement procedure.

Also distinguish a linear external source network's Thevenin equivalent from a global equivalent of the nonlinear junction. A valid port replacement for one part of the circuit does not make every other element linear. Include an intentionally incorrect “one resistor for all biases” calculation and show the residual or sensitivity evidence that rejects it.

## Self-review and scope

The retained report should contain a reference diagram, original equations, uniqueness/bracket argument, independent root solution, local derivative, perturbation/refinement study and signed power table. Browser practice does not evaluate the code or written reasoning. [MIT OCW 6.002 Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) lectures 6–8 provide link-only nonlinear/small-signal/dependent-source scope. All text, parameters and tasks here are original with substantial AI assistance; no source circuit, problem or data is imported. Real device specifications, workload and qualified circuit review remain open; the course stays partial and unreviewed.
