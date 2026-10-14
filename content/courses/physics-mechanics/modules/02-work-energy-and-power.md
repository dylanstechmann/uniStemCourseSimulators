# Work, energy, and power

## Learning objectives

By the end of this reading, you should be able to:

1. Calculate translational kinetic energy and relate net work to its change.
2. Compare gravitational potential energy with final kinetic energy and interpret the difference within a stated model.
3. Calculate power as a rate of energy transfer and check its units.

## Work measures energy transfer by a force

A force does work when its point of application moves. For a constant force \(\vec F\) and displacement \(\Delta\vec r\),

\[
W=\vec F\cdot\Delta\vec r=F\,\Delta r\cos\phi,
\]

where \(\phi\) is the angle between force and displacement. Work is positive when the force component points along the displacement, negative when it points against it, and zero when the force is perpendicular to the displacement. Work is measured in joules: \(1\,\mathrm J=1\,\mathrm{N\,m}\). For a force that changes during motion, the work is accumulated along the path as \(W=\int\vec F\cdot d\vec r\). This integral is a starting definition; later lessons use it with more involved system boundaries and force histories.

The dot product matters. A 10 N force directed along a 2 m displacement does 20 J of work. If that force is perpendicular to the displacement, it does zero work over that interval even though the force is nonzero. A force can also do negative work: kinetic friction acting opposite a sliding object's motion removes mechanical energy from that object's translational motion.

## Kinetic energy and the work–energy theorem

For a point mass moving at speed \(v\) in a declared reference frame, translational kinetic energy is

\[
K=\frac12mv^2.
\]

Kinetic energy is a scalar and is nonnegative in this model. It depends on speed, not the direction of travel, and on the chosen reference frame. Doubling speed multiplies \(K\) by four; doubling mass at fixed speed doubles \(K\). The unit is a joule because \(\mathrm{kg\,m^2/s^2}=\mathrm{N\,m}\).

The work–energy theorem states that the net work by all forces on the chosen particle or body equals the change in its kinetic energy:

\[
W_{\mathrm{net}}=\Delta K=K_f-K_i.
\]

If the net work is positive, the final kinetic energy is larger; if it is negative, the final kinetic energy is smaller. A work calculation and a force-balance calculation describe the same change from different angles. The work method can be convenient when initial and final states are known and the desired intermediate timing is not. It does not by itself reveal how speed changed at every instant.

For the preserved check, a 2 kg object moves at 3 m/s. Its kinetic energy is \(K=\frac12(2)(3^2)=9\,\mathrm J\). The direction of motion does not change this value, although the reference frame used to specify the 3 m/s must be understood. This calculation gives energy associated with translation only. A rotating or vibrating body can also carry other forms of kinetic energy that are outside this one-particle calculation.

## Conservative forces and potential energy

Some forces allow energy to be stored in an interaction. Near Earth's surface, gravitational potential-energy change is \(\Delta U_g=mg\,\Delta y\), where upward is positive. For an ideal linear spring, energy stored relative to its relaxed length is \(U_s=\frac12kx^2\), with spring constant \(k\) and displacement \(x\). The chosen zero level for potential energy is a reference; measurable energy differences do not depend on adding the same constant to every value.

Gravity and an ideal spring are conservative in the models used here: their work between two endpoints depends on those endpoints, not on the path between them. For a conservative force, \(W_c=-\Delta U\). When only conservative forces exchange energy within an isolated mechanical system, kinetic and potential energy trade while their sum stays constant. This is not the only way energy can be transferred, and the system boundary must be stated before deciding which forces or energy stores are internal.

Compressing a spring by 0.05 m with \(k=200\,\mathrm{N/m}\) stores

\[
U_s=\frac12(200)(0.05)^2=0.25\,\mathrm J.
\]

The quadratic dependence means doubling compression to 0.10 m stores 1.0 J, four times as much, in this ideal linear-spring model. The spring's restoring force does negative work while it is being compressed by an external hand; the spring potential energy increases by the same amount if losses are neglected.

## Interpreting mechanical energy that is not retained

The second preserved item describes a 2.0 kg object dropped from rest at a height of 5.0 m. Taking the floor as the zero of gravitational potential energy, initial gravitational potential energy is \(mgh=(2.0)(9.81)(5.0)=98.1\,\mathrm J\). At the stated impact speed of 8.0 m/s, final translational kinetic energy is \(\frac12(2.0)(8.0^2)=64.0\,\mathrm J\). The difference is

\[
98.1\,\mathrm J-64.0\,\mathrm J=34.1\,\mathrm J.
\]

That is the keyed mechanical-energy difference for the stated numbers. In a simple drop model with no uncounted energy stores, it is interpreted as mechanical energy dissipated through effects such as air drag, sound, or deformation. The calculation does not identify which pathway accounts for the difference. If rotation, internal deformation, residual motion, or another store matters, it must be added to the system model before labeling the entire difference “dissipated.” Total energy is not destroyed; the calculation tracks only the listed mechanical stores.

This distinction also explains why conservation of mechanical energy is conditional. If only gravity acts on a point mass between release and impact, \(mgh=\frac12mv^2\), giving a speed near 9.90 m/s after a 5 m drop. The stated 8.0 m/s is lower, so the listed translational mechanical energy does not close by itself. Subtracting final kinetic energy from initial gravitational potential energy quantifies the gap; it does not prove the object experienced a specific force or reveal its material response.

## Power is the rate of transfer

Power describes how quickly work is done or energy is transferred:

\[
P=\frac{dW}{dt}=\vec F\cdot\vec v.
\]

For a force that stays aligned with velocity, 10 N acting on an object moving at 2 m/s gives 20 W. A perpendicular force has zero instantaneous power in the point-mass model, though it can change the direction of motion. Power has units joules per second, or watts. A motor, muscle, or device can transfer the same amount of energy over different durations and therefore operate at different average powers.

Average power over a finite interval is \(\bar P=\Delta E/\Delta t\) when the transferred energy and interval are stated. Do not confuse power with energy: joules describe an amount, while watts describe a rate. Nor does mechanical power alone determine biological efficiency; that comparison needs a defined input, output, and system boundary.

## Common checks and limits

- Square speed, not velocity components with inconsistent frames, when using \(K=\frac12mv^2\).
- Use the force component along displacement for work; retain the sign.
- Compare changes in potential energy, not absolute values with an unstated zero.
- Use \(W_{\mathrm{net}}=\Delta K\), then separately decide whether mechanical energy was stored, transferred, or dissipated.
- Keep joules and watts distinct, and include the time interval for average power.
- A difference between two mechanical-energy values does not identify a unique dissipative mechanism or injury risk.

These examples use constant mass, classical speeds, declared reference frames, and simplified translational or ideal-spring models. They do not estimate injury risk, tissue damage, device performance, or the efficiency of a real biological system. The next energy-focused units develop system boundaries and impact-time/distance calculations in more detail.

## Further study

These link-only OpenStax University Physics Volume 1 sections provide more detail on [kinetic energy](https://openstax.org/books/university-physics-volume-1/pages/7-2-kinetic-energy), the [work–energy theorem](https://openstax.org/books/university-physics-volume-1/pages/7-3-work-energy-theorem), [power](https://openstax.org/books/university-physics-volume-1/pages/7-4-power), and [conservative and non-conservative forces](https://openstax.org/books/university-physics-volume-1/pages/8-2-conservative-and-non-conservative-forces). This lesson uses original wording and calculations; no source prose, examples, problems, figures, or datasets are reproduced.
