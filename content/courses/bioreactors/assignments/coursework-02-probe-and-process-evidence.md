# Assignment 2: probe/process separation and fit evidence

This open analysis report extends the existing synthetic gassing-out lab. It distinguishes the liquid state, its delayed observation, numerical fitting and parameter identification. It is a normalized mathematical exercise; no physical calibration procedure or experimental operating condition is specified. Retain code, plots, estimates and your evidence report locally. Selected browser responses are formative checkpoints, not a scored analysis portfolio.

## Reference table and declared observation model

The [analytic probe reference CSV](../assignments/probe-response-reference.csv) contains normalized time and a rounded probe state generated from the foundation's worked rates $k=2,a=4$. It is an analytic illustration, not measured data, and its rates differ from the assignment parameters below. Verify its values by integrating the two original state equations or evaluating their exact solution. State the file's rounding precision in your residual tolerance.

Use $C'=k(1-C)$ and $P'=a(C-P)$, with zero initial states. Fit only the observed $P$ column in the reference table. Demonstrate the rate-swap symmetry by comparing the parameter pairs $(2,4)$ and $(4,2)$. Both produce the same probe trace, while the corresponding hidden liquid states differ. Additional time samples of this same ideal output cannot label which rate belongs to the probe. Distinguish this exact structural ambiguity from large uncertainty caused by noisy or sparse observations.

## Part A: distinct assignment parameters

For the assignment's separate model use $k=1.5,a=3$. Evaluate at $t=2/3$, so $kt=1$ and $at=2$. The liquid state is $C=1-e^{-1}\approx0.632121$; the probe state is $P=1-2e^{-1}+e^{-2}\approx0.399576$. The initial probe slope is zero and its second derivative is $ak=4.5$.

If that one probe point is treated incorrectly as the liquid concentration, the one-exponential apparent rate is $-\ln(1-P)/(2/3)\approx0.765180$, rather than 1.5. Derive the number from the full expression and compare it with a multi-point fit to an incorrectly specified one-state model. A small optimizer residual does not make a fitted coefficient the physical transfer rate.

Next suppose independent information assigns the probe rate to three in this exact model. Explain why the remaining member of the unordered fitted pair can then be assigned to the process. State what evidence supports that external assignment and what would fail if the probe law or boundary input were wrong. Do not invent actual calibration evidence for this synthetic task.

## Part B: coincident-rate limit

Use a separate equal-rate case $k=a=1$ and $t=1$. The probe expression must be evaluated by its continuous limit $P=1-(1+t)e^{-t}$, giving $1-2/e\approx0.264241$. Derive the limit analytically or from the equal-rate ODE solution. Show why a vanishing denominator in the unequal-rate formula is removable, then test a numerical implementation for two increasingly close positive rates.

Compare a direct expression, the limit and independent integration. Report cancellation error separately from time-integration error. A division-by-zero exception or nonfinite value in one formula is not evidence that the actual two-state system has a singular trajectory. Preserve a regression case with exactly equal rates.

## Part C: separate constant uptake

For another controlled comparison use $C'=k(C^*-C)-u$ with $k=1.5,C^*=1,u=0.3$, retaining a first-order probe with positive rate. Its steady liquid and probe values both equal 0.8. At a stipulated lower admissible level 0.4, the constant-demand capacity is $k(C^*-0.4)=0.9$. These values belong to this separate uptake model; they are not extra parameters to insert into the no-consumption reference CSV.

Explain which conclusion changes if uptake depends on concentration, why an unchanged open-loop steady state does not imply unchanged closed-loop behavior, and what a single plateau can identify about $u/k$. A probe signal above a threshold need not establish every hidden liquid trajectory or local concentration when additional spatial structure is present.

## Evidence required in the retained report

Include exact and integrated reference curves, the swapped-pair identity, hidden-liquid comparisons, a one-state model failure, equal-rate numerical checks and a separate uptake steady-state ledger. Use explicit parameter bounds and starting values in any optimizer. Retain a record of failed or indistinguishable fits; selecting the best one and omitting alternatives would hide the identifiability issue.

The table has constructed analytic values, so its residuals are not instrument noise, independent biological replicates or evidence for a real confidence interval. If you add a hypothetical error model, label it as a new simulation and report its assumptions. Compare prediction at a withheld time with parameter identification: a model can predict this same observed trace well while its parameter labels remain ambiguous.

The [MIT OCW 10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) design/mass-transfer strands provide link-only scope. New explanations, table and tasks are original and AI-assisted; no measured dataset or instrument specification is imported. General sensor chemistry, validated closed-loop design and actual calibration competence remain outside the report. The package stays partial and unreviewed; workload and qualified review are open.
