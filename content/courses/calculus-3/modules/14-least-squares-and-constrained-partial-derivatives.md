# Least-squares fitting and partial derivatives with non-independent variables

The [Hessian lesson](09-hessians-constraints-and-boundary-optima.md) solved stationary equations together and classified the result with the second-derivative test. This lesson applies both steps to one of the most common optimization problems in science: choosing the line that best fits measured points. The unknowns are the line's slope and intercept, and the function being minimized is the total squared error. The second half returns to constraints from another direction. When variables are tied by an equation, "the partial derivative of w with respect to x" is ambiguous until it says which other variable is held fixed. Differentials resolve the ambiguity. All data and relations are synthetic mathematical constructions.

The undergraduate [MIT OCW 18.02SC Multivariable Calculus (Fall 2010) Unit 2](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/2.-partial-derivatives/) places least squares (Session 29) between optimization problems and the second-derivative test, and closes the unit with constrained differentials and the notation for held variables (Sessions 42–43). This lesson follows that pairing within the local optimization weeks. It uses 18.02SC as a scope comparator only and reproduces no MIT material.

## Learning objectives

By the end of this lesson, you should be able to:

1. Set up the squared-error function for a straight-line fit, derive and solve its normal equations, and confirm the minimum with the second-derivative test.
2. Fit an exponential model by taking logarithms, and explain why the result differs from a direct least-squares fit of the original data.
3. Compute partial derivatives of a function whose variables satisfy a constraint, state which variable is held fixed, and check the result with differentials or the triple-product rule.

## The squared-error function

Suppose measurements (x₁, y₁), …, (xₙ, yₙ) should lie near a line y = ax + b. For a candidate slope a and intercept b, the **residual** at point i is yᵢ − (axᵢ + b), the vertical gap between the measurement and the line. Least squares chooses a and b to minimize

**D(a, b) = Σ [yᵢ − (axᵢ + b)]².**

Here the data are fixed numbers and a and b are the variables. Squaring makes every gap count positively, penalizes large misses more than small ones, and gives a smooth function whose minimum can be found with calculus.

## The normal equations

Setting both partial derivatives to zero gives

∂D/∂a = −2 Σ xᵢ[yᵢ − (axᵢ + b)] = 0, ∂D/∂b = −2 Σ [yᵢ − (axᵢ + b)] = 0.

Expanding gives two linear equations, the **normal equations**:

**a Σxᵢ² + b Σxᵢ = Σxᵢyᵢ, a Σxᵢ + b n = Σyᵢ.**

**Synthetic example.** For the four points (1, 2), (2, 3), (3, 5) and (4, 6), the sums are n = 4, Σx = 10, Σx² = 30, Σy = 16 and Σxy = 47. The equations 30a + 10b = 47 and 10a + 4b = 16 give **a = 1.4** and **b = 0.5**. The fitted values are 1.9, 3.3, 4.7 and 6.1, the residuals are 0.1, −0.3, 0.3 and −0.1, and the minimum squared error is **D = 0.20**.

The second normal equation says the residuals sum to zero. This holds for any least-squares line that includes an intercept, and it gives a quick check on arithmetic. The first says the residuals are uncorrelated with x, in the sense that Σxᵢ × residualᵢ = 0. In the example, 0.1 − 0.6 + 0.9 − 0.4 = 0.

## Is it really a minimum?

The second partial derivatives of D are constants: D_aa = 2Σx², D_ab = 2Σx and D_bb = 2n. For the example, the Hessian is [[60, 20], [20, 8]]. Its determinant is 480 − 400 = **80** > 0 and D_aa > 0, so the stationary point is a local minimum. Because D is a quadratic with this Hessian everywhere, the minimum is also global.

In general, the determinant is 4[nΣx² − (Σx)²]. That quantity is positive whenever at least two x values differ, by the Cauchy–Schwarz inequality. If every xᵢ were the same, the determinant would be zero and no unique line would exist: infinitely many lines pass through the mean of a vertical stack of points with the same squared error.

## Fitting an exponential by taking logarithms

Many processes suggest y = c e^{kx}, such as decay toward zero or early growth. Taking logarithms gives ln y = ln c + kx, which is linear in the unknowns ln c and k. A least-squares line through the points (xᵢ, ln yᵢ) therefore gives k as the slope and ln c as the intercept.

