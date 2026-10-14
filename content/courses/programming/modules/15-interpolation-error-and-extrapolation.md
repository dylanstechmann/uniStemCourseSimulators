# Interpolation: exact fit at nodes, error between them

Regression estimates a trend from observations under a chosen loss function. Interpolation solves a different problem: it constructs a function that passes through the supplied tabulated values. This lesson builds a quadratic interpolant, checks it against a known function between nodes, and shows why interpolation does not automatically justify extrapolation.

## Learning objectives

By the end of this lesson, you should be able to:

1. Construct and evaluate a low-degree Lagrange interpolant from tabulated values.
2. Compare interpolated values with a known function and describe the error and domain limits.
3. Choose between interpolation and regression for exact tables and noisy measurements.

## Lagrange interpolation

For distinct nodes \(x_0,\ldots,x_n\), the degree-at-most-\(n\) interpolant is

\[
  p_n(x)=\sum_{i=0}^{n} y_i L_i(x),\qquad
  L_i(x)=\prod_{j\ne i}\frac{x-x_j}{x_i-x_j}.
\]

Each basis function is one at its own node and zero at the others. Therefore \(p_n(x_i)=y_i\) for every supplied pair. That exact match is part of the construction; it does not show that the table has no measurement noise or that the function is accurately represented between nodes.

## Worked example: a quadratic between three nodes

Take the smooth function \(f(x)=1/(1+x^2)\) and the synthetic table

| \(x_i\) | 0 | 1 | 2 |
|---:|---:|---:|---:|
| \(y_i=f(x_i)\) | 1 | 0.5 | 0.2 |

The Lagrange basis gives

\[
  p_2(x)=1-0.6x+0.1x^2.
\]

At \(x=0.5\), the interpolant gives \(p_2(0.5)=0.725\), whereas the known function gives \(f(0.5)=0.8\). The signed interpolation error \(p_2-f\) is \(-0.075\). A straight-line interpolation using only the first two nodes gives 0.75 at the same point, so adding a node did not improve this particular local estimate. Error depends on the function, node locations and degree.

The classical remainder formula is

\[
  f(x)-p_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x-x_i)
\]

for some \(\xi\) in the interval containing the nodes and evaluation point, when the required derivatives exist. It explains why both node geometry and function curvature matter. At \(x=4\), outside the sampled interval \([0,2]\), the same polynomial gives \(p_2(4)=0.2\), while \(f(4)=1/17\approx0.0588\). This is extrapolation, where the data provide less control over the result.

## Interpolation or regression?

- Interpolation is suitable when the supplied values are to be reproduced exactly, such as a trusted table or a deterministic model sampled at selected inputs.
- Regression is usually preferable when observations contain noise and the goal is to estimate a trend or relationship. A least-squares fit generally will not pass through every noisy point.
- High-degree global polynomials can oscillate, particularly near the ends of evenly spaced intervals. Piecewise methods can be more stable, but their choice and error properties require separate analysis.
- Neither a small interpolation error on one example nor an exact match at the nodes establishes validity outside the sampled domain.

MIT OCW 2.086 Fall 2014 places interpolation in its opening numerical-calculus unit and later treats least-squares fitting and regression. This lesson is a small original comparison, not that full numerical-methods sequence; the course still omits a systematic interpolation algorithm and implementation study.
