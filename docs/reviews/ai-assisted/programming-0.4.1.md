# Programming & Numerical Methods 0.4.1 — data contracts and reproducibility

Date: 2026-10-10. Codex expanded the week-1 reading and added a separate unit-conversion check. The same AI assistant authored the lesson and regression, so these checks are not independent code, subject-matter or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson develops data contracts for units, ranges, shape and missing values; contrasts records and arrays; describes small pure functions and hand-checkable cases; and connects immutable raw inputs with provenance. The constructed mass/volume example converts microlitres before calculating concentration. Existing questions, keys and objectives are unchanged; three compact prototype readings remain.

## Numerical checks

The example converts $500\,\mu\text{L}$ to $0.5\,\text{mL}$ before dividing 1.5 mg, giving 3 mg/mL. The regression recomputes the conversion and resulting concentration. It does not run learner-authored code or validate an assay protocol.
