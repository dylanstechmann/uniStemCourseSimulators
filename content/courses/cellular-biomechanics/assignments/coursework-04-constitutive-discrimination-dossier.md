# Assignment 4: constitutive discrimination dossier

This cumulative open report asks how a second observation can distinguish models that agree on an earlier test. It combines tensor elasticity, membrane force–radius inference and loading-history evidence with the existing mechanotransduction/design readings. All coefficients and outcomes are supplied synthetic models. Retain derivations, code, plots and report locally; selected checkpoints do not grade the entire dossier or establish any real biological mechanism.

## Part A: two materials that agree in one loading direction

Model A has aligned orthotropic normal block (6,2),(2,5) and engineering shear coefficient three kPa. Model B has normal block (6,2),(2,8) and shear coefficient 1.5 kPa. Verify positive elastic energy for both.

At prescribed engineering strain e=(0.01,0,0), both predict stress (0.06,0.02,0) kPa. That agreement cannot select one model. It identifies the two coefficients actually excited by this test and leaves the others unresolved under this model family.

For a separate biaxial strain e=(0.01,0.01,0), predicted yy stress is 0.07 kPa for A and 0.10 kPa for B. For a separate pure engineering shear gamma=0.02, shear stress is 0.06 kPa for A and 0.03 kPa for B. Keep these separate loading conditions distinct rather than silently combining their strains.

Calculate full stress and work for each comparison, then show which predicted differences survive a stated synthetic measurement resolution. Resolution alone is not a complete uncertainty model or evidence that the boundary conditions could be achieved in a cell. The purpose is to identify a discriminating prediction before interpreting an experiment.

## Part B: two membranes that agree in force

Use the long-tube, fixed-tension idealization. Model A has kappa=90 pN nm,sigma=0.05 pN/nm. Model B has kappa=45 pN nm,sigma=0.10 pN/nm. Their products agree, so both predict extension force 6pi pN.

The radii differ: A predicts 30 nm and B predicts 15 nm. Reinsert each pair into the energy-minimum and force relations. Explain why adding an independent radius could discriminate the models under those assumptions, while repeating the same ideal force measurement with unlimited numerical precision could not.

A real intervention might change the reservoir condition, cortex coupling or another omitted contribution. Do not interpret the two mathematical alternatives as two established biological states. If a second observation lies outside the supplied models, report that possibility rather than forcing a selection between them.

## Part C: force-history predictions and alternative explanations

Use the selected off-rate/ramp model to construct two parameter choices that agree on one mode at one loading rate but predict different eligible modes at another rate. Keep the interior-versus-boundary condition explicit. Derive or calculate the survivor curves, not only the most frequent force.

Compare a changing loading rate with a changing bond coefficient and state what extra information would separate them. A machine's imposed displacement speed need not define a unique per-bond force ramp. State the mechanical connection that would be required, or leave that inference unresolved.

Generate a small original synthetic comparison from one declared alternative and examine how sampling variation can obscure a theoretical difference. Disclose its source as a simulation rather than measured data, and separate a model-discrimination demonstration from inference about an actual cell population.

## Part D: connect mechanical and biological evidence

Write an evidence table connecting each candidate mechanism to its observable, controlled boundary conditions, comparison and remaining alternative. Use the earlier stiffness/ligand-density and mechanotransduction readings to identify confounders that could alter a biological response without changing the mechanical parameter of interest.

Distinguish an inferred constitutive coefficient, a predicted mechanical response and a signaling interpretation. A traction or pathway readout does not uniquely identify membrane rigidity, passive elasticity or bond kinetics without a connecting model. Shared prerequisites in Statistics and Programming support inference and simulation checks; they do not replace the domain-specific boundary conditions here.

Retain the two elasticity comparisons, two membrane predictions, a force-history discrimination example and the final evidence table. Give diagrams and plots a plain-text description, units, scales and input provenance. Explain one deliberately insufficient comparison and why a more precise number would still leave it insufficient.

[MIT OCW 20.310J Spring 2015 calendar](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/calendar/) supplies link-only tensor/membrane/mechanochemical scope. All examples, model comparisons and tasks are original and AI-assisted; no source problem, figure, code or data is imported. Broad molecular/tissue theory, actual experimental competence, qualified review and measured workload remain open; this course stays partial and unreviewed.
