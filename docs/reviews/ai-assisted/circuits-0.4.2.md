# Electrical Circuits & Instrumentation 0.4.2 — amplifiers and analog front ends

Date: 2026-10-10. Codex expanded the week-4 amplifier reading and added gain/range checks. The same AI assistant authored the reading and regression, so these checks are not independent electrical-engineering, hardware-safety or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson derives inverting and non-inverting gain under the ideal negative-feedback model, then states when that model fails. It discusses differential/common-mode input, reference bias for a unipolar ADC, output headroom, bandwidth, noise and real-device checks. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 7 and 12.

## Numerical checks

A non-inverting stage with $R_f=90$ kΩ and $R_g=10$ kΩ has ideal gain 10; a 0.10 V input gives 1.0 V. The corresponding inverting stage has gain −9 and gives −0.90 V. A constructed 2 mV differential input with gain 100 and 1.65 V reference spans 1.45–1.85 V, within the stated assumed 0.2–3.1 V output window. These are ideal-model checks, not device validation.
