# Cell Biology public numeric-key arithmetic check (0.39.0)

**Date:** 2026-10-10  
**Scope:** all 21 `numeric`-type items in the current public Cell Biology practice bank.  
**Review status:** author-side arithmetic cross-check only. This supplements the 20-item 0.36.0 audit; it is not independent scientific or assessment review and does not approve inactive candidates for grading.

The prior 20 public numeric items and their keys are unchanged from the [0.36.0 audit](cell-biology-numeric-key-audit-0.36.0.md). Version 0.39.0 adds one numeric item; the other two new questions are single-choice. No public numeric question has an authored randomization variant. Numeric cells embedded in CSV uploads, structured questions, lab datasets and inactive candidate packets remain outside this audit.

| Item | Recalculation | Recomputed result | Key and tolerance | Check |
| --- | --- | ---: | ---: | --- |
| `cell-biology-9:rate-at-twice-km` | `Vmax = 4 s⁻¹ × 20 nM = 80 nM/s`; at `[S] = 2 Km`, `v₀ = 80 × 2/(1 + 2)` | 53.3333 nM/s | 53.3333 nM/s (±0.5) | within tolerance |

The calculation assumes the prompt's stipulated active-enzyme concentration, turnover rate, substrate concentration and simple initial-rate model. It checks the arithmetic and declared key only; it does not independently validate whether the model or its assumptions are appropriate for a biological system.
