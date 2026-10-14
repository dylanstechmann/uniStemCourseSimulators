# Nucleotide biosynthesis, salvage and deoxyribonucleotides

Cells build nucleotides for RNA, DNA and many activated cofactors. The ribose-phosphate backbone begins with ribose 5-phosphate, which can be supplied by the pentose phosphate pathway. Purines and pyrimidines use different construction plans, but both connect carbon, nitrogen, folate chemistry and energy use.

## Learning objectives

By the end of this lesson, you should be able to:

1. Trace de novo purine and pyrimidine synthesis to their first major ribonucleotide products and explain control at branch points.
2. Explain how purine salvage, ribonucleotide reduction and thymidylate synthesis connect nucleotide pools with energy and one-carbon metabolism.
3. Calculate PRPP use across synthetic de novo purine synthesis and purine salvage, then separately account for ATP and GTP used at the IMP branch point.

## Shared activated ribose and purine assembly

Ribose 5-phosphate is converted to phosphoribosyl pyrophosphate (PRPP) by PRPP synthetase, using ATP to create an activated ribose donor. PRPP supports de novo purine synthesis, purine salvage and the attachment step in pyrimidine synthesis. Its supply therefore links the pentose phosphate pathway to nucleotide demand.

Purine biosynthesis builds the ring directly on PRPP. Glutamine donates nitrogen at the committed entry step catalyzed by glutamine-PRPP amidotransferase. A sequence of additions and rearrangements forms inosine monophosphate (IMP), the first fully formed purine nucleotide in the pathway. Atoms in the purine ring are contributed by glycine, glutamine, aspartate, carbon dioxide and N10-formyl-tetrahydrofolate. IMP then branches to AMP or GMP.

The two branch routes use different energy currencies. AMP synthesis from IMP uses aspartate and GTP; GMP synthesis uses glutamine and ATP. This cross-use of GTP and ATP can help balance adenine and guanine nucleotide supply. IMP, AMP and GMP also regulate early de novo steps by feedback. Real flux depends on substrate supply, enzyme regulation and cellular demand, not just one nucleotide concentration.

## Pyrimidine assembly follows a different order

Pyrimidine synthesis constructs the ring before attaching it to ribose. In mammalian cells, the multifunctional CAD enzyme begins with glutamine-derived nitrogen, bicarbonate-derived carbon and ATP to form carbamoyl phosphate and then carbamoyl aspartate. Further reactions make dihydroorotate. Dihydroorotate dehydrogenase, associated with the inner mitochondrial membrane, oxidizes it to orotate. Orotate then receives the phosphoribosyl group from PRPP to form OMP; decarboxylation produces UMP.

UMP is phosphorylated to UDP and UTP. CTP synthetase converts UTP to CTP using glutamine and ATP. UTP and related pyrimidine pools feed back on synthesis, while PRPP availability and growth demand also matter. Thus, purines assemble onto PRPP, whereas pyrimidines attach an already-built ring to PRPP at the orotate step.

## Salvage recycles bases; reduction supplies DNA precursors

Salvage pathways recover bases or nucleosides released during RNA and DNA turnover. APRT attaches adenine to PRPP to form AMP. HGPRT attaches hypoxanthine to form IMP and guanine to form GMP. Salvage avoids reconstructing the base ring, but it still consumes PRPP, so it is not energetically free. Salvage and de novo synthesis feed shared nucleotide pools.

Ribonucleotide reductase converts ribonucleoside diphosphates (NDPs) to the matching deoxyribonucleoside diphosphates (dNDPs). It uses reducing equivalents delivered through thioredoxin or glutaredoxin systems, which are regenerated using NADPH. This is the central route from ribonucleotide pools toward the deoxyribonucleotides required for DNA.

Thymidylate synthase provides a separate one-carbon connection: it converts dUMP to dTMP using 5,10-methylene-tetrahydrofolate as the one-carbon donor, producing dihydrofolate. Dihydrofolate reductase uses NADPH to regenerate tetrahydrofolate. Folate therefore supports both purine-ring construction and thymidylate formation through distinct reactions.

## Worked example

**Problem.** A synthetic pathway preparation sends 6 mol IMP through its two branch-point conversions: 4 mol becomes AMP and 2 mol becomes GMP. How much GTP and ATP are consumed at those branch steps? Ignore upstream synthesis of IMP, PRPP formation, and later phosphorylation.

**Reasoning.** Each mol IMP directed to AMP uses 1 mol GTP, so the AMP branch consumes 4 mol GTP. Each mol IMP directed to GMP uses 1 mol ATP at the XMP-to-GMP step, so the GMP branch consumes 2 mol ATP. These are branch-conversion costs only, not the total energy cost of making nucleotides.

**Mixed-route accounting.** A second synthetic preparation makes 4 mol IMP de novo and salvages 3 mol hypoxanthine to IMP. With one mol PRPP used per mol IMP in each stated route, total PRPP use is 4 + 3 = 7 mol. If 2 mol of the resulting IMP are converted to AMP and 1 mol to GMP, those branch conversions consume 2 mol GTP and 1 mol ATP. Keep the PRPP, GTP and ATP ledgers separate; this count omits other pathway costs and does not predict cellular flux.

## Common mistakes

- Saying the purine ring is assembled before ribose attachment; purines are built directly on PRPP.
- Saying the pyrimidine ring is assembled on PRPP; orotate receives PRPP late in the pathway.
- Reversing the branch-point energy inputs: IMP-to-AMP uses GTP, while IMP-to-GMP uses ATP.
- Treating salvage as cost-free; salvage reuses a base but still consumes PRPP.
- Confusing ribonucleotide reductase, which makes dNDPs from NDPs, with thymidylate synthase, which makes dTMP from dUMP.
- Treating a pathway branch ATP/GTP count as the full energy cost of nucleotide synthesis.
- Omitting PRPP from purine salvage or combining PRPP demand with the separate ATP/GTP branch ledger.

## Practice and references

The accompanying questions are open formative checks with unlimited retries; responses are not collected or graded. See the link-only [KEGG purine pathway](https://www.kegg.jp/pathway/hsa00230), [KEGG pyrimidine pathway](https://www.kegg.jp/pathway/map00240), and reviewed [Reactome purine](https://reactome.org/content/detail/R-HSA-73817), [pyrimidine](https://reactome.org/content/detail/R-HSA-500753), [purine-salvage](https://reactome.org/content/detail/R-HSA-74217), [ribonucleotide-reduction](https://reactome.org/content/detail/R-HSA-111751) and [thymidylate-synthesis](https://reactome.org/content/detail/R-HSA-73605) entries. No pathway diagram, source text or table is reproduced here.
