# Power series and Taylor error

A Taylor polynomial builds a local model from the value and derivatives of a function at a chosen center. The degree tells how many derivative terms are retained; a remainder theorem then bounds what was left out. This is different from checking a few decimal digits or assuming that the next term equals the entire error.

## Build a polynomial at zero

For $f(x)=e^x$, every derivative equals $e^x$, so every derivative at zero is 1. The degree-two Taylor polynomial is

$$
P_2(x)=1+x+\frac{x^2}{2}.
$$

At $x=0.2$, it gives $1+0.2+0.2^2/2=1.22$. The actual function value is $e^{0.2}\approx1.2214028$, so the absolute error is about 0.0014028. This difference is small for this input, but a decimal comparison alone does not certify a guaranteed accuracy.

## Attach a Lagrange error bound

If the $(n+1)$st derivative is bounded in magnitude by $M$ between the center $a$ and the input $x$, Taylor's theorem gives

$$
|R_n(x)|\le M\frac{|x-a|^{n+1}}{(n+1)!}.
$$

For $e^x$ on $[0,0.2]$, the third derivative is at most $e^{0.2}$. Therefore

$$
|R_2(0.2)|\le e^{0.2}\frac{0.2^3}{3!}<0.00163.
$$

The actual error is below this guaranteed upper limit. At $x=0.5$, the same polynomial gives 1.625, the actual error is about 0.0237213, and the valid bound on $[0,0.5]$ is $e^{0.5}(0.5)^3/3!<0.0344$. The larger distance from the center requires a larger bound here.

The interval matters because $M$ must bound the derivative everywhere between $a$ and $x$, not only at the center or endpoint. The factorial and distance power both depend on the polynomial degree. To meet a prescribed absolute tolerance, compute a valid bound and raise the degree or shrink the interval until that bound is below the target. If no suitable derivative bound is known, the displayed certificate has not been established.

## Finite polynomials and infinite series

A Taylor polynomial is a finite expression and can be evaluated whether or not the associated infinite Taylor series converges at a particular input. If the infinite series does converge to the function, its partial sums approach the function value; a separate convergence argument is needed to establish that fact. For $e^x$, the series $\sum_{n=0}^\infty x^n/n!$ converges for every real $x$. Other power series have a finite radius, and their endpoints need separate tests; the later power-series lesson develops those questions.

A geometric tail formula applies only when the omitted terms share a fixed ratio. A Taylor Lagrange bound instead uses a derivative over an interval. Alternating-series bounds and integrated Taylor remainders use their own assumptions. Name the theorem that supports an error claim rather than borrowing a formula because the terms appear to shrink.

## Reporting an approximation

State the center, degree and input, then report the polynomial value and a justified error bound. Distinguish actual error, which compares with the exact value, from a guaranteed bound, which may be larger. If units are present, keep them attached to the modeled quantity; the independent variable's units must be consistent with the derivatives. These examples use a constructed mathematical function and say nothing about measurement noise or a separate model's accuracy.
