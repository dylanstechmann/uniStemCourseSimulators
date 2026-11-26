# Chemical Engineering Foundations 0.1.0 review handoff

## Scope and provenance

Chemical Engineering Foundations 0.1.0 is an explicitly partial university-level survey, unreviewed and formative-only. It contains eight lesson routes in six thematic modules, 24 lesson objectives, eight course outcomes, 48 public formative questions worth 56 points, 24 retrieval cards, six zero-point self-assessed cases (one integrative case plus five project milestones) and two public synthetic CSV resources. General Chemistry II and Calculus II are required; Transport, Statistics and Laboratory Measurement are recommended. The new `chemical-process-engineering` pathway contains eight existing/new package nodes and brings the map to ten pathways. The 36 catalog-only nodes remain, including unpromoted thermodynamics, fluid-mechanics and heat-mass-transfer nodes.

The package was developed with substantial AI assistance on 2026-11-26. Readings, questions, cards, cases, generic A/B/S scenarios and datasets are original CC BY 4.0. No third-party prose, figure, table, problem, dataset, code or operating procedure was imported. This document records agent-run checks, not owner, subject-matter, engineering, process-safety, operability or release review.

## Actual sources inspected

The following official pages were retrieved successfully on 2026-11-26 and used as link-only comparators:

1. [MIT OCW 10.302 Transport Processes, Fall 2004 — syllabus](https://ocw.mit.edu/courses/10-302-transport-processes-fall-2004/pages/syllabus/). The syllabus/calendar and laboratory context were compared with local continuity, friction, pump/system-curve, resistance, LMTD/NTU and correlation-applicability scope. Registry ID: `mit-ocw-10-302-fall-2004-syllabus`.
2. [MIT OCW 10.40 Chemical Engineering Thermodynamics, Fall 2003 — syllabus](https://ocw.mit.edu/courses/10-40-chemical-engineering-thermodynamics-fall-2003/pages/syllabus/). The graduate classical/statistical thermodynamics scope was compared with the much smaller local state/path, laws, energy and synthetic K-value flash treatment. Registry ID: `mit-ocw-10-40-fall-2003-syllabus`.
3. [MIT OCW 10.37 Chemical and Biological Reaction Engineering, Spring 2007 — syllabus/calendar](https://ocw.mit.edu/courses/10-37-chemical-and-biological-reaction-engineering-spring-2007/pages/syllabus/). Ideal reactors, selectivity, RTD, nonisothermal and broader biological/catalytic/transport scope were compared. Registry ID: `mit-ocw-10-37-spring-2007-syllabus`.
4. [MIT OCW 10.32 Separation Processes, Spring 2005 — syllabus](https://ocw.mit.edu/courses/10-32-separation-processes-spring-2005/pages/syllabus/). Equilibrium/rate separation, staged, membrane, adsorption and chromatography scope were compared. Registry ID: `mit-ocw-10-32-spring-2005-syllabus`.

**Source-term correction:** the requested 10.40 Spring 2012 and 10.32 Fall 2005 syllabus URLs returned HTTP 404. Official MIT search and the retrieved official pages verify 10.40 Fall 2003 and 10.32 Spring 2005. The package records and crosswalk use those actual editions and disclose the discrepancy rather than inventing sources.

Existing mappings were appended without deleting prior mappings: `chemistry` to modules 1–3, `transport` to modules 3–5, `statistics` to modules 2 and 6, and `control` to module 6. The local [scope crosswalk](../../content/courses/chemical-engineering-foundations/scope-crosswalk.md) distinguishes covered, shallow and absent/deferred topics. Comparator links establish no equivalence or endorsement.

## Evidence to review

- [Course manifest](../../content/courses/chemical-engineering-foundations/course.json), [syllabus](../../content/courses/chemical-engineering-foundations/syllabus.md), [source map](../../content/courses/chemical-engineering-foundations/source-map.json) and [scope crosswalk](../../content/courses/chemical-engineering-foundations/scope-crosswalk.md).
- Six original module readings of 884–969 words each, plus an 854-word reconciliation lab and 854-word project guide.
- [Practice bank](../../content/courses/chemical-engineering-foundations/question-banks/practice.json), [retrieval cards](../../content/courses/chemical-engineering-foundations/question-banks/retrieval-cards.json) and [zero-point cases](../../content/courses/chemical-engineering-foundations/rubrics/case-studio.json).
- [Synthetic reconciliation CSV](../../content/courses/chemical-engineering-foundations/labs/process-reconciliation.csv): nine correlated stream rows in three scenarios, with independent total/component closure checks, measured/reconciled separation and unknown blanks.
- [Synthetic flowsheet rehearsal CSV](../../content/courses/chemical-engineering-foundations/assignments/flowsheet-audit-rehearsal.csv): four distinct scenarios with two reactor-side closure relations each and recovery calculations only where declared; R04 separator outputs remain unknown.
- [Independent package tests](../../tests/content/test_chemical_engineering_foundations_package.py), which recompute all 24 base numeric answers and every CSV conservation/closure relationship, reject misconception responses and tolerance-boundary errors, execute all choice grader paths, check valid/invalid flash domains, and verify objective/source/case/resource links and non-operational boundaries. Version 0.1.0 has no numeric authored variants.

## Checks completed

| Check | Result |
| --- | --- |
| `.venv/bin/python -B tools/validate_content.py --root . --json` | Passed with zero errors/warnings: 31 courses, 711 lessons, 4,199 questions, 2,408 cards and 189 cases. |
| `pytest tests/content/test_chemical_engineering_foundations_package.py` | 11 passed. |
| `pytest tests/content/test_chemical_engineering_foundations_package.py tests/content/test_course_plan_completion.py tests/content/test_assessment_candidates.py tests/content/test_robotics_recalculations.py` | 175 passed. |
| `pytest tests/content/test_materials_science_package.py tests/content/test_agriculture_construction_habitats_package.py tests/content/test_cell_culture_practice_package.py` | 103 passed after the agriculture pathway lookup was made order-independent. |
| Affected `test_content_validation.py` inventory, pathway, assessment-outcome and syllabus tests | 5 passed, 96 deselected. |
| `pytest backend/tests/test_content_repository.py backend/tests/test_case_studio.py` | 41 passed, one third-party Starlette deprecation warning. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after canonical regeneration; 31 packages, 1,935 objectives and 172 outcomes. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after canonical regeneration; 31 packages and 26 inactive candidates, with no candidate activated. |
| Ruff on the new test and all changed Python test files | Passed. |
| `git diff --check` | Passed. |

No broad redundant content suite was run. Frontend files and checks were not changed or run for this content/backend-only task. Pre-existing dirty and untracked files, including Materials Science and Agriculture/Construction/Habitats, were preserved. No commits or pushes were made.

## Limitations requiring human review

- Scientific correctness, instructional sequencing and university-level depth have not been reviewed by a qualified person. Counts and arithmetic tests do not establish course completeness, measured workload or university equivalence.
- Full thermodynamic property methods, statistical thermodynamics, differential fluid/heat/mass transport, advanced reaction engineering, staged/rate-based separations, process dynamics/control, process safety and detailed design remain shallow or deferred to distinct packages.
- Every species, process, property and observation is generic and synthetic. No physical data, independent replication or experimental validation exists. Numeric precision supports reproducible grading, not measurement accuracy.
- Synthetic K values do not describe a real mixture. An admissible flash root is not a phase-data prediction or operating condition; an invalid branch must be rejected rather than forced.
- Pump/system curves, friction terms, LMTD/NTU, ideal reactors and separation performance are reduced model concepts only. No correlation validation, scale-up, line/pump sizing, equipment rating, relief sizing, controller setting or operating target is supplied.
- Reconciliation is deterministic closure practice, not uncertainty-qualified estimation or sensor diagnosis. Scenario rows and derived columns are correlated records, not independent replicates. Missing values stay unknown, never zero.
- Arithmetic closure is not proof of safe or feasible operation. No real production recipe, hazardous operational condition, plant instruction, process-safety assessment or safety/release approval is supplied.
- Unicode equations, text-based flowsheet descriptions and CSV usability/accessibility need review. No frontend, browser, accessibility or measured-workload review was performed.
