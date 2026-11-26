# Materials and chemical engineering review handoff

## Current four-course scope

This consolidated record covers four original, AI-assisted, partial and unreviewed version 0.1.0 packages. It does not replace their version-bound review records:

- [Materials Science](reviews/materials-science-review-handoff.md): eight foundational routes spanning bonding/structure, cubic crystallography and Bragg reasoning, defects/diffusion/strengthening, phases/transformations, failure/degradation, polymers/ceramics/composites, a synthetic characterization lab and a selection project.
- [Chemical Engineering Foundations](reviews/chemical-engineering-foundations-review-handoff.md): eight university-survey routes spanning variables/balances, reactive/recycle reconciliation, energy/VLE, transport concepts, ideal reactors/RTD and separations, plus synthetic reconciliation and flowsheet-model audits.
- [Materials Engineering for Fabrication](reviews/materials-engineering-fabrication-review-handoff.md): eight advanced design-review routes spanning service constraints, process–structure–property evidence, fabrication/joining comparisons, datums/GD&T/tolerance stacks, metrology/SPC/capability and release-evidence governance.
- [Chemical Process Design & Scale-Up](reviews/chemical-process-design-scale-up-review-handoff.md): eight advanced university/industry routes spanning design basis/economics, equipment/containment, dynamic operability/quality, inherently safer design, similarity/transfer and G0–G7 governance.

Each package has 48 public formative questions, 24 retrieval cards, six zero-point self-assessed cases and two public synthetic CSVs: 192 questions, 96 cards, 24 cases and eight CSVs across this batch. The complete current inventory is **33 partial courses, 727 lessons, 4,295 questions, 2,456 cards and 201 cases**, with **36 catalog-only nodes and 10 pathways**. No package is complete, measured for workload, independently reviewed or equivalent to a university course.

## Source corrections and reuse boundaries

The individual handoffs and [source registry](../content/sources/registry.json) retain the actual inspected URLs and provenance. In particular:

- Materials Science uses official MIT 3.091SC Fall 2010 and 3.012 Fall 2005 pages as link-only comparators. Its package checks corrected polymer Mn/PDI and displayed Bragg/diffusion approximations before the recorded content pass.
- Chemical Engineering Foundations records that the requested MIT 10.40 Spring 2012 and 10.32 Fall 2005 URLs returned 404. The verified comparators are **10.40 Fall 2003** and **10.32 Spring 2005**.
- Materials Engineering for Fabrication records that the shorter MIT 2.830J URL returned 404; the verified official comparator is **2.830J Control of Manufacturing Processes (SMA 6303), Spring 2008**. MIT 2.008 Spring 2025, MIT 3.032 Fall 2007 and NIST/SEMATECH remain link-only references.
- Chemical Process Design & Scale-Up records that requested MIT 10.490 Fall 2005 returned 404; the verified comparator is **10.490 Fall 2006**, alongside 10.491 Spring 2006. OSHA, NIST/SEMATECH, FDA and the proprietary ASME public catalog record are link-only; no standard text or acceptance criterion was imported.

Owner application repositories are also link-only personal hobby/learning projects. The recorded cross-project relationships cover `open-construction-equipment`, `machine-cad-agent`, `diaper-changing-machines`, `open-perfusion-rig`, `perfusion-calibration-lab`, `habitat-resource-sandbox` and `rural-florida-agriculture`. No code, CAD, validation artifact or owner review is imported or implied. All instructional prose, problems, fictional names and CSV rows are original synthetic material; source comparison does not establish affiliation or endorsement.

## Eleven shared study tools

The generic React registry now contains **11 deterministic local calculators**. The seven previous tools, including all habitat-ledger behavior, remain. Four additions are:

