# Proper lead compensation and pole design

The root-locus reading changes a proportional gain. A dynamic compensator also changes the loop's pole and zero structure. This original foundation constructs one proper lead controller by matching a declared closed-loop polynomial, then checks its frequency and steady-state implications. All times, signals and coefficients are normalized mathematical inputs, not controller settings for equipment.

## State the loop and controller form

Use unity negative feedback around plant P(s)=1/[s(s+2)]. Choose C(s)=K(s+z)/(s+p), with K>0 and p>z>0 for the selected lead form. The controller pole is stable, its high-frequency gain is finite K, and its zero is closer to the origin than its pole.

The characteristic equation 1+C P=zero becomes

$$s(s+2)(s+p)+K(s+z)=0, $$

or s³+(p+2)s²+(2p+K)s+Kz=zero. Matching polynomial coefficients is useful only if the resulting coefficients satisfy the assumed controller form and no unexamined unstable internal mode is canceled. Not every desired polynomial produces a positive admissible lead controller.

For a worked target (s+3)(s²+3s+9), expansion gives s³+6s²+18s+27. Coefficient matching produces p=4, K=10, z=2.7, which satisfies p>z>0. These are original normalized examples, not a copied design exercise.

## Distinct rehearsal design

Choose target (s+4)(s²+4s+8)=s³+8s²+24s+32. Matching gives p=6, K=12, z=8/3. Verify the original characteristic expression by substitution, then recover poles -4 and -2 plus or minus 2i. The stable target polynomial establishes asymptotic stability of this exact linear closed-loop model.

It does not establish robustness to parameter changes, delay, actuator limits, quantization or an unknown additional pole. A pole-placement statement about the selected model and a validated operating claim are different conclusions. Recompute the closed-loop equation for any changed plant rather than carrying the target roots forward unchanged.

## Tracking has its own limit calculation

The loop contains one integrator, so for an eligible stable unity-feedback response the velocity error constant is Kv=lim as s approaches zero of s C P=Kz/(2p). In the rehearsal Kv=8/3 and unit-ramp steady error is 3/8. A unit step instead has zero asymptotic error under these assumptions; the two inputs are different targets.

Derive the ramp result from its error transform E(s)=R(s)/[1+C P], with R=1/s², and check the final-value conditions. The formal limit is not a valid settling argument for an unstable loop. The worked design similarly gives Kv=27/8 and ramp error 8/27.

## Phase lead is frequency dependent

Controller phase is atan(omega/z)−atan(omega/p). Differentiating with respect to frequency shows maximum boost at omega=sqrt(pz). Its sine is (p−z)/(p+z), so the maximum is positive for the selected p>z form.

For the rehearsal the peak-boost frequency is four and boost is asin(5/13), about 22.619865 degrees. At that frequency controller magnitude is eight. Plant magnitude is one/(four sqrt20), so loop magnitude is one/sqrt5, about 0.44721360.

Therefore the frequency of greatest phase boost is not the unity-gain crossover in this example. Phase margin must use the actual loop crossover and unwrapped phase, not automatically the maximum controller phase. A lead controller changes magnitude as well as phase and can move crossover into a region with other lags.

A compatible one-state controller realization makes the added dynamics explicit. Let wdot=−p w+e, where e is tracking error, and command u=K e+K(z−p)w. Its zero-initial-state transfer is K+K(z−p)/(s+p), equal to the chosen compensator. Coupling it to the two-state plant gives three internal states, so their characteristic can be checked against the matched cubic. A nonzero initial w adds its own transient; it is not represented by assuming the controller starts at rest.

## Proper response and verification

The finite pole distinguishes this controller from an ideal unbounded differentiator. Its DC gain is Kz/p, while high-frequency gain tends to K. That finite increase can still amplify measurement noise; a stable pole does not prove a satisfactory noise or range budget.

Derive a compatible state realization or implement the original differential relations and compare a time response with the target modes. Verify steady ramp error, equilibrium residuals, initial conditions and integration refinement. Then make one documented plant-parameter perturbation and calculate the new roots and tracking result. Retain the comparison as a conditional model study rather than a guarantee over all uncertainty.

[MIT OCW 2.004 Spring 2008 calendar](https://ocw.mit.edu/courses/2-004-dynamics-and-control-ii-spring-2008/pages/calendar/) lectures 25–34 provide link-only root-locus/frequency scope; selected [16.30 Fall 2010 lecture topics](https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/pages/lecture-notes/) 2–4 support the classical-design connection. All controller examples and explanations here are original and AI-assisted, with no source problem, circuit, code or figure imported. General compensation synthesis, physical implementation, workload and qualified review remain open; the package stays partial and unreviewed.
