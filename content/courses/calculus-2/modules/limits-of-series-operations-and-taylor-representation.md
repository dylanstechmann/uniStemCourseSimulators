# Limits of series operations and Taylor representation

The power-series reading permits termwise operations on justified interior intervals. The Taylor reading warns that smoothness alone does not guarantee representation by a Taylor series. This original extension supplies explicit bounds and counterexamples so those qualifications can be checked. It selects elementary examples relevant to calculus operations; it is not a replacement for a real-analysis course. All functions and numerical targets are synthetic mathematical exercises.

## Pointwise and uniform claims quantify differently

For $f_n(x)=x^n$ on $[0,1]$, each fixed $x<1$ has limit zero while $f_n(1)=1$. The pointwise limit is therefore zero except at the right endpoint. Uniform convergence would require one index after which the error is small at every point simultaneously. Here the supremum error from that limit is one for every $n$: points sufficiently close to one from below keep the error arbitrarily near one. That supremum need not be attained at an interior point.

On a smaller interval $[0,r]$ with fixed $r<1$, the limit is zero throughout and $\sup|f_n|=r^n\to0$, a uniform bound. At $r=1/2,n=10$, it is $2^{-10}=9.765625\times10^{-4}$. Ten is the smallest positive integer exponent making this certificate strictly below 0.001. An interval's endpoint is part of the theorem's hypotheses, not a cosmetic plotting choice.

Despite the lack of uniform convergence on $[0,1]$, the integrals $\int_0^1x^n dx=1/(n+1)$ tend to zero, equal to the integral of the pointwise limit. Uniform convergence is one sufficient way to justify an interchange under the relevant integration hypotheses, not a necessary condition in every example. Do not mistake a failed sufficient condition for proof that the interchange fails.

## Pointwise convergence alone can still fail for integrals

For integers $n\geq2$, construct a continuous triangular function: $h_n(x)=n^2x$ on $[0,1/n]$, $h_n(x)=n(2-nx)$ on $[1/n,2/n]$, and zero afterward. The two pieces meet at height $n$, and the triangle has base $2/n$ and area one.

For every fixed $x>0$, eventually $x>2/n$, so $h_n(x)=0$; at zero it is already zero. Thus the pointwise limit is zero everywhere, but each integral is one. Integrating the pointwise limit gives zero instead. At $n=5$, height is five and base is 0.4, while area remains one. A fixed plotting grid can eventually miss the narrow peak, making a graph or sampled integral particularly misleading.

This counterexample uses continuous piecewise-linear functions and an elementary area calculation. It does not require an advanced integration theorem. It shows what a claim based only on pointwise convergence leaves uncontrolled: the position, width and height of the error can change with the index.

## A uniform tail bound for a power series

Consider $\sum_{n=1}^{\infty}x^n/n^2$ on $[0,1]$. Every omitted term is bounded by $1/n^2$, so the tail after index $N$ has the point-independent certificate

$$\sup_{0\leq x\leq1}\left|\sum_{n>N}\frac{x^n}{n^2}\right|\leq\sum_{n>N}\frac1{n^2}\leq\int_N^\infty\frac{dt}{t^2}=\frac1N.$$

This proves uniform convergence through the endpoint for the original series. At $N=100$, the certificate is 0.01. It is an upper bound, not an assertion that the actual error equals 0.01.

The formally differentiated series is $\sum_{n=1}^{\infty}x^{n-1}/n$. It converges at interior $x$ but becomes harmonic at one. Inside the interval its value is $-\ln(1-x)/x$, with the removable value one at zero; at $x=1/2$ it equals $2\ln2$. Uniform convergence of the original series alone does not establish a uniformly convergent derivative series or a finite endpoint derivative. Differentiation requires its own justification and domain. Integration under a valid uniform bound is a different operation with different sufficient conditions.

## Smooth does not mean equal to a Taylor series

Define $F(0)=0$ and $F(x)=e^{-1/x^2}$ for $x\ne0$. Repeated differentiation away from zero produces a polynomial in $1/x$ times the same exponential. Every such product tends to zero as $x\to0$. To see the dominance explicitly, put $u=1/x^2$ and bound $u^{m/2}e^{-u}$ using $e^u\geq u^k/k!$ with an integer $k>m/2$.

Inductively, the derivative at zero is also zero: each difference quotient introduces only another power of $1/x$, still dominated by the exponential. Thus every derivative at zero exists and vanishes. Every Taylor polynomial centered at zero is the zero polynomial, yet $F(1/2)=e^{-4}\approx0.0183156$ is positive. The Taylor series converges to zero and does not represent this smooth function away from its center.

This does not invalidate finite-order Taylor's theorem. Its derivative bound must hold over the relevant interval and may depend on the order; it need not make the remainder tend to zero as order grows. A finite remainder certificate and an infinite representation claim are different statements.

## Evidence and scope

Retain a domain, quantifier and bound ledger before interchanging limits, integrals or derivatives. The [MIT OCW 18.01SC Fall 2010 Taylor-series scope](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-5-exploring-the-infinite/part-b-taylor-series/) motivates explicit approximation/operation conditions; these original selected counterexamples deepen the local qualification without claiming a full analysis curriculum. No source proof, problem or text is imported. Content is AI-assisted, partial and unreviewed; general function-series theory, measured workload and qualified mathematical review remain open.
