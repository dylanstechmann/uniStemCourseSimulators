# Fourier filtering, periodic solutions and truncation evidence

The existing forced-chamber reading uses a few harmonics of one periodic input. A harmonic approximation becomes more useful when we can explain its coefficient conventions, distinguish periodic response from initial-value response, and bound what truncation omits. This original mathematical example uses a unit square input in normalized time; it is not a sampled experimental signal. The derivation connects the existing first-order, Fourier and convolution readings without importing a university problem.

## Fix the input and coefficient convention

Let $u(t)$ be $2\pi$-periodic, equal to one for $0<t<\pi$ and minus one for $-\pi<t<0$. Values at the jumps do not affect its integrals. With

$$u(t)\sim a_0/2+\sum_{n=1}^{\infty}(a_n\cos nt+b_n\sin nt),$$

the coefficients use $1/\pi$ times an integral over $[-\pi,\pi]$. Odd symmetry sets the cosine coefficients and mean to zero. Direct integration gives $b_n=4/(\pi n)$ for odd positive $n$, and zero for even $n$. This identifies both a normalization and a parity pattern; a formula copied from a different period convention can have different frequencies or prefactors.

At a continuity point the series converges to the stated input. At each jump it converges to the average of the two one-sided values, zero here. Finite partial sums exhibit overshoot near the jump and do not converge uniformly to this discontinuous input. More terms narrow the transition region; they do not remove the limiting relative overshoot. These input-series facts do not automatically describe the smoothness or convergence of the filtered output.

## Solve each harmonic, with its phase

Drive $y'+a y=u(t)$ with $a>0$. For one sine input $b_n\sin nt$, seek $A_n\sin nt+B_n\cos nt$. Matching sine and cosine coefficients gives

$$A_n=\frac{a b_n}{a^2+n^2},\qquad B_n=-\frac{n b_n}{a^2+n^2}.$$

The response amplitude is $|b_n|/\sqrt{a^2+n^2}$, and its lag relative to the sine is $\arctan(n/a)$. Both coefficients matter: retaining only an amplitude and the wrong phase changes the output at every observation time. The periodic response is the sum of these particular responses. A nonzero-mean input would additionally supply the constant response $\overline u/a$.

For a worked case choose $a=2$. The fundamental has input amplitude $4/\pi$, response sine coefficient $8/(5\pi)$ and cosine coefficient $-4/(5\pi)$. Its amplitude is $4/(\pi\sqrt5)\approx0.569410$ and lag $\arctan(1/2)\approx0.463648$ radians. The third harmonic has amplitude $4/(3\pi\sqrt{13})\approx0.117711$. Filtering has reduced its size relative to the fundamental more strongly than the raw input coefficient ratio of one third.

The distinct rehearsal uses $a=1$. Its fundamental amplitude is $4/(\pi\sqrt2)$, sine coefficient $2/\pi$, cosine coefficient $-2/\pi$ and lag $\pi/4$. The third-harmonic amplitude is $4/(3\pi\sqrt{10})$. Compute the amplitude ratio from those two outputs rather than assuming it remains the input ratio.

## A conservative uniform output-tail bound

For every omitted odd harmonic above index $N$, its output amplitude is at most $4/(\pi n^2)$ because $\sqrt{a^2+n^2}\geq n$. By the triangle inequality and a decreasing-function integral bound,

$$\sup_t |y_{\rm per}(t)-y_N(t)|\leq\frac4\pi\sum_{n>N}\frac1{n^2}\leq\frac4{\pi N}.$$

The middle sum includes even indices too, so the bound is deliberately conservative. It is valid for the periodic output and integer $N\geq1$, not a claim that the actual worst error equals the bound. Absolute summability proves uniform convergence of the output series even though the input series is not uniformly convergent. At $N=20$ the certificate is $1/(5\pi)\approx0.0636620$. To guarantee this certificate is below 0.02, choose an integer strictly larger than $4/(0.02\pi)$; $N=64$ works.

Do not infer term-by-term differentiability from uniform convergence of the output alone. The differential equation has a discontinuous input: the periodic output is continuous but has different one-sided derivatives at each input jump. Away from the jumps the differential equation can be checked using stronger local convergence reasoning or the separate piecewise exact solution.

## Independent periodic reference from a half-cycle map

For $a>0$ define $E=e^{-a\pi}$. During the positive half cycle,

$$y(t)=1/a+(y(0)-1/a)e^{-at},\quad0\leq t\leq\pi.$$

Half-cycle antisymmetry of the unique periodic response gives $y(\pi)=-y(0)$. Substitution yields

$$y_{\rm per}(0)=-\frac{1-E}{a(1+E)}.$$

For $a=1$ this is approximately $-0.917152$. The negative half-cycle solution follows by antisymmetry. A full-cycle map contracts differences by $e^{-2a\pi}<1$, proving a unique periodic state and attraction to it. This exact piecewise reference provides a comparison independent of Fourier truncation.

An IVP with initial value $y_0$ adds the homogeneous correction $(y_0-y_{\rm per}(0))e^{-at}$. Thus a periodic-tail certificate alone does not bound the error from omitting the initial transient. For example, starting at zero is generally not the same as starting on the periodic orbit. A total error budget must include both harmonic truncation and the missing homogeneous term, plus numerical or input-representation errors if present.

## Evidence and limits

Implement a harmonic sum and the piecewise map separately. Sample densely near switches, compare maximum errors with the conservative bound, and show why a finite grid cannot prove a supremum bound. Check phase, periodicity and the jump in one-sided derivatives. The [MIT OCW 18.03SC Fall 2011 Unit III](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/) is a link-only scope comparator. The text, parameters and tasks are original and AI-assisted. General Fourier convergence theory, arbitrary signals and nonlinear harmonic balance remain deferred; the course is partial and unreviewed.
