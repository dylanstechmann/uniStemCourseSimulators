# Organic Chemistry I course review handoff

This handoff targets Organic Chemistry I for Life Sciences, package version 0.7.0. The [review snapshot](ORGANIC_CHEMISTRY_REVIEW_SNAPSHOT.md) identifies the exact public files. The package remains partial, unreviewed and formative-only; no reviewer or approval is recorded.

## Review scope

- Review the proposed 12-block schedule, prerequisites, outcome mappings and chemical level.
- Recalculate representative acid/base, substitution, elimination, alkene/alkyne addition, carbonyl/acyl-transfer, enolate/aldol, spectroscopic and calibrated-excess examples.
- Check the new alkene/alkyne lessons for mechanism, regiochemistry, stereochemistry, hydration and selective-reduction assumptions.
- Compare the local two-reading addition unit with MIT OCW 5.12 Spring 2005, whose calendar gives weeks 4–7 to alkene/alkyne reactions; judge its selective scope and deferred SNAr and multistep synthesis topics.
- Review the synthetic crossed-aldol and product-evidence drafts for limits on claims about real selectivity, conversion, yield, product identity and synthesis conditions.
- Review notation, accessible alternatives and proposed weekly workload.

## Author-side evidence and its limits

The repository content validator passed for 25 courses, 421 lessons, 2,618 questions, 1,449 cards and 25 cases with zero errors or explicit depth warnings. Representative alkene and alkyne formula and stoichiometry calculations were checked directly. The public package digest matches the snapshot. No test suite was run for version 0.4.8. These checks do not establish independent chemical review, accessible learner usability, semester workload, student learning or university equivalency. Graded homework, exams and a complete laboratory sequence remain absent; the project is inactive and ungraded.

## Review record to complete only after review

After a review actually occurs, record reviewer qualifications, date, exact package version and archive digest, artifacts examined, concrete findings and disposition. Keep separate decisions for chemical and mathematical correctness, instructional design, assessment, accessibility, workload and release. A package hash is an identity check, not approval.

## Open project route (2026-10-22)

The current guide, separate worked example, rehearsal and five private milestone self-checks make the existing project usable as ungraded practice. [The route regression tests](../tests/content/test_remaining_course_project_routes.py) independently recalculate every new numeric field and exercise the backend grader, including exact counts and continuous-quantity precision. Review the written explanation, evidence limits and proposed workload independently; automated arithmetic is not subject review. Historical snapshot evidence remains preserved.

## Deeper mechanism and synthesis target (2026-10-22)

Version 0.6.0 added original aryne/blocked-ring atom maps and multistep forward-compatibility/protection instruction, plus two paper assignments. Review electron/charge flow, original-carbon mapping, formation-rule restrictions, compatibility stipulations, formula/stereochemical reasoning and yield denominators. No real route selectivity, preparation or procedure is established. Written work, workload and qualified review remain open; the current snapshot pins the package.

## Second-comparator target (2026-10-27)

Current target 0.7.0 adds the [scope crosswalk](../content/courses/organic-chemistry/scope-crosswalk.md) against MIT OCW 5.12 Spring 2005 and UCI OpenCourseWare Chem 51A Fall 2009, and a week-2 reaction-energetics reading for a topic both courses teach (three objectives, 13 items, four cards). Check whether the crosswalk's covered, shallow, absent and local-extension labels are fair, given that it compares titles rather than lecture content. In the reading, check the free-energy and population relations, the entropy crossover and its link to elimination, the bond-energy ledger and its gas-phase limits, the transition-state-theory half-lives, the SN1 energy profile and rate law, the Hammond estimate and its stated 70% assumption, kinetic versus thermodynamic product ratios, and the catalyst statement. [The recalculation file](../tests/content/test_organic_chemistry_recalculations.py) recomputes the nine new numeric keys by root-finding, a bond ledger, RK4 integration of parallel channels and normalized state populations, and [the lesson test](../tests/content/test_organic_chemistry_reaction_energetics_lesson.py) checks every number the reading states and that each key rejects a named misconception. These checks were written and run by an AI coding agent; they are not independent review. The current snapshot pins this target, and the 0.6.0 snapshot is preserved.
