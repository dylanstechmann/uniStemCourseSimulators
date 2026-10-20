# Differential Equations course review handoff

This handoff targets Differential Equations for Living & Engineered Systems, package version 0.5.0. The [review snapshot](DIFFERENTIAL_EQUATIONS_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the proposed 14-week sequence, prerequisites, outcome/objective associations and mathematical level.
- Recalculate representative keys for first- and second-order equations, Fourier harmonic coefficients and response, coupled systems, equilibria, stability, logistic fits, numerical methods and the existing scalar-decay lab.
- Independently verify the new coupled system's exact solution, eigenvalues, peak time, explicit-Euler stability and positivity conditions, and backward-Euler recurrence.
- Compare the week-6 impulse-response, convolution and transfer-function reading with MIT OCW 18.03SC Unit III; recalculate the impulse responses and velocity jump, the convolution results, pole-based stability, gain, phase lag and peak-gain frequency, and confirm the delta function is presented through its sifting property only.
- Check the signs in the forward/backward updates and compare both numerical results with the exact state at the stated time.
- Check the week-12 project guide and its rehearsal: the restated system and tasks against the draft, the worked example on a separate system, the rehearsal's solution, peak and Euler keys, and the wording of the five milestone self-checks. Confirm that the guide and rehearsal do not reveal the project's own results, and that the fitting lab's dataset link now resolves to the package-pinned CSV.
- Confirm that normalized states and rates are explicitly synthetic, and assess accessible notation, likely workload and appropriate learner preparation.

## Author-side evidence and its limits

For version 0.3.7, the focused Differential Equations suite passed 7 tests, including direct recomputation of the inactive project's exact and numerical values. For 0.5.0 a dedicated test recomputes the rehearsal keys with exact rational Euler iterates and a fine RK4 integration of the system, rather than the closed forms used to author them, recomputes the guide's worked example, and checks that the guide and rehearsal do not state the project's results. That earlier suite does not cover the Laplace lesson, schedule correction or 0.4.0 Fourier addition; no test suite was run for versions 0.3.8–0.4.0. For 0.4.1 a new recalculation file recomputes the eight new numeric keys. Impulse responses come from RK4 integration after the velocity jump, convolutions from Simpson quadrature, and gains and phase lags from a real 2×2 solve for the particular-solution coefficients instead of |p(iω)|. A short finite pulse checks the impulse velocity jump. A further test checks the values stated in the reading. The full-suite result is in the validation report. Content validation and objective/candidate reports are recorded in the current validation report. Author-side checks do not establish independent mathematical review, accessibility, learner outcomes, semester workload or university equivalency. The draft is inactive and ungraded; graded homework, exams and a laboratory sequence remain absent.

## Review record to complete only after review

After a review actually occurs, record reviewer name and qualifications, date, package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for mathematical correctness, instructional design, assessment, accessibility, workload and release. Do not infer approval from the package hash or test results.
