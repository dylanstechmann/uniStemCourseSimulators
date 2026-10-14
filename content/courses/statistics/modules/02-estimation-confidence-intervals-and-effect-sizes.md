# Estimation, confidence intervals, and effect sizes

An estimate is a summary computed from observed data; it changes from sample to sample. A confidence interval combines a point estimate with a measure of sampling uncertainty under a stated procedure. An effect size describes the magnitude of a contrast or association. These ideas answer related but different questions: how large is the estimated difference, how precisely is it estimated, and what range of values does a procedure cover over repeated samples? Keep the estimand, units, study design, and assumptions clear before interpreting any interval.

## What a confidence procedure promises

In the frequentist framework, a 95% confidence procedure has 95% coverage when its assumptions hold: if the same sampling and analysis process were repeated many times, about 95% of the resulting intervals would include the fixed parameter. Once one particular interval has been calculated, the parameter is fixed and the interval is observed. The confidence level does not mean there is a 95% probability that this fixed value is inside this realized interval. That probability interpretation belongs to a different framework and requires a probability model for the parameter.

An interval depends on both the estimate and the uncertainty calculation. For a mean difference, a simple t interval has the form

**estimate ± critical value × standard error.**

For `n` independent paired differences with sample mean `d̄` and standard deviation `s_d`, a familiar form is **d̄ ± t* s_d/√n**, where `t*` is a critical value with `n−1` degrees of freedom for the chosen confidence level. This simple construction assumes the paired differences are the independent sampling units and that the t procedure is appropriate for their distribution. Other designs require other standard errors and procedures. A 95% label does not repair a poor sampling frame, dependence, unmodeled bias, or a mismatch between the estimand and the analysis.

As a synthetic calculation, suppose 25 independent paired-difference records have a mean change of 4.0 mm and a sample standard deviation of 2.0 mm. The standard error is `2.0/√25 = 0.40 mm`. With the approximate 95% t critical value `2.064` for 24 degrees of freedom, the interval is `4.0 ± 2.064(0.40) mm`, or approximately `[3.17, 4.83] mm`. Under the stated model, this interval excludes zero. It does not by itself tell us whether 4 mm is important, whether the pairing was appropriate, or whether the sample represents the intended population.

## Magnitude, precision, and practical importance

The point estimate describes the measured magnitude on its scale. The interval width describes precision under the statistical procedure: narrower intervals usually indicate less sampling uncertainty for that estimand and model. They do not show that the estimate is unbiased or free of measurement error. A large sample from a selected or systematically mismeasured group can produce a narrow interval around the wrong target. Precision is not accuracy.

The scale matters. A mean difference of 4 mm has a direct physical interpretation when the measured variable is length. A standardized effect divides a difference by a measure of variability, producing a unitless quantity that can help compare scales, but the chosen standard deviation and population can change its meaning. A ratio effect, such as a risk ratio, answers yet another question and requires a meaningful reference group and a defined outcome. Report a scale that supports the scientific question rather than selecting a metric only because it yields a familiar label.

Compare the two estimates in the preserved practice item. Study A estimates 5.0 with a 95% interval from 4.8 to 5.2; Study B estimates 0.5 with an interval from −0.2 to 1.2. A is larger and more precise in the stated units. B is smaller and less precise, and its interval is compatible with zero as well as with modest effects in either direction. A's interval excluding zero is not proof of importance, and B's interval including zero is not proof of no effect. If a practically meaningful threshold is known, compare the whole interval with that threshold, not just with zero.

The interval's width reflects the data, sample size, variability, and chosen confidence procedure. Increasing sample size can reduce sampling uncertainty, but it does not necessarily reduce measurement error or bias. A tiny effect can be estimated very precisely in a large sample; a potentially important effect can remain imprecise in a small one. State the units and define an interpretable threshold when the goal is to discuss practical importance.

## Regression to the mean

Measurements combine a persistent component with variation. In a simple model, an observed value can be written `X = θ + e`, where `θ` is the underlying level and `e` is a random deviation with mean zero. If people or specimens are selected because their first measurement is unusually high, that selection tends to include positive deviations. On a repeat measurement with new, independent deviations, the selected group will tend on average to be closer to its underlying level, even if no treatment or intervention has acted. The same logic applies when selecting unusually low observations.

This movement toward the average is regression to the mean. It is a consequence of selection on a noisy measurement, not proof that an intervention worked or that a biological process reversed. A comparison group, repeated baseline observations, an appropriate design, and a prespecified estimand help separate this pattern from a treatment effect. An interval around a selected group's change may quantify sampling variation while leaving the selection mechanism unaddressed. The later effect-size reading develops this issue in more detail.

## A disciplined interpretation

1. Name the estimand, comparison, population, units, and sampling unit.
2. State the design and assumptions that support the standard error and interval procedure.
3. Report the point estimate and interval together; interpret the interval as a property of the repeated-sampling procedure in the frequentist framework.
4. Separate magnitude from precision and compare results with a meaningful threshold when one is available.
5. Consider bias, measurement error, selection, dependence, and practical importance before drawing a broader conclusion.

These steps do not establish causation, biological relevance, clinical value, or reproducibility. Those conclusions need evidence matched to the question and study design. All quantities in the examples are synthetic teaching values, not results about a real intervention, organism, or person.

## Reference

MIT OpenCourseWare, **18.05 Introduction to Probability and Statistics**, Spring 2022, Reading 23a: “Confidence Intervals: Three Views.” This is a link-only technical reference; the reading, examples, exercises, figures, and other assets are not copied or adapted here.
