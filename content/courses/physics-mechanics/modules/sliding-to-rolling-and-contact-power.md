# Sliding to rolling: contact velocity, torque and power

The [rolling lesson](10-torque-angular-momentum-and-rolling.md) assumes no slip and then checks whether static friction can sustain it. A body initially sliding with the wrong spin does not satisfy that constraint. Kinetic friction changes both center motion and rotation until the contact's relative velocity reaches zero. This reading derives that transition and its energy balance on a fixed horizontal surface. It concerns ideal mathematical bodies and gives no surface-treatment, braking or equipment instructions.

## Define signs at the contact point

Take rightward center velocity v as positive and clockwise angular velocity omega as positive. Let R be the body radius and I=beta mR², with beta>0. The instantaneous bottom-point velocity relative to a fixed surface is s=v−R omega. Positive s means the bottom slides right; kinetic friction on the body therefore points left. The center can move right even when s is negative if the body is spinning fast enough. Friction opposes relative contact slip, not necessarily center motion.

Assume a rigid body, maintained horizontal contact, normal force mg and a constant kinetic coefficient mu while slipping. There is no other horizontal force and no rolling resistance. In the s>0 phase, friction magnitude f=mu mg. Translation gives dv/dt=−mu g, while clockwise torque gives I domega/dt=fR, so R domega/dt=mu g/beta. Together,

$$\frac{ds}{dt}=-\mu g(1+1/\beta).$$

If s starts positive, this constant negative derivative drives it toward zero. The equations are valid only until that first event. Continuing the same signed kinetic force beyond it would make slip reverse while friction still pointed in the old direction, violating the contact model.

## Transition time and the retained rolling speed

For initial center velocity u and initial rim speed w0=R omega0 with u>w0, the transition time is (u−w0)/[mu g(1+1/beta)]. Integrating either velocity to that time gives

$$v_* = R\omega_* = \frac{u+\beta w_0}{1+\beta}.$$

The same final expression follows for initially negative slip, with the friction direction reversed. For that phase dv/dt=+mu g and R domega/dt=−mu g/beta; the transition time uses |u−w0|. If mu is zero and slip is nonzero, there is no finite transition. If initial slip is already zero, this unforced horizontal idealization needs zero friction and remains in rolling motion. Contact friction need not always have magnitude mu mg once slip has ended.

The transition speed is independent of mu for these assumptions, but the transition time and distance are not. That cancellation is a property of the coupled constant-friction equations. It does not imply that all real surfaces, bodies or rolling processes reach the same state regardless of contact behavior.

## Worked spin-up example

Take m=3 kg, R=0.20 m, beta=0.5, initial u=4 m/s, no spin and mu=0.25. With g=9.81 m/s², the body reaches rolling at v*=8/3 m/s and omega*=40/3 rad/s. Transition time is about 0.54366293 s. The center decelerates while clockwise spin increases. If your calculation increases both translation and rotation from this no-spin state without an external drive, the force/torque signs or energy ledger are wrong.

The initial kinetic energy is 24 J. At rolling, translation plus rotation is (1/2)m(1+beta)v*²=16 J, so mechanical energy decreases by eight joules. Linear momentum of the body alone is not conserved because the surface supplies friction impulse. This is a different conservation question from energy transfer through a fixed no-slip contact.

## Power belongs to the force application point

The friction force contributes translational power −fv and rotational power +fR omega in the positive-slip phase. Their sum is −f(v−R omega)=−fs. It is nonpositive while the body slips in the assumed direction. The mechanical energy lost equals the integral of f|s| over the slipping interval. Multiplying f by center displacement alone would omit the simultaneous rotational energy gain and overestimate dissipation.

The general energy loss for the transition is

$$D=\frac12m\frac{\beta}{1+\beta}(u-w_0)^2.$$

You can derive it by subtracting the final rolling kinetic energy from the initial translation-plus-spin energy, or by integrating contact power. It is nonnegative, vanishes when the initial state already rolls, and depends on the square of initial slip. These checks help expose a sign error. The ideal contact model does not determine microscopic heating, deformation, wear or an actual temperature rise.

## A rehearsal that tests the opposite intuition

For a solid-cylinder inertia ratio beta=0.5, use m=2 kg, u=3 m/s, w0=0 and mu=0.20. Rolling begins at v*=2 m/s after about 0.509684 s; the mechanical energy loss is three joules. A separate overspin state uses the same mass and inertia ratio with u=1 m/s and w0=2 m/s. Its bottom slips left, so friction points right and the center accelerates to 4/3 m/s while spin decreases. Initial kinetic energy is three joules and final energy is 8/3 joules. The center speeds up while total mechanical energy falls by one third of a joule.

This overspin example distinguishes friction's direction from a slogan that it always slows an object's center. Report contact velocity, force direction, center acceleration and total power as separate quantities. They can have different signs without contradiction. Once rolling begins on this ideal level unforced surface, zero friction suffices; a slope or applied torque would require a new static-friction calculation and an admissibility check.

## Study task and boundaries

Before using feedback, derive the transition for both slip signs, integrate the contact-power history and test the no-slip and zero-friction limits. The [contact-transition assignment](../assignments/coursework-03-contact-transition.md) asks for a phase-resolved simulation with an event stop instead of blindly continuing kinetic friction.

MIT OCW [8.01SC Classical Mechanics Fall 2016 syllabus](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/pages/syllabus/) and its rolling-dynamics/energy strand provide a link-only scope comparator. All explanations, inputs and derivations here are original and developed with substantial AI assistance; no source problem or diagram was imported. Deformable contact, moving belts, impacts, three-dimensional motion and real friction characterization remain outside this selected model. Qualified review and measured workload remain open; the course is partial and unreviewed.
