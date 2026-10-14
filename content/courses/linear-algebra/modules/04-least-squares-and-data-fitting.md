# Least squares and data fitting

An overdetermined system has more equations than unknowns, and measured data rarely satisfy every equation exactly. Least squares chooses the parameter vector whose predicted outputs are closest to the observations in squared Euclidean distance. The algebra gives a precise fitting rule; residual analysis and study design determine what the fitted model can reasonably tell us.

## Learning objectives

By the end of this lesson, you should be able to:

1. Derive normal equations for a full-rank linear model.
2. Interpret residuals and avoid overclaiming from fit quality.

## Set up the model and residual

Write the model as

\[
Ax\approx b,
\]

where each row of (A) contains the predictors for one observation, (x) contains the unknown coefficients, and (b) contains the observed outcomes. For a line (y=a+mx), the coefficient vector is (x=(a,m)^T), and a row for a measurement at predictor value (t_i) is ((1,t_i)). The fitted values are \(\hat b=Ax\). Define the residual vector as

\[
r=b-Ax.
\]

The sign convention is observed minus predicted. Least squares minimizes

\[
J(x)=\lVert Ax-b\rVert_2^2=(Ax-b)^T(Ax-b).
\]

Squaring makes positive and negative residuals contribute to the total discrepancy without canceling. It also gives larger residuals more influence because their contributions grow quadratically. That weighting can be useful for some error models, but it makes least squares sensitive to outliers.

## Derive the normal equations

Expand the objective:

\[
J(x)=x^TA^TAx-2x^TA^Tb+b^Tb.
\]

Its gradient with respect to (x) is \(2A^TAx-2A^Tb\). Setting the gradient to zero gives the normal equations

\[
A^TA\hat x=A^Tb.
\]

If the columns of (A) are linearly independent, (A) has full column rank and (A^TA) is invertible, so the minimizer is unique. If the columns are dependent, some coefficient combinations produce the same fitted values; least squares may still find a best prediction, but the coefficients are not uniquely identified without an added convention or constraint.

The geometric interpretation is projection. The fitted vector (A\hat x) lies in the column space of (A), and it is the closest vector in that space to (b). At the minimum, the residual is orthogonal to every column of (A):

\[
A^T r=0.
\]

This condition is equivalent to the normal equations. It says the remaining error cannot be reduced by moving the fitted vector in any direction allowed by the model's columns. It does not say the model is true or that the residuals are random.

## Worked example: fit three observations

Consider the synthetic observations \((t,y)=(0,1),(1,2),(2,2)\), and fit (y=a+mt). Then

\[
A=\begin{bmatrix}1&0\\1&1\\1&2\end{bmatrix}, \qquad
b=\begin{bmatrix}1\\2\\2\end{bmatrix}.
\]

The normal equations are

\[
\begin{bmatrix}3&3\\3&5\end{bmatrix}
\begin{bmatrix}a\\m\end{bmatrix}
=\begin{bmatrix}5\\6\end{bmatrix}.
\]

Subtracting the first scalar equation from the second gives \(2m=1\), so (m=1/2); substituting gives \(a=7/6\). The fitted line is \(\hat y=7/6+t/2\). Its residuals are

\[
r=\begin{bmatrix}-1/6\\1/3\\-1/6\end{bmatrix}.
\]

Their sum is zero and their predictor-weighted sum is also zero, so (A^Tr=0). The residual sum of squares is \(1/6\). The data are not exactly on a line, so the residuals show the remaining mismatch rather than disappearing into a perfect-fit claim. All values here are synthetic teaching data.

## Read the residuals, not just a score

Residuals help reveal which errors remain after fitting. Plot them against predictor values, fitted values, time, or other design variables. A curved pattern may suggest a missing nonlinear term; a trend over time may suggest drift; a widening spread may indicate changing variance; and a cluster or isolated large residual may reveal a subgroup, data issue, or influential observation. These patterns are diagnostic clues, not automatic instructions to add parameters. Use the design and subject context to decide what follow-up is justified.

A high \(R^2\) or small average error does not establish that the functional form is appropriate, that important predictors are included, or that the model predicts new observations well. A model can fit the observed range and extrapolate poorly. It can also be predictive without identifying a causal relationship. Residual checks, uncertainty estimates, validation on data not used to fit the model, and a clear account of the domain all matter.

## Rank, scaling, and numerical solution

For a line with an intercept, the columns of (A) are the constant vector and the predictor values. If all predictor values are identical, those columns are dependent and slope and intercept cannot both be uniquely determined from the data. If they vary only slightly, the design may be full rank but poorly conditioned: small measurement changes can produce large coefficient changes. Centering or rescaling predictors can improve numerical behavior and interpretation, but it does not add information to the observations.

Although the normal equations are useful for derivation, explicitly forming (A^TA) can amplify conditioning problems: in the 2-norm, its condition number is the square of that of a full-column-rank (A). Numerical software commonly uses QR factorization or singular value decomposition for a more stable solution. The following lesson develops the geometric projection and QR approach. A computed coefficient should be reported with units, data range, assumptions, and uncertainty appropriate to the application.

## Weighted least squares

If observation errors have different known variances, a justified weighted objective can give less influence to noisier measurements. For independent errors with known variance \(\sigma_i^2\), the conventional weight is proportional to \(1/\sigma_i^2\). Weights should come from a measurement model or a stated design rationale, not from a desire to make residuals look better. Weighting changes the objective and estimand; it does not remove bias, correct an omitted variable, or guarantee an adequate model.

## Common reasoning errors

- Applying ordinary least squares when the design matrix does not have full column rank and reporting a unique coefficient vector.
- Assuming the residuals must sum to zero even when the model has no intercept column.
- Treating residual orthogonality as evidence that the model assumptions are correct.
- Using (R^2) alone to dismiss systematic residual structure.
- Solving normal equations numerically without considering conditioning.
- Choosing weights after looking at the desired result or using weights as a substitute for a measurement model.
- Interpreting a fitted association as a causal effect or extrapolating beyond the observed predictor range without support.

## Further study

MIT OpenCourseWare 18.06SC, *Linear Algebra*, Massachusetts Institute of Technology, offers independent study materials for [Projection Matrices and Least Squares](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/projection-matrices-and-least-squares/) and [Orthogonal Vectors and Subspaces](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/orthogonal-vectors-and-subspaces/). These links are for further study; no source text or problem has been reused in this reading.

## Limits of this lesson

The worked data are synthetic and the least-squares derivation assumes a linear model in its coefficients. Real analyses also require a justified error model, appropriate sampling, uncertainty estimation, and validation in the intended use domain. A small residual cannot establish causality or validate those assumptions.
