# Aromaticity, electrophilic and nucleophilic aromatic substitution

An aromatic ring has an unusually stable, delocalized π system. Reactions that modify such a ring often proceed by temporary loss of that delocalization followed by its restoration. This lesson uses aromaticity to explain electrophilic aromatic substitution (EAS), then uses resonance contributors of the intermediate to predict where a second group is introduced. Examples and practice are original teaching models; this is not a chemical handling or synthesis procedure.

The undergraduate [MIT OCW 5.12 Organic Chemistry I calendar (Spring 2005)](https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2005/pages/calendar/) places aromaticity and electrophilic aromatic substitution in weeks 9–11, after alkene reactions and alkyl-halide substitution/elimination. That calendar pairs electrophilic with nucleophilic aromatic substitution in week 11, so this lesson ends by reversing the roles: the ring becomes the electrophile. This lesson uses that course as a scope comparator only. It does not reproduce MIT text, figures or problems. Separate [benzyne mechanism evidence](benzyne-and-mechanism-evidence.md) and [multistep compatibility](multistep-synthesis-and-compatibility.md) readings now develop selected extensions.

## Learning objectives

By the end of this lesson, you should be able to:

1. Classify a cyclic π system as aromatic, antiaromatic or nonaromatic from its conjugation, geometry and electron count.
2. Explain the addition–elimination sequence of electrophilic aromatic substitution and show where the ring temporarily loses aromaticity.
3. Predict the broad directing pattern of a substituent on a monosubstituted benzene and state when the product distribution cannot be inferred from directing labels alone.
4. Explain the addition–elimination mechanism of nucleophilic aromatic substitution (SNAr) and predict how the position of an electron-withdrawing group and the identity of the leaving group affect an aryl halide's reactivity.

## When is a ring aromatic?

Apply the tests in this order. A candidate must be **cyclic**, approximately **planar**, and have a continuous set of overlapping p orbitals around the ring. Count the π electrons in that conjugated loop. A planar, continuously conjugated ring with \(4n+2\) π electrons (for integer \(n\geq0\)) is aromatic. If a planar, continuously conjugated ring instead has \(4n\) π electrons, it is antiaromatic and destabilized. If it cannot maintain planarity or continuous p-orbital overlap, it is nonaromatic rather than antiaromatic; the electron count alone is not enough.

Examples make the distinctions concrete:

- **Benzene:** three π bonds contribute six π electrons. The planar, conjugated ring satisfies \(4n+2\) for \(n=1\), so it is aromatic.
- **Cyclobutadiene:** its planar conjugated ring has four π electrons. It satisfies the \(4n\) count for \(n=1\), so the ideal planar system is antiaromatic.
- **Cyclooctatetraene:** it has eight π electrons, but its familiar tub-shaped geometry interrupts continuous planar overlap. It is nonaromatic; do not classify it as antiaromatic from the number eight alone.
- **Cyclopentadienyl anion:** two π bonds and one p-orbital lone pair contribute six electrons to a planar conjugated loop, giving an aromatic system.

A resonance drawing is not a set of rings that rapidly switch between structures. It is a bookkeeping representation of one delocalized electronic structure. The aromatic test concerns the whole cyclic π system, not whether one drawing has alternating single and double bonds.

## The EAS mechanism restores aromaticity

Write a generic substitution of a ring hydrogen as

\[
\mathrm{Ar-H + E^+ \longrightarrow Ar-E + H^+}.
\]

The mechanism has two central steps:

1. **Addition:** a ring π bond donates electron density to the electrophile \(E^+\). The carbon–electrophile bond forms, and that carbon still bears its hydrogen. The resulting σ complex (arenium ion) is no longer fully aromatic, but its positive charge is delocalized over several ring positions by resonance.
2. **Elimination:** a base removes the hydrogen from the carbon that now bears \(E\). The C–H bond electrons form a new π bond, restoring the conjugated aromatic ring.

