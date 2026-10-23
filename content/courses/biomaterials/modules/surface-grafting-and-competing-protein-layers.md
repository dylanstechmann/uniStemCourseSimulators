# Surface grafting and competing protein layers

## Chemistry at the exposed interface

Bulk modulus and nominal chemical composition do not specify the interface that a cell encounters. A surface can reconstruct, bind water, acquire proteins or lose a coating while its underlying material retains nearly the same bulk stiffness. The existing surface-characterization and adsorption readings establish that distinction. Here we add a bounded reaction and competitive-layer model to connect modification, accessibility and time-dependent occupancy. All surface sites, rates and proteins are fictional normalized teaching quantities, not a fabrication protocol.

A modification changes accessible chemical groups through a declared reaction or attachment mechanism. Covalent grafting requires compatible reactive groups and can leave unreacted sites; physical adsorption may be reversible; a tethered chain can mask nearby area even when its attachment point occupies only one site. Surface density, accessible ligand density and total material amount are therefore different quantities. A contact-angle change can support a changed wetting response without uniquely identifying a chemical group or proving that an attached ligand remains biologically accessible.

Use a simple accessible-graft fraction g(t)=g_max[1−exp(−kt)] with initially zero grafting and a fixed accessible ceiling g_max. This solves dg/dt=k(g_max−g). It assumes one effective rate, no loss and no changing transport limitation. For g_max=0.8 and k=ln2 per time unit, g(1)=0.4 and g(2)=0.6. The ceiling is less than one by stipulation; it might represent inaccessible area in a teaching interpretation, not a measured reaction yield. Fitting the curve alone cannot identify which microscopic process created that ceiling.

## A wetting measurement is not a full chemical assay

For an explicitly ideal smooth area-composite model, write cos(theta)=g cos(theta_g)+(1−g)cos(theta_base). With component angles 60 and 120 degrees, cos(theta)=g−0.5. At g=0.6 the predicted angle is arccos0.1, approximately 84.2608 degrees. The cosine, rather than the angle itself, is area-weighted in this stipulated expression. State its assumptions before interpreting the arithmetic.

Real roughness, hysteresis, contamination and reconstruction can invalidate that simple area relation. A single angle does not separately determine coverage, component chemistry and roughness. Pair an appropriate surface-sensitive chemical measurement with a hydrated accessibility measurement when assessing those claims. Neither measurement alone establishes cell function. This is a distinction between observables and mechanisms, not an invitation to infer an unmeasured molecular structure from an attractive graph.

## Competing finite sites

Let theta_A and theta_B be fractions of a common protein-binding site population, with theta_0=1−theta_A−theta_B free. A reversible two-species model is

dtheta_A/dt=a theta_0−d_A theta_A,

dtheta_B/dt=b theta_0−d_B theta_B.

Here a and b include fixed bulk concentrations times association rates; d_A and d_B are desorption rates. They all have inverse-time units. Bulk depletion, conformational changes, multilayers, irreversible binding and changing site populations are omitted. At the boundaries theta_A=0 or theta_B=0 the corresponding derivative is nonnegative; at theta_0=0 total occupancy decreases when desorption rates are positive. Thus the physical occupancy triangle is invariant under the stated continuous equations.

At equilibrium, theta_A=(a/d_A)theta_0 and theta_B=(b/d_B)theta_0, with theta_0=1/[1+a/d_A+b/d_B]. A higher association input does not by itself guarantee larger equilibrium coverage, since retention also depends on desorption. Nor does an equilibrium ratio specify the transient path from an initially preadsorbed layer.

## Worked comparison and rehearsal

In a separate equal-desorption example, set a=b=d_A=d_B=1. Starting empty, total occupancy obeys theta'=2−3theta and each species occupies (1−exp(−3t))/3. Their fractions remain equal for that symmetric initial state. Symmetry supplies a useful independent check, but it disappears when initial loading or rates differ.

For the rehearsal, use a=1, b=2, d_A=1 and d_B=2. All three equilibrium fractions equal one third. Starting instead at theta_A=0.8 and theta_B=0, free fraction is 0.2 and initial slopes are −0.6 and +0.4 per time unit. A initially decreases while B increases even though A does not vanish at equilibrium. The deviation matrix is [[−2,−1],[−2,−4]], with eigenvalues −3±sqrt3. Both decay rates are stable; a model for replacement is therefore more informative than ranking proteins by concentration alone.

For a deliberately stipulated masking rule, accessible ligand fraction is L=g theta_0. At the rehearsal equilibrium and g=0.6, L=0.2. This rule is an additional model assumption, not a universal statement that every adsorbed protein blocks every ligand. Compare total grafting, protein occupancy and ligand access separately. Retain derivations, physical-domain checks and a time-course sketch locally; browser checkpoints assess selected values. MIT OCW 3.051J Spring 2006 surface chemistry/modification and protein-interaction lecture topics are link-only comparators. All instruction is original and AI-assisted; real surface chemistry, corrosion, brush conformations and in-vivo layers remain broader than this model.
