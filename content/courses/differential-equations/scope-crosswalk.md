# Differential Equations scope crosswalk

This crosswalk compares the local package, version 0.7.0, with two openly published undergraduate courses: MIT OpenCourseWare 18.03SC Differential Equations, Fall 2011 ([syllabus](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/syllabus/syllabus/), Units I–IV), and Harvard Math 21b Linear Algebra and Differential Equations, taught by Oliver Knill in Spring 2015 ([syllabus](https://people.math.harvard.edu/archive/21b_spring_15/syllabus.html)). It was compiled with AI assistance on 2026-10-27 from each comparator's public session and lecture titles and from the local readings and practice. It is an agent-run comparison, not a review by the owner or by a mathematics instructor. It does not compare lecture content, problem sets, exams or workload, and topic alignment establishes no equivalence, credit or endorsement.

Math 21b spends its first 24 lectures on linear algebra, which belongs to the local Linear Algebra course, so only its differential-equation lectures (25–33) bear on this package. Status labels: **covered** means a local reading develops the topic with a worked example and practice; **shallow** means the topic appears only in passing; **absent** means no local instruction; **elsewhere** means another local course teaches it. Local numbers are lesson IDs (differential-equations-N), and each links to its reading.

## Comparator map

| Topic | MIT 18.03SC sessions | Harvard 21b lectures | Local lessons | Status |
| --- | --- | --- | --- | --- |
| First-order models, geometric and numerical methods | I: Basic DE's, Geometric Methods, Numerical Methods | — | [1](modules/01-first-order-models-and-time-constants.md), [3](modules/03-coupled-systems-equilibria-and-stability.md), [4](modules/04-numerical-odes-and-error-control.md), [5](modules/05-well-mixed-chamber-and-euler-stability.md) | Covered |
| Linear first-order equations and integrating factors | I: Linear ODE's, Integrating Factors | — | [7](modules/07-forced-first-order-systems-in-a-perfused-chamber.md), [16](modules/initial-value-problems-and-variable-coefficients.md) | Covered |
| Complex arithmetic and sinusoidal functions | I: Complex Arithmetic, Sinusoidal Functions | — | [23](modules/23-forced-linear-equations-exponential-response-and-undetermined-coefficients.md) | Covered in 0.7.0; previously complex roots were written without Euler's formula |
| Autonomous equations, equilibria and stability | I: Autonomous Equations, Linear vs. Nonlinear | — | [6](modules/06-equilibria-stability-and-coupled-compartments.md), [10](modules/10-logistic-growth-solution-fitting-and-extrapolation.md) | Covered |
| Characteristic equation and damped oscillators | II: Characteristic Equation, Damped Oscillators | — | [2](modules/02-second-order-systems-and-mechanical-response.md), [8](modules/08-resonance-and-damping-of-a-spring-mass-damper.md) | Covered |
| Exponential response, undetermined coefficients, operators and pure resonance | II: Exponential Response, Undetermined Coefficients, Linear Operators, Pure Resonance | 29 | [23](modules/23-forced-linear-equations-exponential-response-and-undetermined-coefficients.md) | Covered in 0.7.0; previously the steady amplitude was stated without a method |
| Gain, phase lag and frequency response | II: Gain and Phase Lag, Frequency Response | — | [7](modules/07-forced-first-order-systems-in-a-perfused-chamber.md), [8](modules/08-resonance-and-damping-of-a-spring-mass-damper.md), [23](modules/23-forced-linear-equations-exponential-response-and-undetermined-coefficients.md) | Covered |
| Fourier series and periodic input | III: Fourier Series: Basics, Operations, Periodic Input | 30–31 | [17](modules/fourier-filtering-and-error-bounds.md) | Covered for periodic forcing; Parseval's identity is not developed |
| Step and delta functions, impulse response and convolution | III: Step and Delta, Impulse Response, Convolution | — | [15](modules/15-impulse-response-convolution-and-transfer-functions.md) | Covered |
| Laplace transform, partial fractions, transfer functions and poles | III: Laplace Transform, Partial Fractions, Solving IVP's, Transfer Functions, Poles | — | [14](modules/14-laplace-transform-initial-value-problems.md), [15](modules/15-impulse-response-convolution-and-transfer-functions.md) | Covered |
| Linear systems, matrix methods and phase portraits | IV: Linear Systems, Matrix Methods, Phase Portraits | 25–26 (titled "differential equations I" and "II") | [3](modules/03-coupled-systems-equilibria-and-stability.md), [9](modules/09-phase-portraits-of-linear-systems.md) | Covered |
| Matrix exponentials | IV: Matrix Exponentials | — | — | Elsewhere: the Linear Algebra course's matrix-exponential lesson |
| Nonlinear systems, linearization and limit cycles | IV: Nonlinear Systems, Linearization, Limit Cycles and Chaos | 27 | [11](modules/11-linearization-and-bistability-in-a-toggle-switch.md), [18](modules/nonlinear-radius-and-limit-cycles.md) | Covered; chaos is not developed |
| Stiff equations and implicit methods | — | — | [12](modules/12-stiff-equations-and-implicit-methods.md) | Local extension |
| Linear transformations on function spaces | — | 28 | — | Elsewhere: a linear-algebra viewpoint |
| Partial differential equations (heat and wave) | — | 32–33 | — | Absent; named only by Harvard 21b |
| Exams | Exams 1–3 and a final | Two midterms and a final | — | Absent by policy: all practice is formative-only |

## What 0.7.0 changed

Both comparators teach a general method for forced linear equations, and the package stated forced responses without one. The new week-4 reading follows the characteristic-equation lesson and precedes the resonance lesson, as 18.03SC orders these sessions. It introduces Euler's formula and complex magnitude and angle, the exponential response formula, complex replacement, undetermined coefficients, superposition, the resonant cases with an extra factor of t, and the split into steady state and transient. It derives the amplitude formula the resonance lesson states and reproduces that lesson's 20.83 mm value.

## Remaining gaps

- Partial differential equations by separation of variables and Fourier series, named only by Harvard 21b.
- Parseval's identity and chaos, each named by one comparator's titles.
- Graded homework and exams, measured workload, and review by a qualified person.
