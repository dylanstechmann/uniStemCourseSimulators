# Chemical Process Design & Scale-Up 0.1.0 review handoff

## Scope and provenance

Chemical Process Design & Scale-Up 0.1.0 is an explicitly partial advanced university/industry survey, unreviewed and formative-only. It contains eight lesson routes in six thematic modules, 24 lesson objectives, eight course outcomes, 48 public formative questions worth 56 points, 24 base numeric items plus 24 authored numeric variants, 24 retrieval cards, six zero-point self-assessed cases (one integrative case plus five capstone milestones) and two public synthetic CSV resources.

Chemical Engineering Foundations and Signals, Systems & Feedback Control are required; Materials Engineering for Fabrication, Statistics and Laboratory Safety and Biosafety are recommended where the graph permits. The package is appended after Chemical Engineering Foundations in the existing chemical-process-engineering pathway without changing the ten-pathway count. Required/recommended references are valid and acyclic; all 36 catalog-only nodes remain separate.

The package was developed with substantial AI assistance on 2026-11-26. Readings, questions, variants, cards, cases, fictional generic processes/equipment and datasets are original CC BY 4.0. No third-party or owner-repository prose, standard, figure, table, problem, dataset, code, CAD or validation artifact was imported. This document records agent-run checks, not owner, subject-matter, engineering, process-safety, inspection, statistical, quality, regulatory, accessibility, validation or release review.

## Actual sources inspected

The following official pages were retrieved successfully on 2026-11-26 and used as link-only comparators/references:

