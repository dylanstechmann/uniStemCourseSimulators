# Probability, Biostatistics & Experimental Design review handoff

This handoff targets Statistics package version 0.6.0. The [review snapshot](STATISTICS_REVIEW_SNAPSHOT.md) identifies the exact public files. The course remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the 14-week proposal, objective and outcome mappings, prerequisites, and the placement of finite- and continuous-prior updating in week 13.
- Independently recalculate the Beta(2,2) to Beta(10,4) update, the posterior mean and mode, the uniform-prior sensitivity comparison, and the Beta–Binomial probability for two successes in three future trials.
- Check that the future-count calculation integrates parameter uncertainty, and examine the common-rate, conditional-independence and prior assumptions against likely biological and engineering examples.
- Recalculate representative confidence interval, hypothesis-testing, power, regression, resampling, time-to-event and nested-design examples.
- Review the synthetic pilot and inactive protocol project for ethical boundaries, feasible workload, accessible alternatives and separation of a plan from an observed result.

## Author-side evidence and its limits

The repository content validator passed for 25 packages, 421 lessons, 2,618 questions, 1,449 cards and 25 cases with zero errors or explicit depth warnings. The Beta–Binomial arithmetic was independently recalculated: the posterior is Beta(10,4), its mean is 5/7, the exact two-of-three predictive probability is 11/28, and a uniform-prior comparison gives Beta(9,3) with mean 0.75. The package digest matches the snapshot. No test suite was run for 0.4.7. These checks do not establish independent statistical review, research-ethics approval, learner understanding, accessible usability, measured workload or course equivalence. The project is unscheduled, ungraded and collects no data.

## Review record to complete only after review

After an actual review, record reviewer qualifications, date, exact package version and archive digest, artifacts examined, specific findings and disposition. Keep separate judgments for statistical correctness, study-design quality, assessment, ethics, accessibility, workload and release. Do not treat a passing validator or matching hash as approval.

## Open project route (2026-10-22)

The current guide, separate worked example, rehearsal and five private milestone self-checks make the existing project usable as ungraded practice. [The route regression tests](../tests/content/test_remaining_course_project_routes.py) independently recalculate every new numeric field and exercise the backend grader, including exact counts and continuous-quantity precision. Review the written explanation, evidence limits and proposed workload independently; automated arithmetic is not subject review. Historical snapshot evidence remains preserved.

## Joint-law/likelihood/regression target (2026-10-22)

Current target 0.6.0 adds four foundations,four reports and twenty-four checkpoints/cards. Check triangular support/marginals/conditional moments,total variance and zero-covariance dependence; event/censored exposure,score,curvature and open-domain supremum; known-variance normal completion of the square and shared future covariance; full-rank regression,residualization,reduced slope,residual degrees of freedom and mean-versus-new prediction. Verify exact binomial coverage,all-failure resampling,central-tail conventions and inclusive sharp-null allocation counts. All inputs are synthetic; independent-unit/design assumptions remain explicit. Code/proofs/reports,broader theory,empirical validity,workload and qualified review remain open. Earlier evidence above is historical; the current snapshot pins the new target.
