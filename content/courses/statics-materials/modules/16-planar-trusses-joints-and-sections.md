# Planar trusses: method of joints, method of sections and static determinacy

**Status:** original ungraded instruction with substantial AI assistance. Trusses, loads and dimensions are synthetic. This reading extends the week-1 equilibrium lessons from a single rigid body to an assembly of members. It is not a structural design, rating or load-capacity instruction.

## Learning objectives

1. State the assumptions of an ideal planar truss and explain why each member then carries only axial tension or compression.
2. Count members, joints and reactions to classify a planar truss as determinate, indeterminate or a mechanism, and explain why the count alone is not sufficient.
3. Find member forces by the method of joints, using a consistent tension-positive sign convention.
4. Find selected member forces directly by the method of sections, and identify zero-force members before calculating.

## The ideal truss and two-force members

A truss is a set of slender straight members joined at their ends. Roof frames, bridges, cranes and the supports that hold lighting rigs or equipment above a laboratory bench are often built this way, because a triangle of bars resists deformation with little material. Analysis starts from an idealized model:

- members are straight and joined at their ends by frictionless pins;
- loads and reactions act only at the joints;
- member weight is either neglected or lumped at the joints;
- deformations are small, so the undeformed geometry is used in the equilibrium equations.

Under these assumptions every member is a **two-force member**. Draw a free-body diagram of one bar: only two forces act on it, one at each pin. For the bar to be in equilibrium, those two forces must be equal, opposite and collinear, so they lie along the bar's axis. A member is therefore either pulled (**tension**) or pushed (**compression**). It carries no shear and no bending in the ideal model. That one fact turns a structure into a set of particle-equilibrium problems at the joints.

Real joints are bolted, welded or glued gusset plates, and real members have weight and are sometimes loaded between joints. Those effects add secondary bending. The ideal model gives the primary axial forces, which are usually the largest, but it is still a model.

**Sign convention.** Assume every unknown member force is tensile, drawn pulling *away* from the joint on the joint's free-body diagram. A positive answer then means tension and a negative answer means compression. Keeping the assumption the same for every member removes the most common error in truss work, which is losing track of which way a force was drawn.

## Counting: determinate, indeterminate or a mechanism

Each pin joint in a plane gives two independent equilibrium equations, ΣFx = 0 and ΣFy = 0. A truss with **j** joints supplies **2j** equations. The unknowns are the **m** member forces and the **r** support reaction components. Compare them:

- **m + r = 2j**: as many unknowns as equations. If the truss is also geometrically stable, it is **statically determinate**: statics alone gives every force.
- **m + r > 2j**: more unknowns than equations. The truss is **statically indeterminate** to degree **m + r − 2j**. Equilibrium is necessary but not sufficient; member stiffness and deformation compatibility supply the missing equations (lesson on truss deformation, week 3).
- **m + r < 2j**: too few members or reactions. The structure is a **mechanism** and cannot resist a general load.

The count is a necessary condition, not a proof of stability. A square of four bars with a fifth bar across one diagonal and three well-placed reactions satisfies m + r = 2j. Move that fifth bar so that it duplicates a side instead, and the count is still satisfied, but the square has no diagonal and folds like a parallelogram. Three reactions that are all parallel, or whose lines of action all pass through one point, also leave the truss free to move however good the count looks. Check the arrangement as well as the number: a stable simple truss can be built by starting from one triangle and adding two new bars for every new joint.

## Method of joints

The method of joints applies particle equilibrium to each pin in turn:

1. Find the support reactions from the equilibrium of the whole truss.
2. Start at a joint with at most two unknown member forces.
3. Write ΣFx = 0 and ΣFy = 0 for that joint, using the member directions as unit vectors and the tension-positive assumption.
4. Move to the next joint that now has at most two unknowns, carrying the solved forces with their signs.

At the end, the last joints give equations with no unknowns left. Use them as checks: they must balance.

## Worked example: a four-panel support truss

A synthetic overhead support truss carries three pieces of equipment. Its bottom chord has joints L0 to L4 at x = 0, 3, 6, 9 and 12 m. The top chord has joints U1, U2 and U3 directly above L1, L2 and L3, at a height of 4 m. Members are the four bottom-chord panels, two top-chord panels (U1U2, U2U3), two inclined end posts (L0U1, U3L4), three verticals (U1L1, U2L2, U3L3) and two diagonals running down toward the centre (U1L2, U3L2). There is a pin at L0 and a roller at L4. A downward load of 10 kN hangs at each of L1, L2 and L3.

**Count.** j = 8 joints, m = 13 members and r = 3 reactions, so m + r = 16 = 2j. The truss is built from triangles, so it is determinate and stable.

**Reactions.** The loads are symmetric, so each support carries half of the 30 kN total: an upward 15 kN at L0 and at L4, and no horizontal reaction.

**Geometry.** Every inclined member spans 3 m horizontally and 4 m vertically, so its length is 5 m and its direction cosines are 3/5 and 4/5.

