# Receptors, G-protein switches and second messengers

The [glycogen lesson](17-glycogen-storage-and-mobilization.md) later this week uses glucagon and epinephrine to raise cyclic AMP and activate protein kinase A, and the week-13 [fatty-acid synthesis lesson](23-fatty-acid-synthesis.md) uses the same messenger to release stored fat. Neither explains how a hormone outside the cell changes the concentration of a small molecule inside it. This lesson supplies that chemistry first: receptor occupancy and spare receptors, the GTP-timed switch of G proteins, the synthesis, degradation and targets of second messengers, a lipid-kinase route from the insulin receptor, and receptors that act on DNA. The Cell Biology [receptor signaling lesson](../../cell-biology/modules/10a-receptor-signaling-and-network-logic.md) treats network logic and experimental inference and is not repeated here. Every receptor, rate and concentration below is synthetic.

The undergraduate [MIT OCW 7.05 General Biochemistry (Spring 2020) calendar](https://ocw.mit.edu/courses/7-05-general-biochemistry-spring-2020/pages/calendar/) gives sessions 14 and 15 to hormones, receptors, small G proteins and signal transduction. The [University of Guelph BIOC*3560 outline (Winter 2023)](https://www.uoguelph.ca/mcb/system/files/BIOC3560_W23_SG_Final_0.pdf) gives a lecture part to biological signalling, with gated ion channels, receptor enzymes, G protein-coupled receptors and steroid hormone receptors. The local package used cyclic AMP in two metabolic lessons without a reading on how it is made. Both courses are link-only scope comparators; no text, figure or problem is reproduced.

## Learning objectives

By the end of this lesson, you should be able to:

1. Compute receptor occupancy from a dissociation constant, and use a saturating transducer model to explain why a response can be half-maximal at low occupancy.
2. Trace a G protein-coupled receptor to protein kinase A, calculating G-protein active lifetime, cascade amplification and steady-state cyclic AMP, and predict the effect of perturbing each step.
3. Compare the phospholipase C, insulin-receptor and nuclear-receptor routes by their messengers, enzymes and termination steps.

## Occupancy and the spare-receptor effect

A receptor R binds a ligand L with dissociation constant K_d. At equilibrium, with free ligand well in excess of receptor, the fraction of receptors occupied is

\[
\theta = \frac{[L]}{[L] + K_d},
\]

the same hyperbola used in the [binding-equilibria lesson](07-binding-equilibria-and-cooperativity.md). Occupancy is 0.5 at [L] = K_d and 0.9 at [L] = 9K_d.

The cell's response is not occupancy. Downstream enzymes amplify the signal and then saturate. A simple way to describe this is a stipulated transducer in which the response rises hyperbolically with the stimulus θτ, where the efficacy τ grows with receptor number and coupling strength. Normalized so that full occupancy gives a response of 1,

\[
R = \frac{(1 + \tau)\,\theta}{1 + \tau\theta}.
\]

Half-maximal response occurs at θ = 1/(2 + τ), which corresponds to a ligand concentration EC₅₀ = K_d/(1 + τ). With τ = 9, the response is half-maximal at 1/11 occupancy and EC₅₀ = K_d/10. The cell is said to have **spare receptors**: it reaches half its maximum response while most receptors are empty. Removing receptors lowers τ, which first shifts EC₅₀ toward K_d and only later lowers the maximum response. A measured EC₅₀ is therefore not a binding constant, and an EC₅₀ well below K_d is evidence of amplification.

## The G protein as a timed switch

A G protein-coupled receptor (GPCR) has seven transmembrane helices. Ligand binding shifts it to an active conformation that acts as a **guanine-nucleotide exchange factor** (GEF) for a heterotrimeric G protein, Gαβγ. The receptor opens the nucleotide pocket of Gα, which releases GDP and binds GTP, abundant in the cytosol. Gα·GTP separates from Gβγ, and both can regulate effectors. One active receptor can activate many G proteins before it is switched off.

Gα is also a slow GTPase. It stays active until it hydrolyzes its bound GTP to GDP, then reassociates with Gβγ. If hydrolysis is first-order with rate constant k_hyd, the fraction of Gα still active t seconds after activation is e^(−k_hyd t), and the mean active lifetime is 1/k_hyd. **Regulators of G-protein signalling** (RGS proteins) act as GTPase-activating proteins (GAPs) and shorten this lifetime. With a stipulated k_hyd = 0.05 s⁻¹, Gα·GTP lasts 20 s on average; if an RGS protein raises k_hyd to 2.0 s⁻¹, it lasts 0.5 s.

Gαs activates **adenylyl cyclase**, which converts ATP to 3′,5′-cyclic AMP and pyrophosphate. If one Gαs–cyclase complex makes 20 cAMP per second while active, it makes on average 20 × 20 = 400 cAMP per activation without RGS acceleration and 20 × 0.5 = 10 with it. Small changes in a timer change the output of every downstream step.

Amplification multiplies across stages. If one receptor activates 30 Gαs during its active period and each yields 400 cAMP, one receptor produces 12,000 cAMP. Protein kinase A is an inactive R₂C₂ tetramer: two regulatory subunits each bind two cAMP, and the four bound cAMP release two active catalytic subunits. Twelve thousand cAMP can free at most 6,000 catalytic subunits, each of which phosphorylates many substrate molecules, such as phosphorylase kinase in the glycogen cascade.

## Steady-state messenger levels and termination

A second messenger's concentration is set by a balance. If cyclase makes cAMP at a rate V_syn and cyclic-nucleotide **phosphodiesterases** (PDEs) hydrolyze it to 5′-AMP with first-order rate constant k_PDE,

\[
\frac{d[\text{cAMP}]}{dt} = V_{\text{syn}} - k_{\text{PDE}}[\text{cAMP}], \qquad [\text{cAMP}]_{ss} = \frac{V_{\text{syn}}}{k_{\text{PDE}}}.
\]

The level approaches steady state, and decays when synthesis stops, with time constant 1/k_PDE. With V_syn = 1.2 µM/s and k_PDE = 3.0 s⁻¹, the steady state is 0.40 µM and the time constant 0.33 s. A PDE inhibitor that lowers k_PDE to 0.75 s⁻¹ raises the steady state fourfold, to 1.6 µM, and slows both rise and decay fourfold. Raising a messenger by blocking its removal therefore also makes the signal slower to switch off.

Signalling ends at every stage: the ligand dissociates, Gα hydrolyzes GTP, PDEs remove cAMP, and protein phosphatases remove the phosphates that kinases added. The receptor is also switched off directly. A G protein-coupled receptor kinase (GRK) phosphorylates the active receptor, and arrestin binds the phosphorylated receptor, blocking further G-protein coupling and promoting internalization. This **desensitization** lowers the response to a sustained stimulus.

Two bacterial toxins show what happens when one step is removed. Cholera toxin transfers an ADP-ribose group to Gαs and blocks its GTPase, so Gαs stays active and cAMP stays high without any hormone. Pertussis toxin ADP-ribosylates Gαi, the inhibitory α subunit, and prevents receptors from activating it, so cyclase loses an inhibitory input. Both raise cAMP, by different mechanisms.

## Other routes

**Phospholipase C.** GPCRs coupled to Gαq activate phospholipase Cβ, which cleaves the membrane lipid phosphatidylinositol 4,5-bisphosphate (PIP₂) into two messengers. Soluble inositol 1,4,5-trisphosphate (IP₃) opens a Ca²⁺ channel in the endoplasmic reticulum. Resting cytosolic Ca²⁺ is roughly ten thousand times lower than outside the cell, so opening channels raises it quickly. Diacylglycerol (DAG) stays in the membrane and, with Ca²⁺, activates protein kinase C. Ca²⁺ also acts through calmodulin, which binds four Ca²⁺ and then activates other kinases and enzymes.

**Receptor tyrosine kinases.** The insulin receptor is a preformed dimer whose intracellular domains are tyrosine kinases. Insulin binding brings them into position to phosphorylate each other in the activation loop, raising kinase activity. The receptor then phosphorylates insulin receptor substrate (IRS) proteins, whose phosphotyrosines are docking sites for proteins with SH2 domains, among them phosphoinositide 3-kinase (PI3K). PI3K is a lipid kinase: it adds a phosphate at the 3-position of PIP₂ to make PIP₃. Proteins with PH domains that bind PIP₃, including the kinases PDK1 and Akt, gather at the membrane, where Akt is phosphorylated and activated. Akt phosphorylates many targets. It inhibits glycogen synthase kinase 3, which relieves inhibition of glycogen synthase; it promotes movement of GLUT4 glucose transporters to the plasma membrane in muscle and fat; it phosphorylates FOXO transcription factors, keeping them out of the nucleus; and it helps activate the growth-promoting kinase complex mTORC1. The lipid phosphatase PTEN removes the 3-phosphate from PIP₃ and opposes PI3K. Other growth-factor receptors use adaptor proteins and a GEF to load the small G protein Ras with GTP. Ras is a single-subunit switch with the same logic as Gα, and mutants that resist GAP-stimulated hydrolysis stay active. The Geroscience [nutrient-sensing lesson](../../geroscience/modules/07-nutrient-sensing-and-lifespan-interventions.md) reads model-organism evidence about this insulin/IGF, FOXO and TOR network; this lesson describes only its biochemistry.

**Nuclear receptors and channels.** Steroid hormones such as cortisol are lipid-soluble and cross the membrane. Their receptors are intracellular transcription factors: ligand binding releases chaperones and lets the receptor bind response elements in DNA and change transcription. Responses take hours, because new mRNA and protein must be made. At the other extreme, ligand-gated ion channels such as the nicotinic acetylcholine receptor open within milliseconds of binding. G protein and kinase routes fall between, acting over seconds to minutes.

## Worked example

**Problem.** A synthetic Gs-coupled receptor has K_d = 5.0 nM and efficacy τ = 9 in the transducer model. Find the occupancy and response at 15 nM ligand, the EC₅₀, and the effect of a drug that irreversibly removes 80 per cent of the receptors. Then explain what cholera toxin would do in the same cell.

**Step 1: occupancy.** θ = 15/(15 + 5.0) = 0.75.

**Step 2: response.** R = (1 + 9)(0.75)/(1 + 9 × 0.75) = 7.5/7.75 = 0.968. Three-quarters occupancy gives nearly the full response.

**Step 3: EC₅₀.** EC₅₀ = K_d/(1 + τ) = 5.0/10 = 0.50 nM, a tenth of K_d.

**Step 4: receptor loss.** Efficacy scales with receptor number, so τ falls to 0.2 × 9 = 1.8. The new EC₅₀ is 5.0/2.8 = 1.79 nM. The maximum response, relative to the original maximum, is [τ′/(1 + τ′)]/[τ/(1 + τ)] = (1.8/2.8)/(9/10) = 0.714. Losing four-fifths of the receptors moves the curve right more than threefold but lowers its top by only about 29 per cent.

**Step 5: cholera toxin.** The toxin blocks Gαs GTP hydrolysis downstream of the receptor. Cyclic AMP rises without ligand, receptor antagonists cannot prevent it, and a PDE inhibitor would raise it further.

## Common mistakes and checks

- Equating EC₅₀ with K_d, or occupancy with response.
- Treating Gα·GTP as switched off by the receptor rather than by its own GTP hydrolysis.
- Confusing GEFs, which load GTP and activate, with GAPs, which accelerate hydrolysis and inactivate.
- Forgetting that PKA needs four cAMP to release two catalytic subunits.
- Expecting a PDE inhibitor to raise cAMP without also slowing its return to baseline.
- Calling DAG a soluble messenger; it stays in the membrane, while IP₃ diffuses.
- Treating PI3K as a protein kinase; it phosphorylates a lipid, and PTEN reverses it.
- Expecting steroid receptor responses within seconds.

A check: at [L] = K_d occupancy is one half, but with spare receptors the response is already well above one half.

## Limits of this lesson

All receptors, rates, efficacies and concentrations are synthetic. The transducer law is a stipulated saturating model, not a fitted description of any receptor, and assumes equilibrium binding without ligand depletion. First-order GTP hydrolysis and PDE removal ignore enzyme saturation, compartmentalization by scaffold proteins and spatial gradients of messengers. The amplification count is an upper bound that ignores losses at every step. Receptor structures, receptor families beyond the examples, cytokine and integrin signalling, and network feedback are not developed; the Cell Biology lessons treat network logic. Nothing here describes a drug, a dose or a treatment, and the lesson gives no laboratory protocol or medical advice. Original instruction has substantial AI assistance and uses link-only references without copied source text. The course remains partial, unreviewed and formative-only.
