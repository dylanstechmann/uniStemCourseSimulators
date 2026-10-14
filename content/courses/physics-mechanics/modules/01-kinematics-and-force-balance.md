# Kinematics and force balance

## Learning objectives

By the end of this reading, you should be able to:

1. Apply Newton's second law to a defined system and calculate acceleration from its net force and mass.
2. Draw a force balance with stated axes and resolve gravity and support forces on a frictionless incline.

## Describe motion before explaining it

Kinematics describes how position changes with time. Choose a reference frame and a positive direction, then represent position by (x(t)) in one dimension. Displacement over an interval is \(\Delta x=x_2-x_1\); average velocity is \(\bar v=\Delta x/\Delta t\). Instantaneous velocity is the rate of change of position, \(v=dx/dt\), and acceleration is the rate of change of velocity, \(a=dv/dt\). Their SI units are metres, metres per second, and metres per second squared.

Velocity carries a sign or direction; speed is its magnitude. A negative velocity means motion opposite the chosen positive direction, not a negative speed. Acceleration also has a direction. An object can move in the positive direction while accelerating in the negative direction, in which case its speed is decreasing at that instant. The velocity of an object is not itself a force, and a force is not required to keep an object moving at constant velocity.

In an experiment, position measurements are finite and may be noisy. A finite difference such as \((x_{i+1}-x_i)/(t_{i+1}-t_i)\) estimates average velocity over that interval; repeating the difference on velocity estimates acceleration. Smaller intervals do not automatically guarantee a better estimate when measurement noise is present. The later vector-kinematics lesson treats multiple coordinates and changing frames; here the goal is to keep the description of motion separate from the force model.

## Define the body and draw its forces

Newton's second law applies to a specified system. Start by naming the body whose motion you want to predict: a cart, a block, or an instrument package. Sketch only forces exerted **on** that body by other bodies or fields. Gravity acts downward near Earth's surface with weight \(mg\). A surface in contact can exert a normal force perpendicular to itself. A rope can exert tension along its length. Friction or an applied force appears only when the stated physical contacts or interactions provide it.

Do not draw the net force as an additional arrow beside its component forces; the net force is their vector sum. Do not place the equal-and-opposite partner force on the same free-body diagram. For example, the floor's normal force on a cart and the cart's normal force on the floor act on different bodies. They form a third-law pair, but only the first belongs on the cart's diagram.

Choose axes before writing equations. Positive directions are conventions, so state them and keep the signs consistent. On a horizontal track, horizontal and vertical axes may be simplest. On an incline, axes parallel and perpendicular to the surface usually make the contact constraint easier to express. A force arrow can then be resolved into components along those axes.

## Newton's second law is a vector balance

For a body of constant mass \(m\) in an inertial reference frame,

\[
\sum \vec F_{\mathrm{external}}=m\vec a.
\]

The component equations follow the selected axes: \(\sum F_x=ma_x\), \(\sum F_y=ma_y\), and so on. Every force component in a direction contributes to that direction's net force. A zero acceleration means the net force in that direction is zero; it does **not** mean that no forces act. A body at rest can have weight balanced by a support force, and a body moving at constant speed in a straight line can have the same balanced forces.

For the preserved cart question, the system has mass 3 kg and net horizontal force 12 N. Along the horizontal axis, \(12\,\mathrm N=(3\,\mathrm{kg})a\), so \(a=4\,\mathrm{m/s^2}\). The net force is the given sum of all horizontal external forces. The cart's current velocity is unnecessary for this calculation: the force determines its acceleration, not its velocity by itself. The units check because one newton is one kilogram metre per second squared.

## Work an incline with axes along the surface

Consider the preserved 10 kg block sliding without friction down a 30° incline. Choose positive \(x\) down the plane and positive \(y\) perpendicular outward. Gravity \(mg\) points vertically down, so its components are \(mg\sin\theta\) down the incline and \(mg\cos\theta\) into the surface. The surface's normal force \(N\) points outward and is perpendicular to the incline. No friction force belongs in this model because the prompt explicitly says the block slides without friction.

In the perpendicular direction the block does not accelerate away from or into the plane, so \(N-mg\cos\theta=0\). Along the plane,

\[
mg\sin\theta=ma,\qquad a=g\sin\theta.
\]

With \(g=9.81\,\mathrm{m/s^2}\) and \(\theta=30^\circ\), the acceleration is \(9.81\sin30^\circ=4.905\,\mathrm{m/s^2}\) down the plane. The block's mass cancels because both its weight component and its inertial mass are proportional to \(m\) in this ideal model. The normal force is \(N=(10)(9.81)\cos30^\circ\approx84.96\,\mathrm N\), not the full weight of about 98.1 N. The normal force is a contact force, not a universal synonym for weight.

The acceleration result depends on the stated assumptions: a fixed straight plane, no friction, a constant gravitational field, and a block treated as a point mass for translation. Add friction, a rope, or rolling and the force balance changes. A surface that loses contact also cannot supply a negative normal force; that is a sign that the assumed contact model must be reconsidered.

## A vertical force balance uses the same law

For a 0.20 kg instrument package accelerating upward at 2 m/s², choose upward as positive. Tension \(T\) points upward and weight \(mg\) downward, giving \(T-mg=ma\). Thus \(T=m(g+a)=0.20(9.81+2)=2.362\,\mathrm N\), or about 2.36 N. Since the package accelerates upward, tension must exceed its weight. If the acceleration were zero, tension would equal weight; if it accelerated downward, tension would be smaller than weight in this simple rope model.

These examples use the same procedure: define the body, state axes, list external forces, project onto each axis, and solve Newton's law. Kinematics supplies or describes acceleration; dynamics relates it to the net force. This separation helps catch errors such as using \(F=ma\) with one force when several forces act or treating a constant velocity as proof that the body is force-free.

## Checks and boundaries

- Check that the system boundary identifies which body's forces belong in the balance.
- Resolve a weight vector into components; do not rotate gravity itself to align it with the incline.
- Check signs against the stated positive direction before interpreting a negative acceleration.
- Check units: force divided by mass has units \(\mathrm{m/s^2}\).
- In the frictionless-incline model, \(\theta=0\) gives zero acceleration along the plane and \(N=mg\), consistent with a horizontal surface.
- Distinguish the acceleration predicted by the model from measured motion; measurement noise and unmodeled forces can create differences.

This introduction does not cover full three-dimensional constraints, variable-mass systems, non-inertial frames, detailed friction laws, or tissue constitutive response. Later lessons develop vector kinematics and frames, contact and friction, and impact forces. An average force or a simple point-mass prediction alone does not establish a tissue injury threshold.

## Further study

These link-only OpenStax University Physics Volume 1 sections provide more detail on [average and instantaneous acceleration](https://openstax.org/books/university-physics-volume-1/pages/3-3-average-and-instantaneous-acceleration), [Newton's second law](https://openstax.org/books/university-physics-volume-1/pages/5-3-newtons-second-law), and [drawing free-body diagrams](https://openstax.org/books/university-physics-volume-1/pages/5-7-drawing-free-body-diagrams). This lesson uses original wording and calculations; no source prose, examples, problems, figures, or datasets are reproduced.
