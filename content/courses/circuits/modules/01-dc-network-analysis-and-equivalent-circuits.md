# DC network analysis and equivalent circuits

DC circuit analysis relates voltages, currents and component behavior at a steady operating point. Choose a reference node, label unknown node voltages and define current directions before writing equations. Kirchhoff's current law (KCL) states that signed currents sum to zero at a node; Kirchhoff's voltage law (KVL) states that signed voltage changes sum to zero around a closed loop. A negative result usually means the actual direction is opposite the chosen reference, not that the algebra failed.

## Reduce a resistive network

For a resistor, Ohm's law is $V=IR$. Series elements carry the same current and their resistances add; parallel elements share voltage and their conductances add. Keep units consistent: volts divided by kilohms gives milliamps. Once a solution is found, substitute it into the original node or loop equations and check power when useful. For a passive resistor, $P=VI=I^2R=V^2/R$ must be nonnegative under the passive sign convention.

For example, a 12 V ideal source in series with 2 kΩ and 4 kΩ has total resistance 6 kΩ and current $12/6=2$ mA. The drops are 4 V and 8 V, summing to the source voltage. This check catches a common error: adding parallel resistance when the elements share the same series current.

## Replace a linear port with a Thevenin model

Any linear two-terminal network can be represented at its port by an ideal voltage $V_{th}$ in series with resistance $R_{th}$, for the port behavior of interest. Find $V_{th}$ as the open-circuit terminal voltage. For a network with only independent sources, deactivate them to find $R_{th}$: short ideal voltage sources and open ideal current sources, then calculate the resistance seen into the terminals. Keep dependent sources active; if they are present, apply a test source at the port and use the resulting voltage/current ratio.

Consider a 12 V source with a 4 Ω series resistor and a 12 Ω resistor from the output node to the return. The open-circuit port voltage is the divider result $V_{th}=12(12)/(4+12)=9$ V. With the independent source shorted, the port resistance is $R_{th}=4\parallel12=3$ Ω. If a 6 Ω load is connected, the equivalent circuit predicts $V_L=9(6)/(3+6)=6$ V. The original circuit gives the same result: $12\parallel6=4$ Ω at the node, followed by a divider of 4 Ω against the 4 Ω series resistor. The two models agree at the port, though their internal branch currents differ.

## Measurement loading is part of the circuit

A real instrument has finite input resistance. If a 10 kΩ source drives a 1 MΩ voltmeter, the measured fraction is $1\text{ MΩ}/(10\text{ kΩ}+1\text{ MΩ})\approx0.9901$. The meter reads about 0.99% below the unloaded voltage in this simple model. A high input resistance reduces loading but does not remove it, and real instruments also have input capacitance, bias current and range limits.

Thevenin equivalence preserves voltage-current behavior at the chosen terminals under the stated linear model; it does not preserve every internal quantity, transient response or nonlinear operating condition. A static equivalent is not a complete sensor specification. These constructed values are for instruction and describe no actual hardware.
