# Electrodes, impedance, and measurement

## Learning objectives

By the end of this reading, you should be able to:

1. Calculate voltage-divider loading from a sensor's source resistance and a measurement input resistance in a stated model.
2. Explain how electrode-interface potentials and impedance can alter a recorded trace, and qualify what a trace alone can establish.

## A measurement is a connected system

A voltmeter or amplifier does not read a biological source in isolation. A useful first model is a source voltage (V_s), a source resistance (R_s), and an instrument input resistance (R_{in}). The input and source resistances form a divider, so the measured voltage is

\[
V_{in}=V_s\frac{R_{in}}{R_s+R_{in}}.
\]

This expression assumes a resistance-dominated source and input over the condition being modeled. The current drawn from the source is (I=V_s/(R_s+R_{in})). If (R_{in}) is much larger than (R_s), the input voltage is close to the source voltage. If the two resistances are similar, the instrument changes the quantity it is trying to measure.

For the preserved practice calculation, (R_s=1\,\text{M}\Omega) and (R_{in}=9\,\text{M}\Omega). The fraction delivered to the input is (9/(1+9)=0.90), so a 1 V source would produce 0.90 V at the input in this model. With equal 1 MΩ resistances, the fraction is 0.50. If the input is 100 times the source resistance, the fraction is (100/101\approx0.9901), about one percent below the source. These are ratios, not universal instrument specifications.

A high input resistance can reduce resistive loading, but it does not make every measurement ideal. Input bias current can create a voltage drop across source resistance. Cable and amplifier input capacitance can lower input impedance at higher frequencies. Leakage, noise, finite common-mode rejection, and gain range can also matter. Calibration can correct a known reporting scale, but it cannot restore signal content removed or altered by the electrical connection.

For sinusoidal signals, the source and input are more generally described by complex impedances. The transfer depends on both their magnitudes and phases, and the input capacitance can make the divider frequency dependent. We use the simple resistance divider here to interpret the preserved item; the following phasor lesson develops complex transfer, phase, and RMS power. Do not apply the 0.90 result to every frequency or every electrode.

## What an electrode contributes

Biological tissue carries ionic current, while the metal lead and amplifier use electronic current. The electrode–electrolyte boundary is part of that conversion. A simplified measurement model may include a half-cell potential, solution resistance, and an interface with capacitive and charge-transfer behavior. A skin-contact electrode adds the skin and contact region, so a single resistor or capacitor cannot represent every electrode, material, frequency, contact condition, or current density.

The half-cell potential is an interface voltage, not the tissue signal. In a two-electrode measurement, the amplifier responds to the difference between its two input-side potentials. Equal interface offsets would cancel in an ideal matched measurement. Real interfaces are not identical, so differences can leave a DC offset or a slowly changing baseline on top of the desired tissue voltage. The instrument can also distort a source when finite input impedance draws current through the electrode and tissue impedances.

In a restricted small-signal model, an interface is sometimes represented by a double-layer capacitance (C_{dl}) in parallel with a charge-transfer resistance (R_{ct}), together with solution and contact resistance. This is a teaching approximation. Some interfaces need distributed or frequency-dependent elements; fitted circuit values depend on the measurement conditions and model choice. Treat the circuit as a way to ask what could affect a trace, not as a unique microscopic description of a particular person or electrode.

The capacitive branch helps explain why impedance depends on frequency. For an ideal capacitor, the magnitude of capacitive reactance is

\[
X_C=\frac{1}{2\pi f C}.
\]

For example, a 1 μF capacitor has (X_C\approx15.9\,\text{k}\Omega) at 10 Hz and (X_C\approx1.59\,\text{k}\Omega) at 100 Hz. The magnitude falls as frequency rises. An actual electrode interface also includes resistance, electrochemical processes, geometry, and the skin; this capacitor calculation illustrates one mechanism and is not a fitted electrode model. The important measurement consequence is that an interface that barely loads one signal band may attenuate or reshape another.

## Differential measurement and mismatch

Many biopotential systems compare two electrodes and amplify their voltage difference. A voltage shared by both inputs is common mode; the wanted difference is differential. An ideal differential amplifier rejects the common-mode part. Real amplifiers have finite common-mode rejection, and unequal electrode impedances can turn some shared interference into a differential error. Matching the two signal paths therefore affects rejection, while large electrode or contact impedance can increase noise and loading sensitivity.

Keep the sources separate in a diagram: tissue potential, each electrode's half-cell contribution, each interface impedance, any shared interference, and the amplifier input. Then identify which components are differential and which are shared. A stable amplifier gain does not guarantee a stable tissue signal, and a changed trace does not by itself reveal which part of this chain changed.

## Interpreting a drifting baseline

The preserved scenario describes a slow baseline shift after an electrode is attached. The shift decays over minutes and does not follow the subject's activity. Within that simplified choice question, electrode half-cell polarization and interface settling are the best-supported explanation. The useful reasoning is the time and context: the trace changes after contact is made, then relaxes without tracking the stated activity.

That pattern is not a diagnostic rule. In an actual recording, movement of the electrode or cable, changing contact pressure or hydration, temperature, amplifier offset or saturation, and signal-processing choices can also alter the baseline. Some real physiological signals are slow, so filtering away low frequencies can remove information as well as drift. Distinguishing these explanations requires controlled observations and knowledge of the instrument; the voltage trace alone does not prove that the tissue is unchanged.

The second preserved question asks for the most likely origin from a deliberately limited set of choices. Its keyed interface explanation is the intended inference for that scenario, not a claim that activity-independent drift always has one cause. A stronger real-world analysis would compare channels and reference measurements, check amplifier range and coupling, examine whether the effect follows contact or motion, and document the measurement conditions. Those are reasoning categories, not a protocol for attaching electrodes or delivering current.

## Common checks

- Use (R_{in}/(R_s+R_{in})) only when the stated model treats source and input as resistances.
- Keep electrode half-cell potential distinct from tissue potential.
- Remember that a differential channel rejects only the common-mode signal that reaches both inputs equally, and only to the extent allowed by the amplifier.
- Treat a simple interface circuit as an approximation with a declared frequency and operating range.
- Describe slow baseline movement as evidence consistent with an interface effect, not proof of its cause.
- Do not infer a safe stimulation current or electrode procedure from this recording model.

## Further study

For the basic frequency dependence of capacitive reactance, see OpenStax University Physics Volume 2, [15.2 Simple AC Circuits](https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits). Geddes reviews how electrode–electrolyte circuit models developed and why their resistive and capacitive behavior depends on operating conditions: [Historical evolution of circuit models for the electrode-electrolyte interface](https://pubmed.ncbi.nlm.nih.gov/9124725/). These are link-only references. This lesson uses original wording and calculations and imports no source prose, figures, examples, problems, or datasets.
