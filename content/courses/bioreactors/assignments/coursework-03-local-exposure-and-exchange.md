# Assignment 3: local exposure, exchange and conservation

A reactor-scale average is not a complete exposure history. This open report connects the existing oxygen, mixing, scale-up and scale-down readings with an explicit two-zone amount balance. It asks for local and total evidence, an exchange requirement and reproducible numerical checks. All values and thresholds are normalized synthetic inputs, not process settings or validated tissue/culture limits. Keep the full derivation, code and report locally; browser checkpoints evaluate selected quantities only.

## Part A: solve the distinct two-zone case

Use the foundation's two control-volume equations with $V_1=1,V_2=2,k_1=5,k_2=0,C^*=1,u_1=u_2=0.2,E=1$. The exchange coefficient $E$ is a volume rate, while $E(C_1-C_2)$ is an amount rate. Draw the two boundaries and label every external source, consumption term and internal exchange. Divide concentration equations by each zone's own volume, not by a common convenient number.

At steady state the total demand is $0.2(1)+0.2(2)=0.6$. Zone-one supply gives $C_1=1-0.6/5=0.88$. Zone two requires an exchange amount rate of 0.4, so $C_1-C_2=0.4/E=0.4$ and $C_2=0.48$. The volume-weighted mean is $(0.88+2(0.48))/3=46/75\approx0.613333$.

Verify both original zone equations separately. Their sum cannot detect every internal exchange error because the intended internal terms cancel. Check the exchange amount on each side and confirm that the numerical implementation uses opposite signs and the correct concentration-rate volume divisions. Report the actual zone-one driving force rather than replacing it with the weighted mean.

## Part B: a local requirement

Take a stipulated lower admissible concentration $C_{min}=0.5$. The weighted mean exceeds it, but zone two does not. Solve $C_2\geq C_{min}$ for the minimum exchange, retaining the other stated coefficients. The requirement is

$$E\geq\frac{0.4}{0.88-0.5}=\frac{20}{19}.$$

This bound is conditional on $C_1>C_{min}$ and the fixed-transfer/constant-demand model. If the total supply cannot put $C_1$ above the level, no finite exchange solves the deficit. Explain that distinction between a transfer-capacity limit and an internal mixing limit.

For the separate controlled perturbation $E=2$, $C_1$ remains 0.88, while $C_2=0.68$ and the mean becomes $56/75\approx0.746667$. Show explicitly why the first state stays fixed here: total demand and the only external supply coefficient are held constant. An actual agitation change could also alter transfer, shear or consumption; this mathematical comparison does not demonstrate that those physical changes are absent.

## Part C: transient verification

Write the affine two-state matrix equation and solve its steady state independently with a linear solver. Derive its eigenvalues or trace/determinant conditions and compare relaxation with a numerical transient from an admissible initial state. Use at least three successively halved steps and evaluate both local concentrations and total amount at shared observation times.

Track external input, uptake and internal exchange as separate rate histories. Integrate the total input-minus-demand and compare it with the change in $V_1C_1+V_2C_2$. A tiny total error alongside a large local error is possible: adding a deviation delta to C1 and subtracting delta V1/V2 from C2 preserves the weighted mean. Demonstrate that counterexample separately. Then intentionally introduce one incorrect volume factor in the solver and inspect which local and total checks reject it. Keep incorrect runs clearly labeled.

Constant uptake is not guaranteed to preserve nonnegative states from every start. Define a stopping event at the declared admissible boundary and report any failure. Do not silently clip a negative concentration and continue to claim the original equation has been solved. Distinguish a genuine model-domain failure from an integration error that disappears under refinement.

## Part D: model and observation comparison

Construct a single-uniform-state approximation with a declared effective transfer coefficient, then identify its extra assumption about local driving force. Compare its predictions with the two-zone model for the supplied case. Explain why the volume average of a coefficient times a driving force is not generally the product of the separate averages.

Propose an additional observation or controlled mathematical perturbation that separates competing local-exposure explanations. State which parameters or boundary terms it changes and which are assumed fixed. A bulk trace alone need not identify every local concentration and uptake, even if one fitted curve is excellent. Link this limitation with the probe-identifiability report: spatial averaging and observation delay are different reasons a reported signal can hide the state of interest.

## Self-review and scope

The retained report should contain two-zone diagrams, original and reduced equations, local/total residuals, conditional exchange bounds, transient refinement and a model-identifiability argument. Selected checkpoints do not grade the code, proof or proposed observation plan. [MIT OCW 10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) mass-transfer/scale-up/scale-down topics are link-only comparators; no source problem or data was imported. All text and examples are original with substantial AI assistance. CFD, validated exposure limits and real vessel performance remain outside this narrower report; the course remains partial and unreviewed.
