# Visualization and uncertainty communication

A scientific plot is a quantitative claim. Its labels, scales, marks and interval definitions determine what a reader can infer. Show the observations when possible, identify the independent sampling unit, state units and make comparisons legible. A clean graphic cannot correct a biased design, but it can reveal spread, outliers, pairing and missing structure that a summary alone hides.

## Preserve the design in the display

Suppose four donors are each measured before and after a constructed treatment:

| Donor | Before (mg/mL) | After (mg/mL) | Paired change (mg/mL) |
|---|---:|---:|---:|
| A | 2 | 3 | 1 |
| B | 3 | 3 | 0 |
| C | 4 | 6 | 2 |
| D | 5 | 6 | 1 |

Plot each donor's two points and connect the pair. This makes the within-donor direction visible; two separate bars would hide which changes belong together. A companion plot of the four differences can show a zero reference line and the mean paired change, which is 1 mg/mL. The independent sample size is four donors, not eight measurements or the number of cells within them.

Use position and length for quantitative comparisons. Label the vertical axis `concentration (mg/mL)`, state what each point represents, and keep the paired group identity visible. If multiple points overlap, a small transparent offset can reveal them, but jitter is display-only and must not change the underlying values. Color should not be the sole group cue; use distinct shapes or direct labels as well.

## Name the uncertainty interval

The four paired changes are $1,0,2,1$ mg/mL. Their mean is 1 mg/mL and their sample standard deviation is about 0.82 mg/mL, describing variation among these donor-level changes. A standard error instead describes precision of the estimated mean under a sampling model; a confidence interval adds a stated procedure and coverage level. These are different quantities and answer different questions.

For illustration, a two-sided 95% paired-$t$ interval for the mean uses the four independent donor differences, their sample standard deviation, and a $t$ critical value with three degrees of freedom. It is approximately $[-0.30,2.30]$ mg/mL. With only four constructed donors, the interval is wide and depends on the paired differences being an appropriate independent sample with a roughly normal distribution. It does not show where 95% of individual donor responses lie, and it does not establish a treatment effect or biological relevance.

Choose the interval before plotting and label it directly, for example `mean paired change; 95% t interval across donors`. If the bars show standard deviation, standard error, a confidence interval or a measurement range, say which one. An unexplained “error bar” has no unique interpretation. Include the denominator and the independent unit in the caption.

## Make scales and processing visible

Use a zero baseline for bars when their length encodes magnitude. For points and paired differences, a nonzero axis can be useful when its limits are visible and a meaningful reference such as zero remains clear. A logarithmic scale changes distances and requires positive values; label it and do not interpret equal visual distances as equal additive changes. For time series, show sampling times and identify smoothing or missing intervals rather than drawing an uninterrupted line that implies observations were made there.

Retain the raw values and document transformations, exclusions, units, sample counts and plotting code version. A plot of a small experiment should let a reader recover the observations and the summary definition. Visual clarity supports scrutiny; it does not substitute for a valid sampling design, independent replication or qualified statistical review. The example is synthetic and makes no claim about an actual treatment.
