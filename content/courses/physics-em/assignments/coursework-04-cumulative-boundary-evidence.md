# Assignment 4: cumulative boundaries and energy claims

This final open report connects electrostatic, circuit, induction and wave evidence. It asks which conservation law and boundary condition support a claim, and which additional assumptions would be needed. The new capacitor case is a synthetic ideal circuit calculation, not a build instruction. Retain diagrams, code, derivations and report locally; selected browser responses are practice checkpoints and do not score a cumulative examination or design portfolio.

## Part A: an isolated two-capacitor relaxation

Take $C_1=2$ microfarads initially at 6 V and $C_2=4$ microfarads initially at zero. Join corresponding terminals through a finite resistance of 2 kilo-ohms, with no external battery. Define positive connecting current from the initially higher-potential capacitor toward the other. State the ideal capacitance, fixed-geometry and closed-charge assumptions explicitly.

Total charge on the connected positive-side nodes is 12 microcoulombs. The common final voltage is therefore $12/(2+4)=2$ V. Initial field energy is 36 microjoules and final field energy is 12 microjoules; the decrease is 24 microjoules. Charge conservation does not imply conservation of capacitor field energy alone during the resistive transient.

Write the differential equations for each capacitor voltage and derive the voltage-difference equation. The effective capacitance for the difference is $C_1C_2/(C_1+C_2)=4/3$ microfarads, giving relaxation time $RC_{eq}=8/3$ milliseconds. Initial current is $6/2000=3$ mA. These instantaneous and asymptotic quantities constrain a numerical model without specifying an actual component or instrument.

## Part B: integrate a complete energy ledger

Solve the voltage-difference equation analytically and reconstruct both capacitor voltages from conserved charge. Implement the two original voltage equations independently. Compare trajectories under step refinement and track the charge residual, capacitor-energy change and integral of $I^2R$. The integrated dissipation should approach 24 microjoules.

Reject an energy-only shortcut that assumes the final common voltage follows from preserving the initial capacitor energy while omitting resistive loss. Show which original balance it violates. Explain why making resistance small shortens the ideal relaxation without making its total energy loss vanish. At an ideal zero-resistance connection the lumped transient needs additional inductive/radiative or other physical structure; the finite-resistance model does not describe an instantaneous lossless equilibration.

## Part C: three distinct overbroad claims

First consider the statement “zero net enclosed charge means zero electric field everywhere on the enclosing surface.” Supply a counterexample with entering and leaving field flux and relate it to the earlier point-charge/Gauss reading. State what symmetry was required for the correctly derived cylindrical field and why it is absent in the counterexample.

Second consider “a negative total inductor port power proves the passive model has negative stored energy.” Use a positive definite inductance matrix and a decreasing-energy current state to separate stored amount from its time derivative. Retain signed port references and verify $\mathbf i^T\mathbf v=U'$. Explain the separate role of the coefficient passivity bound; returning previously stored energy is compatible with it.

Third consider “nonzero electromagnetic field energy requires positive net time-average power flow through a plane.” Use the perfect-reflection standing pattern to distinguish stored electric/magnetic energy from average Poynting transport. Derive the relevant average from fields, rather than assuming intensities add without interference terms. Identify where momentum transfer and an energy-storage statement answer different questions.

These three counterexamples concern different mathematical objects: a closed-surface integral, a derivative of stored energy, and a time-average flux. Avoid replacing them with one generic assertion that everything depends on context. Specify the object, its boundary and the verified counterexample.

## Part D: integrated evidence table

Build a table connecting each report's claimed result with its supporting equation, source/observation boundary, unit convention, independent reference and unresolved limitation. Include the distributed-charge energy integral, coupled-inductor source/storage/loss identity, radiating-sheet outward flux and the new capacitor charge/dissipation balance.

For at least one case retain an intentionally wrong implementation and the test that rejects it. Separate value agreement, equation residuals, conservation, admissibility and refinement. A small residual from a wrong model can coexist with a wrong physical interpretation. State which of your conclusions are mathematical consequences of stipulated inputs and which would require material properties, measurements or qualified engineering review.

## Self-review and scope

The retained report should contain the capacitor derivation and numerical energy integral, three explicit counterexamples and the integrated evidence table. Browser checkpoints assess selected values/choices; they do not evaluate written physics reasoning or certify equipment safety, mastery or course equivalence. The [MIT OCW 8.02 Spring 2007 syllabus](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/syllabus/) and [class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) are link-only scope comparators. All examples and explanations are original and AI-assisted. The source's TEAL experimental/group format, qualified review and measured workload are not reproduced. The course remains partial and unreviewed.
