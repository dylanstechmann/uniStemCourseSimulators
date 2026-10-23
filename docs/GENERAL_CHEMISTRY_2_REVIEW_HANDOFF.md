# General Chemistry II course review handoff

This handoff targets General Chemistry II: Kinetics, Acid–Base Systems & Coordination Chemistry, package version 0.6.0. The [review snapshot](GENERAL_CHEMISTRY_2_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded. The local General Chemistry I/II boundary divides one integrated 5.111SC comparator and does not claim two independent course equivalents.

## Review scope

- Review the proposed schedule, prerequisites, objective/outcome associations and mathematical level.
- Independently recalculate representative public buffer, kinetics, electrochemical, coordination, solubility, relaxation-lab and self-assessment work.
- Check the new portfolio's half-reaction scaling, charge and electron balance, standard cell potential, Gibbs-energy and equilibrium signs, reaction quotient, Nernst correction, and current–time–extent conversion.
- Confirm that the `A` and `B` tokens, potentials and activities remain explicitly fictional, and that the charge calculation is not presented as measured chemical yield.
- Compare the week-3 titration-curve reading with MIT OCW 5.111SC Unit III Lectures 22–24; independently recalculate the equivalence concentration, the start, buffer, half-equivalence, equivalence and beyond-equivalence pH values for the weak- and strong-acid curves, the exact charge-balance comparison, and the diprotic equivalence volumes. Confirm that indicator ranges are labelled illustrative and that nothing is presented as a laboratory procedure.
- Check the week-8 project guide and its rehearsal: the restated half-reactions and inputs against the draft, the worked example on a separate fictional cell, the rehearsal's balance, free-energy, Nernst and charge keys, and the wording of the five milestone self-checks. Confirm that the guide and rehearsal do not reveal the project's own results.
- Check the relaxation lab's dataset link, which now resolves to the package-pinned CSV.
- Review whether the paper-only draft complements the existing synthetic relaxation lab and preserved case; assess notation, accessible alternatives, manual accessibility and likely workload.

## Author-side evidence and its limits

Historical version 0.4.6 records a focused suite of 110 passing tests, including independent recomputation of the redox portfolio and the earlier package snapshot identity. No tests were run for version 0.4.7. For 0.4.8 the General Chemistry II recalculation file recomputes all 72 numeric keys. The eight new keys come from an exact charge-balance solution at each titrant volume rather than the region-by-region shortcuts the reading teaches, and the equivalence volumes are located from the steepest point of the computed curve. A further test checks the values stated in the reading. For 0.5.0, a dedicated test recomputes every rehearsal key independently: electron counts from a least common multiple, potentials as exact fractions, the Nernst potential by bisection on the free-energy relation rather than the rearranged equation, and the charge amounts exactly. It also recomputes the guide's worked example, checks that the guide, worked example, cards and rehearsal items do not state the project's own results, and checks that the lab and guide links resolve in the application. The full-suite result is in the validation report. These checks come from the same AI-assisted authoring effort. These earlier author-side results do not establish independent chemical review, accessible learner usability, semester workload, student learning or university equivalency. Graded homework, exams and a laboratory sequence remain absent; the project is inactive and ungraded.

## Review record to complete only after review

After a review actually occurs, record reviewer name and qualifications, date, package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for chemical and mathematical correctness, instructional design, assessment, accessibility, workload and release. Do not infer approval from the package hash or test results.

## Coupled speciation/coordination/evidence target (2026-10-22)

Current target 0.6.0 adds three foundations and three connected reports. Check free/protonated/bound ligand and spectator-charge signs, closed versus imposed-h/free-ligand boundaries, spectral units and occupation/pair/spin-only assumptions, reduced mechanism equivalence/discrimination/time scales and full-network limits, and free-to-total redox factors/Nernst signs. Eighteen checkpoints/cards assess selected outputs; solvers, reports, proposed studies, actual chemical validity, workload and qualified review remain open. The reduced-rate CSV is analytic, not measured. Earlier evidence remains historical; the current snapshot pins the package.
