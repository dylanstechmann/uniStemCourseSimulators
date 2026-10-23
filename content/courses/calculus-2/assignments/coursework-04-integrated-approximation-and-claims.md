# Assignment 4: integrated approximation and representation claims

This open report connects power-series operations, alternating bounds, definite integrals and the new counterexamples about function limits. It asks for an approximation whose precision and certificate are useful for the actual comparison. All inputs and targets are synthetic normalized mathematics. Retain derivations, code and report locally. Browser checkpoints assess selected numbers and interpretations rather than a graded proof or numerical study.

## Part A: integrate a justified approximation

For $0\leq x\leq1/2$, use the alternating expansion $\arctan x=x-x^3/3+x^5/5-\cdots$. Justify the decreasing magnitudes and the entire integration interval's position inside the radius. Integrate the cubic truncation from zero to b=1/2:

$$A_{cubic}=b^2/2-b^4/12=23/192\approx0.119792.$$

The first omitted pointwise magnitude is $x^5/5$, so the integrated truncation certificate is $b^6/30=1/1920\approx5.2083333\times10^{-4}$. Derive the bound by integrating the variable remainder, rather than multiplying an endpoint estimate by the whole interval without identifying that more conservative choice.

An independent exact integral is $A=b\arctan b-\tfrac12\ln(1+b^2)\approx0.12025203$. The actual error of the unrounded cubic integral is approximately 4.60362177×10⁻⁴, below the certificate. These are three separate objects: the approximation, an a priori bound and an independently evaluated error.

Report the approximation field to **six significant figures**, giving 0.119792. Three significant figures would round both the approximation and exact integral to 0.120, concealing the difference this exercise is intended to study. Other continuous checkpoint fields request three significant figures. Keep the exact fraction 23/192 for the truncation derivation; the displayed six-figure value has its own rounding difference of one part in three million and needs a separate entry if used in a total error budget.

## Part B: select an order by the certificate

Retain arctangent terms indexed n=0 through N, so the polynomial has N+1 nonzero terms and degree 2N+1. Integrating the first omitted alternating magnitude gives

$$B_N=\frac{b^{2N+4}}{(2N+3)(2N+4)}.$$

For target $10^{-6}$ at b=1/2, N=4 gives about $1.84955\times10^{-6}$ and N=5 gives about $3.35358\times10^{-7}$. Hence six nonzero arctangent terms, through degree eleven, are the first sufficient choice under this certificate. State both the index and term-count convention to avoid an off-by-one claim.

Verify the neighboring candidates with full precision. The N=4 bound failing the target does not by itself prove its actual error fails; a reference calculation or a sharper argument is needed for that separate conclusion. If the final N=5 accumulated estimate is displayed to six significant figures, budget the display rounding as well as truncation before claiming a total tolerance. A certificate proved for an exact polynomial does not automatically cover every rounded implementation.

## Part C: test an interchange claim

Use the continuous triangular sequence from the new foundation. Derive its pointwise zero limit and its integral one. Explain why a numerical grid can miss its shrinking support and return an apparently small area. Then compare with $x^n$ on [0,1], whose integrals do converge to the integral of its pointwise limit despite a lack of uniform convergence on that whole interval.

State precisely which conclusion each example supports. Pointwise convergence alone is insufficient for a general integral interchange, while a failed sufficient uniform condition alone does not prove a particular interchange is wrong. A counterexample and a theorem hypothesis answer different questions.

## Part D: restrict an infinite Taylor claim

For the flat function $F(x)=e^{-1/x^2}$ away from zero with F(0)=0, explain why every derivative at the center vanishes while F(1/2) remains positive. Identify the step that would be missing in the claim “all derivatives exist, therefore the Taylor series represents the function.” Contrast that infinite claim with the valid finite-order remainder theorem and its interval-dependent derivative bound.

This counterexample does not invalidate the arctangent expansion used in Parts A/B. Its representation and alternating hypotheses are independently justified on the chosen interval. Keep a function's domain, a series' radius, endpoint behavior and a polynomial's everywhere-defined algebra separate in the report.

## Verification and scope

Implement the arctangent polynomial integral with exact rational coefficients where practical and compare it with independent quadrature. Refine numerical integration and vary polynomial order separately. Report truncation, display rounding and integration error distinctly; no one of these bounds controls a physical measurement or a misspecified model.

The retained report should contain the cubic estimate/certificate/reference, a minimal sufficient order, precision budget and explicit interchange/representation counterexamples. [MIT OCW 18.01SC Fall 2010 Taylor-series scope](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-5-exploring-the-infinite/part-b-taylor-series/) is a link-only comparator. All cases and explanations are original and AI-assisted. General analysis theory, qualified mathematical review and measured workload remain open; the local paired calculus split does not establish two MIT-course equivalence.
