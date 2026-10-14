# Cell Biology public numeric-key arithmetic check (0.36.0)

**Date:** 2026-10-10  
**Scope:** all 20 `numeric`-type items in `content/courses/cell-biology/question-banks/practice.json`.  
**Review status:** author-side arithmetic cross-check only. These calculations were recomputed from the prompt data and stated equations, then compared with the public key and tolerance. They are not independent scientific or assessment review, and do not approve any inactive candidate for grading.

No numeric question in this bank currently has authored randomization variants. This audit does not cover numeric cells embedded in CSV uploads, structured questions, lab datasets, inactive assessment candidates, assumptions behind the models, or scientific validity of the source data.

| Item | Recalculation | Recomputed result | Key and tolerance | Check |
| --- | --- | ---: | ---: | --- |
| `cell-biology-3:check` | 120 × 6 / (3 + 6) | 80 μmol/min | 80 μmol/min (±1.2) | within tolerance |
| `cell-biology-9:coupling-energy` | (+12.0) + (−21.0) | -9 kJ/mol | -9 kJ/mol (±0.05) | within tolerance |
| `cell-biology-9:rate-at-km` | kcat × [E] × Km/(Km + Km) = 4 × 20 / 2 | 40 nM/s | 40 nM/s (±0.4) | within tolerance |
| `cell-biology-10:rate-prediction` | 120 × 40 / (20 + 40) | 80 nM/s | 80 nM/s (±0.8) | within tolerance |
| `cell-biology-11:resolution-estimate` | 0.61 × 520 / 1.30 | 244 nm | 244 nm (±1) | within tolerance |
| `cell-biology-12:er-marker-recovery` | 4 + 18 + 68 + 5 | 95 % | 95 % (±0.5) | within tolerance |
| `cell-biology-13:hybrid-fraction` | After the second round, one of two daughter duplexes retains an original heavy strand | 50 % | 50 % (±0.5) | within tolerance |
| `cell-biology-16:chip-percent-input` | 100 × 0.01 × 2^(25 − 22) | 8 % | 8 % (±0.1) | within tolerance |
| `cell-biology-17:isoform-fraction` | 100 × 60 / (60 + 30) | 66.666667 % | 66.7 % (±0.2) | within tolerance |
| `cell-biology-18:protein-half-life` | signal falls from 80 to 40 in 4 h; one half-life = 4 h | 4 h | 4 h (±0.05) | within tolerance |
| `cell-biology-19:affected-child-risk` | (1/2 transmission) × 80% penetrance | 40 % | 40 % (±0.1) | within tolerance |
| `cell-biology-21:occupancy-model` | 1 / (1 + 4) | 0.2 | 0.2 (±0.005) | within tolerance |
| `cell-biology-21:relative-response` | 36 / 4 | 9 | 9 (±0.05) | within tolerance |
| `cell-biology-24:uniform-stress` | 12 × 10^−6 N / (3 × 10^−9 m²) | 4000 Pa | 4000 Pa (±40) | within tolerance |
| `cell-biology-24:yap-relative-increase` | 100 × (0.76 − 0.28) / 0.28 | 171.42857 % | 171.429 % (±2) | within tolerance |
| `cell-biology-25:phase-snapshot` | 100 × 60 / 240 | 25 % | 25 % (±0.25) | within tolerance |
| `cell-biology-25:edu-relative-reduction` | 100 × (27 − 11) / 27 | 59.259259 % | 59.3 % (±0.6) | within tolerance |
| `cell-biology-27:functional-fraction` | 100 × 18 / 80 | 22.5 % | 22.5 % (±0.225) | within tolerance |
| `cell-biology-12:image-quantification-contrast` | 22% − 13% = 9 percentage points | 9 percentage points | 9 pp (±0.01) | within tolerance |
| `cell-biology-3:delta-g-from-k` | −8.314 × 298 × ln(10) / 1000 kJ/mol | -5.7048204 kJ/mol | -5.7 kJ/mol (±0.05) | within tolerance |

All 20 recomputed values fall within their declared numeric tolerances. The `cell-biology-12:image-quantification-contrast` key uses the context-specific `pp` unit. The learner must enter `pp`; the grader rejects `%`, keeping an absolute percentage-point difference distinct from relative percent change.
