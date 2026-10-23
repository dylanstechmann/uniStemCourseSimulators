# Assignment 2: compensation and model evidence

This open report constructs a proper dynamic compensator for a distinct normalized plant and checks its time, frequency and steady-state consequences. All coefficients and signals are invented mathematical inputs. Retain equations, code, plots and report locally; selected browser responses do not grade the full design or establish operating settings for equipment.

## Part A: solve a declared characteristic problem

Use unity negative feedback with P(s)=1/[s(s+3)] and C(s)=K(s+z)/(s+p). Require K>0 and p>z>0 for the selected proper lead form. Target closed-loop characteristic is (s+5)(s²+6s+13), with poles -5 and -3 plus or minus 2i.

Expand both the target and the original characteristic s(s+3)(s+p)+K(s+z). Coefficient matching gives p=8, K=19, z=65/19. Check each inequality and substitute the values into the original expression to recover s³+11s²+43s+65.

A formal algebraic coefficient match outside the assumed controller form would need rejection or a newly stated design family. Do not silently call a negative coefficient or a pole/zero reversal the same lead design. The chosen family and admissible parameter domain are part of the problem.

## Part B: phase and tracking checks

The maximum controller-phase frequency is sqrt(pz)=sqrt(520/19), about 5.2314836 in inverse normalized time units. Its phase boost is asin(87/217), about 23.635808 degrees. Derive the peak condition rather than identifying it from a sparse plot.

For unit-ramp tracking, the stable unity-feedback model has Kv=Kz/(3p)=65/24 and steady error 24/65. Derive this through the error transform and final-value eligibility. A step target and a ramp target are different tests; zero asymptotic step error does not imply zero ramp error.

Find the actual loop unity-gain crossover independently. Compare loop phase there with the controller's maximum phase frequency. The two frequencies need not coincide because the controller also changes magnitude and the plant contributes its own frequency dependence. Use the original complex transfer functions, not only a maximum phase formula, to evaluate a margin.

## Part C: a compatible dynamic realization

Build a two-state plant realization and the one-state proper controller wdot=−p w+e, u=K e+K(z−p)w. Combine them under the stated negative feedback. Verify that the full three-state characteristic matches the target cubic and that no hidden unstable mode was discarded by transfer simplification.

Choose consistent initial states and compare a step or ramp response from direct integration with an independent transform or matrix-exponential calculation. Refine the step and report residuals, not only a smooth tracking plot. A nonzero controller initial state produces a transient absent from a zero-initial-state transfer calculation.

Track requested input magnitude and distinguish it from any separately introduced delivered-input limit. If adding a clamp for a comparison, define its threshold and storage policy explicitly and analyze that changed nonlinear model. The exact linear target roots no longer prove its global response.

## Part D: change one model assumption

Make one documented change to the plant's second pole or gain while keeping the original controller fixed. Derive the new characteristic and tracking limit. Compare its roots and actual frequency response with the nominal model before interpreting the design as insensitive or fragile.

A finite set of parameter comparisons is evidence for those selected models, not a proof over every uncertain plant or delay. If proposing a bounded uncertainty statement, state the entire parameter set and the condition that would need to hold throughout it. Do not infer a universal robustness result from a nominal stable polynomial.

Compare high-frequency controller gain K with its DC gain Kz/p and explain the possible measurement-noise tradeoff. The proper controller has finite high-frequency gain but still changes how sensor disturbances enter the loop. Without a noise spectrum or actuator model, the report cannot establish actual signal quality or range performance.

Derive the sensitivity and complementary-sensitivity functions S=one/(one+CP)and T=CP/(one+CP). Check S+T=one and identify the sign/path by which an added measurement-noise signal enters the output. That equation explains why controller magnitude alone is not the complete noise-transfer budget, even when nominal closed-loop poles are stable.

Retain the coefficient solution, admissibility checks, reference-error derivation, actual crossover, combined realization and parameter comparison. Plots require units, scales and a text description. [MIT OCW 2.004 Spring 2008 calendar](https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/pages/calendar/) and selected [16.30 Fall 2010 topics 2–4](https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/pages/lecture-notes/) provide link-only classical-control scope. All examples and tasks are original and AI-assisted; no source problem, code, circuit, figure or data is imported. General robust synthesis, physical implementation, workload and qualified review remain open; the course stays partial and unreviewed.
