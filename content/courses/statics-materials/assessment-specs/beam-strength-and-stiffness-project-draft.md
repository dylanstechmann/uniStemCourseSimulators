# Beam strength and stiffness comparison: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. The beam, load, candidate properties and thresholds are synthetic teaching values. This is not a design basis, safety factor recommendation, or analysis for a real structure, fixture, implant or device.

## Purpose and model

Compare three hypothetical rectangular beam sections using equilibrium, bending stress and small-deflection beam theory. Unlike the fatigue lab, this project focuses on a static midpoint load and the distinction between strength and stiffness limits.

Use a simply supported beam of span `L=0.300 m` and width `b=0.020 m`, with a centered point load `F=30 N`. The public [candidate table](beam-candidate-comparison.csv) supplies depth `h`, elastic modulus `E` and yield strength `S_y`. For this idealized exercise, use

\[
R_A=R_B=F/2,\quad M_{max}=FL/4,\quad I=bh^3/12,
\]

\[
\sigma_{max}=M_{max}(h/2)/I=6M_{max}/(bh^2),\qquad
\delta_{max}=FL^3/(48EI).
\]

Assume linear-elastic Euler–Bernoulli behavior and ignore shear deformation, stress concentrations, joints, fatigue, manufacturing variation and uncertainty. These assumptions are for arithmetic only.

## Teaching criteria and work sequence

For this exercise, classify a candidate as a pass only if both `σ_max ≤ S_y/2` and `δ_max ≤ 0.600 mm` hold.

1. Draw the free-body diagram and calculate support reactions and maximum bending moment.
2. Convert every candidate property to consistent SI units. Calculate `I`, maximum bending stress and maximum deflection for A, B and C.
3. Apply the two criteria separately. Explain why a candidate can pass the strength check and fail the stiffness check.
4. For each candidate, calculate the load at which the strength limit would be reached and the load at which the deflection limit would be reached. The smaller value controls under this simplified model.
5. Re-evaluate the only passing candidate at a 20% higher load, then identify the missing evidence that prevents this calculation from being a real design decision.

## Author calculation key

The reactions are `15 N` each and `M_max=2.25 N·m`. The recalculated results are:

| Candidate | `I` (m⁴) | `σ_max` (MPa) | `δ_max` (mm) | Strength load limit (N) | Deflection load limit (N) |
|---|---:|---:|---:|---:|---:|
| A | `9.720×10⁻⁹` | 2.083 | 0.868 | 144.000 | 20.736 |
| B | `2.304×10⁻⁸` | 1.172 | 0.488 | 192.000 | 36.864 |
| C | `1.333×10⁻⁸` | 1.688 | 1.266 | 160.000 | 14.222 |

All three pass the stipulated yield-based stress check, but only B satisfies the `0.600 mm` deflection limit at `30 N`. Its governing load limit is `36.864 N`, set by the deflection criterion. A 20% load increase gives `36 N` and predicts `0.586 mm`, still inside the classroom limit. The controlling calculation is not validation: boundary conditions, shear, stress concentrations, fatigue, imperfections, material variability, load uncertainty and actual acceptance criteria are outside this model.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Equilibrium | Correct support reactions and maximum moment |
| Stress | Consistent section moment and unit conversion |
| Deflection | Correct second moment and span/depth scaling |
| Failure criteria | Applies yield and deflection limits independently |
| Limits | Separates this idealized calculation from real structural safety or design |

The rubric has no point weights or automatic prose grader. Workload, accessibility, mathematical accuracy and instructional design need qualified review. The project remains inactive until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and synthetic candidate properties, CC BY 4.0, developed with substantial AI assistance. No third-party dataset or real-world design basis is included.
