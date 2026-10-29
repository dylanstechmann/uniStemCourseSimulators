# Membrane lipids, bilayer organization and membrane proteins

The [alternating-access lesson](alternating-access-and-coupled-transport-cycles.md) that follows this one treats a transporter as a protein that moves solutes across a membrane, and the week-11 [mitochondrial lesson](11-mitochondrial-bioenergetics-and-atp-yield.md) relies on a membrane that holds a proton gradient. Both take the membrane itself for granted. This lesson builds it from its parts. It explains why amphipathic lipids assemble into a bilayer rather than a droplet, how chain structure and cholesterol set the bilayer's physical state, how proteins sit in or on it, and how fast its components move. The Cell Biology [membranes and transport lesson](../../cell-biology/modules/02-membranes-transport-and-compartmentalization.md) covers electrochemical gradients and is not repeated here. Every lipid, protein and measurement below is synthetic.

The undergraduate [MIT OCW 7.05 General Biochemistry (Spring 2020) calendar](https://ocw.mit.edu/courses/7-05-general-biochemistry-spring-2020/pages/calendar/) introduces membranes in session 12, before channels, transporters and pumps in session 13. The [University of Guelph BIOC*3560 Structure and Function in Biochemistry outline (Winter 2023)](https://www.uoguelph.ca/mcb/system/files/BIOC3560_W23_SG_Final_0.pdf) gives a lecture part to membrane lipids, membrane organization, membrane proteins and membrane dynamics. The local package had a transport reading but no reading on what a membrane is made of. Both courses are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Relate lipid shape to the aggregate it forms with the packing parameter, and predict how chain length, unsaturation and cholesterol change a bilayer's physical state.
2. Classify membrane proteins as integral, peripheral or lipid-anchored, and use a hydropathy window and helix geometry to judge whether a segment can cross the bilayer.
3. Quantify lateral diffusion and mobile fraction from recovery data, and explain why transverse movement between leaflets is slow and how leaflet asymmetry decays.

## Amphipathic lipids and the shape that decides the aggregate

A membrane lipid has a polar headgroup and one or two hydrocarbon chains. Glycerophospholipids such as phosphatidylcholine (PC), phosphatidylethanolamine (PE) and phosphatidylserine (PS) carry two fatty-acyl chains on glycerol and a phosphate-linked headgroup. Sphingolipids such as sphingomyelin build the same overall shape on sphingosine. Cholesterol is different: a rigid, flat four-ring system with a single hydroxyl group that sits near the headgroups.

In water, the chains are driven together because exposing hydrocarbon disrupts the hydrogen-bonded structure of the surrounding water; this is the hydrophobic effect met in the [folding lesson](09-protein-folding-and-stability.md). What the chains assemble into depends on the lipid's shape. The **packing parameter** compares the chain volume v with the product of the headgroup area a₀ at the interface and the chain length l_c:

\[
P = \frac{v}{a_0\, l_c}.
\]

A molecule with P below about 1/3 is cone-shaped, with a head wider than its tail, and packs into spherical micelles. Values between 1/3 and 1/2 give cylindrical micelles. Values between 1/2 and 1 describe a roughly cylindrical molecule that packs into flat or gently curved bilayers. Values above 1 describe an inverted cone, which favours inverted phases that curve toward the water.

Take two synthetic lipids with the same headgroup area, a₀ = 0.70 nm². A single-chain surfactant with v = 0.35 nm³ and l_c = 1.67 nm has P = 0.35/(0.70 × 1.67) = 0.299, below 1/3, so it forms micelles. A two-chain phospholipid with v = 0.92 nm³ and l_c = 1.75 nm has P = 0.92/(0.70 × 1.75) = 0.751, so it forms a bilayer. Doubling the chains roughly doubles v while barely changing l_c, which is why two-chain lipids make membranes and single-chain detergents dissolve them. Shrinking the headgroup of the two-chain lipid to a₀ = 0.45 nm², as for a PE-like lipid with a small, weakly hydrated head, gives P = 1.17. Such lipids favour curvature toward the water and do not form stable flat bilayers alone, although mixed with PC they help membranes bend and fuse.

## Physical state: gel, fluid and the effect of cholesterol

A bilayer of one saturated lipid melts over a narrow range. Below its transition temperature T_m the chains are extended and packed in an ordered **gel** phase. Above it they are disordered and the bilayer is **fluid**, which is the state in which membrane proteins diffuse and function. Two structural rules predict T_m. Longer saturated chains have more van der Waals contact, so T_m rises with chain length. A cis double bond puts a fixed kink in the chain that prevents tight packing, so unsaturation lowers T_m sharply. Cells adjust both, along with the headgroup mix, to keep their membranes fluid at the temperature they live at.

Cholesterol acts in both directions. Its rigid rings sit beside the first carbons of neighbouring chains. In a fluid bilayer it orders those chains and reduces permeability. Below T_m it keeps chains from crystallizing. At high cholesterol content the transition broadens and a **liquid-ordered** state appears that is fluid in the plane but has ordered chains. Sphingolipid- and cholesterol-rich ordered domains, often called rafts, form readily in model membranes. Their size and lifetime in living cells remain under study, so treat them as a hypothesis about local organization, not a fixed structure.

## Membrane proteins

Proteins associate with a membrane in three ways.

- **Integral** proteins cross the hydrocarbon core or are embedded in it. Releasing them requires disrupting the bilayer, conventionally with a detergent.
- **Peripheral** proteins bind the surface through electrostatic contacts and hydrogen bonds with headgroups or with integral proteins. A change in salt concentration or pH can release them while the bilayer stays intact.
- **Lipid-anchored** proteins are covalently attached to a lipid that inserts into one leaflet: an N-terminal myristoyl group, a cysteine palmitoyl or prenyl group, or a glycosylphosphatidylinositol (GPI) anchor on the outer surface.

Most segments that cross the core are α-helices. In a helix every backbone N–H and C=O pairs with another within the same helix, so no polar backbone group is left unsatisfied inside the hydrocarbon. A helix rises 0.15 nm per residue. The hydrocarbon core is about 3 nm thick, so a perpendicular helix needs about 3.0/0.15 = 20 residues, most of them nonpolar, to span it. Thicker, cholesterol-rich membranes need slightly longer segments. The outer membranes of bacteria, mitochondria and chloroplasts also use β-barrels, in which strands of about 9 to 11 residues pair into a closed sheet whose hydrogen bonds face inward.

A **hydropathy window** turns this into a sequence test. Assign each residue a value, average the values over a window about as long as a transmembrane helix, and slide the window along the chain. Published hydropathy scales are derived from measured transfer free energies; this lesson uses a stipulated three-level teaching scale: +1 for I, L, V, F, M, A and C; 0 for G, S, T, P, Y, H and W; and −1 for D, E, K, R, N and Q. Use a 19-residue window and treat a mean above 0.5 as a candidate transmembrane segment. A high mean is a prediction, not proof of topology: signal peptides and buried hydrophobic cores also score high. Positively charged residues are often enriched on the cytoplasmic side of a transmembrane segment, a pattern that helps predict orientation.

## Movement within and between leaflets

Lipids and many proteins diffuse laterally in a fluid bilayer. For two-dimensional random motion, the mean-squared displacement grows linearly with time:

\[
\langle r^2 \rangle = 4Dt,
\]

where D is the lateral diffusion coefficient. A synthetic lipid with D = 1.0 µm²/s has ⟨r²⟩ = 4.0 µm² after 1 s, a root-mean-square displacement of 2.0 µm. A synthetic membrane protein with D = 0.05 µm²/s moves 0.45 µm in the same second and takes 20 s to reach 2.0 µm. Proteins diffuse more slowly because they are larger and because many are tethered to the cytoskeleton or confined between barriers.

**Fluorescence recovery after photobleaching** (FRAP) measures this. A fluorescent label is bleached in a small spot, and unbleached molecules diffuse in from around it. If F_i is the spot intensity before bleaching, F₀ the intensity just after, and F_∞ the plateau reached on recovery, the **mobile fraction** is

\[
M_f = \frac{F_\infty - F_0}{F_i - F_0}.
\]

This assumes the bleached spot is a small part of the labelled pool and that bleaching during observation is negligible. The rate of recovery reflects D; the plateau reflects M_f. A plateau below the starting intensity means some molecules did not move during the measurement, not that they are absent.

Movement from one leaflet to the other, **transverse diffusion** or flip-flop, is much slower, because the polar headgroup must cross the hydrocarbon core. Uncatalyzed flip-flop of a phospholipid takes hours or longer, whereas lateral exchange with a neighbour takes far less than a second. Consider a labelled lipid placed entirely in the outer leaflet, flipping in each direction with the same first-order rate constant k. The outer fraction x obeys dx/dt = k(1 − 2x), so the asymmetry x − 1/2 decays as e^(−2kt). With a single-molecule flip half-time t½ = ln 2/k, the asymmetry halves every t½/2, because molecules leave the crowded leaflet faster than they return. Cells oppose this with enzymes: ATP-driven flippases move PS and PE inward, floppases move lipids outward, and scramblases equalize the leaflets when activated. The plasma membrane therefore keeps PS and most PE on its cytoplasmic leaflet and PC, sphingomyelin and glycolipids mostly on the outer leaflet. Exposure of PS on the outer surface is one signal by which phagocytes recognize apoptotic cells.

## Worked example

**Problem.** A synthetic protein contains the 19-residue segment LLVAIFGLLAVLMSCAVLW. In FRAP of the labelled protein, the spot reads 1000 before bleaching, 200 just after and 760 at the plateau, and the recovery corresponds to D = 0.10 µm²/s. Decide whether the segment can cross the membrane, find the mobile fraction, and estimate how far the mobile protein moves in 10 s.

**Step 1: hydropathy.** Sixteen residues (L, V, A, I, F, M and C) score +1; G, S and W score 0; none scores −1. The window mean is 16/19 = 0.842, well above 0.5.

**Step 2: geometry.** Nineteen residues at 0.15 nm per residue make a helix 2.85 nm long, close to the 3 nm core. The segment is a plausible single transmembrane helix, with a few flanking residues completing the span.

**Step 3: mobile fraction.** M_f = (760 − 200)/(1000 − 200) = 560/800 = 0.70. Seventy per cent of the labelled protein moved during the measurement; 30 per cent did not.

**Step 4: distance.** ⟨r²⟩ = 4 × 0.10 × 10 = 4.0 µm², a root-mean-square displacement of 2.0 µm for the mobile population.

**Step 5: what the data do not show.** The immobile 30 per cent could be anchored to the cytoskeleton, trapped in a domain, or aggregated. FRAP alone does not distinguish these, and the hydropathy window does not say which end of the helix faces the cytoplasm.

## Common mistakes and checks

- Treating the packing parameter as a property of the chains alone; headgroup area matters as much.
- Expecting unsaturation to raise the transition temperature, or chain length to lower it.
- Describing cholesterol as simply fluidizing or simply rigidifying; its effect depends on the phase.
- Calling every membrane-bound protein integral. A protein released by a salt or pH change, with the bilayer intact, is peripheral.
- Using ⟨r²⟩ = 2Dt, the one-dimensional form, for diffusion in the plane of a membrane, or forgetting to take the square root for a distance.
- Reading a FRAP plateau below the starting intensity as protein loss rather than an immobile fraction.
- Assuming lipids exchange between leaflets as fast as they diffuse within one.

A check: a transmembrane helix needs about 20 residues, a lipid crosses a micrometre in about a second, and a phospholipid takes hours to change leaflets unaided.

## Limits of this lesson

All lipids, proteins, sequences and fluorescence values are synthetic, and the hydropathy scale is a stipulated three-level teaching scale, not a published one. The packing parameter is a geometric guide that ignores chain flexibility, headgroup charge and mixing. Transition temperatures are discussed as trends, without values for real lipids. FRAP analysis is reduced to the mobile fraction and a diffusion scaling, without fitting a recovery curve or correcting for bleaching during acquisition. Membrane protein folding, insertion and structure determination are not developed. The lesson gives no laboratory protocol. Original instruction has substantial AI assistance and uses link-only references without copied source text. The course remains partial, unreviewed and formative-only.
