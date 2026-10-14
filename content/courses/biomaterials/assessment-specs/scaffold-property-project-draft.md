# Scaffold property comparison: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. The candidate values and thresholds are synthetic teaching constructs, not specifications for a material, scaffold, implant or tissue-engineering application.

## Purpose and scenario

Compare a small portfolio of hypothetical scaffold profiles across architecture, transport and time-dependent mechanical support. The project uses explicit constraints rather than a weighted score: a pass on one property cannot silently compensate for failure on another. The portfolio extends the existing degradation lab, which analyzes one constructed time course, into a multi-candidate evidence exercise.

The public [candidate table](scaffold-property-comparison.csv) gives initial porosity `φ`, initial modulus `E₀`, a permeability index and a modulus half-time `t₁/₂`. For this exercise alone, assume

\[
E(t)=E_0 2^{-t/t_{1/2}}.
\]

The table is fully synthetic. No equation here predicts biocompatibility, cell response, structural safety or in-vivo behavior.

## Teaching criteria

A hypothetical candidate passes at a stated horizon only if it meets all four stipulated criteria:

- `φ ≥ 0.65`;
- permeability index `≥ 4` (in the CSV's scaled column);
- `E₀ ≥ 1.5 MPa`;
- projected modulus at the chosen horizon `E(t) ≥ 0.8 MPa`.

These numbers exist only to support transparent arithmetic and are not acceptance criteria for a real application.

## Work sequence

1. Recalculate `E(42)` and `E(56)` for candidates A, B and C. Keep at least four significant digits during calculations and report MPa to three decimals.
2. Build a pass/fail matrix for the four criteria at day 42. Identify which candidates fail architecture, transport, initial mechanics or the time-dependent modulus requirement; do not average criteria into a single score.
3. Derive the time at which each modeled modulus reaches 0.8 MPa. Compare the resulting support horizons, then identify the maximum horizon that meets every stipulated criterion.
4. Repeat the feasibility decision at day 56 and explain why a candidate that passes at day 42 can fail under the longer horizon.
5. List important missing evidence that prevents the table from supporting a real material decision, including uncertainty, degradation modes, geometry, loading, cell response, biological evidence and application-specific acceptance criteria.

## Author calculation key

| Candidate | `E(42)` MPa | `E(56)` MPa | Time to `0.8 MPa` (days) |
|---|---:|---:|---:|
| A | 0.871 | 0.660 | 46.267 |
| B | 0.350 | 0.220 | 16.954 |
| C | 0.938 | 0.770 | 53.286 |

At day 42, A meets the modeled modulus threshold but fails porosity and permeability; B meets porosity and permeability but fails initial and day-42 modulus; C passes all four stipulated teaching criteria. At day 56, C's modeled modulus is below 0.8 MPa, so none of the candidates passes all four. Solving `E₀ 2^(−t/t₁/₂)=0.8` gives `t=t₁/₂ log₂(E₀/0.8)`. These classifications follow only from the stipulated table, exponential assumption and arbitrary thresholds.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Degradation calculation | Applies the exponential half-time relation with correct values and units |
| Constraint logic | Evaluates every criterion separately and does not average away a failure |
| Time horizon | Solves the threshold time and repeats the decision at the longer horizon |
| Evidence limits | Identifies missing material, biological and uncertainty evidence |
| Scope | Avoids presenting the synthetic comparison as a real selection or safety recommendation |

The rubric has no point weights or automatic prose grader. Workload, accessibility, mathematical accuracy and instructional design need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and synthetic candidate values, CC BY 4.0, developed with substantial AI assistance. No third-party dataset or real-world protocol is included.
