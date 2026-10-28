# Calculus III scope crosswalk

This crosswalk compares the local package, version 0.7.0, with two openly published undergraduate multivariable-calculus courses: MIT OpenCourseWare 18.02SC Multivariable Calculus, Fall 2010 ([syllabus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/pages/syllabus/), Units 1–4), and Harvard Math 21a Multivariable Calculus, taught by Oliver Knill in Summer 2003 ([syllabus and lecture plan](https://abel.math.harvard.edu/~knill/teaching/summer2003/syllabus.html)). It was compiled with AI assistance on 2026-10-28 from each comparator's public part, session and lecture titles and from the local readings and practice. It is an agent-run comparison, not a review by the owner or by a mathematics instructor. It does not compare lecture content, problem sets, exams or workload, and topic alignment establishes no equivalence, credit or endorsement.

Two format notes bear on the comparison. The Harvard offering is a seven-week summer course with 22 meetings, so its pace and depth are not those of a 14-week semester. For MIT, the syllabus page lists units and parts; session titles were read for Unit 1 Part C, Unit 3 Part A and Unit 4 Part A, and the other rows compare at part level. Status labels: **covered** means a local reading develops the topic with a worked example and practice; **shallow** means the topic appears only in passing or as a tool inside another topic; **absent** means no local instruction; **elsewhere** means another local course teaches it. Local numbers are lesson IDs (calculus-3-N), and each links to its reading.

## Comparator map

| Topic | MIT 18.02SC | Harvard 21a lectures | Local lessons | Status |
| --- | --- | --- | --- | --- |
| Vectors, dot and cross products, lines and planes | Unit 1 Part A; Part C sessions 15–16 (lines; line and plane) | 1–4 | [7](modules/07-vectors-planes-and-spatial-curves.md) | Covered |
| Matrices and systems of equations | Unit 1 Part B | — | — | Elsewhere: the Linear Algebra course |
| Functions of two variables, graphs and level curves | Unit 2 Part A | 5 ("functions, graphs, quadrics") | [1](modules/01-vectors-partial-derivatives-and-gradients.md), [5](modules/05-gradients-in-a-concentration-field.md) | Covered for graphs and level curves |
| Quadric surfaces | — | 5 | — | Shallow: a paraboloid appears only as a boundary shape in coursework 3; named only by Harvard |
| Parametric surfaces | — | 6 | — | Absent; named only by Harvard |
| Parametric curves, velocity, speed and traced length | Unit 1 Part C sessions 17–20 | 7–8 | [7](modules/07-vectors-planes-and-spatial-curves.md) | Covered |
| Acceleration, tangential and normal parts, curvature | Unit 1 Part C session 19 (acceleration) | 7–8 ("curves, velocity, acceleration"; "arclength, curvature") | [22](modules/22-acceleration-curvature-and-swept-area-of-space-curves.md) | Covered in 0.7.0; the earlier curves lesson stated that curvature was not developed |
| Kepler's second law and swept area | Unit 1 Part C session 21 | — | [22](modules/22-acceleration-curvature-and-swept-area-of-space-curves.md) | Covered in 0.7.0; named only by MIT |
| Cycloid and general parametric equations | Unit 1 Part C sessions 17–18 | — | [22](modules/22-acceleration-curvature-and-swept-area-of-space-curves.md) | Covered in 0.7.0 as a worked example; named only by MIT |
| Partial derivatives, tangent approximation and the chain rule | Unit 2 Parts A and B | 10 ("pde's, gradient, chain rule, tangents", the plan's wording for partial derivatives) | [1](modules/01-vectors-partial-derivatives-and-gradients.md), [8](modules/08-partial-derivatives-and-total-change.md), [14](modules/14-least-squares-and-constrained-partial-derivatives.md) | Covered |
| Gradient and directional derivatives | Unit 2 Part B | 10 | [1](modules/01-vectors-partial-derivatives-and-gradients.md), [5](modules/05-gradients-in-a-concentration-field.md) | Covered |
| Extrema and the second-derivative test | Unit 2 Part A | 11 | [2](modules/02-multivariable-optimization-and-constraints.md), [9](modules/09-hessians-constraints-and-boundary-optima.md) | Covered |
| Constrained extrema and Lagrange multipliers | Unit 2 Part C | 12 | [6](modules/06-constrained-optimization-and-polar-integrals.md), [9](modules/09-hessians-constraints-and-boundary-optima.md) | Covered |
| Double integrals, order of integration and polar coordinates | Unit 3 Part A sessions 47–50 | 13–14 | [3](modules/03-multiple-integrals-and-coordinate-transforms.md), [10](modules/10-multiple-integrals-and-jacobian-measures.md), [17](modules/singular-integrals-order-and-cutoff-evidence.md) | Covered |
| Applications: mass, average value and moment of inertia | Unit 3 Part A sessions 51–52 | — | [23](modules/23-mass-average-value-and-moments-of-inertia.md) | Covered in 0.7.0; previously absent; named only by MIT |
| Change of variables and the Jacobian | Unit 3 Part A sessions 53–55 | 14 (polar coordinates) | [3](modules/03-multiple-integrals-and-coordinate-transforms.md), [10](modules/10-multiple-integrals-and-jacobian-measures.md), [16](modules/nonlinear-jacobians-and-global-coverage.md) | Covered |
| Surface area | — | 15 | [12](modules/12-surface-flux-and-divergence.md) | Shallow: appears only as the conversion factor in the graph-flux element; named only by Harvard |
| Triple integrals in rectangular, cylindrical and spherical coordinates | Unit 4 Part A sessions 74 and 76–77 | 16 | [3](modules/03-multiple-integrals-and-coordinate-transforms.md), [10](modules/10-multiple-integrals-and-jacobian-measures.md) | Covered |
| Applications of triple integrals | Unit 4 Part A session 75 | — | [23](modules/23-mass-average-value-and-moments-of-inertia.md) | Covered in 0.7.0 by a solid with density varying along its axis |
| Gravitational attraction | Unit 4 Part A session 78 | — | — | Absent; named only by MIT |
| Vector fields, line integrals and path independence | Unit 3 Part B | 17 ("line integrals, fundamental thm of lineintegrals") | [4](modules/04-line-integrals-flux-and-integral-theorems.md), [11](modules/11-line-integrals-potentials-and-green.md) | Covered |
| Green's theorem | Unit 3 Part C | 19 | [11](modules/11-line-integrals-potentials-and-green.md) | Covered |
| Flux and the divergence theorem | Unit 4 Part B | 21 | [12](modules/12-surface-flux-and-divergence.md) | Covered |
| Stokes' theorem | Unit 4 Part C | 20 | [13](modules/13-stokes-theorem-and-spatial-balances.md) | Covered |
| Physics applications | Unit 4 "Physics Applications" | — | [lab](labs/01-boundary-flux-and-balance.md), [project guide](assignments/integrative-field-project-guide.md) | Shallow: one synthetic boundary-flux lab and an optional field project |
| Exams | Four exams and a final | Two midterms and a final | — | Absent by policy: all practice is formative-only |

## What 0.7.0 changed

The curves lesson had traced length and a helix but stated that curvature was out of scope, and nothing in the course differentiated a path twice. Both comparators teach acceleration along a curve, and Harvard teaches curvature, so a new week-2 reading follows the curves lesson. It splits acceleration into tangential and normal parts, derives curvature two ways, works an ellipse whose perimeter has no closed form, and uses r × v for Kepler's second law, with a cycloid as the worked example. The multiple-integrals block lacked any application of the integrals, although MIT gives separate sessions to mass, average value and moment of inertia, so a new week-9 reading covers mass, the center of mass, average value, moments of inertia in rectangular and polar coordinates, the parallel-axis theorem and a solid with variable density. Together they add six objectives, 26 practice items and eight retrieval cards.

## Remaining gaps

- Quadric surfaces, parametric surfaces and surface area as a topic, each named only by Harvard 21a.
- Gravitational attraction by a solid body, named only by MIT 18.02SC.
- Graded homework and exams, measured workload, and review by a qualified person.
