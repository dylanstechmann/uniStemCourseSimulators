# Derivative rules and chain rule

A derivative can be read as a local slope with respect to a named input. Rules for sums, products, quotients and nested functions make the limit calculation practical, but they do not remove the need to track what each variable means. This lesson develops those rules and follows units through a model whose output depends on a changing concentration. Implicit differentiation and longer related-rate chains are developed later.

## Rules organize the limit calculation

For differentiable functions \(f\) and \(g\), the derivative of a sum is \((f+g)'=f'+g'\), and a constant factor stays outside: \((cf)'=cf'\). The product rule is different from multiplying derivatives:

\[
(fg)'=f'g+fg'.
\]

For example, if \(p(x)=x e^{-x}\), then \(p'(x)=e^{-x}-xe^{-x}=e^{-x}(1-x)\). Both factors vary, so each contributes one term. At \(x=1\), the derivative is zero; this local flatness does not say the function is zero there, since \(p(1)=e^{-1}\).

The quotient rule follows from the product rule applied to \(f(1/g)\):

\[
\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^2},\qquad g\ne0.
\]

For \(q(x)=(x^2+1)/(x+1)\),

\[
q'(x)=\frac{2x(x+1)-(x^2+1)}{(x+1)^2}
     =\frac{x^2+2x-1}{(x+1)^2}.
\]

At \(x=2\), this is \(7/9\). The original quotient is undefined at \(x=-1\); simplifying the derivative does not make that excluded input valid.

## Nested dependence needs the chain rule

If an output has the form \(F(g(x))\), first differentiate the outer function while keeping its input visible, then multiply by the derivative of the inner function:

\[
\frac{d}{dx}F(g(x))=F'(g(x))g'(x).
\]

For \(z(x)=(3x+1)^4\), the outer derivative is \(4(3x+1)^3\), and the inner derivative is 3. Thus \(z'(x)=12(3x+1)^3\); at \(x=1\), the value is 768. Omitting the inner factor would give a result three times too small. The chain rule applies repeatedly when a model nests several functions.

## Rates carry units

Suppose \(C(t)=5e^{-0.2t}\) millimolar, where time \(t\) is in hours. The exponent must be dimensionless, so 0.2 has units \(\mathrm{h}^{-1}\). Differentiation gives

\[
\frac{dC}{dt}=-0.2\,\mathrm{h}^{-1}C(t).
\]

At \(t=2\) hours, \(C(2)=5e^{-0.4}\approx3.3516\) mM and \(dC/dt\approx-0.6703\) mM/h. The negative sign describes a declining concentration; it does not mean the concentration itself is negative. A rate must state both the changing quantity and the unit of its input.

Now let a response be \(R(c)=100c/(2\,\mathrm{mM}+c)\), measured on a 0-to-100 percent scale, while \(c(t)=4e^{-(0.1\,\mathrm{h}^{-1})t}\) mM. The rate constant makes the exponent dimensionless. The quotient rule gives

\[
\frac{dR}{dc}=\frac{200\,\mathrm{mM}}{(2\,\mathrm{mM}+c)^2}.
\]

At \(t=0\), \(c=4\) mM and \(dc/dt=-0.4\) mM/h. Applying the chain rule yields \(dR/dt=(200/36\,\mathrm{mM}^{-1})(-0.4\,\mathrm{mM/h})\approx-2.22\) percentage points per hour. The millimolar units cancel. This calculation describes the stated model; it does not establish that a real response follows this saturation curve.

## A reliable workflow

Before differentiating, identify the input and output and write their units. Choose the rule that matches the expression, preserve parentheses around inner functions, and check denominators on the domain. After differentiating, inspect units: a derivative of position in meters with respect to time in seconds is in m/s, while a concentration response differentiated with respect to concentration is a response change per concentration unit. If the input itself changes with time, multiply by its time rate.

Common errors include differentiating a product as a product of derivatives, dropping the inner derivative, losing a negative sign in exponential decay, and reporting a rate without its denominator unit. These rules compute local rates for differentiable models. They do not by themselves justify extrapolation, identify a causal mechanism, or resolve a vertical tangent or discontinuity; those questions require domain and model checks.
