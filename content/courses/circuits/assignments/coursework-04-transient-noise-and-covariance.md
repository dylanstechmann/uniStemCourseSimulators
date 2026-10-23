# Assignment 4: transient, noise and covariance evidence

This open mixed report connects existing filter loading, noise bandwidth, covariance and calibration ideas with a second-order response and a conditional noise-combination problem. It asks which model justifies multiplying transfer functions, integrating a spectrum or choosing a subtraction weight. All parameters and random-source assumptions are invented mathematical inputs, not measured instrument performance. Retain calculations, code and report locally; checkpoints assess selected outputs rather than the complete evidence argument.

## Part A: two explicitly buffered stages

Take two identical first-order RC stages with ideal buffers, each time constant $\tau=0.002$ s. Their combined transfer is $H(s)=(1+s\tau)^{-2}$ with DC gain one. State why the buffers matter: an unbuffered passive ladder has loading and does not generally equal the product of two isolated first-order transfers.

Derive the unit-step response $y(t)=1-(1+t/\tau)e^{-t/\tau}$. At t=0.004 s it is $1-3e^{-2}\approx0.59399415$. Verify initial state and derivative, final value and the original two-state equations. Compare this repeated-pole response with a single stage of the same tau; they have different transients even when their DC gains agree.

Use an independent two-state integration and refine the step. Compare trajectory error with a numerical root or event-location error if you estimate a threshold time. A good final-value match does not verify the intermediate waveform or its initial derivatives.

## Part B: one-sided noise bandwidth

Stipulate input white amplitude spectral density 40 nV per square-root Hz, flat over the entire mathematical integration range. Use a one-sided PSD convention. The squared transfer magnitude is $[1+(f/f_c)^2]^{-2}$ with $f_c=1/(2\pi\tau)$, so

$$B_{eq}=f_c\int_0^\infty\frac{dx}{(1+x^2)^2}=\frac{\pi f_c}{4}=\frac1{8\tau}=62.5\ \mathrm{Hz}.$$

Derive the integral with a trigonometric substitution or another justified method. This bandwidth differs from both the single-stage $\pi f_c/2$ and a brick-wall cutoff approximation. The output RMS is $40\sqrt{62.5}\approx316.227766$ nV under the stipulated input and unit DC transfer.

Keep amplitude density, power density, variance and RMS units separate. A two-sided PSD convention would require corresponding normalization; mixing conventions creates a factor-of-two error. Actual spectra, additional stages and nonwhite components are not established by this infinite-band mathematical example. A single datasheet density value would not prove the flat-input assumption.

## Part C: shared and independent channel terms

For a separate normalized observation model write $X=S+N_c+N_1$ and $Y=N_c+N_2$. The three noise terms are zero-mean and mutually independent, with RMS values 5, 3 and 4 microvolts respectively. S is retained signal only in X. Then Var(X)=34, Var(Y)=41 and Cov(X,Y)=25 in squared microvolts.

For X−Y, shared noise cancels and the variance is 25, giving RMS 5 microvolts. Treating the two channels as independent would instead give $\sqrt{75}\approx8.66025404$ microvolts. Explain which independence statements were stipulated: independence of the underlying three sources does not imply independence of the two channels sharing one source.

## Part D: common cancellation and minimum variance differ

For X−gY, the variance is $34+41g^2-50g$. Complete the square or differentiate to find the conditional minimum at $g=25/41\approx0.60975610$, with RMS $\sqrt{769/41}\approx4.33083105$ microvolts. At g=1 common noise cancels exactly, but the independent noise in Y makes that weight different from the minimum-variance choice.

The optimum preserves S in this declared model because S appears only in X. A different signal mapping or gain uncertainty would change the problem. State those assumptions before interpreting the weight as an improved estimate. Simultaneous recording alone does not establish the covariance model, and constructed numerical values do not validate a real cancellation scheme.

Compare empirical variances from an optional explicitly labeled simulation with the analytic formulas. Report the random generator, number of draws and Monte Carlo uncertainty. Do not describe that simulation as measured circuit noise or physical experimental replication.

A covariance table must itself be consistent: its matrix should be positive semidefinite. Here the determinant is 34 times 41 minus 25 squared, or 769, which is positive. Completing the square gives variance 41(g−25/41)²+769/41. If an estimated table instead implied a negative minimum variance, investigate its uncertainty or consistency rather than interpreting that output as physical negative noise.

## Self-review and scope

Retain the buffer/topology condition, step and two-state comparison, one-sided bandwidth derivation, covariance ledger, quadratic optimum and unresolved measurement assumptions. The existing [NIST combined-standard-uncertainty guidance](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-5-combined-standard-uncertainty) is link-only support for covariance/sensitivity concepts; the filter and channel examples are original. [MIT OCW 6.002 Spring 2007 calendar](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/pages/calendar/) provides circuit/filter scope. No source table, example or code is imported. Content is AI-assisted, partial and unreviewed; real spectra, equipment validity, measured workload and qualified review remain open.
