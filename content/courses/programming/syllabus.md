# Programming & Numerical Methods for Bioengineering

**Maturity: partial. Version: 0.4.9.**

A practical introduction to reproducible scientific code, numerical methods, model fitting, validation and communication for bioengineering data.

## Prerequisites

Algebra, introductory calculus and basic probability; linear algebra and differential equations are useful. Structured course relations remain subject to author review, and this package establishes no university prerequisite equivalency.

## Authored outcomes

- Write modular code with explicit inputs and outputs.
- Select numerical methods and diagnose error.
- Fit models without confusing interpolation and validation.
- Make reproducible plots and document data provenance.
- Interpolate a value from tabulated data and assess the error and domain limits.

## Proposed 14-week schedule

This is a proposed scope, not a measured or reviewed semester. The interpolation reading is grouped with regression in week 10 to compare methods within the same approximation unit.

| Week | Theme | Readings |
|---|---|---|
| 1 | Data structures, units and reproducible code | Data structures, units and provenance |
| 2 | Input contracts and pure functions | Parsing and validated scientific functions |
| 3 | Testing scientific functions | Known answers, tolerances, seeds and provenance |
| 4 | Algorithmic cost and scaling | Cost, scaling and data structures |
| 5 | Array shapes and memory-aware reductions | Broadcasting and safe reductions |
| 6 | Floating-point arithmetic | Rounding, cancellation and safe comparisons |
| 7 | Numerical integration and differential models | Numerical integration and differential models |
| 8 | Root brackets, residuals and conditioning | Root solving and scale-aware stopping |
| 9 | Quadrature and stability checks | Quadrature, step error and stability |
| 10 | Interpolation, regression, uncertainty and validation | Interpolation: exact fit at nodes and error between them; regression, uncertainty and validation |
| 11 | Linear systems, conditioning, least squares and scaled coordinates | Linear-system conditioning and least-squares geometry |
| 12 | Visualization and uncertainty communication | Reproducible visualization |
| 13 | Grouped validation and reproducible reports | Thresholds and held-out reporting |
| 14 | Virtual lab | Contract checks and held-out donor reports |

## Assessment and study policy

The package has 16 readings, 106 public practice items and 56 retrieval cards. Every lesson has open formative items mapped to provisional objectives, and the synthetic-data lab has a public data file. Learner code execution is disabled; the checks assess method selection, calculations and interpretation, not submitted implementations. Nothing is graded for university credit. Workload has not been measured.

## Inactive project

The [sensor-calibration project](assessment-specs/integrative-sensor-calibration-project.md) is an inactive, ungraded draft. It is not part of the assessment schedule and makes no claim about real sensors, donors or classifier performance.

## Current limitations

The proposed schedule is unmeasured and unreviewed; graded homework, exams, full labs and a cumulative graded project remain absent. Interpolation coverage consists of one hand-worked quadratic comparison; implemented barycentric and piecewise interpolation algorithms and a systematic stability study remain outside the sequence. Direct, iterative and sparse solver comparisons and eigenvalue algorithms also remain limited. All data and functions are synthetic examples. Qualified subject, code, accessibility and workload review remain open.

## Sources and licensing

MIT OCW 2.086 Fall 2014 is an undergraduate numerical-computation comparator. Its calendar places interpolation in the opening numerical-calculus unit and later lists least-squares model fitting; its syllabus also includes interpolation, regression, integration, differentiation, equation solving and deterministic/probabilistic methods. The local lesson is an original, narrow comparison. MIT material is linked only and none was copied or adapted. See [content/SOURCES_AND_LICENSES.md](../../SOURCES_AND_LICENSES.md). No affiliation or equivalency is implied.
