# Sequences, series, and approximation error

A sequence is an ordered list of terms $a_0,a_1,\ldots$. A series asks what happens when those terms are added. Its $N$th partial sum is $S_N=\sum_{n=0}^N a_n$, and the infinite series converges only if the sequence of partial sums approaches a finite limit. The terms themselves must approach zero for that to happen, but this necessary condition is not sufficient: the harmonic terms $1/n$ tend to zero while their partial sums grow without bound.

## A geometric series has an exact tail

For a geometric series with first term 1 and ratio $r$, its finite partial sum is

$$
S_N=1+r+r^2+\cdots+r^N=\frac{1-r^{N+1}}{1-r}\quad(r\ne1).
$$

When $|r|<1$, the omitted powers tend to zero and the partial sums approach $1/(1-r)$. The tail after including terms through index $N$ is exactly

$$
R_N=\frac{r^{N+1}}{1-r}.
$$

For a negative ratio the tail alternates in sign; its magnitude is $|r|^{N+1}/|1-r|$. A small next term is not itself the full error: the denominator accounts for all later terms.

Set $r=0.2$. The infinite sum is $1/(1-0.2)=1.25$. Keeping terms through $n=2$ gives $1+0.2+0.04=1.24$. The exact remaining tail is $0.2^3/(1-0.2)=0.01$, so the approximation is low by precisely 0.01. This geometric-series remainder formula applies because the omitted terms continue with the same ratio; it is not a universal error bound for arbitrary approximations.

For $r=0.4$, the partial sum through $n=3$ is $1+0.4+0.16+0.064=1.624$, while the total is $1/(1-0.4)=5/3$. Its tail is $0.4^4/(1-0.4)=0.042666\ldots$. If a calculation requires absolute error at most 0.001, four terms are insufficient; continue until the exact tail bound is below the stated tolerance. State whether the final retained index is $N$ or whether $N$ denotes the number of terms, since those conventions differ by one.

## A series test needs its hypotheses

The condition $a_n\to0$ can reject a divergent series when it fails. Passing that check does not decide convergence, as the harmonic example shows. For positive terms, the p-series test says $\sum_{n=1}^{\infty}1/n^p$ converges when $p>1$ and diverges when $p\le1$. Other tests answer other structural questions: a comparison needs a valid inequality, a ratio limit below 1 controls a tail, and a ratio limit of 1 is inconclusive. Later readings develop positive, alternating and power-series tests with their assumptions and endpoint checks.

Convergence is a statement about the infinite tail. Changing finitely many terms can change the sum but not whether the series converges. A finite partial sum is always computable; its existence says nothing by itself about the limit of all partial sums.

## Taylor approximation has a different error argument

A Taylor polynomial is another finite sum, but its error is generally controlled by a Taylor remainder theorem rather than by the geometric-tail formula. For $e^x$ near zero, $P_2(x)=1+x+x^2/2$. At $x=0.5$, it gives $1.625$. On $[0,0.5]$, the third derivative is $e^x\le e^{0.5}$, so the Lagrange bound is

$$
|R_2(0.5)|\le e^{0.5}\frac{0.5^3}{3!}<0.0344.
$$

The actual error $e^{0.5}-1.625$ is about 0.02372, within that bound. The bound guarantees an interval containing the error; it does not say that the error equals the upper limit. A valid remainder claim names the degree, interval and derivative bound. The later Taylor lessons provide other estimates, including error integrated over an interval.

When reporting a truncated sum, identify the terms kept, give the value and the error bound, and state the interval or convergence conditions that justify it. These examples are mathematical constructions: an error bound for the stated function does not cover data noise, a different model or unrepresented behavior.
