# Oxygen-transfer capacity and a growing demand: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. All concentrations, rates and time are normalized synthetic quantities. This is a mathematical paper exercise, not a vessel design, operating procedure, culture recommendation or real oxygen-control specification.

## Purpose and outcomes

Connect a substrate-style mass balance, exponential demand growth, transfer capacity and a control threshold. The exercise distinguishes an instantaneous quasi-steady capacity calculation from a transient state response. It does not repeat the existing lab's dynamic-gassing-out estimate of `kLa`.

## Model

Let `C(t)` be a normalized dissolved-oxygen index, with saturation `C*=1` and initial `C(0)=1`. The stipulated transfer coefficient is `k=0.8` per normalized time unit. Oxygen demand starts at `OUR₀=0.1` normalized concentration units per time unit and grows as `OUR(t)=OUR₀ e^(μt)`, with `μ=0.2` per time unit. The linear balance is

\[
\frac{dC}{dt}=k(C^*-C)-OUR_0e^{\mu t}.
\]

The threshold for this mathematical exercise is `Ccrit=0.4`. These values are selected only to make the calculations transparent; they are not measured biological or engineering parameters.

## Work sequence

1. Define the oxygen deficit `D=C*−C` and derive its differential equation and initial condition.
2. Solve the linear equation for `D(t)` using an integrating factor. Verify the result at `t=0` and by substitution.
3. Compute the initial transfer-minus-demand margin at `Ccrit`, then find when an instantaneous quasi-steady capacity check would first predict demand equal to transfer at that threshold.
4. Solve for the actual time at which the transient state first reaches `Ccrit`. Show that `D(t)` is strictly increasing, bracket the crossing, and calculate it numerically to three decimals.
5. Compare the quasi-steady time with the transient crossing time. Evaluate `C` at the quasi-steady time and explain why stored dissolved oxygen delays the crossing in this constructed dynamic model.
6. State where the model should stop being interpreted and list evidence that would be required before applying a balance like this to a real process. Do not invent operating conditions or safety advice.

## Author calculation key

The deficit satisfies `D′+kD=OUR₀e^(μt)`, `D(0)=0`, giving

\[
D(t)=\frac{OUR_0}{k+\mu}\left(e^{\mu t}-e^{-kt}\right)
=0.1\left(e^{0.2t}-e^{-0.8t}\right),\qquad C(t)=1-D(t).
\]

Its derivative is `D′(t)=0.1(0.2e^(0.2t)+0.8e^(−0.8t))>0`, so the threshold is crossed at most once. At the threshold, transfer capacity is `k(C*−Ccrit)=0.8×0.6=0.48`. Initially demand is `0.1`, leaving a positive margin of `0.38`. The quasi-steady equality `0.1e^(0.2t)=0.48` occurs at `t=ln(4.8)/0.2≈7.843`. The transient crossing solves `D(t)=0.6`; `D(8)≈0.495137`, `D(9)≈0.604890`, and bisection gives `t≈8.959`. At the quasi-steady equality time, the transient state is still `C≈0.520188`, above `0.4` because the state has not yet equilibrated. The solution is used only through the first threshold crossing; later negative `C` values would be mathematical extrapolation outside the intended range.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Balance | Defines the deficit with a consistent sign and obtains the correct linear ODE |
| Solution | Applies the integrating factor and verifies the initial condition |
| Capacity | Distinguishes threshold transfer capacity from instantaneous demand |
| Transient crossing | Shows monotonicity, brackets the root and reports a checked approximation |
| Limits | Separates the normalized model from real process or safety claims |

The rubric has no point weights or automatic prose grader. Workload, accessibility, mathematical accuracy and instructional design need qualified review. Do not activate this draft or describe it as a course assessment until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and normalized synthetic values, CC BY 4.0, developed with substantial AI assistance. No third-party dataset or real-world procedure is included.
