# Assignment 3: feedback modes and operating claims

This open report connects finite DC feedback, a three-state dynamic model and numerical transient verification. It asks whether a proposed closed-loop equilibrium actually attracts nearby states. The poles and gains are invented teaching inputs, not a particular amplifier's measured response or a compensation prescription. Retain the derivation, code, plots and report locally; browser checkpoints assess selected values and interpretations only.

## Part A: a distinct stable loop

Use $A(s)=A_0/(1+s/\omega)^3$ with $A_0=120$, $\omega=1000$ rad/s and constant negative-feedback fraction $\beta=0.025$. Define G=$\beta A_0$. Derive the closed-loop transfer from the input-error equation and form its characteristic polynomial before calculating any DC gain.

Here G=3 and the formal DC gain is 30. Let $q=\sqrt[3]3$. The characteristic roots are $-1000(1+q)$ and $1000(-1+q/2)\pm500\sqrt3 q\,i$ per second. The pair's real part is approximately -278.875215 and its positive imaginary magnitude approximately 1249.02477. Every real part is negative, so the homogeneous deviations decay in this stipulated model.

Recover these roots independently from the compatible three-state matrix. Verify its characteristic polynomial and use a separate numerical eigensolver or exact calculation as a check. Do not infer a response peak or settling time solely from one pole without specifying the input, residues and error criterion.

## Part B: a separate stronger-feedback variant

Keep A0 and omega fixed but set $\beta=8/15$, giving G=64. The real pole is -5000 per second, while the pair has real part +1000 and imaginary magnitudes $2000\sqrt3\approx3464.10162$ per second. Its formal DC gain is $120/65=24/13$.

Explain why that finite algebraic DC value does not establish an attracting output. The negative-feedback sign and stable open-loop poles have not prevented a growing closed-loop mode. The threshold G=8 belongs to this three-identical-pole model; changing the pole distribution or feedback network requires rederiving the characteristic equation rather than reusing the threshold.

Compare a small zero-input perturbation with a constant-input equilibrium calculation. The former directly exposes homogeneous growth/decay; the latter alone supplies only a candidate state. Label the two variants separately and do not insert the stronger-feedback gain into the stable variant's pole calculation.

## Part C: numerical transient and domain evidence

Implement the three lag states explicitly. For each variant, compute the equilibrium for a small stipulated input and simulate a nearby initial condition. Compare with a matrix-exponential reference or another independently verified linear-system solution at common times. Use at least three successively halved steps and report error and observed order where the reference and rounding permit it.

For the unstable variant, define a clearly stated linear-range event and stop when the assumed domain is left. The event is a study boundary, not a real device rating. An arbitrary hard clamp after integration changes the model and cannot be used to claim that the original linear response became stable. If you choose to analyze a nonlinear clamp, write its new equations and preserve the distinction.

Retain initial-derivative checks, original-state residuals, eigenvalues and transient errors. A visually bounded plot over a short observation window need not rule out an unstable slow mode. Conversely, a numerically exploding curve needs refinement and a reference comparison before its growth is attributed to the exact model rather than an unstable time step.

## Part D: limited compensation exploration

Propose one explicit model change that might alter the modes, such as a different first-pole coefficient or a frequency-dependent feedback law. Derive the new state or characteristic model and test it. Do not claim that changing a coefficient in this invented loop supplies a validated compensation design for a real amplifier and load.

Discuss bandwidth, finite DC gain, dynamic stability, output/input range, noise and slew as distinct constraints. The selected transfer model includes only some of them. Missing constraints should be listed with the information needed to evaluate them, rather than assigned invented product values.

## Self-review and scope

The retained report should contain input/error conventions, characteristic and state-matrix derivations, the stable/unstable comparison, equilibrium-versus-mode reasoning, numerical refinement and a clearly labeled domain limit. Browser practice does not evaluate code, compensation proposals or circuit safety. [MIT OCW 6.002 Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) lecture 23 and [Texas Instruments SLOA020A](https://www.ti.com/lit/an/sloa020a/sloa020a.pdf) are link-only stability concept references. All models, parameters and tasks are original and AI-assisted; no source circuit, figure or problem is imported. Experimental validation, measured workload and qualified review remain open; the course stays partial and unreviewed.
