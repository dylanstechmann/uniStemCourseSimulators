# Experimental design, regression, and reproducibility

Good analysis begins before data collection. The design determines what was randomized, what counts as an independent replicate, which comparisons are supported, and what can be generalized. Regression can describe relationships and account for measured design factors, but it cannot repair a confounded experiment or create independent information that was never collected. Keep the scientific question, assignment mechanism, experimental unit, and analysis model connected from planning through reporting.

## Identify units and sources of variation

The experimental unit is the smallest unit independently assigned to a treatment or condition. It may be a person, animal, donor, culture dish, well, or batch, depending on where assignment occurs. An observational unit is where a value is recorded, such as a cell, image field, technical replicate, or time point. These can differ. If a treatment is assigned to four animals per group and 100 cells are measured in each animal, the study has four independently assigned animals per group, not 400 independent animals. The cell measurements can describe within-animal variation and improve the precision of an animal-level summary, but they do not supply the between-animal replication needed to generalize across animals.

Replication means independently repeating the intervention at the unit relevant to the claim. Technical repeats of the same specimen help reveal instrument or processing variability. Biological or subject-level repeats represent variation across independent entities. Labels alone do not determine independence: separate wells may still share a single treated cell suspension, plate, litter, or processing event. Draw a hierarchy of assignment, sampling, and measurement before choosing an analysis. A multilevel model can represent dependence when the design contains enough independent groups; it cannot convert many subsamples from one assigned unit into many independently randomized units.

## Randomize and block for a reason

Random assignment of experimental units to conditions reduces systematic differences between groups in expectation, including differences from factors that were not measured. It does not guarantee balance in a small sample, and it does not make a nonrandom sample representative of a wider population. Randomize at the level where the intervention is assigned. If a treatment is applied to a whole dish, randomizing individual cells within that dish does not create cell-level treatment replication.

Blocking is useful when a known nuisance factor may shift the response, such as processing day, donor, plate, instrument, or starting-size category. Form blocks before treatment outcomes are known, then allocate each treatment within each block. This makes comparisons occur across more similar units and can reduce residual variation. For example, if samples are measured on four days, distribute both conditions across every day and randomize processing order within day. If all controls are measured on day one and every treated sample on day four, treatment and day are entangled; adding “day” to a regression cannot separate their effects when the design contains no within-day treatment comparison. Blocking does not guarantee a benefit when the block variable is irrelevant, mishandled, or modeled inconsistently with the allocation.

Randomize processing order as well as treatment allocation when drift, operator learning, temperature, or instrument state could track the order. Blinding can reduce expectation-driven measurement choices. Record the allocation method, unit, blocks, exclusions, and outcome definitions. Randomization, blocking, and blinding address different paths to bias; none substitutes for adequate independent replication or reliable measurement.

## Use regression to represent the design

Regression expresses an expected outcome as a function of predictors. For a continuous response with one treatment indicator and a day block, a simple model is

**outcome = baseline + treatment effect + day effects + residual.**

The treatment coefficient estimates a conditional mean difference under the model. With randomized treatment allocation within each day, that comparison follows the design; with observational treatment assignment, adjusting for recorded predictors only addresses measured confounders and the model's assumptions. A regression coefficient does not become causal just because several covariates appear on the right-hand side. Unmeasured confounding, selection, measurement error, and a misspecified relationship may remain.

For a grouped or repeated design, the model may need donor, animal, dish, or subject effects, and measurements may need a repeated-measures covariance structure. Another defensible approach in a simple design is to summarize subsamples to one value per independently assigned unit, then analyze those unit-level values. The choice depends on the target, design, and assumptions; report it explicitly. Do not use cell count or image count as the sample size when treatment assignment and generalization occur at a higher level.

## Read residuals as diagnostics, not proof

Residuals are observed outcomes minus fitted values. A residual-versus-fitted plot can reveal curvature, unequal spread, or influential points; residuals plotted in collection order can reveal drift or dependence; and a normal quantile plot can show departures from the normal-error approximation when that assumption is used for small-sample inference. Check whether the conditional mean is represented reasonably, whether spread changes with fitted values, whether observations are independent at the modeled level, and whether a few units dominate the fit. The relevant residuals are those from the analysis model at the level of independent units, not simply from a plot of every cell as if cells were independent.

Residual checks are informative but not a pass/fail certificate. With few independent units, plots have little ability to reveal modest departures. Normality concerns model errors or conditional residuals, not a requirement that every raw variable look normal. A good-looking plot cannot prove randomization, eliminate confounding, or establish that the sample represents the target population. Report meaningful deviations and consider a model or design matched to the data rather than applying a transformation solely to obtain a preferred p-value.

## Worked synthetic design

Suppose 24 independent donor-derived samples are assigned to two conditions across four processing days. Place six samples in each day block, allocate three to each condition at random within every day, and randomize measurement order within each day. If the intervention is assigned to each donor-derived sample, there are 24 experimental units. Multiple wells, fields, or cells measured from a sample are nested observations. A model with treatment and day terms estimates the comparison while accounting for the block; a donor-level summary is another option for a simple design. Inspect residuals from that unit-level or grouped model. If condition A were run only on the first two days and condition B only on the last two, a day-adjusted treatment estimate would not be separately identified from the schedule.

This example is synthetic and illustrates a design, not an experimental protocol. Its interpretation still depends on the intended population, sample selection, measurement process, model, missing data, and faithful random allocation. The sample size is the number of independently assigned donor-derived units for this claim, not the number of images or cells.

## Make the work reproducible

Before analysis, record the primary outcome, estimand, independent unit, block structure, sample-size rationale, exclusions, planned contrasts, and treatment of missing observations. Preserve an analysis script that starts from clearly identified data and produces the reported summaries. Track data cleaning, software versions, and deviations from the plan. Share enough methods and metadata for another analyst to understand how records map to experimental units and how results were calculated, while respecting privacy and other governance limits.

Reproducibility is not the same as replication: rerunning code checks computational transparency, while repeating a study with new independent units checks whether evidence recurs. Both depend on a design that exposes the unit, comparison, and assumptions. MIT OpenCourseWare and the open methods papers listed for this lesson are optional, link-only references. No source wording, figure, exercise, or dataset has been copied or adapted.
