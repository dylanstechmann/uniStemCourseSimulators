# Integrative project draft: a bounded concentration and flux field

**Inactive authoring draft for Calculus III 0.4.7.** This proposal is not scheduled, submitted or graded. It has no point total, and the platform does not collect a project report. The field is a synthetic mathematical construction, not a biological measurement or engineering specification. Human mathematical review, workload measurement, accessibility review and activation decisions remain open.

## Project question

Analyze the amount and outward transport represented by a smooth two-dimensional field in a circular region. The project connects gradients and coordinate frames, constrained extrema, area measure, polar coordinates, boundary orientation and the divergence theorem. Its goal is to make each calculation agree with the model and geometry, then state what the construction cannot establish.

Use coordinates $x,y$ in metres and define the surface concentration

$$
c(x,y)=12\;\mathrm{amount/m^2}-(1\;\mathrm{amount/m^4})(x^2+y^2)
$$

on the disk $x^2+y^2\le 4\;\mathrm{m^2}$. Take the constant scalar diffusivity to be $D=0.5\;\mathrm{m^2/s}$ and define flux by $\mathbf J=-D\nabla c$. Coefficients carry the units needed for dimensional consistency. Every value is synthetic.

## Milestones and deliverables

1. **Model and frame:** state the coordinate frame, units, region and assumptions. Compute $\nabla c$, identify the constrained maximum and boundary minimum, and explain why a zero gradient alone does not establish an extremum.
2. **Total amount:** transform the disk integral to polar coordinates. State the Jacobian and bounds, integrate $c$ over the region, and report the units of the result.
3. **Boundary transfer:** parameterize the positively oriented circle, identify its outward unit normal, and integrate $\mathbf J\cdot\mathbf n$ around the boundary. Keep the orientation and sign explicit.
4. **Independent theorem check:** compute $\nabla\cdot\mathbf J$ and its area integral over the disk. Compare this result with the direct boundary integral, explain which smoothness and domain conditions are satisfied, and describe how changing $D$ to 0.75 m²/s changes the predicted transfer.
5. **Figure and interpretation:** provide a labelled contour/gradient/flux figure with a text alternative or data table. Distinguish a mathematical consequence of the chosen field from a measurement, mechanism or claim about real tissue.

## Reviewer-side construction check

The domain radius is 2 m and its area is $4\pi\;\mathrm{m^2}$. The field has its global maximum at the center and value 12 amount/m²; its boundary value is 8 amount/m². The polar integral of $c$ is $40\pi$ amount. The defined flux is $\mathbf J=(x,y)$ amount/(m·s), with divergence 2 amount/(m²·s); both the outward boundary integral and the divergence-area integral equal $8\pi$ amount/s. At $D=0.75\;\mathrm{m^2/s}$, the predicted transfer is $12\pi$ amount/s. These values are visible self-checks for an ungraded draft, not protected answers or evidence of learner performance.

## Draft human rubric

No weights, points, submission rules or performance cutoffs are assigned.

| Criterion | Strong evidence | Developing evidence | Little or no evidence |
| --- | --- | --- | --- |
| Model and units | Field, domain, coordinate frame, coefficients and dimensions are explicit and consistent. | Model is usable but has an unclear coefficient unit or assumption. | Region or units are missing or inconsistent. |
| Gradient and constrained extrema | Gradient and boundary behavior are correct; the global claim is justified over the stated disk. | Main calculations are present with a minor gap in boundary or classification reasoning. | A stationary point is treated as a global extremum without justification. |
| Coordinate measure | Polar bounds and Jacobian are correct, and the total amount has appropriate units. | Integral is mostly correct but has a bound, Jacobian or unit gap. | The area measure or domain is materially wrong. |
| Flux and theorem check | Direct oriented flux matches the divergence integral with signs and theorem conditions stated. | The comparison is attempted but orientation or a condition is unclear. | Flux sign, normal or theorem use is incorrect. |
| Sensitivity and interpretation | The diffusivity change is recomputed and conclusions stay within the synthetic model. | Sensitivity or limitations are described incompletely. | The model is presented as an empirical or biological result. |
| Figure and communication | Axes, units, arrows and text alternative make the geometry interpretable. | The figure is readable but omits a key label or alternative. | The graphic obscures orientation or has no interpretable scale. |
| Reproducibility | Steps, formulas and numerical checks are clear enough for another learner to reproduce. | A small implementation detail is missing. | The calculations cannot be independently followed. |

Before activation, a qualified reviewer must check the calculus, sign conventions, rubric, accessible figure alternatives and realistic workload. A course owner would also need to set collaboration, submission and feedback policies. This project draft is not part of the course manifest's assessment schedule and creates no grade.