The second step does not remove the incoming electrophile. It removes a proton from the same carbon where the new substituent attached. Confusing these positions often produces an impossible product or an incorrect charge balance.

For the net reaction, the ring replaces one hydrogen with one electrophile. The carbon framework and the number of ring atoms remain unchanged. Reagents used to generate a sufficiently reactive electrophile depend on the specific transformation; naming them does not specify an operational procedure.

## Directing effects on a substituted ring

Label the carbon already bearing a substituent as position 1. Positions 2 and 6 are **ortho**, 3 and 5 are **meta**, and 4 is **para**. In a monosubstituted benzene, resonance contributors of the σ complex explain the broad orientation of a second EAS:

- **Electron-donating groups** such as methoxy can donate a lone pair into the ring. Their resonance contributors stabilize the ortho and para σ complexes, so these groups generally activate the ring and direct incoming electrophiles ortho/para.
- **Strong electron-withdrawing groups** such as nitro pull electron density from the ring. The ortho and para σ complexes place positive charge in an unfavorable relationship to the attached withdrawing group, while the meta pathway avoids that particular contributor. These groups generally deactivate the ring and direct meta.
- **Halogens are an exception worth explaining:** they withdraw inductively and deactivate the ring, but their lone pairs can donate by resonance. The broad directing pattern is therefore ortho/para despite a lower reaction rate than benzene under a comparable set of conditions.

“Ortho/para director” names allowed broad positions; it does not say that all those products form equally or that an exact ratio is known. Steric crowding, the other groups on a ring, and the specific reaction conditions can affect the distribution. When two substituents direct to different positions, identify the competing σ complexes and report the limit of the evidence rather than inventing a ratio.

## Worked example: a methoxy-substituted ring

Predict the broad products when an electrophile replaces a ring hydrogen on methoxybenzene.

**Step 1: identify the substituent effect.** Methoxy can donate an oxygen lone pair into the aromatic π system. It activates the ring and stabilizes σ-complex resonance contributors from attack at the ortho and para positions.

**Step 2: compare allowed sites.** Positions 2/6 are equivalent ortho sites, and position 4 is para. Position 3/5 is meta and is not the broad resonance-favored pathway for this substituent.

**Step 3: state what the model supports.** The broad product set is ortho- and para-substituted methoxybenzene. This directing analysis alone does not determine the exact ortho:para ratio; steric effects and specified conditions would be needed for a quantitative product distribution.

## Nucleophilic aromatic substitution: the ring as electrophile

An ordinary aryl halide such as chlorobenzene resists the substitution mechanisms from the alkyl-halide lessons. An SN2 nucleophile would have to approach from behind the C–Cl bond, which points through the ring itself. An SN1 path would need an aryl cation, whose empty orbital is an sp² orbital in the ring plane that the π system cannot stabilize. A different mechanism operates when the ring carries strong electron-withdrawing groups. Write the net change as

\[
\mathrm{Ar-X + Nu^- \longrightarrow Ar-Nu + X^-}.
\]

Like EAS, SNAr is an **addition–elimination** sequence that temporarily gives up aromaticity. The electron flow runs the other way.

1. **Addition:** the nucleophile donates a pair to the **ipso** carbon, the ring carbon that bears the leaving group. That carbon becomes sp³ and holds both Nu and X. The ring is no longer aromatic, and it now carries a negative charge. This anionic σ complex is called a **Meisenheimer complex**.
2. **Elimination:** the ring's electron pair returns to re-form the aromatic π system, and the halide leaves from the same ipso carbon.

The resonance contributors of the Meisenheimer complex put the negative charge on the ring carbons **ortho and para to the ipso carbon**, never on the meta carbons. That one fact explains the substrate requirement. A nitro, cyano or carbonyl group attached at an ortho or para position can carry the charge onto its own electronegative atoms. For a nitro group, an additional contributor places it on oxygen. A withdrawing group at a meta position cannot share the charge this way. It offers only a weaker inductive effect, so a meta-nitro aryl halide is much less activated than its ortho or para isomer.

