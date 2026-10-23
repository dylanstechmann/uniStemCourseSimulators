# Assignment 2: constraint reactions and release evidence

This open report develops a constrained acceleration solve, its work ledger and the difference between a bilateral equality and a nonadhesive wall. The supplied generalized masses and inputs are invented. They are not a contact calibration, force limit or machine specification. Keep diagrams, equations, code and report locally; selected browser responses do not grade the complete analysis.

## Part A: solve a distinct coupled contact state

Use constant generalized mass matrix M with rows (4,1),(1,1). Let q1>=0 be the allowed side of a stationary flat wall, with q1=v1=0 at the instant considered. Choose unit normal A=(1,0) pointing into the allowed region and input tau=(-2,3). There are no other generalized forces in this frozen model.

Write M a=tau+A'lambda and A a=0. Solve the full three-by-three block system before simplifying it. The active solution is a1=0,a2=3 and lambda=5. Verify both original dynamic rows and the acceleration constraint. M is symmetric positive definite, and the independent normal row makes the Schur scalar positive.

Normal mobility is A M^-1 A'=1/3, so effective normal mass is three in the declared generalized units. Derive the same reaction from the free normal acceleration and that mobility. Matching the block and reduced solutions checks signs and matrix placement; it does not establish that this frozen model describes a complete robot.

## Part B: change the input and check admissibility

For a separate input set tau=(5,1), keeping the same boundary state and matrix. An equality solve would require a negative multiplier. For a nonadhesive unilateral wall that branch is inadmissible. The free acceleration is (4/3,-1/3), directed into the allowed region in its normal component, so this instant uses release rather than a tensile wall force.

Show the rejected multiplier and substitute the released acceleration into the unconstrained equation. Explain why that rejection depends on the wall assumption: a bilateral mechanical linkage could support either multiplier sign under its own physical model. Do not impose nonnegative reaction on every equality constraint merely because the same algebra is used.

Describe how the branch decision would differ if initial normal velocity were already inward rather than zero. The acceleration-level model alone does not resolve an impact or erase an inconsistent velocity. No restitution coefficient, friction law or impulse model has been supplied, so do not manufacture an impact trajectory.

## Part C: workless reaction and curved geometry

For the compatible flat-wall state, reaction power is lambda A v=0. Compare this with its nonzero effect on acceleration. A workless force can redirect motion and alter coupled accelerations without adding energy. If the boundary moves, or friction or compliance is added, a different power ledger is needed.

Use a separate point-mass check on a circle of radius two meters with unit mass, speed three m/s and no other force. At the boundary the inward acceleration magnitude is v²/R=4.5 m/s². Derive it by differentiating the circle constraint twice, including Adot v, and verify zero reaction power. State why freezing the normal derivative would lose the centripetal term.

Implement a short compatible curved-constraint trajectory and compare constraint residual, velocity compatibility and energy as the time step is refined. If you project positions or velocities numerically, identify the projection method and check its effect on energy. A small position residual after projection does not prove the original differential equations or work balance were satisfied accurately.

## Part D: rank and model boundaries

Construct a deliberately redundant constraint set by repeating the same normal row. Show why A M^-1 A' becomes singular and how the underlying independent constraint can still be represented once. Do not solve a singular system by silently assigning a unique physical meaning to arbitrary multipliers from a numerical fallback.

Relate the analysis to hybrid position-force control: motion directions and constraint-force directions answer different objectives. A commanded force does not establish an admissible contact branch or a stable dynamic loop. The report needs the state, normal convention, original equations and branch evidence before discussing a controller.

Retain block/Schur calculations, free/active/released comparisons, rank diagnosis, power identity and refinement results. [Modern Robotics 8.7](https://modernrobotics.northwestern.edu/nu-gm-book-resource/8-7-constrained-dynamics/) supplies link-only workless-constraint context. All examples and tasks are original and AI-assisted; no source mechanism, problem or code is imported. General impact/friction/contact integration, physical validation, measured workload and qualified review remain open; this package stays partial and unreviewed.
