# Assignment 3: constrained optimization and root certificates

Build a report connecting feasible sets, derivative signs, existence theorems and numerical root evidence. Read the [shape/optimization lesson](../modules/09-shape-analysis-and-constrained-optimization.md) and [Mean Value Theorem lesson](../modules/14-rolle-mean-value-theorem-and-consequences.md). These are exact mathematical problems, not validated designs. Save your derivations, sign tables and numerical evidence locally. Browser practice checks selected outputs and choices; it cannot assess a proof or an engineering recommendation.

## 1. Derive the objective from geometry

A constructed rectangular sheet has side lengths 14 and 10 centimeters. Remove equal corner squares of side x and fold the remaining flaps to form an ideal open box, ignoring thickness and fold radius. Derive V(x)=x(14−2x)(10−2x). State the interval giving nonnegative geometric dimensions and distinguish its endpoints from the strictly positive-volume designs. Explain why treating x as unrestricted would change the mathematical problem.

Differentiate V, solve for both stationary roots and classify them relative to the feasible interval. Create a derivative-sign table. Compare the feasible stationary value with the endpoints to justify a global maximum. A second-derivative test alone is a local argument; explain what additional domain and endpoint reasoning closes the global claim. Use exact radicals in the derivation and keep intermediate precision when producing numerical values.

Now impose a height limit x≤1.5 centimeters while retaining the same objective. Determine the new optimum by feasible derivative signs and boundary comparison. Explain why the old unconstrained stationary point is no longer an admissible answer. Compare the two maximum volumes and explain the direction of change using set inclusion: restricting the same feasible set cannot improve its maximum. Identify physical effects omitted by ideal folding, without inventing a real device specification.

## 2. An existence point need not be unique

For g(t)=t³−3t on [−2,2], verify the hypotheses of the Mean Value Theorem. Calculate its secant slope and solve g′(c) equal to that slope for every c in the open interval. Explain why two valid values do not contradict the theorem. Draw or describe the derivative sign intervals and identify the zeroes of g itself. The function changes sign between its endpoints but has more than one root; explain why an intermediate-value existence argument cannot establish uniqueness.

Give counterexamples showing why dropping continuity on the closed interval or differentiability on the open interval invalidates the standard theorem. Distinguish a theorem's sufficient hypotheses from necessary conditions for its conclusion in one special case. For example, an identity could happen to have matching slopes even when a particular standard proof is unavailable; that does not license applying the theorem without checking its assumptions.

## 3. Certify a numerical root with a derivative bound

Let h(t)=t+exp(t)−2 on [0,1]. Establish existence by endpoint signs and continuity. Prove uniqueness using h′(t)=1+exp(t)>0. On this interval h′≥2, so a Mean Value Theorem argument bounds the error of any candidate t in the interval by |h(t)|/2 relative to the unique root. Derive that inequality explicitly; distinguish a residual from a location error and state why the derivative lower bound makes the conversion possible.

Take one Newton step from t0=0.5, keeping full precision. Report the new iterate, its residual and the certified location-error bound. Retain a bisection bracket as a separate check. Repeat Newton from an alternative point and compare the actual error reduction using a more accurate reference root, but do not treat observed convergence as a universal theorem. A zero derivative, an out-of-domain step or a non-smooth function can invalidate the usual update.

Find a derivative-based bound converting an output tolerance into an input uncertainty for the local inverse, and explain its connection to sensitivity. Compare it with a case where the derivative approaches zero, such as a quadratic near its minimum. The same residual can then allow a much larger location uncertainty. A small calculator residual is not enough without the relevant hypotheses and scale.

## Self-review and completion evidence

The feasible volume interval is [0,5]. Stationary roots are (12−sqrt(39))/3 and (12+sqrt(39))/3; only the first lies in the interior. The constrained height-limit optimum is x=1.5 with volume 115.5 cubic centimeters. Compare this with your independently computed unrestricted feasible maximum. For g, the secant slope is one and both c=−2/sqrt(3) and c=2/sqrt(3) satisfy the theorem; g has roots −sqrt(3), zero and sqrt(3).

For h, the specified Newton iterate is 0.5−[0.5+exp(0.5)−2]/[1+exp(0.5)]. Compute it and its residual rather than copying a rounded root from feedback. Your report must include the feasible sign table, all candidate comparisons, theorem-hypothesis checks, existence/uniqueness distinction, derived residual certificate and independent bracket. State which conclusions concern exact mathematics and which depend on a stipulated geometry model.

The assignment is original and developed with substantial AI assistance. MIT OCW [18.01SC Fall 2010 Unit 2](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-2-applications-of-differentiation/) supplies a link-only scope comparator; no course problem, solution or diagram was imported. This is open practice with no institutional credit. Qualified review and measured workload remain open, and the course remains partial and unreviewed.