1. **Cubic crystal diffraction** → Materials Science. It computes `d = a/√(h²+k²+l²)` and first-order `θ`/`2θ`, requires nonnegative integer Miller indices with a nonzero family, and rejects missing/nonfinite/negative/overflow inputs and `λ > 2d`. The `λ = 2d` boundary returns 90°/180°. It is explicitly a cubic toy model, not phase identification, refinement, instrument operation or settings.
2. **Reactive stream balance** → Chemical Engineering Foundations. For only steady synthetic `1 mol A → 1 mol B`, it returns A in/out, B formed/product/unrecovered and the A closure residual. Feed and all fractions are validated; empty input never becomes zero, and no recycle, bypass, accumulation, plant recipe or target is invented.
3. **Tolerance stack** → Materials Engineering for Fabrication. It returns nominal total and worst-case `Σt`; conditional `RSS = √(Σt²)` is omitted until the learner explicitly declares independent variation. Result text retains that condition and makes no GD&T compliance, inspection acceptance, conformity or release claim.
4. **Process capability indices** → Materials Engineering for Fabrication and Chemical Process Design & Scale-Up. It validates finite inputs, `s > 0` and `LSL < USL` in every state. Unknown and unstable declarations omit Cp/Cpk with an explanation; only an explicit stable declaration shows `Cp = (USL−LSL)/(6s)` and `Cpk = min(USL−mean, mean−LSL)/(3s)`. Arithmetic never returns capable/accepted/release-approved status.

All tools use labeled native inputs/selects, keyboard-submit/reset behavior, live results and related-course links. Conditional controls reset to their non-declaring defaults, stale results clear on change, and calculations perform no API request or grading operation.

## Actual verification in this frontend/browser batch

| Check | Actual result |
| --- | --- |
| `npx vitest run src/studyTools.test.ts src/components/StudyTools.test.tsx` | **54 passed** across two files; defaults, independent recomputation, scaling, reset, zero values, invalid/nonfinite/cross-field inputs, overflow, conditional/stable states, course links and keyboard operation. |
| `npm test` from `frontend/` | **136 passed across 22 files**; one existing Three CJS deprecation warning. |
| `npm run lint`, `npm run typecheck`, `npm run build` | All passed. Vite transformed **902 modules** and retained its existing large-chunk advisory. |
| Four package suites | **40 passed**: Materials Science 10, Chemical Engineering Foundations 11, Materials Engineering for Fabrication 9 and Chemical Process Design & Scale-Up 10. |
| Preserved agriculture/cell-culture, course-plan, assessment-candidate and robotics global tests | **259 passed**. |
| Six affected inventory/outcome/syllabus/pathway/cycle selections | **6 passed, 95 deselected**. |
| `tools/validate_content.py --root . --json` | PASS, zero errors/warnings; **33 courses, 727 lessons, 4,295 questions, 2,456 cards, 201 cases**. |
| Canonical objective-coverage and assessment-candidate `--check` commands | Both passed with no regeneration needed for this frontend-only change. |
| `tools/check_security.py --bundle frontend/dist` and security-scan tests | PASS: **2,238 source files, zero findings; 2 tests passed**. |
| `git diff --check` | PASS after all edits; no existing dirty/untracked or staged state was reset or committed. |
| `npm audit --audit-level=high` | Reported the existing locked-tree **17 advisories (4 low, 11 moderate, 2 high)** in Vitest, KaTeX, minimatch, Vite and Zod paths. No dependency or lockfile change was made. |
| `PLAYWRIGHT_BROWSERS_PATH=/workspace/uniStemCourseSimulators/frontend/node_modules/.cache/ms-playwright E2E_BASE_URL=http://127.0.0.1:5173 npx playwright test e2e/materials-chemical-engineering.spec.ts` | **2 passed in 49.8 s**. Covered search/pathway discovery for all four courses, all **32 lesson routes**, 192 rendered items, 96 cards and 24 cases, all eight byte-identical `synthetic-original` CSVs, disabled unauthenticated controls, zero non-GET API requests, all four tools' defaults/valid/invalid/boundary/reset behavior, links, keyboard operation and **seven representative axe WCAG 2.1 A/AA scans with zero violations**. |

