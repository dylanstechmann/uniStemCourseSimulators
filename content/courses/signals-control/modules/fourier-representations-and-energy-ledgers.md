# Fourier representations and energy ledgers

A sinusoidal frequency response describes one input component. A Fourier representation combines components to describe a complete signal and makes convolution, filtering and energy comparable in two domains. This original foundation uses explicit continuous and discrete conventions; their frequency variables and normalization factors differ. All signals are mathematical constructions, not measured instrument recordings.

## Fix the continuous convention

Define X(omega)=integral x(t)exp(−i omega t) dt over the real line. The inverse has factor one/(2pi), and omega is angular frequency per unit time. For square-integrable signals the energy identity is integral |x(t)|²dt=(one/2pi)integral |X(omega)|²domega. Changing the frequency convention to cycles per time changes the constants.

A worked rectangular pulse has height one on |t|<=one half and zero elsewhere. Direct integration gives X=2sin(omega/2)/omega, with limiting value one at omega=zero. Input energy is one. Its self-convolution is a triangle of height one on support [-1, 1], with energy two thirds. The transform of that convolution is X², not the transform of the pointwise square x².

## A distinct rectangle and its convolution

For the rehearsal take height one on |t|<=one. Its transform is

$$X(\omega)=2\sin\omega/\omega, \qquad X(0)=2.$$

The zero-frequency value equals the pulse area. At omega=pi/2 it is 4/pi, and its first positive zero is pi. The apparent zero-over-zero at the origin is a removable limit, not a zero spectral component. Point values at pulse boundaries do not change these integrals.

Convolving the pulse with itself counts the overlap of two intervals. The result is y(t)=2−|t| on |t|<=two, zero elsewhere. Peak is two and energy is sixteen/three. Its area is four, matching Y(0)=X(0)². Integrating the squared triangle independently checks energy without using a Fourier table.

Filtering in this setting multiplies transforms: Y=H X. Output energy is a frequency-weighted integral of |H|²|X|². Multiplying input energy by DC gain squared is generally incorrect when H varies over the occupied spectrum. A constant input/output gain and an entire frequency-dependent system are different objects.

## Discrete frequency is periodic

For a summable sequence define Xd(Omega)=sum x[n]exp(−i Omega n), where Omega is radians per sample. Replacing Omega with Omega+2pi gives the same transform because n is an integer. The inverse and energy identity integrate over any full interval of length 2pi:

$$\sum_n|x[n]|^2=\frac1{2\pi}\int_{-\pi}^{\pi}|X_d(\Omega)|^2d\Omega.$$

Physical angular frequency and normalized sample frequency are related by Omega=omega T, with the periodicity that produces aliases. That mapping does not make continuous and discrete transforms interchangeable without the sampling and reconstruction assumptions.

For h[n]=(one half)^n for n>=zero, zero otherwise, the geometric sum gives H=1/[1−(one half)exp(−i Omega)]. Absolute summability establishes a stable convolution operator here. DC gain is two and the value at Omega=pi is two thirds. At Omega=pi/2 the magnitude is two/sqrt5, obtained from the complex denominator rather than by inserting an analog corner frequency.

## Verify a finite input and infinite output tail

Let x[n] equal one at n=0, 1, 2 and zero elsewhere. Its causal output begins one, three halves, seven quarters, seven eighths. From n=3 onward it decays geometrically by one half. Thus y[2]=7/4 and y[3]=7/8.

The energy ledger includes the entire tail. The first three squared values sum to 101/16; the remaining geometric-square tail is 49/48. Total is 22/3. A truncated sequence that omits the tail would undercount energy even if its plot appears to have settled. Input energy is three, and neither DC gain squared times three nor a one-frequency magnitude gives this total output energy.

Compute the same result by integrating |H Xd|² over a full discrete frequency period, refining quadrature. Keep frequency-grid error separate from truncation of a time-domain tail. A finite numerical DFT also introduces its own length and periodic-extension conventions; it is not automatically the infinite-sequence transform.

## Interpretation and scope

Retain signal support, amplitude, transform convention, phase, convolution bounds and the energy denominator. Signed signals can have zero area and nonzero energy; a Fourier magnitude alone loses phase and need not determine the original signal. Modulation, general Fourier-series convergence and broad filter design remain outside these selected examples.

[MIT OCW 6.003 Fall 2011 calendar](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/pages/calendar/) lectures 14–20 provide link-only Fourier/continuous/discrete scope. All examples, integrals and tasks are original with substantial AI assistance; no source exercise, figure, code or data is imported. Numerical agreement checks the supplied signal models, not real acquisition performance or measured workload. The package remains partial and unreviewed.
