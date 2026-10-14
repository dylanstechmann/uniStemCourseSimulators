# Operational amplifiers and analog front ends

An operational amplifier (op amp) can amplify, buffer or combine sensor signals. Analyze the feedback network first, then check whether the real device can meet its input, output, bandwidth and noise requirements. The ideal equations are a useful starting model, not a datasheet or proof that a physical stage operates as intended.

## Negative feedback and closed-loop gain

For an ideal op amp in a stable negative-feedback configuration, input current is approximately zero and the input terminals sit at nearly equal voltage while the output remains within its allowed range. These assumptions let the feedback network set the gain. If the output saturates or feedback is lost, the equal-input approximation no longer applies.

For an inverting stage with input resistor $R_{in}$ and feedback resistor $R_f$, $A_v=-R_f/R_{in}$. For a non-inverting stage with $R_f$ from output to the inverting input and $R_g$ from that input to reference, $A_v=1+R_f/R_g$. The minus sign in the inverting case represents a phase reversal. Resistors must be connected in the stated topology; swapping the input and feedback roles changes the circuit.

With $R_f=90$ kΩ and $R_g=10$ kΩ, the non-inverting gain is 10. An input of 0.10 V ideally produces 1.0 V. A separate inverting stage with $R_{in}=10$ kΩ and $R_f=90$ kΩ has gain −9 and produces −0.90 V for the same input. If its supply or output range does not include −0.90 V, the actual output clips and the linear gain calculation is invalid.

## Preserve a small differential signal

Many sensors encode a small wanted difference on top of a larger shared voltage. An instrumentation amplifier is often appropriate because it offers high input impedance and specified common-mode rejection. Ideally its output follows $V_{out}=V_{ref}+G(V_+-V_-)$, where $V_{ref}$ sets the output baseline. For a constructed $2$ mV differential signal, gain 100 and $V_{ref}=1.65$ V, the ideal output is 1.85 V; reversing the differential polarity gives 1.45 V. Both fit an assumed 0.2–3.1 V output window, but this arithmetic does not establish the amplifier's common-mode range, stability or output swing.

For a unipolar ADC, a reference or level shift may place a bipolar signal around midscale, but the reference must be stable and the full signal must remain inside both amplifier and converter limits. Increasing gain can improve use of the ADC range, but also amplifies input noise and offset and reduces headroom. Instrumentation amplifiers cannot remove every electrode mismatch, reference error or interference source.

## Check the real operating limits

Before interpreting a gain equation, check the data sheet for input common-mode range, output swing at the intended load, input offset and bias current, gain-bandwidth product, noise, stability and recovery after overload. A stage can clip even when its nominal small-signal gain is correct. Cascaded stages can also amplify an offset until a later stage saturates. Power-supply bypassing and layout affect behavior that a resistor-only model omits.

State the signal range, reference, load and bandwidth at each stage. For human-connected equipment, electrical isolation and applicable safety requirements need qualified design review; this synthetic course example does not specify or validate a patient-connected circuit. The later feedback and differential-signal lessons develop finite gain, bias, common-mode range and interface imbalance in more detail.
