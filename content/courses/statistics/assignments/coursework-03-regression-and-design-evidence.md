# Assignment 3: regression and design evidence

This open report connects a multiple-regression calculation with the design and assumptions needed to interpret it. It uses six constructed rows with normalized predictors, not a real biological experiment. Keep matrices, plots, code and report locally. Browser checkpoints evaluate selected coefficients and standard errors; they do not grade model diagnosis, causal reasoning or implementation quality.

## Part A: fit a distinct two-predictor model

Fit y=a+b x+c z by ordinary least squares to these supplied rows:

| Row | x | z | y |
| --- | ---: | ---: | ---: |
| 1 | -1 | -1 | 1.5 |
| 2 | -1 | 1 | -3.5 |
| 3 | 0 | -1 | 4 |
| 4 | 0 | 1 | 2 |
| 5 | 1 | -1 | 9.5 |
| 6 | 1 | 1 | 4.5 |

Build the design matrix with its intercept column. Verify its rank and solve the original normal equations or use a documented QR factorization. The solution is a=3,b=4,c=-2. The residuals are (0.5,-0.5,-1,1,0.5,-0.5), with SSE three. Check their sum and their inner products with both predictor columns; all must vanish to numerical tolerance.

Do not infer that orthogonal residuals are independent random errors. Orthogonality is an algebraic property of the least-squares projection. The table was constructed, and the stochastic assumptions for inference would need separate justification in an empirical analysis.

## Part B: uncertainty for two different targets

There are six rows and three independent fitted coefficients, leaving three residual degrees of freedom. Hence MSE=3/3=one. At x=0,z=0 the fitted mean is three, and leverage for the row (1,0,0) is one sixth.

Under a correctly specified fixed-design homoskedastic independent-error model, the estimated standard error for that mean response is sqrt(1/6), about 0.40824829. For a single new independent observation with the same error variance it is sqrt(7/6), about 1.0801234. Derive both from the coefficient covariance and a separate new-error term.

State what extra assumptions would support a small-sample t interval and name its degrees of freedom. Do not use a supplied standard error as a complete interval without selecting the target, confidence level and appropriate critical value. Neither standard error includes unmodeled systematic error or uncertainty about which mean model is correct.

## Part C: reduced models, rank and influence

Compare the full fit with an intercept-and-x-only fit. Here the balanced x and z columns are orthogonal, so omission has a different slope consequence from the foundation's correlated-predictor rehearsal. Calculate the reduced residuals and SSE rather than assuming the same omitted-variable shift applies in every design.

Construct a separate rank-deficient variant with z=x. Show why individual b and c are not identified from that matrix. Give two distinct coefficient pairs with the same fitted values and explain why more decimal places in an optimizer cannot resolve the deficiency. Changing the predictor design could supply information, but choosing such a design for a real experiment needs context outside this synthetic exercise.

Plot fitted responses and residuals against each predictor. Label the normalized scales and supply a text description of any pattern. Refit after excluding one row and document how coefficients and residual degrees of freedom change. The comparison illustrates sensitivity, not a general rule to discard an inconvenient point after seeing its outcome.

## Part D: association and a defensible claim

Write two different interpretation paragraphs. The first assumes the supplied rows are merely observational: describe conditional fitted associations and the unverified assumptions. The second describes what additional random assignment, adherence, missing-data and interference information would be needed before a treatment-effect interpretation could be defended. Do not invent that information or claim it is present in the table.

Adjustment for the observed z does not establish that all confounding is removed. A selected predictor set, high R² or a significant coefficient cannot supply the missing design. Compare this limitation with the existing study-design and nested-replication lab; several measurements from one unit do not become independent rows by entering a regression matrix.

Retain raw rows, rank check, coefficient solution, residual ledger, variance/standard-error derivation, reduced and deficient comparisons, and the interpretation paragraphs. [MIT OCW 18.05 Spring 2022 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) class 26 is link-only regression scope. The original AI-assisted table and tasks import no external problem, code or dataset. General model selection, real causal identification, measured workload and qualified review remain open; this package stays partial and unreviewed.
