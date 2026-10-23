# Assignment 1: integration methods and improper-limit evidence

This open mixed report joins substitution, completing the square, integration by parts, partial fractions and improper-limit reasoning. It asks for justified method choices and independent checks, not a list of antiderivatives copied from software. All functions and targets are synthetic normalized mathematical examples. Retain the calculations, code and report locally; browser checkpoints assess selected values and interpretations only.

## Part A: choose transformations before integrating

Evaluate $I=\int_0^1x/(x^2+4x+5)\,dx$. Complete the square in the denominator and write the numerator as a multiple of its derivative plus a remainder. This gives an antiderivative $\tfrac12\ln(x^2+4x+5)-2\arctan(x+2)$. Differentiate it and simplify the original rational integrand before evaluating the bounds.

The definite value is $\tfrac12\ln2-2\arctan(1/7)\approx0.06277948$. Justify the arctangent-difference simplification on the actual positive arguments; inverse-trigonometric identities require attention to branches. The denominator stays positive on the integration interval, so there is no singularity or logarithmic-domain split there.

Next evaluate the distinct integral $J=\int_0^1x^2\ln(1+x)\,dx$. Use integration by parts to move the logarithmic derivative into a rational remainder, then perform the polynomial division. The result is $2\ln2/3-5/18\approx0.18432034$. Retain the endpoint product and the divided remainder so that a missing sign or boundary term can be located.

Explain why these two problems invite different first steps, even though both eventually contain rational terms. A symbolic system's output can be a check, but the report should identify the structure supporting the method and verify the original derivative/domain. Do not invoke L’Hôpital’s rule as a general integration technique; it addresses eligible limit quotients under its own hypotheses.

## Part B: couple partial fractions to a finite upper limit

Consider $A=\int_0^\infty1/[(x+1)(x+2)]\,dx$. Decompose the integrand, but keep one shared finite upper cutoff $T$ until the logarithmic difference has been evaluated. The original positive integrand is integrable, whereas the two separated positive logarithmic integrals would individually diverge. Writing their values as infinity minus infinity is not a valid evaluation.

For finite $T$, the accumulation is $\ln2-\ln[(T+2)/(T+1)]$. Taking its limit gives $A=\ln2$. The positive omitted tail is exactly $R(T)=\ln[(T+2)/(T+1)]$. Show it decreases with $T$ and tends to zero. This rational tail differs from the existing exponential-tail project and needs its own cutoff calculation.

Find the smallest nonnegative integer $T$ with $R(T)\leq0.01$. The real threshold is $1/(e^{0.01}-1)-1\approx98.5008333$, so the smallest integer is 99. Its actual tail is $\ln(101/100)\approx9.95033085\times10^{-3}$. Check both neighboring integers directly; a rounded real threshold alone can select the wrong integer near a boundary.

For much smaller targets, evaluating exp(delta) minus one can lose relative precision through cancellation. A stable expm1 evaluation can help preserve the cutoff calculation, but the neighboring-integer inequalities still need to be checked. Numerical stability and the analytic tail identity are separate evidence.

## Part C: ordinary improper integrals and cancellation

Analyze $\int_{-1}^1dx/x$ as an ordinary improper integral by splitting at its internal singularity. Each one-sided integral must converge separately. They do not, so the ordinary integral diverges despite the odd integrand and a symmetric-cutoff expression that cancels.

State that a symmetric principal-value limit is a different object with a different definition. No advanced principal-value theory is required here; the point is to preserve the ordinary integral's separate-limit convention. Contrast this invalid cancellation across an internal singularity with the valid shared-cutoff partial-fraction evaluation of the original positive integral on a nonsingular finite interval followed by one upper limit.

## Part D: numerical evidence and method failure

Implement numerical quadrature for I and J and compare with the derived exact values under refinement. For A, separate finite-interval quadrature error from the analytic infinite-tail remainder. A quadrature routine returning a number on a finite cutoff cannot establish the missing tail or the convergence classification by itself.

Retain one intentionally wrong antiderivative or an invalid singular-limit shortcut and show the original derivative/domain check that rejects it. State how rounding, truncation and a mathematical identity differ. A close decimal result at one point is weaker than a verified identity and a justified limiting argument.

## Self-review and scope

Your retained report should contain method choices, transformations, derivative/domain checks, two exact finite integrals, a coupled partial-fraction limit, a minimal-integer tail certificate and numerical refinement. Browser practice does not evaluate the proof or code. [MIT OCW 18.01SC Fall 2010 Unit 4 Part B](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-4-techniques-of-integration/part-b-partial-fractions-integration-by-parts-arc-length-and-surface-area/) and [Unit 5 Part A](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-5-exploring-the-infinite/part-a-lhospitals-rule-and-improper-integrals/) are link-only comparators. All problems and explanations are original and AI-assisted; no source assessment or teaching text is imported. The paired local split does not establish two-course equivalence. Qualified review and measured workload remain open.
