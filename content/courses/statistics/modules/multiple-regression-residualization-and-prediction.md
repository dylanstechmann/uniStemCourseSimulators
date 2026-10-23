# Multiple regression, residualization and prediction

A simple regression line describes one response against one predictor. If another predictor is associated with both, a simple slope may combine their contributions. Multiple regression fits a specified mean surface and makes that conditional comparison explicit. It still does not create random assignment, repair omitted variables or prove a causal mechanism. This original foundation develops the algebra, residual checks and prediction uncertainty for two predictors.

## Fit the specified model rather than three separate lines

Stipulate mean response a+b x+c z with an intercept and known predictor values. Write the six-row design matrix with columns 1,x,z and solve X'X beta=X'y. A unique coefficient vector needs independent design columns. If z=x exactly, the data identify b+c rather than the individual slopes; an optimizer choosing one coefficient pair does not supply missing information.

For a worked balanced design let x=(-1,-1,0,0,1,1), z=(-1,1,-1,1,-1,1) and response y=5+2x+3z+e, where e=(1,-1,-2,2,1,-1). The residual vector is orthogonal to each design column. Thus fitted coefficients are exactly (5,2,3), X'X has diagonal (6,4,6), and the residual sum of squares is twelve. With six rows and three independent fitted coefficients, residual degrees of freedom are three and MSE is four.

These residuals are constructed algebraic teaching inputs. Calling their squared average a residual variance estimate does not make them sampled independent normal errors or measured biological replicates.

## A distinct rehearsal with correlated predictors

Use the following synthetic normalized rows:

| Row | x | z | y |
| --- | ---: | ---: | ---: |
| 1 | 0 | 0 | 2 |
| 2 | 0 | 1 | 3 |
| 3 | 1 | 1 | 4 |
| 4 | 1 | 2 | 11 |
| 5 | 2 | 2 | 12 |
| 6 | 2 | 3 | 13 |

The multiple fit is a=1,b=2,c=3 with the same residual vector and SSE twelve. In contrast, the simple y-on-x slope is five. In this table Cov(x,z)/Var(x)=one using consistent sums, so the omitted z contribution to the simple slope is c times one, or three. This is a decomposition of the specified linear projection, not proof that either predictor is a cause.

Residualization gives another route: remove the linear projection on intercept and z from both x and y, then regress the residualized response on residualized x. That slope agrees with the full model's b when the residualized predictor has nonzero squared length. This equivalence identifies what “holding z fixed” means algebraically and makes collinearity visible.

## Residual variance and coefficient uncertainty

Under a correctly specified fixed-design mean model with independent equal-variance errors, covariance of the coefficient estimate is sigma²(X'X)^−1. Replacing sigma² with MSE yields the familiar estimated covariance. Exact small-sample t intervals additionally need the relevant normal-error assumptions. Independence and equal variance are assumptions to assess, not consequences of the normal equations.

For the rehearsal, inverse X'X is

$$\begin{pmatrix}7/12&1/12&-1/3\\1/12&11/12&-2/3\\-1/3&-2/3&2/3\end{pmatrix}.$$

The predictor correlation inflates the uncertainty of separated slopes relative to an equally informative orthogonal design. Coefficient signs or individual p-values can therefore change with the predictor set without identifying a biological interaction or removing confounding.

## Mean response versus a new noisy observation

At x=1,z=1.5, the fitted rehearsal response is 7.5. For row vector h=(1,1,1.5), leverage h(X'X)^−1h' is 1/6. The estimated standard error for the mean response is sqrt(4/6), about 0.81649658. For one independent new observation with the same error variance it is sqrt[4(1+1/6)], about 2.1602469. The extra one represents new observation noise, not another fitted coefficient.

These are standard errors, not complete intervals until a confidence level, critical value and target are specified. Extrapolation, predictor measurement error, changed populations or unequal variance can invalidate their intended interpretation. High R² does not certify the mean model or the new observation process.

## Retain a reproducible diagnosis

Check the rank, original row values, fitted values, residual orthogonality and residual degrees of freedom. Plot residuals against both predictors and fitted values with units and a plain-text description. Compare the multiple and reduced model, and demonstrate a deliberately collinear design. A conditional association needs design evidence before causal wording; adjustment for available covariates does not prove all confounding is removed.

[MIT OCW 18.05 Spring 2022 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) class 26 supplies link-only linear/multiple-regression scope. All rows, derivations and tasks are original and AI-assisted; no source table, code or exercise is imported. Generalized linear models, broad model selection and qualified statistical review remain open; the package remains partial and unreviewed.
