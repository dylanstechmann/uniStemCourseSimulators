# Materials Engineering for Fabrication scope crosswalk

This crosswalk covers version 0.1.0, an explicitly partial advanced university/industry design-review survey with eight routes grouped into six modules. It was compiled with AI assistance on 2026-11-26 from the original local readings and official public comparator pages. It is an **agent-run comparison**, not scientific, engineering, statistical, metrology, standards or release review. Topic alignment establishes no equivalence, credit, endorsement, physical validation, supplier approval or production readiness.

## Comparator boundaries

[MIT OCW 2.008 Design and Manufacturing II, Spring 2025 — calendar](https://ocw.mit.edu/courses/2-008-design-and-manufacturing-ii-spring-2025/pages/calendar/) sequences injection molding, thermoforming, CAD/CAM and CNC, metal cutting, assembly/disassembly, joining, quality and SPC, design review, manufacturing planning/cost/system simulation, forming, casting and additive processes, plus a yo-yo project. This package compares those topics at a non-operational design-review level. It deliberately imports none of the lectures, labs, CAD/CAM, homework, quizzes, project or machine settings.

[MIT OCW 2.830J Control of Manufacturing Processes (SMA 6303), Spring 2008 — calendar](https://ocw.mit.edu/courses/2-830j-control-of-manufacturing-processes-sma-6303-spring-2008/pages/calendar/) covers manufacturing variation, probability models, parameter estimation, sampling, hypotheses, Shewhart SPC, capability, alternative/advanced/multivariate SPC, yield, ANOVA, factorial/fractional models, response surfaces, robustness, nested variance components and sequential experimentation. The local package selects measurement/subgroup/control/capability/yield foundations only. The requested short URL without `sma-6303` returned HTTP 404; the verified official calendar linked here is the registered source.

[MIT OCW 3.032 Mechanical Behavior of Materials, Fall 2007 — syllabus](https://ocw.mit.edu/courses/3-032-mechanical-behavior-of-materials-fall-2007/pages/syllabus/) connects continuum and atomistic/molecular mechanical behavior, elastic/plastic deformation, creep, fracture and processing across metals, ceramics and (bio)polymers, with physical laboratories. Local process–structure–property instruction is selective and paper-only; it does not reproduce those laboratories or deeper mechanical behavior.

The [NIST/SEMATECH Engineering Statistics Handbook process monitoring/control chapter](https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm) covers process-control concepts, capability, acceptance sampling, univariate/multivariate charts, time-series models and a case study. It is a link-only methods reference; no acceptance-sampling plan, source table, dataset or procedure is imported.

Existing MIT 3.091SC and 3.012 records provide materials foundations; `mechanics` supports load/mechanics prerequisites; `statistics` supports variance, sampling and independence. Their old mappings remain intact. Chemical Engineering Foundations is an optional acyclic process/monitoring cross-link, not evidence of deeper cure, transport, reaction or quality coverage.

## Topic status

**Covered** means an original local reading develops the topic with examples and public practice. **Shallow** means selected foundations are present but substantial depth remains. **Absent/deferred** means deliberately not taught here.

| Topic | Local route and status | Comparator and remaining boundary |
| --- | --- | --- |
| Service requirements and selection | [Lesson 1](modules/01-service-requirements-selection.md): **covered at design-review level** | Loads/temperature/media/wear/lifecycle/cost/throughput and evidence uncertainty are included. Full design optimization, supplier analysis and qualification are deferred. |
| Process–structure–property and defects | [Lesson 2](modules/02-process-structure-property-defects.md): **covered conceptually with bounded arithmetic** | Heat treatment, forming, residual stress, porosity, cure, fiber orientation and scatter are included. Detailed constitutive, transformation, fatigue/fracture and physical testing depth remains in later work. |
| Machining/casting/forming/molding/additive/powder routes | [Lesson 3](modules/03-process-comparison-dfm-dfa.md): **covered comparatively; shallow by design** | MIT 2.008 develops many with laboratories and analysis. Local comparison omits process physics derivations and all operating settings. |
| Welding/adhesive joining and DFM/DFA | Lesson 3: **covered at evidence-plan level** | Joint mechanisms, distortion, interface, aging, inspection and process-plan logic are included. Detailed joint design, procedures and qualification are absent/deferred. |
| Datums/GD&T/fits/stacks | [Lesson 4](modules/04-datums-gdt-fits-tolerance-stacks.md): **covered conceptually with synthetic arithmetic** | Worst-case and independent RSS are distinct. Full GD&T standards syntax, GPS standards, covariance/tail models and drawing approval are deferred. |
| Metrology and gauge R&R | [Lesson 5](modules/05-metrology-spc-capability-yield.md): **covered at concepts/evidence-design level** | Resolution, bias, repeatability/reproducibility and repeated-reading boundaries are included. Real ANOVA gauge R&R and calibration procedures are absent/deferred. |
| Subgrouping, charts, Cp/Cpk and yield | Lesson 5 and [lab](labs/fabrication-evidence-lab.md): **covered with stability/pooling boundaries** | MIT 2.830J and NIST cover much broader SPC, DOE and time-series material. Local unstable/improperly pooled Cp/Cpk is withheld, not rescued by arithmetic. |
| Drawing/BOM, risk and supplier evidence | [Lesson 6](modules/06-release-evidence-governance.md): **covered as evidence-gap review** | Revision, risk, control-plan, lot, first-article, nonconformance and change-control links are included. Standard-specific compliance and supplier approval are excluded. |
| Fabrication evidence lab | [Lab](labs/fabrication-evidence-lab.md): **covered for one original synthetic CSV** | Sixteen actual parts across four lots, repeated readings, clearances, stable-only capability and yields are recomputed. No physical validation or production capability exists. |
| Release-evidence project | [Project](assignments/release-gap-analysis-project-guide.md): **covered as zero-point fictional rehearsal** | Five scenarios test evidence gates and dispositions. Only R04 is synthetic_review_complete; real authorized release remains outside. |

## Link-only sources by module

| Module | Registered sources and exact use |
| --- | --- |
| 1 | MIT 2.008, MIT 3.032, existing mechanics and owner open-construction-equipment application link. No source exercises or design artifacts imported. |
| 2 | MIT 3.032, existing MIT 3.091SC/3.012/mechanics and MIT 2.830J for materials, mechanics and variation breadth. |
| 3 | MIT 2.008 for process-family breadth and owner application context. Every scenario and arithmetic input is newly invented. |
| 4 | MIT 2.008 for assembly/design review/measurement context and existing statistics for variance/independence. No GD&T standard copied. |
| 5 | MIT 2.830J, NIST/SEMATECH and statistics for monitoring/capability/metrology context. No source data or sampling plan imported. |
| 6 | MIT/NIST/statistics plus three owner repositories as link-only evidence/application context. Lab/project CSVs are original synthetic files. |

## Remaining gaps

- Detailed process physics, machine operation, feeds/speeds, CNC toolpaths, weld parameters, cure schedules, machine setups and process qualification.
- Full GD&T/GPS standards, formal drawing approval, advanced covariance/tail tolerance models and geometric inspection procedures.
- Physical gauge R&R/calibration, DOE, multivariate/time-series SPC, acceptance sampling, validated capability and independently collected production data.
- Full mechanical design, detailed joint/life design, quality-system regulation, supplier approval, procurement and production release.
- Qualified scientific/engineering/safety/statistical/metrology/standards/accessibility review, measured workload and named authorized human release.