1. [MIT OCW 10.490 Integrated Chemical Engineering I, Fall 2006 — syllabus with calendar](https://ocw.mit.edu/courses/10-490-integrated-chemical-engineering-i-fall-2006/pages/syllabus/). Design, model limitations, economics, safety/environment and project scope were compared. The requested Fall 2005 URL returned HTTP 404; the verified official Fall 2006 edition is registered instead and the correction is explicit. Registry ID: `mit-ocw-10-490-fall-2006-syllabus`.
2. [MIT OCW 10.491 Integrated Chemical Engineering II, Spring 2006 — syllabus with calendar](https://ocw.mit.edu/courses/10-491-integrated-chemical-engineering-ii-spring-2006/pages/syllabus/). Continuous conceptual design, flowsheet models, economics, alternatives, HAZOP and team design-report scope were compared. Registry ID: `mit-ocw-10-491-spring-2006-syllabus`.
3. [OSHA 29 CFR 1910.119](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.119). Process safety information, hazard analysis, mechanical integrity, MOC, PSSR and incident-learning scope were checked. Registry ID: `osha-29cfr1910-119-public`.
4. [NIST/SEMATECH Process or Product Monitoring and Control](https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm). Monitoring, capability, charts and time-series scope were checked; the existing link-only record was extended. Registry ID: `nist-sematech-process-monitoring-control`.
5. [ASME BPVC.VIII.1 Section VIII Division 1 public catalog](https://www.asme.org/codes-standards/find-codes-standards/bpvc-viii-1-bpvc-section-viii-rules-construction-pressure-vessels-division-1). The verified public page displays the 2025 edition and broad proprietary design/fabrication/inspection/testing scope. No standard text or acceptance criterion was accessed or imported. Registry ID: `asme-bpvc-viii-1-public-catalog`.
6. [FDA Process Validation: General Principles and Practices, January 2011](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/process-validation-general-principles-and-practices). Lifecycle and continued-verification context was checked; no process validation or regulated disposition is performed. Registry ID: `fda-2011-process-validation`.

Existing mappings were appended without deleting prior mappings: control, statistics, MIT 10.302, MIT 3.032, mechanics, the laboratory-safety OSHA record, NIST/SEMATECH, habitat-resource-sandbox and rural-florida-agriculture. New link-only owner application records cover open-perfusion-rig and perfusion-calibration-lab. All owner repositories are presented as personal hobby and learning projects; no code or artifacts were copied and no owner review is implied. The [scope crosswalk](../../content/courses/chemical-process-design-scale-up/scope-crosswalk.md) distinguishes covered, shallow and absent/deferred topics.

## Evidence to review

- [Course manifest](../../content/courses/chemical-process-design-scale-up/course.json), [syllabus](../../content/courses/chemical-process-design-scale-up/syllabus.md), [source map](../../content/courses/chemical-process-design-scale-up/source-map.json) and [scope crosswalk](../../content/courses/chemical-process-design-scale-up/scope-crosswalk.md).
- Six original module readings of approximately 1,095–1,211 words each, plus an approximately 892-word lab guide and 1,064-word capstone guide.
- [Practice bank](../../content/courses/chemical-process-design-scale-up/question-banks/practice.json), [retrieval cards](../../content/courses/chemical-process-design-scale-up/question-banks/retrieval-cards.json) and [zero-point cases](../../content/courses/chemical-process-design-scale-up/rubrics/case-studio.json).
- [Synthetic process-design/safety/equipment evidence CSV](../../content/courses/chemical-process-design-scale-up/labs/process-design-evidence.csv): eight scenarios with heat recovery, NPV, lag-one residual correlation and scale ratios recomputed for every row. Reused scenario rows and repeated residuals are explicitly correlated/descriptive, not independent replication; all eight evidence states remain HOLD.
- [Synthetic industry design-review rehearsal CSV](../../content/courses/chemical-process-design-scale-up/assignments/industry-design-review-rehearsal.csv): nine scenarios with NPV, lifecycle and CAPA arithmetic. R01–R08 fail successive G0–G7 evidence gates and remain `HOLD` / `evidence_gaps_remain`; R09 alone is `synthetic_review_complete`, which grants no real readiness or release.
- [Independent package tests](../../tests/content/test_chemical_process_design_scale_up_package.py): all 48 numeric forms recomputed with misconceptions, domains and tolerance boundaries; every lab/rehearsal CSV relationship recomputed; all grader paths, G0–G7 holds, correlated-record disclosures, source/case/resource links and no-operational/no-release boundaries checked.

## Checks completed

| Check | Result |
| --- | --- |
| `.venv/bin/python -B tools/validate_content.py --root . --json` | Passed with zero errors/warnings: **33 courses, 727 lessons, 4,295 questions, 2,456 cards and 201 cases**. |
| `.venv/bin/python -m pytest tests/content/test_chemical_process_design_scale_up_package.py -q` | **10 passed**. |
| Final focused package/global suite: new package plus four preserved packages, course-plan, assessment-candidate and robotics recalculation tests | **216 passed**. |
| Affected global inventory, syllabus, pathway, cycle and assessment-outcome selections in `test_content_validation.py` | **5 passed, 96 deselected**; the known approximately 20-minute full module was not rerun unnecessarily. |
| `.venv/bin/python -m pytest backend/tests/test_content_repository.py backend/tests/test_case_studio.py -q` | **41 passed**, one existing Starlette deprecation warning. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after canonical regeneration: 33 packages, 727 lessons, 1,983 objectives and 4,295 practice items. One pre-existing Statistics no-practice-item note remains; no new unmapped objective/outcome was introduced. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after canonical regeneration: 33 packages and 26 inactive candidates, with no candidate activated. |
| `.venv/bin/ruff check .` | Passed. |
| `git diff --check` | Passed. |
| `tools/course_package_digest.py --course-id chemical-process-design-scale-up` | Version 0.1.0; 17 files; 260,105 archive bytes; archive SHA-256 `ca0d476a968e5b9a30c6a0be6ce11a9c5ae6583267cd9014ba2d785fc16665ee`; manifest SHA-256 `04a87213a7da06c9be9036504e65f99453d667b03406248d8483b85c95727972`. |

The first focused run identified four prior-package assertions that pinned exclusive shared-source/pathway mappings. Those assertions were updated for the intentional append-only relationships; the corrected tests and the final complete 216-test focused run passed. No frontend files were edited or frontend checks run for this content/backend-only task. No commit or push was made.

## Limitations requiring human review

- Scientific/engineering correctness, process-safety and statistical reasoning, standards/regulatory interpretation, instructional sequencing and university/industry depth have not been reviewed by a qualified person. Counts and arithmetic tests do not establish course completeness or measured workload.
- All species, equipment, scenarios, frequencies, probabilities, risks and measurements are fictional. No physical data, independent replication, equipment qualification, process capability or validation exists. Numeric precision supports reproducible grading, not measurement accuracy.
- No real chemical identifier, recipe, concentration, startup/shutdown, bypass/isolation, emergency or waste-transport instruction is supplied. No wall thickness, weld parameters, WPS/PQR, pressure-test/NDE instructions, relief sizing, dispersion/explosion design or equipment duty rating is supplied.
- No controller download, pilot run sheet, production setpoint, regulated batch disposition, process validation or commercial release is supplied. LOPA arithmetic cannot assign SIL, tolerable risk or approve an IPL; RPN is not probability.
- Missing compatibility, inspection, safety or acceptance evidence is unresolved, never zero or pass, and always produces HOLD. Synthetic dispositions are limited to `synthetic_review_complete` and `evidence_gaps_remain`; neither is `production_approved`.
- Reused scenario rows and repeated instrument records are correlated and descriptive, not independent replication. Real readiness requires named qualified process, mechanical/materials, control, safety, inspection, operations, quality and regulatory reviewers and current authoritative standards.
- Unicode equations, text-based PFD/barrier descriptions and CSV usability/accessibility need review. No frontend, browser, accessibility or measured-workload review was performed.
