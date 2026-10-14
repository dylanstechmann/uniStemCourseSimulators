# Steady heat generation in a slab: inactive project draft

**Status:** authoring draft only. It is not scheduled, assigned, submitted, collected or graded. All dimensions and thermal values are synthetic teaching quantities, not vessel, tissue, equipment or process specifications.

## Purpose and model

Derive a one-dimensional steady temperature field with internal generation, then check its boundary flux, average and lumped-model limit. This thermal portfolio complements the oxygen-profile lab without reusing its diffusion-reaction data.

Consider a symmetric plane slab occupying `−L≤x≤L`, with `L=0.010 m`, uniform conductivity `k=0.50 W/(m·K)`, uniform generation `q'''=10,000 W/m³`, and both surfaces convecting to a fluid at `T∞=25 °C` with `h=20 W/(m²·K)`. Assume steady one-dimensional conduction, constant properties, symmetry at `x=0`, and no radiation or edge effects. On `0≤x≤L`, the model is

\[
k\frac{d^2T}{dx^2}+q'''=0,\qquad T'(0)=0,\qquad -kT'(L)=h[T(L)-T_\infty].
\]

## Work sequence

1. Integrate the equation twice and apply the center symmetry and surface convection conditions to derive `T(x)`.
2. Calculate the surface and center temperatures, then verify the surface heat flux against the internally generated heat per unit area.
3. Derive the half-slab average temperature. Independently use composite Simpson's rule at the five normalized positions `x/L=0, 0.25, 0.50, 0.75, 1.00` to check the average.
4. Compute `Bi=hL/k`. Compare the exact maximum and average temperatures with the uniform steady energy-balance estimate. Explain why the Biot screening check matters for the lumped approximation.
5. State which boundary conditions and omitted transport modes make this result unsuitable as a real thermal or biological design.

## Author calculation key

The solution on the half-slab is

\[
T(x)=T_\infty+\frac{q'''L}{h}+\frac{q'''}{2k}(L^2-x^2)=31-(x/L)^2\;°C.
\]

Thus the surface is `30 °C`, the center is `31 °C`, and the surface flux is `q'''L=100 W/m²`. Convection gives `h(T_s−T∞)=20×5=100 W/m²`, so the boundary and generation balance agree. The half-slab average is `T∞+q'''L/h+q'''L²/(3k)=30.666667 °C`. The Simpson check uses nodal temperatures `(31, 30.9375, 30.75, 30.4375, 30) °C` and gives the same average exactly because the profile is quadratic.

The Biot number is `Bi=hL/k=0.4`, above the common 0.1 screening rule. A uniform steady energy balance predicts `T∞+q'''L/h=30 °C`; it matches the surface but misses the internal gradient, giving an average error of `0.666667 °C` and a center error of `1 °C`. The Biot criterion is a model screen rather than universal proof of accuracy. The assumed conductivity, generation, geometry and convection coefficient are teaching values only.

## Proposed unweighted review rubric

| Criterion | Evidence for future human review |
|---|---|
| Boundary-value solution | Applies symmetry and convection conditions with consistent signs |
| Energy balance | Matches generated heat per area to the surface convective flux |
| Average check | Derives the average and verifies it by Simpson's rule |
| Model selection | Interprets Biot and the internal temperature gradient correctly |
| Limits | Avoids presenting the synthetic slab as a process or biological design |

The rubric has no point weights or automatic prose grader. Workload, accessibility, mathematical accuracy and instructional design need qualified review. This project remains inactive until those reviews and the course's missing homework, exams and laboratory sequence are addressed.

## Provenance

Original authoring and synthetic thermal values, CC BY 4.0, developed with substantial AI assistance. No third-party dataset or real-world procedure is included.
