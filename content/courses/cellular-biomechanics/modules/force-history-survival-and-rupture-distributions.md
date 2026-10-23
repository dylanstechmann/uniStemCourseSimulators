# Force history, survival and rupture distributions

A constant-force off-rate does not directly give the rupture-force distribution during a force ramp. The bond experiences changing hazard as force rises, and survival depends on the whole prior history. This original foundation integrates a stipulated single-bond law, derives a force density and distinguishes its mode from its median. All rates and force scales are invented mathematical inputs, not measurements of a receptor, material or cell.

## Begin with survival under a declared history

Assume one initially intact bond, irreversible rupture and no rebinding or competing pathway. Stipulate off-rate k(F)=k0 exp(F/Fb), with k0>0 in inverse seconds and Fb>0 in force units. Under prescribed nonnegative force history F(t), survival satisfies dS/dt=−k(F(t))S, with S(0)=one.

Therefore S(t)=exp[−integral from zero to t of k(F(s)) ds]. The integral is a dimensionless cumulative hazard. An off-rate is not a probability, and its product with a finite time need not be a probability either. For constant force the solution is exponential in time; that shortcut cannot retain the same rate while force changes substantially.

A Bell-type single-barrier interpretation sometimes writes Fb=kBT/xb under its chosen barrier-distance assumption. Here Fb itself is a supplied model coefficient. The selected law does not describe catch bonds, load-sharing clusters or an identified energy landscape merely because its parameters are positive.

## Convert a linear ramp into a force law

For F(t)=r t with r>0, change variables from time to force. The cumulative hazard and survivor are

$$H(F)=\frac{k_0F_b}{r}\left[e^{F/F_b}-1\right],\qquad S(F)=e^{-H(F)}.$$

The rupture-force density is pF(F)=k(F)S(F)/r. Its factor one/r comes from the time-to-force change of variables. Integrating the density over nonnegative force gives one because S(0)=one and S tends to zero as the unbounded ramp continues in this ideal model. A finite observation horizon instead leaves a surviving, right-censored fraction.

## Mode and quantile answer different questions

Differentiate log pF: its force derivative is 1/Fb−k(F)/r. An interior mode therefore satisfies k(F)=r/Fb, giving

$$F_{mode}=F_b\ln\left[\frac r{k_0F_b}\right]$$

when r>k0 Fb. If r is smaller or equal, the maximum is at the boundary F=0; a negative algebraic interior candidate is not a negative physical rupture force.

For quantile q, solve S(Fq)=1−q:

$$F_q=F_b\ln\left[1+\frac r{k_0F_b}[-\ln(1-q)]\right].$$

At q=one half this is the median. The density's highest point and the location splitting cumulative probability in half need not coincide, and neither is an observed guarantee for one bond.

## Worked and distinct rehearsal

Choose k0=0.1 per second,Fb=2 pN and r=1 pN/s. The dimensionless coefficient k0 Fb/r is 0.2. Mode is 2ln5, about 3.2188758 pN, while median is about 2.9928680 pN. These different summaries arise from the same specified distribution.

For the rehearsal use k0=0.2,Fb=3 and r=1.2 in corresponding units. At F=3 pN, cumulative hazard is (e−one)/two, about 0.85914091, and survival is about 0.42352577. Mode is 3ln2, about 2.0794415 pN, while median is about 2.6092251 pN. Their ordering is different from the worked example and is not a universal rule.

Doubling only the rehearsal loading rate to 2.4 gives mode 3ln4, about 4.1588831 pN, and median about 3.9832843 pN. At the original rate the 90th percentile is about 5.1710683 pN. For a separate slow rate 0.3 pN/s, the mode is the zero-force boundary because r<k0 Fb=0.6 pN/s.

## Verify history and identification

Compare the integrated hazard with direct numerical survival integration and refine the time step. Generate original synthetic rupture forces by inverse transformation of uniform probabilities and compare empirical survival or quantiles with their exact references, including sampling uncertainty. Numerical agreement checks the generator under the supplied model, not an empirical bond law.

Across eligible interior modes, force versus ln(r) has slope Fb under this model. One mode at one loading rate leaves parameters confounded, and a boundary-mode regime cannot be fit as though every mode obeys the interior logarithm. Machine loading rate also need not equal per-bond rate when link compliance or load sharing changes the history.

[MIT OCW 20.310J Spring 2015 calendar](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/calendar/) lecture 5 supplies link-only mechanochemical-rate scope. Classical bibliographic credit: G. I. Bell, *Models for the specific adhesion of cells to cells* (1978), [PMID 347575](https://pubmed.ncbi.nlm.nih.gov/347575/), DOI 10.1126/science.347575. Metadata was verified through NCBI; full paper text was not examined. The selected law and calculations here are self-contained original AI-assisted instruction, with no source prose, figure, problem or data imported. General bond kinetics, empirical identification and qualified review remain open; the course stays partial and unreviewed.
