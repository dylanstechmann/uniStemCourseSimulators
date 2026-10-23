# Assignment 1: electronic-model evidence

## Purpose and submission contract

Construct a paper or computational evidence packet that connects quantum-state counting, photon-energy differences and radial probability. Use the hydrogenic companion's definitions, not a periodic-trend arrow as a substitute for a probability calculation. The model contains one electron and a point nucleus with charge parameter Z=3. All lengths and energies use the stipulated a* and E* scales; no real element, measured spectrum or experimental protocol is specified.

Save a derivation, calculation sheet, two plots and a short limitations discussion locally. Browser responses check selected quantities only. There is no upload, institutional grade or automatic evaluation of plots, reasoning or code. Organize the packet so someone can trace each conclusion from the original equation to the numerical check without reading an unlabelled calculator dump.

## Task A: count allowed states

Build a table for n=1 through 4. List the allowed l values, number of m states within each subshell, shell orbital total and spin-inclusive capacity. Justify the difference between one spatial orbital, a subshell and a shell. For the 4d state, give radial and angular node counts and the number of d spatial orbitals. Explain why a shell-capacity total does not specify the actual ground-state configuration of a many-electron atom.

Use a separate consistency check: sum 2l+1 over allowed l and compare it with n². Do not count the two spin choices a second time when you report spatial orbitals. Your report should make an incorrect 4d claim of four angular nodes visibly inconsistent with the definition of l, rather than simply replacing it with a correct integer.

## Task B: signed levels and positive photons

For Z=3, calculate the energy of n=4 and n=2, the energy emitted by a 4→2 transition, and the energy required to ionize from n=4. The emitted photon is 27E*/16, whereas ionization from the fourth level requires 9E*/16. A level energy is negative relative to the separated reference; the photon energy and required ionization input are positive. Draw the reference zero and both bound levels on a signed energy axis.

Check the difference two ways: subtract the signed levels and use the difference-of-reciprocal-squares formula. Then consider a proposed transition with the same initial level but final n=1. Without importing a wavelength table, determine whether its photon energy would be larger or smaller. Explain what additional dimensional information would be required to turn E* into a wavelength and why the normalized exercise cannot supply a real spectral identification.

## Task C: density versus radial distribution

Derive p(r)=4Z³r²exp(−2Zr) from the stipulated 1s model and normalize it by integration. Differentiate to locate its positive-radius maximum; calculate its mean radius by a separate integral. For Z=3 the mode is a*/3 and mean is a*/2. Plot the radial density and its cumulative probability over a domain whose tail omission you quantify. Label the ordinate as probability per normalized radius, rather than probability per volume.

Calculate the cumulative probability inside R=0.5a*. It is 1−8.5exp(−3), approximately 0.576810. Verify it by evaluating the cumulative formula and independently integrating the radial density. If using numerical quadrature, refine the grid or tolerance and distinguish quadrature error from truncating the plotted radial range. Check zero and infinite-radius limits symbolically. A numerical value greater than one is a failed probability ledger, not a rare physical outcome.

## Task D: diagnose competing explanations

A hypothetical student reports that the electron's most probable radial location must be zero because the 1s density per volume is largest there. Identify the different measures in that claim and your plot. Another reports a negative probability after changing the orbital's global sign. Explain which mathematical operation is missing. Finally, compare Z=1 and Z=3 curves after rescaling the horizontal coordinate to Zr. State which features coincide under the ideal model and which dimensional lengths differ.

Use these diagnoses to separate a model assumption from an arithmetic mistake. Hydrogenic scaling excludes electron–electron interaction; a wrong shell-volume factor violates the very model being used. No calculation here establishes a many-electron atomic radius, a measured ionization energy or an actual electron trajectory.

## Completion criteria

A usable packet includes the state-count table, signed energy diagram, normalized radial and cumulative curves, one independent integral check, a finite numerical-error discussion and explicit model omissions. Continuous checkpoint entries use three significant figures in the named normalized scales; exact state and node counts are whole numbers. Keep unrounded intermediate values for final calculations. MIT OCW 5.111SC Fall 2014 Unit I is a link-only scope comparator; every problem and number in this assignment is an original synthetic construction with substantial AI assistance.
