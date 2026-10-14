# Repository-wide roadmap

The active scope is all 25 partial course packages and their shared learning platform. No package is complete or independently reviewed. Historical authoring and validation records remain in [PROGRESS_REVIEW.md](PROGRESS_REVIEW.md), [VALIDATION_REPORT.md](VALIDATION_REPORT.md), and the course review packets; they are not the current work queue.

## Next bounded instructional rotation

The [2026-10-11 scope audit](COURSE_SCOPE_AUDIT.md) compares all 25 authored packages with relevant official MIT OpenCourseWare courses and records covered, limited and deferred topics. Recent completed batches are recorded in [PROGRESS_REVIEW.md](PROGRESS_REVIEW.md) and [VALIDATION_REPORT.md](VALIDATION_REPORT.md). Organic Chemistry I, Statistics, Thermodynamics & Transport, Programming & Numerical Methods, Cell & Molecular Biology, Physics II: E&M, the General Chemistry I/II sequence, Biomaterials & Tissue Engineering, Signals & Feedback Control, Bioreactors, Differential Equations and Statics & Mechanics of Materials have delivered bounded batches. The React reader has a searchable cross-course notebook. Organic Chemistry I now pairs EAS with an SNAr strand, Linear Algebra has a determinants reading before eigenvalues, Bioreactors teaches fed-batch operation between batch exhaustion and continuous culture, Signals & Control adds Routh–Hurwitz and the root locus to its feedback week, Physiology adds passive membrane and cable properties to its membrane-potential week, Circuits & Instrumentation adds op-amp summing, integrators, differentiators and active filters to its feedback week, Calculus II adds trigonometric integrals, trigonometric substitution and completing the square to its methods week, and Robotics adds gravity compensation and computed-torque control to its dynamics week. Continue rotating across courses.

| Order | Course | Deliverable | Acceptance evidence |
| --- | --- | --- | --- |
| 1 | Second pass over thinly covered packages: Genetics, Physiology or Signals & Control | Select one audited foundational gap and integrate it into an existing week. | Inspect actual readings against the official MIT OCW calendar; integrate rather than append a week; add independent recalculations for every new numeric key and run the full suite. |
| 2 | Owner decision: Cell Biology and Biochemistry re-pinning | Cell Biology 0.61.1 lost its syllabus week-8 links to the two synthesis readings, and its homework/lab packets and the Biochemistry kinetics lab carry stale package-version labels. Correcting them changes files frozen inside assessment-candidate prerequisite digests and the Cell Biology workload-pilot pin. | A deliberate release that re-binds candidate digests and repins the workload protocol, chosen by the owner; not a silent relabel. |

Each batch ends when its stated instructional outcome and relevant checks pass. Integrate new material into a defensible course sequence instead of appending another nominal week. Bundle required version, source-map, digest and review-report changes once with that batch. Do not select report regeneration, version relabeling, empty review scaffolds or another near-duplicate case as the next milestone.

## Scope and redundancy cleanup

- Define core versus optional applications in Cell Biology and Biochemistry. Both packages now state their scope boundaries and consolidate repeated explanations. Pending human review is a separate gate, not a reason to keep extending either package.
- Group the compact-primer and expanded-treatment readings into shared calendar blocks in General Chemistry; Organic Chemistry has already grouped four such pairs while retaining stable lesson IDs.
- Clarify the local Calculus I/II and General Chemistry I/II divisions; each pair shares an MIT comparator sequence. They are not four independent MIT-equivalent courses. General Chemistry I groups compact/expanded reading pairs within a ten-week sequence, and the new paired-course crosswalk records the I/II handoff and deferred topics.
- Resolve the Thermodynamics & Transport title/scope mismatch: author a bounded thermodynamics strand or narrow the declared title. The Biomaterials/Tissue and merged Signals/Control boundaries are now documented.
- The Mechanics centrifuge discussion is bounded to stipulated models; a separate week-6 variable-mass momentum sequence now addresses the audited recoil/mass-flow gap.
- Calculus III now integrates theorem choice, boundary orientation, cylindrical volume bounds and direct checks in its existing week-13 Stokes lesson.
- Link common Statistics/Programming foundations rather than repeatedly teach experimental units, uncertainty and data validation in every applied course. Retain domain-specific reasoning and distinct worked problems.

The audit retains open work for every package. Cellular Biomechanics, Geroscience, Biochemistry I, Organic Chemistry I, Statistics, Thermodynamics & Transport, Programming & Numerical Methods, Cell & Molecular Biology, Physics II: E&M, General Chemistry I/II, Biomaterials & Tissue Engineering and Signals & Feedback Control have recent bounded deliveries. The next course batch checks whether the bioreactor package's animal-cell focus is coherent within the 10.442 comparator boundary and selects one fitting foundational gap.

## Shared platform

Delivered: guest/account access; version-pinned enrollment; server-backed notes, progress, bookmarks and practice; formative gradebooks; retrieval scheduling; protected graded-assessment infrastructure and appeal/archive handling; public curriculum explorer; six scientific calculators; and a shared React case studio for all 25 packages.

The case studio supports private drafts, version/prompt snapshots, conflict protection, earlier response history, account export/deletion and read-only archived cases. Historical feature-batch verification is recorded in the linked review reports. Since 2026-10-13 each batch runs the full root, backend and frontend suites; earlier batches recorded "no test suite was run", and the drift they left was repaired in one pass. Platform verification is not course review or protected-exam release approval.

The searchable notebook reuses the existing private note store, exposes case-insensitive literal search with course filtering and pagination, and links matches back to enrolled course lessons. Remaining shared work should address a demonstrated learner workflow or blocker and fit alongside the instructional rotation. Avoid adding isolated grader types while course foundations remain thin.

## Course development and review

Apply the [quality standard](CONTENT_QUALITY_STANDARD.md) to each course's declared scope, level and appropriate assessment form. Official university references guide breadth, prerequisites and expectations; they do not establish affiliation, transfer credit or equivalent learning outcomes. Write original lessons, examples and problems and preserve attribution.

Develop coherent instruction, appropriately challenging assessment, source support, independent numerical/mechanistic checks and accessible activities. Do not infer mastery from an automatically scored choice or claim measured workload from a proposed 14-week schedule. Course-specific scientific, assessment, accessibility, workload and operator gates remain open until their actual evidence exists. The previous Cell Biology blueprint remains a local plan, not the repository's sole objective or the mandatory template for every subject.

## Catalog and operation

The catalog contains 25 authored partial packages, 37 planning nodes and eight pathway maps. Validate prerequisite edges and subject boundaries against appropriate references before promoting planning nodes to instruction. Preserve historical packages and assessment evidence during consolidation.

Operational work remains bounded by verified needs: deployment/backup and archive recovery, privacy and learner isolation, distributed throttling, accessibility and protected-delivery validation. The existing [historical assessment archive recovery runbook](HISTORICAL_ASSESSMENT_ARCHIVE_RECOVERY.md) documents conservative handling of unverifiable records. Local test passes do not establish public deployment readiness or independently reviewed courses.
