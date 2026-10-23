# Workless constraints and signed reactions

A position or force target does not replace the equations of constrained motion. An ideal stationary constraint can redirect acceleration through a reaction that does no instantaneous work at compatible velocity. A unilateral wall also needs a nonadhesive sign check. This original foundation develops those ideas with small prescribed mass matrices and a separate curved-constraint example. These are mathematical constructions, not measured contact conditions or a hardware-control procedure.

## Differentiate the actual constraint

For a holonomic equality b(q)=0, differentiating gives A(q)v=0, with A the gradient matrix. Differentiate again to obtain A a+Adot v=0. Even if velocity is instantaneously tangent to the constraint, Adot v need not vanish on a curved surface. Compatible initial position and velocity are required; an acceleration equation alone cannot repair an initial gap or impact.

Write the dynamics as M a=tau+A'lambda when tau includes the other declared generalized inputs. With independent constraint rows and positive-definite M, solve the block equations

$$\begin{pmatrix}M&-A^T\\A&0\end{pmatrix}\begin{pmatrix}a\\\lambda\end{pmatrix}=\begin{pmatrix}\tau\\-\dot A v\end{pmatrix}.$$

The Schur equation is (A M^-1 A')lambda=−Adot v−A M^-1 tau. The matrix is invertible under the stated rank conditions. Redundant constraint rows can make it singular; blindly inverting a projection or adding decimal precision does not restore missing rank.

## Workless does not mean dynamically irrelevant

Reaction power is lambda' A v, which is zero for compatible velocity. The reaction can nevertheless change acceleration substantially. It excludes motion through the ideal constraint rather than contributing stored or dissipated energy in this construction. Friction, moving boundaries, compliance and impact impulses need additional terms or models.

For one unit-normal constraint at rest, the normal mobility is A M^-1 A', and its reciprocal is a local effective normal mass. This scalar depends on the mass matrix, direction and coordinate convention. If A is rescaled, lambda and the reciprocal change; name the normal normalization before assigning physical force/mass units.

## A flat-wall worked example

Stipulate M with rows (2,1),(1,2) in generalized mass units and a wall q1>=0. At the boundary q1=v1=0 choose A=(1,0), with positive reaction pushing into the allowed region. Input tau=(-3,1) gives a1=0 from the active constraint. The second equation gives a2=0.5 and the first gives lambda=3.5.

Without the wall the acceleration would be (-7/3,5/3). The positive reaction prevents the forbidden inward normal acceleration while changing the coupled tangential acceleration. Its zero power at v1=0 is consistent with that substantial dynamic effect.

## Distinct rehearsal and release

For the rehearsal use M with rows (3,1),(1,2), the same flat wall and tau=(-4,2). The active solution is a2=one and lambda=five. Normal mobility is 2/5 and effective normal mass 5/2. The free acceleration (-2,2) verifies why a positive contact reaction is required.

For a separate input tau=(4,2), the equality-constrained solution would require lambda=-3. A nonadhesive wall cannot pull the mechanism back. At this compatible resting boundary, release instead gives free acceleration (1.2,0.4), directed into the allowed region in its normal component. A negative equality multiplier is not automatically invalid for a bilateral linkage; the unilateral wall assumption creates the sign condition here.

This branch reasoning applies to an instant at zero normal velocity. It is not a complete complementarity integrator, an impact law or a proof of contact persistence over a finite interval. A subsequent state needs new gap, velocity, acceleration and reaction checks.

## Curvature supplies an acceleration term

Use a separate unit-mass Cartesian point constrained at the inside boundary of a unit circle. Let b=(1−q'q)/2, so A=−q'. At q=(1,0),v=(0,2), the velocity is tangent and Adot v=−four. Thus A a=four, giving ax=-4. With no other force, inward reaction magnitude is four.

Dropping Adot v would incorrectly give zero inward acceleration and leave the circle. Reaction remains perpendicular to velocity and does zero power. The centripetal acceleration is a geometric requirement, not energy loss. This example is distinct from the flat frozen-matrix wall and does not assert an entire robot can be modeled as a unit point.

## Verify and bound the conclusion

Retain the original equations, normal sign, rank, initial compatibility, multiplier and free/active branch checks. For a trajectory, check constraint drift, energy and integration refinement separately; projecting a position after each step changes the numerical method and does not by itself verify the original differential equations.

[Modern Robotics 8.7 Constrained Dynamics](https://modernrobotics.northwestern.edu/nu-gm-book-resource/8-7-constrained-dynamics/) and [MIT OCW 2.12 Fall 2005 syllabus/calendar](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/) provide link-only constrained/hybrid-control scope. All examples are original and AI-assisted; no source circuit, mechanism diagram, exercise or data is imported. General contact/friction/impact solvers and physical validation remain outside this selected treatment. The course stays partial and unreviewed.
