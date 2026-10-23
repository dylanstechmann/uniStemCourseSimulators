# Assignment 4: sampled stability and implementation evidence

This open report joins an exact sampled scalar plant with a specified two-state PI timing contract. It compares a repeated stable pole, a strict stability boundary and an unstable gain variant before considering a separately defined saturated implementation. All values and signals are invented teaching inputs. Retain recurrence, derivations, code, plots and report locally; selected browser responses do not grade the full analysis or establish real-device performance.

## Part A: preserve the old-integrator contract

Use y[k+1]=a y[k]+b u[k], a=b=0.5 and T=one. Command u[k]=kp(r[k]−y[k])+ki z[k] and update z[k+1]=z[k]+T(r[k]−y[k]). Use kp=one, ki=one half. The command uses z[k], not the updated z[k+1].

For constant-reference deviations, the matrix has rows (0, 0.25), (-1, 1), trace one and determinant one quarter. Its characteristic is (lambda−one half)². A repeated pole strictly within the unit circle still decays, although this matrix can produce a polynomial sample-index factor multiplying the geometric decay.

Show the defective structure directly:subtract one-half identity and square the remaining matrix. Its nonzero first power and zero second power explain the polynomial factor. Do not confuse this stable repeated pole with a repeated pole at magnitude one, where polynomial growth can prevent decay.

## Part B: check the first samples and equilibrium

Start with y[0]=z[0]=zero and unit reference from k=zero. The contract gives y[1]=0.5, z[1]=one, then y[2]=0.75, z[2]=1.5. A third step gives y[3]=0.875. Derive these by the original update statements before comparing with a matrix implementation.

At steady state y=one and u=one, so z=two for the selected ki. Verify that substituting these values into both original equations preserves the state. A correct equilibrium alone does not prove that the initial trajectory reaches it; the strict pole conditions supply the linear decay argument.

Implement a deliberately different current-integrator command using z[k+1]. Calculate how its first output differs and derive its new matrix. A program that silently changes that order is not merely a different numerical approximation of the same recurrence; it implements a different controller.

## Part C: derive and test the gain boundary

For fixed kp=one, the selected second-order inequalities reduce to 0<ki<two. Derive them through trace/determinant and independently through the bilinear left-half-plane map. At ki=two the roots lie on the unit circle and fail strict asymptotic stability.

For a separate variant set ki=three. Trace remains one, determinant becomes 1.5 and the conjugate roots have real part one half, imaginary magnitude sqrt5/two and modulus sqrt1.5. This variant is unstable despite a stable open-loop plant and positive gains.

Compare direct recurrence with matrix powers for the stable, boundary and unstable cases under the same declared initial state. Plot enough samples to expose the modes without treating a short apparently bounded transient as proof of stability. Exact pole analysis and numerical trajectories answer complementary questions.

## Part D: a separate nonlinear implementation

Add a documented command clamp for an exploratory comparison. State whether the integrator continues accumulating, freezes under a condition, or follows a specific stored-output policy. Those are different nonlinear systems. The linear inequalities above do not automatically establish their global behavior or rule out persistent offset, oscillation or range violations.

Separate requested and delivered command in the plant update, and record the integrator state. A graph showing output alone can hide accumulation or a timing mismatch. If changing sample period, derive a and b again from the supplied continuous plant rather than changing T in only one equation.

Use the exact normalized hold factor to distinguish phase and amplitude changes, and keep computation delay as an additional model if introduced. A ten-samples-per-time-constant rule is a heuristic rather than the proof for this specified recurrence. Do not infer physical robustness, noise performance or implementation correctness from one nominal stable case.

As an implementation invariant, rescale the integrator coordinate by a known nonzero factor and transform the full state matrix consistently. The upper-right and lower-left entries change inversely, while trace, determinant and output trajectory remain unchanged. Changing only one coefficient after a state-unit conversion would define a different loop and can change its stability.

Retain the update contract, early samples, equilibrium, defective-pole calculation, strict inequalities, three trajectory comparisons and the separately defined clamp experiment. [MIT OCW 6.003 Fall 2011 calendar](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/calendar/) and selected [16.30 Fall 2010 digital-control scope](https://ocw.mit.edu/courses/16-30-feedback-control-systems-fall-2010/pages/lecture-notes/) are link-only references. All examples and tasks are original and AI-assisted; no source code, problem, figure or data is imported. General delayed/quantized/multirate design, physical validation, measured workload and qualified review remain open; the course stays partial and unreviewed.