Docker was unavailable in this environment. The browser run used the documented explicit SQLite development fallback, Alembic through 0012, and Uvicorn/Vite bound only to `127.0.0.1:8000`/`127.0.0.1:5173`; both servers were stopped afterward. Cached Chromium was used without dependency, browser or lockfile installation. No authentication, guest session, commit or push was created. The disposable database and reports stayed under ignored frontend cache/test-output paths. Existing dirty/untracked work, `implementation_plan.md`, `.local/` and staged lockfile state were preserved.

## Canonical package identities

The packages were not rewritten by this frontend batch. The canonical `tools/course_package_digest.py` command produced these current identities; no hash was hand-authored:

| Package | Files | Archive bytes | Archive SHA-256 | Manifest SHA-256 |
| --- | ---: | ---: | --- | --- |
| Materials Science 0.1.0 | 17 | 198,133 | `f1df8917652888d97a99b7a9f69874e99867221e94d680e76a6133e2a13da1f5` | `4b220ea7ca61ae7b66e42a74666170715770978315ac6cdb5895cbf681891343` |
| Chemical Engineering Foundations 0.1.0 | 17 | 204,153 | `d25554359e44e79ddf5ddd9b5213754ab0faeaed20d57f65d0082d7079edbdb8` | `4aabcedfc7abc537d64ffad4c79db97809ee0614bc440421e49f5d45aed65757` |
| Materials Engineering for Fabrication 0.1.0 | 17 | 241,595 | `ac49d269151c9823ee452d6a4d27068923b565396e4f7974c02a2febb12fb7f1` | `6ce1b1b8d8b4fc9c6436b4cf73d06e51c90958b8185ac3d79198ae131e34f7df` |
| Chemical Process Design & Scale-Up 0.1.0 | 17 | 260,105 | `ca0d476a968e5b9a30c6a0be6ce11a9c5ae6583267cd9014ba2d785fc16665ee` | `04a87213a7da06c9be9036504e65f99453d667b03406248d8483b85c95727972` |

## Unresolved human review and release limits

Automated arithmetic, package tests, browser checks and axe scans are not qualified scientific, engineering, statistical, metrology, standards, process-safety, quality, regulatory or accessibility review. They do not establish measured workload, physical validation, independent replication, process capability or course completeness.

Materials identification, corrosion/fatigue/fracture and selection decisions remain unresolved. Fabrication readiness still requires approved drawings/BOM, qualified engineering/safety review, material/process qualification, calibrated inspection/MSA, traceability, nonconformance closure and named authorized human release. No feeds/speeds, toolpaths, weld/cure settings, machine setup or supplier/production approval is supplied.

Chemical-process readiness still requires qualified process, mechanical/materials, control, safety, inspection, operations, quality and regulatory review with current authoritative standards and physical evidence. Closure, Cp/Cpk, NPV, LOPA/RPN or gate arithmetic does not establish safe/feasible operation, equipment rating, SIL/IPL approval, process validation, regulated disposition or commercial release. Missing evidence remains unknown and fail-closed, never zero or pass. Manual accessibility/usability and assistive-technology review also remain open despite zero automated axe violations.

## Final comprehensive validation (2026-11-26)

The first complete root run found three genuine expansion regressions: two learner-visible numeric-formatting tests and the package LF-line-ending test. Its exact result was **3 failed, 4,846 passed, 1 skipped in 1,886.82 seconds**. The fixes only rounded learner-visible decimal/exponent displays, normalized six new CSV files from CRLF to LF, and updated the existing Chemical Engineering display-fragment expectations to the rounded strings. Numeric `solution_spec` keys, scientific/engineering answers, course versions, maturity and review status were not changed. Current package identities were recalculated after the corrections.

