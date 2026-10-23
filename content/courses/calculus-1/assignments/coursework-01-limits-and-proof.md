# Assignment 1: limits, domains and proof hypotheses

Prepare a calculation-and-reasoning packet using the [limit-definition reading](../modules/07-limits-continuity-and-derivative-definition.md) and [derivative-rule reading](../modules/02-derivative-rules-and-chain-rule.md). Retain your arguments locally. Browser checkpoints evaluate selected values and choices; they do not evaluate proofs or written counterexamples. All functions are exact constructed teaching examples. Treat domains as part of each problem, and do not use a numerical graph as the sole proof of a limit.

## 1. A removable expression with a non-removable choice

Define f(x)=(x²−9)/(x−3) when x<3, and f(x)=A+B(x−3)+2(x−3)² when x≥3. State the original domain of each branch. Find A for continuity at three, then B for differentiability there. Calculate the one-sided first derivatives directly from difference quotients. Finally, determine whether the supplied quadratic coefficient allows a two-sided second derivative. Replace that coefficient by an unknown C and state the condition needed for the second derivative to exist.

Do not differentiate the simplified left branch at three before checking that the actual value assigned by the right branch agrees with its limit. Explain the logical difference between canceling x−3 for x≠3 and evaluating an original quotient with a zero denominator. Repeat the analysis if A is changed while the other constants are held fixed. Give a formula for the difference quotient showing exactly which term prevents differentiability.

## 2. Build an epsilon–delta argument

For g(x)=x² at a=2, prove that its limit is four using |x²−4|=|x−2||x+2|. First restrict |x−2|<1 so that |x+2|<5. Then choose a positive delta as a function of any positive epsilon. The order of these choices matters: a bound on the second factor supplies a valid neighborhood before an output tolerance determines its final radius.

For epsilon=0.05, report one valid delta using min(1,epsilon/5). Check the strict implication for all points in the punctured neighborhood, not just its endpoints. Explain why a larger delta might also work and why the task asks for a valid radius rather than the largest possible one. Contrast this proof with checking ten decimal inputs close to two. Identify what the finite check leaves unproved.

Compute the forward secant slope [g(2+h)−g(2)]/h symbolically for nonzero h. At h=0.02, calculate the slope and its signed error relative to g′(2). Find a step condition that keeps the absolute secant-slope error at most 0.001. Explain why this exact algebraic error relation does not automatically predict finite-precision rounding error in a program using very small h.

## 3. Separate continuity from differentiability

Analyze k(x)=|x−1| at one, using both one-sided quotients and continuity. Explain why a minimum can occur where the derivative does not exist. Construct another function with a zero derivative but no extremum at the evaluation point, and justify its behavior on both sides. A label such as “critical point” is a candidate description, not a complete classification.

For a more demanding counterexample, let h(x)=x sin(1/x) for x≠0 and h(0)=0. Prove continuity at zero using |h(x)|≤|x|. The derivative quotient at zero is sin(1/x). Evaluate it along x_n=1/(2πn+π/2) and y_n=1/(2πn+3π/2), for positive integers n. Explain why both input sequences approach zero but their quotient limits disagree. If you use a plot, vary the sampling density and describe why any finite plot can miss oscillation.

## 4. Audit claims rather than only answers

For each of the following claims, provide either a proof with hypotheses or a counterexample: a two-sided limit fixes the function value; continuity implies differentiability; differentiability implies continuity; a zero derivative at one point forces constancy on an interval; and equality of one-sided derivatives can be discussed independently of the assigned function value. Distinguish a statement about one point from a statement about every point of an interval. State whether endpoints need one-sided definitions.

## Self-review and retained evidence

For the piecewise function, continuity requires A=6 and differentiability then requires B=1. The left second derivative is zero while the supplied right second derivative is four, so the second derivative fails; with the unknown coefficient C it exists when C=0. For the quadratic epsilon proof, delta=min(1,epsilon/5) works and gives 0.01 at the supplied tolerance. The secant slope is 4+h, hence 4.02 at h=0.02, with signed error +0.02. The oscillatory quotient takes values +1 and −1 on the two sequences, so it has no limit despite continuity of h.

Your final packet should contain domain declarations, exact algebra, one complete quantified proof, one pair of one-sided arguments, one sequence counterexample and a claim audit. A page of numerical answers alone does not satisfy the assignment. Identify any actual feedback honestly; passing checkpoints is not a proof review. This original AI-assisted assignment uses the [MIT OCW 18.01SC Fall 2010 syllabus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/syllabus/) as a link-only scope comparator and imports no source problem. The course remains partial and unreviewed; workload is unmeasured.
