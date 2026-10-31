# Counting cells and viability with a hemocytometer

Most cell-culture decisions start with a number: how many cells to seed, how much medium to add, whether a thaw recovered well enough to use. The hemocytometer, already in routine use when Student analysed its errors in 1907, is the manual way to get that number. It gives two results from one preparation: the concentration of cells and the fraction that exclude trypan blue. This lesson treats the count as a measurement with a model, a geometry and an uncertainty, and shows which parts of the procedure come from sources and which are choices made for this course's simulation.

This is lesson 4 of the outlined cell-culture layer and, for now, the only lesson that exists. Lessons 1–3 and 5–8 (aseptic technique, media, passaging, cryopreservation, contamination, pluripotent stem cells and records) are not written yet. You practise the count in the [hemocytometer bench simulation](#/bench/hemocytometer-cell-count-viability), which uses synthetic, non-human cells.

## Learning objectives

By the end of this lesson, you should be able to:

1. Prepare a representative counting sample and calculate the overall dilution factor, including non-twofold and two-step dilutions.
2. Relate Improved-Neubauer geometry to the volume counted, and apply a consistent boundary rule that is kept separate from the stain decision.
3. Calculate viable-cell concentration and percent viability from two-chamber tallies.
4. Estimate Poisson counting uncertainty from the number of cells counted, state its assumptions, and plan how many squares to count for a target precision.
5. Interpret chamber disagreement, sparse or crowded fields and trypan-blue results, distinguishing counting error from systematic error and membrane integrity from overall cell health.

## A representative sample

Student, writing in 1907 about counting yeast with a haemacytometer, named the two main sources of error at the start of his paper: the drop may not represent the bulk of the liquid, and the cells are never spread perfectly evenly over the area counted. The second is the random counting error treated later in this lesson. The first is the preparation's job.

Cells in suspension settle within minutes, and adherent cells released by an enzyme can stay in clumps. Mix the suspension gently but thoroughly immediately before withdrawing the sample, take it from the middle of the liquid, and load the chamber promptly. An aliquot drawn from the top of a tube that stood for ten minutes undercounts. An aliquot drawn near the bottom overcounts. Both errors are invisible in the count itself.

The dye is usually added to the sample before loading, which dilutes it. The **dilution factor** is the total volume divided by the volume of cell suspension in it:

  dilution factor = (V_sample + V_dye) / V_sample.

Equal volumes (10 µL cells + 10 µL trypan blue) give (10 + 10)/10 = 2. Twenty microlitres of cells with 30 µL of dye give 50/20 = 2.5, not 30/20 = 1.5 and not "1:1.5". When a dense suspension is first diluted in medium, the factors multiply: 100 µL into 900 µL of medium is a factor of 10, and a subsequent equal-volume dye step makes the overall factor 10 × 2 = 20. Record each step and its volumes, not only the final factor.

## The chamber: geometry and volume

Marienfeld's description of its counting grids gives the Improved-Neubauer geometry: a chamber depth of 0.1 mm and a ruled area of 3 × 3 large squares, each 1 mm × 1 mm. The centre large square is divided into 25 group squares of 0.2 mm side, each holding 16 small squares of 0.05 mm side. The volume above one large square is therefore

  1 mm × 1 mm × 0.1 mm = 0.1 mm³ = 0.1 µL = 10⁻⁴ mL,

so every cell counted in one large square represents 10⁴ cells per millilitre of the loaded mixture. That number is a property of this geometry, not of hemocytometers in general. The same catalogue lists a Fuchs-Rosenthal chamber at 0.2 mm depth, where a 1 mm² square holds 0.2 µL and the factor is 5,000. Disposable chambers and other rulings differ again. Read the depth and ruling marked on the chamber and follow the device's instructions before applying any factor.

Marienfeld's instructions for use state the depth and handling cautions but deliberately do not describe filling or counting, which they leave to trained laboratory staff and the literature. The loading practice below is therefore common practice, not a manufacturer's protocol: clean and dry the chamber and coverslip, seat the coverslip on the raised supports before loading, and fill each side by capillary action in one smooth delivery from the edge. A chamber that overflows into the grooves, is under-filled or holds bubbles over the grid no longer has a known volume. Clean it and load again.

## Boundary decisions

Cells sit on the ruled lines as often as between them. On an Improved-Neubauer grid the large squares are bounded by triple lines, and Marienfeld describes the middle line as the dimension line, with the outer lines as aids for deciding whether a cell is inside. Your laboratory's procedure should say which line marks the edge.

Some rule is needed because a square is not an isolated object. A cell straddling the line between two squares would be counted twice if both squares included it, and not at all if both excluded it. This course uses a common convention that assigns every straddling cell to exactly one square:

- **Include** a cell that touches the **top** or **left** boundary.
- **Exclude** a cell that touches the **bottom** or **right** boundary.
- **At corners, exclusion wins.** A cell touching both the top and the right line is excluded here, because the square to its right sees it on that square's top and left lines and includes it. A cell on the top-left corner touches only including lines and is counted here.

Equivalent conventions exist, for example including bottom and right instead. The choice is less important than applying one rule consistently across every square, chamber and person. The bench simulation uses top/left, as its instructions state.

## Stain decisions are separate

Each cell needs two decisions, taken in order. The first is the **boundary decision**: is it inside the counted area? If not, it enters neither tally, whatever its colour. The second is the **stain decision**: if it is inside, is it unstained (dye excluded) or stained (dye taken up)? Mixing the two decisions produces specific errors. Counting every blue cell on the bottom and right lines while correctly excluding the unstained ones adds stained cells to the tally only. The viable-cell concentration is unchanged, but viability is biased low. Debris, clumps of several cells and faintly tinted cells need a written rule too: count a clump's individual cells if you can resolve them, and record that the sample clumped if you cannot.

## From tallies to concentration and viability

With an Improved-Neubauer chamber and one large square per chamber,

  viable cells/mL = mean included unstained count per large square × 10,000 × dilution factor,

  viability (%) = unstained / (unstained + stained) × 100.

Total cells per mL use the mean of all included cells instead. The dilution factor cancels in the viability ratio because stained and unstained cells were diluted together, which is also how Strober presents the calculation.

**Worked example 1: two chambers, twofold dilution.** Ten microlitres of a mixed suspension are combined with 10 µL of trypan blue (dilution factor 2). After the boundary rule, chamber A holds 41 unstained and 5 stained cells in its large square, and chamber B 47 unstained and 7 stained.

- Mean unstained = (41 + 47)/2 = 44, so viable cells/mL = 44 × 10,000 × 2 = 8.8 × 10⁵.
- Viability = 88/(88 + 12) × 100 = 88.0%.
- Total cells/mL = (46 + 54)/2 × 10,000 × 2 = 1.0 × 10⁶.

**Worked example 2: a non-twofold dilution and more squares.** Twenty microlitres of suspension are mixed with 30 µL of trypan blue (dilution factor 50/20 = 2.5). The four corner large squares are counted in each chamber.

| Chamber | Unstained per square | Stained per square | Totals |
| --- | --- | --- | --- |
| A | 31, 28, 35, 30 | 4, 6, 3, 5 | 124 unstained, 18 stained |
| B | 29, 33, 27, 32 | 5, 4, 6, 3 | 121 unstained, 18 stained |

Eight large squares were counted, so the mean unstained count per square is 245/8 = 30.625 and viable cells/mL = 30.625 × 10,000 × 2.5 = 7.66 × 10⁵. Viability = 245/281 × 100 = 87.2%. Dividing by 8 squares, not by 2 chambers, is the step most often missed when more than one square per chamber is counted.

## Counting uncertainty

Even a perfectly mixed suspension does not place the same number of cells over every square. Student showed that, when cells are distributed at random, the count per square follows what is now called the Poisson distribution, for which the variance equals the mean. He then gave the standard deviation of a mean count over M squares as √(m/M), where m is the mean per square. Since the total number counted is N = mM, the relative standard deviation is √(m/M)/m = 1/√N. As a percentage:

  relative counting uncertainty ≈ 100/√N %.

A count of 100 cells carries about 10%; 400 cells about 5%. Precision improves with the number of cells counted, not with the number of chambers as such. Apply N to the quantity you report. For a total-cell concentration, N is all included cells: 281 in worked example 2, giving 5.97%. For the viable concentration alone, N is the unstained count, 245, giving 6.39%. The bench simulation asks for the total-count value, 100/√(all included cells), as its instructions say.

The formula assumes that cells are independent and randomly distributed, that each is counted and classified correctly, and that the volume is known. Student noted that the error is always larger when organisms occur as aggregates of varying size. Poisson uncertainty therefore describes counting variation only. It excludes an unrepresentative aliquot, pipetting error in the dilution, a mis-filled chamber, a misapplied boundary rule, misclassified stains and dye exposure that runs too long. These are **systematic** errors: they shift every count the same way, and counting more cells does not reduce them.

To plan a count, invert the formula. A 5% target needs N = (100/5)² = 400 cells. At about 50 cells per large square that is 8 squares, for example four corners in each of two chambers.

## When chambers disagree, and sparse or crowded fields

Two chambers loaded from the same mixture should agree within counting variation. For counts a and b, the standard deviation of their difference is about √(a + b). Counts of 31 and 74 differ by 43 against √105 ≈ 10.2, more than four standard deviations. That is not counting noise. Suspect settling between the two loadings, an under-filled or overflowing chamber, or bubbles. Do not average the two numbers; remix, reload and count again.

Close agreement is not proof of accuracy either. Both chambers loaded from one unmixed aliquot share its bias, so they can agree well and both be wrong. Replicate agreement measures **precision**; only a better preparation, or comparison with an independent method, addresses **systematic error**.

Field density limits both kinds of error. A field with a handful of cells per square has a large relative counting uncertainty: count more squares, or concentrate the cells and record the new factor. A crowded field has overlapping cells that are hard to assign and classify: dilute further, recalculate the dilution factor and recount. The bench simulation flags fields outside 20–80 cells per displayed square. That range is a teaching choice for its synthetic fields, not a laboratory acceptance criterion; real ranges come from your laboratory's procedure.

## What trypan-blue exclusion shows

Strober's protocol describes trypan-blue exclusion as an indirect estimate of viability from membrane integrity: cells with intact membranes exclude the dye and keep a clear cytoplasm, while cells with damaged membranes take it up and appear blue. Several of its practical cautions shape how a count is done:

- Serum proteins also take up the dye and can mislead, so the count is made in serum-free solution such as buffered saline.
- Counting should be done within a few minutes of mixing; Strober gives 3 to 5 minutes, because longer exposure kills cells and lowers the apparent viability.
- Small amounts of dye uptake are easy to miss by eye, and visual scoring varies between people.
- A cell with an intact membrane may already have lost the ability to grow or function, and some membrane damage can be repaired.

So a viability of 90% means that about 90% of the counted cells excluded the dye at the moment of counting. It does not show that the culture will grow, that the cells have the intended phenotype, that the culture is free of bacteria, fungi or mycoplasma, or that the cells are healthy in any broader sense. Other assays answer those questions. Trypan blue is a hazardous chemical; read the safety data sheet for the product you use.

## The biosafety boundary

The simulation uses synthetic, non-human cells. Real counts of human or other primate cells are different. Appendix H of BMBL, 6th edition (CDC and NIH, 2020, pp. 466–468), says that risk rises with human and other primate cell lines and with primary cells, and that the assessment considers the tissue source, cell type and culture type. At a minimum, human and primate cells are treated as potentially infectious and handled with BSL-2 practices, engineering controls and facilities. BMBL calls a biological safety cabinet for culturing the universally accepted best practice, requires waste culture material to be decontaminated, and says staff should be enrolled in an occupational medical program for bloodborne pathogens. A loaded hemocytometer is contaminated material and must be decontaminated after use. Neither this lesson nor the simulation establishes competency to handle human cells; that requires your institution's risk assessment, training and supervision.

## Practise in the bench simulation

Open the [hemocytometer bench simulation](#/bench/hemocytometer-cell-count-viability) and work through it as a formative exercise:

1. Mix the suspension, prepare the 10 µL + 10 µL trypan-blue mixture, seat the coverslip and load chamber A, then chamber B.
2. In each field, decide the boundary for every cell before its stain. You can click the cells, or move between them with the keyboard. Some drawn cells overlap; select a covered cell from the text list below the field. Record each chamber's included unstained and stained tallies.
3. Calculate viable cells/mL, viability and the Poisson uncertainty of the total count by hand, then submit.
4. Read all nine checkpoints in the debrief, from mixing and dilution through boundary rule, density and the three calculations. For each one that is not met, find the step in this lesson that explains it. Then run it again and change one thing deliberately, for example skip the mixing step, and see which checkpoints respond.

The debrief compares your calculations with your own tallies. Its tolerances (0.2% for concentration and viability, 0.5% for uncertainty) are rounding allowances, not measurement accuracy. At the end it reveals the synthetic culture's generating values, which a finite count only estimates. Nothing is graded or recorded as a qualification.

## Common mistakes

- Using the ratio of dye to sample (30/20) instead of total over sample (50/20) as the dilution factor.
- Forgetting a pre-dilution in medium, or adding dilution factors instead of multiplying them.
- Dividing the total count by the number of chambers when several squares per chamber were counted.
- Counting a cell on the right or bottom line because it is blue: the boundary decision comes first.
- Averaging two chamber counts that disagree by far more than counting variation.
- Treating close replicate agreement, or a high viability, as proof that the count or the culture is right.

## Sources and simulation choices

| Statement in this lesson | Basis |
| --- | --- |
| Improved-Neubauer depth 0.1 mm, 1 mm² large squares, 0.1 µL per large square; triple lines with the middle line as the dimension line; Fuchs-Rosenthal 0.2 mm | Marienfeld counting-grid description, catalogue pp. 58–61 (link only) |
| Instructions for use leave filling and counting to the laboratory | Marienfeld instructions for use, counting chambers according to DIN 12847 (link only) |
| Two sources of counting error; variance equals the mean; SD of a mean count √(m/M); larger error with aggregates | Student, *Biometrika* 5(3):351–360, 1907, pp. 351, 353, 359–360 |
| Membrane-integrity principle, serum-free counting, 3–5 minute window, subjectivity and limits of the test | Strober, *Curr Protoc Immunol* 111:A3.B.1–A3.B.3, 2015 (link only) |
| Human and primate cells at BSL-2 minimum; risk factors; occupational medical program | BMBL 6th edition, Appendix H, pp. 466–468 (US federal work, adapted) |
| Top/left inclusion, exclusion at corners; loading steps | Common practice taught as this course's convention; follow your device and laboratory procedure |
| Twofold target dilution, 20–80 cells per field, 0.2% and 0.5% tolerances, uncertainty from all included cells | Simulation choices for teaching, not laboratory acceptance criteria |

All examples and numbers are synthetic. Full source records, links and access dates are in the repository's source registry and in this package's scope crosswalk, which the syllabus links.
