# Oxygen-probe dynamics and parameter identifiability

The existing virtual lab fits a first-order oxygen-transfer trace. Its result depends on what the reported signal represents. A probe with its own response time can smooth the liquid's trajectory and make a one-exponential fit misleading. This reading derives a two-state observation model, an exact ambiguity and the evidence needed to resolve it. All inputs and traces are analytic normalized examples; this is a mathematical data exercise, not an experimental procedure or a probe calibration claim.

## Separate the process state from its observation

For a stipulated unit step in normalized equilibrium concentration, use

$$C'=k(1-C),\qquad P'=a(C-P),\qquad C(0)=P(0)=0,$$

where $C$ is liquid concentration, $P$ is the probe state, $k>0$ is the process transfer rate and $a>0$ the probe response rate. A common time basis is required. The probe time constant is $1/a$ and the process time constant is $1/k$. A small ratio $k/a$ supports a fast-probe approximation; it does not make that approximation exact at every initial time.

This first model has no consumption, constant volume and a fixed imposed equilibrium boundary. A separate uptake term can be introduced only by changing and verifying the process equation. Normalization to one removes units for this exercise; it does not supply a real saturation concentration or an instrument operating condition.

The liquid solution is $C=1-e^{-kt}$. Solving the probe equation by an integrating factor gives, for $a\ne k$,

$$P(t)=1-\frac{a e^{-kt}-k e^{-at}}{a-k}.$$

At equal rates the expression has a removable singularity, with limit

$$P(t)=1-(1+kt)e^{-kt},\qquad a=k.$$

Use this limit or a numerically stable evaluation near coincident rates; subtracting nearly equal exponentials can lose significant digits. A denominator near zero is not evidence that the physical state diverges.

## Initial slopes and a worked comparison

The liquid initially rises at rate $k$, but $P'(0)=a(C_0-P_0)=0$. Differentiating once more gives $P''(0)=ak$. Thus the probe trace starts with curvature even though the liquid has a nonzero initial slope. This distinguishes a measurement delay from a delayed physical transfer onset within the stated model.

For a worked case use $k=2,a=4$. At $t=0.5$, $C=1-e^{-1}\approx0.632121$ and

$$P=1-2e^{-1}+e^{-2}\approx0.399576.$$

If one incorrectly treats that single observed probe point as the true liquid state, the estimate $k_{app}=-\ln(1-P)/t$ is about 1.02 rather than two. Derive its actual value from the supplied expression rather than using that rounded illustration. A fit to many points may still have a small residual while estimating the wrong model parameter.

A distinct rehearsal uses $k=1,a=3$. At $t=1$, $C=1-e^{-1}$ and $P=1-(3e^{-1}-e^{-3})/2$. The probe's second initial derivative is three. For equal rates $k=a=2$ at $t=0.5$, $P=1-2e^{-1}\approx0.264241$. These are different systems; keep their states and initial conditions separate.

## An exact ambiguity, not merely noisy fitting

Exchange the parameters $k$ and $a$ in the formula for $P$. Both numerator and denominator change sign, leaving exactly the same observed trace at every time. Equivalently the transfer factor from the boundary input to $P$ is $ka/[(s+k)(s+a)]$, symmetric in its two rates. The trace can identify an unordered pair under favorable ideal conditions, but cannot tell which rate belongs to the process and which to the probe without additional information.

The liquid trajectory does change when the rates are exchanged. At the worked half-time, the alternative process rate four gives $C=1-e^{-2}$ while preserving the same $P$. Consequently an excellent probe-only fit does not establish the liquid's transient. More samples of that same ideal output do not remove a structural symmetry. Independent information assigning the probe rate, a second justified observation or a controlled change with known equation effects is needed.

The companion analytic table contains only normalized time and $P$, rounded for file delivery. It is generated from the worked model, not measured, and deliberately does not identify the two rates by labeling a hidden liquid column. Rounding creates a finite numerical tolerance; it does not supply sampling uncertainty, instrument noise or biological replication.

## Consumption and steady-state limits

For a separate constant-uptake model write $C'=k(C^*-C)-u$ and retain $P'=a(C-P)$. A steady state has $C_*=P_*=C^*-u/k$. Probe lag does not change that open-loop steady value, though it changes the observed transient and can matter in a closed loop. A physical lower concentration limit requires $u\leq k(C^*-C_{min})$ within this simplified model. A negative formal steady concentration signals failure of the constant-uptake/state assumptions before it supplies a valid physical prediction.

One steady plateau constrains only the ratio $u/k$ when $C^*$ is known. It does not separately identify uptake and transfer. An actuator command, a probe value and a true local state should therefore occupy different columns in an evidence ledger.

## Verification and scope

Implement the two differential equations and compare with both unequal- and equal-rate formulas. Check zero initial values, the initial slope/curvature, long-time limit and invariance under swapping the rates. Repeat after assigning a known probe rate and report what ambiguity remains. Use residuals, sensitivity and controlled comparisons separately; a solver or optimizer success flag does not establish identifiability.

The [MIT OCW 10.442 Spring 2005 calendar](https://ocw.mit.edu/courses/10-442-biochemical-engineering-spring-2005/pages/calendar/) mass-transfer/design strands and the local gassing-out/control readings motivate this original extension. No source data, instrument specification or procedure is imported. General sensor chemistry, measurement noise, nonlinear uptake and validated control design remain outside this selected model. All content is original and AI-assisted; the package remains partial and unreviewed.
