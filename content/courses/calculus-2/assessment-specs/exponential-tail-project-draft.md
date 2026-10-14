# Exponential tail and Taylor error certificate: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded, and it is not a protected assessment. The normalized response below is a mathematical construct, not a measured rate or a model of a real process.

## Purpose and outcomes

Build a certificate for a finite approximation to an infinite accumulation. The sequence connects convergence of an improper integral, a tail tolerance, Taylor approximation, integration of a remainder bound and the distinction between approximation error and model error.

## Model and work sequence

Let `x ≥ 0` be a dimensionless normalized coordinate and let `q(x)=e^(−x)`. Its values and accumulated amount are dimensionless. Use the given function as an exact teaching model; do not assign a biological, mechanical or experimental interpretation.

1. Evaluate `Q=∫₀∞ q(x) dx` from the limit definition of the improper integral and explain why the limit is finite.
2. Find the omitted tail after a cutoff `T`. Calculate it at `T=3`, then find the smallest cutoff for which the tail is at most `0.01`.
3. On `[0,1]`, use the degree-four Maclaurin polynomial `P₄(x)=1−x+x²/2−x³/6+x⁴/24`. Integrate it exactly.
4. Use the Lagrange remainder for `e^(−x)` to bound the absolute error in `∫₀¹P₄(x)dx`. Compare the bound with the actual error obtained from the exact integral.
5. Combine the degree-four approximation over `[0,1]` with the exact tail over `[1,∞)`. Report the resulting approximation to `Q`, its signed error and the separate sources of error.
6. Explain why a small Taylor remainder certifies approximation to the stipulated function but does not validate that function as a model for any external system.

## Author calculation key

The improper integral is

\[
Q=\lim_{b\to\infty}\int_0^b e^{-x}dx=\lim_{b\to\infty}(1-e^{-b})=1.
\]

The tail after `T` is `e^(−T)`. At `T=3` it is approximately `0.0497871`. Solving `e^(−T)≤0.01` gives `T≥ln(100)≈4.6051702`.

The integrated Taylor polynomial is

\[
\int_0^1P_4(x)dx=1-\frac12+\frac16-\frac1{24}+\frac1{120}=\frac{19}{30}=0.6333333.
\]

On `[0,1]`, the fifth derivative has magnitude `e^(−ξ)≤1`, so `|R₅(x)|≤x⁵/120`; therefore the absolute integrated error is at most `∫₀¹x⁵/120 dx=1/720≈0.0013889`. The actual error of the polynomial integral is `19/30−(1−e^(−1))=e^(−1)−11/30≈0.0012128`, which is within the bound. Adding the exact tail `e^(−1)` gives an approximation `19/30+e^(−1)≈1.0012128` to `Q=1`, with the same positive local approximation error.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Improper integral | Uses the limiting definition and states the convergence result |
| Tail requirement | Derives `e^(−T)` and solves the tolerance inequality with the correct direction |
| Taylor approximation | Integrates all five polynomial terms correctly |
| Error certificate | Uses an interval-valid derivative bound and integrates it |
| Interpretation | Separates approximation to the stipulated formula from validation of an external model |

The rubric has no point weights or automatic prose grader. Workload, accessibility, mathematical accuracy and instructional design need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and exact mathematical values, CC BY 4.0, developed with substantial AI assistance. No dataset, third-party text or real-world procedure is included.
