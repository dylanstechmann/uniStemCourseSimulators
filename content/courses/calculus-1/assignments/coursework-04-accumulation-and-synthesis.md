# Assignment 4: accumulation, quadrature and cumulative reasoning

Produce a cumulative calculus packet that combines signed rates, states, total travel, integral hypotheses, finite sums and approximation certificates. Use the [piecewise-rate reading](../modules/piecewise-rates-and-integral-hypotheses.md), [accumulation reading](../modules/10-accumulation-ftc-and-substitution.md) and [numerical-calculus reading](../modules/11-numerical-derivatives-integrals-and-error.md). Retain derivations and any source code locally. Browser checkpoints assess selected quantities only; they do not assess the full packet, written proof or implementation.

## 1. One rate gives several different quantities

A stipulated velocity is v(t)=2t−3 meters per second on 0≤t≤4 seconds, with initial position x(0)=7 meters. Derive the position function, locate every velocity sign change and calculate net displacement, final position, minimum position and total distance. Draw a signed rate-area diagram and a position graph. Explain why the integral of speed differs from the absolute value of the integral of velocity. Identify when those two expressions would agree and justify the condition.

As a transfer problem, interpret the same algebra as an abstract net balance rather than a velocity. Explain what additional definitions are needed before negative rates and absolute throughput make sense for that balance. A net balance alone does not identify independent inflow and outflow histories; construct two different pairs of nonnegative inflow/outflow functions with the same net rate. State which quantities those alternatives leave unchanged and which they can change.

## 2. Derive a quadrature reference before coding

Partition [0,4] into n equal intervals. Derive the left- and right-endpoint sums for v directly using the finite sum of positive integers. Show that they bracket the signed integral because v is increasing. Calculate both at n=8 and their trapezoidal average. Determine the least positive integer n making the right-sum absolute error at most 0.05 meter under this exact model. State whether equality at the tolerance is permitted.

If using code, verify the sums at n=1,2,8 and that the error scales as your derived expression predicts. Check a reversed integration interval and an identically constant function. Compare midpoint and trapezoidal values for this affine model; explain why their exactness here does not establish universal exactness or measured-data accuracy. Repeat a numerical sum for |v| and explain why splitting at its sign change matters to the integrand's smoothness and exactness assumptions.

## 3. A jump tests the theorem's hypotheses

Define a separate rate q(t)=−2 for 0≤t<2 and q(t)=3 for 2≤t≤4. Write its accumulation A(t) from zero as two formulas. Verify continuity at two, compute the one-sided derivatives there and decide whether A′(2) exists. Change the single value q(2) to a different finite value and explain which integral and derivative conclusions change, if any. Do not apply the continuous-integrand fundamental theorem at a jump without checking the actual accumulation quotient.

Calculate net accumulation and absolute accumulation over [0,4]. Compare with the smooth velocity model and state whether matching endpoints would identify the underlying rate history. Explain the distinction between an integrable piecewise rate, a continuous accumulation function and a differentiable accumulation function. Supply a counterexample to any incorrect implication you reject.

## 4. Moving boundaries and a model comparison

For H(t)=integral from t to 2t of (s²−1) ds, derive H′ using both moving-boundary differentiation and an explicit antiderivative. Evaluate at t=1 and verify the sign of the lower-bound contribution. Explain why integrating with respect to a dummy variable s prevents confusing the bound t with the integration variable.

Compare the fundamental theorem used above with the derivative-bound root certificate from [Assignment 3](coursework-03-optimization-and-certificates.md). In each case, identify the domain, continuity/differentiability assumptions and the exact conclusion. Write one paragraph distinguishing exact quadrature error for a known function, floating-point error in an implementation, measurement uncertainty and mismatch between a real process and a mathematical model. No amount of numerical refinement by itself removes the last two.

## Self-review after attempting the packet

The smooth position is x(t)=7+t²−3t. Net displacement is four meters, final position eleven meters, and the minimum is 4.75 meters at t=1.5. Negative and positive travel contributions have magnitudes 2.25 and 6.25 meters, so total distance is 8.5 meters. The right sum is 4+16/n and the left sum 4−16/n; at n=8 they are six and two meters, with trapezoidal average four. The allowed right-sum tolerance requires n≥320.

For the jump model, A(t)=−2t until two and A(t)=3t−10 afterward. It is continuous with value −4 at two, but its one-sided derivatives −2 and +3 disagree. Net accumulation over four seconds is two and absolute accumulation ten in the corresponding units. Changing one finite point value does not change the integral or repair the derivative. The moving-boundary derivative is 7t²−1, giving six at t=1.

A complete packet contains sign-aware ledgers, finite-sum derivations, theorem-hypothesis arguments, numerical verification cases and explicit uncertainty categories tied to examples. This original AI-assisted coursework uses [MIT OCW 18.01SC Fall 2010 Unit 3](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/unit-3-the-definite-integral-and-its-applications/) as a link-only scope comparator and imports no source problem or dataset. Advanced integration, geometry and series remain in Calculus II within the shared comparator sequence. Neither the packet nor browser feedback establishes full-course equivalence, qualified review or measured workload; the course remains partial and unreviewed.
