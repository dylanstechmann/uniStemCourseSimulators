# Regression, uncertainty, and validation

Regression estimates a relationship between predictors and observations under a chosen model and loss function. For a simple line $\hat y_i=\hat\beta_0+\hat\beta_1x_i$, least squares chooses the coefficients to minimize the sum of squared residuals, where $r_i=y_i-\hat y_i$. A small training residual sum describes fit to those observations; it does not show how well the model will predict new samples or whether the fitted relationship is causal.

## Residual scatter and uncertainty

Residuals are observed differences between outcomes and fitted values. Their pattern can reveal curvature, changing variance, outliers, time dependence or unmodeled groups. A residual standard error summarizes their typical scale under the fitted model. With $n$ observations and $p$ estimated parameters, a common estimate is

$$
s=\sqrt{\frac{\sum_i r_i^2}{n-p}}.
$$

For residuals $0.1,-0.2,0.1,0,0$, the sum of squares is $0.06$. With $n=5$ and $p=2$, the residual standard error is $\sqrt{0.06/3}=0.1414$ in the outcome's units. This estimates scatter around the fitted model under its assumptions. It is not the standard error of every coefficient and is not, by itself, an uncertainty interval for one future observation.

Parameter uncertainty describes how uncertain the estimated coefficients are under a sampling model. Predictive uncertainty for a new outcome also includes residual variation, and often is wider than uncertainty about the fitted mean. Both depend on the design, noise assumptions and independence structure; a formula cannot repair a misspecified model or a biased sample.

## Validation must match the prediction target

Training error is optimistically tied to data used to fit the coefficients. A held-out set or cross-validation estimates performance on data excluded from fitting, provided every learned step is kept inside the training partition. Scaling, imputation, feature selection and threshold choice must be fit or selected using training data only, then applied unchanged to that fold's held-out data. Looking at held-out results to revise the pipeline makes that data part of selection.

Rows are not always independent units. If several measurements come from one donor and the target is prediction for a new donor, keep all rows from a donor together in one split. A random row split can place the same donor on both sides, allowing donor-specific information to inflate apparent validation performance. Grouping should follow the intended use: a future-time target needs temporal separation, while a new-site target needs site-aware evidence. None of these splits alone proves external validity.

Report the split unit, preprocessing fit, model choices, metric and its denominator, and the uncertainty from limited independent groups. Examine residual patterns as well as one summary score. A lower held-out error is evidence under that validation design, not proof of causal mechanism or future performance in every population. The week-13 lesson develops grouped validation and threshold reporting with a constructed classifier example; neither lesson evaluates a real model or dataset.
