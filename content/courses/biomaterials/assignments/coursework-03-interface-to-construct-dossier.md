# Assignment 3: interface-to-construct dossier

## Integrate distinct constraints

Build a fictional construct dossier that connects interface access, mechanics, transport and functional evidence. The purpose is to explain a feasible trade-off and its failure modes, rather than select a real implant or repeat the existing two-time-point scaffold project. Use dimensionless design variables and normalized constitutive scales unless a unit is explicitly supplied. Every candidate, response and threshold below is stipulated teaching input.

Retain the derivation, constraint diagram, sensitivity calculations and evidence plan locally. Browser checkpoints assess selected quantities only. They do not establish a valid design, clinical performance or the quality of a report. Link back to the existing scaffold, hydrogel, release and host-response readings when an assumption comes from those foundations, and identify what each model leaves unresolved.

## Part A: solve a simultaneous architecture window

Let porosity be phi with 0<phi<1. A chosen normalized stiffness relation is E=(1−phi)², and a chosen permeability relation is K=phi³/(1−phi)². Require E≥0.04 and K≥4. The stiffness requirement gives phi≤0.8. Since K increases over the interval, the permeability inequality has a single lower crossing. Determine that crossing numerically and prove monotonicity by differentiating log K=3log phi−2log(1−phi).

Evaluate candidate phi=0.75. Its stiffness is 0.0625 and permeability 6.75, satisfying both stipulated thresholds. Compare with phi=0.85, which increases modeled permeability but fails stiffness. The argument uses two named endpoint constraints and one architecture law; it does not imply that equal porosity gives equal pore connectivity, anisotropy, strength or measured wet modulus across materials.

## Part B: add a changing interface

For a separately characterized fictional interface, fix graft fraction g=0.7. Use a competing-layer equilibrium with a/d_A=1 and b/d_B=2. Derive free fraction 0.25, the two occupied fractions and accessible ligand L=g theta_0=0.175 under the stipulated complete-masking rule. Require L≥0.15, so this candidate passes that particular access threshold.

Now let protein input b double while a and both desorption rates remain fixed. Free fraction becomes one sixth and L becomes 7/60, approximately 0.116667. The same graft fraction then fails access without changing the architecture or bulk stiffness model. Describe how a change in surrounding protein conditions could alter this prediction and what real measurements would be needed to support it. Do not treat the simple common-site layer as a universal description of a biological corona.

## Part C: distinguish function from cell number

Two fictional construct outputs at the chosen horizon are F_A=80 units with N_A=2,000 compatible viable cells and F_B=72 with N_B=1,200. Calculate both total and per-cell outputs. If the application requires total F≥75, only A passes that threshold; B's larger normalized output does not reverse its failed total requirement. If an assay signal is used as a substitute for F, specify and test the transduction model rather than relabeling intensity as function.

Explain why a high early attachment fraction does not guarantee the later population or the functional endpoint. Include distinct attachment, division/loss and assay-interference alternatives. State what an animal or tissue-context result would need to add beyond these in-vitro model quantities. The course does not supply an automatic bridge from a threshold in a paper exercise to compatibility or efficacy.

## Part D: expose temporal and boundary assumptions

Choose one existing degradation/release model and state how it could alter the architecture or accessible interface over time. Recalculate the modeled stiffness at a later stipulated porosity, without assuming that mass fraction and modulus fraction share a rate. Explain when fixed pore geometry, constant permeability or a perfect external sink would cease to be valid. Identify an alternative model or measurement that would detect the proposed failure.

Create an evidence matrix with rows for graft chemistry, hydrated ligand access, connected transport, wet mechanical response, compatible population count, total function and host response. For each row, supply its estimand, proposed independent observable, key control, missing uncertainty and the strongest justified conclusion. Distinguish same-agent mathematical checks from experimental evidence and qualified scientific review.

## Completion criteria and boundary

A usable dossier includes the simultaneous architecture interval, both interface environments, total-versus-normalized function comparison, one time-dependent failure analysis and a measurement-specific evidence matrix. Continuous checkpoint fields request three significant figures. Keep full intermediate precision and show inequality boundaries rather than rounding a failing candidate into acceptance. MIT OCW 3.051J Spring 2006 is the undergraduate scope comparator; 20.441J Fall 2009 remains a selective graduate tissue-interaction reference, not a second complete course promise. All tasks are original AI-assisted constructions with no imported source data or design standard. Broader fabrication, corrosion, biosensors, organ replacement and regulatory practice remain outside this selected application boundary; workload and qualified review remain open.
