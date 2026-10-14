# Enzyme mechanisms and inhibition

Enzymes change reaction rates by providing a pathway with a lower activation barrier. They do not change the free-energy difference between reactants and products or the equilibrium constant; they help the system approach equilibrium faster. To interpret an inhibitor or a kinetic parameter, separate the chemical mechanism from the rate model used to summarize data.

## Catalysis and the active site

An active site positions substrates and stabilizes features of the transition state. Catalytic strategies can include general acid-base transfer, transient covalent bonds, metal-ion assistance, and proximity or orientation effects. These strategies are not mutually exclusive. Binding energy contributes when it preferentially stabilizes the transition state relative to the ground state; binding a substrate tightly in a nonproductive pose does not guarantee fast chemistry.

Enzyme structure can fluctuate, and substrate binding may shift conformational populations. A measured rate may combine substrate association, conformational change, chemical conversion, product release, and product rebinding. A simple Michaelis-Menten curve is useful when those steps can be represented by an effective model, but the fitted parameters do not automatically identify every microscopic step.

## Reading a reaction-coordinate diagram

A reaction-coordinate diagram plots free energy against progress along a reaction. For one elementary step, the transition state is the high-energy configuration at the top of that step's barrier; it is not a stable species that accumulates. An intermediate is different: it occupies a local minimum between barriers and may have a measurable lifetime, even if it is short. A multistep enzyme reaction can therefore have several transition states and one or more intermediates. The highest point on a hand-drawn profile is not automatically the only rate-controlling event: measured kinetics can also depend on substrate binding, conformational changes, product release, and the conditions used.

In a simple transition-state model at fixed temperature, the rate constant varies approximately as $k\propto e^{-\Delta G^{\ddagger}/RT}$ when the transmission factor and the other prefactors are held constant. At 298 K, $RT\ln(10)=5.71$ kJ/mol. Thus, a hypothetical pathway whose activation free energy is lower by about 5.7 kJ/mol would be predicted to run about ten times faster than a comparison pathway under those matched assumptions. This is a scale illustration, not a measured enzyme effect: different activation entropies, transmission factors, mechanisms, or rate-limiting steps can change the comparison. Binding that stabilizes the ground-state enzyme-substrate complex as much as the transition state may provide little rate advantage.

## A serine-protease example: chymotrypsin

Chymotrypsin illustrates how catalytic strategies can work together. In a simplified peptide-cleavage cycle, the active-site Ser195 attacks a substrate carbonyl while His57 acts as a general base; Asp102 helps organize and tune the catalytic network. The carbonyl carbon passes through a tetrahedral, oxyanion-like high-energy configuration. Hydrogen bonds from the oxyanion hole stabilize that developing negative charge. Collapse of the first tetrahedral intermediate breaks the peptide bond and leaves a covalent acyl-enzyme intermediate on Ser195, while His57 helps transfer a proton to the departing amino group.

Water then enters the active site. His57 can accept a proton as water attacks the acyl-enzyme carbonyl, producing a second tetrahedral intermediate. Its collapse releases the carboxyl-containing product and restores Ser195. The tetrahedral configurations are intermediates along this simplified pathway; the transition states occur as bonds form or break between them. That distinction matters in a mechanism sketch: drawing a tetrahedral intermediate as though it were the transition state hides the fact that the pathway has separate barriers for acylation and deacylation.

This cycle is a teaching model, not a claim that one residue or one step always controls the observed rate. Experiments with a chemically modified chymotrypsin support an important acid-base contribution to deacylation, while also showing that the result depends on pH and the modified enzyme. Structural and kinetic evidence for the catalytic network should therefore be interpreted with the particular substrate and assay in view. See the linked primary studies below for the catalytic-site proposal and a focused deacylation test.

**Rate-barrier check.** If two hypothetical pathways have the same prefactor at 298 K and one has an activation free energy 5.71 kJ/mol lower, their predicted rate-constant ratio is $e^{5710/(8.314\times298)}\approx10$. If the data instead show a much smaller rate change, the pathways may not share the assumed prefactor or kinetic bottleneck. Do not infer a barrier difference from a rate ratio without stating the model assumptions.

## The initial-rate Michaelis-Menten model

For a one-substrate scheme $E+S\rightleftharpoons ES\rightarrow E+P$, the initial rate is often summarized as

$$v_0=\frac{V_{max}[S]}{K_m+[S]}, \qquad V_{max}=k_{cat}[E]_T.$$

The model assumes an initial-rate window with little product accumulation or reverse reaction, substrate in excess of enzyme, and approximately steady $ES$ concentration during measurement. It also assumes a suitable single-substrate saturation description. If these conditions fail, a fitted curve may still summarize observations, but its parameters need more cautious interpretation.

