# Assignment 3: coordination evidence and a conditional redox ledger

Prepare a cumulative paper report connecting electron/ligand bookkeeping, a limited field-energy model and a separate ligand-dependent redox equilibrium. Use [ligand-field evidence](../modules/ligand-field-spin-and-spectral-evidence.md), [Nernst/metal centers](../modules/07-redox-potentials-and-metal-centers.md) and [electrochemical composition/work](../modules/12-electrochemical-stoichiometry-and-work.md). Save calculations, diagrams and claim audits locally. Browser checkpoints assess selected results, not a full molecular interpretation or an actual electrochemical measurement.

## Occupation and energy evidence

For a fictional group-eight metal center assigned formal oxidation state +3, find the nominal d count. Under the supplied ideal octahedral model, compare high- and low-spin occupations. Use lower-orbital energy −0.4 Delta and upper energy +0.6 Delta with pairing cost P per doubly occupied orbital. Derive the energy difference from electron and pair counts instead of copying a formula without checking the occupation.

For a distinct d4 center, stipulate one absorption transition is explicitly assigned to Delta at wavelength 650 nm. Use h=6.62607015×10^−34 J s, c=299792458 m/s and NA=6.02214076×10^23 mol^−1, with P=190 kJ/mol. Compute the molar splitting, low-minus-high energy difference, favored candidate in this simplified energy comparison and its number of unpaired electrons. Compute the corresponding spin-only moment, stating its assumptions and units.

Describe evidence that would be needed before assigning an actual complex's geometry, oxidation state and spin from a spectrum or magnetic measurement. Distinguish the provided transition assignment from a proof that a real visible band is a simple d–d splitting. Explain why an energy comparison omitting entropy does not directly supply a measured finite-temperature spin-population ratio.

## A separate neutral-ligand redox model

For the following problem, use a different fictional metal family and neutral ligand L. The uncomplexed reduction is Ox2+ + e− ⇌ Red+, with standard potential E0=0.200 V under the declared ideal convention. Both forms bind one neutral L: OxL2+ has formation parameter KO=10000 L/mol and RedL+ has KR=100 L/mol. Free ligand concentration l=0.001 mol/L is independently held by a reservoir. This model is separate from the closed protonating-ligand family in Assignment 1; do not transfer its charge or reservoir assumptions silently.

Let TO and TR be analytical totals of the oxidized and reduced family, including their respective one-to-one complexes. Derive free Ox=TO/(1+KO l) and free Red=TR/(1+KR l). Start from the one-electron Nernst equation E=E0+(RT/F) ln(free Ox/free Red), using the declared equal standard concentration so the ratio is dimensionless. Substitute the total/free relations and separate the total-state ratio from the ligand-dependent shift.

Use T=298.15 K, R=8.31446262 J mol^−1 K^−1 and F=96485.33212 C/mol. For equal TO and TR, calculate the potential shift and conditional potential. Explain why preferential stabilization of Ox by stronger binding lowers this reduction potential in the stated model. The sign should follow the free-species ratio; do not infer it from a slogan that every stronger ligand raises or lowers every potential.

## Change the boundary or endpoint

If the free ligand were not held externally, explain what additional ligand/metal balances would be required and why inserting analytical LT for l could fail. Compare this with Assignment 1's finite-pool/protonation ledger. If the complex stoichiometries differed between redox states, derive the appropriate binding polynomials rather than retaining the same one-to-one factors by habit. No additional equilibrium constants are supplied for such a model.

Now let TO/TR change while the ligand reservoir remains fixed. Determine how the potential changes and distinguish this reaction-composition term from the conditional shift. Relate a defined cell-potential difference to Gibbs energy using the correct electron number, while keeping an electrode potential separate from a complete cell voltage. Explain why neither the field-energy result nor the equilibrium potential specifies the ligand-exchange rate from Assignment 2.

## Self-review and completion evidence

The formal group-eight/+3 count is d5. For the separate d4 case at 650 nm, Delta is about 184.041 kJ/mol. Low-minus-high energy is about +5.959 kJ/mol under the pairing model, so the high-spin candidate is lower. It has four unpaired electrons and spin-only moment sqrt(24) Bohr magnetons. This does not identify an actual complex or supply a complete free energy.

For the separate redox model, the ligand factor is (1+KR l)/(1+KO l)=1.1/11=0.1. Thus the conditional shift at equal analytical totals is (RT/F)ln(0.1), approximately −0.05915935 V, and the conditional potential is approximately 0.14084065 V. Keep unrounded constants through the calculation and verify the Nernst expression independently from reconstructed free concentrations.

A complete report contains electron/donor/charge distinctions, checked occupations, spectral units, a qualified spin prediction, the free-to-total redox derivation, sign and boundary checks, and a claim audit separating thermodynamics from kinetics. All text, inputs and problems are original and developed with substantial AI assistance; [MIT OCW 5.111SC Fall 2014](https://ocw.mit.edu/courses/5-111sc-principles-of-chemical-science-fall-2014/pages/syllabus/) is the shared local scope comparator. No source problem, diagram or data was imported. Qualified review, real chemical validation and measured workload remain open; the package is partial and unreviewed.
