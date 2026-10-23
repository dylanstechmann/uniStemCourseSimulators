# Exact sampled PI states and Schur stability

A half-sample phase estimate is useful context, but a specified digital loop has an exact update order and state matrix. This original foundation derives a two-state PI implementation, proves its strict unit-circle conditions and compares it with a continuous-time design. All plant/gain values are normalized mathematical inputs, not controller settings for equipment.

## Preserve the sampling and update contract

For a first-order plant with a command held constant over each period T, the exact sampled relation is y[k+1]=a y[k]+b u[k], with a=exp(−T/tau), b=Kplant(1−a). Assume 0<a<1, b>0 and T>0. Let z store an integral of error and explicitly use its old value:

$$u[k]=k_p(r[k]-y[k])+k_i z[k], \qquad z[k+1]=z[k]+T(r[k]-y[k]).$$

For deviations about a constant-reference equilibrium, the state matrix is

$$A_d=\begin{pmatrix}a-bk_p&bk_i\\-T&1\end{pmatrix}.$$

The trace is t=1+a−bkp and determinant d=a−bkp+bkiT. Its characteristic is lambda²−t lambda+d. With physical units, z carries output-times-time, kp input-per-output and ki input-per-output-per-time; the trace, determinant and poles are dimensionless.

Using z[k+1] in the command instead would change the top row. An extra computational delay would add another state. Do not reuse the same characteristic after changing those timing rules. Clamping commands also creates a nonlinear implementation rather than preserving this global linear matrix.

For an attainable constant reference and nonzero ki, the ideal equilibrium has y*=r, u*=(1−a)r/b and z*=(1−a)r/(bki). Subtracting it gives the homogeneous matrix above. Existence of this algebraic equilibrium does not prove that a trajectory approaches it; the strict root conditions provide that missing step for the linear model.

The update contract also has an immediate check from y[0]=z[0]=zero and unit reference: y[1]=bkp and z[1]=T. Using the updated integrator in u[0] would add bkiT to that first output. One sample can therefore expose a timing mismatch that a final-value comparison misses.

## Derive strict unit-circle conditions

Map lambda=(1+eta)/(1−eta), which takes the left half eta-plane into the unit disk. Multiplying the characteristic by (1−eta)² gives

$$(1+t+d)\eta^2+2(1-d)\eta+(1-t+d).$$

For this real quadratic, strict left-half-plane roots require the three coefficients to share a positive sign. The all-negative alternative is impossible here because their sum is four. Thus the original roots lie strictly inside the unit circle exactly when

$$1-t+d>0, \qquad1+t+d>0, \qquad1-d>0.$$

These are the selected second-order Schur/Jury conditions. The bilinear boundary at lambda=-one and equality cases require care; strict inequalities deliberately exclude those marginal boundaries. A sign test for a continuous plant polynomial does not substitute for this discrete characteristic.

## Worked and distinct rehearsal

A worked model has a=b=0.5, T=one, kp=ki=one. Trace is one, determinant one half and poles one half plus or minus one-half i. Their common modulus is sqrt(one half), so the linear update decays.

For the rehearsal use a=0.8, b=0.2, T=one, kp=2, ki=one. Trace is 1.4 and determinant 0.6. Poles are 0.7 plus or minus i sqrt0.11, with modulus sqrt0.6. The three strict test quantities are 0.2, three and 0.4, all positive.

At fixed kp=two, the inequalities reduce to 0<ki<3. At ki=three the determinant is one and the conjugate pair lies on the unit circle, so this boundary is not asymptotically stable. At the separate ki=four the determinant is 1.2 and pole modulus sqrt1.2 exceeds one. The loop is unstable despite the stable open-loop plant.

## Continuous stability does not settle implementation stability

The rehearsal's scalar continuous plant can have Kplant=one, tau=−one/ln0.8 and T=one. A continuous PI controller with kp=two, ki=four has characteristic tau s²+3s+4, whose positive coefficients establish strict stability for this second-order continuous model. The stated sampled old-integrator implementation with those gains is nevertheless unstable.

The difference is not a contradiction:the two dynamical systems have different equations. Approximation quality, hold behavior and update timing matter. The exact normalized hold frequency factor is exp(−i omega T/2) times sinc(omega T/2). In its first lobe its phase includes the half-period term, but its magnitude is not identically one. Treating it as a pure delay at all frequencies drops information.

## Verification and model limits

Compare direct recurrence with matrix powers for stable, boundary and unstable cases under the same initial state. Include a repeated pole strictly inside the unit circle to distinguish polynomial-times-geometric decay from a boundary repeated pole. If adding saturation, state the actual stored-command/integrator policy and analyze that separate nonlinear sequence rather than claiming the linear inequalities prove it stable.

[MIT OCW 6.003 Fall 2011 calendar](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/calendar/) discrete approximation/Z-transform/sampling topics and selected [16.30 Fall 2010 digital-control scope](https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/pages/lecture-notes/) are link-only references. The derivation and examples are original and AI-assisted; no source code, problem, figure or data is imported. General delayed/multirate/quantized control, robust guarantees, physical implementation and qualified review remain open; the course stays partial and unreviewed.
