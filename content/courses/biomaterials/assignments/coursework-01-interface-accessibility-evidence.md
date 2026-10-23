# Assignment 1: interface-accessibility evidence

## Design question and evidence contract

Investigate why a larger grafted fraction need not deliver a proportionally larger accessible ligand signal after a protein layer forms. Use a fictional surface with accessible graft ceiling g_max=0.9 and rate k=ln2 per normalized time. The measured quantities and rates are stipulated teaching inputs. They are not instructions to modify a surface or evidence of compatibility with actual cells.

Prepare a reaction/occupancy derivation, a wetting calculation, a time-course figure and a mechanism-versus-observable table. Save the complete packet locally. Browser checks assess selected numeric responses and interpretations, rather than evaluating your code, drawing or materials design. Use the surface foundation and existing characterization reading to connect chemical claims to the measurements that would be needed to test them.

## Task A: reaction ceiling and wetting model

From dg/dt=k(g_max−g) with g(0)=0, derive g(t)=0.9[1−exp(−kt)]. At t=2, g=0.675. Calculate the time to reach g=0.8 and show that it is longer than two units. Also explain why the model cannot reach a target above 0.9, regardless of how long the surface is allowed to react. A numerical solver that returns a finite time above the ceiling has failed the model domain.

Use the stipulated ideal smooth-composite relation cos(theta)=g cos60°+(1−g)cos120°. At t=2, cos(theta)=0.175 and theta is approximately 79.9213 degrees. Compare this with the incorrect procedure of averaging 60 and 120 degrees directly. State the surface assumptions required by the cosine rule. Identify at least two mechanisms, such as roughness or contamination, that could change the observed angle without proving a changed covalent graft density.

## Task B: solve a distinct competing-layer model

Let protein A have association input a=2 and desorption d_A=1; protein B has b=1 and d_B=3. Use the same common-site model as the foundation. Derive equilibrium from the two rate equations and the site balance. The equilibrium fractions are theta_0=0.3, theta_A=0.6 and theta_B=0.1. Check that they are nonnegative and sum to one, then substitute them into both original rate equations.

Begin a separate transient at theta_A=0.2 and theta_B=0.5. Free fraction is 0.3. Initial slopes are +0.4 for A and −1.2 for B. Explain how this can occur without either equilibrium fraction being inferred from the initial slope alone. Derive the affine system and its deviation matrix; a numerical time course must remain inside the occupancy triangle within its numerical accuracy. If an explicit time step produces a negative fraction, refine the step and compare against the continuous equations rather than presenting the negative fraction as a material prediction.

## Task C: connect grafting and accessibility

Freeze graft fraction at its t=2 value while the protein layer reaches equilibrium, and use the deliberately declared masking rule L=g theta_0. The accessible fraction is 0.2025. Compare it with the graft fraction and explain the difference in denominators and physical meaning. Neither a high graft count nor a low contact angle alone identifies L under an unknown layer.

Now propose a second fictional surface with a different graft fraction and protein rates, and show a case in which more grafting yields less accessible L. Derive the rates and site balance for your own example. This is a counterexample within a stipulated model, not a claim that all real protein layers obey one masking rule. Explain what hydrated ligand-binding measurement would test the access claim and what independent surface-sensitive measurement would test the modification claim.

## Task D: model discrimination

Compare three candidate explanations for a low cell-binding readout: little grafting, protein masking and reduced cell-receptor availability. Place each in a causal diagram from modification to interface to cell measurement. Specify one observation that would distinguish at least two explanations and one that would leave them confounded. Avoid identifying a chemical group solely from an angle or a protein conformation solely from equilibrium coverage.

A usable packet includes the ceiling/domain analysis, wetting calculation with explicit assumptions, equilibrium and initial-slope checks, a physical transient plot, the graft-versus-accessibility ledger and the discriminating-evidence table. Continuous checkpoint entries request three significant figures; retain unrounded values between steps. The original examples are AI-assisted and synthetic. MIT OCW 3.051J Spring 2006 surface-modification and protein-interaction lecture topics are link-only comparators; no source text, experiment, image or dataset is reproduced. Qualified materials review, real measurements and measured workload remain open.
