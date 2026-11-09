# Frames and machines: multi-force members, dismembering frames and mechanical advantage

**Status:** original ungraded instruction with substantial AI assistance. Structures, loads and dimensions are synthetic. This reading extends the week-1 equilibrium lessons from trusses (whose members all carry axial force only) to frames and machines, whose members are not always two-force members. It is not a structural design, rating or load-capacity instruction.

## Learning objectives

1. Distinguish two-force members from multi-force members, and state the consequence (axial force only versus bending, shear and axial force).
2. Analyse a frame by identifying its two-force members, solving the whole-structure reactions, then dismembering at pins and applying equilibrium to each member.
3. Find an output force and a mechanical advantage of a machine from member and joint equilibrium.
4. Check that a solved frame or machine satisfies equilibrium on every member and state the ideal-model limits.

## Two-force members and why frames are different

In the truss lesson every member is pinned at both ends and loaded only at its pins, so each carries a single axial force: **tension** or **compression**. A member like that is a **two-force member**, because only two forces act on it and equilibrium forces them to be equal, opposite and collinear.

A **frame** or **machine** relaxes that assumption. Its members can carry loads applied *between* the pins, can be rigidly joined, and can hold three or more forces. Such a member is a **multi-force member**: its free-body diagram needs, in general, an axial force, a shear force and a bending moment at each cut. The quick "it is a bar, so it is axial" shortcut no longer applies.

- A **frame** is a structure intended to stay in place: a support bracket, a crane arm, a ladder. Its members transfer load while keeping the assembly rigid.
- A **machine** is intended to move and to change a force: a toggle clamp, a pair of pliers, a pulley hoist. A machine multiplies or redirects an input force.

The key skill is the same for both: write a complete free-body diagram for *each* member, not just for the whole assembly, and keep every pin force equal and opposite between the two members it joins.

## Analysing a frame

The procedure mirrors truss work but adds one member-level step:

1. Identify any two-force members and replace each with a single axial unknown.
2. Solve the whole-structure free-body diagram for the support reactions.
3. Dismember at the pins: separate the members, and draw equal-and-opposite pin forces on each.
4. Apply ΣFx = 0, ΣFy = 0 and ΣM = 0 to each member in turn.
5. Use the last equations as checks; every member must balance.

Because a frame member is not axial, taking it apart is not optional. The whole-structure equations alone usually leave the pin forces unknown.

## Worked example: a supported beam frame

A synthetic frame holds an 8 kN downward load. Member AB is a rigid horizontal beam from A = (0, 0) to B = (3, 0), in metres, with a pin support at A. Member BC is a slender link from B = (3, 0) to C = (6, 4), pinned at both ends, so it is a two-force member. The load acts at the midpoint of AB, x = 1.5 m.

**Identify.** AB carries a load between its pins, so it is a multi-force member. BC carries no load between its pins, so it is a two-force member: its force lies along its axis. The link length is √(3² + 4²) = 5 m, with direction cosines (3/5, 4/5) from B toward C.

**Whole structure.** The unknowns are the pin reactions A_x and A_y and the axial link force F (tension positive, along BC). Take the whole assembly and sum moments about A. The 8 kN load gives −12 kN·m. The link force at B acts at (3, 0) with components (−3/5·F, −4/5·F), giving a moment 3·(−4/5·F) − 0 = −12F/5. So −12 − 12F/5 = 0, and **F = −5 kN** (compression).

**Dismember.** With F known, the link pushes on the beam at B with components (3, 4) kN. Force balance on beam AB gives:

- ΣFx = 0: A_x + 3 = 0, so **A_x = −3 kN**.
- ΣFy = 0: A_y + 4 − 8 = 0, so **A_y = +4 kN**.

Both reactions point as expected: the 8 kN load is carried 4 kN by the link (vertical component) and 4 kN by the pin at A (upward), while the link's 3 kN horizontal push is balanced by a 3 kN horizontal reaction at A. Every member now balances, which is the internal consistency check.

## Machines and mechanical advantage

A machine transforms an input force into a different output force. Consider a synthetic toggle clamp: two links AC and BC, each 5 m long, with A = (0, 0) pinned to ground, B = (6, 0) a roller that slides horizontally, and C = (3, 4) the clamping point. A horizontal input force is applied at B, and the clamp presses vertically at C. Both links are two-force members, so each carries only an axial force.

Let the two links share one unknown axial force T, equal by symmetry. Vertical equilibrium at joint C gives the clamp force F_c = (4/5)(T + T) = (8/5)T. Horizontal equilibrium at the sliding joint B gives the input force F_in = (3/5)T, with the slider supplying only a vertical reaction.

Taking magnitudes, the **mechanical advantage** is the ratio of output to input:

F_c / F_in = (8/5·|T|) / (3/5·|T|) = **8/3**.

A 30 N horizontal pull at B therefore produces |T| = 50 N in each link and an 80 N vertical clamping force at C. The advantage 8/3 comes entirely from the geometry: near the fully opened position the links are almost in line and the advantage is much larger, and, conversely, it falls as the clamp closes. The machine never creates energy; a larger output force travels through a proportionally shorter output displacement.

## Common mistakes

- Assuming a member is a two-force member because it looks like a bar; check whether anything loads it between its pins.
- Solving only the whole structure and never dismembering, so the pin forces are never found.
- Forgetting that pin forces are equal and opposite on the two members they connect.
- Dropping the moment equation when checking a multi-force member, which lets a bending-moment error pass.
- Reporting a mechanical advantage without saying which input and output forces it relates, or implying a machine amplifies energy.

## Scope and sources

MIT OpenCourseWare, **2.001 Mechanics & Materials I**, Fall 2006, covers multi-member structures and frames/machines in its equilibrium sequence after planar trusses, and is used here as a link-only scope comparator ([syllabus](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/)). This reading and its synthetic frame and toggle are original; no source text, figure, data or problem is imported. Friction (2.001 lecture 4), space trusses and matrix stiffness analysis are not taught here. Original material is CC BY 4.0 with AI assistance; qualified review and measured workload remain open.