# Free-body diagrams and equilibrium

## Learning objectives

1. Draw a free-body diagram for a stated planar beam, with external loads and support reactions kept on the isolated body.
2. Solve a determinate two-dimensional beam reaction problem using signed force and moment balance.

## Isolate the body before writing equations

Statics asks what loads and reactions can balance a body under a specified model. Begin by naming the body or structure that will be analyzed. Draw only that isolated object, choose coordinate axes, and add every force and couple that the surrounding world exerts on it. A support is replaced by the reaction components allowed by its idealized constraint. The [MIT OpenCourseWare Solid Mechanics lecture notes](https://ocw.mit.edu/courses/1-050-solid-mechanics-fall-2004/pages/lecture-notes/) include a lecture on static-equilibrium requirements and are used here as a link-only course reference.

A free-body diagram is a model of forces on one chosen body. If the beam pushes down on a support, that force belongs on a separate support diagram; the beam diagram instead shows the equal and opposite force the support applies to the beam. Do not include both members of an action–reaction pair on the same isolated object. Do not draw “net force” as an additional force: the net force is the vector sum of the actual external forces already shown.

Use axes that make the unknowns and equations easy to read. For a horizontal beam, a convenient choice is positive **x** to the right, positive **y** upward, and counterclockwise moments positive. Label the load locations and distances from a reference point. If a support is idealized as a pin, it can exert horizontal and vertical reaction components but no couple moment. A roller on a level surface supplies a reaction normal to that surface, usually vertical in this diagram. A fixed support can resist horizontal and vertical translation and can also exert a reaction moment. These are modeling assumptions; the word “support” alone does not tell you which reactions are present.

## Apply the planar equilibrium conditions

For a rigid body at rest in a plane, translational and rotational acceleration are zero. The independent equilibrium equations are

**ΣFx = 0, ΣFy = 0, ΣMO = 0.**

The first two equations balance horizontal and vertical force components. The third balances moments about a chosen point **O**. For a force with components **Fx** and **Fy** applied at position **(x, y)** relative to **O**, its signed out-of-plane moment is **MO = xFy − yFx**. A force whose line of action passes through **O** has zero moment about that point. Moments have units N·m when force is in newtons and distance is in metres.

Choose the moment center strategically. Taking moments about a pin can eliminate its two unknown force components from the moment equation because their lever arms are zero at the pin. This often gives one support reaction directly; force balance then gives the other. The pivot is a calculation choice, not a claim that the beam rotates about that support. Any point gives the same physical reactions if the force equations and moment equation are applied consistently.

Equilibrium is more than a vertical-force sum. Two equal and opposite forces can produce zero net force but a nonzero couple if they act along different lines. Such a body would tend to rotate. The moment equation catches that missing balance. Conversely, checking moments about one origin does not replace the horizontal and vertical force equations; a complete planar rigid-body check uses all three independent conditions.

## Solve a simply supported beam

Consider a level beam of span **L** supported by a pin at its left end and a roller at its right end. A downward point load **P** acts a distance **a** from the left support. The beam free-body diagram contains **P** downward at **x = a**, the pin reactions **RLx** and **RLy** at the left, and the roller reaction **RRy** at the right. There is no support couple in this ideal pin-and-roller model. The unknown horizontal reaction is zero when there are no other horizontal loads, from **ΣFx = 0**.

Take counterclockwise as positive and sum moments about the left support. The left reaction has zero lever arm, while the load turns clockwise and the right reaction turns counterclockwise:

**ΣML = RRy L − P a = 0**, so **RRy = P a/L**.

Vertical force balance then gives **RLy + RRy − P = 0**, so **RLy = P(1 − a/L)**. The reactions add to the applied load, and their division depends on where that load acts. A load near the left support produces a smaller right reaction; a load centered on the beam produces equal vertical reactions.

For a **600 N** point load at midspan of a **4 m** beam, **a = L/2 = 2 m**. The moment equation gives **RRy = (600 N)(2 m)/(4 m) = 300 N**. Force balance gives **RLy = 600 N − 300 N = 300 N**. The reactions are upward, and their sum balances the downward load. This recovers the unchanged week‑1 practice answer of 300 N at either support.

For the preserved off-center item, the load is **200 N** at **a = 1.0 m** on a **4.0 m** span. Taking moments about the left support gives **RRy = (200 N)(1.0 m)/(4.0 m) = 50 N**. Then **RLy = 200 N − 50 N = 150 N**. A useful check is to take moments about the right end: the left reaction produces a clockwise moment of **(150 N)(4.0 m) = 600 N·m**, and the point load produces a counterclockwise moment of **(200 N)(3.0 m) = 600 N·m**. The moments cancel with the same sign convention.

## Support models and load resultants need care

An ideal support removes selected rigid-body motion but does not automatically provide every possible reaction. A roller can move parallel to its contact surface in the ideal model. A pin can rotate but prevents translation. A fixed support resists rotation through a couple as well as translation. Adding a reaction the support cannot exert may make an unknown count look larger and produce a false model; omitting a permitted reaction can make the equations incomplete.

A distributed load can sometimes be replaced by a single resultant for whole-body equilibrium. A uniform downward load of intensity **q N/m** over a length **L** has total force **qL** acting at its midpoint. The units check is **(N/m)(m) = N**. A nonuniform distribution acts at its centroid, found from its force-weighted position. The equivalent resultant preserves the total force and moment for the rigid-body balance; it does not preserve the detailed local load distribution needed for later internal-force or stress calculations.

## Check whether equilibrium can determine the unknowns

Count the unknown reaction components after the support model is drawn, then identify independent equations. A planar rigid body supplies at most three independent equilibrium equations. If there are more unknown reactions than independent equations, rigid-body statics alone cannot determine every reaction. Additional deformation compatibility, stiffness information or another justified relation may be needed. If the equations are redundant or the supports do not constrain the body in the needed directions, a unique static reaction solution may not exist.

This is why “statically determinate” describes the solvability of a particular idealized structure by equilibrium alone, not the general strength or reliability of a design. The later forearm lesson applies equilibrium to a biological lever, while the later materials lessons calculate stress, deflection and failure criteria. This first reading treats supports as ideal and beams as rigid for reaction calculations; it makes no claim about how a real structure deforms or whether it is safe.

## A repeatable solution check

Before solving, state the isolated body, support assumptions, axes, force directions and load locations. Write **ΣFx = 0** and **ΣFy = 0** for the external forces on that body, then use a moment center that removes avoidable unknowns. Carry signs and units through the moment equation. Finally, substitute the reactions into both force balances and check a second moment center when practical. If reactions point opposite to an assumed arrow, the negative answer signals the actual direction; it is not automatically an algebra error.

The two practice items preserve different checks: symmetry gives equal reactions under a central load, while taking moments about one support solves the off-center reaction. Their original IDs, prompts and answer keys are unchanged. The arithmetic is short, but the free-body diagram and support model determine whether the equations describe the intended beam at all.
