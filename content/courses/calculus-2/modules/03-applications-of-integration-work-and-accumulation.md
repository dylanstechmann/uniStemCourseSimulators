# Applications of integration: work and accumulation

Integration adds many small contributions. For a one-dimensional force that varies with position, a short displacement $\Delta x$ near position $x$ contributes approximately $F(x)\Delta x$ of work. Summing across the path and refining the partition leads to

$$
W=\int_a^b F(x)\,dx.
$$

This model assumes that $F(x)$ is the force component along the displacement and that the path is described by the coordinate $x$. A constant force gives the familiar result $W=F(b-a)$. A changing force requires the integral because equal distances can contribute different amounts of work.

## A linear force model

Take the constructed force $F(x)=4x$ newtons over the displacement from $x=0$ to $x=3$ metres. The accumulated work is

$$
W=\int_0^3 4x\,dx
=\left[2x^2\right]_0^3
=18\ \text{N·m}=18\ \text{J}.
$$

The units follow directly: newtons multiplied by metres are joules. The value is not the endpoint force multiplied by the whole distance; that shortcut would give $12\ \text{N}\times3\ \text{m}=36\ \text{J}$ and overcount because the force starts at zero and increases linearly. The area under the force-versus-position graph is a triangle with base 3 m and height 12 N, giving the same 18 J.

On a short step from $x=1$ m to $x=1.1$ m, the left-endpoint rectangle estimates $F(1)(0.1)=0.4$ J. The exact integral over that step is

$$
\int_1^{1.1}4x\,dx=2(1.1^2-1^2)=0.42\ \text{J}.
$$

Reducing the step width improves the rectangle approximation for this smooth force. The full integral is the limit of such sums, while numerical quadrature applies a finite rule to sampled values.

## Direction and bounds determine the sign

Work is signed. If the modeled force points opposite to the positive displacement, $F(x)$ is negative and the integral is negative. For example, $F(x)=-4x$ over the same positive displacement produces $-18$ J. This sign records the direction of the force contribution relative to the path; it is not a negative amount of energy. Reversing the integration bounds also changes the sign:

$$
\int_3^0 4x\,dx=-18\ \text{J}.
$$

Before integrating, define the coordinate direction, state the starting and ending positions, and choose the force component that acts along that coordinate. If the force changes direction, its graph crosses the axis and positive and negative portions contribute with their signs. The net work is their signed sum. Taking an absolute value would answer a different question about total magnitude of work contributions.

## Use the same accumulation structure elsewhere

The integral combines a density with the measure over which it acts. A rate per minute integrated over minutes gives a total amount; a force in newtons integrated over metres gives work. In each case, bounds come from the process and units provide a consistency check. The formula alone does not supply the correct bounds or establish what the modeled quantity means.

For measured force data, first retain the actual position coordinates and any calibration information. A trapezoidal estimate treats each adjacent pair as a straight segment. Its accuracy depends on spacing, curvature, measurement error and offsets. The later force-work lab separates offset correction from quadrature and compares numerical work with a specified synthetic model. Neither a smooth fit nor a precise integral removes uncertainty in the measurements or the model.

These values are constructed examples for learning integration. They establish no actuator specification, material property or hardware behavior.
