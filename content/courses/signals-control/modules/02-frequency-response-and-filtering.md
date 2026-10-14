# Frequency response and filtering

## Learning objectives

1. Calculate the magnitude and phase response of a first-order low-pass system at a stated sinusoidal frequency, including its cutoff frequency.
2. Explain why filtering must precede sampling when a signal contains frequencies above the Nyquist limit, and calculate a simple alias.

## Ask how the model responds at one frequency

An input signal can contain slow trends, periodic components and faster fluctuations at the same time. A stable linear time-invariant system treats a sinusoid especially simply: after any transient has decayed, a sinusoidal input at frequency **f** produces a sinusoidal output at the same frequency, with a changed amplitude and phase. The frequency response describes those two changes as the input frequency varies. It is the complex transfer function evaluated on the imaginary axis, **G(jω)**, where **ω = 2πf** is angular frequency in radians per second.

The magnitude **|G(jω)|** is the output-to-input amplitude ratio for the sinusoid. The argument or phase **∠G(jω)** is the output phase relative to the input. If the gain magnitude is 0.5, a 2-unit sinusoidal amplitude becomes 1 unit at steady state. A negative phase means the output lags the input under the usual sinusoidal convention. The [MIT OpenCourseWare frequency-response lecture](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-9-frequency-response/) develops this representation. Frequency response is a steady-state description: an abrupt start or a changing signal can also produce transients that are not summarized by one amplitude ratio at one frequency.

The qualification “stable LTI” matters. A nonlinear clipper can create new frequencies instead of merely changing the gain and phase of one sinusoid. A time-varying process may respond differently at different times. An unstable model may not settle to a bounded sinusoidal steady state. For a real measurement, the transfer function should represent the system between the chosen input and output points, including the components that lie inside that boundary.

## Work through a first-order low-pass filter

For a unity-gain first-order low-pass system with time constant **τ > 0**,

**G(s) = 1/(τs + 1).**

To find its sinusoidal steady-state response, set **s = jω**:

**G(jω) = 1/(1 + jωτ).**

The magnitude is **|G(jω)| = 1/√(1 + (ωτ)²)** and the phase is **−tan⁻¹(ωτ)**. Both depend on the dimensionless product **ωτ**. Since **ω** has units of inverse seconds and **τ** has units of seconds, the product has no units. At very low frequency, **ωτ ≪ 1**, the magnitude is close to one and phase is near zero. At much higher frequency, the magnitude decreases and phase approaches −90°; fast variations are attenuated and lagged by this model.

The conventional cutoff of this first-order low-pass occurs at **ωc = 1/τ**, or **fc = 1/(2πτ)** in hertz. Substitution gives a magnitude of **1/√2 ≈ 0.707** of the passband amplitude and phase of **−45°**. The amplitude level is about −3.01 dB because **20 log₁₀(1/√2) ≈ −3.01 dB**. “Cutoff” here names a standard point for this response; other filter families and applications can define their useful band using a different criterion.

For **τ = 0.05 s**, the cutoff is **fc = 1/(2π × 0.05 s) ≈ 3.18 Hz**. The same model with **τ = 0.10 s** has a cutoff near **1.59 Hz**. Doubling the time constant halves the cutoff, so the slower filter begins attenuating at a lower frequency. This inverse relation is easy to reverse accidentally: a larger time constant does not give a higher cutoff. The preserved week-4 practice item asks for the first calculation, and its keyed value is 3.18 Hz.

At a frequency well below the cutoff, the response is close to the static gain of one. At the cutoff the output amplitude is about 70.7% of the input amplitude. At one decade above cutoff, **ωτ = 10**, so the magnitude is about **1/√101 ≈ 0.0995**, roughly one tenth, and the phase is about −84.3°. These checks make the direction of the effect explicit. They are calculations for this ideal model, not measured performance values for a particular sensor.

## Gain and phase describe different costs

Filtering changes more than amplitude. A low-pass filter can reduce a fast disturbance, but it also introduces phase lag. In an isolated measurement, a delay may shift the time at which a feature appears. Inside a feedback loop, that phase shift may reduce stability margin around the frequency where the loop gain is near one. The later Bode-plot and feedback-case lessons calculate those loop effects; this reading uses the filter's single-system response and does not specify any controller tuning.

The filter time constant should therefore be related to the frequencies that matter to the measurement. A physiological trend may occupy a low-frequency band while electrical interference lies higher, but no universal cutoff follows from those labels alone. A useful design statement names the passband that should be retained, the unwanted band to attenuate, the acceptable amplitude error and phase delay, and the system boundary being measured. Instrument noise, sensor dynamics and downstream feedback can all change the decision.

## Sampling creates aliases

A digital sampler records values at discrete instants separated by the sampling period **Ts**. Its sampling frequency is **fs = 1/Ts**. A sinusoid above the Nyquist frequency **fs/2** can produce the same sample sequence as a lower-frequency sinusoid. That ambiguity is aliasing: once samples have been recorded, the data alone generally cannot tell which of the compatible continuous frequencies was present.

For a real sinusoid, a simple fold calculation maps a frequency into the interval from zero to **fs/2**. For the preserved example, a **120 Hz** interference tone is sampled at **fs = 200 Hz**, so the Nyquist frequency is **100 Hz**. The tone lies above it and folds to **|120 − 200| = 80 Hz**. The sampled record therefore contains a component at 80 Hz, which is indistinguishable from a genuine 80 Hz input under this sampling setup. The alias question's answer is 80 Hz.

An anti-alias filter must act on the analog signal before the sampler. A digital filter applied after conversion can attenuate the recorded 80 Hz component, but it cannot determine whether that component came from a genuine 80 Hz signal or an aliased 120 Hz signal. The [MIT OpenCourseWare sampling lecture](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/resources/lecture-21-sampling/) discusses sampling and anti-alias filtering. Ideal bandlimited signals can be reconstructed when the sampling conditions are met; practical measurements need margin for finite filter roll-off, noise and frequency content beyond the nominal band edge.

The Nyquist condition is not a recommendation to set the sample rate at exactly twice the highest expected component and assume the hardware is safe. A real anti-alias filter needs a transition band between frequencies to retain and frequencies to suppress, and components above Nyquist must be attenuated before sampling to an acceptable level. The required suppression depends on signal amplitudes, measurement error and the later analysis. This lesson explains the mechanism and the preserved arithmetic; it does not prescribe acquisition settings for a real instrument.

## Connect the model to a measured signal

Frequency-response calculations assume a model, while recorded data include sensor noise, offsets, quantization and finite duration. An observed spectral component may be a true process oscillation, a sensor artifact, a sampled alias or a combination. The transfer function, sampling rate and pre-sampling filter all influence what remains distinguishable. A model that attenuates frequencies can clarify a signal, but lost information cannot be recreated just by smoothing the sampled record.

For a first-order low-pass, verify **τ** is in seconds before using **fc = 1/(2πτ)**, report frequency in hertz, and check that increasing **τ** lowers **fc**. For aliasing, compare the tone with **fs/2**, state that the filter must precede sampling, and compute the folded frequency in the allowed range. These checks preserve the distinction between a continuous-time response model and a discrete measurement. Later units examine Bode plots, detailed sampling rules, implementation phase costs and the consequences of adding a sensor filter inside a loop.
