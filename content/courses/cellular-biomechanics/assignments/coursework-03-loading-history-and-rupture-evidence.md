# Assignment 3: loading history and rupture evidence

This open report follows one irreversible synthetic bond population under a prescribed force ramp. It connects a rate law, integrated history, distribution summaries and generated data. All coefficients and trial labels are invented; no measurement of a biological bond is supplied. Retain code, calculations, plots and report locally; selected practice responses do not evaluate the complete simulation or empirical inference.

## Part A: specify the history before the summary

Use initially intact independent bonds conditional on one common law k(F)=k0 exp(F/Fb), with k0=0.05 per second,Fb=4 pN and prescribed per-bond loading rate r=0.8 pN/s. There is no rebinding, catch pathway or load redistribution after rupture. Write F(t)=rt and the survivor differential equation with S(0)=one.

Integrate its cumulative hazard analytically and verify the expression by differentiation. The dimensionless coefficient k0 Fb/r is one quarter. The rupture-force mode is 4ln4, about 5.5451774 pN, and median is 4ln[1+4ln2], about 5.3110457 pN. Derive both from their different definitions, keeping the interior-mode condition visible.

A most frequent force and a median need not have the same value or ordering across parameter choices. Neither is the force at which every bond ruptures. Explain why applying the initial rate as a constant throughout the ramp would give a different survivor law.

## Part B: evaluate survivor and expected count

At force F=8 pN, cumulative hazard is (e²−one)/four, about 1.5972640. The survivor is about 0.20244966. For one hundred initially intact trials under the conditional independent model, expected intact count is about 20.244966.

The expectation is continuous even though an actual count is an integer. Do not round it to an exact count or claim that precisely twenty trials must survive. State the conditional binomial sampling model for that endpoint if the supplied independence and common-rate assumptions hold; a cohort of synthetic bond trials is not automatically an independent sample of cultures or organisms.

For a separate variant double only the loading rate. In the eligible interior-mode regime the mode shifts by Fb ln2=4ln2, about 2.7725887 pN. Demonstrate this from the difference of the logarithms, then verify that the same shift is not automatically the median shift.

## Part C: generate original data with a known reference

Generate rupture forces by transforming independent uniform probabilities with the exact quantile formula. Document the random seed and number of trials. Compare empirical survival at selected force values and empirical median with the analytic references. Quantify sampling uncertainty separately from a numerical integration tolerance.

Document the uniform generator interval and how the inverse transform handles its endpoints. The ideal quantile tends to infinity as its probability approaches one; silently replacing that limit with an arbitrary maximum force changes the generated distribution.

Independently integrate dS/dt=−k(rt)S with a documented method and refine the time step. Compare the result at the same force/time points. A generated histogram can agree with another program because both share an incorrect formula, so retain the derivative/normalization checks as well as the plot.

Choose a finite force observation horizon and record which trials remain intact as right-censored rather than forcing all of them to rupture at that horizon. Compare the observed-event and survival contributions qualitatively with the likelihood/exposure foundation in Statistics. Do not count a censored observation as an event or discard its known survival history.

## Part D: discriminate the selected model

Compare several loading rates and identify which support an interior mode. Within that regime, mode versus log loading rate has slope Fb. Show why a slow boundary-mode condition cannot be fit as though it belonged to the same unconstrained logarithmic line.

Write two alternative reasons that a real dataset might depart from the stipulated law: a different force history per bond and a different rupture mechanism are distinct possibilities. Instrument compliance, multiple bonds, rebinding or competing pathways would need additional equations and evidence. A good fit to one endpoint or one histogram does not uniquely identify a molecular mechanism.

Retain the declared force history, rate/survivor derivation, mode/quantile/count table, generator and integration checks, censoring convention and the comparison across rates. Plot labels must distinguish time, force, density and cumulative probability. The [force-history foundation](../modules/force-history-survival-and-rupture-distributions.md) provides classical bibliographic credit with explicit metadata-only verification. [MIT OCW 20.310J Spring 2015 calendar](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/calendar/) lecture 5 is link-only concept scope. All tasks and values are original and AI-assisted, with no source problem, code or dataset imported. General kinetics, real identification, measured workload and qualified review remain open; the package stays partial and unreviewed.
