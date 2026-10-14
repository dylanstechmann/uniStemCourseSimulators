# Rolle's Theorem, the Mean Value Theorem and consequences

The derivative gives local rates. The Mean Value Theorem (MVT) connects one of those local rates to the average rate across an entire interval. Its hypotheses matter: without continuity at the endpoints or differentiability inside, the conclusion can fail. The examples below use exact functions, not measured data.

## Learning objectives

1. Verify continuity and differentiability hypotheses, then apply Rolle's Theorem or the MVT.
2. Use the theorem to justify monotonicity and uniqueness, while separating existence from uniqueness of the point guaranteed by MVT.
3. Turn a derivative bound into a finite-interval change bound and state what assumptions support it.

## The theorem and its hypotheses

If f is continuous on the closed interval [a,b] and differentiable on the open interval (a,b), then there is at least one c in (a,b) such that

f'(c) = [f(b) - f(a)]/(b - a).

The right side is the secant slope, or average rate of change. The theorem does not say which c works, and more than one may work. Continuity is required on the whole closed interval; differentiability is required only at interior points.

One proof builds the secant line L through (a,f(a)) and (b,f(b)), then sets g=f-L. The function g is continuous on [a,b], differentiable on (a,b), and has g(a)=g(b)=0. Rolle's Theorem gives an interior point c with g'(c)=0. Since g'=f'-(f(b)-f(a))/(b-a), that c satisfies the MVT equation. Rolle's Theorem is the special case f(a)=f(b), where the secant slope is zero.

For f(x)=x² on [1,3], the secant slope is (9-1)/(3-1)=4. Since f'(x)=2x, c=2 satisfies f'(c)=4. For f(x)=x²-1 on [-1,1], the endpoint values agree and Rolle's point is c=0.

## Why the hypotheses cannot be dropped

Define f(0)=0 and f(x)=1 for 0<x≤1. Its secant slope on [0,1] is 1, but f'(x)=0 at every interior point. The function is not continuous at 0, so the MVT does not apply.

For f(x)=|x| on [-1,1], the secant slope is zero, but f'(x) is -1 to the left of zero and +1 to the right. The function is not differentiable at the interior point zero, so Rolle's Theorem does not apply. These examples show why endpoint continuity and interior differentiability are separate checks.

## Monotonicity and uniqueness

Let x<y in an interval where f is continuous on [x,y] and differentiable on (x,y). MVT gives a point c between them with f(y)-f(x)=f'(c)(y-x). If f'(t)>0 throughout the interval, then f(y)>f(x), so f is strictly increasing. If f'(t)≥0, the same argument gives f(y)≥f(x), so f is nondecreasing. This is the justification behind derivative-sign analysis.

For p(x)=x³+x-1 on [0,1], p is continuous, p(0)=-1 and p(1)=1, so the Intermediate Value Theorem gives at least one root. Also p'(x)=3x²+1>0, so MVT implies p is strictly increasing and therefore has at most one root. Together these results prove exactly one root in (0,1). A derivative sign can establish uniqueness; it does not by itself establish that a root exists.

## A finite-change bound

If |f'(t)|≤M throughout the open interval between a and b, MVT gives

|f(b)-f(a)| = |f'(c)| |b-a| ≤ M|b-a|.

For example, if |f'(x)|≤1 on [0,0.1], then the endpoint values can differ by no more than 0.1. For f(x)=exp(-x) on that interval, the actual change is 1-exp(-0.1)≈0.0952, within the bound. A loose bound is still valid; it is not an estimate of the actual change or an uncertainty interval unless the model and derivative bound are justified.

## Common mistakes

- Checking differentiability at the endpoints instead of continuity on the closed interval and differentiability only in the interior.
- Applying the theorem across a jump or a corner.
- Treating an existence guarantee for c as a uniqueness guarantee.
- Claiming a root exists from monotonicity alone; use a sign change or another existence argument.
- Using a derivative bound beyond the interval where it was established.

## Limits of this lesson

The results concern real-valued, one-variable functions on stated intervals. They do not supply a derivative bound, identify a physical model, or justify extrapolation outside the interval. The unit adds the theorem and its immediate consequences; it does not cover the later antiderivative and differential-equation sequence in MIT 18.01SC.
