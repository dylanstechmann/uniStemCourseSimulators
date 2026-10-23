# Assignment 2: mutual energy and source-work ledger

This open report joins Faraday/Lenz reasoning, coupled-inductor states and resistive transients. It asks whether the same declared references satisfy voltage, energy and source-work identities. The circuit is an invented ideal mathematical model, not a transformer or equipment design. Retain derivations, code, plots and report locally; selected browser quantities do not constitute a graded design or proof.

## Part A: a distinct instantaneous state

Choose currents entering both dotted terminals and passive voltage references. Use $L_1=0.03$ H, $L_2=0.12$ H and $M=0.03$ H. At the selected instant, currents are $(i_1,i_2)=(2,1)$ A and their derivatives are $(-1,2)$ A/s. State all references in a verbal diagram before calculating signs.

Compute the inductance matrix determinant and coupling magnitude. The coupling magnitude is one half, and the determinant is positive, so the stated linear passive model has positive definite energy. Derive $U=\mathbf i^TL\mathbf i/2$ and evaluate it: the self terms are 0.06 and 0.06 J, with mutual term 0.06 J, totaling 0.18 J.

The coil voltages from $\mathbf v=L\mathbf i'$ are 0.03 and 0.21 V. Total coil port power is $2(0.03)+1(0.21)=0.27$ W. Differentiate the energy expression directly and show that it gives the same rate. A negative current derivative in one component does not determine the sign of total energy change when the states are coupled.

## Part B: add sources and resistances

Now include series resistances $R_1=2$ ohms and $R_2=3$ ohms. At that same instant, external voltages must be $\mathbf u=\mathbf v+R\mathbf i$: 4.03 V and 3.21 V. The instantaneous resistive loss is $2(2^2)+3(1^2)=11$ W. Total source input is $4.03(2)+3.21(1)=11.27$ W, split into loss 11 and storage rate 0.27 W.

Keep coil terminal voltages and external source voltages in different columns. Using one in place of the other would either omit or double count the resistor power. Identify the signed current associated with each source's power and explain how a later state could return energy through a source while resistive dissipation remains nonnegative.

For a transient study, hold the external voltages at those selected values and start from the selected current state. The initial derivative should then recover $(-1,2)$ A/s. The derivative data are an instantaneous consistency condition, not a claim that the same derivative persists for the entire forced transient.

## Part C: independent transient and integral evidence

Solve $L\mathbf i'+R\mathbf i=\mathbf u$ using a documented numerical method. Independently form the affine state matrix and compute a reference solution using a matrix exponential or a separately verified linear-system method. Compare current trajectories at common times and halve the step. Retain enough precision to separate truncation error from display rounding.

Integrate signed source input and positive resistive loss over the same time interval. Compare their difference with the computed stored-energy change. Report the original voltage residual as well as the integral energy residual. A small current error does not prove the source-work bookkeeping was implemented with the right reference signs.

Repeat a comparison with $M=0$ while preserving the other stated coefficients and references. This is a different model with a different coupled response. Then reverse one complete coil reference convention consistently and show that the physical energy and source-work conclusions agree after transforming currents, voltages and the mutual sign together.

## Part D: reject an inconsistent coefficient model

Construct a clearly labeled coefficient example with $|M|>\sqrt{L_1L_2}$. Find an explicit current direction with negative quadratic energy, or diagonalize the symmetric matrix to reveal a negative eigenvalue. Explain why such a table cannot represent the assumed passive pair of ideal inductors. Do not interpret the inconsistency as permission to extract free energy from a real device.

Contrast this with a valid negative mutual sign caused by the declared dot/reference orientation. The energy bound concerns the matrix as a whole; the sign of one cross coefficient alone is insufficient. At the ideal equality bound, identify why the inverse-based state equation becomes singular and which additional constraint interpretation is needed.

## Self-review and scope

The retained report should contain a reference diagram, passivity check, instantaneous voltage/source/storage/loss table, transient reference comparison, refinement evidence and an invalid-model counterexample. Browser checkpoints do not score those artifacts or certify electrical safety. The [MIT OCW 8.02 Spring 2007 class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) mutual-inductance and magnetic-energy sessions are link-only scope comparators. All cases and explanations are original and AI-assisted; no source problem or code is imported. Nonlinear cores, equipment behavior and qualified physics review remain outside this selected model. The course stays partial and unreviewed.
