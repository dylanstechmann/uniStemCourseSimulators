# Assignment 3: convergence and integer certificates

This open mixed report joins positive-series comparisons, improper integrals, alternating remainders and power-series endpoint tests. It asks for a classification, a justified bound and an integer choice as separate results. All examples and targets are synthetic mathematical tasks. Retain proofs, calculations and code locally. Browser responses check selected quantities and interpretations; they do not evaluate a full convergence argument.

## Part A: slow positive tails

Analyze $\sum_{n=2}^{\infty}1/[n(\ln n)^p]$ using a comparison integral and the substitution $u=\ln x$. Verify positivity and eventual monotonicity before applying the integral test. For p=1 and p=2 the summand's continuous version is decreasing on the stated interval from two onward.

The transformed integral is a power integral in u, giving convergence for p>1 and divergence for p≤1 under the appropriate eventual test hypotheses. Explain why changing a finite initial set of terms does not change that classification. In particular, the p=1 series diverges even though its terms decrease to zero and finite partial sums grow very slowly.

For p=2, bound the remainder after terms through index N by $\int_N^{\infty}dx/[x(\ln x)^2]=1/\ln N$. At N=100 this certificate is about 0.217147. It is a conservative upper bound, not the exact omitted sum. Solve for the smallest integer N making that certificate at most 0.1. Since $\ln N\geq10$, the answer is 22027.

Check N=22026 and N=22027 with sufficient precision. An approximate exponential rounded too early can select the wrong side of an integer boundary. State whether your code reports the last included index or the number of terms: a sum starting at two has N−1 included terms through index N.

## Part B: a different alternating certificate

Use the alternating harmonic series $\sum_{n=1}^{\infty}(-1)^{n+1}/n$. Verify that magnitudes decrease to zero and compare even and odd partial sums. Its ordinary sum is $\ln2$, while its absolute-value series diverges, so it is conditionally convergent.

If the first N terms are retained, the next omitted magnitude is $1/(N+1)$. The smallest positive integer N making this certificate at most 0.001 is 999. Check the previous integer as well. Do not replace N+1 by N or confuse the first omitted term with the last included term.

Compare the theorem-based bound with the actual difference from $\ln2$ for selected partial sums. The actual error may be smaller than the bound. Failure of a sufficient certificate to meet a requested target does not prove the approximation itself fails that target. Preserve approximation, certificate and reference error in separate columns.

## Part C: radius and endpoint behavior

For $\sum_{n=1}^{\infty}(x-1)^n/(n2^n)$, find the radius centered at one, then test the two boundary points separately. The interior ratio condition is $|x-1|<2$. At x=-1 the terms form an alternating harmonic series and converge conditionally; at x=3 they form a positive harmonic series and diverge. Thus the full real convergence interval is [-1,3).

Differentiate or integrate only on an interval where the operation is justified, and state what extra argument would be needed at an endpoint. A finite polynomial formed by truncation is defined at points outside the convergence interval, but that does not establish convergence of the infinite series there. Connect this distinction with the new uniform-bound and Taylor-representation counterexamples.

## Part D: numerical evidence without a false verdict

Implement partial sums using a documented summation order and compare several truncations. Show why finite computed values cannot alone decide an infinite convergence question. The p=1 positive series and the conditionally convergent alternating series can both have modest-looking partial sums for the first few observations, despite different behavior.

For the slow positive tail, compare the integral upper bound with a long finite tail segment and explain why the finite segment is only a lower estimate of the full positive remainder. For the alternating series, compare parity-based brackets. Distinguish floating-point summation error from the analytic omitted tail; adding more terms can eventually worsen numerical cancellation even while mathematical truncation improves.

Include a deliberately invalid test application and identify its missing hypothesis. Examples include calling a series convergent because terms tend to zero, applying a positive comparison argument to signed terms without separating absolute values, or reading endpoint inclusion directly from a ratio inequality. Use the original series to reject the shortcut.

## Self-review and scope

The retained report should contain integral-test hypotheses, p-classification, two minimal-integer certificates, actual-error comparisons and a separate radius/endpoint argument. [MIT OCW 18.01SC Fall 2010 Unit 5](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-5-exploring-the-infinite/) is a link-only scope comparator for infinite processes and series. All tasks and explanations are original and AI-assisted; no source problem or proof is imported. A general theory of rearrangements, function spaces or real analysis is outside this selected report. The course remains partial and unreviewed, with workload and qualified review open.
