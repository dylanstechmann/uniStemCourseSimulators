# Filters, sampling, and anti-aliasing

An analog filter changes signal amplitude and phase as a function of frequency. Sampling then records values at discrete times. These steps solve different problems: a filter limits unwanted analog content before conversion, while a sampling rate determines which frequencies can be represented without overlap under ideal assumptions.

## First-order RC low-pass response

For a resistor $R$ followed by a capacitor $C$ to the return node, with output across the capacitor, the cutoff frequency is

$$
f_c=\frac{1}{2\pi RC}.
$$

The transfer magnitude at frequency $f$ is $|H(f)|=1/\sqrt{1+(f/f_c)^2}$. At cutoff, the amplitude is $1/\sqrt2\approx0.707$ of its low-frequency value, or about −3 dB. Above cutoff, a single pole eventually attenuates by about 20 dB per frequency decade. The cutoff is not a brick wall: components above it remain, and the phase also changes.

With $R=1$ kΩ and $C=10$ µF, $RC=0.01$ s and $f_c\approx15.9$ Hz. At 20 Hz, the amplitude ratio is $1/\sqrt{1+(20/15.9)^2}\approx0.622$. A requirement to preserve a signal band and suppress interference therefore needs both an allowed in-band change and a specified out-of-band attenuation; selecting a cutoff alone does not answer either question.

## Sampling and frequency folding

For an ideally band-limited signal whose highest frequency is $f_{max}$, uniform sampling requires $f_s>2f_{max}$ to reconstruct arbitrary phases without spectral overlap. The value $2f_{max}$ is a nominal Nyquist boundary, not a practical design target for a real signal and filter. At exactly the boundary, phase can be ambiguous: a 150 Hz sine sampled at 300 Hz at zero phase produces only zero-valued samples, while another phase produces a nonzero alternating sequence.

Frequencies separated by integer multiples of $f_s$ can produce the same sample sequence. For example, a 250 Hz cosine sampled at 300 samples/s has the same samples as a 50 Hz cosine. Once high-frequency content has folded into the sampled band, a later digital filter cannot distinguish it from a genuine in-band signal.

## Filter before conversion

An anti-alias filter acts in the analog path before the ADC. Its stop-band attenuation should reduce out-of-band components enough that their aliased contribution is acceptable relative to the signal and converter range. Because practical filters have a transition band, the sampling rate usually sits above twice the retained signal bandwidth, leaving room for the analog roll-off. A single RC pole may be insufficient when strong interference lies near the passband.

Sampling rate, analog bandwidth, ADC resolution, acquisition settling and clock timing must be considered together. More samples per second do not automatically improve analog bandwidth or remove noise. A sample-and-hold circuit may also need time to settle after a channel change. The preserved numeric item asks for the nominal $2f_{max}$ threshold; its key is unchanged, and it should not be read as a sufficient real acquisition specification.

The equations use idealized linear components and uniform timing. Component tolerance, loading, source impedance and converter behavior alter a real response. The examples specify no hardware or clinical measurement procedure.
