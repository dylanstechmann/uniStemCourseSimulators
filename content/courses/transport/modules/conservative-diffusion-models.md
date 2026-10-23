# Conservative diffusion models: derive the cells, faces and checks

**Status:** original ungraded instruction developed with substantial AI assistance. Concentrations, meshes and transport coefficients are synthetic. This reading connects continuum balances to a small discrete model, so a solver can be checked against physics and mathematics separately. Use Programming for general solver implementation; the focus here is the transport formulation.

## Integrate the balance over a cell

For a one-dimensional medium of constant cross-sectional area A, species balance is ∂c/∂t=−∂j/∂x+s, with concentration c, molar flux j and volumetric source s. Integrating over a cell of width Δx gives

AΔx dc_i/dt=A j_(i−1/2)−A j_(i+1/2)+AΔx s_i.

The concentration is a cell average in this formulation. A face flux is positive to the right. The right face of one cell is the left face of its neighbor, so use one shared numerical face value with opposite balance signs. If two cells independently calculate inconsistent values for their common face, internal transfer no longer cancels and the scheme can create or destroy mass.

For constant diffusivity D and uniform cell spacing, an internal face approximation is j_(i+1/2)=−D(c_(i+1)−c_i)/Δx. Substitute it to obtain the familiar second difference at an interior cell. The area cancels from the concentration update, but it still belongs in the total amount M=AΔx sum c_i. Omitting that geometric factor changes the units of a reported mass balance.

## Boundary conditions determine the first and last rows

A zero-flux boundary imposes its face flux directly as zero. For three cells with no sources, the rate vector is D/Δx² times [c_2−c_1,c_1−2c_2+c_3,c_2−c_3]. Summing these entries gives zero, so the semi-discrete total amount is conserved.

A fixed concentration at a boundary face is different from a fixed value at the first cell center. With a cell center half a cell width from the face, the left flux is 2D(c_L−c_1)/Δx. The left update becomes D/Δx²(2c_L−3c_1+c_2). Similarly the right row is D/Δx²(c_(n−1)−3c_n+2c_R). Using a full-cell distance at a half-cell boundary introduces an extra resistance and solves a different discretization.

Always draw or describe where unknowns and boundaries lie. A node-centered grid has a different boundary layout from this cell-centered grid. Neither label by itself specifies the equations; the geometric distances and balance volumes do.

## A steady reference catches boundary mistakes

Take a domain of length L=0.003 m divided into three cells, D=10^−9 m²/s, fixed boundary concentrations c_L=1 and c_R=0 mol/m³, and no reaction. The exact continuum steady profile is c(x)=1−x/L. At cell centers x=0.0005,0.0015,0.0025 m, its values are [5/6,1/2,1/6]. Because the profile is linear, each cell average equals its center value.

The face flux is D(c_L−c_R)/L≈3.3333333×10^−7 mol/(m² s). Substituting the center values into both half-cell boundary formulas and internal formulas produces that same flux. Each cell's inflow equals outflow. A solver that uses the wrong boundary distance can still have a tiny algebraic residual for its own incorrect matrix, so this independent flux/reference comparison matters.

With nonlinear profiles, a pointwise center value need not equal an exact cell average. A manufactured-solution check should compare like quantities or account for that difference. Grid refinement can reveal convergence behavior, but it cannot repair inconsistent definitions of the unknown.

## Explicit steps have positivity and stability limits

For the three-cell no-flux system, forward Euler with r=DΔt/Δx² uses the old vector in every component. From c^0=[1,0,0] and r=0.25, the next vector is [0.75,0.25,0], and the following vector is [0.625,0.3125,0.0625]. Both remain nonnegative and preserve the sum one.

At an interior cell the coefficient of its old concentration is 1−2r and each neighbor receives weight r. Nonnegative weights are sufficient for positivity when 0≤r≤0.5 in this source-free uniform stencil. The endpoint pulse [1,0,0] happens to give nonnegative first steps even at r=0.6; this does not prove the update preserves nonnegativity for all inputs. A separate center pulse [0,1,0] immediately gives [0.6,−0.2,0.6] at r=0.6, preserving the sum while producing a negative concentration. One acceptable trajectory does not establish a positivity-preserving scheme.

The half-cell Dirichlet boundary row has self-coefficient 1−3r rather than 1−2r, so its simple nonnegative-weight condition is r≤1/3. Do not transplant the interior positivity bound to every boundary scheme. Absolute stability, positivity and accuracy are distinct tests; an adequate condition for one does not automatically establish the others.

## Reaction terms belong in both local and global ledgers

For a first-order sink s_i=−k c_i, the continuous total with no-flux boundaries satisfies dM/dt=−kM. Under explicit Euler, internal face terms still cancel and M_new=(1−kΔt)M_old. The interior concentration coefficient becomes 1−2r−kΔt, giving the sufficient positivity condition 2r+kΔt≤1 for this uniform no-flux formulation.

For a constant zero-order sink, subtracting the same amount forever eventually produces negative concentrations. That is a failure of the declared uptake law at depletion, not a reason to clip negative numbers silently and still claim the original equation was solved. If depletion changes the model, specify the change and recompute the ledger. A conservation correction that hides an inconsistent source term is not a verification method.

## Implicit solving changes the numerical task

Backward Euler evaluates diffusion/reaction at the new state and produces a linear system for these linear laws. The matrix has diagonal and neighbor structure determined by the same cell and boundary derivation. Use a numerical solver appropriate for that structure, then inspect both the linear residual and physical balance. An accurately solved matrix can still represent the wrong boundary model.

Large implicit steps can be stable while smoothing the transient too much. Compare a known transient solution or refine the time step. Independently refine the spatial grid while keeping the domain, material parameters and boundary conditions fixed. A two-dimensional table of spatial/time resolution helps separate the two discretization errors.

## Rehearsal and report

For D=2×10^−9 m²/s and Δx=0.0001 m, compute the largest explicit no-flux interior step under r≤0.5. With k=0.1 s^−1, recompute the sufficient combined positivity step. Starting from [0,1,0], perform one no-flux diffusion step with r=0.2 and verify both total and minimum value.

For a separate fixed-boundary problem, take L=0.004 m, four cells, c_L=2 and c_R=0 mol/m³, D=2×10^−9 m²/s. Derive the steady center values and compare every face flux. Your report should show cell geometry, face directions, source terms, matrix/update equations, units, independent references, refinement and explicit failure evidence.

The [MIT OCW 20.330J Spring 2007 syllabus/calendar](https://ocw.mit.edu/courses/20-330j-fields-forces-and-flows-in-biological-systems-spring-2007/pages/syllabus/) is a link-only comparator for conservation, diffusion and boundary-value reasoning. This original lesson covers a narrow one-dimensional finite-volume construction, not general CFD, mesh generation or experimental validation. No external code, problem or dataset was imported. Original material is CC BY 4.0 with AI assistance; qualified review and measured workload remain open.
