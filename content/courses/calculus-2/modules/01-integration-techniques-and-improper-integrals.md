# Integration techniques and improper integrals

An integral can be difficult for two different reasons: its antiderivative may require a method choice, or its interval may be unbounded or contain a singularity. Separate those questions. First inspect the algebraic structure to choose a technique; then verify the antiderivative by differentiating it. If an endpoint is infinite or the integrand is unbounded, replace that endpoint by a variable cutoff and take a limit. A finite-looking plot is not a convergence test.

## Choose a method from the integrand

Substitution is useful when part of the integrand is the derivative of an inner expression. For

$$
\int_0^2\frac{2x}{x^2+3}\,dx,
$$

set $u=x^2+3$, so $du=2x\,dx$ and the bounds change from 0 and 2 to 3 and 7. The integral becomes $\int_3^7du/u=\ln(7/3)$. Differentiating $\ln(x^2+3)$ returns the original integrand. Substitution changes the variable, differential and bounds together.

Integration by parts follows the product rule:

$$
\int u\,dv=uv-\int v\,du.
$$

It is useful when differentiating one factor simplifies it and integrating the other is manageable. For $\int_0^1x\ln x\,dx$, choose $u=\ln x$ and $dv=x\,dx$. Then $du=dx/x$ and $v=x^2/2$, giving the antiderivative $x^2\ln x/2-x^2/4$. At the lower endpoint, $\lim_{x\to0^+}x^2\ln x=0$, so the integral is $-1/4$. That endpoint limit matters: substituting $x=0$ directly into the intermediate logarithm is not valid.

Partial fractions are useful for a rational function with a factorable denominator. Since

$$
\frac{1}{(x+1)(x+3)}=\frac12\left(\frac{1}{x+1}-\frac{1}{x+3}\right),
$$

integration gives $\frac12\ln|(x+1)/(x+3)|+C$ on intervals that do not cross either pole. On $[0,1]$, the integral is $\frac12\ln(3/2)$. The absolute values preserve the real logarithm's domain; an antiderivative formula is valid only on an interval that avoids its singularities.

These patterns are clues, not a mechanical classifier. After obtaining a primitive, differentiate it, check that every denominator stays nonzero on the interval, and only then apply the bounds. Numerical agreement can help catch arithmetic errors but cannot establish that a proposed antiderivative is correct everywhere.

## Infinite intervals are limits

An integral to infinity is defined by a limit of finite-interval integrals. For $p\ne1$,

$$
\int_1^B x^{-p}\,dx=\frac{B^{1-p}-1}{1-p}.
$$

As $B\to\infty$, this has a finite limit $1/(p-1)$ when $p>1$. At $p=1$, the integral is $\ln B$ and grows without bound; for $p<1$, the power term also grows without bound. Thus $\int_1^\infty x^{-p}\,dx$ converges exactly when $p>1$. The fact that $x^{-p}$ tends to zero is insufficient by itself: the harmonic integrand $1/x$ tends to zero, but its integral diverges.

An endpoint singularity also requires a limit, even when the interval is finite. For $p\ne1$,

$$
\int_\epsilon^1x^{-p}\,dx=\frac{1-\epsilon^{1-p}}{1-p}.
$$

Taking $\epsilon\to0^+$ gives a finite limit when $p<1$, and divergence when $p\ge1$. If a singularity lies inside an interval, split the integral there and require both one-sided integrals to converge. Cancellation across a singularity does not make the ordinary improper integral converge.

## A decaying exposure example

For a constructed exponential curve $C(t)=C_0e^{-kt}$ with $C_0>0$ and $k>0$,

$$
\int_0^B C_0e^{-kt}\,dt=\frac{C_0}{k}(1-e^{-kB})
\quad\longrightarrow\quad
\int_0^\infty C_0e^{-kt}\,dt=\frac{C_0}{k}.
$$

The limit exists because the exponential decays for positive $k$. If $k=0$, the curve is constant and its integral over an infinite interval diverges. For $k<0$, the curve grows and also has no finite total. In the convergent case the units of $C_0/k$ are concentration times time. This is a mathematical example only: its parameters are constructed and imply no real exposure, biological behavior or dosing conclusion.

## A checking routine

Before reporting an integral, state the interval and any excluded points, identify the method, verify the resulting derivative, and inspect every endpoint that can cause an infinite limit. Evaluate the finite expression before taking a limit. Convergence is part of the answer, not a detail that can be inferred from a small graph or from a rate approaching zero.
