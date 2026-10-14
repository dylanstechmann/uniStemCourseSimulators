# Limits, continuity, and approximation

A limit describes nearby function values. It does not, by itself, describe the value assigned at the point. Continuity connects those two claims, and a local linear approximation uses nearby behavior to estimate a value. These ideas are useful for checking models, but a few measured points cannot prove that a real process follows a smooth curve.

## Approaching a point

Consider

\[
q(x)=\frac{x^2-1}{x-1},\qquad x\ne 1.
\]

Factoring gives \(q(x)=x+1\) wherever the original quotient is defined. Values at \(x=0.9, 0.99, 1.01, 1.1\) are respectively 1.9, 1.99, 2.01, and 2.1. From either side they approach 2, so \(\lim_{x\to 1}q(x)=2\), even though \(q(1)\) is not defined by the quotient. If a new function assigns \(q(1)=2\), it is continuous there. If it assigns \(q(1)=4\), the nearby values and limit are unchanged, but the function is discontinuous at 1.

This is why a limit is a statement about a punctured neighborhood: inputs approach 1 while staying different from 1. A graph may draw a hollow point at the missing value, but the algebra makes the domain restriction explicit. Canceling the factor \(x-1\) is valid only for \(x\ne 1\); it does not retroactively define the original quotient at the excluded input.

## Limits from both sides

For a two-sided limit at an interior point, the left-hand and right-hand values must approach the same number. Suppose a threshold response is modeled by \(r(t)=3\) for \(t<2\) and \(r(t)=6\) for \(t>2\). Its left limit at 2 is 3 and its right limit is 6. No choice for \(r(2)\) can make the two-sided limit exist, because assigning a value at one point does not change either side.

Continuity at \(a\) requires three things: \(f(a)\) is defined, the two-sided limit exists, and the limit equals \(f(a)\). At an endpoint of a domain, only the available one-sided limit is required. A table or graph can help reveal a jump or a missing point; it cannot settle every continuity question when the function between observations is unknown.

## A local line and its range

A derivative gives the slope of a tangent line, which can estimate the function near a reference input. Let \(f(u)=\sqrt{100+u}\) for \(u\ge -100\). At \(u=0\), the value is 10 and the slope is \(f'(0)=1/20=0.05\). The tangent approximation is

\[
L(u)=10+0.05u.
\]

At \(u=4\), the line gives 10.2 while the exact value is \(\sqrt{104}\approx10.198039\); the absolute error is about 0.001961. At \(u=20\), it gives 11 while \(\sqrt{120}\approx10.954451\), an error of about 0.045549. The approximation remains useful here, but the error grows as we move away from the reference input.

We can make that range claim more precise. The second derivative is

\[
f''(u)=-\frac{1}{4(100+u)^{3/2}}.
\]

For \(|u|\le25\), its magnitude is at most \(1/[4(75)^{3/2}]\approx3.850\times10^{-4}\). Taylor's remainder bound therefore gives

\[
|f(u)-L(u)|\le \tfrac12(3.850\times10^{-4})u^2.
\]

At \(u=20\), this rounded-up bound is 0.07700, larger than the actual error 0.045549 as a valid upper bound should be. The bound applies only on the stated interval. At \(u=50\), the tangent estimate is 12.5 and the exact value is about 12.247449, but the \(|u|\le25\) guarantee says nothing about that input. An approximation should travel with its reference point, error estimate, and declared range.

## Separate mathematical and measurement claims

For the exact function above, factoring and the remainder theorem justify the calculations. For experimental observations, a smooth-looking curve does not establish continuity or a derivative. The sampling interval, instrument resolution, noise, and model assumptions matter. A local line can summarize a chosen mathematical model without proving that the underlying biological, chemical, or mechanical process follows that model outside the observed range.

When evaluating a limit or using a local approximation, state the domain first, compare the left and right behavior, distinguish the limit from the assigned point value, and identify how far the approximation is justified. These checks make a calculation easier to interpret and harder to overstate.
