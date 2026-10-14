# Electrical Circuits & Instrumentation 0.4.3 — filters and sampling

Date: 2026-10-10. Codex expanded the week-7 filters/sampling reading and added response and alias checks. The same AI assistant authored the reading and regression, so these checks are not independent electrical-engineering or human review. The course remains **partial, unreviewed and formative-only**.

## Scope

The lesson derives the first-order RC cutoff and magnitude, distinguishes analog anti-alias filtering from digital filtering, and explains the nominal Nyquist condition with exact-boundary phase ambiguity. It states that real filter transition bands and converter timing/acquisition matter. Existing questions, keys and objectives are unchanged; one compact prototype reading remains in week 12.

## Numerical checks

For $R=1$ kΩ and $C=10$ µF, $f_c\approx15.9155$ Hz and the magnitude at 20 Hz is approximately 0.622. A 250 Hz cosine sampled at 300 samples/s matches the 50 Hz cosine's samples. At the 150 Hz boundary, a zero-phase sine samples to all zeros while a quadrature-phase sine alternates. The existing nominal Nyquist answer remains 300 Hz; this does not specify a practical acquisition system.
