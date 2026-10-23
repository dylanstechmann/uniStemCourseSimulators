# Assignment 1: transform and energy evidence

This open report connects signed time signals, complex Fourier phase, convolution and complete energy ledgers in continuous and discrete time. All inputs are mathematical constructions. Retain derivations, code, plots and report locally; selected browser fields do not grade the complete transform argument or implementation. State conventions before calculating, because a normalization mismatch can preserve a plausible shape while changing every energy value.

## Part A: a causal signed pulse

Let x(t)=one on [0, 1], minus one on [1, 2], zero elsewhere, with consistent normalized time and amplitude units. Individual endpoint values do not affect the integrals. Its area is zero while its energy is two. Explain why cancellation in the area does not imply absence of a signal or zero energy.

Integrate each interval separately under X(omega)=integral x(t)exp(−i omega t)dt. Combining the terms gives X=(1−exp(−i omega))²/(i omega), with its zero-frequency value supplied by a limit. At omega=pi the transform is -4i/pi and its magnitude is 4/pi. A magnitude-only plot hides this phase information.

Compare a direct numerical time integral with the complex formula at several frequencies, including a small nonzero frequency near the removable limit. Document a numerically stable evaluation or a limiting rule rather than dividing zero by zero. Keep angular frequency distinct from cycles per unit time.

## Part B: convolve the signed signal

Derive y=x*x by interval overlap or by expressing x as a rectangular pulse minus its unit-shifted copy. The resulting pieces are t on [0, 1], 4−3t on [1, 2], 3t−8 on [2, 3], and 4−t on [3, 4], with zero elsewhere.

Check continuity where the pieces meet and compare selected values with direct convolution integration. Its energy is eight/three. Derive that from the four squared linear pieces; taking an absolute overlap length everywhere would lose the negative middle response and give a different convolution.

Verify Y=X² at omega=pi, where its real value is -16/pi². A negative real transform value is not a negative signal energy. Parseval uses the squared magnitude with its one/(2pi)factor, not the raw transform or its real part.

Compare time-domain energy with a frequency integral using a documented cutoff or transformation and a numerical error budget. If truncating the frequency axis, derive a tail bound from the transform's large-frequency envelope. Refinement of quadrature panels does not remove a fixed omitted tail. An energy agreement should state both error contributions.

## Part C: a separate discrete sequence

Use causal impulse response h[n]=(one third)^n for n>=zero and input x[n]=delta[n]−delta[n−1]. Its output is one at n=zero and -(two thirds)(one third)^(n−1) afterward. Thus y[1]=-2/3 and the complete output energy is three halves.

Derive that energy from the geometric tail. Independently integrate |Yd(Omega)|² over a full discrete frequency period using H=1/[1−(one third)exp(−i Omega)] and Xd=1−exp(−i Omega). At Omega=pi/2 the output transform is 1.2+0.6i and magnitude three/sqrt5.

The input's DC component is zero even though H has nonzero DC gain. Explain why the output therefore has zero DC component without zero energy. Replacing every frequency by the DC gain would answer neither the finite sample nor complete energy question.

As an additional phase check, shift the continuous input by a declared time offset. Its transform acquires a complex phase factor without changing input energy. The self-convolution shifts by twice that offset. Verify both statements using the original interval definitions, not only a transform table; they distinguish phase conventions that a magnitude-only comparison would miss.

## Part D: implementation and interpretation

Implement direct finite convolution and compare its early output with the analytic expressions. For the infinite discrete tail, report how much energy remains after a chosen last index. If using a finite DFT, document its length, zero padding and periodic-extension convention and distinguish circular from linear convolution.

Label every plot with time or sample index, amplitude or magnitude, frequency convention and support. Include a text description of the signed middle convolution and the complex phase comparison. A high-resolution image cannot establish the normalization or support assumptions by itself.

Retain original integrals, interval bounds, piecewise convolution, geometric sums and independent numerical checks. [MIT OCW 6.003 Fall 2011 calendar](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/calendar/) lectures 14–20 provide link-only transform scope. All examples and tasks are original and AI-assisted; no source signal, problem, code, figure or dataset is imported. General Fourier convergence, modulation, real acquisition performance, measured workload and qualified review remain open; the course stays partial and unreviewed.
