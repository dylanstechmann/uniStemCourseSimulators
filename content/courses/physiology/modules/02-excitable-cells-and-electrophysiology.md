# Excitable cells and electrophysiology

The cell membrane separates electrical charge and acts approximately as a capacitor. Ion-selective pathways provide conductances through which charged species move. Define membrane voltage as $V_m=V_{inside}-V_{outside}$; a negative value means the inside is at lower electrical potential than the outside. Current sign also needs a convention. Here ionic current is outward-positive, so a negative current means net inward movement of positive charge.

## Reversal potential and driving force

For an ohmic pathway selective to one ion, its current is

$$
I_i=g_i(V_m-E_i),
$$

where $g_i$ is conductance and $E_i$ is that ion's reversal potential. At $V_m=E_i$, the net current through that pathway is zero. If $V_m$ is above $E_i$, the outward-positive current is positive; if it is below, the current is negative. Conductance sets how strongly the pathway responds to the voltage difference. Since 1 nS·mV = 1 pA, unit conversion can remain simple when those scales are used.

For potassium with $V_m=-60$ mV, $E_K=-90$ mV and $g_K=2$ nS, the driving force is +30 mV and $I_K=+60$ pA, outward-positive. For sodium with $V_m=-50$ mV, $E_{Na}=+50$ mV and $g_{Na}=4$ nS, the driving force is −100 mV and $I_{Na}=-400$ pA, indicating inward positive charge under this convention. The sign describes the direction relative to the declared convention; it is not a negative conductance.

## Multiple pathways shape the membrane potential

Opening a conductance moves $V_m$ toward that pathway's reversal potential, all else equal. With several passive ohmic pathways and no externally applied current, steady state satisfies zero net membrane current:

$$
\sum_i g_i(V_m-E_i)=0,
\qquad
V_m=\frac{\sum_i g_iE_i}{\sum_i g_i}.
$$

This weighted relation applies only to the stated fixed-conductance model. For example, take $g_K=2$ nS at $E_K=-90$ mV and $g_{Na}=0.2$ nS at $E_{Na}=+50$ mV. The steady voltage is about −77.3 mV, not either reversal potential. The potassium current is about +25.5 pA and sodium current about −25.5 pA; they balance. Changing a conductance changes both currents and the equilibrium.

When current is not balanced, the membrane capacitance causes voltage to change over time. Voltage- and time-dependent channel gates make conductances vary during an action potential. Refractory behavior follows channel kinetics and recovery, while propagation also depends on cable properties and cell geometry. A fixed voltage threshold alone does not explain every excitable-cell response.

The Nernst relation estimates a single-ion equilibrium potential from concentrations and charge under stated temperature and activity assumptions. A membrane with several permeant ions needs a multi-ion model, such as the Goldman relation, rather than treating resting voltage as the Nernst potential of one selected ion. The next membrane-potential lesson develops those equilibrium and permeability equations. All numerical examples are constructed teaching values; they describe no person, diagnosis or treatment.
