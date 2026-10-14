# Variable-mass momentum and continuous mass transfer

The familiar relation between force and momentum still applies when material enters or leaves a body, but the boundary must be drawn carefully. A cart that captures pellets gains mass and momentum; a rocket that ejects gas loses mass and gains momentum. In each case, the exchanged material carries momentum across the boundary at its velocity in a stated inertial frame. Ignoring that momentum flux produces the wrong acceleration, even when the arithmetic is flawless. This lesson derives a one-dimensional balance, applies it to an ideal rocket and to a cart that captures material, and makes the assumptions visible. All numbers are synthetic.

## Choose the system and the velocity frame

Let the changing-mass body have mass $m$ and velocity $v$ along a chosen positive axis in an inertial frame. During a short time $dt$, let material enter at rate $\dot m_{in}$ and leave at rate $\dot m_{out}$; these rates are positive magnitudes. Let their velocities in the same inertial frame be $w_{in}$ and $w_{out}$. Let $F_{ext}$ be the sum of other external forces along the axis. Then the one-dimensional momentum balance is

$$\frac{d(mv)}{dt}=F_{ext}+\dot m_{in}w_{in}-\dot m_{out}w_{out}.$$

The mass of the body changes at $\dot m=\dot m_{in}-\dot m_{out}$. Expanding the derivative gives an equivalent acceleration equation:

$$m\frac{dv}{dt}=F_{ext}+\dot m_{in}(w_{in}-v)-\dot m_{out}(w_{out}-v).$$

The extra terms account for the momentum carried in or out relative to the moving body. A flow rate is not enough; its velocity at the boundary and the chosen frame are part of the model. If both inflow and outflow occur, keep the two fluxes separate even when their mass rates cancel.

## Derive the ideal rocket equation

For a rocket ejecting gas but taking in no mass, $\dot m_{in}=0$ and $\dot m_{out}=q>0$. Let the exhaust speed relative to the rocket be a constant $u>0$ in the backward direction, so the gas has inertial-frame velocity $w_{out}=v-u$. Substitution gives

$$m\frac{dv}{dt}=F_{ext}-q((v-u)-v)=F_{ext}+uq.$$

Because the rocket mass decreases, $\dot m=-q$. Therefore the same equation can be written

$$m\frac{dv}{dt}=F_{ext}-u\dot m.$$

When external force is negligible and $u$ is constant, divide by $m$ and integrate between initial and final rocket masses:

$$\Delta v=u\ln\left(\frac{m_0}{m_f}\right).$$

This is a velocity increment. It is not the exhaust speed, and the logarithm depends on the mass ratio, not just the propellant mass. A larger exhaust speed or a larger initial-to-final mass ratio increases the ideal increment, but structural limits and real engine performance are outside this model.

**Worked rocket example.** A synthetic rocket has initial mass $m_0=600$ kg, final mass $m_f=450$ kg and exhaust speed relative to the rocket $u=800$ m/s. Ignoring gravity, drag and other external forces,

$$\Delta v=800\ln(600/450)=800\ln(4/3)=230.1\ \mathrm{m/s}.$$

The initial and final masses are positive and $m_0>m_f$, so the predicted increment is positive. If the rocket starts from rest, this idealized increment is its final speed in the chosen inertial frame; any initial velocity must otherwise be added with its sign.

## Compare with incoming material

For a body that captures material moving at inertial velocity $w_{in}$, with no outflow,

$$m\frac{dv}{dt}=F_{ext}+\dot m_{in}(w_{in}-v).$$

If a 20 kg cart moves at 10 m/s on a low-friction track and captures 5 kg of pellets that were initially at rest, neglect the external horizontal impulse and suppose it retains the pellets. The incoming velocity is zero, so the added mass slows the cart. Across the brief capture, momentum conservation gives

$$v_f=\frac{(20\ \mathrm{kg})(10\ \mathrm{m/s})+(5\ \mathrm{kg})(0)}{25\ \mathrm{kg}}=8.0\ \mathrm{m/s}.$$

The body and captured pellets form the final system. This case has the opposite mass-flow direction from a rocket. It also shows why a body does not automatically accelerate just because it gains mass: the incoming material's momentum matters.

## Common mistakes

- Applying $F_{ext}=m\,dv/dt$ to a changing-mass body while omitting momentum flux.
- Using exhaust speed relative to the rocket as if it were exhaust speed in the inertial frame.
- Giving an outflow rate as positive but then using the signed mass derivative without checking the sign.
- Combining inflow and outflow into one net mass rate when their velocities differ.
- Applying the ideal rocket logarithm when external forces, changing exhaust speed or multidimensional flow are important.
- Calling $u\ln(m_0/m_f)$ a guaranteed real-world final speed.

## Practice bounds and source comparison

The model is one-dimensional, nonrelativistic, and based on a stated inertial frame with uniform stream velocities. It does not cover nozzle thermodynamics, staging, pressure forces at an outlet, structural limits, vehicle control or real propulsion design. The incoming-mass example assumes a brief capture, negligible horizontal external impulse and retained pellets. These are paper calculations, not engineering advice.

MIT OpenCourseWare's undergraduate [8.01SC Classical Mechanics (Fall 2016) syllabus](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/) includes continuous mass transfer in Week 6. The [Week 6 course materials](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/week-6-continuous-mass-transfer/) sequence relative velocity and recoil with rocket problems, and include rocket-sled and snowplow examples. This original lesson uses different values and examples; no MIT wording, assessment, figure or data is reproduced.
