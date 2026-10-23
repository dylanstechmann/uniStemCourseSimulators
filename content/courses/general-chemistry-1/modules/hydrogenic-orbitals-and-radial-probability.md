# Hydrogenic orbitals and radial probability

## What this model describes

The earlier atom reading counts electrons and photons; the configuration primer explains trends without calculating an orbital probability. Here a single electron moves in an ideal point-nucleus Coulomb field. Electron–electron repulsion, finite nuclear size, relativity and environmental interactions are omitted. Those omissions matter: a hydrogenic formula cannot be applied to a many-electron atom merely by inserting its atomic number. We use normalized scales E* and a*, so energy, length and probability can be audited without importing a table of measured spectra. A positive integer Z is the nuclear-charge parameter of this model, not a fitted shielding correction.

A stationary orbital is a spatial amplitude. Its squared modulus gives probability density per volume, not the trajectory of a small particle. Multiplying an entire orbital by minus one changes no density. Relative signs in a superposition can change interference, however, which is why amplitude and probability cannot be exchanged in bonding arguments. A negative amplitude is not a negative probability. A spherical orbital density still produces a nonuniform probability of finding the electron at different radii because shells have different volumes.

## Quantum numbers, counts and nodes

The bound-state labels obey n=1,2,…; l=0,…,n−1; and m=−l,…,l. For a specified l there are 2l+1 spatial orbitals. Summing those counts at fixed n gives n² orbitals and, after allowing two opposite spin states per orbital, capacity 2n². Capacity is a counting statement, not the ground-state filling order of every real atom. A hydrogenic orbital has l angular nodes and n−l−1 radial nodes, excluding the origin and asymptotic vanishing. Thus a 3p orbital has one radial and one angular node; the p subshell has three orbitals. These counts distinguish one orbital, a subshell and an entire shell.

In this ideal model E_n/E*=−Z²/n². Energies are negative relative to a separated electron and nucleus. An emission from n_high to n_low releases positive photon energy Z²(1/n_low²−1/n_high²)E*. Ionization from n instead requires Z²E*/n². Photon energy is a difference of levels, not the absolute value of whichever level happens to appear first. No physical wavelength follows until E* and the electromagnetic conversion constants are specified consistently.

## Derive the radial measure

Let r denote distance in units a*. For a normalized 1s orbital, the radial probability density is p(r)=4Z³r²exp(−2Zr), for r≥0. It is a probability per unit normalized radius: integrating over dr must give one. The factor r² comes from spherical-shell volume. The density per volume is largest at the origin, whereas p(r) is zero there and has its maximum at r=1/Z. These statements answer different questions and are compatible.

Differentiating log p away from zero gives 2/r−2Z, establishing that mode. Integrating r p(r) gives mean radius 3/(2Z), which differs from the mode because the distribution has a tail. Direct integration also gives the cumulative probability

P(r≤R)=1−exp(−2ZR)[1+2ZR+2Z²R²].

Check the endpoints: P(0)=0 and P tends to one at large R. Differentiating this cumulative expression recovers p(R). A cumulative probability must stay between zero and one and increase with its radius. Those checks catch an omitted shell-volume factor more effectively than extra displayed decimals.

## Separate worked example

For Z=1, the 1s mode is 1a* and mean is 1.5a*. The probability inside one a* is 1−5exp(−2), approximately 0.323324. A 4→2 transition emits 3E*/16; ionizing from n=2 requires E*/4. Thus the emission and ionization energies differ even though they both involve the second level. For a 4d orbital, l=2, radial nodes equal one and angular nodes equal two; the whole d subshell contains five spatial orbitals.

## Rehearsal and interpretation

Use Z=2, a 3→2 transition, and the 1s radial distribution. Derive the positive photon energy, the n=2 ionization energy, the mode and mean radius, and the probability inside the modal radius. The emission is 5E*/9 and ionization requires E*. The radial mode and mean are 0.5a* and 0.75a*, but the probability inside the mode is still 1−5exp(−2). Scaling the radius changes the physical length while retaining this dimensionless cumulative probability. This is a model scaling result, not evidence that all atomic sizes can be predicted this way.

Explain separately what happens when a global orbital sign changes, and when two amplitudes with different relative signs are combined. Retain derivations, a normalized radial plot and a count table locally. Selected browser checkpoints do not evaluate the plot or derivation. The source-map comparison uses MIT OCW 5.111SC Fall 2014 Unit I as a link-only scope reference; all examples here are original and AI-assisted. General many-electron wavefunctions, spectroscopy corrections and measured atomic properties remain outside this bounded foundation.