**Synthetic example.** For (0, 5), (1, 3) and (2, 2), the logarithms are 1.609, 1.099 and 0.693. The fitted slope is k = **−0.458**, and the intercept gives c = e^{1.592} = **4.91**.

This is not the same as minimizing Σ[yᵢ − c e^{kxᵢ}]². The log fit minimizes squared errors in ln y, which weights a fixed relative error equally at every point. A direct fit of the original values, solved numerically, gives c ≈ 4.97 and k ≈ −0.474, with squared error 0.0152 in y against 0.0203 for the log fit. Neither is wrong. They answer different questions, and the choice should match how the measurement errors behave: roughly constant relative error favours the log fit, and roughly constant absolute error favours the direct fit. A power law y = c xᵖ is handled the same way with ln y against ln x.

## Partial derivatives when the variables are tied

Now take w = xyz, where the three variables must satisfy z = x + y. Only two of them can vary freely. "∂w/∂x" now has two different meanings:

- **Holding y fixed**, z changes with x. Substituting z gives w = xy(x + y) = x²y + xy², so (∂w/∂x)_y = 2xy + y².
- **Holding z fixed**, y = z − x changes instead. Then w = x(z − x)z = xz² − x²z, so (∂w/∂x)_z = z² − 2xz.

At the point (1, 2, 3), these are **8** and **3**. The subscript names the variable held fixed, and it is part of the meaning, not decoration. Without it, the question has no single answer.

**Differentials give both at once.** Write dw = yz dx + xz dy + xy dz = 6 dx + 3 dy + 2 dz at the point, and the constraint as dz = dx + dy. To hold y fixed, set dy = 0. Then dz = dx and dw = 8 dx. To hold z fixed, set dz = 0. Then dy = −dx and dw = 6 dx − 3 dx = 3 dx. This bookkeeping avoids solving the constraint explicitly, which matters when the constraint cannot be solved in closed form.

## The triple-product rule

For any smooth relation F(x, y, z) = 0 with nonzero partial derivatives,

**(∂x/∂y)_z (∂y/∂z)_x (∂z/∂x)_y = −1.**

The sign is not a typo: cancelling as if these were fractions would wrongly give +1. **Synthetic example.** Take the relation PV = 10T, with P = 2 and V = 5, so T = 1. Then (∂P/∂V)_T = −P/V = −0.4, (∂V/∂T)_P = 10/P = **5** and (∂T/∂P)_V = V/10 = 0.5. Their product is −1. Thermodynamics uses this notation heavily, because a state can be described by several pairs of variables and every derivative must say which pair.

## Common mistakes

- Minimizing the sum of residuals rather than of squared residuals; positive and negative gaps then cancel, and every line through the mean point scores zero.
- Treating the data as variables and the slope and intercept as constants when differentiating D.
- Reporting a log-transformed fit as if it minimized squared error in the original units.
- Taking logarithms of zero or negative values in an exponential fit.
- Writing ∂w/∂x for constrained variables without saying which variable is held fixed.
- Cancelling the triple product to +1.

## Worked example

**Problem.** Measurements (0, 1), (1, 3), (2, 4) and (3, 6) are synthetic. Find the least-squares line, confirm it is a minimum, and check the residuals.

**Step 1: sums.** n = 4, Σx = 6, Σx² = 14, Σy = 14 and Σxy = 29.

**Step 2: solve.** The normal equations 14a + 6b = 29 and 6a + 4b = 14 give a = 1.6 and b = 1.1.

**Step 3: classify.** The Hessian is [[28, 12], [12, 8]] with determinant 224 − 144 = 80 > 0 and D_aa > 0, so the point is the global minimum.

**Step 4: check.** The fitted values are 1.1, 2.7, 4.3 and 5.9, the residuals are −0.1, 0.3, −0.3 and 0.1, and they sum to zero. The minimum squared error is 0.20. A line 0.1 higher would raise it by 4 × 0.01 = 0.04, which agrees with D_bb/2 × 0.1² = 4 × 0.01.

## Limits of this lesson

All data, models and relations are synthetic. The lesson fits lines and log-linearized exponentials by ordinary least squares with vertical residuals. It does not develop weighted or total least squares, matrix formulations, uncertainty in the fitted parameters, outliers, model selection or statistical inference. Direct nonlinear fits are mentioned only for comparison. Practice checks selected numerical values and interpretations; it does not grade a derivation or a choice of model. Original explanation and examples were developed with substantial AI assistance. The course remains partial, unreviewed and formative-only.
