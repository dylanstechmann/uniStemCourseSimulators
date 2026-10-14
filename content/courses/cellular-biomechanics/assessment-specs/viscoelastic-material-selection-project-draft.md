# Viscoelastic material selection across loading time scales: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. Candidates A, B and C are mathematical teaching models, not real gels, tissues or cell substrates. Every parameter and design threshold below is synthetic.

## Stipulated model and decision brief

Each candidate follows a standard linear solid with relaxation modulus

`E(t) = E_inf + E_1 exp(-t/tau)`

and complex-modulus components

`E'(omega) = E_inf + E_1 (omega tau)^2/[1+(omega tau)^2]`,
`E''(omega) = E_1 (omega tau)/[1+(omega tau)^2]`.

Use the values in [the candidate table](viscoelastic-material-candidates.csv), `E_inf` and `E_1` in kPa, `tau` in seconds, and angular frequency `omega` in rad/s. Assume small-amplitude linear response and a fixed temperature. For this fictional selection exercise, a candidate should have equilibrium stress no greater than `0.25 kPa` under a held strain of `0.050`, storage modulus of at least `8.0 kPa` at `omega=1 rad/s`, and loss tangent `E''/E'` no greater than `0.15` at that frequency.

## Work sequence

1. Compute each instantaneous modulus `E(0)=E_inf+E_1` and equilibrium modulus. Rank the candidates in each limit and explain why a single stiffness label cannot represent both.
2. Under a step strain of `0.050`, calculate the stress at `t=5.0 s` and as `t` tends to infinity for each candidate. Keep stress in kPa.
3. Calculate `E'`, `E''` and `tan(delta)` for each candidate at `omega=0.010 rad/s` and `omega=1.00 rad/s`. Explain the change in the storage-modulus ranking across time scales.
4. Apply the stated decision thresholds and identify which candidate(s) satisfy every requirement. Report the binding criterion for each rejected candidate.
5. At `omega=1 rad/s` and strain amplitude `epsilon_0=0.030`, calculate dissipated energy density per cycle, `W_diss = pi E'' epsilon_0^2`, converting from kPa to J/m³. Compare energy loss with stored response; do not treat either as a cell outcome.
6. State at least two model assumptions that a qualified reviewer would want examined before applying the calculation to measurements, and name a measurement that could test each assumption without proposing a protocol here.
7. Separate the material-model conclusion from a mechanobiology conclusion. The stipulated models cannot establish how any cell would signal, adhere, grow or differentiate.

## Author calculation key

The instantaneous moduli for A/B/C are `10/8/7 kPa`; the equilibrium values are `1/4/2 kPa`. At `t=5 s`, the stresses are approximately `0.322939/0.200000/0.101684 kPa`; at equilibrium they are `0.050/0.200/0.100 kPa`.

At `omega=0.010 rad/s`, `(E', E'')` in kPa are approximately A `(1.089109, 0.891089)`, B `(4.000004, 0.004000)` and C `(2.000500, 0.049995)`. At `omega=1.00 rad/s`, they are A `(9.910891, 0.891089)`, B `(4.039604, 0.396040)` and C `(4.500000, 2.500000)`. The storage-modulus ordering changes: B exceeds A at low frequency, while A exceeds B at the higher frequency. At the higher frequency, `tan(delta)` is approximately `0.0899`, `0.0980` and `0.5556`, respectively. Only A meets all three stipulated thresholds; B fails the storage-modulus threshold and C fails both the storage-modulus and loss-tangent thresholds.

At `omega=1 rad/s`, energy dissipated at strain amplitude `0.030` is approximately `2.52 J/m³` for A, `1.12 J/m³` for B and `7.07 J/m³` for C. These are consequences of the stipulated linear models, not measured material properties.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Time-scale reasoning | Distinguishes instantaneous, equilibrium and frequency-dependent moduli |
| Calculation | Computes relaxation stress, complex moduli, loss tangent and energy density with units |
| Decision | Applies all thresholds and identifies trade-offs without substituting one modulus for another |
| Assumptions | Names limits of the single-relaxation-time linear model and an appropriate check |
| Scope | Keeps the model-based material choice separate from claims about cell behavior or real materials |

The rubric has no point weights or automatic prose grader. Mathematical accuracy, instructional design, accessibility and workload need qualified review. Do not activate this draft or describe it as a course assessment until that review and the course's missing homework, exams and broader laboratory sequence are addressed.

## Provenance

Original authoring and synthetic parameters, CC BY 4.0, developed with substantial AI assistance. No third-party data or laboratory procedure is included.