**Joint L0.** The unknowns are the end post L0U1 (direction (3, 4)/5 from L0) and the chord L0L1 (direction (1, 0)).

- ΣFy: 15 + (4/5)F_L0U1 = 0, so F_L0U1 = −18.75 kN, which is **compression**.
- ΣFx: F_L0L1 + (3/5)F_L0U1 = 0, so F_L0L1 = +11.25 kN, which is **tension**.

**Joint L1.** The bottom chord continues, so F_L1L2 = F_L0L1 = 11.25 kN. Vertically, the vertical U1L1 must hold up the 10 kN load: F_U1L1 = +10 kN (tension).

**Joint U1.** Four members meet here. Two are known (L0U1 = −18.75 kN, U1L1 = +10 kN), leaving the top chord U1U2 and the diagonal U1L2 (direction (3, −4)/5 from U1).

- ΣFy: from the end post, −(4/5)(−18.75) = +15; from the vertical, −10; from the diagonal, −(4/5)F_U1L2. So 15 − 10 − 0.8F_U1L2 = 0 and F_U1L2 = +6.25 kN (tension).
- ΣFx: −(3/5)(−18.75) + F_U1U2 + (3/5)(6.25) = 0, so F_U1U2 = −11.25 − 3.75 = −15 kN (compression).

By symmetry the right half carries the same forces. The last joints serve as checks. At L2, the two diagonals each pull up with (4/5)(6.25) = 5 kN, together balancing the 10 kN load, so the vertical U2L2 carries **zero**. At U2 no load is applied and the top chords are collinear, so U2L2 must be zero there too. Both checks agree.

The pattern is typical of a simply supported truss under downward loads. The top chord is in compression and the bottom chord in tension, like the top and bottom fibres of a sagging beam, and the end posts carry the largest compression. Compression members are the ones to check later for buckling (week 10).

## Method of sections

The method of joints finds every force, one joint at a time. When only one or two members matter, the **method of sections** is faster. Cut the truss into two parts through no more than three members whose forces are unknown, and apply the three equilibrium equations of a rigid body to either part.

Use the same example and cut through the second panel. The cut crosses the top chord U1U2, the diagonal U1L2 and the bottom chord L1L2. Keep the left part, which contains L0, L1 and U1, and draw each cut member force as tension, pulling away from the part.

- **Top chord.** Take moments about L2 at (6, 0), where the diagonal and bottom chord meet, so neither appears in the equation. Counterclockwise is positive. The 15 kN reaction at x = 0 gives (0 − 6)(15) = −90 kN·m, and the 10 kN load at L1 gives (3 − 6)(−10) = +30 kN·m. The top-chord force acts horizontally at height 4 m and gives −4F_U1U2. So −90 + 30 − 4F_U1U2 = 0 and F_U1U2 = −15 kN.
- **Bottom chord.** Take moments about U1 at (3, 4), where the top chord and diagonal meet. The reaction gives (0 − 3)(15) = −45 kN·m, the load at L1 has no lever arm, and the bottom-chord force gives +4F_L1L2. So F_L1L2 = +11.25 kN.
- **Diagonal.** The two chords are horizontal, so ΣFy involves only the diagonal: 15 − 10 − (4/5)F_U1L2 = 0, and F_U1L2 = +6.25 kN.

All three agree with the method of joints. The moment-centre choice is the whole skill: pick the point where two of the three unknown forces intersect, and the third force falls out of a single equation. Finally, check ΣFx for the cut part: −15 + 11.25 + (3/5)(6.25) = 0.

## Zero-force members

Two quick joint rules identify members that carry no force under a given loading:

- If only two non-collinear members meet at an unloaded joint with no support, both are zero-force members.
- If three members meet at an unloaded joint with no support and two of them are collinear, the third is a zero-force member.

U2L2 in the example satisfies the second rule at U2. Zero-force members are not useless. They brace compression members against buckling, keep the geometry stable, and carry load as soon as the loading changes. A load hung at U2 would immediately put force into U2L2.

## Common mistakes

- Drawing member forces in whatever direction looks right, then mixing up the signs; assume tension everywhere instead.
- Treating m + r = 2j as proof of stability without checking for a mechanism or for parallel or concurrent reactions.
- Starting the method of joints at a joint with three or more unknowns.
- Cutting through four unknown members in a section, which leaves more unknowns than the three equilibrium equations can solve.
- Forgetting the support reactions when writing moments for a section.
- Deleting zero-force members from a design because they carry nothing under one load case.

## Scope and sources

MIT OpenCourseWare 2.001 Mechanics & Materials I, Fall 2006, schedules planar trusses in lecture 3 ("Applying the Equations of Equilibrium, Planar Trusses") and is used here as a link-only scope comparator ([syllabus](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/)). This reading and its synthetic truss are original; no source text, problem, figure or data is imported. Friction (2.001 lecture 4) and frames and machines, whose members are not two-force members, are not taught here. Original material is CC BY 4.0 with AI assistance; qualified review and measured workload remain open.
