# Frontier versus established

**Date:** 2026-11-27
**Scope:** Learner-facing RC charging and discharging correction on the `finish-cell-culture-practice` branch.

## Established for this correction

- Independent arithmetic using `R = 100 kΩ`, `C = 10 μF`, and `t = 0.693147 s` gives `τ = RC = 1.000000 s`, `100 exp(−t/τ) = 50.000009028%` initial voltage remaining, and `100 exp(−2t/τ) = 25.000009028%` initial energy remaining.
- Source-level inspection confirms that tool ID `rc` retains the `#/tools/rc` route. The current unit, component, and Playwright test definitions cover the discharge arithmetic, accessible tool/navigation labels, `aria-current`, the direct route, and the 390 × 844 horizontal-overflow check. These are test definitions and source inspection, not evidence that the current tests passed.

## Current validation gap

The current component tests, browser tests, and production build were **NOT run** because Docker was unavailable and the managed project container could not be started. Earlier native test or build results are not evidence for this correction.

## Frontier / open

- Execute the current focused component and unit tests, Playwright browser tests, and production build in the managed project environment.
- Complete the browser and small-screen verification, including accessible naming, the stable direct route, discharge results, and absence of horizontal overflow.
- Obtain qualified instructional and scientific review of the corrected explanation and worked example.
- University equivalence remains unestablished and would require separate institutional evaluation.
- Accreditation remains unestablished and is not claimed by this repository or correction.

## Update when evidence changes

Update this record when new evidence changes a claim or closes a validation gap. Move an item from frontier/open to established only with current, directly relevant evidence; retain skipped checks and review limits until then.
