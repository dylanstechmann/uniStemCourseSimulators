# Thermodynamics & Transport in Bioengineering

**Maturity: partial. Version: 0.6.0.**

Conservation laws, thermodynamic driving forces, fluid mechanics, heat and mass transfer, and scaling applied to cells, tissues, and bioprocess equipment.

## Prerequisites

Differential Equations; Physics: Mechanics; General Chemistry II. Structured required, recommended, and concurrent relationships appear in the manifest and remain subject to author review. This package establishes no university prerequisite equivalency.

## Authored outcomes

- Write control-volume balances for mass and energy.
- Apply diffusion and advection models with boundary conditions.
- Estimate flow regime and pressure drop.
- Use dimensional analysis to select dominant mechanisms.
- Write entropy balances for closed and steady-flow systems and assess consistency with the second law.
- Relate chemical-potential differences to reaction Gibbs energy and equilibrium, and calculate composition for a stated ideal mixture.
- Analyze phase partitioning, nonideal mixture stability and electrochemical or osmotic driving forces under explicit thermodynamic and transport assumptions.

## Proposed 14-week schedule

This is a proposed scope, not a measured or reviewed semester. Week 1 links control-volume balances, entropy and chemical equilibrium in a thermodynamic foundation; the course retains a 14-week proposal.

| Week | Readings and activities |
| --- | --- |
| 1 | [Control volumes and conservation](modules/01-control-volumes-and-conservation.md); [Entropy balances and irreversibility](modules/14-entropy-balances-and-irreversibility.md); [Chemical potential and reaction equilibrium](modules/15-chemical-potential-and-reaction-equilibrium.md) |
| 2 | [Well-mixed chambers: residence time, wash-in and washout, and tanks in series](modules/12-residence-time-and-tanks-in-series.md); [Activities, phase partitioning and nonideal stability](modules/mixtures-and-phase-equilibrium.md) |
| 3 | [Diffusion, reaction, and characteristic length](modules/02-diffusion-reaction-and-characteristic-length.md); [Electrochemical potentials, coupled energy and solvent flux](modules/electrochemical-coupling.md) |
| 4 | [Transient diffusion: penetration depth, the error function and equilibration times](modules/07-transient-diffusion-and-the-error-function.md); [Finite-volume diffusion, boundary geometry and conservation](modules/conservative-diffusion-models.md) |
| 5 | [Oxygen limits in thick constructs: zero-order uptake, critical thickness and time scales](modules/05-oxygen-limits-in-thick-constructs.md); [Assignment 1: phase and free-energy ledger](assignments/coursework-01-phase-ledger.md) |
| 6 | [Oxygen in a spheroid: the critical radius, the anoxic core and why the rim is not a constant thickness](modules/09-oxygen-in-a-spheroid-and-the-anoxic-core.md) |
| 7 | [When zero order fails: Michaelis–Menten oxygen uptake and a softer edge to the limit](modules/10-michaelis-menten-uptake-and-the-limits-of-zero-order.md) |
| 8 | [Virtual lab 1: oxygen depth profiles in cell-laden slabs](labs/01-oxygen-depth-profiles-in-cell-laden-slabs.md) |
| 9 | [Fluid mechanics and microvascular flow](modules/03-fluid-mechanics-and-microvascular-flow.md) |
| 10 | [Perfusing a culture through tubing: control-volume balances, Reynolds number and pressure drop](modules/06-perfusion-tubing-balances-and-pressure-drop.md); [Energy balances on flowing systems: the steady-flow first law, Bernoulli and friction losses](modules/16-steady-flow-energy-balances-bernoulli-and-friction-losses.md); [Assignment 2: coupled reservoirs and energy ledgers](assignments/coursework-02-coupled-reservoirs.md) |
| 11 | [Advection and diffusion together: the Péclet number and mass-transfer coefficients](modules/08-advection-diffusion-and-the-peclet-number.md) |
| 12 | [Heat transfer and coupled transport](modules/04-heat-transfer-and-coupled-transport.md) |
| 13 | [Heat transfer: lumped capacitance, the Biot number and thermal time scales](modules/11-heat-transfer-lumped-capacitance-and-the-biot-number.md); [Slab project guide: steady heat generation, an energy check and the lumped limit (optional, ungraded)](assignments/heat-generation-slab-project-guide.md) |
| 14 | [A perfused construct with a hypoxic center: advection supplies the channel, diffusion supplies the tissue](modules/13-perfused-construct-with-a-hypoxic-center.md); [Assignment 3: conservative transport verification](assignments/coursework-03-transport-verification.md) |

## Assessment and study policy

The package has 24 readings/activity guides, 137 public practice items and 81 retrieval cards. Lessons use mapped formative checks, including numeric, choice, structured-response and CSV-upload items. Week 8 is a synthetic-data virtual lab; week 14 pairs an integrative transport lesson with an inactive course-case draft. These are open, ungraded activities with no institutional or transferable credit. Workload has not been measured.

## Connected coursework (open, ungraded)

Three original packets in weeks 5, 10 and 14 require a phase/free-energy ledger, coupled ion/solvent balances and a conservative transport verification study. Each supplies distinct paper-model inputs, derivation/simulation tasks, selected checkpoint fields and self-review evidence. Learners save implementations/reports locally; no code, prose or plot is automatically evaluated. The existing lab and project remain separate. Workload has not been measured; the 14-block label does not establish a semester equivalent.

## Optional heat-generation slab project (ungraded)

The [slab project guide](assignments/heat-generation-slab-project-guide.md) makes the project below usable as open practice. It restates the project's slab, conditions and tasks, works a separate slab, and pairs a rehearsal slab with open practice items in week 13. Five milestones, suggested for weeks 13–14, are Case studio self-checks whose responses can be saved privately and are not submitted for grading.

## Inactive integrative project draft

The [steady heat-generation slab portfolio](assessment-specs/heat-generation-slab-project-draft.md) derives a one-dimensional steady temperature field with internal generation, then checks boundary flux, the mean temperature and the lumped-model limit using synthetic thermal values. The draft itself is an authoring draft only: not scheduled, assigned, submitted, collected or graded, and the open project guide above does not submit work to it. The course-case draft is self-assessed and inactive. It is not scheduled or graded and does not give design, laboratory or medical advice.

## Current limitations

The 14-week proposal is unmeasured and unreviewed; there are no graded homework sets, midterm, cumulative final or completed laboratory sequence. The new phase/activity, electrochemical/coupled/osmotic and finite-volume readings extend the former single ideal-reaction example. They develop selected models; general nonideal phase diagrams, statistical thermodynamics, self-consistent multi-ion fields and general CFD remain beyond the selected combined scope. The oxygen-construct models are first-order teaching estimates, not design methods. All data and values are synthetic, and qualified human review is required before the course could meet a complete-course standard.

## Sources and licensing

MIT OCW 20.110J Fall 2005 is a broad undergraduate thermodynamics comparator; its calendar places equilibrium/free energy, chemical potential and chemical equilibrium in sessions 8–12. The original A⇌B lesson is narrower. The calendar and Lecture 9 resource are link-only; no source assets are copied or adapted. See [content/SOURCES_AND_LICENSES.md](../../SOURCES_AND_LICENSES.md). No affiliation or equivalency is implied.

The 2026-10-22 expansion compares the actual original readings/examples with 20.110J Fall 2005 phase/nonideal/osmotic topics and 20.330J Spring 2007 ion-transport/conservation/diffusion foundations. It adds original derivations and connected coursework, not imported university assignments. This personal hobby and learning project uses substantial AI assistance; no owner walkthrough or qualified approval is implied.
