# Programming & Numerical Methods 0.4.4 — visualization and uncertainty

Date: 2026-10-10. Codex expanded the week-12 reading and added a paired-data interval check. The same AI assistant authored the reading and regression, so these checks are not independent statistical or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson develops paired-observation plots, independent-unit counts, interval definitions, axis choices and provenance. A four-donor synthetic before/after example distinguishes donor-level changes from individual measurements and names the assumptions of a paired-$t$ interval. Existing questions, keys, objectives and counts are unchanged. All scheduled lessons now have expanded or original instructional text; the toy data lab is not a laboratory sequence.

## Numerical checks

Constructed paired changes $[1,0,2,1]$ mg/mL have mean 1 and sample standard deviation $\sqrt{2/3}\approx0.8165$ mg/mL. With standard error $0.4082$ mg/mL and $t_{0.975,3}\approx3.1824$, the interval is approximately $[-0.299,2.299]$ mg/mL. The regression recomputes the mean, spread and interval; it does not establish a real treatment effect.