**Leaving-group order reverses the SN2 pattern.** For activated substrates, the addition step is usually rate-determining, and the C–X bond breaks only afterward. Fluorine's high electronegativity makes the ipso carbon more electron-poor and stabilizes the developing negative charge, so activated aryl fluorides commonly react faster than the corresponding chlorides, bromides or iodides. This reverses the SN2 trend and is not a contradiction: the strong C–F bond is not being broken in the slow step. Treat this as a qualitative trend for activated rings, not a fixed rate ratio.

**One substituent, opposite roles.** A nitro group deactivates a ring toward EAS because it destabilizes a *cationic* σ complex. The same group activates a ring toward SNAr when it is ortho or para to the leaving group, because it stabilizes an *anionic* σ complex. Ask which intermediate forms before reaching for a directing label. In EAS, the ring is the nucleophile and the group that leaves is H⁺. In SNAr, the ring is the electrophile and the group that leaves is the halide.

## Worked example: a dinitro aryl chloride and methoxide

Compare 1-chloro-2,4-dinitrobenzene with 1-chloro-3,5-dinitrobenzene as substrates for methoxide (CH₃O⁻).

**Step 1: label positions from the ipso carbon.** In the 2,4-isomer, C2 is ortho and C4 is para to the C–Cl carbon. Both nitro groups sit where the Meisenheimer charge appears. In the 3,5-isomer, both nitro groups are meta, so neither can accept the charge by resonance.

**Step 2: follow the charge.** Methoxide adds to C1. The ring contributors place the negative charge on C2, C4 and C6, which are three ring carbons. In the 2,4-isomer, further contributors move that charge onto the oxygens of the C2 and C4 nitro groups. Adding a neutral substrate and a monoanion gives a complex with a net charge of −1. Loss of Cl⁻ restores aromaticity and gives neutral 2,4-dinitroanisole.

**Step 3: state what the model supports.** The 2,4-isomer is predicted to be far more reactive toward SNAr. The model does not supply a rate constant or yield, and the 3,5-isomer is not absolutely inert under all conditions. The prediction compares charge stabilization only.

**A biochemical connection.** 1-Fluoro-2,4-dinitrobenzene ("Sanger's reagent") combines both trends, with a fluoride leaving group and ortho and para nitro activation. Its SNAr reaction with free amino groups attaches a dinitrophenyl label. Historically, this let the N-terminal residue of a peptide chain be identified after hydrolysis. The lesson explains the mechanism only. It is not a labeling procedure.

## Common errors and checks

- Counting electrons before checking that the ring is planar and continuously conjugated.
- Calling every \(4n\)-electron ring antiaromatic even when it avoids planarity and is therefore nonaromatic.
- Drawing the σ complex as though the ring stayed aromatic during electrophile addition.
- Removing the incoming electrophile instead of the hydrogen from its carbon during deprotonation.
- Treating an ortho/para label as a measured product ratio.
- Calling halogens activating because they direct ortho/para, while ignoring their inductive deactivation.
- Drawing SNAr as a one-step backside SN2 displacement at an sp² ring carbon, or as an aryl-cation SN1 path.
- Expecting a meta nitro group to activate SNAr as strongly as an ortho or para nitro group.
- Carrying the SN2 leaving-group order (I > Br > Cl > F) into SNAr of activated rings.
- Removing H⁺ instead of the halide in the elimination step of SNAr.

Check an answer by counting the conjugated electrons, following formal charge through the σ-complex contributors, and confirming that the final substitution restores the ring's aromatic π system. For SNAr, also confirm that the charge on the Meisenheimer complex sits ortho and para to the ipso carbon. The benzyne pathway for unactivated aryl halides, directing conflicts on multiply substituted rings, and multi-step aromatic synthesis remain outside this lesson.