| Actual command/check | Final result |
| --- | --- |
| `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m pytest tests/content/test_learner_visible_number_formatting.py tests/content/test_package_line_endings.py tests/content/test_materials_science_package.py tests/content/test_chemical_engineering_foundations_package.py tests/content/test_materials_engineering_fabrication_package.py tests/content/test_chemical_process_design_scale_up_package.py -q -p no:cacheprovider` | **46 passed in 21.68 seconds**. The existing formatting and line-ending tests are the focused regressions; all four independent package suites also passed. |
| `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m pytest tests -q -p no:cacheprovider` from repository root, rerun in full after the fixes | **4,849 passed, 1 skipped in 1,884.80 seconds (31:24)**; zero failures. The remaining skip is `tests/content/test_biochemistry_homework_candidates.py:304`: protected answer fixtures are incomplete in this checkout. A separate identification run gave 12 passed, 1 skipped in 6.26 seconds. |
| `PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -B -m pytest -q -p no:cacheprovider` from `backend/`, rerun in full on the corrected tree | **9,225 passed, 7 skipped, 1 warning in 177.65 seconds (2:57)**; zero failures. Two skips are symbolic response/wrong-response builders (`tests/test_authored_items.py:110,119`); five are intentional over-confluent seed skips because that branch is tested separately (`tests/test_bench.py:1379`). The warning is the existing FastAPI/Starlette test-client `StarletteDeprecationWarning` about httpx. |
| `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B tools/validate_content.py --root . --json` | PASS: **33 courses, 727 lessons, 4,295 questions, 2,456 cards, 201 cases; zero errors and zero warnings**. This full validator also calls `validate_curriculum_map`; no standalone `tools/validate_curriculum_map.py` exists in this checkout. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` and `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Both PASS on the corrected tree; no report regeneration was needed. The gap report retains the pre-existing single Statistics no-practice-item note for `statistics-27-objective-4`. |
| `PYTHONDONTWRITEBYTECODE=1 .venv/bin/ruff check --no-cache backend tools tests` | PASS. |
| `npm run test:legacy` from repository root | **7 passed**, zero failures/skips. The root package exposes `test:legacy`, not a root `test` script. |
| `git diff --check` and `git diff --cached --check` | Both PASS. |
| Scoped credential-free external source-link check | Not run: `validate_content.py` exposes repository-wide `--check-links` but no course/source-scoped link option. The prior per-source retrieval and 404/edition corrections recorded above remain the link evidence; no full external-link check is claimed and no authenticated source was accessed. |

Final canonical identities, each recomputed with `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B tools/course_package_digest.py --course-id COURSE_ID`:

| Course ID | Version | Files | Archive bytes | Archive SHA-256 | Manifest SHA-256 |
| --- | --- | ---: | ---: | --- | --- |
| `materials-science` | 0.1.0 | 17 | 198,133 | `f1df8917652888d97a99b7a9f69874e99867221e94d680e76a6133e2a13da1f5` | `4b220ea7ca61ae7b66e42a74666170715770978315ac6cdb5895cbf681891343` |
| `chemical-engineering-foundations` | 0.1.0 | 17 | 204,153 | `d25554359e44e79ddf5ddd9b5213754ab0faeaed20d57f65d0082d7079edbdb8` | `4aabcedfc7abc537d64ffad4c79db97809ee0614bc440421e49f5d45aed65757` |
| `materials-engineering-fabrication` | 0.1.0 | 17 | 241,595 | `ac49d269151c9823ee452d6a4d27068923b565396e4f7974c02a2febb12fb7f1` | `6ce1b1b8d8b4fc9c6436b4cf73d06e51c90958b8185ac3d79198ae131e34f7df` |
| `chemical-process-design-scale-up` | 0.1.0 | 17 | 260,105 | `ca0d476a968e5b9a30c6a0be6ce11a9c5ae6583267cd9014ba2d785fc16665ee` | `04a87213a7da06c9be9036504e65f99453d667b03406248d8483b85c95727972` |

No dependency was installed or updated, no audit fix was run, and no commit, push or sibling-repository edit occurred. The pre-existing `implementation_plan.md` modification, untracked `.local/`, lockfile and all other dirty/untracked state were preserved. These final software/content checks do not close the qualified scientific, engineering, accessibility, workload or release reviews listed above.
