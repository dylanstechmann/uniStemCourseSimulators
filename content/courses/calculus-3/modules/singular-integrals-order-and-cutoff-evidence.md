# Singular integrals, order and cutoff evidence

The regular-coordinate reading states conditions for exchanging integration order. This original counterexample shows why those conditions matter: two iterated integrals exist and disagree when absolute integrability fails. It then compares different simultaneous cutoffs. The example is a signed mathematical function, not a nonnegative physical density or a model of oxygen demand. It is a bounded extension of the calculus discussion, not a general measure-theory treatment.

## Specify the singular function and domain

Use f(x, y)=(x²−y²)/(x²+y²)² on the open unit square 0<x, y<one. The singularity lies at the corner approached by the integration limits. Assigning any finite value at that one corner cannot control the behavior throughout nearby regions.

For each fixed positive x, an antiderivative in y is y/(x²+y²). Therefore integrating y from zero to one gives one/(one+x²). The remaining x integral is pi/four. Each one-dimensional section in this order is well-defined under its stated positive outer coordinate and limiting convention.

For each fixed positive y, the x antiderivative is -x/(x²+y²). Its section integral is -one/(one+y²), so the opposite iterated order gives -pi/four. A symbolic system may return either value if it is asked to execute one order without checking the hypotheses for identifying both as the same double integral.

## Absolute integrability supplies the missing test

In polar coordinates inside a quarter disk, f=cos(2theta)/r² and dA=r dr dtheta. The absolute angular integral from zero to pi/two is one. Thus on a quarter annulus epsilon<=r<=one,

$$\iint |f|\, dA=\int_\epsilon^1\frac{dr}{r}=\ln(1/\epsilon).$$

For epsilon=0.01 it is ln100, about4.6051702. It grows without bound as epsilon tends to zero. The quarter annulus lies inside the unit square, so this proves the square's absolute integral diverges. The function does not satisfy the absolute-integrability condition that would justify the unqualified order exchange.

Positive and negative sectors both contribute unbounded magnitudes near the corner. Signed cancellation under one exclusion rule does not turn those into an ordinary order-independent finite integral. Fubini's theorem is not contradicted by an example outside its required conditions.

## Calculate a simultaneous rectangular cutoff

For a positive rectangle [epsilon_x, one]times[epsilon_y, one], the function is continuous and ordinary order exchange is valid. Direct integration gives

$$I=\pi/4-\arctan\epsilon_x-\arctan(1/\epsilon_y)+\arctan(\epsilon_x/\epsilon_y).$$

Now shrink with epsilon_x=c epsilon_y and fixed c>zero. The limit is arctan(c)−pi/four. For c=two it is arctan(one/three), about 0.32175055; for c=one half it is the negative of that value. Equal cutoffs give zero by symmetry.

These are different regularization paths for the same singular expression. The finite rectangles all permit Fubini, their integrals can be computed accurately, and their limiting values still depend on how the corner is excluded. Passing a quadrature refinement check on one rectangle does not establish a unique excluded-corner limit.

## Balanced cancellation is a declared operation

A symmetric radial exclusion also gives zero for the signed square integral by exchanging x and y. That value can be studied as a chosen balanced cutoff. It does not replace the two different iterated limits or establish absolute integrability.

The issue is not that every singular integral must fail. For a proper continuous function on a compact rectangle, the ordinary theorem applies; many improper functions also have finite absolute integrals. One must check the actual function and domain rather than either exchanging all orders automatically or rejecting every singular case by name.

Likewise, changing the integrand to include a fixed positive regularization parameter defines a different family of functions. It can make each finite problem integrable, but a later parameter limit still needs its own justification. A small denominator cutoff hidden inside code can silently choose one such altered problem.

## Independent numerical and conceptual checks

Derive both antiderivatives, verify their derivatives and evaluate finite-cutoff rectangles in both orders. Compare at least two cutoff ratios while separating numerical error from the changing domain. Plot or describe the opposite-sign sectors and the logarithmic absolute growth. A plotted grid can miss the corner while its nearby contribution remains important.

Retain the domain, order, antiderivative, absolute bound, cutoff ratio and conclusion about theorem applicability. A correct selected decimal is not a proof of integrability. [MIT OCW 18.02SC Fall 2010 Unit 3 Part A](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/3.-double-integrals-and-line-integrals-in-the-plane/part-a-double-integrals/) supplies link-only order-exchange/integration scope; this original signed counterexample makes the existing qualification concrete. No source proof, problem, figure, code or data is imported. All instruction is AI-assisted and remains partial and unreviewed; general integration theory, measured workload and qualified review remain open.