At $[S]=K_m$, the model predicts $v_0=V_{max}/2$. At low substrate, $[S]\ll K_m$, the rate is approximately $(k_{cat}/K_m)[E]_T[S]$; the ratio $k_{cat}/K_m$ therefore measures catalytic efficiency in the low-substrate regime and has units of concentration$^{-1}$time$^{-1}$. At high substrate, $[S]\gg K_m$, the rate approaches $V_{max}$ as the enzyme becomes saturated.

$K_m$ is the substrate concentration at half $V_{max}$ in this model. It is not generally the substrate dissociation constant. For the elementary mechanism, $K_m=(k_{-1}+k_{cat})/k_1$; it approaches the binding dissociation constant $k_{-1}/k_1$ only when chemistry is slow compared with substrate dissociation. $V_{max}$ also depends on total active enzyme, so changing enzyme concentration changes $V_{max}$ without necessarily changing $K_m$.

**Worked example.** Without inhibitor, let $V_{max}=100$ µmol/min and $K_m=2$ mM. At $[S]=2$ mM, the initial rate is 50 µmol/min. A simple competitive inhibitor that raises apparent $K_m$ to 8 mM leaves $V_{max}$ at 100; at the same substrate concentration, the rate is $100\times2/(8+2)=20$ µmol/min. At saturating substrate, both ideal curves approach the same $V_{max}$.

## Inhibition as a change in model parameters

In the simplest competitive model, inhibitor binds free enzyme and competes with substrate. The apparent $K_m$ rises while $V_{max}$ remains unchanged; enough substrate can overcome the effect in the ideal equilibrium model. A common factor is $\alpha=1+[I]/K_i$, giving $K_{m,app}=\alpha K_m$. The specific binding mechanism and assay conditions determine whether this approximation is appropriate.

For ideal **pure noncompetitive** inhibition, inhibitor binds free enzyme and enzyme-substrate complex equally. The apparent $V_{max}$ falls while $K_m$ is unchanged. **Mixed** inhibition binds the two states unequally and can shift both parameters. **Uncompetitive** inhibition binds only the enzyme-substrate complex in the idealized scheme and lowers both apparent $V_{max}$ and apparent $K_m$ by the same factor. These labels describe model behavior; many real inhibitors are mixed, tight-binding, time-dependent, irreversible, or allosteric, and a dataset may not distinguish them cleanly.

Mechanism should not be inferred from one point or a linearized plot alone. Inspect initial-rate data across a range of substrate and inhibitor concentrations, fit the rate equation directly when appropriate, and examine residuals and parameter uncertainty. Assay pH, temperature, enzyme concentration, preincubation time, substrate depletion, and signal coupling can all alter the apparent result.

## From rate to catalytic efficiency

The catalytic efficiency ratio is $k_{cat}/K_m$. Convert concentration units before dividing: with $k_{cat}=500$ s$^{-1}$ and $K_m=25$ µM $=25\times10^{-6}$ mol/L,

$$\frac{k_{cat}}{K_m}=\frac{500\text{ s}^{-1}}{25\times10^{-6}\text{ mol/L}}=2.0\times10^7\text{ L mol}^{-1}\text{ s}^{-1}.$$

This is an apparent second-order rate constant for the stated model and low-substrate regime. It is not a direct binding-affinity measure, and its interpretation requires consistent conditions and a valid estimate of $k_{cat}$ and $K_m$.

## Common mistakes

- Saying an enzyme changes the reaction's equilibrium constant rather than the rate of approach to equilibrium.
- Treating $K_m$ as $K_d$ without checking the kinetic assumptions.
- Assuming competitive inhibition lowers $V_{max}$ in the ideal model, or that all real inhibitors are purely competitive or noncompetitive.
- Comparing rates at different substrate concentrations without accounting for saturation.
- Reporting $k_{cat}/K_m$ without converting micromolar to molar units.
- Treating a fitted inhibition pattern as a complete molecular mechanism.

## Check your model

State whether a value is measured at initial rate, identify the assumptions behind the one-substrate model, and separate the fitted effect on $K_m$ from the fitted effect on $V_{max}$. The public items preserve the competitive-inhibition pattern and the calculation $500/(25\times10^{-6})=2.0\times10^7$ L/(mol·s). These are formative calculations and do not characterize a real enzyme preparation.

## Selected primary research connections

- Blow, D. M., Birktoft, J. J. & Hartley, B. S. (1969). [Role of a Buried Acid Group in the Mechanism of Action of Chymotrypsin](https://doi.org/10.1038/221337a0). *Nature*, 221, 337–340.
- Fastrez, J. & Houyet, N. (1977). [Mechanism of Chymotrypsin: Acid/Base Catalysis and Transition-State Solvation by the Active Site](https://doi.org/10.1111/j.1432-1033.1977.tb11977.x). *European Journal of Biochemistry*, 81, 515–522.
- Eyring, H. (1935). [The Activated Complex in Chemical Reactions](https://doi.org/10.1063/1.1749604). *The Journal of Chemical Physics*, 3, 107–115.

These are link-only references; no article text, figure, table, or data are reproduced here.
