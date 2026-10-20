## Searchable cross-course notebook (2026-10-11)

Added an authenticated `GET /api/v1/notes` search over existing learner-owned notes. It returns only non-empty notes in current-version enrollments, supports literal case-insensitive text and course filters with bounded pagination, includes safe course/lesson labels, and never renders note bodies as HTML. The React **My notes** page includes accessible search/filter controls, empty/error states, paginated lesson links and a notice for stale enrollment versions. No table, migration, or duplicate note store was added.

Content validation passed: 25 courses, 424 lessons, 2,644 questions, 1,461 cards and 25 cases; zero errors or explicit depth warnings. Backend Ruff, frontend TypeScript, ESLint/Prettier and production build passed. No tests were run. These static checks do not substitute for a browser session/privacy integration test.

## Signals & Feedback Control scope crosswalk (2026-10-11)

Signals & Feedback Control 0.4.7 documents its selected combined scope against MIT OCW 6.003 Fall 2011 and 2.004 Dynamics and Control II Spring 2008. The crosswalk states the continuous-to-sampled control bridge and limits in Fourier coverage, physical component modeling, formal controller design and laboratory instruction. No lesson, assessment or learning count changed. Content validation passed (25 courses, 424 lessons, 2,644 questions, 1,461 cards, 25 cases; zero errors or explicit depth warnings); assessment-candidate and objective-coverage checks passed. The digest matches 24 files and 338,720 bytes. No tests were run; the course remains partial, unreviewed and formative-only.

## General Chemistry I/II MIT 5.111SC scope crosswalk (2026-10-11)

Added a maintainer-facing topic crosswalk for all five MIT 5.111SC Fall 2014 units and both local packages. It makes the deliberate prerequisite-to-extension handoffs visible and distinguishes local omissions from repeated teaching. No course package, version, question, lesson or card changed. Repository counts remain 25 packages, 424 lessons, 2,644 questions, 1,461 cards and 25 cases. This is link-only comparison; no source material was copied. No tests were run.

## Cell Biology scope clarification and E&M interference unit (2026-10-11)

Cell Biology 0.61.1 passes content validation at 25 courses, 423 lessons, 2,636 questions, 1,457 cards and 25 cases. Its public numeric-key recalculation passed 21/21 items; public table reconciliation passed 114/114 cells; the review-evidence index, objective-coverage report and assessment-candidate report passed their drift checks. The digest-bound snapshot matches 122 files and 2,113,739 bytes.

Physics E&M 0.4.7 adds an original two-source interference lesson, eight formative items and four cards inside Week 11. The final repository content validation passed at 25 courses, 424 lessons, 2,644 questions, 1,461 cards and 25 cases, with zero errors or explicit depth warnings. Objective-coverage and assessment-candidate reports pass their drift checks; package snapshot identity is current. Direct arithmetic was checked independently. `git diff --check` passed with only existing line-ending notices. No tests were run. Both courses remain partial, unreviewed and formative-only.

## Programming & Numerical Methods interpolation unit (2026-10-11)

Programming 0.4.8 adds one original week-10 lesson comparing quadratic interpolation with regression. The synthetic table yields p₂(x)=1−0.6x+0.1x², p₂(0.5)=0.725 against f(0.5)=0.8, signed error −0.075, and an extrapolated p₂(4)=0.2 against f(4)=1/17. Nine formative items and four cards cover node fit, between-node error, extrapolation, method choice and assumptions. MIT OCW 2.086 Fall 2014 places interpolation in its opening numerical-calculus unit and later includes least-squares fitting; this lesson is selective, and no MIT content was copied.

Content validation passed: 25 courses, 423 lessons, 2,636 questions, 1,457 cards and 25 cases; zero errors or explicit depth warnings. Objective-coverage and assessment-candidate reports pass their drift checks. Package digest: 26 files, 329,778 bytes; archive SHA-256 `41c6ea2786d2d22669456c6f070569a8b054961861eb336dcf25d2a7ef4b1ddc`; manifest SHA-256 `531ffdba665b585375deb76d833166460f9ff96a47de2a5b2980292a3f6fd578`. No test suite was run. The course remains partial, unreviewed and formative-only.

## Thermodynamics & Transport chemical-potential unit (2026-10-11)

Thermodynamics & Transport 0.4.7 adds an original week-1 reading on chemical potential, reaction Gibbs energy, equilibrium constants and an ideal A⇌B composition. Nine formative items and four cards distinguish Q from K, equilibrium from reaction rate, and thermodynamic direction from kinetics. MIT OCW 20.110J Fall 2005 places equilibrium/free energy, chemical potential and chemical equilibrium in sessions 8–12; the local lesson is one bounded example, with phase equilibrium and nonideal solutions still outside scope.

Content validation passed: 25 courses, 422 lessons, 2,627 questions, 1,453 cards and 25 cases; zero errors or explicit depth warnings. The check suites were not run. Package digest: 24 files, 339,920 bytes; archive SHA-256 `0e4a3a49a7010445c0505240ac1061e0a4d26472b617f858b5ba6fd562ccc774`; manifest SHA-256 `33abc493119da72377a07a38a552f1db64a7b71ad2fef9bc3aa5d7be58f76ab2`. The course remains partial, unreviewed and formative-only.

## Organic Chemistry alkene/alkyne reactions and Statistics continuous Bayesian updating (2026-10-11)

Organic Chemistry I 0.4.8 adds two original alkene/alkyne readings, 18 formative questions and eight cards within its 12-block schedule. MIT OCW 5.12 Spring 2005 assigns several weeks to these reactions; the local block is a selective two-reading subset, with SNAr and multistep synthesis still open. Statistics 0.4.7 adds one original Beta–Binomial conjugacy and prediction lesson inside week 13, with nine formative questions and four cards. MIT OCW 18.05 Spring 2022 includes Beta conjugacy; normal conjugacy and broader Bayesian/MLE coverage remain limited. Both source sets are link-only; no source instruction or assessment was imported.

Content validation passed: 25 courses, 421 lessons, 2,618 questions, 1,449 cards and 25 cases; zero errors or explicit depth warnings. Objective coverage and assessment-candidate report checks pass. Organic Chemistry digest: 26 files, 391,546 bytes; archive SHA-256 `82ea4e533d191f1e7dfeda42fe5c74ccb1e99f7055b7dcdd040e5e4e2036afd0`; manifest SHA-256 `7a7b092c5eb06751f678b60933cb7515e131cb0c6e8d59d3a312e09702968178`. Statistics digest: 26 files, 384,072 bytes; archive SHA-256 `5f4b17230ce989ca45b9043198810829b19fd10589ef6955e7636c9e02a69d81`; manifest SHA-256 `d12c0185b23f1b698dfef1ed5bb0767ac28b0658e2f4c23916d333806ffed1e4`. No test suites were run. Both courses remain partial, unreviewed and formative-only.

## Biochemistry 0.4.85 sequence consolidation (2026-10-11)

Consolidated overlapping explanations while retaining lesson/question IDs: the central-carbon primer is now an overview with full thermodynamics and mitochondrial accounting in their dedicated readings, and the network primer frames perturbation evidence before the quantitative control-coefficient lesson. The syllabus, manifest, source map and audit explicitly distinguish covered animal-cell metabolism from deferred photosynthesis/CO₂ assimilation, membrane transport and translation, using MIT OCW 7.05 Spring 2020 as a link-only breadth comparator.

`python -B tools/validate_content.py`: PASS, 25 courses / 418 lessons / 2,591 questions / 1,437 cards / 25 cases, zero errors or explicit depth warnings. Objective coverage and assessment-candidate report checks pass; all 11 inactive candidate prerequisite hashes match the updated readings. Package digest: 70 files, 1,125,089 bytes; archive SHA-256 `281ee947fac158f6d9ce6befa7b040a9983a36d640e09e95d2eef717a8547942`; manifest SHA-256 `d7a4eff4abdf375eee7ab178729c004fbb09b949cabd62bc11703b016e6a3906`. `git diff --check` is recorded after the final edit. No tests were run. The course remains partial, unreviewed and formative-only.

## Geroscience primary-study intervention comparison (2026-10-11)

Geroscience 0.5.8 extends the existing Week 11 paper-reading lesson with an original comparison of Baker et al. (2016) and Harrison et al. (2009). The matrix distinguishes inducible p16(Ink4a)-cell clearance from dietary rapamycin, their mouse models and survival/function outcomes, and why the studies cannot be ranked as a head-to-head trial. It checks the reported 14%/9% change in age at 90% mortality and distinguishes target engagement from mechanism. Eight formative items and four cards support the comparison without adding a week.

The primary sources were checked directly: [Baker et al.](https://pubmed.ncbi.nlm.nih.gov/26840489/) reports INK-ATTAC/AP20187 clearance from one year of age and median-lifespan effects in both sexes and two backgrounds; [Harrison et al.](https://pubmed.ncbi.nlm.nih.gov/19587680/) reports late-life rapamycin from 600 days at three sites and the 14%/9% age-at-90%-mortality figures. The official MIT OCW [2.787J syllabus](https://ocw.mit.edu/courses/2-787j-tissue-engineering-and-organ-regeneration-fall-2024/pages/syllabus/) and [calendar](https://ocw.mit.edu/courses/2-787j-tissue-engineering-and-organ-regeneration-fall-2024/pages/calendar/) describe a graduate tissue-engineering/regeneration course with aging-associated impediments; it is a selective regeneration comparator, not a full geroscience course match. No MIT or paper assets/data were imported.

Repository content validation passed with 25 courses, 418 lessons, 2,591 questions, 1,437 cards and 25 cases; zero errors or explicit depth warnings. Objective coverage and candidate reports were regenerated and their drift checks passed. The 0.5.8 public package has 26 files, 363,850 bytes, archive SHA-256 `04cfc8f0135c8ed766383307ce59c638aa68cad46b7c702777bfbc6ebb335a35`, and manifest SHA-256 `3548aaf8753eb448f3e6764ba06c0deda317c062fcdf5a7a529b2d36b25776fe`. No test suite was run. The course remains partial, unreviewed and formative-only.

## Cellular Biomechanics specimen-size relaxation unit (2026-10-11)

Cellular Biomechanics 0.3.7 adds an original Week 3 comparison of a size-independent standard-linear-solid time with the approximate poroelastic scaling \(\tau\approx L^2/D_{\mathrm{eff}}\). Invented relaxation means at drainage lengths 0.5, 1 and 2 mm are 5, 20 and 80 s, giving exponent 2 and effective diffusivity 0.050 mm^2/s = 5.0×10^-8 m^2/s; the model predicts 45 s at 1.5 mm. Eight formative items and four cards cover unit conversion, model comparison, boundary conditions, independent specimens and inference limits. The new material is grouped in the existing Week 3, preserving the 14-week proposal.

MIT OCW [20.310J Spring 2015 syllabus](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/syllabus/) describes undergraduate tissue viscoelastic and poroelastic behavior and cell mechanics. Its [calendar](https://ocw.mit.edu/courses/20-310j-molecular-cellular-and-tissue-biomechanics-spring-2015/pages/calendar/) separates tissue viscoelasticity (lectures 10–12), poroelasticity (13–14) and a later cell-scale comparison (16–18). This local diagnostic is narrower and original; all values are synthetic, and no MIT asset was imported.

Repository content validation passed with 25 courses, 418 lessons, 2,583 questions, 1,433 cards and 25 cases; zero errors or explicit depth warnings. Objective coverage and candidate reports were regenerated and their drift checks passed. The 0.3.7 public package has 24 files, 337,328 bytes, archive SHA-256 `be8759406627b69deeed3568bf6098c2a1387d0d6be2c7029a6b26511e289ef3`, and manifest SHA-256 `84d34dd7831351fd48453bc1dfb682d565e086c0d18d7f6f0b92ff4f29aebed2`. No test suite was run. The course remains partial, unreviewed and formative-only.

## Linear Algebra four-fundamental-subspaces unit (2026-10-11)

Linear Algebra 0.3.6 expands the existing rank/null-space reading with an original 3 × 4 matrix. The lesson computes bases and dimensions for C(B), N(B), C(Bᵀ) and N(Bᵀ), checks both rank-nullity identities and both orthogonal pairs, uses the left null space to test consistency, and locates the least-squares residual in that space. Six formative items and four cards are mapped to a new objective without adding a week. MIT OCW [18.06SC Fall 2011](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/syllabus/) includes a dedicated [Four Fundamental Subspaces session](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/ax-b-and-the-four-subspaces/the-four-fundamental-subspaces/) and a [computational recitation](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/resources/computing-the-four-fundamental-subspaces/); the local example is original.

Repository content validation passed with 25 courses, 407 lessons, 2,462 questions, 1,372 cards and 25 cases; zero errors or warnings. Objective coverage reports 1,064 objectives and 106 course outcomes with no unmapped or unpractised objectives; candidate audit and both report checks passed. The 0.3.6 public package has 23 files and 295,146 bytes (archive SHA-256 `25366abd6f4a4e049d2d178d2483bc31853962da49a97ea2cef45f723510c232`; manifest SHA-256 `c83ca4e4aec1275052ab04a321c03de4c93580b03ecde800f072c205d1a2ea2d`). No test suite was run for this increment. The course remains partial, unreviewed and formative-only.

## Genetics & Genomics microbial-genetics and regulatory-circuits unit (2026-10-11)

Genetics 0.5.6 adds original Hfr-entry, cotransduction and plasmid-complementation instruction; a short unordered-tetrad recombination section; and a prokaryotic regulatory-circuit lesson covering negative inducible control, positive CAP–cAMP activation, negative repressible control and bounded reporter design. The 14-week proposal places microbial topics before expression analysis and marks Mendelian randomization and locus follow-up as an optional human-genetics extension. MIT OCW [7.03 Genetics, Fall 2004 calendar](https://ocw.mit.edu/courses/7-03-genetics-fall-2004/pages/calendar/) lists tetrad analysis, phage genetics, bacterial transduction/plasmid complementation, and separate negative/positive prokaryotic regulation topics. The added work is original and synthetic; substantial eukaryotic-genome and microbial topics remain outside scope.

Repository content validation passed with 25 courses, 407 lessons, 2,456 questions, 1,368 cards and 25 cases; zero errors or warnings. Objective coverage reports 1,063 objectives and 106 course outcomes with no unmapped or unpractised objectives; the candidate audit and both report checks passed. The 0.5.6 public package has 27 files and 372,988 bytes (archive SHA-256 `d2c6ee59eeb8f507ce316dc9c0ce29f7f0e601204b9b7f506509c8841156d80a`; manifest SHA-256 `bc567e193d41ae109ace2ee0cff28ef71f25c7bb3add64256b75dadd6d210b98`). No test suite was run for this increment. The course remains partial, unreviewed and formative-only.

## Physics II: E&M displacement-current and wave-energy unit (2026-10-11)

Added original instruction on capacitor current continuity, Ampère–Maxwell closure, the magnetic field from displacement current, and plane-wave energy transport. Package 0.4.6 adds 3 objectives, 8 practice items (6 numeric and 2 multiple-select) and 4 retrieval cards. Its public archive has 24 files and 324,683 bytes (archive SHA-256 `b62e009e060c73c74b5dd690b25be5ce87cf3dd00ec0083cd3432a2f05e94a9b`; manifest SHA-256 `cfef47e916872988f39972c14da59c8b81d9977b0b25e48a67327f33f552ebdd`). The proposed 14-week schedule groups the two opening electrostatics readings and puts the new lesson after induction. MIT OCW [8.02 class topics](https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/pages/class-topics/) lists Maxwell equations, radiation and energy flow in week 12; the package remains narrower, with radiation generation and interference still outside its scope.

Independent arithmetic checks give 0.50 mA displacement current, 1.25 nT and 2.00 nT for the inside/outside capacitor examples, and a 120 V/m peak plane wave with 0.400 μT magnetic amplitude, 38.2 W/m² peak flux and 19.1 W/m² average flux. Repository content validation passed with 25 courses, 405 lessons, 2,442 questions, 1,358 cards and 25 cases; zero errors and warnings. The package remains partial, unreviewed and formative-only. No test suite was run for this increment.

## Repository-wide validation follow-up (2026-10-11)

The first content-validation pass after the course rotation found malformed schedule ID fields in Differential Equations and an Organic Chemistry worked-example field below the repository's 35-word minimum. Differential Equations 0.3.9 now stores all grouped schedule IDs as arrays. Organic Chemistry 0.4.7 expands the example to show the methoxy directing conclusion and the geometry check for cyclooctatetraene. Both package snapshots and candidate inventory were refreshed. The corrected repository validation passed with 25 courses, 404 lessons, 2,434 questions, 1,354 cards and 25 cases, with zero errors or warnings. No test suite was run for these corrections or the course rotation; content validation is not independent course review.

## Statics & Materials beam diagrams unit (2026-10-11)

Added a bounded lesson on beam reactions, distributed-load slopes, point-load shear jumps, piecewise shear/moment functions, simple-support checks and a nominal bending-stress calculation. The 0.4.6 public archive is 24 files and 328,648 bytes (archive SHA-256 `3c7b5543cb0a79c8769adf4697ae72086383ad772c1fb6c7c4de29cb12f2db50`; manifest SHA-256 `a4e8827801d6fab2c015dacb289e32e93c14b88cce3fd5a2e4a531d4b3bae55f`). The objective-coverage report now lists 15 lessons, 41 objectives, 98 formative questions and 53 cards for this package; repository totals are 404 lessons, 1,053 objectives, 2,434 questions and 1,354 cards. The assessment-candidate inventory and Statics review snapshot were regenerated.

The new example values were independently recalculated from equilibrium and the stated beam relations: reactions 6 kN each; (V(x)=6-2x) kN; (M(x)=6x-x^2) kN·m; (M_{max}=9) kN·m; and rectangular-section nominal stress 13.5 MPa. The off-center 4 kN check gives reactions (8/3) and (4/3) kN, a (-4) kN shear jump, and continuous moment (16/3) kN·m at the load. MIT OCW [2.001 syllabus](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/syllabus/) and [lecture notes](https://ocw.mit.edu/courses/2-001-mechanics-materials-i-fall-2006/pages/lecture-notes/) were used as scope comparators; no MIT material was copied. No test suite was run for this increment. The package remains partial, unreviewed and formative-only; schedule time is unmeasured and compatibility/truss coverage remains limited.

## Organic Chemistry aromaticity/EAS unit (2026-10-11)

Added an original aromaticity/EAS lesson with 4 electron-count and 5 conceptual checks, plus 4 retrieval cards. Regrouped four primer/expanded pairs into an 11-block proposed content sequence; this reduces repeated calendar space without asserting measured weekly workload. MIT OCW [5.12 Organic Chemistry I, Spring 2005](https://ocw.mit.edu/courses/5-12-organic-chemistry-i-spring-2005/pages/calendar/) places aromaticity/EAS in its undergraduate sequence and also includes alkynes, broader alkene reactions, and nucleophilic aromatic substitution. A follow-up worked-example expansion cleared the repository's 35-word example threshold, advancing the course to version 0.4.7. The package remains partial, unreviewed and formative-only.

Public digest: version 0.4.6, archive SHA-256 `74cac903f6e385cfb6e0ed81eddd5c98095a177171691449b17e9423a9b0da8c`, manifest SHA-256 `aac4b222ad98354bc324027695770ba2d684b15aef3b8f019808b782d0464b08`, 24 package files, 340,646 bytes. Objective coverage and public assessment-candidate reports were refreshed. No test suite was run for this lesson increment.

## Differential Equations Laplace IVP unit (2026-10-11)

Added an original initial-value lesson, six public formative items and four retrieval cards. A follow-up schedule schema correction converted grouped lesson and assessment fields to arrays, advancing the course to 0.3.9 without adding scope. The package remains partial, unreviewed and formative-only. No test suite was run for either Differential Equations increment.

MIT OCW [18.03SC, Fall 2011 Unit III](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/pages/unit-iii-fourier-series-and-laplace-transform/) confirms the wider transform-unit scope: Fourier series, impulse/step inputs, impulse response, convolution, Laplace IVPs, transfer functions and poles. This lesson covers initial-value terms, partial fractions and delayed steps; it does not claim the remaining unit. The proposed 14-week schedule combines two related logistic readings into one block to make room without a nominal extra week. The schedule remains unmeasured and is not evidence of semester equivalence.

## Shared case studio (2026-10-11)

Existing case prompts and ungraded checklists are now available in the React reader across all 25 partial packages. Server-owned private drafts retain course version, visible case digest and snapshot, response, learner checklist marks, and a revision counter. Earlier responses remain readable and exported; archived studios cannot save. No graded project candidate or course completion gate was activated.

| Check | Result |
| --- | --- |
| Full container backend suite | **5,146 passed, 2 skipped**; skips are existing symbolic right/wrong response builders. Case regressions cover ownership, enrollment/CSRF, source changes, revision conflicts, unchanged gradebooks, registration, export and deletion, and all 25 authored case packages. |
| Alembic 0012 lifecycle | Upgrade, metadata comparison and downgrade passed in the backend suite. Runtime preview migrated a fresh disposable SQLite database through head. |
| Container frontend suite | **71 passed**; includes case save/load/conflict/history/archive/error flows and current/archived schedule links. |
| Production build, ESLint/Prettier and Ruff | Passed. |
| Browser coverage | **5 passed**: public Cell Biology, Circuits and Biochemistry studios; keyboard self-check/save; reload persistence; two-tab stale-write protection; export; archived case routing; complete caveat disclosure; 390-pixel layout; all six scientific calculators. WCAG 2.1 A/AA axe scans passed and desktop/mobile screenshots were visually inspected. |
| Scope | Shared platform feature only; authored course bytes, versions, review status and release gates unchanged. Qualified accessibility and scientific review remain open. |

## Shared scientific study tools (2026-10-11)

The six legacy scientific calculator models now have React implementations with explicit units and model assumptions, validated inputs, keyboard submission, result clearing and example resets. Direct public-reader routes and course navigation make them available across subjects; they make no API writes or grading changes.

| Check | Result |
| --- | --- |
| Container frontend suite | **64 passed**, including formula/unit, numeric-range, public-route and keyboard regressions. |
| Production build and ESLint/Prettier | Passed. |
| Playwright calculator flows | **2 passed**: six calculators, expected results, invalid target, keyboard navigation, no API writes, and 390-pixel layout. |
| axe WCAG 2.1 A/AA scans | All six calculator screens passed after calculation; qualified manual accessibility review remains open. |
| Desktop and mobile visual inspection | Passed; results and controls fit their layouts. |

This feature does not change any course package version, grading policy, review status, or release gate.

## Cell Biology 0.57.0 package-pinned learner resource (2026-10-11)

Replaced the week-5 lab's mutable raw-GitHub CSV link with an allowlisted package resource. The API serves current package bytes publicly and saved package bytes to enrolled learners through the historical course-version route. Added schema/content checks plus repository and API regressions for rewritten links, allowlisting, enrollment and historical byte preservation. Refreshed digest-bound reports and the prospective workload packet; preserved the 0.56.0 snapshot and evidence. No learner data or release decisions were added.

| Actual command/check | Result |
| --- | --- |
| Public package digest | Version 0.57.0; 122 files; 2,114,450 bytes; archive SHA-256 `a731447f4eb6d6bf596199480007484d152522b6ff4915654a8fdd501e1ad79e`; manifest SHA-256 `2f7a159a454b13206daf9774d226f27a1099c80cae4daf852de2747c4ab4ccd0`. |
| Content validator with live links | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards, 25 cases; zero errors and 11 access-denied limitation warnings. |
| Focused resource/content regressions | **127 passed, 3 skipped** (Windows symlink support); the corrected version-history handoff test passed separately (**1 passed**), including current and archived resource API checks. |
| Digest-bound report checks | Candidate, review-evidence, objective-coverage, response-mode, numeric and table report checks pass; 21 numeric and 114 table calculations pass. |
| Ruff and `git diff --check` | Passed. |

## Cell Biology 0.56.0 week-14 dataset count correction (2026-10-11)

Corrected the week-14 virtual lab's ambiguous data count. The CSV contains 40 independent culture-level records (two conditions × five days × four cultures) and 160 constructed outcome measurements across four fields per record. The data and activity are unchanged. Added a regression test for row count and replicate structure, refreshed the lab candidate's source hash and advanced the package version. Digest-bound review artifacts now target 0.56.0; no review or release gate was closed.

| Actual command/check | Result |
| --- | --- |
| Focused Cell Biology and content-validation regression suite | **223 passed, 2 skipped**. |
| Virtual-lab dataset count and replicate regression | **3 passed**; the week-5, week-11, and week-14 CSVs contain 8, 120, and 40 culture-level rows respectively, with their documented replicate structures. |
| `uv run --project backend --with jsonschema python tools/validate_content.py --check-links` | **Passed**: 25 courses, 401 lessons, 2,411 questions, 1,341 cards, 25 cases; 0 errors and 12 explicit `link-access-denied` limitation warnings. |
| Candidate, review-evidence, objective-coverage, and response-format drift checks | Passed. The evidence index reports 142 unresolved candidate gates, four unresolved course-level gates, zero reviewer sign-offs, and no release authorization. |
| Public numeric and table recalculations | **21/21** numeric checks and **114/114** table checks passed; protected answer sources were not read. |
| Ruff on changed Cell Biology tests | Passed. |

## Cell Biology 0.55.0 workload-pilot packet (2026-10-11)

Refreshed the prospective workload protocol and blank log for package version 0.55.0. Its weekly inventory is checked against the course manifest, and the protocol carries the exact public package and manifest hashes. It remains a planning artifact only: no required learner activities, time targets, recruitment, or results are recorded.

| Actual command/check | Result |
| --- | --- |
| `uv run --project backend --with jsonschema pytest tests/content/test_cell_biology_review_handoff.py -q` | **1 passed**; verifies current package hashes, all 14 manifest weeks and activity IDs, and a header-only CSV log. |
| `uv run --project backend --with jsonschema python tools/validate_content.py --check-links` | **Passed**: 25 courses, 401 lessons, 2,411 questions, 1,341 cards, 25 cases; 0 errors and 13 explicit `link-access-denied` limitation warnings. |
| `uv run --project backend ruff check tests/content/test_cell_biology_review_handoff.py` | Passed. |

## Cell Biology studio accessibility and browser regression (2026-10-11)

Added a dedicated browser check for the week-14 written-design studio and expanded axe WCAG 2.1 A/AA scans across all 43 Cell Biology lesson routes. The checks use keyboard activation to open every route, and the studio test verifies its five-prompt self-check, no-submit practice status, focus movement through linked lesson references, and navigation from the syllabus to a linked lesson. The wider scan found horizontally scrollable CSV code blocks that were not keyboard-focusable; the shared Markdown renderer now gives code blocks a keyboard tab stop and has a component regression test. Package-local lesson links are rewritten to in-app routes, preserving archive version paths; backend tests confirm external URLs and non-lesson links remain unchanged. These are automated checks only; they do not establish manual screen-reader usability or qualified accessibility review.

The first full browser run exposed stale test expectations for weeks 9–14 and an outdated percentage unit in a week-5 lab test. Those checks now align with the current public assessment plan and its `pp` answer unit. The shared limiter also throttled later browser writes, so the API now reads optional `RATE_LIMIT` and `AUTH_RATE_LIMIT` environment overrides. Local and production defaults remain 120 and 30 writes per rolling minute; CI raises them only for its disposable Compose test stack.

| Actual command/check | Result |
| --- | --- |
| Focused week 5 and week 9–14 browser regressions | **9 passed**. |
| Cell Biology lesson-route accessibility sweep | **43 lesson routes** passed axe WCAG 2.1 A/AA checks with keyboard activation. |
| Full Playwright browser suite | **22 passed, 2 skipped**; the two skipped protected-assessment cases require the separate QA fixture. |
| Backend content repository | **24 passed, 1 skipped**; the skip is the unsupported Windows symlink test. Current and archived lesson/syllabus routes are covered. |
| Frontend lint, unit tests, and production build | Passed; **46 unit tests** across 13 files. |
| Backend configuration tests and Ruff | **8 configuration tests passed**; lint passed. |
| Compose development configuration | `docker compose config --quiet` passed. |

The course remains partial, unreviewed, and formative-only. The new route scan does not close the qualified accessibility, scientific, assessment, workload, institutional-equivalency, or release gates.

## Cell Biology 0.55.0 review-target refresh (2026-10-11)

Refreshed the in-package independent-review handoff, which had lagged at 0.53.0 and 42 lessons, and advanced the public package version to 0.55.0. The current inventory is 43 lesson records, 69 objectives, 166 public practice questions, 89 cards, and 28 assessment records. No learner-facing assessment or policy changed. Preserved the empty 0.54.0 review scaffold under a versioned filename and generated the current review-evidence index against the new package digest.

| Actual command/check | Result |
| --- | --- |
| Focused Cell Biology candidate, design-studio, integrity, evidence, response-mode, and handoff tests | **149 passed**. |
| Content-validation regression suite | **98 passed, 2 skipped**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards, 25 cases; 0 errors and 0 warnings. |
| Public numeric-key and table-reconciliation audits | **21/21** numeric checks and **114/114** table checks passed; protected candidate answer sources were not read. |
| Candidate report, review-evidence index, objective coverage, and response-mode reports | Current and validated. The review index remains at 142 candidate gates and four course-level gates; no reviews or operator approval are recorded. |
| Public package snapshot | Version 0.55.0; 122 files; 2,113,091 bytes; archive SHA-256 `a288f02bca6867bb7cf4f922bc974b37dbf48367d6efd503be0f82a0d8df168a`; manifest SHA-256 `cb97a90093f40d36e664cd09a9761024bf0ab11d71f4e3ad6b8de708c7a2efa0`. |

The package remains partial, unreviewed, and formative-only. This refresh improves review targeting but does not satisfy scientific, assessment, accessibility, workload, institutional-equivalency, or release gates.

## Biochemistry 0.4.84 kinetics-lab consistency (2026-10-11)

Aligned the kinetics-lab header with its package version and added a CSV regression for all displayed means, reciprocal fits and inhibition calculations. The container Biochemistry suite passed **103 tests with one incomplete protected-fixture skip**; content validation reported zero errors and zero explicit limitation/depth warnings, and Ruff passed. The public package remains partial, unreviewed and formative-only: 70 files, 1,119,349 bytes; package SHA-256 `b650c42d64a583e2828de5e588b646a0b9316b967332042a8d629b485fda28eb`, manifest SHA-256 `cba02bb31072d88e073e4bf444771e5071743a2cc62a4b8c7f94d4fb82089751`.

## Biochemistry 0.4.83 free-energy standard-state clarity (2026-10-11)

Made the biochemical reaction quotient explicitly dimensionless by defining activities relative to the 1 M standard concentration, then rewrote the ATP-hydrolysis example to show its normalized activities. Added an equation regression for the displayed ATP, phosphorylation-equilibrium, hexokinase-coupling, NADH-to-oxygen, and isomerization calculations. Updated all 11 inactive candidates to the new package version and refreshed the two candidate prerequisite hashes that cite the free-energy reading. Rebound the current snapshot, evidence register, workload protocol, review checklist, and response-format inventory; preserved the 0.4.82 artifacts. Course maturity and assessment policy are unchanged.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regression suite | **102 passed, 1 skipped**; the protected-answer fixture is incomplete, so its consistency test skipped before reading any key file. |
| Free-energy equation regression | Recomputes dimensionless ATP Q and displayed actual/standard ΔG, equilibrium constant, redox potential difference, and stopping ratio. |
| Content validator | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors and 0 explicit limitation/depth warnings. |
| Candidate, review-evidence, and objective-coverage drift checks | Passed. The evidence index retains 88 unresolved candidate-gate instances and four course-level gates, with zero reviewer sign-offs and no release authorization. |
| Public package digest | Version 0.4.83; 70 files; 1,119,100 bytes; archive SHA-256 `83d21f6b34bc076298c3aec2e9082552848dcbb30513cbd7b25cfc00222a7a33`; manifest SHA-256 `b0ec7af9367295ec69ea5f5d56c75328c2e371f22d37c2b6744219a792da580c`. |
| Ruff and `git diff --check` | Passed. |

## Biochemistry 0.4.82 binding-equilibria worked example (2026-10-11)

Expanded the week-4 binding-equilibria reading with a derivation of the ligand-depletion quadratic, a worked example that checks free and bound concentrations against mass balance, and an explicit statement of the model assumptions. Added a regression that independently recomputes the example and recovers the stated K_d. Updated all 11 inactive candidates to the new package version and refreshed the three candidate prerequisite hashes that include this lesson. Rebound the current snapshot, empty evidence register, workload protocol, review checklist, and response-format inventory; preserved the 0.4.81 artifacts. The course remains partial, unreviewed, and formative-only; no activity, assessment policy, or review decision changed.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regression suite | **101 passed, 1 skipped**; the protected-answer fixture is incomplete, so its consistency test skipped before reading any key file. |
| Binding-equilibria example regression | Recomputes 15 nM complex, 5 nM free receptor, 45 nM free ligand, and recovers K_d = 15 nM; the 16 nM approximation and 6.7% overestimate are checked against the lesson. |
| Content validator | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors and 0 explicit limitation/depth warnings. |
| Candidate, review-evidence, and objective-coverage drift checks | Passed. The evidence index retains 88 unresolved candidate-gate instances and four course-level gates, with zero reviewer sign-offs and no release authorization. |
| Public package digest | Version 0.4.82; 70 files; 1,118,417 bytes; archive SHA-256 `2b08ccf0c715d31142d118f364d422d16c05045282b31ead654a92310a94bbcb`; manifest SHA-256 `95512ab22432ec9cf2ac972d6f5623a59b252c377f91279095d767c7cd8a814e`. |
| Ruff and `git diff --check` | Passed. |

## Biochemistry 0.4.81 workload-estimate labeling (2026-10-11)

Marked the week-7 kinetics lab's 2–3 hour duration as an unvalidated author estimate. Refreshed its package version, all 11 inactive candidate course-version bindings, and the public prerequisite hashes on the homework-4, midterm, and final candidates that cite the lab. Rebound the review snapshot, evidence index, workload protocol, reviewer checklist, and response-mode inventory to the 0.4.81 package. The course remains partial, unreviewed, and formative-only; no learner time was measured, no target was approved, and no review or release gate was closed.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regression suite | 100 passed, 1 skipped; the protected-answer fixture is incomplete in this checkout, so its private-key consistency test skipped before reading any key file. |
| Content validator | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors and 0 explicit limitation/depth warnings. |
| Candidate, review-evidence, objective-coverage and response-mode drift checks | Passed. The evidence index retains 88 unresolved candidate-gate instances and four course-level gates, with zero reviewer sign-offs and no release authorization. |
| Public package digest | Version 0.4.81; 70 files; 1,117,012 bytes; archive SHA-256 `b2b723acb41cced40fcb4ec25528bc60a2e053fb835107ca6d79b74d9dc15134`; manifest SHA-256 `96f09bc371679b2e4dc30774ca62c3f2cc1debb7d21f6dc71989835967c3a9ec`. |
| Ruff and `git diff --check` | Passed. |

The duration remains unvalidated. External review, measured workload, and operator release decisions remain open.

## Biochemistry 0.4.79 physical-lab proposal (2026-10-11)

Added a non-scheduled instructor and safety review draft for supervised potato-catalase kinetics at `docs/reviews/biochemistry-physical-lab-candidate-0.4.79.md`, with a [blank instructor pilot log](reviews/biochemistry-physical-lab-pilot-log-0.4.79.md) for local approvals, raw observations, measured workload, and evidence-based decisions. The draft notes that captured oxygen alone cannot verify peroxide depletion. Local piloting, exact-product SDS review, institutional EHS approval, accessibility planning, and waste/emergency procedures remain prerequisites to student use. These files are outside the public package and do not satisfy the physical-lab gate. A historical 0.4.53 workload-protocol reference in the progress review was marked unavailable rather than redirected to a different package version. No course package files or version-bound hashes changed.

Added a version-pinned external-review checklist at `docs/reviews/biochemistry-reviewer-checklist-0.4.79.md`. It describes the eight candidate gate types, four course-level gates, record requirements, and the evidence tool's identity and qualification limitations. The checklist does not create reviewer evidence or release approval.

## Historical graded-assessment archive triage (2026-10-11)

Added `docs/HISTORICAL_ASSESSMENT_ARCHIVE_RECOVERY.md` to explain the privacy-preserving aggregate audit statuses, exact-source evidence threshold, and conservative human handling of unverifiable or inconsistent historical submissions. It distinguishes public course-package backfill from private assessment-source recovery and forbids reconstruction from current files or direct database repair. This is operator guidance; it does not recover data or enable historical regrading.

## Biochemistry 0.4.79 protein-purification lab walkthrough (2026-10-11)

Expanded the synthetic-data purification lab with a worked table for all four fractions: total protein, total activity, specific activity, activity recovery and fold enrichment. The new comparison makes the crude baseline explicit and states that one observation per fraction cannot estimate replicate variability. It remains a paper-only virtual lab, with no real protein, experimental procedure, or evidence of a physical separation.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **99 passed**, including a regression that recalculates all four displayed rows from the synthetic CSV. |
| Review snapshot/evidence tests | **8 passed**; the version-bound package digest, generated reports and evidence-register structure checks passed. |
| Private grader and one-field mutation audit | **122 questions, 247 response fields and 247 mutations**; each keyed response received full credit and each single-field mutation lost exactly that field’s points. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Public-package snapshot | 70 files, 1,116,201 bytes; archive SHA-256 `2a3e4df695f46db6ef54426db20e0594420815ef3adda0dece17c83bfb86ff61`; manifest SHA-256 `f9f3fac07002318bf85ecd13324ca5cdbb4e2d2d544c90a3407544cdd14b7aa2`. |

The cumulative final maps all 75 lesson objectives, but the course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.79-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.79.md) bind this package.

## Biochemistry 0.4.78 cumulative-final urea-cycle ledger (2026-10-11)

Added final case 52 using the lesson’s synthetic closed-balance load of 5 mol nitrogen atoms. It yields 2.50 mol urea, 7.50 mol ATP molecules and 10 mol high-energy phosphate equivalents, keeping the ATP-to-AMP cost explicit and treating the load as stoichiometry rather than a measured rate. The inactive cumulative final now has 52 cases and 520 proposed points, mapping all 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **98 passed**. |
| Full backend and content suite | **8,058 passed, 5 skipped**; skips cover unsupported symbolic response builders and Windows symlink tests. |
| Review snapshot/evidence tests | **8 passed**; the package digest, generated reports and evidence-register structure checks passed. |
| Private grader and one-field mutation audit | **122 questions, 247 response fields and 247 mutations**; each keyed response received full credit and each single-field mutation lost exactly that field’s points. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Public-package snapshot | 70 files, 1,114,442 bytes; archive SHA-256 `37efca303772bce4d682f1f7599b2a30bde20747fb24b3b938d98aed3ffe3dc2`; manifest SHA-256 `5b429f510372a884734f9650ad60c062737537977272d55b0b227e16f90e0703`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.78-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.78.md) bind this package.

## Biochemistry 0.4.77 cumulative-final labeled-ribose case (2026-10-11)

Added final case 51 using a synthetic ribose isotopomer distribution: M+1 plus M+2 equals 60% labeled ribose. The item supports labeled-carbon appearance under the stated model and explicitly avoids inferring oxidative/nonoxidative branch contributions or a quantitative PPP rate from the isotopomer fraction alone. The inactive cumulative final now has 51 cases and 510 proposed points, mapping 74 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **97 passed**. |
| Review snapshot/evidence tests | **8 passed**; the package digest, generated reports and evidence-register structure checks passed. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Public-package snapshot | 70 files, 1,123,023 bytes; archive SHA-256 `59b23cac4e3e1193d064d131c4bfae26e5d3dc287f5b62e3950c2d682fa64092`; manifest SHA-256 `5c1a2a928260e107af2c960f428e600079dbb6ced6fe77ec7e43ab033a65a1f2`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.77-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.77.md) bind this package.

## Biochemistry 0.4.76 cumulative-final amino-acid tracer case (2026-10-11)

Added final case 50 using the lesson’s synthetic adipocyte tracer comparison: modeled BCAA contribution to lipogenic acetyl-CoA changes from 8% to 26%, a rise of 18 percentage points. The interpretation remains specific to the modeled pool and cultured-cell states; it does not imply total oxidation, whole-body flux or net glucose from leucine. The inactive final now has 50 cases and 500 proposed points, mapping 73 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **96 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.76. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **120 keyed questions across 243 response fields**; **243 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,119,488 bytes; archive SHA-256 `ec942ca7db746aacc12b27a6c16ccf99933b94616bbbf18dca3d75d6bd6a29f5`; manifest SHA-256 `4501e24e1696c7ec5b047c65d09cb0189704a29befad2eded1d4c8d423529537`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.76-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.76.md) bind this package.

## Biochemistry 0.4.75 cumulative-final neutral-lipid/VLDL case (2026-10-11)

Added final case 49 tracing glycerol-3-phosphate through lysophosphatidic acid, phosphatidic acid and diacylglycerol to TAG, then connecting hepatic TAG storage to VLDL export. The inactive final now has 49 cases and 490 proposed points, mapping 72 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **95 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.75. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **119 keyed questions across 241 response fields**; **241 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,115,737 bytes; archive SHA-256 `d8c3338c2ec4acbc78c206495f85adeef4c64a4ad63a89936b4f341e0df61c00`; manifest SHA-256 `f438b24b1402f9e33a8ac5a985d4224d3845224861a7f5f212f6206607ab3eef`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.75-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.75.md) bind this package.

## Biochemistry 0.4.74 cumulative-final citrate-shuttle and malonyl-CoA case (2026-10-11)

Added final case 48 connecting citrate export and ATP-citrate-lyase regeneration of cytosolic acetyl-CoA to ACC regulation. The response also captures malonyl-CoA’s dual role as a fatty-acid-synthesis substrate and CPT1 inhibitor. The inactive final now has 48 cases and 480 proposed points, mapping 71 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **94 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.74. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **118 keyed questions across 239 response fields**; **239 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,112,380 bytes; archive SHA-256 `59f5b0d18a6936bfc4fe1dcafc760a86252c985f9954c244cca1ab37fe044c97`; manifest SHA-256 `f397117ff5fecbff1205c3838e5571cd3f8303ec3732840ecb22b19ae3dac917`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.74-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.74.md) bind this package.

## Biochemistry 0.4.73 cumulative-final nitrogen and carbon-fate case (2026-10-11)

Added final case 47 separating alanine's transferred amino group from its pyruvate carbon skeleton, then applying the mammalian acetyl-CoA net-carbon boundary. It distinguishes label appearance in downstream pools from net glucose production. The inactive final now has 47 cases and 470 proposed points, mapping 70 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **93 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.73. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **117 keyed questions across 237 response fields**; **237 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,108,724 bytes; archive SHA-256 `a1cbdaa5e444415edc204967028e6b23ac6f2f2d88b954dfeb946f2f5eba94b9`; manifest SHA-256 `d7692aa59e7c6eeef6e43e6acc1de81b9cae0aef89c631ddd342e42c1bf2dadb`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.73-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.73.md) bind this package.

## Biochemistry 0.4.72 cumulative-final amino-acid carbon-fate case (2026-10-11)

Added final case 46 mapping alanine to pyruvate, aspartate to oxaloacetate, leucine to acetyl-CoA/acetoacetate, and phenylalanine to fumarate plus acetoacetate. The companion classification distinguishes glucogenic, exclusively ketogenic, and mixed carbon fates. The inactive final now has 46 cases and 460 proposed points, mapping 69 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **92 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.72. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **116 keyed questions across 235 response fields**; **235 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,105,266 bytes; archive SHA-256 `52f0b4b75961f93046d2d1b641d8ad63b8c128d18091b788ff48651328ff448b`; manifest SHA-256 `bfcc425627effcff5438d6590ad4b0be934af53315be6d019fc2d8e636b850ec`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.72-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.72.md) bind this package.

## Biochemistry 0.4.71 cumulative-final pentose-demand case (2026-10-11)

Added final case 45 for reversible nonoxidative pentose-phosphate carbon rearrangement. Six mol F6P and three mol G3P form nine mol pentose-phosphate equivalents while preserving 45 mol of carbon equivalents. A second response distinguishes NADP+ as a G6PD substrate from a complete flux predictor and relates glycolytic intermediates to ribose demand. The inactive final now has 45 cases and 450 proposed points, mapping 68 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **91 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.71. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **115 keyed questions across 233 response fields**; **233 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,101,816 bytes; archive SHA-256 `1566448e7343d13fe16e3979ee6977d6d6905f6423bf79b23dab92781c8496ae`; manifest SHA-256 `dad7382947b877f0bbdabfb6c11dc4522af5a7908ddeee38dd21476c7a1b5fbf`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.71-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.71.md) bind this package.

## Biochemistry 0.4.70 cumulative-final inhibition-method case (2026-10-11)

Added final case 44 to distinguish the supported competitive-inhibition pattern from misuse of reciprocal plots and to select a trustworthy initial-rate interval. The fitted y-intercept is unchanged while the slope rises; a separate synthetic interval has 4% substrate use with no product-inhibition signal, compared with a late interval at 18% use with a signal. The inactive final now has 44 cases and 440 proposed points, mapping 67 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **90 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.70. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **114 keyed questions across 231 response fields**; **231 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,097,918 bytes; archive SHA-256 `c67df9b05652757f8c1183c99d20e789637990377bd038155d23ef26bee87e37`; manifest SHA-256 `ed4d3e06385d24de1f9ac8599a9ad19be729247d68ff5329c5ae68e0c743ffa7`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.70-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.70.md) bind this package.

## Biochemistry 0.4.69 cumulative-final kinetic-parameter case (2026-10-11)

Added final case 43 using synthetic double-reciprocal fits. From the shared 0.0100 min/μM intercept, the case derives Vmax = 100 μM/min in both conditions; the slopes give control Km = 5 μM and inhibitor Km,app = 15 μM. With 4 μM inhibitor, Ki = 2 μM. The inactive final now has 43 cases and 430 proposed points, mapping 66 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **89 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.69. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **113 keyed questions across 229 response fields**; **229 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,093,026 bytes; archive SHA-256 `38a588e7190634659fc0241c6492e92fc8b37ae3503070de1a0edcf0999629e1`; manifest SHA-256 `9062b4646ca4d9df276aa89bef02009da7b04959297e28dcb3ecbcf90f6df62c`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.69-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.69.md) bind this package.

## Biochemistry 0.4.68 cumulative-final replicate-summary case (2026-10-11)

Added final case 42 for four synthetic initial-rate groups: control and inhibitor at 2.5 and 20 μM substrate, each with three independent reactions. Learners calculate each group mean and preserve both experimental factors in the summary. The inactive final now has 42 cases and 420 proposed points, mapping 65 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **88 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.68. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **112 keyed questions across 227 response fields**; **227 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,089,150 bytes; archive SHA-256 `54cae6cf81bc75e0d2f622a76a7bf4c304ed18288dd82de440c3dd716ba5e86f`; manifest SHA-256 `4bedf27a3c61fda442507b480a1ecea17a45a516e719db75fa0f4aec1f33aaa8`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.68-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.68.md) bind this package.

## Biochemistry 0.4.67 cumulative-final mutation and proteostasis case (2026-10-11)

Added final case 41 for a synthetic destabilizing substitution. A −8.00 kJ/mol change in unfolding free energy raises K_u by 25.2-fold; the variant remains about 99.895% folded, while its unfolded fraction rises about 25.18-fold. The case links marginal stability to increased chaperone and degradation demand. The inactive final now has 41 cases and 410 proposed points, mapping 64 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **87 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.67. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **111 keyed questions across 222 response fields**; **222 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,082,158 bytes; archive SHA-256 `2fbbf6e469671d346fc7effb219c8336956be7584816be623d1c37c5c8eb63fa`; manifest SHA-256 `4ed409fed8e2db28f5cbea6c0a97160755e989e893e961678631e5ffe735280a`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.67-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.67.md) bind this package.

## Biochemistry 0.4.66 cumulative-final denaturant-stability case (2026-10-11)

Added final case 40 for a synthetic two-point denaturant series. The linear model gives m = 10.0 kJ mol⁻¹ M⁻¹, ΔG_H₂O = 21.0 kJ/mol, and C_m = 2.10 M. The inactive final now has 40 cases and 400 proposed points, mapping 63 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **86 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.66. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **110 keyed questions across 220 response fields**; **220 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,078,099 bytes; archive SHA-256 `4e1e4f9b0bd33e42fb7937449c3b1c6852ad39c5929db1c1c6c495862a269415`; manifest SHA-256 `8c51697b35e557d9fc0d3d155f9267807d045e9c7bcc19da0ddd0090e4b3f102`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.66-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.66.md) bind this package.

## Biochemistry 0.4.65 cumulative-final two-state folding case (2026-10-11)

Added final case 39 for a synthetic two-state protein equilibrium. From ΔG_unfold = +8.00 kJ/mol and RT = 2.479 kJ/mol, the case evaluates Ku = exp(−ΔG/RT) = 0.039672 and f_folded = 1/(1+Ku) = 0.961842, then checks the sign and population interpretation. The inactive final now has 39 cases and 390 proposed points, mapping 62 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry regressions | **85 passed**. |
| Review snapshot/evidence tests | **8 passed**; the public digest, empty evidence register and generated reports match version 0.4.65. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register checks and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; no reviewer signoffs or operator approval are recorded. |
| Private answer and actual-grader audit | All private fingerprints match. The actual grader awarded full credit to **109 keyed questions across 218 response fields**; **218 one-field mutations** each lost exactly their field points. |
| Broader content regression checks | **195 passed, 2 skipped**; five assertions still expected an older repository-wide inventory. Updated them to the validated totals and reran those five affected cases: **5 passed**. |
| Public-package snapshot | 70 files, 1,074,806 bytes; archive SHA-256 `c732e944fa3e4d064d1b1657232ba92605ae807069d1a4f21874e53e2aca1c64`; manifest SHA-256 `a5a7182fbb14a61a5eb70e8d2a644da8ee757e2ba6328bde03a922297a7fc79d`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.65-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.65.md) bind this package.

## Biochemistry 0.4.64 cumulative-final connected-pathway case (2026-10-11)

Added final case 38 from the pathway-integration lesson. It calculates the initial accumulation rate after a partial block and predicts reduced downstream delivery, while separating that immediate response from possible later feedback or alternate routing. The inactive final now has 38 cases and 380 proposed points, mapping 61 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **94 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **108 keyed questions across 216 response fields**; **216 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,071,227 bytes; archive SHA-256 `d7755319f767ac8743c9d1e500993ab4b81810fc65d8a81519371e62ae41e698`; manifest SHA-256 `0b468bbe0743757580a5f5a0af0157f43772ed16894f9cfe83f4442b5a4b57c0`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.64-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.64.md) bind this package.

## Biochemistry 0.4.63 cumulative-final regulation-layer case (2026-10-11)

Added final case 37 from the pathway-regulation lesson. It distinguishes changes in substrate supply, rapid allosteric response, covalent modification and slower enzyme expression from controlled synthetic observations. The inactive final now has 37 cases and 370 proposed points, mapping 60 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **93 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **107 keyed questions across 214 response fields**; **214 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,066,514 bytes; archive SHA-256 `83966068278d81b38ec8221555a477265fa2d827c9cf782e438c02dad3b5ad16`; manifest SHA-256 `34f6e40536753e2653029a966ad03e0b93b93d8cd22192c25782527e6035ff43`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.63-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.63.md) bind this package.

## Biochemistry 0.4.62 cumulative-final catalytic-efficiency case (2026-10-11)

Added final case 36 from the enzyme-mechanisms lesson. It converts Km to molar units, calculates kcat/Km, compares the low-substrate regime with near saturation, and distinguishes catalytic efficiency from binding affinity. The inactive final now has 36 cases and 360 proposed points, mapping 59 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **92 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **106 keyed questions across 212 response fields**; **212 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,059,345 bytes; archive SHA-256 `1b1a7b9bdd7af6c390546225b0ad62c41511383da8fc821509fa3b5fe9abc112`; manifest SHA-256 `877302d509ebbbc3e5315ff0637def1d4903969a4496b3cc03174fcdbaacee51`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.62-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.62.md) bind this package.

## Biochemistry 0.4.61 cumulative-final protein-charge case (2026-10-11)

Added final case 35 from the amino-acid charge lesson. It calculates a modeled charge shift with pH, then predicts migration direction and cation/anion-exchange binding from pH relative to pI. The inactive final now has 35 cases and 350 proposed points, mapping 58 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **91 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **105 keyed questions across 210 response fields**; **210 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,054,442 bytes; archive SHA-256 `47d80b4064332b9111ae2e4ea31f9178200e48284bcf81f30346dead71c550eb`; manifest SHA-256 `02454f3ce5310bbec18b6043d3b114bcb1b61c71f31464ae87e16a0535bd7758`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.61-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.61.md) bind this package.

## Biochemistry 0.4.60 cumulative-final isoelectric-point case (2026-10-11)

Added final case 34 from the amino-acid charge lesson. It calculates alanine’s pI and applies the correct pKa brackets to amino acids with acidic and basic side chains. The inactive final now has 34 cases and 340 proposed points, mapping 57 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **90 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **104 keyed questions across 208 response fields**; **208 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,050,228 bytes; archive SHA-256 `81e225cf95c917570c25ab356075330e1708ae243e6f56bfd788ba6abd42c174`; manifest SHA-256 `d057a127637a563a0f0d963a588d8e233ddee30f3f41df8acbc624dba413976c`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.60-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.60.md) bind this package.

## Biochemistry 0.4.59 cumulative-final protonation case (2026-10-11)

Added final case 33 from the amino-acid charge lesson. It sums fractional charges for a synthetic short peptide using separate acid and base protonation equations and identifies the independent-group approximation. The inactive final now has 33 cases and 330 proposed points, mapping 56 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **89 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **103 keyed questions across 206 response fields**; **206 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,045,664 bytes; archive SHA-256 `30a3eb899673879384d2a4dbf062190ed1cfb6f840c065c815fdbc0c6409f136`; manifest SHA-256 `41095e1fdad8be7549bb2246fd3388c31bfab3cc771294fd79ccee4903ff54b5`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.59-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.59.md) bind this package.

## Biochemistry 0.4.58 cumulative-final pool/flux case (2026-10-11)

Added final case 32 from the flux-regulation lesson. It compares two steady-state perturbations with the same 8 mM intermediate pool but different pathway fluxes, reinforcing that a pool size alone does not measure flow. The inactive final now has 32 cases and 320 proposed points, mapping 55 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **88 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **102 keyed questions across 204 response fields**; **204 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,040,508 bytes; archive SHA-256 `789c98e75793b41daaa66b8d84c63e23721635403aa59bbc4194ac677ee697f9`; manifest SHA-256 `7961bbba910d789034dea3a1f0d7ec2348f51b4354fb676d55c9b1ab668ae104`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.58-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.58.md) bind this package.

## Biochemistry 0.4.57 cumulative-final cooperative-binding case (2026-10-11)

Added final case 31 from the binding-equilibria lesson. It calculates hemoglobin-like oxygen unloading between lung and tissue pressures, compares a non-cooperative myoglobin-like curve, and treats the Hill coefficient as a steepness parameter rather than a site count. The inactive final now has 31 cases and 310 proposed points, mapping 54 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **87 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **101 keyed questions across 202 response fields**; **202 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,035,583 bytes; archive SHA-256 `a233903ff793cb163505d3096e8c625c099747e1f217e8ac154e8b7ffd3b257f`; manifest SHA-256 `48ac2e0fa94a2206f38636efb79f17c212c11d5663d374816a0b576a1a9f73aa`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.57-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.57.md) bind this package.

## Biochemistry 0.4.56 cumulative-final enzyme-turnover case (2026-10-11)

Added final case 30 from the flux-regulation lesson. It uses an 18-hour enzyme half-life to calculate the 90% transition time after a synthesis-rate change, then distinguishes enzyme-abundance turnover over hours to days from rapid allosteric and covalent control. The inactive final now has 30 cases and 300 proposed points, mapping 53 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **86 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **100 keyed questions across 200 response fields**; **200 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,031,056 bytes; archive SHA-256 `b3f25634ed263d88a85ff7712ccae339b9265aa046213fbc242f576b79591ea8`; manifest SHA-256 `3ccf50efc11dce4f87cdcd3d4fa624ac2511ca52cb309d25b0a8c98040c2599e`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.56-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.56.md) bind this package.

## Biochemistry 0.4.55 cumulative-final pathway-block case (2026-10-11)

Added final case 29 from the week-14 lesson. It calculates glucose uptake and lactate output required when oxidative phosphorylation is blocked, then compares oxygen-consumption evidence for a respiratory-chain block and a primary glycolytic defect with alternate-fuel support. The inactive cumulative final now has 29 cases and 290 proposed points, mapping 52 of 75 lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **85 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. Git reports line-ending normalization notices only. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded inventories match. The actual grader awarded full credit to **99 keyed questions across 198 response fields**; **198 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 1,027,201 bytes; archive SHA-256 `267c3e2af73637078965b02327715e05a120119f1ede73c3302be27c3b77d164`; manifest SHA-256 `80dcf33125ab64c46702afd1e0f8951991c072a6105e0b0919e029cafd963dbe`. |

The course remains partial, formative-only and unreviewed. Qualified scientific and assessment review, accessibility/fairness review, measured workload, institutional scope/equivalency review, physical laboratory training and operator release approval remain open. The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.55-finalized.json) and prospective [workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.55.md) bind this package.

## Biochemistry final redox/tracer interpretation case (0.4.54, 2026-10-11)

Added a synthetic matched-culture case that estimates the medium-glucose contribution to lactate from M+3 enrichment and reads the lactate/pyruvate ratio as LDH-linked redox context at fixed pH. Its interpretation explicitly distinguishes a tracer source fraction from a flux rate. The cumulative final now has 28 inactive cases and 280 proposed points; it maps 50 of 75 Biochemistry lesson objectives.

| Actual command/check | Result |
| --- | --- |
| Biochemistry and assessment-candidate regressions | **84 passed**. |
| Content validation with private assessment root | **25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases**; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective-gap report, review-evidence check, Ruff and `git diff --check` | Passed; the candidate register remains inactive with 88 candidate gates and four course-wide gates unresolved. Git emitted line-ending notices only. |
| Private answer fingerprint and actual grader audit | **98 keyed questions, 196 fields and 196 one-field mutations** passed; each incorrect field lost exactly its assigned points. |
| Public package | 70 files, 1,021,492 bytes; archive SHA-256 `2591bd0dd766af39d5b21e4a9b8d30df7dcf045a5da5be3fd59d0d727cac9dd5`; manifest SHA-256 `7481201deb5cf2bb044358e12a99ea758c259fcd3dd0a566a66ca8beea5f1eae`. |

The course remains partial, formative-only and unreviewed. No reviewer signoffs, learner workload evidence or operator release decision were added.

## Previous increment: Biochemistry final distributed flux-control case (0.4.53, 2026-10-11)

Added a synthetic pathway case that uses the coefficient summation theorem and predicts a small perturbation's effect on flux. The cumulative final now has 27 inactive cases and 270 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **83 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **97 keyed questions, 194 fields and 194 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 1,015,806 bytes; archive SHA-256 `433bd4dc74bf2a37091d99cbcdebcace2b340a2a77b680fdeac9dbf98db22c78`; manifest SHA-256 `8bfb07b6919a9f59e8223ff7bd3fec9f90bba39236c898d717ce13f7cc3c406f`. |

## Previous increment: Biochemistry final uncoupling/ATP-turnover case (0.4.52, 2026-10-11)

Added a quantitative oxygen/P/O comparison that distinguishes electron flow from oxidative ATP production under uncoupling. The cumulative final now has 26 inactive cases and 260 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **82 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **96 keyed questions, 192 fields and 192 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 1,012,905 bytes; archive SHA-256 `e18af224675b4f7a4f87ec624d01270babf6bc553cad99034e47da4a29ba0156`; manifest SHA-256 `aa650f59ae1cea1bc2b34b1d4ce1ec7be0214bad0272fe6eee90e5155cf4af04`. |

## Previous increment: Biochemistry final exact ligand-depletion case (0.4.51, 2026-10-11)

Added an exact quadratic binding calculation with a comparison against the hyperbolic approximation that substitutes total ligand for free ligand. The cumulative final now has 25 inactive cases and 250 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **81 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **95 keyed questions, 190 fields and 190 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 1,009,419 bytes; archive SHA-256 `e7f4e4545f11bbcc418e15bbdbb079ab3eaa81be80784334a2ebb6c61c84b54e`; manifest SHA-256 `b1160a3a42eabb1f39139f486ae35d5d4d3d0cc1fb5b3ade28a46279dd930e4a`. |

## Previous increment: Biochemistry final redox free-energy/coupling case (0.4.50, 2026-10-11)

Added a cytochrome-c-to-oxygen redox calculation and an interpretation of how electron-transport energy release couples through a proton gradient to ATP synthesis. The cumulative final now has 24 inactive cases and 240 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **80 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **94 keyed questions, 188 fields and 188 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 1,006,425 bytes; archive SHA-256 `0f4efd4c32bec3980f6c7ba1eeee8b6011d3bc0d121eea468707580c15930dd9`; manifest SHA-256 `3c9f41bcd644838e3c662aded31510ba5f9b93f33792201f85c312cf9a826247`. |

## Previous increment: Biochemistry final protein structure hierarchy (0.4.49, 2026-10-11)

Added a two-part protein-structure case: a sequence substitution directly changes primary structure, while tetramer dissociation removes quaternary association without necessarily unfolding individual chains. The cumulative final now has 23 inactive cases and 230 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **79 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **93 keyed questions, 186 fields and 186 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 1,003,291 bytes; archive SHA-256 `1726efdb4713e1c749063b6915546f9eb9dfc200782fa74058d72049d0ad0f05`; manifest SHA-256 `58b51a7da513abf19921692a7415b5f52c728228d8866da49779fcfdba6e1036`. |

## Previous increment: Biochemistry final PFK pool/flux case (0.4.48, 2026-10-11)

Added a synthetic glycolysis-control case that checks the ATP/AMP effectors of PFK-1 and computes a measured glucose-uptake rate change while distinguishing rates from the fructose-6-phosphate pool. The cumulative final now has 22 inactive cases and 220 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **78 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **92 keyed questions, 184 fields and 184 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 1,000,107 bytes; archive SHA-256 `069445dcc53cc2a4e82a1bf7fd2c96fe242e7bfaffbe56c23d46a6ff6307803d`; manifest SHA-256 `ababcf04d1c9912b9c8e2f644dbf59847dc09d72ef5e18b582a924fcf06bb557`. |

## Previous increment: Biochemistry final TCA pool/flux interpretation (0.4.47, 2026-10-11)

Added a synthetic intermediate-pool balance with anaplerotic input, cataplerotic withdrawal and relative redox/energy ratios. The case explicitly separates pool balance from cycle-flux inference. The cumulative final now has 21 inactive cases and 210 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **77 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **91 keyed questions, 182 fields and 182 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 995,001 bytes; archive SHA-256 `854a16e60f3eb27410946a8906a5458b816ea98ebf83ec895ec256c401450360`; manifest SHA-256 `981221f3c464dd33dd56f05d95e2671b4f68b6e041bb3329503c8a25a8ccad3c`. |

## Previous increment: Biochemistry final gluconeogenesis cost/source case (0.4.46, 2026-10-11)

Added a paired calculation and interpretation case for ATP/GTP cost and the even-chain fatty-acid carbon boundary. The cumulative final now has 20 inactive cases and 200 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **76 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **90 keyed questions, 180 fields and 180 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 991,244 bytes; archive SHA-256 `6d8ab52e8a3313c00f09aa0f8ca104437ae523930b65a4452e82be651e57ea6b`; manifest SHA-256 `f406b89623f3ffa094dfa2a8b9b2b3f2451a39e380c72e8959d6daa318778256`. |

## Previous increment: Biochemistry final citrate-label/flux case (0.4.45, 2026-10-11)

Added a synthetic citrate isotopologue case that computes the change in labeled fraction and separates labeling from a quantitative TCA-flux inference. The cumulative final now has 19 inactive cases and 190 proposed points.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **75 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, version-bound review-register check and Ruff | Passed. |
| Private actual-grader audit | **89 keyed questions, 178 fields and 178 single-field mutations** passed; every mutation lost exactly its field points. |
| Public package | 70 files, 988,039 bytes; archive SHA-256 `34333bbb1396fd61fae6a89f67ae54fa1a0f2bae6844b8556c50bf630e2ca04b`; manifest SHA-256 `bc2ec9a782c784fd70f6552519a5b1ef00f80e80ff494b8d139f2b4326d20f22`. |

## Previous increment: Biochemistry final conditional-ketone case (0.4.44, 2026-10-11)

Added cumulative-final case 18 to calculate conditional acetoacetate ATP-equivalents and interpret mouse hepatic isotope evidence within its species and pathway boundary. Distinct synthetic parameters are provided; the candidate stays inactive.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **74 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded question inventories match. The actual grader awarded full credit to **88 keyed questions across 176 response fields**; **176 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 974,603 bytes; archive SHA-256 `c47d4bde60c2e3bf83fceefd96aea6e20f81572da5bd7eae85b5bef11184f15a`; manifest SHA-256 `bb6466cedb2f24bb6bd5f8838ab136e1237506b9b9c570a12e1a5fa3f697e144`. |

## Previous increment: Biochemistry final glycolysis/uncoupling case (0.4.43, 2026-10-11)

Added cumulative-final case 17 to check glycolytic pyruvate/ATP/NADH accounting and the distinction between oxygen use and ATP synthesis under uncoupling. Each response field maps to the corresponding bioenergetics objective. The case is inactive and adds no required learner workload.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **73 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded question inventories match. The actual grader awarded full credit to **87 keyed questions across 174 response fields**; **174 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 970,491 bytes; archive SHA-256 `38853ad2a4e7311faa9e13b71d39e03c587774619f7436672feb59d5add7f634`; manifest SHA-256 `8fb18bbafb74dfc9eb5bf8b11ff54b80a06e0abda1592b03e014407feef08486`. |

## Previous increment: Biochemistry cumulative fatty-acid objective mapping (0.4.42, 2026-10-11)

Corrected the alignment of the existing palmitate ATP-yield calculation to the fatty-acid objective for integrating beta-oxidation, the TCA cycle and electron transport. Updated the formative question and final case mapping plus candidate evidence/fingerprints; no question, answer key or workload was added. All candidates remain inactive.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **72 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded question inventories match. The actual grader awarded full credit to **86 keyed questions across 172 response fields**; **172 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 967,226 bytes; archive SHA-256 `e690c7ef76975c9e8c5d94a8147f92f51779da92d1ad306b73c4cdb314ab9f16`; manifest SHA-256 `8b9ee7d3528dc9c08b1b5659c4a5591e740f7c571b68667a8fe121bf9d5840ea`. |

## Previous increment: Biochemistry week-9 ATP pool-balance expansion (0.4.41, 2026-10-11)

Added a synthetic quantitative objective for ATP-pool amount change from stipulated synthesis and utilization rates, bounded separately from turnover, concentration and pathway flux. Added two formative checks, a retrieval card, Homework 5 case 09 and cumulative final case 16. All public machine-candidate inventories match their private drafts; assessments remain inactive.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **72 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded question inventories match. The actual grader awarded full credit to **86 keyed questions across 172 response fields**; **172 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 966,577 bytes; archive SHA-256 `2fa6abcaf2d5cb8e0fdeffebed34b2c352c99f063d66d61fabbc42b836f69149`; manifest SHA-256 `39693203e61b46409f08a472c085c3a971bc5146cf1f0fa71b9260f365eb9400`. |

## Previous increment: Biochemistry week-9 mixed-route nucleotide accounting expansion (0.4.40, 2026-10-11)

Added a synthetic quantitative objective for PRPP use across de novo purine synthesis and salvage, while separately accounting for ATP/GTP at the IMP branch point. Added two formative checks, a retrieval card, Homework 5 case 08, and cumulative final case 15. All public machine-candidate inventories match their private drafts; assessments remain inactive.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **70 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,409 questions, 1,340 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded question inventories match. The actual grader awarded full credit to **84 keyed questions across 168 response fields**; **168 one-field mutations** each lost exactly their field points. |
| Public-package snapshot | 70 files, 956,243 bytes; archive SHA-256 `00d6ea874cd1fb4dce64f9e6247a71dab733c2d097edde06bb04ab3febc99aa4`; manifest SHA-256 `1f1cfb9de500b1fb975d25c385a4f7b39673c1a1c4520c82b583df839f661f96`. |

## Previous increment: Biochemistry week-12 cholesterol-pool accounting expansion (0.4.39, 2026-10-11)

Expanded the cholesterol/lipoprotein lesson with a defined-cell mass balance and a synthetic calculation, while bounding its relevance to plasma LDL and whole-body sterol balance. Added one objective, two formative items and a retrieval card. Inactive Homework 7 now has nine cases and 90 proposed points; the cumulative final has 14 cases and 140 proposed points, with distinct cases aligned to the new objective. All machine-graded public/private question inventories match; no assessment was activated.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **67 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,407 questions, 1,339 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded question inventories match. The actual grader awarded full credit to **82 keyed questions across 164 response fields**; **164 one-field mutations** each lost exactly their field points. The human-scored project remains outside automatic grading. |
| Biochemistry public-package snapshot | 70 files, 962,660 bytes; archive SHA-256 `98c9ce1ea33f6ffa917fb62c6fd84e9901d500fb27190c5df37f8dffdda143b5`; manifest SHA-256 `2583b6942be492c0d37afb17c157342011b09bbf62f99f2fa04f374bfe6f6a34`. |

## Previous increment: Biochemistry week-2 urea-cycle stoichiometry expansion (0.4.38, 2026-10-11)

Expanded the urea-cycle lesson with a closed-balance calculation that separates stoichiometric urea/energy demand from pathway rate and ATP-pool change. Added one objective, two formative items and a retrieval card. Inactive Homework 1 now has eight cases and 80 proposed points, and the inactive midterm has 12 cases and 120 proposed points to cover the added first-seven-week objective. A private-key coverage audit found and repaired missing protected entries for the newly added Homework 8 tracer and Homework 1 urea cases. All machine-graded public/private question inventories now match; no assessment was activated.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **66 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,405 questions, 1,338 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All private fingerprints and machine-graded question inventories match. The actual grader awarded full credit to **80 keyed questions across 160 response fields**; **160 one-field mutations** each lost exactly their field points. The human-scored project remains outside automatic grading. |
| Biochemistry public-package snapshot | 70 files, 950,965 bytes; archive SHA-256 `f5bbba1db79de93d47db9dfa9da26e93a07834db568e924e97bacc6afc9a273e`; manifest SHA-256 `6a9612cc511c5b77d7599b39e012d6ebae3192a687828f3f5c988bfb54717a83`. |

## Previous increment: Biochemistry week-13 PPP isotope-tracer expansion (0.4.37, 2026-10-11)

Expanded the pentose-phosphate lesson with a synthetic [1,2-13C2]glucose/ribose isotopomer calculation and an explicit boundary between label incorporation and quantitative branch-flux inference. Added two link-only primary references, a third objective, two formative items and a card. Inactive Homework 8 now has ten synthetic cases and 100 proposed points, including the two-field tracer case. All eleven private candidates target package 0.4.37; no assessment was activated.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **64 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,403 questions, 1,337 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective coverage, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All 11 private drafts match public candidate, instruction, dataset and prerequisite fingerprints. The actual grader awarded full credit to all **77 keyed questions across 154 response fields**; **154 one-field mutations** each lost exactly their field points. The human-scored project remains outside automatic grading. |
| Biochemistry public-package snapshot | 70 files, 940,894 bytes; archive SHA-256 `5bbd1b87903c18b1e5728052810727e18d65a2aa5c08cf8bad4ce6f9bd9799f4`; manifest SHA-256 `f646b74e80194f7a70aa4b657a2d8d959d95f56a35b93771eec2ce395aa52926`. |

## Previous increment: Biochemistry week-2 amino-acid carbon-skeleton and tracer expansion (0.4.36, 2026-10-11)

Expanded the amino-acid carbon-skeleton lesson with a representative entry-point table, separate nitrogen and carbon ledgers, the net-carbon limit on acetyl-CoA, and an isotope-tracing example bounded to differentiated adipocyte cultures. Added a third lesson objective, two formative items and one card with a link-only primary reference. Homework 1 now has a seventh inactive case (70 proposed points) with synthetic percentage-point data; the midterm’s existing carbon-fate field now also maps to the new tracer objective. All eleven private candidates target version 0.4.36.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **63 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,401 questions, 1,336 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective-coverage reports, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All 11 private drafts match public candidate, instruction, dataset, prerequisite and rubric fingerprints. The actual grader awarded full credit to all **77 keyed responses**; **154 one-field mutations** each lost exactly their field points. The human-scored project remains outside automatic grading. |
| Biochemistry public-package snapshot | 70 files, 914,618 bytes; archive SHA-256 `ec36a6dd8f2814bd5614a9fc491d1fb14c4f41b2dafbe4f295143818aedf5c09`; manifest SHA-256 `d7e05c6f594aa94f09d7c4b29aa280b6a6aaf44c78e83966e095779ecdf14287`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [post-authoring evidence register](reviews/biochemistry-review-evidence-0.4.36-post-authoring.json) and prospective [workload protocol](reviews/biochemistry-workload-pilot-0.4.36.md) identify the exact package. Scientific/assessment review, accessibility/fairness, measured workload, physical laboratory training, institutional equivalency and operator release gates remain open.

## Previous increment: Biochemistry week-11 ketone-body energy accounting and evidence boundary (0.4.35, 2026-10-11)

Expanded the ketone-body lesson with assumption-bound ATP-equivalent calculations for acetoacetate and D-BHB, SCOT's opportunity cost of one GTP-forming step, and a tissue/pathway-specific distinction between canonical oxidative ketolysis and SCOT-independent anabolic use reported in mouse hepatocytes. Added two link-only primary studies, two objective-aligned formative questions/cards and a two-field case to inactive Homework 7; all private candidates are pinned to version 0.4.35. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry lesson and candidate regressions | **62 passed**. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,399 questions, 1,335 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate report, objective-coverage report, review-register check, Ruff and `git diff --check` | Passed. Eleven inactive candidates retain 88 unresolved candidate gates and four unresolved course gates; there are no reviewer signoffs or operator approval. |
| Private assessment fingerprint and actual-grader audit | All 11 private drafts match public candidate, instruction, dataset, prerequisite and rubric fingerprints. The actual grader awarded full credit to all **76 keyed responses**; **152 one-field mutations** each lost exactly 5 points. The human-scored project remains outside automatic grading. |
| Biochemistry public-package snapshot | 70 files, 901,995 bytes; archive SHA-256 `a18e9a7a7d6a74a55594a30c6954ccb424078d02277a5e3b4c786a43b73477b4`; manifest SHA-256 `7f833d898e7b4e06a1b25f515f6518107b299944f8eda08bbd647963eed79428`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [evidence register](reviews/biochemistry-review-evidence-0.4.35.json) and prospective [workload protocol](reviews/biochemistry-workload-pilot-0.4.35.md) bind the exact public package. External scientific/assessment review, accessibility/fairness, measured workload, physical laboratory training, institutional equivalency and operator release gates remain open.

## Previous increment: Biochemistry week-9 TCA isotope-tracing expansion (0.4.34, 2026-10-11)

Expanded the citric-acid-cycle lesson with conditional ¹³C entry patterns, a synthetic labeled-citrate time course, model and identifiability limits, and two link-only primary studies. Added one objective-aligned formative question and retrieval card. Homework 5 now includes a seventh inactive case (70 proposed points total) with matching synthetic CSV rows and an unreviewed private key/grader entry.

| Actual command/check | Result |
| --- | --- |
| Biochemistry course and candidate regressions | 61 passed in 2.54 seconds. |
| Content validator with private assessment root | Passed: 25 courses, 401 lessons, 2,397 questions, 1,333 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Private assessment fingerprint and actual-grader audit | All 11 private drafts match public candidate, instruction, dataset, prerequisite and rubric fingerprints. The actual grader awarded full credit to all 75 keyed responses; 150 one-field mutations each lost exactly 5 points. The human-scored project remains outside automatic grading. |
| Candidate report, objective-coverage report, review-register check, Ruff and `git diff --check` | Passed. Biochemistry has 11 inactive candidates, 88 unresolved candidate gates, 4 unresolved course gates, no reviewer signoffs and no operator approval. |
| Biochemistry public-package snapshot | 70 files, 888,642 bytes; archive SHA-256 `295bac5bc6e2f0fe54411c3c5fa9916f6f7ec51427db4cab3745eb3163297b3e`; manifest SHA-256 `1f97517b8fc5a58bc7b63a3f4b54766bc9ebecc4933404fdaf8f443fc047abc8`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), empty [evidence register](reviews/biochemistry-review-evidence-0.4.34.json) and prospective [workload protocol](reviews/biochemistry-workload-pilot-0.4.34.md) bind this package. All external review, measured-workload, physical-lab, institutional and operator-release gates remain open; the package is not a credit-approved or independently reviewed university course.

## Previous increment: Biochemistry week-1 protein-structure and ensemble expansion (0.4.33, 2026-10-11)

Expanded the week-1 reading with the limits of static structural models, a measured glucose/galactose-binding protein ensemble as a primary example, a synthetic open/closed population-odds calculation, and a checklist matching binding claims to affinity, kinetics and perturbation evidence. Added two link-only primary studies without importing text or figures. Existing formative questions and private answer keys are unchanged; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry course tests and assessment-candidate regressions | 59 passed in 2.58 seconds. |
| Content validator (`uv run --project backend --with jsonschema python tools/validate_content.py`) | Passed: 25 courses, 401 lessons, 2,396 questions, 1,332 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Private assessment fingerprint and actual-grader audit | All 11 private drafts match public candidate, instruction, dataset, rubric and prerequisite fingerprints. The backend grader awarded full credit to all 74 keyed responses; 148 single-field mutations each lost exactly 5 points. The human-scored project remains outside automatic grading. |
| Assessment-candidate and objective-coverage drift checks; Biochemistry review-register check; Ruff and `git diff --check` | Passed. Biochemistry has 11 inactive candidates, 88 unresolved candidate gates, 4 unresolved course gates, no reviewer signoffs and no operator approval. |
| Biochemistry public-package snapshot | 70 files, 894,209 bytes; archive SHA-256 `7ffa65183d03650cfa80d07608534a828d8cf374c463327edb404acaa4d7a229`; manifest SHA-256 `dcfc92ca6312583e9c316b03d34c567f5d747727b304742737609dea098796bb`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), [hash-pinned evidence register](reviews/biochemistry-review-evidence-0.4.33.json) and [prospective workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.33.md) identify this target. Qualified scientific and assessment review, accessibility and fairness review, measured workload, physical laboratory training, institutional scope/equivalency review and operator release approval remain open. The package is prepared for qualified review; authoring tests do not constitute independent review or credit approval.

## Previous increment: Biochemistry week-5 enzyme-mechanism expansion (0.4.32, 2026-10-11)

The week-5 reading now distinguishes reaction-coordinate transition states from intermediates, develops a conditional 298 K activation-barrier comparison, and follows a simplified chymotrypsin acylation/deacylation cycle. Three primary studies are linked as references only; no article assets are imported. The backend unit grammar now supports conventional enzyme activity (`U` = 1 µmol/min), specific activity (`U/mg`) and exact-only fold-change labels, allowing the existing purification practice fields to pass the actual grader. Existing formative questions and private answer keys are unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Combined backend, content and security suite (repository root and backend import paths; UTF-8 mode) | 7,975 passed, 5 skipped in 562.66 seconds. |
| Focused backend grading/unit tests and authored Biochemistry purification items | 165 passed; the new enzyme-unit conversion and fold-label cases pass. |
| Focused Biochemistry mechanism, structure, bioenergetics, regulation and review-snapshot regressions | 6 passed. |
| Content validator (`uv run --project backend --with jsonschema python tools/validate_content.py`) | Passed: 25 courses, 401 lessons, 2,396 questions, 1,332 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Private assessment hash and actual-grader audit | All 11 private drafts match their public candidate, instruction, dataset, rubric and prerequisite fingerprints. The backend grader awarded full credit to all 74 keyed responses; 148 single-field mutations each lost exactly 5 points. The human-scored project remains outside automatic grading. |
| Assessment-candidate report, objective-coverage report, review-register checks, Ruff and `git diff --check` | Passed. Biochemistry has 11 inactive candidates, 88 unresolved candidate gates, 4 unresolved course gates, no reviewer signoffs and no operator approval. |
| Biochemistry public-package snapshot | 70 files, 890,032 bytes; archive SHA-256 `20a86953d264e15b43dc6592c321ceb742f5e2e8cb51609629edd427af92551d`; manifest SHA-256 `54da370abc5f39bf50076618f56de5c006b8915cb5973fdd5612ec016991a546`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), [hash-pinned evidence register](reviews/biochemistry-review-evidence-0.4.32.json) and [prospective workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.32.md) identify this target. The inherited week-1 and week-9 readings remain short. Qualified biochemical and assessment review, accessibility and fairness review, measured workload, physical laboratory training, institutional scope/equivalency review and operator release approval remain open. The package is prepared for qualified review; this authoring validation is not independent review or credit approval.

## Previous increment: Biochemistry week-12 pathway-regulation expansion (0.4.31, 2026-10-11)

Expanded the inherited week-12 pathway-regulation reading to 2,077 words with a clearer pool/flux distinction, local flux-control example and limits, a synthetic two-input isotope-mixing calculation, regulatory layers, and a structured perturbation-analysis method. Added two link-only primary studies to the course source map and registry without importing their content. Existing objectives and assessment keys are unchanged; the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Full cross-course content suite (`uv run --project backend --with jsonschema --with pytest-xdist pytest -n 6 -q tests/content`, repository root on `PYTHONPATH`) | 2,872 passed, 2 skipped in 327.36 seconds. |
| Focused regulation, policy, review-ledger, candidate and project regressions | 22 passed in 5.29 seconds. |
| Content validator | Passed: 25 courses, 401 lessons, 2,396 questions, 1,332 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Private assessment schema, fingerprint and actual-grader audit | All 74 private questions are schema-valid and match current public prompts, options, units and objective links; all 11 private drafts match candidate, prerequisite, instruction, dataset and rubric hashes. The backend grader gave all 74 correct cases full credit; 148 single-field mutations each lost exactly 5 points. |
| Candidate-report drift, objective-coverage drift, Biochemistry and Cell Biology review-register checks, Ruff and `git diff --check` | Passed. Biochemistry has 11 candidates, 88 unresolved candidate gates, 4 unresolved course gates, no reviewer sign-offs and no operator approval. |
| Biochemistry public-package snapshot | 70 files, 884,430 bytes; archive SHA-256 `4f38bbb314553f847be9b4b8e8125235811d0a5c44e31d9459ddc0642b8656c7`; manifest SHA-256 `e40244745e01be72ba2923bd313d71ef714de9f14e2d06f5d1d0ec5605a65243`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), [hash-pinned evidence register](reviews/biochemistry-review-evidence-0.4.31.json) and [prospective workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.31.md) identify the exact review target. Three inherited readings remain short, and qualified biochemical/assessment review, accessibility and fairness review, measured workload, physical laboratory training, institutional scope review and operator release approval remain open.

## Previous increment: Biochemistry inactive grading-policy proposal (0.4.30, 2026-10-11)

Added an inactive course-level policy candidate with illustrative weights, a calculation formula, provisional grade bands and proposed attempt, feedback, extension, accessibility and appeal rules. A new course-level review-ledger gate tracks grading-policy review. The manifest remains formative-only; no candidate is assigned or graded.

| Actual command/check | Result |
| --- | --- |
| Full cross-course content suite (`uv run --project backend --with jsonschema --with pytest-xdist pytest -n 6 -q tests/content`, repository root on `PYTHONPATH`) | 2,871 passed, 2 skipped in 323.83 seconds. |
| Focused policy, review-ledger, candidate and project regressions | 22 passed in 5.63 seconds. |
| Content validator | Passed: 25 courses, 401 lessons, 2,396 questions, 1,332 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Private assessment schema, fingerprint and actual-grader audit | All 74 private questions are schema-valid and match their public prompts, options, units and objective links; all 11 private drafts match current public artifact hashes. The backend grader gave all 74 correct cases full credit; 148 single-field mutations each lost exactly 5 points. |
| Candidate-report drift, objective-coverage drift, Biochemistry and Cell Biology review-register checks, Ruff and `git diff --check` | Passed. Biochemistry has 11 candidates, 88 unresolved candidate gates, 4 unresolved course gates, no reviewer sign-offs and no operator approval. |
| Biochemistry public-package snapshot | 70 files, 874,431 bytes; archive SHA-256 `64ad1242a29dcdfa1303d52a0bbba270a605a3c8157cc4f660f6d97cc06d16b2`; manifest SHA-256 `4d2edb0aea4a2bf425a88fb04a0ef4695f0925a775969e099319d602959ca10a`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), [hash-pinned evidence register](reviews/biochemistry-review-evidence-0.4.30.json) and [prospective workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.30.md) identify the exact review target. Policy adoption, qualified biochemical and assessment review, accessibility and fairness review, measured workload, physical laboratory training, institutional scope review and operator release approval remain open.

## Previous increment: Biochemistry human-scored project candidate (0.4.29, 2026-10-11)

Added an inactive, human-scored portfolio candidate with five deliverables, an uncalibrated 100-point rubric, objective links, and a private worked-solution guide. The public brief no longer exposes the numeric solution. The public package remains partial, unreviewed and formative-only; the project is not scheduled or graded.

| Actual command/check | Result |
| --- | --- |
| Full cross-course content suite (`uv run --project backend --with jsonschema --with pytest-xdist pytest -n 6 -q tests/content`, repository root on `PYTHONPATH`) | 2,870 passed, 2 skipped in 315.14 seconds. |
| Focused project, assessment-candidate, homework/exam and review-snapshot regressions | 23 passed in 27.89 seconds. |
| Content validator | Passed: 25 courses, 401 lessons, 2,396 questions, 1,332 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Private assessment schema, unit, prompt, choice and fingerprint audit | All 74 private graded questions match current prompts/options/units and exact candidate, instruction and dataset hashes; all ten packets have balanced choice positions. |
| Actual backend grader exercise against local private drafts | All 74 correct cases earned full credit; 148 one-field mutations each lost exactly 5 points. This is author-side testing, not independent reviewer evidence. |
| Candidate-report drift, exact-package review-evidence check, targeted Ruff and `git diff --check` | Passed. The register records 11 candidates, 88 unresolved candidate gates, 3 unresolved course gates, no reviewer sign-offs and no operator approval. |
| Biochemistry public-package snapshot | 69 files, 868,234 bytes; archive SHA-256 `a6148db1e9d54900ff05452f416bd518001fd490236edbd3ba37bdc322c6478a`; manifest SHA-256 `643a4a3ee8624cf07ac1acbd7dcaef2863dba813ad969dd7f586f6f2a0204c4c`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), [hash-pinned evidence register](reviews/biochemistry-review-evidence-0.4.29.json) and [prospective workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.29.md) identify the exact review target. The policy, qualified biochemical and assessment review, accessibility and fairness review, workload measurement, physical laboratory training, institutional scope review and operator release approval remain open.

## Previous increment: Biochemistry inactive exam keys and grader-ready candidate repairs (0.4.28, 2026-10-11)

Added unreviewed private key/grader drafts for the inactive midterm and cumulative final; balanced their choice positions, normalized numeric units, specified kinetic-fit instructions and corrected the syllabus case counts. All ten homework/exam candidate keys remain isolated outside the public package and pinned to the exact candidate, instruction and dataset bytes. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Full cross-course content suite (`uv run --project backend --with jsonschema --with pytest-xdist pytest -n 6 -q tests/content`, repository root on `PYTHONPATH`) | 2,868 passed, 2 skipped in 299.38 seconds. |
| Focused homework, midterm, final and package-snapshot regressions | 10 passed. |
| Content validator | Passed: 25 courses, 401 lessons, 2,396 questions, 1,332 cards and 25 cases; 0 errors or warnings. |
| Private assessment schema, unit, prompt, choice and fingerprint audit | All 74 private questions pass `question.schema.json`, match current public prompts/options/units and match exact candidate, instruction and dataset hashes. Choice positions are balanced in all ten packets. |
| Actual backend grader exercise against local private drafts | All 74 correct cases earned full credit; 148 one-field mutations each lost exactly 5 points. This is author-side testing, not independent reviewer evidence. |
| Candidate-report drift, objective-coverage drift, exact-package evidence check, Ruff and `git diff --check` | Passed. The register records 80 unresolved candidate gates, 3 unresolved course gates, no reviewer sign-offs and no operator approval. |
| Biochemistry public-package snapshot | 67 files, 858,529 bytes; archive SHA-256 `87479fd02c0f5e16aa5fdaf8f7ac62f5cf194865953a9f781616794a2ff1f569`; manifest SHA-256 `8d89023258cae72c115a9734b9fad90d7e5e6dbd0aace2e6b154e6f679ce788f`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), [hash-pinned evidence register](reviews/biochemistry-review-evidence-0.4.28.json) and [prospective workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.28.md) identify the exact review target. Qualified biochemical and assessment review, accessibility and fairness review, workload measurement, course grade policy, approved project and laboratory assessments, physical laboratory training, institutional scope review and operator release approval remain open.

## Previous increment: Biochemistry homework keys and grader validation (0.4.27, 2026-10-11)

Balanced choice positions across all eight inactive homework candidates, corrected the H3 enzyme-amount and H4 inhibitor-concentration inputs, specified nonlinear fitting and three-significant-figure responses, and created local unreviewed key/grader drafts outside the public package. The key drafts match the exact public candidate, instruction and dataset hashes. All remain inactive; Biochemistry remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Full cross-course content suite (`uv run --project backend --with jsonschema --with pytest-xdist pytest -n 6 -q tests/content`, repository root on `PYTHONPATH`) | 2,868 passed, 2 skipped in 296.16 seconds. |
| Focused homework-candidate and Biochemistry snapshot regressions | 6 passed. |
| Private assessment question schema and fingerprint audit | All 50 private question specs pass `question.schema.json`; all eight candidates match their instruction and dataset fingerprints, and choice answers match the exact current options. |
| Actual backend grader exercise against private drafts | All 50 correct case attempts earned full credit; 100 single-field mutations each lost exactly that field’s 5 points. This is author-side testing, not independent reviewer evidence. |
| Content validator | Passed: 25 courses, 401 lessons, 2,396 questions, 1,332 cards and 25 cases; 0 errors or warnings. |
| Candidate report drift, objective-coverage drift, exact-package review-evidence check, Ruff and `git diff --check` | Passed. The register records 80 unresolved candidate gates, 3 unresolved course gates, no reviewer sign-offs and no operator approval. |
| Biochemistry public-package snapshot | 67 files, 857,578 bytes; archive SHA-256 `dc4cd5fce160744516d3e67a533c1796b967b525a5d5548976301a7086f3134a`; manifest SHA-256 `29e7efb0d98213f3138901d78f0cab8f23d0de46711df2590b8b29326d668386`. |

The [review snapshot](BIOCHEMISTRY_REVIEW_SNAPSHOT.md), [hash-pinned evidence register](reviews/biochemistry-review-evidence-0.4.27.json) and [prospective workload-pilot protocol](reviews/biochemistry-workload-pilot-0.4.27.md) identify the current target. No learner workload has been collected. Qualified biochemical and assessment review, accessibility and fairness review, a course grade policy, graded exams/project/labs, physical laboratory work, institutional scope review and operator release approval remain open. Keep the course partial and formative-only until those gates are met.

## Previous increment: Biochemistry 14-week homework-candidate set (0.4.26, 2026-10-11)

Added eight inactive, answer-free homework candidates with synthetic datasets across all 14 proposed weeks. Together they contain 50 cases and 500 proposed points; every response field links to lesson objectives and course outcomes. At that version, the drafts had no protected keys or graders and no live policy. The course remained partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Full cross-course content suite | 2,867 passed, 2 skipped in 340.49 seconds. |
| Focused Biochemistry and assessment-candidate regressions | 53 passed. |
| Content validator | Passed: 25 courses, 401 lessons, 2,396 questions, 1,332 cards and 25 cases; 0 errors or warnings. |
| Biochemistry public-package snapshot | 67 files, 852,925 bytes; archive SHA-256 `4ade7d69dccfb59e83ce92e1b6cd9f6f323de374b8722bd20585f7f1179958c1`; manifest SHA-256 `d20526e68cb5f789f10601cf8a7e0ddeca6a77bb81852ad2a8f7838d4cda3290`. |

## Current increment: Biochemistry inactive midterm review candidate (0.4.23, 2026-10-11)

Added an answer-free ten-case, 100-point midterm review candidate for the proposed first seven weeks. The synthetic kinetic dataset includes replicate control and inhibitor rates; a separate purification table supports recovery and specific-activity analysis. The candidate is not listed in the live assessment manifest and has no key or grader specification. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry course and inactive-candidate regressions | 47 passed. |
| Full cross-course content suite (`uv run --project backend --with jsonschema --with pytest-xdist pytest -n 6 -q tests/content`, with repository root on `PYTHONPATH`) | 2,856 passed, 2 skipped. |
| Candidate audit, including inactive midterm and cumulative-final drafts | Passed; 17 inactive candidate artifacts are inventoried across all courses. |
| Content validator | Passed: 25 courses, 400 lessons, 2,389 questions, 1,328 cards and 25 cases; 0 errors or warnings. |
| Ruff, generated report checks and `git diff --check` | Passed. |
| Biochemistry package snapshot | 41 files, 634,069 bytes; archive SHA-256 `bf618e6ec1df496af28b221270b902a0aa18d4a3694d05dc64622df01dacc3ce`. |

Qualified subject-matter and assessment review, accessibility and fairness review, workload measurement, protected-delivery verification and operator release decisions remain open.

## Current increment: Biochemistry cumulative final candidate and complete lesson map (0.4.22, 2026-10-11)

Added a twelve-case, 120-point cumulative final review candidate as an inactive, answer-free public packet. It is not listed in the live assessment manifest and has no answer key, grader specification or assignment policy. Updated the proposed syllabus to list all 26 lessons by their manifest titles and refreshed the independent numeric recalculation inventory. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Biochemistry and candidate-audit regressions | 45 passed. |
| Full cross-course content suite (`uv run --project backend --with jsonschema --with pytest-xdist pytest -n 6 -q tests/content`, with repository root on `PYTHONPATH`) | 2,854 passed, 2 skipped. |
| Biochemistry numerical practice recalculation | All 76 numeric items are included in the independent recalculation inventory and pass. |
| Backend `ContentRepository` delivery tests | 23 passed, 1 skipped because this Windows host cannot create symlinks; one upstream Starlette/httpx deprecation warning. |
| Content validator | Passed: 25 courses, 400 lessons, 2,389 questions, 1,328 cards and 25 cases; 0 errors or warnings. |
| Candidate audit, Ruff, generated report drift and `git diff --check` | Passed; 16 inactive candidate artifacts are inventoried across all courses. |
| Biochemistry package snapshot | 38 files, 599,315 bytes; archive SHA-256 `9f01ecaa0179ceceb0fd421e17f7a26e4aa004a87e8003c29aaf69361770d19d`. |

Independent biochemical and assessment review, accessibility and fairness review, measured workload, protected-delivery verification and release policy remain open.

## Current increment: Biochemistry fed-to-fasting capstone case (0.4.21, 2026-10-11)

Expanded the existing week-14 ungraded case with a synthetic fed-like versus mobilization-like liver index table. The self-check integrates glycogen, gluconeogenesis, glycerol delivery, fatty-acid oxidation, malonyl-CoA/CPT1 control, ketone export and urea output. The dataset explicitly uses arbitrary relative indices and is not mass-balanced; six checklist criteria remain ungraded.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including case objective mapping, ungraded rubric, synthetic-data limits, source permissions, existing lessons and package snapshot | 34 passed. |
| Backend `ContentRepository` delivery regressions for weeks 2, 4, 8, 9, 10, 11, 12, 13 and 14 | 13 passed. |
| Real authored-key grader checks for current fatty-acid and neutral-lipid practice items | 28 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 400 lessons, 2,389 questions, 1,328 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Current increment: Biochemistry neutral-lipid storage and mobilization (0.4.20, 2026-10-11)

Extended the week-13 fatty-acid lesson with glycerol-3-phosphate acylation to TAG, hepatic VLDL export, adipose ATGL-HSL-MGL lipolysis, glycerol return to liver and a direct distinction from capillary LPL. Seven public formative items and four retrieval cards add two objectives. KEGG, Reactome and Endotext are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including TAG product/acyl-CoA accounting, lipase roles, source permissions, outcome mapping, existing lessons and package snapshot | 34 passed. |
| Backend `ContentRepository` delivery regressions for weeks 2, 4, 8, 9, 10, 11, 12, 13 and 14 | 13 passed. |
| Real authored-key grader checks for the fourteen fatty-acid and neutral-lipid items | 28 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 400 lessons, 2,389 questions, 1,328 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Current increment: Biochemistry nucleotide biosynthesis and salvage (0.4.19, 2026-10-11)

Added a week-8 lesson contrasting purine assembly on PRPP with pyrimidine ring-first synthesis, then linking salvage, ribonucleotide reduction and folate-dependent dTMP formation. Seven public formative items include explicit reciprocal GTP/ATP accounting at the IMP branch point; four retrieval cards map two objectives to metabolism and regulation outcomes. KEGG and Reactome are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including IMP branch energy, pathway order, salvage, source permissions, outcome mapping, existing lessons and package snapshot | 33 passed. |
| Backend `ContentRepository` delivery regressions for weeks 2, 4, 8, 9, 10, 11, 12, 13 and 14 | 13 passed. |
| Real authored-key grader checks for the seven nucleotide items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 400 lessons, 2,382 questions, 1,324 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Current increment: Biochemistry cholesterol and lipoprotein metabolism (0.4.18, 2026-10-11)

Added a week-12 lesson on cholesterol biosynthesis, ER sterol feedback through SREBP2, the statin/HMG-CoA-reductase mechanism as a pathway example, and apolipoprotein-specific dietary and liver-derived transport. Seven public formative questions and four retrieval cards map two objectives to metabolism and regulation outcomes. KEGG, Reactome and Endotext are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including sterol-feedback direction, apolipoprotein roles, source permissions, outcome mapping, existing lessons and package snapshot | 31 passed. |
| Backend `ContentRepository` delivery regressions for weeks 2, 4, 9, 10, 11, 12, 13 and 14 | 12 passed. |
| Real authored-key grader checks for the seven cholesterol/lipoprotein items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 399 lessons, 2,375 questions, 1,320 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Current increment: Biochemistry fatty-acid synthesis (0.4.17, 2026-10-11)

Added a week-13 lesson on cytosolic acetyl-CoA supply, palmitate carbon/ATP/NADPH accounting, ACC regulation, and malonyl-CoA inhibition of CPT1. Seven public formative questions and four retrieval cards map two new objectives to metabolism and pathway-regulation outcomes. KEGG and Reactome are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including independent fatty-acid synthesis ledger, source permissions, outcome mapping, existing lessons and package snapshot | 29 passed. |
| Backend `ContentRepository` delivery regressions for weeks 2, 4, 9, 10, 11, 12, 13 and 14 | 11 passed. |
| Real authored-key grader checks for the seven fatty-acid synthesis items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 398 lessons, 2,368 questions, 1,316 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Current increment: Biochemistry ketone-body synthesis and use (0.4.16, 2026-10-11)

Added a week-11 lesson connecting hepatic ketogenesis, mitochondrial redox, gluconeogenic demand, and extrahepatic SCOT-dependent ketolysis. Seven public formative questions and four retrieval cards map two objectives to metabolism and regulation outcomes. Reactome, NCBI and a review are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including ketolysis stoichiometry, tissue/source checks, outcome mapping, existing lessons and package snapshot | 27 passed. |
| Backend `ContentRepository` delivery regressions for weeks 2, 4, 9, 10, 11, 12, 13 and 14 | 10 passed. |
| Real authored-key grader checks for the seven ketone-body items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 397 lessons, 2,361 questions, 1,312 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Previous increment: Biochemistry amino-acid carbon skeletons (0.4.15, 2026-10-11)

Added a week-2 lesson on amino-acid carbon-skeleton entry points, glucogenic/ketogenic/mixed fates, and separating nitrogen transfer from carbon metabolism. Seven public formative questions and four retrieval cards include a multi-select entry-point item and map two new objectives to metabolism and regulation outcomes. NCBI Bookshelf and a review are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including amino-acid carbon-fate checks, source permissions, outcome mapping, existing lessons and package snapshot | 25 passed. |
| Backend `ContentRepository` delivery regressions for weeks 2, 4, 9, 10, 11, 12, 13 and 14 | 9 passed. |
| Real authored-key grader checks for the seven amino-acid carbon items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 396 lessons, 2,354 questions, 1,308 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Previous increment: Biochemistry amino-nitrogen and urea cycle (0.4.14, 2026-10-11)

Added a week-2 lesson on amino-nitrogen transfer and urea-cycle atom, compartment and energy accounting, including the three-ATP/four-high-energy-bond distinction, CPS1 activation and fumarate connection. Seven public formative questions and four retrieval cards map two new objectives to metabolism and regulation outcomes. KEGG, Reactome and NCBI are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including urea-cycle atom/energy checks, source permissions, outcome mapping, existing lessons and package snapshot | 23 passed. |
| Backend `ContentRepository` delivery regressions for weeks 2, 4, 9, 10, 11, 12, 13 and 14 | 8 passed. |
| Real authored-key grader checks for the seven urea-cycle items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 395 lessons, 2,347 questions, 1,304 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Previous increment: Biochemistry fatty-acid beta-oxidation (0.4.13, 2026-10-11)

Added a week-11 lesson on mitochondrial beta-oxidation, carnitine transport, palmitate cycle and carrier accounting, activation cost, and an ATP estimate under explicit P/O assumptions. Seven public formative questions and four retrieval cards map two new objectives to metabolism and bioenergetics outcomes. KEGG, Reactome and a review are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including palmitate cycle/carrier/ATP recalculation, source permissions, outcome mapping, existing lessons and package snapshot | 21 passed. |
| Backend `ContentRepository` delivery regressions for weeks 4, 9, 10, 11, 12, 13 and 14 | 7 passed. |
| Real authored-key grader checks for the seven fatty-acid oxidation items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 394 lessons, 2,340 questions, 1,300 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Previous increment: Biochemistry pentose phosphate pathway (0.4.12, 2026-10-11)

Added a week-13 lesson on oxidative-branch NADPH and CO2 accounting, reversible nonoxidative sugar rearrangements, pentose demand and NADP-sensitive flux. Seven public formative questions and four retrieval cards map two new objectives to metabolism and pathway-regulation outcomes. KEGG and Reactome pathway entries are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including PPP redox/carbon recalculation, source permissions, outcome mapping, existing lessons and package snapshot | 19 passed. |
| Backend `ContentRepository` delivery regressions for weeks 4, 9, 10, 12, 13 and 14 | 6 passed. |
| Real authored-key grader checks for the seven PPP items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 393 lessons, 2,333 questions, 1,296 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Previous increment: Biochemistry glycogen storage and mobilization (0.4.11, 2026-10-11)

Added a week-12 lesson on glycogen synthesis and breakdown, UDP-glucose activation cost, muscle ATP accounting, reciprocal phosphorylation control, and liver-versus-muscle roles. Seven public formative questions and four retrieval cards map two new objectives to metabolism and pathway-regulation outcomes. KEGG, Reactome and a human glycogen-metabolism review are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, including glycogen storage and mobilization recalculations, sources, outcome mapping, existing lessons and package snapshot | 17 passed. |
| Backend `ContentRepository` delivery regressions for weeks 4, 9, 10, 12 and 14 | 5 passed. |
| Real authored-key grader checks for the seven glycogen items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 392 lessons, 2,326 questions, 1,292 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Previous increment: Biochemistry gluconeogenesis lesson and practice (0.4.10, 2026-10-11)

Added a week-10 lesson on the three gluconeogenic bypasses, energy inputs from pyruvate, reciprocal liver regulation by F2,6BP and carbon-source limits. Seven public formative questions and four retrieval cards map two new objectives to the existing metabolism and regulation outcomes. KEGG, Reactome and a primary F2,6BP study are linked only. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regression suite, including independent energy-ledger checks, source permissions, outcome mapping, existing lessons and package snapshot | 15 passed. |
| Backend `ContentRepository` delivery regressions for weeks 4, 9, 10 and 14 | 4 passed. |
| Real authored-key grader checks for the seven gluconeogenesis items | 14 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 391 lessons, 2,319 questions, 1,288 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Previous increment: Biochemistry citric-acid-cycle lesson and practice (0.4.9, 2026-10-11)

Added a week-9 lesson that tracks one citric-acid-cycle turn, separates pyruvate dehydrogenase from the cycle, accounts for glucose-level carbon and carrier outputs, and explains intermediate withdrawal, anaplerosis and flux evidence. Seven public questions and four retrieval cards map to existing metabolism and regulation outcomes. KEGG and Reactome pathway records are linked only; the examples are original bookkeeping models.

| Actual command/check | Result |
| --- | --- |
| Biochemistry package regressions, including TCA accounting, purification recalculation, case studio, outcomes and package snapshot | 13 passed. |
| Backend `ContentRepository` delivery regressions for weeks 4, 9 and 14 | 3 passed. |
| Real authored-key grader checks for the new purification and TCA items | 26 passed: each correct answer earns full credit and each deliberately wrong answer earns none. |
| Content validator | Passed: 25 courses, 390 lessons, 2,312 questions, 1,284 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff, generated report drift checks and `git diff --check` | Passed. |
| Public package snapshot | Archive and manifest digests match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified biochemical review remain open.

## Previous increment: Biochemistry protein-purification lesson and practice (0.4.8, 2026-10-11)

Added a substantial week-4 reading on charge-, size- and affinity-based separation, purification-table calculations, recovery versus enrichment, and the limits of specific activity. Six public practice items and four retrieval cards connect two new objectives to a fifth course outcome. The example fractions are synthetic; three Cytiva technical handbooks are cited by link only. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry content regressions, including independent purification-table recalculation, case studio, outcome mapping and project calculations | 11 passed. |
| Backend `ContentRepository` delivery regressions for weeks 4 and 14 | 2 passed; confirms both readings, linked practice and ungraded case delivery. |
| Content validator | Passed: 25 courses, 389 lessons, 2,305 questions, 1,280 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff on changed tests | Passed. |
| Course package snapshot and generated coverage/candidate reports | Digest and report checks passed; see [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

No textbook or handbook text, tables, figures or data were copied. Qualified biochemical, accessibility, workload and assessment review remain open.

## Previous increment: Biochemistry week-14 case studio (0.4.7, 2026-10-11)

The week-14 metabolic case now appears as an explicit learner-facing self-check in the delivered reading. Its case record and scheduled activity map to the three metabolic-perturbation objectives, and the empty checklist now calls for observable calculation, tracer/redox interpretation, and competing-hypothesis predictions. The worksheet records no response, has zero points, remains formative-only, and creates no graded assessment or answer key. The public package snapshot was recalculated.

| Actual command/check | Result |
| --- | --- |
| Biochemistry content regressions, including case mapping, checklist, course snapshot, outcome mapping and project recalculation | 9 passed. |
| Backend `ContentRepository` week-14 delivery regression | 1 passed; the scheduled case is self-assessment and the lesson DTO contains the worksheet. |
| Content validator | Passed: 25 courses, 388 lessons, 2,299 questions, 1,276 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Public package snapshot | Course package digest, manifest digest and archive inventory match [BIOCHEMISTRY_REVIEW_SNAPSHOT.md](BIOCHEMISTRY_REVIEW_SNAPSHOT.md). |

The course remains partial, unreviewed and formative-only; workload and qualified instructor review remain open.

## Current increment: machine-readable public numeric-key recalculations (0.54.0, 2026-10-11)

Added a report that recomputes all 21 numeric items in the public Cell Biology formative bank from stated values, checks each calculation against an anchored prompt and authored tolerance, and pins the output to the public package digest. The review handoff links the report and CI checks it. The inventory reads no inactive candidate answer source and does not satisfy independent recalculation or review gates.

| Actual command/check | Result |
| --- | --- |
| Cell Biology suite, including numeric evidence, candidate, table, design-studio, archive and review regressions | 139 passed. |
| Backend content-repository delivery regression | 10 passed, 1 platform-dependent symlink check skipped; verifies the week-14 studio schedule entry and readable ungraded lesson DTO. |
| Public numeric-key evidence CLI | 21/21 checks passed for 0.54.0; inactive candidate answer sources not read; release unauthorized. |
| Public table reconciliation CLI | 114/114 checks passed across 12 items. |
| Content validator | Passed: 25 courses, 388 lessons, 2,299 questions, 1,276 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Ruff and CI workflow YAML parse | Passed. |

The report is [cell-biology-public-numeric-recalculation.json](reviews/cell-biology-public-numeric-recalculation.json). The course remains partial, unreviewed and formative-only.

## Previous increment: response audit lists formal ungraded writing resources (0.54.0, 2026-10-11)

Extended the response-format audit to separate public question-bank formats from formal course lessons that offer ungraded written responses. The report now lists the early chemistry rehearsal and the week-14 design studio with their authored objective links. It does not evaluate response quality, learner work, or human scoring.

| Actual command/check | Result |
| --- | --- |
| Cell Biology regression suite, including response-audit and new design-studio tests | 137 passed. |
| Response-audit drift check | Passed: 166 public practice items plus 2 ungraded writing lessons linked to 8 distinct objectives. |
| Ruff | Passed. |

The extra inventory documents available writing practice; it does not establish learner performance. The course remains partial, unreviewed, and formative-only.

## Previous increment: Cell Biology written-design studio and review-package refresh (0.54.0, 2026-10-11)

Expanded the optional week-14 design brief into a learner-visible course lesson with self-assessed written prompts mapped to all five create-labeled objectives. Four new scenarios cover variant controls, signaling feedback, matrix mechanics, and cell-state inference; the existing lineage-to-function design prompt covers the fifth. The lesson remains uncollected and ungraded. No grading policy or maturity label changed.

| Actual command/check | Result |
| --- | --- |
| Cell Biology design-studio, integrity, review-handoff, review-evidence, public-table-evidence and response-audit regressions | 24 passed at the time of this increment. |
| Cell Biology manifest/content regression subset | 13 passed, 89 deselected. |
| Content validator | Passed: 25 courses, 388 lessons, 2,299 questions, 1,276 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, objective-coverage and response-format drift checks | Passed. |
| Public-data recalculation artifact | Current at 0.54.0; 12 items, 114/114 checks; protected assessment sources not read. |
| Public package digest | 0.54.0; archive SHA-256 `de3d1a96c782a1c43937102ef59efbcb3a0c9835e734793e6cbd4f3269a490f4`; manifest SHA-256 `dbbe621e036b27229a283d168169bb1106cf633b117fde18c8ba52ec44f4bcb0`; 122 files, 2,112,056 bytes. |
| Review-evidence index | 15 inactive artifacts; 142 candidate-gate instances and 3 course-level gates unresolved; 0 review records; release unauthorized. |
| Ruff | Passed. |

The public-package digest and review scaffold now target 0.54.0. The course remains partial, unreviewed and formative-only; the studio does not establish learner design performance.

## Current increment: machine-readable Cell Biology public-data recalculation artifact (0.53.0, 2026-10-11)

Added a deterministic JSON report for the 114 summary-table calculations across 12 public formative items. Every row records the public source and replicate values, computed result, authored answer, tolerance and result, and the report binds to the current course archive plus source-file hashes. CI checks the report against its inputs. It covers formative public data only and does not sign off a protected candidate or satisfy independent review.

| Actual command/check | Result |
| --- | --- |
| New artifact, public table-key and review-evidence regressions | 10 passed. |
| Public table evidence CLI | Current Cell Biology 0.53.0; 12 table items; 114/114 calculations reconcile. Protected assessment sources not read; release not authorized. |
| CI workflow YAML parse with the repository's Prettier installation | Passed. |

The report is [cell-biology-public-table-recalculation.json](reviews/cell-biology-public-table-recalculation.json). The course remains partial and formative-only.

## Previous increment: Cell Biology review-evidence index and platform gate (0.53.0, 2026-10-11)

Added a read-only reviewer-evidence index bound to the current Cell Biology public archive and all 15 inactive candidate artifacts. It checks public evidence file hashes, rejects stale package/candidate inventories and incomplete signed records, separates course-level workload from candidate gates, and keeps operator release separate. It does not read protected answer sources, authenticate reviewer qualifications, modify course state or authorize release.

| Actual command/check | Result |
| --- | --- |
| Cell Biology review-evidence, handoff, candidate, integrity, assembled-assessment and public-table regressions | 130 passed. |
| Review-evidence CLI audit | Current package 0.53.0; 15 candidate artifacts; 142 candidate-gate instances and 3 course-level gates unresolved; 0 review records; no operator decision; release remains unauthorized. |
| Backend suite (`PYTHONUTF8=1 uv run --project backend pytest -q backend/tests`) | 4,890 passed, 3 skipped; one upstream Starlette/httpx deprecation warning. |
| Ruff and Python compilation for review-evidence tools | Passed. |

The ledger is a record validator, not reviewer authentication or a course-completion decision. The public package remains partial and formative-only.

## Current increment: Cell Biology review handoff for 0.53.0 (2026-10-11)

Prepared a human-review handoff for the 15 inactive candidate artifacts representing 14 intended assessment components. The packet binds to the reproducible public package digest, identifies the external protected answer boundary, and lists independent subject, numerical, assessment, accessibility, workload, human-scoring, archive and operator gates that remain unresolved.

| Actual command/check | Result |
| --- | --- |
| Cell Biology candidate, integrity, assembled-assessment, public-table and review-handoff tests | 123 passed. |
| Public package digest | Passed: version 0.53.0; archive SHA-256 `56398f41805dccae2ed08ef7607c8c1261a25062b30faa45cf53c62728d5b7d5`; manifest SHA-256 `04bb0d6114545faf36ba2a081ea256c311eb349eda921bfd07a699c8eb1b3ef3`; 122 files; 2,102,096 bytes. |
| Cell Biology candidate audit and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The handoff does not sign off or activate any candidate. The package remains partial, unreviewed and formative-only; the protected key package was not opened.

## Current increment: review handoff for Physics: Mechanics 0.4.5 (2026-10-11)

Pinned the Mechanics package and prepared a handoff for the inactive equal-RCF rotor trade-off portfolio. The synthetic comparison recomputes angular speed, disk inertia, stored energy and imbalance force, and explicitly supplies no real-device operating or safety guidance.

| Actual command/check | Result |
| --- | --- |
| Mechanics regressions, rotor recalculation and snapshot identity | 106 passed. |
| Public package digest | Passed: version 0.4.5; archive SHA-256 `383e32433d68e14b49e0b48727dbf24e19a9853ef0838b7503b96df6f29bc02c`; manifest SHA-256 `934c84082657e8afea63a43a00af44534c1b6b0d5e1cf0f6d57179e61dabff82`; 23 files; 306,622 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded, fictional and unreviewed; the package remains partial.

## Current increment: review handoff for Human Physiology 0.4.6 (2026-10-11)

Pinned the Physiology package and prepared a handoff for the inactive renal-clearance ledger. The synthetic dataset reconciles a reference clearance with filtered load, excretion, net tubular transport and an idealized glucose transport maximum.

| Actual command/check | Result |
| --- | --- |
| Physiology regressions, ledger recalculation and snapshot identity | 8 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `c795d6743ee706c75646da3427171062f662c4674ff564db585982f7613cabcb`; manifest SHA-256 `c93b9beb80eeb706f01579db849f562cbb8b0d8a8e0cfd4e34149edb53bff092`; 24 files; 295,390 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

All quantities are fictional teaching data; the draft is not a clinical protocol. The course remains partial, unreviewed and formative-only.

## Current increment: review handoff for Geroscience 0.5.7 (2026-10-11)

Pinned the Geroscience package and prepared a handoff for the inactive synthetic surrogate-endpoint dossier. Its three fictional comparisons distinguish age association, marker response, tissue function and survival without claiming human-aging or real-intervention effects.

| Actual command/check | Result |
| --- | --- |
| Geroscience regressions, dossier interval recomputation and snapshot identity | 488 passed. |
| Public package digest | Passed: version 0.5.7; archive SHA-256 `712fd4709574cbd7688869053bff710143bc34181f22b2d5ef737853d549c746`; manifest SHA-256 `2fb24344db1ec339dde1c78a9d21472e578d9804b0ad5e398e125e304c6536d3`; 26 files; 340,325 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards and 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |
| Repository-wide content tests | 2,779 passed and 2 skipped; five stale version assertions were corrected, and the five affected tests passed on targeted rerun. |

The dossier remains inactive, ungraded and synthetic. The package remains partial, unreviewed and formative-only; no claim is made about real interventions or human aging.

## Current increment: review handoff for Cellular Biomechanics 0.3.6 (2026-10-10)

## Cell Biology 0.61.0 syllabus workload-label alignment (2026-10-11)

Marked the two remaining 2–3 hour lab-duration descriptions in the syllabus as unvalidated author estimates, matching the labels already used in all eight homework and three lab packet headers. Updated the current package labels and three inactive lab candidates' public prerequisite hashes, then regenerated current and versioned review artifacts. Added regression coverage that recomputes the displayed summary examples in all three virtual labs from their linked CSVs. The course remains partial, unreviewed, and formative-only; no learner time was measured, no workload target was approved, and no review or release gate was closed.

| Actual command/check | Result |
| --- | --- |
| Package, review-handoff, and content-repository regressions | 39 passed, 1 skipped (Windows symlink support). |
| Homework and virtual-lab source-to-example regressions | Recompute all eight homework summary tables and selected derivations plus the displayed summary examples for all three labs from their linked CSVs; author consistency only. |
| Current-version content assertions | 6 passed; 95 unrelated content-validation tests deselected. |
| Content validator | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors and 0 explicit limitation/depth warnings. |
| Candidate/evidence, objective-coverage, response-mode, numeric, and table drift checks | Passed; numeric 21/21, public table 114/114; 142 candidate gates, four course-level gates, zero reviewer sign-offs and no release authorization. |
| Public package digest | Version 0.61.0; 122 files; 2,118,140 bytes; archive SHA-256 `63ce2392d5586830e414c4e214af42de73adef03a9f1276dbbd58024a4a9b50a`; manifest SHA-256 `75449a3d7439567f29afd56bb88e81e21340d7bd68eaa5d469dc4d1bf24de173`. |
| Ruff and `git diff --check` | Passed. |

The estimates remain unvalidated. External review, measured workload, and operator release decisions remain open.

## Cell Biology 0.60.0 unvalidated workload labels (2026-10-11)

Marked the suggested 2–3 hour values in all eight homework and three lab packets as unvalidated author estimates. This clarifies their status without presenting them as measured learner workload or approved time targets. Split two lab metadata lines for consistent packet formatting and refreshed those candidates' public prerequisite hashes. Regenerated the current and versioned package snapshot, audit reports, evidence index, and prospective workload protocol. The course remains partial, unreviewed, and formative-only; no learners were recruited, no workload data or targets were approved, and no review or release gate was closed.

| Actual command/check | Result |
| --- | --- |
| Package, review-handoff, and content-repository regressions | 38 passed, 1 skipped (Windows symlink support). |
| Current-version content assertions | 6 passed; 95 unrelated content-validation tests deselected. |
| Content validator | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors and 0 explicit limitation/depth warnings. |
| Candidate/evidence, objective-coverage, response-mode, numeric, and table drift checks | Passed; numeric 21/21, public table 114/114; 142 candidate gates, four course-level gates, zero reviewer sign-offs and no release authorization. |
| Public package digest | Version 0.60.0; 122 files; 2,117,340 bytes; archive SHA-256 `bead4874f7ebdd104f8a7c2fcef1c60a55d06d5d5357224d8ad7841500c95b3f`; manifest SHA-256 `7e4092a09591ab50fc19e659df5f5cb8d676bd95defb8e936b9e2a1c97153ba5`. |
| Ruff and `git diff --check` | Passed. |

The estimates remain explicitly unvalidated. External review, measured workload, and operator release decisions remain open.

## Cell Biology 0.59.0 packet-version alignment (2026-10-11)

Aligned the embedded course-package labels in the eight homework packets and three lab packets with the 0.59.0 manifest. Refreshed the matching public prerequisite hashes on three inactive lab candidates; candidate questions and protected answer-source digests remain unchanged. Regenerated current and versioned digest-bound review artifacts. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Package, review-handoff, and content-repository regressions | 38 passed, 1 skipped (Windows symlink support). |
| Homework worked-example source regression | Recomputes all eight learner-facing summary tables and key worked derivations from their linked CSVs; this is author-side consistency evidence only. |
| Current-version assertions in content-validation tests | 6 passed; 95 unrelated tests deselected. |
| Content validator | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; 0 errors and 0 explicit limitation/depth warnings. |
| Candidate/evidence and public numeric/table drift checks | Passed; 142 candidate gates, four course-level gates, zero reviewer sign-offs, no release authorization; numeric 21/21 and table 114/114. |
| Public package digest | Version 0.59.0; 122 files; 2,116,301 bytes; archive SHA-256 `78fbdce816d2f68c264a306ee2e9e20f8604a6190a42e4c9b07756e55c98341e`; manifest SHA-256 `b9857af6e169b0e31ae1153c3770e64cc7f9c150b3faae131d444d9b9e4e6e5b`. |
| Ruff and `git diff --check` | Passed. |

Pinned the Cellular Biomechanics package and prepared a handoff for standard-linear-solid relaxation, frequency-dependent moduli, loss and energy accounting. The synthetic model boundary is explicit, and a snapshot regression verifies archive identity.

| Actual command/check | Result |
| --- | --- |
| Cellular Biomechanics regressions, project recalculations and snapshot identity | 8 passed. |
| Public package digest | Passed: version 0.3.6; archive SHA-256 `ef6f33137f273fe065ab5c3dbea6e202a0891c4de7249fcb8643e88786d361f9`; manifest SHA-256 `2d99d4a6f423bbdf3d054cb7757ea388e07180e0bd2497d36df92c042b48c4f3`; 23 files; 311,372 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The project is inactive, ungraded, synthetic and unreviewed.

## Prior increment: inactive viscoelastic material-selection portfolio for Cellular Biomechanics 0.3.6 (2026-10-10)

Added a paper-only project draft comparing three fictional standard-linear-solid candidates across step relaxation, angular frequency, loss tangent and cycle dissipation. It complements the existing stiffness/ligand virtual lab without predicting real material properties or cell behavior.

| Actual command/check | Result |
| --- | --- |
| Cellular Biomechanics regressions and project recalculations | 7 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed; all candidates and thresholds are synthetic teaching constructs.

## Current increment: review handoff for General Chemistry II 0.4.6 (2026-10-10)

Pinned the General Chemistry II package and prepared a handoff for half-reaction balance, electrochemical thermodynamics, Nernst sign and Faraday amount accounting. The fictional-symbol boundary is explicit, and a snapshot regression verifies archive identity.

| Actual command/check | Result |
| --- | --- |
| General Chemistry II regressions, project recalculations and snapshot identity | 111 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `58445a0eb4b603ec7f2a41c0ce23cf936ac592c8f96053b201c6a27403f19502`; manifest SHA-256 `96d91af0018ca35d035f04801db1dd9ac38f882dc8de9559b6465c19783e7f4e`; 23 files; 319,037 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The project is inactive, ungraded, synthetic and unreviewed.

## Prior increment: inactive fictional redox-cell portfolio for General Chemistry II 0.4.6 (2026-10-10)

Added a paper-only electrochemistry draft linking balanced fictional half-reactions, standard cell potential, `ΔG°`, `K`, a Nernst correction and Faraday-law amount accounting. It complements the existing relaxation lab without describing a real cell or experiment.

| Actual command/check | Result |
| --- | --- |
| General Chemistry II regressions and project recalculations | 110 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed; all symbols, potentials and activities are fictional teaching constructs.

## Current increment: review handoff for General Chemistry I 0.4.6 (2026-10-10)

Pinned the General Chemistry I package and prepared a handoff for stoichiometry, activity conventions, equilibrium-root selection and enthalpy sign. The new project's fictional species boundary is explicit, and a snapshot regression verifies archive identity.

| Actual command/check | Result |
| --- | --- |
| General Chemistry I regressions, project calculations and snapshot identity | 88 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `883481ab7b2966673646cbf8dd5370d73a04c79ae2d2299af290198305004945`; manifest SHA-256 `1d5a0100e0e30edc3cec7835379f703e795dbd211d57268a5cf05c89ed75ad62`; 22 files; 295,493 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The project is inactive, ungraded, synthetic and unreviewed.

## Prior increment: inactive abstract equilibrium portfolio for General Chemistry I 0.4.6 (2026-10-10)

Added a fictional-gas equilibrium portfolio connecting reaction extent, conserved-unit accounting, `Q`/`K`, an admissible quadratic root and constant-temperature reaction enthalpy. It is distinct from the buffer calibration lab and does not define a real chemical system.

| Actual command/check | Result |
| --- | --- |
| General Chemistry I course regressions and project recalculations | 87 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed; all species and inputs are fictional teaching constructs.

## Prior increment: review handoff for Transport 0.4.5 (2026-10-10)

Pinned the Transport package and prepared a handoff for the thermal boundary-value draft, heat-balance signs, Biot check and quadrature cross-check. The snapshot regression verifies deterministic archive identity.

| Actual command/check | Result |
| --- | --- |
| Transport regressions, project recalculations and snapshot identity | 12 passed. |
| Public package digest | Passed: version 0.4.5; archive SHA-256 `d0d1db4715f29b972070640ea13a920f69398efb868257c40eb966d6b2245a2c`; manifest SHA-256 `78e8a0ece36bd23cbc7626fff4f23879b3efafad790a4bb26200deeee0219ae8`; 22 files; 293,597 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The thermal project is inactive, ungraded and unreviewed; it gives no real process guidance.

## Prior increment: inactive heat-generation slab project for Transport 0.4.5 (2026-10-10)

Added a steady thermal boundary-value draft with symmetric and convective boundaries, an internal-generation balance, a Biot screening calculation, and an exact-vs-Simpson average-temperature check. It complements the oxygen-profile lab with no real process guidance.

| Actual command/check | Result |
| --- | --- |
| Transport regressions and project recalculations | 11 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed; workload and accessibility remain open.

## Prior increment: review handoff for Statics & Materials 0.4.5 (2026-10-10)

Pinned the Statics & Materials package and prepared a handoff covering beam assumptions, unit conversions, the two independent teaching limits and the non-design boundary. The snapshot regression compares package hashes and inventory with the deterministic builder.

| Actual command/check | Result |
| --- | --- |
| Statics & Materials regressions, project recalculations and snapshot identity | 11 passed. |
| Public package digest | Passed: version 0.4.5; archive SHA-256 `4dfb1c9b2e83ffbccad726cd2c84450aca09a52bf7838e1649e123d06b39c966`; manifest SHA-256 `68b89c0f6ed8e40bd0e869b6498438c6d97e45bc3348708eb78b2e705d8e7c88`; 23 files; 307,953 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The snapshot proves identity only. The beam exercise is inactive, synthetic and unreviewed; it is not a design or safety basis.

## Prior increment: inactive beam strength/stiffness portfolio for Statics & Materials 0.4.5 (2026-10-10)

Added a synthetic simply supported beam comparison with equilibrium, bending stress, elastic deflection and separate classroom strength/stiffness limits. It complements the fatigue-life lab and explicitly disclaims real structural design or safety use.

| Actual command/check | Result |
| --- | --- |
| Statics & Materials regressions and project recalculations | 10 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project is inactive, ungraded and unreviewed; its values are synthetic teaching constructs.

## Prior increment: review handoff for Biomaterials 0.3.6 (2026-10-10)

Pinned the Biomaterials package and prepared a handoff for the course's degradation and mechanics keys, synthetic candidate thresholds, and the inactive property-comparison draft. The snapshot regression checks public archive identity.

| Actual command/check | Result |
| --- | --- |
| Biomaterials regressions, project recalculations and snapshot identity | 8 passed. |
| Public package digest | Passed: version 0.3.6; archive SHA-256 `591ea17bd735553b47c94d68595deb26302fa489698e790007779423f97556bb`; manifest SHA-256 `47b90dc15e95ec6c09b14c3e055e94d4649d91630ce5cee2b9d4ddef82a454a5`; 23 files; 303,951 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The snapshot proves identity only. The candidate comparison is synthetic, inactive and unreviewed; it gives no real material recommendation.

## Prior increment: inactive scaffold-property portfolio for Biomaterials 0.3.6 (2026-10-10)

Added a synthetic three-candidate comparison across porosity, permeability and time-dependent modulus. The draft uses explicit unweighted thresholds at 42 and 56 days, exposes the time-horizon tradeoff, and makes no material or implant recommendation.

| Actual command/check | Result |
| --- | --- |
| Biomaterials course regressions and project recalculations | 7 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project is inactive, ungraded and unreviewed; the course remains partial.

## Prior increment: review handoff for Signals & Control 0.4.5 (2026-10-10)

Pinned the Signals & Control package and prepared a handoff covering sampling/filtering conventions, phase margin, saturated PI updates, sampled-plant arithmetic and the inactive project. The snapshot regression checks the exact public archive identity.

| Actual command/check | Result |
| --- | --- |
| Signals & Control regressions, project recalculations and snapshot identity | 11 passed. |
| Public package digest | Passed: version 0.4.5; archive SHA-256 `d7936a157d864b2a1faf0bd8c26ec64f504b0a92f1bb9d3f64ee3a40d1dc3339`; manifest SHA-256 `bec714bb65340fe754d8664524e1a8793f034e87699eac65c782b622ea3d5ff1`; 22 files; 312,047 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The hash establishes package identity only. The project is inactive, ungraded and unreviewed; it does not authorize real-device use.

## Prior increment: inactive sampled-loop project for Signals & Control 0.4.5 (2026-10-10)

Added a calculation-only project covering pre-sampling aliasing/filtering, sample-period selection, hold phase, a clamped discrete PI update and the exact sampled-plant recurrence. It is distinct from the step-identification lab and the filter-retuning case, and is not device guidance.

| Actual command/check | Result |
| --- | --- |
| Signals & Control regressions and project recalculations | 10 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed; all modeled values are synthetic.

## Prior increment: review handoff for Bioreactors 0.4.6 (2026-10-10)

Pinned the Bioreactors public package and prepared a handoff covering growth/mass-balance work, oxygen-transfer conventions, the transient project and its boundary from the existing `kLa` lab. A regression verifies the snapshot identity.

| Actual command/check | Result |
| --- | --- |
| Bioreactors growth/project recalculations and snapshot identity | 8 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `6a43ececc873fbce92ad703917e40eb8381e7493dc562fcd3cd2317fbceb37b1`; manifest SHA-256 `340a9f0840148436d539888eb31f383beeab1b30d1e7442f0c0cea8854ca7f41`; 22 files; 285,689 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The snapshot confirms package identity only. The paper project is inactive, ungraded and unreviewed; workload and accessibility remain open.

## Prior increment: inactive oxygen-capacity portfolio for Bioreactors 0.4.6 (2026-10-10)

Added a normalized transient oxygen-demand project that derives a deficit solution and compares a quasi-steady capacity threshold with the actual state crossing. The paper draft supplements the existing gassing-out `kLa` lab without specifying a real vessel or process.

| Actual command/check | Result |
| --- | --- |
| Bioreactors growth and project recalculation regressions | 7 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The portfolio is inactive, ungraded and unreviewed; the course remains partial.

## Prior increment: review handoff for Differential Equations 0.3.7 (2026-10-10)

Pinned the Differential Equations package and prepared a handoff for coupled-system math, numerical stability/positivity and the inactive stiff-system project. The snapshot regression verifies the public archive and manifest identity.

| Actual command/check | Result |
| --- | --- |
| Differential Equations regressions, project recalculations and snapshot identity | 8 passed. |
| Public package digest | Passed: version 0.3.7; archive SHA-256 `bf417ad3d9dfccc120a50e32b98ceaa40759784a374b589ea2ffebe699efe5c1`; manifest SHA-256 `3d9807190791a7e1569f7b330ed66acedb492aadcd758da0718efae2152baeb1`; 22 files; 301,142 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The hash proves identity only. The project is inactive, ungraded and unreviewed; the package remains partial.

## Prior increment: inactive stiff-system project for Differential Equations 0.3.7 (2026-10-10)

Added a paper-only coupled-system project with an exact solution, eigenvalue stability and positivity bounds, and explicit-versus-implicit Euler comparisons. It extends the existing scalar decay lab with a distinct stiff-system case and makes no claims about real systems.

| Actual command/check | Result |
| --- | --- |
| Differential Equations regressions and project recalculations | 7 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The draft remains inactive, ungraded and unreviewed; its normalized system is synthetic.

## Prior increment: review handoff for Calculus II 0.4.6 (2026-10-10)

Pinned the Calculus II package and prepared a handoff covering the existing force lab, series and integration keys, and the inactive exponential-tail portfolio. The snapshot regression checks the archive and manifest hashes against the deterministic public-package builder.

| Actual command/check | Result |
| --- | --- |
| Calculus II regressions, project recalculations and snapshot identity | 90 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `71e7436dacd4aa3eec4576408b77fa9f04ade1a5095f34601d00a1acf4b5c6fb`; manifest SHA-256 `7bdc7bbe1c5666537ca6f345c1b57641bd95ab786c0a5229e5f3a5fbc682d308`; 22 files; 266,250 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The snapshot establishes package identity only. The project remains inactive, ungraded and unreviewed; workload, accessibility and qualified review remain open.

## Prior increment: inactive exponential-tail portfolio for Calculus II 0.4.6 (2026-10-10)

Added a paper-only draft using an improper-integral limit, tolerance-based tail cutoff, degree-four Maclaurin approximation and integrated Lagrange remainder bound. The focus complements the existing sampled-force lab; it adds no real-world interpretation or active grading.

| Actual command/check | Result |
| --- | --- |
| Calculus II regressions and project recalculations | 89 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed; workload, accessibility and qualified mathematical review remain outstanding.

## Prior increment: review handoff for Calculus I 0.4.6 (2026-10-10)

Pinned the Calculus I public package and prepared a handoff covering the existing washout lab and inactive model portfolio, calculus keys, numerical error, units, accessibility and workload. The snapshot regression compares its hashes and inventory with the deterministic archive builder.

| Actual command/check | Result |
| --- | --- |
| Calculus I regressions, portfolio recalculations and snapshot identity | 83 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `2b46c6ff4284f7174d11e2c56dcb529657d3f18d359e020bef0369c8a09b103b`; manifest SHA-256 `3b5f831f893770ec1b29e62e267d85d06e317957a75bb67da4c8a66c615c7af9`; 23 files; 268,524 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The package hash establishes identity only. The new portfolio is inactive, ungraded and unreviewed; course workload and accessibility remain open.

## Prior increment: inactive washout model portfolio for Calculus I 0.4.6 (2026-10-10)

Pinned the Calculus I public package and prepared a handoff covering the existing washout lab and inactive model portfolio, calculus keys, numerical error, units, accessibility and workload. The snapshot regression compares its hashes and inventory with the deterministic archive builder.

| Actual command/check | Result |
| --- | --- |
| Calculus I regressions, portfolio recalculations and snapshot identity | 83 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `2b46c6ff4284f7174d11e2c56dcb529657d3f18d359e020bef0369c8a09b103b`; manifest SHA-256 `3b5f831f893770ec1b29e62e267d85d06e317957a75bb67da4c8a66c615c7af9`; 23 files; 268,524 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The package hash establishes identity only. The new portfolio is inactive, ungraded and unreviewed; course workload and accessibility remain open.

## Prior increment: inactive washout model portfolio for Calculus I 0.4.6 (2026-10-10)

Added an inactive paper-only portfolio with a constructed biexponential signal, derivative/monotonicity analysis, a Newton threshold estimate, exact and composite-Simpson accumulation, and blank-sensitivity calculation. The existing lab now explicitly describes the draft as inactive and unscheduled.

| Actual command/check | Result |
| --- | --- |
| Calculus I course regressions, including project recalculations and status | 82 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed; it uses constructed data and adds no real-world clearance or treatment guidance.

## Prior increment: review handoff for Linear Algebra 0.3.5 (2026-10-10)

Pinned the current public package and prepared a review handoff for the proposed sequence, 69 numeric public answers, linear-algebra conventions and the inactive state-reconstruction project. The archive digest is checked against the deterministic package builder; it proves identity only.

| Actual command/check | Result |
| --- | --- |
| Linear Algebra regressions, project recalculations and snapshot identity | 86 passed. |
| Public package digest | Passed: version 0.3.5; archive SHA-256 `c5aa468682077ff41a00ed07f21211d94c09632e27fd8c0bb91054951b9c539f`; manifest SHA-256 `d415b906099ce75da58b34d1546280abbee0414a7354759a1618eaa332ee1bfc`; 23 files; 282,250 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The snapshot does not imply mathematical review or release. The project draft is inactive, synthetic and ungraded; workload, accessibility and qualified review remain open.

## Prior increment: inactive state-reconstruction project for Linear Algebra 0.3.5 (2026-10-10)

Added a linked, inactive project draft with a synthetic least-squares dataset and a separate transition-dynamics analysis in orthonormal coordinates. Recalculation tests pin the solution, residual, singular values/condition number and eigenmode behavior. The package remains partial; no graded work or human review is claimed.

| Actual command/check | Result |
| --- | --- |
| Linear Algebra content regressions, including project checks | 85 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project uses constructed data only and remains ungraded, inactive and unreviewed.

## Prior increment: review handoff for Statistics 0.4.5 (2026-10-10)

Pinned the Statistics public package and prepared a reviewer handoff for the synthetic pilot, design assumptions, numeric keys, inactive protocol draft, accessibility, workload and research-ethics boundary. The snapshot is outside the archive and a regression compares it with the deterministic archive builder.

| Actual command/check | Result |
| --- | --- |
| Statistics-focused regressions and snapshot identity | 557 passed; 671 unrelated tests deselected. |
| Public package digest | Passed: version 0.4.5; archive SHA-256 `65ea774959641838cab0180e83e9448d55581260b6b58252fc8dbd7fe4aad2a8`; manifest SHA-256 `3f89595ad999b7af416a11efd2a9e1fb1761a026fccdcfe5db406eeeeee79ea2`; 24 files; 337,681 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The snapshot proves package identity only. The protocol draft is inactive, ungraded, unreviewed and not real-world research guidance.

## Current increment: inactive confirmatory-study project for Statistics 0.4.5 (2026-10-10)

Added a paper-only protocol portfolio that extends the week-14 pilot lesson into a complete pre-study plan: question and estimand, independent unit, allocation/blinding, effect and variance assumptions, sample-size sensitivity, multiplicity, data structure, visualization and bounded interpretation. The pilot is explicitly synthetic; no observations are collected and no real-world research guidance is given. The unweighted human rubric is inactive and outside the manifest's assessment schedule. Existing questions and keys are unchanged.

| Actual command/check | Result |
| --- | --- |
| Statistics-specific regressions, project draft, and relevant AI-assisted checks | 556 passed; 671 unrelated tests deselected. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The draft remains unreviewed, unmeasured, ungraded and not a substitute for qualified statistical or research-ethics review.

## Current increment: review handoff for Circuits & Instrumentation 0.4.6 (2026-10-10)

Pinned the public Circuits package and prepared a handoff covering sequence, numerical keys, loading, CMRR, filter/sampling assumptions, the inactive project, accessibility and workload. The digest snapshot is outside the package and regression-checked against the archive builder.

| Actual command/check | Result |
| --- | --- |
| Circuit recalculations, project checks and snapshot identity | 127 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `9944010af6a01affa84cde894b7aaadac57d6e0c7502a611f587f9380adfca2d`; manifest SHA-256 `6143955fa1866944fca6a30e1ab761c00d1bbdc279348063035d31eea5e2ec1a`; 22 files; 292,592 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

Hash and tests do not establish physical safety, hardware performance or independent review. The project remains inactive, ungraded and unreviewed.

## Current increment: inactive sensor-channel design project for Circuits 0.4.6 (2026-10-10)

Added an idealized paper-design project that integrates input loading, differential gain and headroom, common-mode rejection, first-order filtering, sampling and ADC quantization. It defines a synthetic low-frequency signal and fixed assumptions, highlights the 50 Hz/Nyquist filter limitation, and includes an unweighted human rubric. The syllabus links it as inactive; it is not in the course assessment list and authorizes no hardware build. Existing readings, public items and keys are unchanged.

| Actual command/check | Result |
| --- | --- |
| `tests/content/test_circuits_integrative_project_draft.py` and `tests/content/test_circuits_recalculations.py` | 126 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The design remains synthetic, ungraded and unreviewed. Hardware suitability, workload, accessibility and release policy have not been established.

## Current increment: review handoff for Calculus III 0.4.7 (2026-10-10)

Pinned the current Calculus III public package and created a reviewer handoff for its course sequence, math keys, sign/unit conventions, theorem conditions, inactive project, accessibility and workload. The digest snapshot stays outside the archive. A regression compares the digest CLI's output with the snapshot, so later package changes require a fresh review target.

| Actual command/check | Result |
| --- | --- |
| Calculus III numerical/reasoning suite plus snapshot regression | 92 passed. |
| Public package digest | Passed: version 0.4.7; archive SHA-256 `f3b0b990402c10fb01d98ee9819eea3ad46876c5994d17973802e913c7be5284`; manifest SHA-256 `dc9c6a5f7ff2591341f041b3f1a12e4d957ee6fea6887b61f2f2c1beb70f438a`; 22 files; 269,030 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The snapshot proves package identity only. The project, course and all numerical material remain unreviewed and formative-only.

## Current increment: inactive integrative vector-field project for Calculus III 0.4.7 (2026-10-10)

Added an ungraded project draft that extends the existing rectangular flux lab with a circular field: constrained extrema, polar area measure, oriented boundary flux, divergence-theorem comparison and diffusivity sensitivity. It includes an unweighted human rubric and remains outside the course's scheduled assessment list. Existing readings, items, keys and cards are unchanged.

| Actual command/check | Result |
| --- | --- |
| `tests/content/test_calculus_three_recalculations.py` | 91 passed, including the project mass/flux and draft-status regression. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project is a mathematical authoring draft, not a graded or reviewed course component. Workload, accessibility, mathematical review and activation remain open.

## Current increment: review handoff for Programming 0.4.6 (2026-10-10)

Pinned the complete Programming public package and prepared a reviewer checklist for course scope, numeric/data checks, the inactive capstone, accessibility, workload and release boundaries. The snapshot is outside the course archive to avoid self-referential hashing. A regression invokes the archive builder and compares the computed version, package/manifest digests and inventory with the snapshot.

| Actual command/check | Result |
| --- | --- |
| Programming project + recalculation regressions | 112 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `66892cafa5b170c9e187412aff1db2321c493ece2d1684f729e21b022d740443`; manifest SHA-256 `ce943ef928c0783693198aef001b6c972bc0418354f9c3d95274e1c7dd06de3d`; 24 files; 285,225 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves file identity only. The capstone remains an ungraded draft, and no reviewer or release decision is recorded.

## Current increment: inactive integrative project draft for Programming 0.4.6 (2026-10-10)

Added a public authoring draft for a course-scale sensor-calibration pipeline project, a deterministic 90-row synthetic dataset and generator, five staged deliverables, and a seven-criterion unweighted human rubric. The draft is linked from the syllabus as inactive; it is not in the manifest's scheduled assessment list, carries no points and does not run learner code. Training uses batches B01–B04, while B05–B06 remain held out for new-batch evaluation. The computed keys and answers are public because the draft is ungraded.

| Actual command/check | Result |
| --- | --- |
| `tests/content/test_programming_integrative_project_draft.py` | 3 passed: deterministic regeneration, separate least-squares and held-out error recalculation, and inactive/ungraded status. |
| `tests/content/test_programming_recalculations.py` | 108 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

This is a project design draft, not a reviewed or measured course component; assessment, accessibility, workload, code-submission safety and release decisions remain open.

## Current increment: Calculus III frame-consistency example (0.4.6, 2026-10-10)

Expanded the first Calculus III reading with a numerical example that rotates both the gradient and a unit direction into a new orthonormal frame. It shows the directional derivative remains 5 when the representations are consistent, while mixing components from different frames produces a misleading zero. The manifest worked example and syllabus version now match 0.4.6; public questions, answers, objectives and cards are unchanged.

| Actual command/check | Result |
| --- | --- |
| `tests/content/test_calculus_three_recalculations.py` | 90 passed, including the new frame-invariance regression. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

This worked example strengthens one mathematical explanation; the package remains partial, unreviewed and formative-only.

## Current increment: refresh catalog metrics on the project front page (2026-10-10)

Updated the README's course-catalog totals to match the current content validator: 387 lessons and 2,299 formative questions. The package count, card and case totals, and explicit statement that no package meets the complete-course standard remain unchanged.

| Actual command/check | Result |
| --- | --- |
| Content validator, with declared development requirements | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| README stale/new metric check | Passed. |
| `git diff --check` | Passed. |

## Current increment: cross-course numeric-key regression coverage (2026-10-10)

Audited public practice-bank numeric items across the catalog. All 25 banks contain 1,462 numeric items; the dedicated recalculation suites exercise the course-specific reference calculations, and each course suite pins its expected key inventory. Cell Biology previously split its checks across week-specific tests, so an exact 21-item inventory assertion now makes additions require an explicit coverage update. The check does not recalculate inactive private assessment candidates.

| Actual command/check | Result |
| --- | --- |
| Dedicated recalculation suites (`test_*_recalculations.py`, `test_ai_assisted_checks.py`, `test_cell_biology_assembled.py`) | 1,890 passed across all 25 courses. |
| Public numeric-bank inventory | 25 course banks; 1,462 numeric items. |
| Cell Biology numeric inventory regression | 21 current keys match the audited coverage set. |
| Ruff on the changed regression file | Passed. |

These are author-side, separately coded arithmetic/model checks. They do not provide independent scientific review, validate inactive private candidates, or satisfy assessment, accessibility and workload release gates.

## Current increment: deterministic Cell Biology review-package snapshot (2026-10-10)

Added a read-only CLI and a reviewer-facing snapshot outside the course archive so reviewers can identify the exact public package without a self-referential digest. The snapshot names the course version, archive SHA-256, manifest SHA-256, file count and byte count; it explicitly does not imply approval. A regression invokes the CLI and compares its JSON with the checked-in snapshot.

| Actual command/check | Result |
| --- | --- |
| `tests/content/test_cell_biology_integrity.py` | 10 passed, including snapshot-to-archive digest verification. |
| Package digest CLI | Passed: Cell Biology 0.53.0; archive SHA-256 `56398f41805dccae2ed08ef7607c8c1261a25062b30faa45cf53c62728d5b7d5`; manifest SHA-256 `04bb0d6114545faf36ba2a081ea256c311eb349eda921bfd07a699c8eb1b3ef3`; 122 files; 2,102,096 bytes. |
| Ruff on the new CLI and regression | Passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| `git diff --check` | Passed; Git emitted existing CRLF-to-LF normalization notices. |

The digest establishes package identity only. Scientific, assessment, accessibility and workload reviews remain external release gates.

## Current increment: deterministic Cell Biology review-package snapshot (2026-10-10)

Added a read-only CLI and a reviewer-facing snapshot outside the course archive so reviewers can identify the exact public package without a self-referential digest. The snapshot names the course version, archive SHA-256, manifest SHA-256, file count and byte count; it explicitly does not imply approval. A regression invokes the CLI and compares its JSON with the checked-in snapshot.

| Actual command/check | Result |
| --- | --- |
| `tests/content/test_cell_biology_integrity.py` | 10 passed, including snapshot-to-archive digest verification. |
| Package digest CLI | Passed: Cell Biology 0.53.0; archive SHA-256 `56398f41805dccae2ed08ef7607c8c1261a25062b30faa45cf53c62728d5b7d5`; manifest SHA-256 `04bb0d6114545faf36ba2a081ea256c311eb349eda921bfd07a699c8eb1b3ef3`; 122 files; 2,102,096 bytes. |
| Ruff on the new CLI and regression | Passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| `git diff --check` | Passed; Git emitted existing CRLF-to-LF normalization notices. |

The digest establishes package identity only. Scientific, assessment, accessibility and workload reviews remain external release gates.

## Current increment: regression coverage for all Cell Biology public numeric keys (2026-10-10)

Compared the 21 current numeric-type practice items with test references. Existing week-level regressions cover 19; added independent recomputations for the two uncovered week-3 keys: the Michaelis–Menten rate at twice Km and standard free energy from the stated equilibrium constant. Every public numeric question now has a regression reference. The question bank and teaching content are unchanged; all items remain public formative practice.

| Actual command/check | Result |
| --- | --- |
| `tests/content/test_cell_biology_assembled.py` | 5 passed, including the two added numerical checks. |
| Numeric-key coverage scan | 21 numeric questions; 0 without a regression reference. |
| Ruff on the changed regression file | Passed. |
| Content validator and candidate, course-gap, response-mode report checks | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| `git diff --check` | Passed; Git emitted existing CRLF-to-LF normalization notices. |

These are author-side consistency checks, not independent scientific review or evidence of learner mastery.

## Current increment: plain-language alternatives for Cell Biology equations (2026-10-10)

Cell Biology 0.52.0 adds adjacent plain-language equivalents for 16 central standalone equations across 11 quantitative readings. The course metadata now distinguishes that author check from the still-open comprehensive notation and assistive-technology review. To preserve source binding, prerequisite digests were refreshed in nine affected inactive candidate records; candidate prompts, datasets, point totals, and protected answer stores were not changed. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Equation-alternative, scope and inventory regressions | 3 passed. |
| Candidate-audit and response-mode regression files | 11 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff on changed content regression files | Passed. |
| `git diff --check` | Passed; Git emitted existing CRLF-to-LF normalization notices. |

Plain-language summaries improve access to the listed equations but do not verify screen-reader pronunciation, structural navigation, every inline calculation or table, or learner usability. A qualified accessibility review remains required.

## Current increment: early-course short-answer rehearsal for Cell Biology 0.51.0 (2026-10-10)

Added an optional week-1/2 written-response rehearsal with three self-checked prompts on acid-base state, potassium equilibrium, and transport-route evidence. Linked it from the week-2 syllabus row and assessment crosswalk. The lesson sits outside the public question bank, no response is collected or scored, and the grade policy and assessment counts are unchanged. Cell Biology remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Cell Biology scope and repository-inventory regressions | 2 passed, including the corrected week-2/week-8 schedule and ungraded-prompt links. |
| Candidate-audit and response-mode regression files | 11 passed. |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff on changed content regression files | Passed. |
| `git diff --check` | Passed; Git emitted existing CRLF-to-LF normalization notices. |

The rehearsal adds self-check opportunities but not automated or human-scored evidence of learner performance.

## Current increment: week-8 synthesis readings for Cell Biology 0.50.0 (2026-10-10)

Added two original, ungraded readings to Cell Biology week 8: one connects quantitative models to assumptions, units, and limits; the other synthesizes controls, independent replicates, uncertainty, and bounded claims. Both are linked from the syllabus and assessment crosswalk and reuse existing objectives. They add no question-bank items or grading; the cumulative review remains 25 questions / 44 points, not a midterm. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 386 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Content, response-mode and candidate regression files | 107 passed, 2 skipped, with one new scope assertion corrected; the isolated corrected week-8 scope test passed (1 passed). |
| Candidate, course-gap and response-mode report drift checks | Passed. |
| Ruff on changed content regression files | Passed. |
| `git diff --check` | Passed; Git emitted existing CRLF-to-LF normalization notices. |

The readings provide private study prompts and are not collected or scored. Their author-side checks are not independent scientific or accessibility review.

## Current increment: complete cross-course content regression repairs (2026-10-10)

The complete content suite exposed stale fixed snapshots in nine course checks, four numeric questions absent from the independent recalculation maps, and a long-decimal Taylor bound in Calculus I. The version checks now compare each syllabus with its manifest; Chemistry I/II item counts and Statistics outcome counts match their current packages. The Bayes positive-predictive value, bioreactor impeller Reynolds number, steady-flow energy balance and solid-shaft torsion stress are now independently recomputed in regression tests. The Calculus I remainder bound now displays a rounded-up `3.850 × 10⁻⁴` second-derivative bound, preserving the inequality.

| Actual command/check | Result |
| --- | --- |
| Full content suite with six workers (`PYTHONUTF8=1 uv run --project backend --with jsonschema --with pytest-xdist pytest -n 6 -q tests/content`) | 2,705 passed, 2 skipped. |
| All five affected regression files | 1,408 passed. |
| Ruff on affected content regression tests | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |

The new recalculations validate the authored assumptions only; they are not independent expert scientific review.

## Current increment: week-14 lineage-to-function design rehearsal (2026-10-10)

Cell Biology 0.49.0 adds an optional ungraded written brief using the lesson's synthetic matrix-by-cue example. It asks learners to design a blocked follow-up with differentiation batch as the biological unit, verify the inputs cells encounter, separate marker/identity/function measurements, and bound any translational claim. The syllabus and assessment crosswalk link it. Responses are not collected or scored; maturity and grading policy remain partial and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused week-14 worksheet, prior matrix-design and scope-status tests | 3 passed. |
| Objective response-mode audit regression | 2 passed. |
| Content validator | Passed: 25 courses / 384 lessons / 2,299 questions / 1,276 cards / 25 cases; 0 errors or explicit limitation/depth warnings. |
| Candidate, objective-gap and response-mode generated report checks | Passed. |

This adds a written rehearsal for one design objective; it does not establish course mastery, assessment readiness or qualified review.

## Current increment: aggregate audit for graded-source archive coverage (2026-10-10)

Added `python -m courselab.audit_graded_archives`, a read-only operator audit that streams graded submissions, checks their enrollment/plan/assessment links, and verifies the matching archived source bytes against their SHA-256. Results aggregate by course/version/assessment/status and omit learner or submission IDs, responses, scores and source content. It distinguishes missing archives from digest mismatches, corrupt bytes and broken snapshot links. `source_archive_verified` covers source linkage and bytes only; it does not certify grading correctness. The command never tries to reconstruct historical material from current files.

| Actual command/check | Result |
| --- | --- |
| Focused graded-archive audit regressions | 2 passed, covering verified source archive, missing archive, corrupt bytes, CLI reporting and omission of learner/submission details. |
| Full backend suite (`PYTHONUTF8=1 uv run --project backend pytest -q backend/tests`) | 4,890 passed, 3 skipped, 1 upstream Starlette/httpx deprecation warning. UTF-8 mode is required for a Windows fixture that reads UTF-8 question content with the platform default encoding. |
| Full backend Ruff check | Passed. |

This makes archive coverage measurable but does not restore unverifiable records or enable historical regrading where source evidence is absent.

## Current increment: distinguish blocked source probes from broken links (2026-10-10)

The optional live-link validator now scans 214 registry entries and Markdown destinations across public course packages, deduplicating them to 251 unique URLs. HTTP 401/403 responses are `link-access-denied` warnings rather than broken destinations; a 404 remains an error. The two official JHU AAP pages returning 403 were separately opened and their current program and prerequisite content verified; their registry access dates were refreshed. The automated HTTP client still cannot fetch those pages, and the live probe continues to report that limitation.

| Actual command/check | Result |
| --- | --- |
| `python tools/validate_content.py --check-links` in the dedicated content-validation image | Passed: 25 courses, 384 lessons, 2,270 questions, 1,276 cards, 25 cases; 0 errors and 3 explicit access-denied warnings (two JHU URLs, one IUPAC URL). |
| `tests/content/test_content_validation.py` | 87 passed, including Markdown link discovery/deduplication, current inventory, source-map references, HTTP 403 classification and HTTP 404 errors. |

This change improves probe reporting; it does not grant the validator access to denied servers or replace qualified review of the curriculum map.

## Current increment: digest-gated legacy public archive recovery (2026-10-10)

Added `python -m courselab.backfill_course_archives` for operator-reviewed recovery of migration-0011 archives. It is dry-run-only by default, lists distinct course/version enrollment groups without learner IDs, skips versions unavailable in the current package root, and requires an independently verified deterministic package SHA-256 before `--apply` can write. The command does not assert historical equivalence from a version string alone, and no persistent database was modified during validation.

| Actual command/check | Result |
| --- | --- |
| Full backend suite in the shared development container | 4,828 passed, 2 expected skips; one upstream Starlette/httpx deprecation warning. |
| Archive recovery and archive API regressions | 12 passed. |
| Ruff on the recovery command and archive tests | Passed. |
| Disposable PostgreSQL 17 production-image smoke | Passed migration 0011, restricted-role checks, dry-run with no insert, rejection without expected digest, verified CLI apply, version index and answer-free archive DTO reads. |
| Candidate report and course-gap drift checks | Passed. |
| `git diff --check` | Passed; Git reported only existing CRLF-to-LF normalization notices. |

Only a package verified against an independent trusted release digest can be backfilled. Unavailable historical package bytes and older versions remain unrecoverable through this command.

## Current increment: read-only rendering of archived course versions (2026-10-10)

Enrolled learners can open a prior course version from its digest-verified public-package snapshot. The API exposes archived syllabus and lesson content only through the existing `PublicCourse` and `PublicLesson` DTOs; lesson questions carry no variant token or grader fields. Historical views require a current enrollment, allow no notes, progress, ratings or submissions, and exclude the separate private assessment source root. An enrollment-gated version index lists saved packages newest-first; the workspace links to older versions and back to the current package. No archive is created on a read request, and legacy enrollments remain unbackfilled.

| Actual command/check | Result |
| --- | --- |
| Full backend suite in the shared development container | 4,824 passed, 2 expected skips; one upstream Starlette/httpx deprecation warning. |
| Archive API regressions | 8 passed, including upgrade history, enrollment gating, safe archived DTOs and answer-key exclusion. |
| Full frontend unit suite | 45 passed across 13 files. |
| Frontend typecheck, lint and production build | Passed. |
| Production-image CI job | Added a job to build the hardened API/web images, provision the restricted `courselab_app` role, migrate disposable PostgreSQL through 0011 as the migration owner, and smoke-test enrollment/archive DTOs as the runtime role. It also checks the built reader and production Compose parse; these exact steps passed locally. |
| Production API image smoke | On disposable PostgreSQL 17, applied Alembic through 0011 as `courselab`, then confirmed non-superuser `courselab_app` can pass health, enroll in Cell Biology, list versions, and read archived course/lesson DTOs without grader fields in the read-only API image. |
| Production web image smoke | Built the runtime image and confirmed the historical-view bundle is present. |
| `docker compose -f compose.production.yaml config --quiet` with placeholder deployment values | Passed configuration parsing; no deployment secrets or persistent services were used. |
| Ruff on changed backend sources/tests | Passed. |
| Content validation in the Docker build stage | Passed: 25 courses, 384 lessons, 2,270 questions, 1,276 cards, 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed locally; both checks are now part of the `content-backend` CI job. |

Read-only viewing closes the learner rendering gap but does not support historical regrading or backfill records from before migration 0011. Course maturity and all external review gates are unchanged.

## Previous increment: immutable public course-package archives (2026-10-10)

Alembic 0011 archives a deterministic snapshot of every public course-package file when a learner enrolls or upgrades to a content version. The archive records a package digest and per-file SHA-256 values, validates safe paths and sizes, and rejects edits that reuse an already archived version. Private answer sources are excluded. Existing enrollments are not backfilled; learner-facing rendering from archived versions and historical regrading remain open. Numeric unit support now includes kW, used by an authored transport item.

| Actual command/check | Result |
| --- | --- |
| Full backend suite in the shared development container | 4,822 passed, 2 skipped; two warnings (upstream Starlette/httpx deprecation and read-only pytest cache). |
| Deterministic archive sweep over the live catalog | 25 courses and 628 files archived and round-tripped; largest archive 1,949,252 bytes. |
| Ruff on changed backend sources and tests | Passed. |
| `git diff --check` | Passed. |

The archives contain public packages only; private assessment material remains on its separate source path. Snapshot storage does not yet make historical content available in the learner UI and does not promote any course beyond its existing maturity status.

## Previous increment: Biology candidate dataset integrity checks through the final and integrative project (2026-10-10)

Strengthened answer-free data-contract regressions for inactive Biology Homeworks 1–8, the cumulative midterm and final, Labs 1–3, and the integrative project. Homework 1 checks four named preparations per condition, matched 0/30/90-minute observations, positive preparation-specific pulse denominators, finite measurements, and valid scales. Homework 2 checks the four assay days crossed with all three conditions, alongside calibration, blank/reaction, substrate and time-window structure. Homework 3 checks three conditions crossed with four cultures, matched 0/2/6-hour observations, finite channels and positive DNA-reference denominators. Homework 4 checks the stated four-culture assignments for both ChIP and reporter datasets while preserving the duplicate-well, construct, and unpaired-sample structure. Homework 5 checks the four named cultures per condition, matched baseline/chase condition assignments, 0/2/4/6-hour observations, finite chase measurements, and positive recovery references. Homework 6 checks the named four-clone groups, the two culture replicates nested within each clone, finite assay channels, and within-clone condition consistency. Homework 7 checks four named parent preparations crossed with the six distinct conditions, finite values, matched seeded-cell denominators, and the low/high accessible-ligand matching. Homework 8 checks four named cultures per condition, the matched 0/24/72-hour time courses, and consistent condition assignments within each culture. Midterm measurements are checked for matching case/metric coverage and unit declarations across both authored forms. Lab 1 checks all four culture input/fraction pairs, positive matched inputs across forms, and bounded collected-fraction activities. Lab 2 checks both time-dependent measurements for each of four cultures and both forms, including positive, declining 10-to-30-minute trajectories. Lab 3 checks four paired viable/marker-positive counts, marker bounds, and matching viable denominators across forms. Final and project main observations pin the expected measured-case sets and row counts; the project supplemental table also checks the complete form-by-condition-by-culture-by-time structure, finite measurements, and declared reference/count bounds. Candidate prompts, private keys, hashes, and activation states are unchanged.

| Actual command/check | Result |
| --- | --- |
| `tests/content/test_cell_biology_candidate.py` | 105 passed after the Homework 4–8, midterm, Labs 1–3, and project checks. |
| Ruff on the candidate integrity regression (`--no-cache` for the read-only container mount) | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,270 questions, 1,276 cards and 25 cases; 0 errors and 0 warnings. |
| Assessment-candidate report drift check | Passed. |
| Course-gap report drift check | Passed; no objective-to-outcome, practice or assessment-mapping gaps. |

These checks validate only public dataset structure and plausible ranges. They do not recalculate protected answer keys or satisfy independent scientific, assessment, accessibility, workload or release review. All eight checked homework candidates, the midterm, Labs 1–3, and the integrative project remain inactive.

## Previous increment: Robotics & Mechatronics 0.4.5 (2026-10-10)

Linked the first four lesson objective pairs to outcomes 1–4 and added direct practice for transform-composition order, torque from angular acceleration, and uncertainty-aware safety margins. Existing prompts and keys are unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Robotics recalculation and outcome-alignment selection | 112 passed. |
| Ruff on the focused Robotics regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,270 questions, 1,276 cards and 25 cases; 0 errors and 0 warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration; 0 objectives lack outcome links, assessment mappings or practice items. |

The new safety item compares a conservative clearance bound with stopping distance plus the stated margin; it is a teaching example, not a validated robot safety function. These same-AI checks are not independent robotics, engineering-safety or accessibility review.

## Previous increment: Human Physiology for Engineers 0.4.5 (2026-10-10)

Linked the first four lesson objective pairs to their course outcomes, clarified the homeostasis objective, corrected the membrane-current item association, and added direct practice for feedback-loop components, membrane voltage as a state variable, and ventilation limitation. Existing numeric prompts and keys are unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physiology focused regression selection | 5 passed. |
| Ruff on the focused Physiology regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,267 questions, 1,276 cards and 25 cases; 0 errors and 0 warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration; 8 objectives still lack outcome links. |

The new questions distinguish measurement/feedback roles, voltage from current, and ventilation from perfusion and diffusion. These same-AI checks are not independent physiology, clinical or accessibility review.

## Previous increment: Cellular Biomechanics & Mechanobiology 0.3.5 (2026-10-10)

Linked the first four lesson objective pairs to outcomes 1–4, corrected the stress-relaxation and perturbation/rescue item associations, and added direct practice for mechanical quantities, the ECM-to-nucleus force path, and mechanical inputs versus molecular readouts. Existing numeric prompts and keys are unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Cellular Biomechanics focused regression selection | 5 passed. |
| Ruff on the focused Cellular Biomechanics regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,264 questions, 1,276 cards and 25 cases; 0 errors and 0 warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration; 16 objectives still lack outcome links. |

The assessments list both outcomes for lesson 1 because its linked objectives cover stress/strain and constitutive behavior. These same-AI checks are not independent biomechanics, cell-biology or accessibility review.

## Previous increment: Calculus III 0.4.5 (2026-10-10)

Linked the first four lesson objective pairs to outcomes 1–4, clarified outcome 1 to include vector-frame representation, corrected the vector-component, constrained-optimum and divergence-theorem item associations, and added direct practice for the affected objectives. Existing numeric prompts and keys are unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Calculus III recalculation and outcome-alignment selection | 90 passed. |
| Ruff on the focused Calculus III regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,261 questions, 1,276 cards and 25 cases; 0 errors and 0 warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration; 24 objectives still lack outcome links. |

The new Hessian item uses a positive-definite quadratic, and the line-integral item asks for work along an oriented path. These same-AI checks are not independent mathematics, pedagogy or accessibility review.

## Previous increment: Calculus II 0.4.5 (2026-10-10)

Linked the first four lesson objective pairs to outcomes 1–4, clarified outcome 1 to include convergence of improper integrals, corrected the exponential-integral question association, and added direct formative checks for integration-method choice, Taylor construction and a geometric-series convergence interval. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Calculus II recalculation and outcome-alignment selection | 87 passed. |
| Ruff on the focused Calculus II regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,258 questions, 1,276 cards and 25 cases; 0 errors and 0 warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration; 32 objectives still lack outcome links. |

The convergence interval excludes both endpoints because the geometric-series terms fail to approach zero there. These same-AI checks are not independent mathematics, pedagogy or accessibility review.

## Previous increment: Calculus I 0.4.5 (2026-10-10)

Linked the first four lesson pairs to outcomes 1–4, corrected the first lesson's derivative-item association, and added a direct removable-limit question. The preserved derivative prompt and numeric key are unchanged; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Calculus I recalculation and outcome-alignment selection | 80 passed. |
| Ruff on the focused Calculus I regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,255 questions, 1,276 cards and 25 cases; 0 errors and 0 warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration; 40 objectives still lack outcome links. |

The new item checks the limit of a factored expression on its punctured domain; it does not claim the function is defined at the excluded point. These same-AI checks are not independent mathematics, pedagogy or accessibility review.

## Previous increment: Biochemistry I 0.4.5 (2026-10-10)

Linked the first four lesson pairs to outcomes 1–4, corrected the occupancy and pool/flux question associations, and added direct formative checks for protein structure levels and regulatory layers. Existing numeric prompts and keys are unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry focused regression selection | 5 passed. |
| Ruff on the focused Biochemistry regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,254 questions, 1,276 cards and 25 cases; 0 errors and 0 warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration; 48 objectives still lack outcome links. |

The new questions target the previously under-tested structure-level and regulatory-layer objectives. These same-AI checks are not independent biochemical, laboratory or accessibility review.

## Current increment: Biomaterials & Tissue Engineering 0.3.5 (2026-10-10)

Linked the first four lesson pairs to outcomes 1–4. Reassigned the preserved degradation-mass and cartilage-evidence questions to their matching objectives, clarified the tissue-strategy objective to include functional readouts, and refined outcome 4 to include application-specific failure modes. Added direct practice for scaffold architecture tradeoffs and cell-source choices; existing prompts and numeric keys are unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biomaterials regression/content selection | 5 passed. |
| Ruff on the focused Biomaterials regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,252 questions, 1,276 cards and 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration. |

The new items ask learners to balance pore connectivity against compression/fabrication constraints and to compare conditional tradeoffs among autologous, allogeneic, and progenitor cell sources. The checks are not independent biomaterials, clinical, or accessibility review.

## Current increment: Bioreactors & Tissue Culture Engineering 0.4.5 (2026-10-10)

Broadened outcome 2 to include scale-up constraints and linked the first four lesson pairs to outcomes 2–4. Corrected the oxygen-demand and constant-tip-speed item associations; added a direct impeller Reynolds-number calculation. Existing question prompts and keys are unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Bioreactors regression/content suite | 5 passed. |
| Ruff on the focused Bioreactors regression source | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,250 questions, 1,276 cards and 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration. |

For ρ=1000 kg/m³, N=0.80 s⁻¹, D=0.10 m and μ=0.001 Pa·s, the stated impeller Reynolds number is 8,000. This is a dimensionless regime estimate, not a standalone scale-up criterion. These same-AI checks are not independent bioprocess, hardware-safety or accessibility review.

## Current increment: General Chemistry II 0.4.5 (2026-10-10)

Linked the two weak-acid/buffer objectives to outcome 1. The existing pKa-and-ratio item is now associated with the Henderson–Hasselbalch objective, and new practice asks learners to form Ka from the weak-acid material balance. The prior question prompts and keys are unchanged; the syllabus now lists 98 public practice items. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry II focused regression/content suite | 7 passed. |
| Ruff on the focused General Chemistry II regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,249 questions, 1,276 cards and 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration. |

For HA ⇌ H⁺ + A⁻, the item uses [HA]=C−x and [A⁻]=x to obtain Ka=x²/(C−x); it distinguishes this exact balance from the small-dissociation approximation. These same-AI checks are not independent chemistry or accessibility review.

## Current increment: General Chemistry I 0.4.5 (2026-10-10)

Refined outcome 2 to include electronic structure alongside bonding and molecular geometry, then linked the two module-1 objectives to it. The old trigonal-planar question now maps to the VSEPR objective, and a new item directly tests the Period 3 atomic-radius trend. The original question prompt and key are unchanged; the syllabus now lists 92 public practice items. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry I focused regression/content suite | 4 passed. |
| Ruff on the focused General Chemistry I regression sources | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,248 questions, 1,276 cards and 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration. |

The new item compares the n=3 configurations of sodium and chlorine; the reading explains the across-period effective-nuclear-charge trend and the model's limits. These same-AI checks are not independent chemistry or accessibility review.

## Current increment: Electrical Circuits & Instrumentation 0.4.5 (2026-10-10)

Linked the first four lesson pairs to outcomes for DC networks, amplification, frequency response, and calibrated measurements. Added a unit-required node-voltage calculation for a three-branch network and a direct check of analog anti-alias filtering; existing questions and answer keys remain unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Circuits regression/content suite | 124 passed. |
| Ruff on the changed Circuits regression source | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,247 questions, 1,276 cards and 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration. |

The new KCL example gives v=96/13≈7.385 V; the sampling item distinguishes the Nyquist threshold from pre-conversion analog filtering. These same-AI checks are not independent circuits, instrumentation, hardware-safety or accessibility review.

## Current increment: Programming & Numerical Methods for Bioengineering 0.4.5 (2026-10-10)

Linked the first four lesson pairs to outcomes 1–4 according to the existing practice and instructional goals: reproducible data/provenance and plotting, testable functions, numerical integration and constraints, and fit/validation. Existing questions and keys are unchanged; all readings were already expanded. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Programming & Numerical Methods regression | 108 passed. |
| Ruff on the focused Programming regression source | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,245 questions, 1,276 cards and 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration. |

The report now shows all 38 Programming lesson objectives linked to and practiced against course outcomes; across the catalog, 76 lesson objectives remain without an outcome link. These same-AI checks are not independent programming or accessibility review.

## Current increment: Differential Equations for Living & Engineered Systems 0.3.6 (2026-10-10)

Linked the first four lesson pairs to outcomes 1, 2 and 4. Clarified the damping-ratio objective, reassociated the existing coupled-system stability item with the eigenvalue objective, and added direct checks for damping regime and local linearization; the original numeric prompts and keys remain unchanged. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Differential Equations focused regression | 5 passed. |
| Ruff on the focused Differential Equations regression source | Passed. |
| `python tools/validate_content.py --root . --json` | Passed: 25 courses, 384 lessons, 2,245 questions, 1,276 cards and 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration. |

The damping example has ζ=1 and is critically damped. For f(x)=x(1−x) near x*=1, the first-order perturbation equation is δ̇≈−δ. These same-AI checks are not independent mathematics, engineering or accessibility review.

## Current increment: Thermodynamics & Transport in Bioengineering 0.4.4 (2026-10-10)

Expanded week 12 with conduction, convection and radiation rate laws; steady thermal-resistance networks; transient energy storage; lumped-capacitance assumptions; Biot and Fourier numbers; and limits of the models. Mapped the heat-transfer-mode objective to outcome 4 and the resistance-network objective to outcomes 1 and 4. Corrected the preserved slab-resistance item association and added direct practice distinguishing the three mechanisms; both original numeric prompts and keys are unchanged. MIT OpenCourseWare 2.51 readings are link-only. All four former compact readings now have expanded instruction; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Thermodynamics & Transport focused regression | 8 passed. |
| Ruff on the focused regression sources | Passed. |
| python tools/validate_content.py --root . --json | Passed: 25 courses, 384 lessons, 2,243 questions, 1,276 cards and 25 cases; 0 errors and 0 depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |
| Course-gap report drift check | Passed after regeneration. |

The slab and film resistances are 0.40 K/W and 0.10 K/W; a 50 K difference gives 100 W. The transient section states the Biot screening assumption and when a spatial model is needed. These same-AI checks are not independent heat-transfer, accessibility or domain review.

## Previous increment: Thermodynamics & Transport in Bioengineering 0.4.3 (2026-10-10)

Expanded week 9 with Reynolds scaling, characteristic-length conventions, fully developed Poiseuille flow, radius sensitivity, network resistance and limits for microvascular suspensions. Mapped both objectives to outcomes 3 and 4, and added a Reynolds-limit interpretation item while preserving the existing numeric prompts and keys. MIT OpenCourseWare microfluidics and fluid-mechanics resources are link-only. One compact reading remains in week 12; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Thermodynamics & Transport focused regression | 6 passed. |
| Ruff on the focused regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,242 questions, 1,276 cards and 25 cases; 0 errors and 1 disclosed depth warning. |
| Assessment-candidate report drift check | Passed after regeneration. |

The ideal tube example gives Q≈2.45×10⁻⁸ m³/s, and the micro-scale Reynolds example gives 0.1; the text states where those assumptions do not generalize. These same-AI checks are not independent fluid-mechanics, accessibility or domain review.

## Previous increment: Thermodynamics & Transport in Bioengineering 0.4.2 (2026-10-10)

Expanded week 3 with Fickian flux direction, transient diffusion, boundary conditions, diffusion and reaction time scales, the Damköhler comparison, reaction-diffusion length, and model limits. Mapped both objectives to outcomes 2 and 4, aligned the preserved diffusion-time check to time-scale comparison, and added direct flux-direction and regime items. Existing numeric prompts and keys are unchanged. MIT OpenCourseWare 10.37 Lecture 20 is link-only. Two compact readings remained in weeks 9 and 12; the course was partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Thermodynamics & Transport focused regression | 4 passed. |
| Ruff on the focused regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,241 questions, 1,276 cards and 25 cases; 0 errors and 2 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

For D=2×10⁻⁹ m²/s, L=200 μm and k=0.05 s⁻¹, the example gives tD=tR=20 s, Da≈1 and λ=200 μm. These same-AI checks are not independent transport, accessibility or domain review.

## Current increment: Thermodynamics & Transport in Bioengineering 0.4.2 (2026-10-10)

Expanded week 3 with Fickian flux direction, transient diffusion, boundary conditions, diffusion and reaction time scales, the Damköhler comparison, reaction-diffusion length, and model limits. Mapped both objectives to outcomes 2 and 4, aligned the preserved diffusion-time check to time-scale comparison, and added direct flux-direction and regime items. Existing numeric prompts and keys are unchanged. MIT OpenCourseWare 10.37 Lecture 20 is link-only. Two compact readings remain in weeks 9 and 12; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Thermodynamics & Transport focused regression | 4 passed. |
| Ruff on the focused regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,241 questions, 1,276 cards and 25 cases; 0 errors and 2 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

For D=2×10⁻⁹ m²/s, L=200 μm and k=0.05 s⁻¹, the example gives tD=tR=20 s, Da≈1 and λ=200 μm. These same-AI checks are not independent transport, accessibility or domain review.

## Previous increment: Thermodynamics & Transport in Bioengineering 0.4.1 (2026-10-10)

Expanded week 1 with control-volume selection, species and total-mass balances, accumulation, residence time, transient and steady state, reaction terms, and the signed open-system energy balance. Mapped both objectives and the assessment to outcome 1. Added a required-unit steady-flow energy item; existing concentration and mass-accumulation prompts and keys are unchanged. MIT OpenCourseWare Unified Engineering thermodynamics notes are link-only. Three compact readings remained in weeks 3, 9 and 12; the course was partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Thermodynamics & Transport focused regression | 2 passed. |
| Ruff on the focused regression source | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,239 questions, 1,276 cards and 25 cases; 0 errors and 3 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

The synthetic tank reaches 2.5 g/L at steady state with first-order consumption; the separate steady-flow energy example requires +10 kW heat into the control volume. These same-AI checks are not independent thermodynamics, accessibility or domain review.

## Previous increment: Probability, Biostatistics & Experimental Design 0.4.4 (2026-10-10)

Expanded week 8 with assignment and observational units, randomization, blocking, nested replication, regression representation of the design, residual diagnostics and reproducibility. Mapped both objectives and the assessment to outcomes 1, 2 and 4. Corrected the preserved sample-size item's objective association and added a blocked-randomization item so both objectives have direct practice evidence; existing prompts and keys remain unchanged. MIT OpenCourseWare Reading 26 and a PLOS Biology experimental-unit paper are link-only. All four readings migrated from the prototype now have expanded instruction; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Probability, Biostatistics & Experimental Design focused regression | 8 passed. |
| Ruff on the focused regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,238 questions, 1,276 cards and 25 cases; 0 errors and 4 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

The synthetic blocked example allocates three units from each condition to each processing-day block. The independent sample size is 24 donor-derived units, not the nested cell or well measurements. These same-AI checks are not independent statistics, accessibility or domain review.

## Previous increment: Probability, Biostatistics & Experimental Design 0.4.3 (2026-10-10)

Expanded week 6 with NHST assumptions, p-value interpretation, error and power, family-wise multiplicity, Bonferroni and confirmatory versus exploratory analysis. Corrected the preserved ten-test FWER objective link and added a direct p-value check while keeping both existing numeric prompts and keys. Both objectives and assessment map to outcomes 2 and 3. The focused Statistics suite passed 6 tests and Ruff passed. Full validation passed (25 courses, 384 lessons, 2,237 questions, 1,276 cards and 25 cases; 0 errors, 5 disclosed depth warnings); the assessment-candidate report was regenerated and its drift check passed. MIT OpenCourseWare 18.05 NHST II and Problem Set 9 Solutions are link-only references. These checks are not independent statistical, accessibility or domain review; one compact reading remained and the course was partial, unreviewed and formative-only.

## Previous increment: Probability, Biostatistics & Experimental Design 0.4.2 (2026-10-10)

Expanded week 4 with repeated-sampling interval coverage, a paired t-interval example, effect-size scales, practical thresholds, bias limits and regression to the mean. Mapped both objectives and the unchanged questions to outcome 3. The focused regression passed 4 tests; Ruff passed. Full validation passed (25 courses, 384 lessons, 2,236 questions, 1,276 cards and 25 cases; 0 errors, 6 disclosed depth warnings); the assessment-candidate report was regenerated and its drift check passed. MIT OpenCourseWare 18.05 Reading 23a is a link-only reference. These checks are not independent statistics, accessibility or domain review; two compact readings remained and the course was partial, unreviewed and formative-only.

## Previous increment: Statics & Mechanics of Materials 0.4.4 (2026-10-10)

Expanded week 8 with yield, ultimate tensile strength, fracture, fatigue, and functional failure; capacity-to-demand ratios; explicit terminology for pre-factored allowables; and uncertainty limits. Corrected the preserved allowable-to-demand item's objective association without changing its prompt or answer, then added a criterion-discrimination practice item so both objectives have direct evidence. Both objectives and the assessment map to outcome 4. MIT OpenCourseWare's 2.001 Mechanics & Materials I lecture-notes page is link-only; no source assets were copied or adapted. All four original prototype readings now have expanded instruction, but the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Statics & Mechanics of Materials focused regression suite | 8 passed. |
| Ruff on the Statics regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,235 questions, 1,276 cards and 25 cases; 0 errors and 8 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

The preserved ratio items still calculate to 3 and 2.5; the new criterion item separates yield, ultimate, fatigue and functional criteria from probability claims about a factor. These same-AI checks are not independent mechanics, reliability, accessibility or safety review.

## Previous increment: Statics & Mechanics of Materials 0.4.3 (2026-10-10)

Expanded week 4 with elastic circular-shaft torsion and elementary beam bending, solid/hollow polar moments, the correct area second moment for a rectangular section, unit conversions, geometry sensitivity, and model limits. Corrected the preserved beam-location question's objective association without changing its prompt or key; added one public torsion calculation so both objectives have aligned practice. Both objectives and the assessment map to outcomes 2 and 3. MIT OpenCourseWare's 2.001 Mechanics & Materials I lecture-notes page is link-only; no source assets were copied or adapted. One compact reading remains in week 8, and the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Statics & Mechanics of Materials focused regression suite | 6 passed. |
| Ruff on the Statics regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,234 questions, 1,276 cards and 25 cases; 0 errors and 9 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculation reproduces `τmax = 6.37 MPa` for the added 20 mm shaft under 10 N·m; the preserved beam example remains 6 MPa. These same-AI checks are not independent mechanics, accessibility or safety review.

## Earlier increment: Statics & Mechanics of Materials 0.4.2 (2026-10-10)

Expanded week 3 with average axial stress, engineering strain, linear-elastic modulus, uniform-bar extension and stiffness, segmented-bar reasoning, unit conversions, and explicit geometry, boundary-condition, small-strain and material-response limits. The worked example reports stress, strain, extension and an independent axial-stiffness calculation with consistent N/mm units. Both objectives and the unchanged formative practice assessment map to outcomes 2 and 3. MIT OpenCourseWare's 2.001 Mechanics & Materials I lecture-notes page is a link-only reference; no source asset was copied or adapted. Existing question IDs, prompts and keys remain unchanged. Two compact readings remain in weeks 4 and 8; the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Statics & Mechanics of Materials focused regression suite | 4 passed. |
| Ruff on the Statics regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 10 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

The preserved stress items still calculate to 10 MPa and 40 MPa, and the bar example gives 0.1 mm extension. These same-AI checks are not independent mechanics, accessibility or safety review.

## Earlier increment: Statics & Mechanics of Materials 0.4.1 (2026-10-10)

Expanded week 1 with free-body diagrams, ideal support reactions, planar force and moment balance, beam reactions, load resultants, and determinacy and unit checks. Clarified both objectives and mapped them and the unchanged practice assessment to outcome 1. MIT OpenCourseWare's static-equilibrium lecture-notes page is a link-only reference. Existing central-load and off-center reaction questions, prompts and keys are unchanged. Three compact readings remain; the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Statics & Mechanics of Materials focused regression suite | 2 passed. |
| Ruff on the Statics regression source | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 11 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent equilibrium calculations reproduce 300 N at either support for a centered load and 50 N at the right support for the offset load. These same-AI checks are not independent statics, accessibility or safety review.

## Previous increment: Signals, Systems & Feedback Control 0.4.4 (2026-10-10)

Expanded week 12 with P/I/D action, integral offset removal, windup under saturation, anti-windup, derivative noise, sample-and-hold, quantization and timing limits. Clarified both objectives and mapped them and the unchanged practice assessment to outcomes 3 and 4. Two MIT OpenCourseWare pages are link-only references. Existing integral-action and windup questions, prompts, options and keys are unchanged. All four preserved prototype readings now have expanded instruction; the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Signals, Systems & Feedback Control focused regression suite | 8 passed. |
| Ruff on the Signals regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 12 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

The preserved items still key integral action for steady offset and windup after actuator saturation. These same-AI checks do not provide independent control-systems, safety or accessibility review.

## Previous increment: Signals, Systems & Feedback Control 0.4.3 (2026-10-10)

Expanded week 8 with negative-unity-feedback algebra, characteristic roots, sensitivity and disturbance paths, nominal stability versus performance, model uncertainty, and the preserved gain-margin calculation. Clarified both objectives and mapped them and the unchanged practice assessment to outcomes 1, 3 and 4. Two MIT OpenCourseWare lecture pages are link-only references. Existing unity-feedback and gain-margin questions, prompts and keys are unchanged. One compact reading remains; the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Signals, Systems & Feedback Control focused regression suite | 6 passed. |
| Ruff on the Signals regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 13 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent algebra reproduces the negative unity-feedback transfer `G/(1+G)` and the specified nominal gain-margin factor `1/0.4 = 2.5`. These same-AI checks are not independent controls or accessibility review.

## Previous increment: Signals, Systems & Feedback Control 0.4.2 (2026-10-10)

Expanded week 4 with sinusoidal magnitude and phase, first-order low-pass cutoff and decibel level, anti-alias filtering before sampling, and a worked alias calculation. Clarified both objectives and mapped them and the unchanged practice assessment to outcomes 2 and 4. Two MIT OpenCourseWare lecture pages are link-only references. Existing cutoff and alias questions, prompts and keys are unchanged. Two compact readings remain; the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Signals, Systems & Feedback Control focused regression suite | 4 passed. |
| Ruff on the Signals regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 14 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations reproduce the cutoff 1/(2π × 0.05 s) ≈ 3.18 Hz and the 120 Hz-to-80 Hz alias at a 200 Hz sample rate. These same-AI checks are not independent controls or accessibility review.

## Previous increment: Signals, Systems & Feedback Control 0.4.1 (2026-10-10)

Expanded week 1 with LTI assumptions, impulse-response interpretation, zero-state transfer functions, first-order pole and DC-gain calculations, units, and model boundaries. Clarified both objectives and mapped them and the unchanged practice assessment to outcomes 1 and 2. Two MIT OpenCourseWare lecture pages are registered as link-only references. The original pole and gain questions, prompts, options and keys are unchanged. Three compact readings remain; the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Signals, Systems & Feedback Control focused regression suite | 2 passed. |
| Ruff on the Signals regression source | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 15 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations recover the pole s = −4 for the preserved pole item and steady-state gain 3 for the first-order equation. These same-AI checks are not independent controls or accessibility review.

## Previous increment: Physics: Mechanics for Biomedical Engineers 0.4.4 (2026-10-10)

Expanded week 9 with perpendicular moment arms, signed torque about a stated axis, stress/strain definitions, small-strain modulus calculations and explicit model limits. Clarified both objectives and mapped them and the unchanged practice assessment to outcomes 3 and 4. OpenStax's torque section is a link-only reference; the existing stress/strain section is reused. Existing question IDs, prompts, answer keys and cards are unchanged. All 13 readings now have substantive instruction beside the synthetic data lab. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physics: Mechanics focused regression suite | 103 passed. |
| Ruff on the Physics: Mechanics regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 16 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations recover −6 N·m under the stated clockwise-negative convention and dimensionless strain 0.0025. These same-AI checks are not independent physics or accessibility review.

## Previous increment: Physics: Mechanics for Biomedical Engineers 0.4.3 (2026-10-10)

Expanded week 6 with signed momentum, conditions for momentum conservation, force–time area, impulse–momentum balance, and the distinction between momentum and kinetic-energy conservation. Clarified both objectives and mapped them and the unchanged practice assessment to outcomes 2 and 4. Three OpenStax University Physics Volume 1 sections are registered as link-only references. Existing question IDs, prompts, answer keys and cards are unchanged; one compact reading remains in week 9. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physics: Mechanics focused regression suite | 101 passed. |
| Ruff on the Physics: Mechanics regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 17 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations recover +1.0 m/s for the post-collision cart pair, +2.0 N·s for the triangular pulse, and −1.8 N·s for the ball's velocity reversal. These same-AI checks are not independent physics or accessibility review.

## Previous increment: Physics: Mechanics for Biomedical Engineers 0.4.2 (2026-10-10)

Expanded week 4 with kinetic energy, the work–energy theorem, gravitational and spring potential energy, conservative and dissipative transfers, and power. Clarified both objectives and mapped them and the unchanged practice assessment to outcomes 2 and 4. Four OpenStax University Physics Volume 1 sections are registered as link-only references. Existing question IDs, prompts, answer keys and cards are unchanged; compact readings remain in weeks 6 and 9. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physics: Mechanics focused regression suite | 99 passed. |
| Ruff on the Physics: Mechanics regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 18 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations recover 9 J for the 2 kg object at 3 m/s, and 34.1 J as the difference between 98.1 J initial gravitational potential and 64.0 J final translational kinetic energy. These same-AI checks are not independent physics or accessibility review.

## Previous increment: Physics: Mechanics for Biomedical Engineers 0.4.1 (2026-10-10)

Expanded week 1 with motion variables, free-body diagram boundaries, Newton's second law, incline-force components, and unit and limiting-case checks. Clarified both objectives and mapped them and the unchanged practice assessment to outcomes 1, 2 and 4. Three OpenStax University Physics Volume 1 sections are registered as link-only references. Existing question IDs, prompts, answer keys and cards are unchanged; compact readings remain in weeks 4, 6 and 9. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physics: Mechanics focused regression suite | 97 passed. |
| Ruff on the Physics: Mechanics regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 19 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations recover 4 m/s² for a 3 kg cart with a 12 N net force, and 4.905 m/s² for a frictionless incline at 30°. These same-AI checks are not independent physics or accessibility review.

## Previous increment: Physics: Electricity & Magnetism 0.4.4 (2026-10-10)

Expanded week 12 with a bounded electrode-interface model, resistance-divider loading, differential measurement, frequency-dependent impedance intuition, and limits on interpreting baseline drift. Clarified both objectives and mapped them and the unchanged practice assessment to outcome 4. OpenStax AC circuits and a PubMed-indexed electrode-interface review are registered as link-only references. Existing question IDs, prompts, answer keys and cards are unchanged; all 13 readings now have substantive instruction. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physics II focused regression suite | 111 passed. |
| Ruff on the Physics II regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 20 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations recover 0.90 for a 1 MΩ source and 9 MΩ input, 0.50 for equal resistances, and about 0.9901 when the input is 100 times the source resistance. These same-AI checks are not independent physics or accessibility review.

## Previous increment: Physics: Electricity & Magnetism 0.4.3 (2026-10-10)

Expanded week 8 with Lorentz-force direction and work limits, current-segment force, magnetic flux and orientation, Faraday emf magnitude, Lenz-law direction, and the distinction between induced emf and closed-path current. Clarified both objectives and mapped them and the unchanged practice assessment to outcome 3. Three OpenStax University Physics Volume 2 sections are registered as link-only references. Existing question IDs, prompts, answer keys and cards are unchanged; one compact reading remains in week 12. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physics II focused regression suite | 109 passed. |
| Ruff on the Physics II regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 21 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations recover 10 V for a 50-turn coil with a 0.004 Wb per-turn change over 0.02 s, and 1.0 V for a 0.002 Wb change over 0.10 s. These same-AI checks are not independent physics or accessibility review.

## Previous increment: Physics: Electricity & Magnetism 0.4.2 (2026-10-10)

Expanded week 5 with current and resistance definitions, Ohm's-law operating limits, RC time-constant units, ideal charging and discharging, interpretation of the one-τ fraction, and instrument-loading limits. Clarified both objectives and mapped them and the unchanged practice assessment to outcome 2. Three OpenStax University Physics Volume 2 sections are registered as link-only references. Existing question IDs, prompts, answer keys and cards are unchanged; compact readings remain in weeks 8 and 12. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physics II focused regression suite | 107 passed. |
| Ruff on the Physics II regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 22 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations confirm τ = 10 ms for 2 kΩ and 5 μF, and V꜀(2 ms) ≈ 4.323 V for the 1 ms charging model. These same-AI checks are not independent physics or accessibility review.

## Previous increment: Physics: Electricity & Magnetism 0.4.1 (2026-10-10)

Expanded week 1 with potential-versus-energy distinctions, field-direction signs, conductor equilibrium, parallel-plate capacitance and capacitor energy. Clarified both objectives and mapped them and the unchanged practice assessment to outcome 1. Three OpenStax University Physics Volume 2 sections are registered as link-only references. Existing question IDs, prompts, answer keys and cards are unchanged; compact readings remain in weeks 5, 8 and 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Physics II focused regression suite | 105 passed. |
| Ruff on the Physics II regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 23 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent calculations confirm the preserved energies, 45 μJ and 1.0×10⁻⁴ J. These same-AI checks are not independent physics or accessibility review.

## Previous increment: General Chemistry II 0.4.4 (2026-10-10)

Expanded week 12 with coordination-sphere and donor-atom accounting, formal oxidation-state bookkeeping, geometry constraints, ligand-field and spin qualifications, and protein-environment effects on metal behavior. Clarified both objectives and mapped them and the unchanged practice assessment to outcome 4. One OpenStax Chemistry 2e coordination reference is registered as link-only and the existing ligand-field source is reused. Existing question IDs, prompts, answer keys and cards are unchanged; all four compact prototype readings now have expanded instruction. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry II focused regression suite | 7 passed. |
| Ruff on the General Chemistry II regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 24 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Checks cover charge bookkeeping, donor counts, geometry qualifications, both preserved answer keys and link-only source permissions. These same-AI checks are not independent chemistry or accessibility review.

## Previous increment: General Chemistry II 0.4.3 (2026-10-10)

Expanded week 9 with galvanic-cell components, electrode and cell-potential conventions, electron-flow direction, standard-state assumptions, ΔG° calculations, and a brief Nernst bridge. Clarified both objectives and mapped them and the unchanged practice assessment to outcome 3. Three OpenStax Chemistry 2e electrochemistry pages are registered as link-only sources. Existing question IDs, prompts, answer keys and cards are unchanged. One compact prototype reading remains in week 12; the course stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry II focused regression suite | 5 passed. |
| Ruff on the General Chemistry II regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 25 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

Independent arithmetic checks recover ΔG° = −57.9 kJ/mol for the preserved 0.30 V item and E°cell = +1.10 V for the Cu/Zn cell. These same-AI checks are not independent chemistry or accessibility review.

## Previous increment: General Chemistry II 0.4.2 (2026-10-10)

Expanded week 5 with controlled initial-rate comparisons, empirical rate-law units, a two-temperature Arrhenius calculation, mechanism constraints, catalysis and a limited first-order half-life example. Clarified objective 1 to cover the preserved half-life item, linked both objectives and the unchanged practice assessment to outcome 2, and registered four new OpenStax Chemistry 2e pages as link-only sources while reusing the mechanism source. Existing question IDs, prompts, answer keys and cards are unchanged. Two compact prototype readings remain in weeks 9 and 12; the course stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry II focused regression suite | 3 passed. |
| Ruff on the General Chemistry II regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 26 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

The half-life and Arrhenius calculations were independently recomputed in regression tests, and reference reuse permissions were checked. These same-AI checks are not independent chemistry or accessibility review.

## Previous increment: General Chemistry I 0.4.4 (2026-10-10)

The module-4/week-11 reading now develops dynamic equilibrium, reaction quotients, Q/K direction, concentration disturbances, temperature dependence and catalyst limits. The first objective now describes Q/K interpretation; the first question maps to both interpretation and direction prediction. Both objectives and the practice assessment map to outcome 3. Three OpenStax Chemistry 2e sections are link-only references. Prompts, IDs and keys are unchanged. All four original compact prototype readings now have expanded instruction; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry I focused regression suite | 4 passed. |
| Ruff on the General Chemistry I regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 27 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Current increment: General Chemistry I 0.4.3 (2026-10-10)

The module-3/week-8 reading now establishes heat/work signs, calorimetry balances, state-function reasoning, Hess’s law and reaction enthalpies from formation values. The first objective now describes sign interpretation; the first question maps to both sign interpretation and enthalpy calculation. Both objectives and the practice assessment map to outcomes 3 and 4. Two OpenStax Chemistry 2e sections are link-only references. Prompts, IDs and keyed answers are unchanged. Compact readings remain in weeks 4 and 11; the course stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry I focused regression suite | 3 passed. |
| Ruff on the General Chemistry I regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 28 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Current increment: General Chemistry I 0.4.2 (2026-10-10)

The module-2/week-4 reading now develops mole-ratio calculations, limiting reagents, theoretical yield, molarity and dilution with explicit unit and assumption checks. The dilution item now maps to its dilution objective; the limiting-reagent item maps to equation-stoichiometry and limiting-reagent objectives. Both objectives and the practice assessment map to outcomes 1 and 4. Three OpenStax Chemistry 2e sections are link-only references. Question IDs, prompts and keys are unchanged. The course remains partial, unreviewed and formative-only, with compact readings in weeks 8 and 11.

| Actual command/check | Result |
| --- | --- |
| General Chemistry I focused regression suite | 2 passed. |
| Ruff on the General Chemistry I regression sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 29 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Current increment: Organic Chemistry I for Life Sciences 0.4.4 (2026-10-10)

The week-9 reading now explains carbonyl polarity and charge changes through nucleophilic addition, then distinguishes net addition from acyl substitution by checking the attached substituent and its ability to leave. Both objectives and the practice assessment map to outcomes 1 and 4. Two primary OpenStax sections are registered as link-only references. Existing questions, answer keys and cards are unchanged. All four compact prototype readings have expanded instruction; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Organic Chemistry regression and recalculation suite | 92 passed. |
| Ruff on the changed Organic Chemistry test sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 30 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Current increment: Organic Chemistry I for Life Sciences 0.4.3 (2026-10-10)

The week-7 reading now distinguishes E1, E2 and E1cB, relates mechanisms to simple rate laws, and treats beta-hydrogen inventory, anti-periplanar alignment, cyclohexane trans-diaxial geometry and qualified Zaitsev predictions. Both objectives and the practice assessment map to outcomes 2 and 3. Four primary OpenStax sections are registered as link-only references. Existing questions, answer keys and cards are unchanged. One compact reading remains in week 9; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Organic Chemistry regression and recalculation suite | 91 passed. |
| Ruff on the changed Organic Chemistry test sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 31 disclosed depth warnings. |
| Assessment-candidate report drift check | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Current increment: Organic Chemistry I for Life Sciences 0.4.2 (2026-10-10)

The week-5 reading now compares SN1 and SN2 mechanism evidence, simple rate laws, synthetic concentration changes, and geometric versus descriptor-level stereochemistry. Both objectives and the practice assessment map to outcomes 2 and 3. Four primary OpenStax sections are registered as link-only references. Existing questions, answer keys and cards are unchanged. Two compact readings remain in weeks 7 and 9; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Organic Chemistry regression and recalculation suite | 90 passed. |
| Ruff on the changed Organic Chemistry test sources | Passed. |
| python tools/validate_content.py --root . | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 32 disclosed depth warnings. |
| Assessment-candidate report --check | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Current increment: Organic Chemistry I for Life Sciences 0.4.1 (2026-10-10)

The week-1 reading now compares acidity through conjugate-base stability, checks resonance electron movement and formal charge, and distinguishes pKa equilibrium estimates from reaction rates. Both objectives and the practice assessment map to outcome 1. Two OpenStax pages are registered as link-only references. Existing questions, answers and cards are unchanged. Three compact readings remain in weeks 5, 7 and 9; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Organic Chemistry regression and recalculation suite | 89 passed. |
| Ruff on the changed Organic Chemistry test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 33 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Current increment: Linear Algebra for Modeling & Robotics 0.3.4 (2026-10-10)

The week-4 reading now derives least squares, works a synthetic overdetermined fit, checks residual orthogonality, and covers diagnostics and numerical limits. Both objectives and the practice assessment map to outcome 4. Existing prompts, answers and cards are unchanged. All four compact legacy readings now have expanded instruction; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Linear Algebra regression and recalculation suite | 82 passed. |
| Ruff on the changed Linear Algebra test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 34 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent mathematics or accessibility review.

## Current increment: Linear Algebra for Modeling & Robotics 0.3.3 (2026-10-10)

The week-7 reading now explains eigenmodes in discrete and continuous systems, stability conditions, transition matrices and local linearization. Its first objective was clarified to match the existing continuous-time stability question; both objectives and the practice assessment map to outcome 3. Existing answers and cards are unchanged. All four original compact prototype readings now have expanded instruction; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Linear Algebra regression and recalculation suite | 81 passed. |
| Ruff on the changed Linear Algebra test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 35 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent mathematics or accessibility review.

## Current increment: Linear Algebra for Modeling & Robotics 0.3.2 (2026-10-10)

The week-2 reading now develops span, independence, basis matrices and coordinate conversion; it distinguishes active rotation from changing coordinate frames. Both objectives and the practice assessment map to outcome 2. Existing questions, answer keys and cards are unchanged. Two compact readings remain in weeks 4 and 7; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Linear Algebra regression and recalculation suite | 80 passed. |
| Ruff on the changed Linear Algebra test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 36 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent mathematics or accessibility review.

## Current increment: Linear Algebra for Modeling & Robotics 0.3.1 (2026-10-10)

The week-1 reading now works through elimination, rank, consistency and free-variable cases, and distinguishes exact singularity from numerical sensitivity. Both lesson objectives and the practice assessment map to outcomes 1 and 2. Questions, answer keys and cards are unchanged. Three compact readings remain in weeks 2, 4 and 7; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Linear Algebra regression and recalculation suite | 79 passed. |
| Ruff on the changed Linear Algebra test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 37 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent mathematics or accessibility review.

## Current increment: Geroscience & Regenerative Biology 0.5.6 (2026-10-10)

The week-11 lesson now distinguishes target engagement, function, mechanism and translational claims; includes synthetic survival, function and adverse-event data; and explains study-design controls. Existing objectives, questions, answer keys and cards are unchanged. All four compact legacy prototype readings now have expanded instruction. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Geroscience regression and content selection | 485 passed. |
| Ruff on the changed Geroscience test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 38 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent geroscience or accessibility review.

## Current increment: Geroscience & Regenerative Biology 0.5.5 (2026-10-10)

The week-8 lesson now distinguishes stem-cell abundance from regenerative functions, explains niche and systemic context, compares assays, and uses a synthetic factorial example to reason about donor-cell and recipient-environment age. Existing objectives, questions, answer keys and cards are unchanged; one compact reading remains in week 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Geroscience regression and content selection | 484 passed. |
| Ruff on the changed Geroscience test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 39 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent geroscience or accessibility review.

## Current increment: Geroscience & Regenerative Biology 0.5.4 (2026-10-10)

The week-5 lesson now defines senescence with convergent cell-state evidence, checks a synthetic marker-classification example, and explains how tissue context affects interpretation of secretory signals. Existing objectives, questions, answer keys and cards are unchanged; two compact readings remain in weeks 8 and 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Geroscience regression and content selection | 483 passed. |
| Ruff on the changed Geroscience test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 40 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent geroscience or accessibility review.

## Current increment: Geroscience & Regenerative Biology 0.5.3 (2026-10-10)

The week-1 lesson now develops interacting damage, maintenance and adaptation models, a damage-balance equation, and the distinction between marker change and functional benefit. Existing objectives, questions, answer keys and cards are unchanged; three compact readings remain in weeks 5, 8 and 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Geroscience regression and content selection | 482 passed. |
| Ruff on the changed Geroscience test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 41 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent geroscience or accessibility review.

## Current increment: Genetics & Genomics 0.5.4 (2026-10-10)

The week-11 reading now develops association effect size and uncertainty, multiple-testing and population-context checks, LD and fine-mapping limits, and the distinction between statistical and functional evidence. Added one link-only primary reference. Both objectives and the assessment map to outcome 3; questions, keys and cards are unchanged. All four prototype readings now have expanded instruction; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Genetics regression and content selection | 485 passed. |
| Ruff on the changed Genetics test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 42 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent genetics or accessibility review.

## Current increment: Genetics & Genomics 0.5.3 (2026-10-10)

The week-9 lesson now develops cis/trans regulatory reasoning, synthetic allele-specific expression, controlled perturbation and rescue evidence, and limits on causal claims. Added two link-only primary references. Lesson objectives and the practice assessment map to outcomes 3 and 4; earlier expanded Genetics practice assessments now also list their mapped outcomes. Existing questions, keys and cards are unchanged. One compact reading remains in week 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Genetics regression and content selection | 484 passed. |
| Ruff on the changed Genetics test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 43 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent genetics or accessibility review.

## Current increment: Genetics & Genomics 0.5.2 (2026-10-10)

The week-4 lesson now develops testcross phase identification, recombination-frequency estimation, sampling uncertainty, the short-interval centimorgan convention, and the limits imposed by hidden double crossovers and the 0.5 ceiling. Both existing objectives link to the linkage/recombination outcome; practice items, keys and cards are unchanged. Two compact readings remain in weeks 9 and 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Genetics regression and content selection | 483 passed. |
| Ruff on the changed Genetics test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 44 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent genetics or accessibility review.

## Current increment: Genetics & Genomics 0.5.1 (2026-10-10)

The week-1 lesson now develops Mendelian genotype probabilities, an unaffected-sibling Bayes update, penetrance limits and genotype-versus-phenotype frequencies. Both existing objectives link to the genotype-probability outcome; existing practice items, keys and cards are unchanged. Three compact readings remain in weeks 4, 9 and 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Genetics regression and content selection | 482 passed. |
| Ruff on the changed Genetics test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 45 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent genetics or accessibility review.

## Current increment: General Chemistry II 0.4.1 (2026-10-10)

The week-1 reading now develops weak-acid equilibrium, the qualified Henderson–Hasselbalch relation, stoichiometric buffer updates and total-concentration-dependent capacity. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 5, 9 and 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry II regression/content suite | 835 passed. |
| Ruff on the changed General Chemistry II test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 46 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Current increment: General Chemistry I 0.4.1 (2026-10-10)

The week-1 reading now links electron configuration and periodic trends to Lewis structures, formal charge, electron-domain/molecular geometry and molecular polarity, with explicit model limits. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 4, 8 and 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| General Chemistry I regression/content suite | 734 passed. |
| Ruff on the changed General Chemistry I test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 47 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent chemistry or accessibility review.

## Previous increment: Differential Equations for Living & Engineered Systems 0.3.5 (2026-10-10)

The week-11 numerical-methods reading now explains the Euler step, stability versus accuracy, strict decay and positivity limits, refinement, and stiffness. The Euler item wording was clarified to ask for the stability boundary; its 0.04 s answer key and other keys/objectives are unchanged. All four original compact readings have expanded instruction; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Differential Equations regression/content selection | 103 passed; 1,115 unrelated checks were deselected. |
| Ruff on the changed Differential Equations test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 48 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent mathematics, engineering or accessibility review.

## Current increment: Differential Equations for Living & Engineered Systems 0.3.4 (2026-10-10)

The week-6 reading now develops equilibrium linearization, Jacobian/eigenvalue behavior, nullclines, local classifications and limits on nonhyperbolic or global conclusions. Existing questions, keys and objectives are unchanged; one compact reading remains in week 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Differential Equations regression/content selection | 102 passed; 1,115 unrelated checks were deselected. |
| Ruff on the changed Differential Equations test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 49 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent mathematics, engineering or accessibility review.

## Current increment: Differential Equations for Living & Engineered Systems 0.3.3 (2026-10-10)

The week-4 reading now derives the mass–spring–damper equation, explains natural frequency, damping ratio and response classes, and states the initial-condition and model assumptions. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 6 and 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Differential Equations regression/content selection | 101 passed; 1,115 unrelated checks were deselected. |
| Ruff on the changed Differential Equations test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 50 disclosed depth warnings. |
| Assessment-candidate report `--check` | Pending final check after regeneration. |

These same-AI checks are not independent mathematics, engineering or accessibility review.

## Current increment: Differential Equations for Living & Engineered Systems 0.3.2 (2026-10-10)

The week-1 reading now derives the first-order relaxation solution, gives the integrating-factor form, explains initial conditions and stability, and interprets time constants with units and examples. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 4, 6 and 11. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Differential Equations regression/content selection | 100 passed; 1,115 unrelated checks were deselected. |
| Ruff on the changed Differential Equations test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 51 disclosed depth warnings. |
| Assessment-candidate report `--check` | Pending final check after regeneration. |

These same-AI checks are not independent mathematics, engineering or accessibility review.

## Current increment: Cellular Biomechanics & Mechanobiology 0.3.4 (2026-10-10)

The week-10 reading now works through factorial contrasts and interactions, defines the independent experimental unit, and addresses nested replicates, material verification, blocking and randomization. Existing questions, keys and objectives are unchanged; all four former compact readings now have expanded primers. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Cellular Biomechanics regression/content selection | 72 passed; 1,146 unrelated checks were deselected. |
| Ruff on the changed Cellular Biomechanics test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 52 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent biomechanics, biomedical, clinical or accessibility review.

## Current increment: Cellular Biomechanics & Mechanobiology 0.3.3 (2026-10-10)

The week-8 reading now separates mechanical input, sensor, intermediate response and function; it also distinguishes necessity, sufficiency, rescue and direct-interaction evidence. Existing questions, keys and objectives are unchanged; one compact reading remains in week 10. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Cellular Biomechanics regression/content selection | 71 passed; 1,146 unrelated checks were deselected. |
| Ruff on the changed Cellular Biomechanics test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 54 disclosed depth warnings. |
| Assessment-candidate report `--check` | Pending final check after regeneration. |

These same-AI checks are not independent biomechanics, biomedical, clinical or accessibility review.

## Current increment: Cellular Biomechanics & Mechanobiology 0.3.2 (2026-10-10)

The week-5 reading now explains the matrix–integrin–cytoskeleton load path, distinguishes ligand area from local geometry, and qualifies traction-force inference. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 8 and 10. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Cellular Biomechanics regression/content selection | 70 passed; 1,146 unrelated checks were deselected. |
| Ruff on the changed Cellular Biomechanics test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 54 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent biomechanics, biomedical, clinical or accessibility review.

## Current increment: Cellular Biomechanics & Mechanobiology 0.3.1 (2026-10-10)

The week-1 mechanics reading now develops stress and strain from force/displacement, distinguishes modulus from specimen stiffness, explains relaxation versus creep and compares idealized viscoelastic models. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 5, 8 and 10. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Cellular Biomechanics regression/content selection | 69 passed; 1,146 unrelated checks were deselected. |
| Ruff on the changed Cellular Biomechanics test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 55 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent biomechanics, biomedical, clinical or accessibility review.

## Previous increment: Bioreactors & Tissue Culture Engineering 0.4.4 (2026-10-10)

The week-12 reading now explains the parameter-to-quality chain, feedback-sensor limits, trend interpretation, predeclared acceptance criteria and traceable monitoring records. Existing questions, keys and objectives are unchanged; all four original compact readings have expanded primers. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Bioreactors-specific regression selection | 74 passed; 663 unrelated parameterized checks were deselected. |
| Ruff on the changed Bioreactors test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 56 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent bioprocess, biomedical, clinical or accessibility review.

## Current increment: Bioreactors & Tissue Culture Engineering 0.4.3 (2026-10-10)

The week-9 reading now explains mixing and scale-up criteria, compares idealized geometric scaling, connects local gradients to cell exposure, and qualifies scale-down inference. Existing questions, keys and objectives are unchanged; one compact reading remains in week 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Bioreactors-specific regression selection | 73 passed; 663 unrelated parameterized checks were deselected. |
| Ruff on the changed Bioreactors test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 57 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed after regeneration. |

These same-AI checks are not independent bioprocess, biomedical, clinical or accessibility review.

## Current increment: Bioreactors & Tissue Culture Engineering 0.4.2 (2026-10-10)

The week-5 oxygen reading now relates gas–liquid transfer, cellular uptake and dissolved concentration through a unit-aware dynamic balance. It distinguishes target-level capacity from maximum transfer and explains bulk-measurement limits. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 9 and 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Bioreactors-specific regression selection | 72 passed; 663 unrelated parameterized checks were deselected. |
| Ruff on the changed Bioreactors test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 58 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks are not independent bioprocess, biomedical, clinical or accessibility review.

## Current increment: Bioreactors & Tissue Culture Engineering 0.4.1 (2026-10-10)

The week-1 reading now develops interval-specific exponential growth, viable-cell versus total-cell balance, loss terms and substrate/product balances. Existing questions, keys and objectives are unchanged; three compact readings remain in weeks 5, 9 and 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Bioreactors-specific regression selection | 71 passed; 663 unrelated parameterized checks were deselected. |
| Ruff on the changed Bioreactors test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 59 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks are not independent bioprocess, biomedical, clinical or accessibility review.

## Previous increment: Biomaterials & Tissue Engineering 0.3.4 (2026-10-10)

The week-13 reading now develops application-specific biocompatibility, evidence scope, failure-mode categories, causal comparisons and manufacturing/time considerations. Existing questions, keys and objectives are unchanged. All four original prototype readings have expanded primers; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biomaterials-specific regression selection | 68 passed; 669 unrelated parameterized checks were deselected. |
| Ruff on the changed Biomaterials test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 60 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks are not independent biomaterials, biomedical, clinical or accessibility review.

## Current increment: Biomaterials & Tissue Engineering 0.3.3 (2026-10-10)

The week-9 reading now maps tissue function to cell, scaffold, signal, mechanical environment and evidence. It also covers time-dependent conditions, controls, tissue-specific readouts and limits on in-vitro inference. Existing questions, keys and objectives are unchanged; one compact reading remains in week 13. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biomaterials-specific regression selection | 67 passed; 669 unrelated parameterized checks were deselected. |
| Ruff on the changed Biomaterials test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 61 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks are not independent biomaterials, biomedical, clinical or accessibility review.

## Current increment: Biomaterials & Tissue Engineering 0.3.2 (2026-10-10)

The week-3 reading now develops scaffold architecture, relative-density mechanics, distinct degradation measures, first-order mass/modulus models and load sharing with tissue formation. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 9 and 13. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biomaterials-specific regression selection | 66 passed; 669 unrelated parameterized checks were deselected. |
| Ruff on the changed Biomaterials test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 62 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks are not independent materials, biomedical, clinical or accessibility review.

## Current increment: Biomaterials & Tissue Engineering 0.3.1 (2026-10-10)

The week-1 reading now develops bulk/surface properties, contact-angle interpretation, protein presentation, mechanical modulus and time-dependent characterization. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 3, 9 and 13. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biomaterials-specific regression selection | 65 passed; 669 unrelated parameterized checks were deselected. |
| Ruff on the changed Biomaterials test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 63 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks are not independent biomaterials, clinical or accessibility review.

## Current increment: Biochemistry I 0.4.4 (2026-10-10)

The week-12 reading now develops pool/flux balances, control coefficients, isotope-tracing limits, regulatory layers and perturbation time scales. Existing questions, keys and objectives are unchanged. All four original prototype readings have expanded primers; the course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry-specific regression selection | 55 passed; 682 unrelated parameterized checks were deselected. |
| Ruff on the changed Biochemistry test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 64 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks are not independent biochemical, laboratory or accessibility review.

## Current increment: Biochemistry I 0.4.3 (2026-10-10)

The week-9 reading now develops carbon and redox bookkeeping, free-energy context, proton-motive-force coupling, uncoupling and qualified ATP-yield accounting. Existing questions, keys and objectives are unchanged; one compact prototype remains in week 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry-specific regression selection | 54 passed; 682 unrelated parameterized checks were deselected. |
| Ruff on the changed Biochemistry test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 65 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks are not independent biochemical, laboratory or accessibility review.

## Current increment: Biochemistry I 0.4.2 (2026-10-10)

The week-5 reading now develops catalytic strategies, Michaelis-Menten assumptions, inhibition patterns and catalytic efficiency. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 9 and 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry-specific regression selection | 53 passed; 682 unrelated parameterized checks were deselected. |
| Ruff on the changed Biochemistry test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 66 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks are not independent biochemical, laboratory or accessibility review.

## Current increment: Biochemistry I 0.4.1 (2026-10-10)

The week-1 reading now develops protein structural levels, folding interactions, binding occupancy and the distinction among affinity, specificity, cooperativity and binding pathways. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 5, 9 and 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Biochemistry-specific regression selection | 52 passed; 682 unrelated parameterized checks were deselected. |
| Ruff on the changed Biochemistry test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 67 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks are not independent biochemical, laboratory or accessibility review.

## Current increment: Human Physiology for Engineers 0.4.4 (2026-10-10)

The week-11 reading now develops clearance units, filtered-load balance, tubular-handling interpretation, feedback sensitivity and integrated amount balance. Existing questions, keys and objectives are unchanged. All four original prototype readings have expanded primers; the package remains partial, unreviewed and formative-only and gives no medical advice.

| Actual command/check | Result |
| --- | --- |
| Physiology-specific regression selection | 64 passed; 672 unrelated parameterized checks were deselected. |
| Ruff on the changed physiology test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 68 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks are not independent medical, physiology or accessibility review.

## Current increment: Human Physiology for Engineers 0.4.3 (2026-10-10)

The week-5 reading now develops pressure-flow resistance, pathway combinations, diffusion and ventilation-perfusion matching. Existing questions, keys and objectives are unchanged; one compact reading remains in week 11. The package remains partial, unreviewed and formative-only and gives no medical advice.

| Actual command/check | Result |
| --- | --- |
| Physiology-specific regression selection | 63 passed; 672 unrelated parameterized checks were deselected. |
| Ruff on the changed physiology test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 69 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks are not independent medical, physiology or accessibility review.

## Current increment: Human Physiology for Engineers 0.4.2 (2026-10-10)

The week-3 reading now develops current conventions, ionic driving force and passive multi-ion balance. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 5 and 11. The package remains partial, unreviewed and formative-only and gives no medical advice.

| Actual command/check | Result |
| --- | --- |
| Physiology-specific regression selection | 62 passed; 672 unrelated parameterized checks were deselected. |
| Ruff on the changed physiology test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 70 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks are not independent medical, physiology or accessibility review.

## Current increment: Human Physiology for Engineers 0.4.1 (2026-10-10)

The week-1 reading now develops a compartment balance, state-dependent clearance, feedback direction and response time. Existing questions, keys and objectives are unchanged; three compact readings remain in weeks 3, 5 and 11. The package remains partial, unreviewed and formative-only and gives no medical advice.

| Actual command/check | Result |
| --- | --- |
| Physiology-specific selection from the AI-assisted regression file, plus new feedback regression | 62 passed; 672 unrelated parameterized checks were deselected. |
| Ruff on the changed physiology test sources | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 71 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks are not independent medical, physiology or accessibility review.

## Previous increment: Electrical Circuits & Instrumentation 0.4.4 (2026-10-10)

The week-12 lesson now develops affine calibration inversion, uncertainty propagation, covariance assumptions and traceable range/condition reporting. Existing questions, keys and objectives are unchanged. All scheduled lessons have expanded or original instructional text; the package remains partial and formative-only, and its synthetic lab is not a full laboratory sequence.

| Actual command/check | Result |
| --- | --- |
| Focused Circuits regression file | 122 passed, including calibration inversion, standard-uncertainty and original-item checks. |
| Ruff on the changed Circuits test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 72 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks are not independent metrology, electrical-engineering or accessibility review.

## Current increment: Electrical Circuits & Instrumentation 0.4.3 (2026-10-10)

The week-7 reading now develops the first-order RC magnitude response, analog anti-alias filtering and alias equivalence, and qualifies the Nyquist boundary. Existing questions, keys and objectives are unchanged; one compact prototype reading remains in week 12. The package stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Circuits regression file | 121 passed, including cutoff response, alias equivalence and exact-boundary phase checks. |
| Ruff on the changed Circuits test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 73 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These checks do not validate a physical filter, ADC or acquisition system.

## Current increment: Electrical Circuits & Instrumentation 0.4.2 (2026-10-10)

The week-4 lesson now develops inverting and non-inverting gain, differential front-end context, unipolar ADC bias and real-amplifier limits. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 7 and 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Circuits regression file | 120 passed, including gain, reference bias and output-window calculations. |
| Ruff on the changed Circuits test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 74 disclosed depth warnings. |
| Assessment-candidate report regeneration and `--check` | Passed. |

These same-AI checks are not hardware, electrical-safety or accessibility review.

## Current increment: Electrical Circuits & Instrumentation 0.4.1 (2026-10-10)

The week-1 reading now develops KCL/KVL, Thevenin port equivalence, dependent-source resistance handling and finite meter loading. Existing questions, keys and objectives are unchanged; compact readings remain in weeks 4, 7 and 12. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Circuits regression file | 119 passed, including original-versus-Thevenin loaded-port calculations. |
| Ruff on the changed Circuits test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 75 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks do not validate physical hardware or safety functions.

## Previous increment: Programming & Numerical Methods 0.4.4 (2026-10-10)

The week-12 reading now develops paired displays, independent sample counts, interval definitions and scale choices through a constructed four-donor example. Existing questions, keys, objectives and counts are unchanged. All scheduled lessons have expanded or original instructional text; the synthetic data lab remains a single activity, not a laboratory sequence. The package stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Programming regression file | 107 passed, including paired mean, sample spread and interval calculations. |
| Ruff on the changed Programming test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 76 disclosed depth warnings. |
| Assessment-candidate report regeneration and `--check` | Passed. |

These same-AI checks are not independent statistical or accessibility review and do not establish an experimental effect.

## Current increment: Programming & Numerical Methods 0.4.3 (2026-10-10)

The week-10 lesson now distinguishes fit, residual and predictive uncertainty, and explains training-fold preprocessing and target-aware grouped validation. Existing questions, keys and objectives remain unchanged; one compact reading remains in week 12. The package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Programming regression file | 106 passed, including recomputation of residual standard error. |
| Ruff on the changed Programming test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 77 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These same-AI checks do not supply statistical, code, accessibility or dataset review.

## Current increment: Programming & Numerical Methods 0.4.2 (2026-10-10)

The week-7 reading now compares two quadrature rules and develops the forward-Euler recurrence, decay stability condition and limits of numerical tolerances. Existing public answers and keys are unchanged; compact readings remain in weeks 10 and 12. The course remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Programming regression file | 105 passed, including quadrature and Euler amplification checks. |
| Ruff on the changed Programming test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 78 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks do not provide independent numerical-methods review or evaluate learner-authored code.

## Current increment: Programming & Numerical Methods 0.4.1 (2026-10-10)

The week-1 reading now covers units and missing-data contracts, metadata-preserving structures, pure functions, hand-checkable examples and provenance. Existing questions, keys and objectives are unchanged; three compact readings remain. The course stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Programming regression file | 104 passed, including the 1.5 mg / 500 µL conversion. |
| Ruff on the changed Programming test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 79 disclosed depth warnings. |
| Assessment-candidate report regeneration | Passed. |

These same-AI checks do not run learner-authored code or supply biological, code or accessibility review.

## Current increment: Calculus III 0.4.4 (2026-10-10)

The week-10 lesson now derives work along an oriented curve, compares parameterized circulation with Green's theorem, develops Green's flux form, and distinguishes Green, Stokes and divergence theorem conditions. Existing questions, keys, objectives and item counts are unchanged. All scheduled lessons now have expanded or original instructional text; the package remains partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Calculus III regression file | 89 passed, including path reversal, Green circulation/flux and divergence-theorem checks. |
| Ruff on the changed Calculus III test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 80 disclosed depth warnings. |
| Assessment-candidate report regeneration and `--check` | Passed. |

These same-AI checks do not provide independent mathematical or accessibility review.

## Current increment: Calculus III 0.4.3 (2026-10-10)

The week-8 reading now develops the change-of-variables Jacobian, polar-coordinate area, region bounds and a unit-aware variable-density example. Existing questions, keys, objectives and item counts are unchanged; one compact prototype reading remains. The package stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Calculus III regression file | 88 passed, including polar/Cartesian area, linear-map Jacobian and radial-density checks. |
| Ruff on the changed Calculus III test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 81 disclosed depth warnings. |
| Assessment-candidate report regeneration and `--check` | Passed. |

These same-AI checks do not provide independent mathematical or biological review.

## Current increment: Calculus III 0.4.2 (2026-10-10)

The week-5 optimization lesson now distinguishes stationarity from classification, develops the Hessian test and its inconclusive case, and demonstrates a regular equality constraint with a direct global-bound check. Existing questions, keys, objectives and item counts are unchanged; two compact prototype readings remain. The package stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Calculus III regression file | 87 passed, including Hessian and constrained-bound calculations. |
| Ruff on the changed Calculus III test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 82 disclosed depth warnings. |
| Assessment-candidate report regeneration and `--check` | Passed. |

These same-AI checks do not provide independent mathematical or accessibility review.

## Current increment: Calculus III 0.4.1 (2026-10-10)

The week-1 vectors reading now develops coordinate partials, the gradient as a local linear model, unit-direction derivatives, level-curve geometry and the limits of finite-change predictions. Existing practice questions, keys, objectives and item counts are unchanged; three compact readings remain. The course stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Calculus III regression file | 86 passed, including centered-difference gradient and directional-change checks. |
| Ruff on the changed Calculus III test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 83 disclosed depth warnings. |
| Assessment-candidate report `--check` | Passed. |

These checks were authored with the content by the same AI assistant; they are not independent mathematical or accessibility review.

## Current increment: Robotics & Mechatronics 0.4.4 (2026-10-10)

Robotics' final compact reading now distinguishes a path from its time-scaled trajectory, treats frame and sensor readings as uncertain evidence, and works a static biased-measurement feedback update. It qualifies this calculation against dynamic behavior and states the limits of recovery claims. Existing practice keys, objectives and item counts remain unchanged. All scheduled lessons now have expanded or original instructional text; the package stays partial, unreviewed and formative-only.

| Actual command/check | Result |
| --- | --- |
| Focused Robotics regression file | 110 passed, including recomputation of static feedback residuals 0.9, 0.45 and 0.225. |
| Ruff on the changed Robotics test | Passed. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 84 disclosed depth warnings. |
| Assessment-candidate report regeneration and `--check` | Passed. |

These checks were authored with the content by the same AI assistant; they do not constitute independent academic, engineering or safety review.

The hosted validation recorded below covers Biology 0.34.0 and its published commit. The Biology 0.35.0 final-candidate revision, protected authored-form runtime and graded-source archive have focused local checks summarized here; they have not passed hosted CI or independent review.

## Current increment: manifest-selected practice bank and catalog router (2026-10-10)

Lesson question delivery now uses the optional `practice_question_bank` manifest field, with `question-banks/practice.json` retained as the default. The offline validator checks the selected bank and rejects unsafe paths. Read-only catalog, authentication, lesson, learner-state, retrieval, formative-attempt/history/appeal, and legacy instructor appeal routes are separated into routers with shared request dependencies; public URLs and response models remain unchanged. Biology remains partial and formative-only.

| Actual command/check | Result |
| --- | --- |
| API and repository tests in the rebuilt API image | 51 passed, including custom-bank delivery through the lesson API, existing catalog endpoints, and unsafe-reference rejection. |
| Retrieval and API route regressions after extraction | 59 passed, including due/new/upcoming queues, edited-card resets, CSRF, gradebook isolation and the learner route suite. |
| Full backend suite after auth-router extraction | 4,742 passed, 2 skipped; Ruff passed across `courselab` and `tests`. |
| Focused offline-validator tests | 3 passed for manifest-selected bank loading, course escape rejection and non-path schema rejection. |
| Production-image CI job | Added a job to build the hardened API/web images, provision the restricted `courselab_app` role, migrate disposable PostgreSQL through 0011 as the migration owner, and smoke-test enrollment/archive DTOs as the runtime role. It also checks the built reader and production Compose parse; these exact steps passed locally. |
| Production API image smoke | On disposable PostgreSQL 17, applied Alembic through 0011 as `courselab`, then confirmed non-superuser `courselab_app` can pass health, enroll in Cell Biology, list versions, and read archived course/lesson DTOs without grader fields in the read-only API image. |
| Production web image smoke | Built the runtime image and confirmed the historical-view bundle is present. |
| `docker compose -f compose.production.yaml config --quiet` with placeholder deployment values | Passed configuration parsing; no deployment secrets or persistent services were used. |
| Ruff on changed backend sources/tests | Passed. |
| API image build-time content validation | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 96 disclosed warnings. |

## Current increment: typed learner week schedule (2026-10-10)

Course responses now expose typed week entries with validated lesson references and safe lesson/activity labels. The syllabus renders lesson links and deep links scheduled practice/graded activities through the enrollment-pinned assessment plan, without presenting week numbers as dates or implying that workload has been measured. The Biology package remains partial, inactive for graded assessment and unreviewed; this schedule does not add assignment dates or workload evidence.

| Actual command/check | Result |
| --- | --- |
| `backend/tests/test_api.py` and `backend/tests/test_content_repository.py` in the API image | 49 passed, including malformed week-order, duplicate-ID and range cases; API responses omit manifest internals/answer keys. |
| `tests/content/test_content_validation.py -k week_schedule` | 5 passed for reference, order, duplicate and maximum-week validation. |
| Ruff on the changed validator and test sources | Passed with the backend Ruff configuration. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards, 25 cases; 0 errors and 96 disclosed warnings. |
| `npm run test` in the project frontend test image | 43 passed across 13 files, including lesson/activity links, app-level assessment deep routing, sequence labels, empty weeks and explicit timing/workload wording. |
| `npm run typecheck`, `npm run lint` and `npm run build` in the project frontend test image | Passed. |

## Current increment: archived graded sources for historical appeals (2026-10-10)

Alembic 0010 stores the exact source bytes for each newly pinned graded assessment in a private archive keyed by course version, assessment and SHA-256. Instructor review reconstructs the original prompt and assigned variant from these bytes even after a live source or course version changes. Missing or tampered archives and mismatched grader digests still block score decisions. Archives are not backfilled for earlier submissions, and the existing formative appeal route remains tied to installed content. No active catalog course is graded; these checks use synthetic fixtures. Database dumps now contain protected answer keys.

| Actual command/check | Result |
| --- | --- |
| `backend/tests/test_assessment_api.py` and `backend/tests/test_migrations_config.py` in the shared dev container | 25 passed, including historical recovery after source/course updates, archive tamper rejection, same-version source immutability, legacy-plan archival and migration metadata parity. |
| `tests/content/test_assessment_candidates.py`, `test_cell_biology_integrity.py` and `test_content_validation.py` | 96 passed. |
| `python tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed with all 15 inactive candidates carrying unresolved candidate-specific archive and protected-delivery gates. |
| `python tools/validate_content.py --root .` | Passed: 25 courses, 384 lessons, 2,233 questions, 1,276 cards, 25 cases; 0 errors and 96 disclosed depth warnings. |
| Changed Python sources/tests with Ruff | Passed. |
| Frontend suite, typecheck, lint and production build | 39 tests passed; typecheck, lint and build passed. No frontend code changed in this archive increment. |

## Current increment: persisted protected authored-form assignments (2026-10-10)

Graded assignments now persist a shared authored form and opaque token for each learner attempt. Refreshes replay the saved form, retakes cycle through unused form IDs before reuse, and submissions store the selected variant with the exact grader digest used by appeal review. Migration 0009 adds the append-only assignment record. The active Biology package remains formative-only; the integration fixtures are synthetic and do not verify or activate its assessment candidates.

| Actual command/check | Result |
| --- | --- |
| `PYTHONPATH=.:backend pytest -q backend/tests tests/content -p no:cacheprovider` in the project API image with `jsonschema` installed | 7,270 passed, 2 skipped. A later focused variant/protection run passed 21 tests after adding shared-form-set validation. |
| `npm run test` in the project frontend test image | 39 passed across 11 files, including token submission, retake loading and the last-attempt notice. |
| `npm run typecheck`, `npm run lint` and `npm run build` in the project frontend test image | Passed. |
| `ruff check --no-cache` on changed Python sources/tests | Passed. |
| `python tools/validate_content.py --root .` | 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases validated; 0 errors and 96 disclosed depth warnings. |

## Scope and result

2026-10-06; synthetic local learner data only. Milestones 1 and 2 are implemented. Milestone 3 remains partial; deterministic graders and prototype graded-assignment and review workflows are described below. A Milestone 4 curriculum-map increment is implemented and tested, while subject-matter review and map refinement remain. All 25 course packages are **partial**; zero are beta, complete or externally reviewed. Human score review is limited to saved attempts and does not constitute course-content review. No semester equivalence, university credit, security certification or public production deployment is asserted.

## Current increment: Biology assembled authoring drafts and assessment boundary (0.34.0, 2026-10-09)

Developed with substantial Codex assistance. Added H5–H8 candidates (eight items/25 proposed points each), three limited 12-point lab packets, a 16-case/100-point midterm and 28-case/150-point final with two fixed authored forms each, and an integrative-project portfolio with a reproducible 96-row two-form culture dataset, five milestones and seven four-level human criteria. Its separate 18-point machine subset is never a project grade; human weights/workflow remain unset. All fourteen candidates are inactive with external keys, unreviewed and absent from enrolled grading policy. Earlier H1–H4 files/versions/bindings remain preserved. The catalog remains 25 partial/unreviewed/formative-only packages, 384 lessons, 2,233 formative items, 1,276 cards and 25 cases; Biology retains 39 catalog lessons/137 practice items/89 cards. Two expanded reader entries and worked examples preserve their compact prototypes. A membrane temperature label was corrected from registered SI constants; no new source record/paper/asset was imported.

The cumulative mappings link 34/70 objective occurrences across 33/69 distinct objectives, including a reused water/molecular objective. Fields check only bounded calculations or categorical decisions, not full written/design performance or accepted blueprint coverage. Final early cases were reparameterized to avoid duplicate midterm stems; their numeric keys were recomputed. Three H6/H7 numeric keys were repaired from actual raw counts/mean precision, with datasets and tolerances unchanged. New two-form categorical option positions were rotated without changing semantic answers. See the [AI-assisted record](reviews/ai-assisted/cell-biology-0.34.0.md) for assumptions and limits.

At the 0.34 baseline, platform work had added a [public candidate audit](ASSESSMENT_CANDIDATE_REPORT.md) with artifact hashes and unresolved gates, plus explicit content-validation and runtime rejection of authored variants in graded assignments. That route could not assign/replay exam variants and rejected practice tokens; it had silently served a base question before the guard was added. Standalone signed A/B replay and disposable fixed-form-A protected delivery were separate checks. Neither activated the actual two-form packet or supplied a protected retake/archive policy.

| Actual command/check | Result |
| --- | --- |
| `python -B -m pytest --import-mode=importlib` with external H1–H5 `test_private_candidate.py` paths | Initial combined 404 passed/4 failed: four earlier protected fixtures copied the course before the expanded worked-example fix. H5's 89 tests passed within that run. |
| Same external H1–H4 paths after the fix | 319 passed (65/83/84/87); source/version/binding preservation and protected fixtures passed. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-completion-2026-10-09/test_homework_candidates.py -q -p no:cacheprovider` | Initial assembled 44 passed/4 failed at fixture depth checks; final 48 passed. Earlier H6/H7 arithmetic-key repairs and test precision/index assumptions are retained in authoring notes. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-completion-2026-10-09/test_exam_candidates.py -q -p no:cacheprovider` | Early exam attempts each 352 passed/2 failed (fixture type, mixed-field schema, then unsupported protected variant assumptions). First expanded batch 400 passed/6 failed at worked-example/project duplicate-stem checks; corrected batch 406 passed. |
| Same external component file, `-k "equivalent_units or near_misses or cannot_validate"` | 201 passed/406 deselected: unit conversions, precision-aware near misses and actual two-form activation rejection. |
| Same external component file, `-k final`, after separating final inputs/stems | 337 passed/270 deselected; all final recalculation/mutation/replay/unit/precision and fixed-form protected checks passed. |
| Public candidate/integrity/assembled/audit test files | Final 120 passed. Initial 103 passed/7 failed (scope assertion case and ignored bytecode directory); focused 130 passed/3 failed after header spacing affected embedded stems. Rebuilt exact handout sections and restored item text. |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --frontend --log-dir /workspace/courselab-session-artifacts/codex-biology-completion-2026-10-09/verification-publishable` | PASS all seven steps: content zero errors/96 explicit legacy warnings; legacy seven; security 829 files/zero findings; ruff; root 2,536; backend 4,729 with two existing symbolic-builder skips; frontend lint/37 unit tests/build/bundle scan. |
| Earlier runner directories `verification-final`, `verification-accepted`, `verification-stable` | Superseded root suites stopped at known failures/authoring changes, with logs and FAIL/143 statuses retained. Other steps ran; none is counted as a passing full verification. Current promotion tests still reject unreviewed courses; the short-original adversary now supplies an explicitly short reading. |
| `python -B tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | PASS: public packet/report/prerequisite hashes and unresolved-gate record current. No private store opened. |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: public inventory and gap report unchanged; 101 linked/listed outcomes and 184 preserved unlinked prototype objectives remain. |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: zero HIGH/MED/LOW findings before publication report update; staged recheck recorded in external handoff. This is not correctness or review evidence. |
| `git diff --check` | PASS. |

Initial authoring also encountered Fraction JSON serialization and a syntax error before bank/manifest writes, incorrect SI dimension names, a numeric lesson-map collision with lab IDs, and a system-Python/Pydantic mismatch in a helper. Fixed these under the pinned runtime, recorded failures and refreshed only the affected uncommitted draft bindings. Read-only path/PowerShell discovery probes failed harmlessly; no credential or private bank was committed. Keys, answer-specific checks, logs and hash-bound evidence are retained outside Git in the completion and H5–H8 artifact roots. Hosted CI cannot independently verify those private banks.

Local Compose/Playwright were not run by this runner. Hosted CI is checked for the exact published SHA and recorded separately; a registry failure or skipped browser step is never called a pass. Qualified independent numerical/scientific/assessment review, manual accessibility/fairness review, measured workload, accepted human assessment components, protected variant/archive support and operator conduct/provisioning/release decisions remain missing. Passing automated checks does not make the course complete, reviewed or graded.

## Previous increment: Biology Homework 4 inactive review candidate (0.23.0, 2026-10-09)

Developed with Codex assistance. Eight new answer-free public item DTOs, original instructions, 72 synthetic ChIP technical-well observations and 12 separate matched reporter preparations form a 25-point review candidate. Its key and candidate-specific tests stay outside Git. Earlier candidate files, authored versions and key bindings are unchanged. All 39 readings, 137 enrolled practice items, 89 cards, modules, assessments, grading policy, case and course review remain unchanged. All four candidates are inactive; all 25 packages remain partial, unreviewed and formative-only.

Fraction/Decimal arithmetic reconstructs threshold-relative amounts, applies the declared significant-figure rounding, computes raw background-corrected reporter ratios and recalculates every numerical key and nine CSV cells. Wrong denominators, amplification factor, technical-well counting, transformed-well averaging, pooled reporter ratios and omitted backgrounds lose credit. Alternate fraction/scientific/signed forms, unit/precision/scale/sign/near-miss and malformed/injection/partial responses, plus each numeric/categorical/CSV key/cell mutation, are checked. Temporary protected delivery covers enrollment, complete-response requirements, answer-free DTO equality, full-credit synthetic submission and missing/changed key fail-closed behavior. Fixture grading/attempt settings are not installed on the real course. The [AI-assisted record](reviews/ai-assisted/cell-biology-0.23.0.md) states the same-AI boundary and absent qualified review.

| Command/check (Linux development container) | Actual result |
|---|---|
| `python -B tools/validate_content.py` (early probe before syllabus update) | FAIL: one syllabus-version mismatch, zero inventory changes; syllabus updated before full verification. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h4-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | Initial 83 passed / 4 failed; final 87 passed. Objective mapping, recalculation rounding and a unit-spelling assumption were corrected; numeric keys, tolerances and answer indices were unchanged. |
| `python -B -m pytest tests/content/test_cell_biology_candidate.py tests/content/test_cell_biology_integrity.py -q -p no:cacheprovider` | Initial 32 passed / one unknown-objective failure; final 33 passed after mapping to existing manifest objectives. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h1-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | PASS: 65 prior-candidate checks after version advance. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h2-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | PASS: 83 prior-candidate checks. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h3-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | PASS: 84 prior-candidate checks. |
| `ruff format tests/content/test_cell_biology_candidate.py` | One intended test file formatted. |
| `ruff check tests/content/test_cell_biology_candidate.py tests/content/test_cell_biology_integrity.py` | PASS. |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-biology-h4-2026-10-09/verification-final` | PASS: content zero errors/98 legacy warnings; legacy seven; security 788 files/zero findings; ruff; root 2449; backend 4723 passed/two existing symbolic-builder skips. |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS; report/public inventory unchanged. |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: zero HIGH/MED/LOW findings. |
| `git diff --check` | PASS. |

The first private recalculation assertions compared unrounded quantities to keys representing the explicitly requested three-significant-figure response. Decimal rounding now follows that response contract before tolerance comparison. One scientific-notation test used an unsupported unit spelling; it now uses the supported percent symbol. The first objective mapping mistakenly used numbered lesson-prose objectives absent from the manifest; items now reference existing manifest objectives, and the key hash/DTOs were refreshed. Numerical answers, tolerances and categorical answer indices did not change. Initial failure logs are retained. Read-only discovery probes also encountered unavailable paths/PowerShell wildcard syntax; subsequent direct-file discovery resolved them.

ChIP input fraction, common amplicon factor, threshold, linear range and compatible recovery are stipulated assumptions; no measured calibration or uncertainty exists. Duplicate Cq averaging is the declared summary rule. ChIP and reporter samples are different cultures matched only by condition, not paired across assays. Reference correction assumes applicable background, linear channels and stable biological meaning; raw channel variation does not establish reference stability. Cross-linked recovery can be indirect and a motif/plasmid result does not establish native target identity or native transcriptional causation. No-template observations, endogenous perturbation/RNA and direct-binding evidence are absent. Written methods, scripts, plots, uncertainty and experiment design are ungraded; workload is unmeasured.

Existing original lessons provide context; no outside source, identifier, prose, problem, dataset or figure was imported and no new citation-resolution pass is claimed. Original packet and synthetic observations are CC BY 4.0 with substantial AI assistance. Key/public/prerequisite/test hashes and empty reviewer lists are recorded outside Git. Independent numerical, grader-mutation, qualified scientific/assessment, manual accessibility/fairness and operator review/release requirements remain missing. No assessment is activated on automated-check success.

Frontend, Compose and Playwright were not run locally for this increment. Publication CI attempts them; skipped browser verification is not a pass. The preceding Homework 3 exact-SHA run [37992507776](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37992507776) passed content/backend and frontend lint/unit/build/bundle security but failed Compose before application startup across four attempts (Docker Hub pull limits and an auth-token timeout); Playwright was skipped. Its full hosted verification remains incomplete. Logs and exact attempt results are retained in its external artifact root. Homework 4's eventual CI result is recorded separately in its external evidence/handoff after publication.

## Previous increment: Biology Homework 3 inactive review candidate (0.22.0, 2026-10-09)

Developed with Codex assistance. The separate original candidate has eight answer-free public item DTOs, learner instructions, an unscored discussion rubric, 36 synthetic lesion/background/DNA-reference observations and a private answer bank outside Git. Its proposed 25 points are a review allocation, not a course grade. All previous 137 practice items, 89 cards, 39 readings, modules, assessments, review, case and grading policy remain unchanged. All three candidates are inactive; all 25 packages remain partial, unreviewed and formative-only.

Fraction arithmetic recalculates matched culture ratios, contrasts, viable-cell fraction and nine summary cells. Explicit strand-identity enumeration checks the duplex count and composite percentage under the stipulated copying model. Equivalent units, precision, scale/sign, near misses, malformed/injection/partial responses and numerical/categorical/CSV key/cell mutations pass. Raw-channel comparison, omitted background, pooled reference weighting, time-point pseudoreplication and division by viable-cell fraction do not receive full summary credit. Complementary sequence and parental-strand conservation checks add model evidence. Protected API delivery is exercised only in an isolated temporary copy: enrollment, complete submissions, answer-free DTO equality, full-credit synthetic submission and fail-closed missing/changed key sources pass. No fixture grade-category/attempt policy is installed on the catalog course. The [AI-assisted record](reviews/ai-assisted/cell-biology-0.22.0.md) distinguishes these same-AI checks from independent or qualified review.

| Command/check (Linux development container) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS first run: 25 packages, 384 lessons, 2233 public questions, 1276 cards, 25 cases; zero errors, 98 legacy warnings. Inactive candidates do not inflate enrolled inventory. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h3-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | PASS first run: all 84 candidate-specific recalculation, mutation and delivery checks. Keys/tests remain outside Git. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h1-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | PASS: all 65 prior-candidate checks after the version advance. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h2-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | PASS: all 83 prior-candidate checks after the version advance. |
| `python -B -m pytest tests/content/test_cell_biology_candidate.py tests/content/test_cell_biology_integrity.py -q -p no:cacheprovider` | PASS first run: all 27 public checks across three candidates and original Biology content. |
| `ruff format tests/content/test_cell_biology_candidate.py tests/content/test_cell_biology_integrity.py` | One file formatted, one unchanged; unrelated whitespace-only formatting in the existing integrity file was later trimmed to retain only the intended whitelist change. |
| `ruff check tests/content/test_cell_biology_candidate.py tests/content/test_cell_biology_integrity.py` | PASS first run and in the full run after formatting cleanup. |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-biology-h3-2026-10-09/verification-final` | PASS: content, legacy (7), security (783 files, zero findings), ruff, root (2443), backend (4723 passed, two existing symbolic-builder skips). |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS; public inventory/report unchanged. |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS; zero HIGH/MED/LOW findings. |
| `git diff --check` | PASS. |

No inspection, content, recalculation, mutation, grader, lint, security or full-verification command failed for this increment. No numeric answer, tolerance or key index changed to make a check pass. Existing candidates' public files, authored versions 0.20.0/0.21.0 and key bindings remain unchanged. Version-aware public checks preserve their historical identities rather than inventing new reviews. No new outside source, identifier, prose, problem, figure or dataset was imported; no new identifier-resolution pass is claimed. Original packet, stems and data are CC BY 4.0 with substantial AI assistance.

Reference normalization assumes a positive background-corrected reference, linear channels and shared multiplicative loading/recovery. Loaded DNA is assay material, not total genome synthesis. A synthesis-label fraction is not completed genome doubling; viable-cell counts do not recover lesion burden in lost cells. A restored condition is not proof of direct catalysis or mutation-free sequence. The separate copying model assumes synchronized generations, retained parental strands and no new heavy isotope or repair replacement. No physical measurement, calibrated uncertainty, direct repair flux or mutation-frequency assay was performed.

Starting corrected ratios are equal by construction, so matching scored cells cannot certify that a learner implemented culture pairing; some alternative calculations coincide on these values. Analysis method and understanding remain ungraded.

Hash-bound development evidence records public/key/prerequisite/test-script hashes with no reviewer records. Independent numerical review, qualified scientific and assessment review, manual accessibility/fairness review, measured workload and operator provisioning/release decisions remain absent. Written discussion is unscored. Frontend, Docker Compose and Playwright were not run locally for this increment; publication CI runs them. Keys, private tests, full logs and evidence stay outside Git in courselab-session-artifacts/codex-biology-h3-2026-10-09.

## Previous increment: Biology Homework 2 inactive review candidate (0.21.0, 2026-10-09)

Developed with Codex assistance. The new original candidate supplies eight answer-free public item DTOs, learner instructions, an unscored written-discussion rubric, 420 synthetic calibration/blank/reaction observations and a private answer package outside Git. Its proposed 25 points are a review allocation, not a course-grade policy. Neither Homework 1 nor Homework 2 is activated. The course preserves all 137 practice items, 89 cards, 39 readings, modules, existing assessments, case, review and formative-only grading policy. All 25 packages remain partial and unreviewed.

Separate Fraction arithmetic recomputes detector intercepts/gains, matched reaction/blank slopes, four numeric keys, the composite ratio and nine CSV cells directly from the public raw table. Tests cover equivalent units, precision, dimensions, sign/scale/near misses, malformed/injection responses, partial fields, numeric/categorical/CSV key mutations and analysis counterexamples. Omitted blank drift, transferring vehicle gain to another optical condition, unsuitable late windows, pooled gains and time-point pseudoreplication do not receive full summary credit. Calibration residuals and product-range checks apply only to the stipulated construction. An isolated temporary course copy validates the external private bank and checks enrollment, answer-free protected delivery, complete full-credit submission and fail-closed missing/changed key sources. Fixture grading settings are not applied to the catalog course. The [AI-assisted record](reviews/ai-assisted/cell-biology-0.21.0.md) details scope; all checks are same-AI evidence, not independent or qualified review.

| Command/check (Linux development container) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS first run: 25 packages, 384 lessons, 2233 public questions, 1276 cards, 25 cases; zero errors, 98 legacy warnings. Inactive candidates do not inflate enrolled inventory. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h2-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | PASS first run: all 83 candidate-specific recalculation, mutation and delivery checks. Keys and tests remain outside Git. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h1-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | PASS: all 65 prior-candidate checks after the course-version advance. |
| `python -B -m pytest tests/content/test_cell_biology_candidate.py tests/content/test_cell_biology_integrity.py -q -p no:cacheprovider` | PASS first run: all 21 checks across both candidates and existing Biology content. |
| `ruff format tests/content/test_cell_biology_candidate.py` | Formatted. |
| `ruff check tests/content/test_cell_biology_candidate.py` | PASS first run. |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-biology-h2-2026-10-09/verification-final` | PASS: content, legacy (7), security (779 files, zero findings), ruff, root (2437), backend (4723 passed, two existing symbolic-builder skips). |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS; public inventory/report unchanged. |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS; zero HIGH/MED/LOW findings. |
| `git diff --check` | PASS. |

No content, numerical, mutation, grader, lint, security or full-verification check failed for this increment; no answer, tolerance or key index changed to make a check pass. An initial read-only probe for 04b-enzyme-kinetics-and-inhibition.md failed because the actual module is 04b-initial-rates-and-enzyme-inhibition.md; it was located and read. No verification pass is claimed for that path probe. Existing prerequisite files match their Git blobs. No new outside source, identifier, prose, problem, figure or dataset was imported and no new identifier-resolution pass is claimed. Original instructions, stems and data are CC BY 4.0 with substantial AI assistance.

The four days are independent preparation units by stipulation; time points, standards and substrate levels are matched observations. Gain transfer across substrate levels is assumed, not experimentally validated. The early window uses ordinary-least-squares slopes over 0,2,4 seconds; the later comparison uses a 0–10-second endpoint slope. Prescribed curvature does not identify depletion, enzyme instability or another mechanism. Apparent Km is calculated from separately supplied constants, not fitted to these observations. No actual experiment, calibration uncertainty, molecular binding site or clinical utility was measured.

Homework 1 retains byte-identical public files, its authored version 0.20.0 and original key hash. Candidate version tests preserve historical identity rather than rebinding old metadata to 0.21.0. Hash-bound development evidence identifies public files, private key, prerequisite readings and the external check script, with no reviewers. Independent numerical, scientific, assessment and manual-accessibility review, workload evidence and operator provisioning/release decisions remain absent. Frontend, Docker Compose and Playwright were not run locally for this increment; publication CI runs them. External answer files/tests/logs/evidence stay outside Git in courselab-session-artifacts/codex-biology-h2-2026-10-09.

## Previous increment: Biology Homework 1 inactive review candidate (0.20.0, 2026-10-09)

Developed with Codex assistance. A new original seven-item, 25-point Homework 1 candidate supplies learner instructions, 36 synthetic pulse-chase observations, answer-free public item DTOs and an external private answer package. The candidate is separate from the open practice companion and not referenced by the actual assessment manifest. The course retains every previous assessment, all 137 practice items, 89 cards, 39 readings, review and formative-only grading policy. All 25 packages remain partial and unreviewed; none has an activated graded assignment.

Fraction-based separate calculations cover three numeric keys and nine CSV cells from preparation-specific input denominators and matched time points. Equivalent units, lexical precision, sign/scale/near misses, malformed and injection responses, partial criteria, each CSV cell/key mutation, categorical key mutation, pooled-normalization and pseudoreplication counterexamples are exercised. The candidate is schema-validated and submitted for full credit through the existing protected API in an isolated temporary course copy. Enrollment, complete response requirements, answer-free DTO equality and fail-closed missing/changed sources pass. The fixture category/attempt policy is not applied to the real course. This is same-AI evidence, not independent or qualified review. See the [candidate record](reviews/ai-assisted/cell-biology-0.20.0.md).

| Command/check (Linux development container) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS first run: 25 packages, 384 lessons, 2233 public questions, 1276 cards, 25 cases; zero errors, 98 legacy warnings. Inactive candidate items do not inflate enrolled inventory. |
| `python -B -m pytest /workspace/courselab-session-artifacts/codex-biology-h1-2026-10-09/test_private_candidate.py -q -p no:cacheprovider` | Initial: 6 failed/59 passed; second: 1 failed/64 passed; repaired third: all 65 passed. Tests and keys remain outside Git. |
| `python -B -m pytest tests/content/test_cell_biology_candidate.py tests/content/test_cell_biology_integrity.py -q -p no:cacheprovider` | First and second: 1 failed/14 passed; after the two old directory/specification assumptions were narrowed, all 15 passed. |
| `ruff format tests/content/test_cell_biology_candidate.py` | Formatted. |
| `ruff check tests/content/test_cell_biology_candidate.py` | Initially failed one E741 ambiguous local; renamed; rerun passed. |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-biology-h1-2026-10-09/verification-final` | PASS content, legacy (7), security (775 files, zero findings), ruff, root (2431), backend (4723 passed, two existing symbolic-builder skips). |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS; unchanged public inventory/report. |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS; zero HIGH/MED/LOW findings. |
| `git diff --check` | PASS. |

Initial private test failures were a binary float comparison at a rounding tolerance boundary, expectations that invalid empty request shapes score zero rather than schema rejection, a wrong multiple-select partial-credit expectation and an unsupported staged assessment outcome field. Rational comparison and normative request/manifest behavior corrected the checks. The learner scoring-policy wording was also corrected to equal-share correct-minus-incorrect scoring. The second private run's remaining failure expected guest creation HTTP 201; the actual service returns 200. No numeric key, tolerance or correct option index changed. The private source hash changed because the scoring prompt changed. Public checks retain no-key assertions while explicitly allowing the new answer-free JSON/CSV beside the three still-unauthored summative specifications.

Read-only probes of nonexistent homework/backend/module/log paths failed; actual files were located and read. These are inspection errors, not evidence of passing checks. No new outside source, paper identifier, teaching material, figure or dataset was imported and no new identifier-resolution pass is claimed. The construction is original, synthetic and CC BY 4.0 with substantial AI assistance.

Independent numerical review, scientific/assessment/manual-accessibility review, measured workload and operator provisioning/release decisions remain absent. A file hash identifies the checked key, but does not create those approvals or establish assessment security. The written-discussion rubric is unscored. The candidate's temporary test does not configure production grading. Frontend, Docker Compose and Playwright were not run locally for this increment; publication CI runs them. Private files, test scripts, full logs and hash-bound development evidence stay outside Git in courselab-session-artifacts/codex-biology-h1-2026-10-09.

## Previous increment: Robotics lessons, near-extension lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Robotics advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven original lessons develop frames/calibration/uncertainty, Jacobians/singularities/force mapping, inverse branches/limits/clearance, mass matrices/gravity/energy, motor envelopes/backlash/feedback, trajectory timing/stopping bounds and sensing/case evidence. Each has six numeric and three conceptual choices. One synthetic near-extension motion lab and a proposed 14-week sequence complete this increment. There are 71 new items and 32 new cards; the package has 14 readings, 91 items and 48 cards. All 20 prior questions, 16 cards, six module definitions, seven assessments and the original stall case remain unchanged. All 25 packages now have proposed weekly sequences; none is a complete or reviewed semester course.

Separate calculations cover all 62 numeric keys, including 16 preserved ones, and twenty-four CSV cells. Frame round trips and composition, Jacobian finite differences and power duality, inverse branches and limits, segment clearance edge cases, point-mass inertia and nonzero-rate energy balance, same-point motor power, trajectory extrema and stopping arithmetic add evidence. A common speed limiter preserves the requested Cartesian direction under the frozen Jacobian, whereas independent joint clipping does not. The [AI-assisted record](reviews/ai-assisted/robotics-0.4.0.md) documents construction and limits. The same AI authored content and tests; no independent or qualified human review occurred.

Five primary Modern Robotics web supplements by Kevin M. Lynch and Frank C. Park were retrieved and metadata checked directly, covering transforms, singularities, mass matrices, torque control and trajectories. They remain link-only with no imported prose, problems, examples, figures or data and no broadened permissions. An initial Lagrangian part-one retrieval failed; the retrieved mass-matrix supplement was selected. No DOI/PMID/NCT or paper link was introduced and no identifier-resolution pass is claimed.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS on first run: 25 packages, 384 lessons, 2233 questions, 1276 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `ruff format tests/content/test_robotics_recalculations.py` | Formatted initially; unchanged after comparison repair |
| `ruff check tests/content/test_robotics_recalculations.py` | PASS initially and after comparison repair |
| `python -B -m pytest tests/content/test_robotics_recalculations.py -q -p no:cacheprovider` | Initial FAIL: 104 passed, two binary floating-point exact-comparison failures in the checks; repaired |
| `python -B -m pytest tests/content/test_robotics_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS after comparison repair: 590 |
| `python -B /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py robotics robotics-` | PASS on first run: all 91 items earn full credit in the actual grader |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-robotics-2026-10-09/verification-final` | PASS: content, legacy (7), security (770 source files, 0 findings), ruff, root (2425), backend (4723 passed, 2 existing symbolic-builder skips) |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |
| `git diff --check` | PASS |

The failed comparisons evaluated 1.5×0.4/0.2 as 3.0000000000000004 and 6×0.4/4 as 0.6000000000000001. The separate test now uses exact rational arithmetic for duration and bounds and an approximate assertion for the floating acceleration evaluation. No authored answer or tolerance changed. Full verification began after a separate successful schema pass and the repaired focused run.

Read-only inspection probes for nonexistent `content/schemas/solution-spec.schema.json` and `.github/workflows/ci.yml` failed. The normative question schema and actual `.github/workflows/ci.yaml` were read instead. These were path-inspection errors, not verification passes.

Twenty-four synthetic reports cover four elbow angles and two fixed-base velocity directions. The 2-degree inward request demands elbow rate approximately 2.387227 rad/s; a common scale approximately 0.209448 keeps its command at 0.5 rad/s, yielding approximately 2.094480 mm/s inward motion. All tangent requests retain scale one. Deterministic component offsets are construction values, not actual sensor errors. There is no integration between postures or dynamic robot simulation. The inward/tangent labels refer to base x/y, not exact radial/tangent directions at all bent postures.

Instruction explicitly qualifies the preserved case: inverse velocity and dynamic requirements differ from direct finite-force mapping JᵀF, which does not universally diverge; continuous redundancy requires added degrees of freedom or task relaxation. The point-mass joint inertia stays positive definite at a singular endpoint Jacobian. Stopping-distance arithmetic is conditional and establishes no physical stopping performance or safety approval. Seven preserved numeric items require units; none enforces significant figures or dimensions. Written diagnoses and planner/controller implementations are ungraded.

Frontend checks, Docker Compose and Playwright were not run locally for this increment; publication CI runs them. Logs and helpers remain outside git in courselab-session-artifacts/codex-robotics-2026-10-09. Qualified review, assistive-technology review and measured workload remain absent.

## Previous increment: Programming lessons, pipeline lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Programming advances from 0.3.2 to 0.4.0 while remaining partial, unreviewed and formative-only. Six original lessons develop input contracts/parsing/pure functions, array axes/broadcasting/memory, root brackets/residual conditioning, quadrature/refinement/stability, least-squares rank/scaling and grouped validation/thresholds. Each has six numeric and three conceptual choices. One synthetic pipeline lab and a proposed 14-week sequence complete the increment. There are 62 new items and 28 new cards; the package has 14 readings, 88 items and 48 cards. All 26 prior questions, 20 cards, seven module definitions, eight assessments and the original classifier case remain unchanged. Learner code execution remains disabled.

Separate calculations cover all 54 numeric keys, including 14 preserved ones, and sixteen CSV cells. Root bracket invariants and domain counterexamples, quadrature order, stability versus positivity, residual orthogonality/rank, exact binade spacing, group separation and frozen threshold counts add evidence. The trusted authored concentration snippet is checked on valid, invalid, nonfinite and overflow-result inputs. All three new code blocks have syntax checks; the NumPy snippets are not executed in these tests. Array and affine-fit outputs are recalculated with standard Python arithmetic. This is developer-side checking, not execution of learner code. The [AI-assisted record](reviews/ai-assisted/programming-0.4.0.md) documents models and limits. The same AI authored content and tests; no independent or qualified human review occurred.

Five official documentation pages were opened and relevant behavior/metadata checked directly: Python CSV, NumPy broadcasting and least squares, SciPy bisection and scikit-learn cross-validation. They remain link-only with no imported prose, examples, figures or data, no broadened permissions and no new DOI/PMID/NCT or paper link. No identifier-resolution pass is claimed. Displayed documentation versions do not describe the project's installed dependencies.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | Initial FAIL: uppercase CSV check/rubric IDs, with cascading missing references; IDs repaired |
| `python -B tools/validate_content.py` | Second FAIL: uppercase CSV row codes, with cascading missing references; dataset/guide/key codes repaired |
| `python -B tools/validate_content.py --json` | PASS after repairs: 25 packages, 376 lessons, 2162 questions, 1244 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `ruff format tests/content/test_programming_recalculations.py` | Formatted; formatted again after naming repair |
| `ruff check tests/content/test_programming_recalculations.py` | Initial FAIL: four E741 ambiguous locals; renamed; rerun PASS |
| `python -B -m pytest tests/content/test_programming_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 573 on first run; 573 again after ID/naming repairs; no numeric answer or tolerance changed |
| `python -B /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py programming programming-` | PASS on first run: all 88 items earn full credit in the actual grader |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-programming-2026-10-09/verification-final` | PASS: content, legacy (7), security (759 source files, 0 findings), ruff, root (2305), backend (4581 passed, 2 existing symbolic-builder skips) |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |
| `git diff --check` | PASS |

Schema initially rejected uppercase check/rubric IDs and then row codes. Final row codes d01–d08 are consistent in the dataset, guide and summary specifications. These repairs changed identifiers only; no numerical key or tolerance was changed to make a recalculation pass. Full verification began after a separate repaired schema pass. The preserved approximate spacing key stays |x| times epsilon near 10⁸; new instruction and a separately checked item distinguish exact binade spacing 2⁻²⁶. Its original tolerance does not validate the approximate key as exact.

The pipeline has twenty synthetic records, sixteen valid concentrations and four distinct failures. Eight donors have two accepted rows each, with disjoint training/evaluation membership. Scores and labels are supplied toy values without a fitted classifier. The stipulated complete-record evaluation rule is not a universal or unbiased policy. At frozen score≥0.5, evaluation counts are 2,3,1,2 for TP,FP,FN,TN; at the predefined 0.7 comparison they are 2,1,1,4. Selection from that comparison consults evaluation information. No real utility, clinical decision or external validation is inferred.

Frontend checks, Docker Compose and Playwright were not run locally for this increment; publication CI runs them. Logs and helpers remain outside git in courselab-session-artifacts/codex-programming-2026-10-09. Qualified review and measured workload remain absent.

## Previous increment: Circuits lessons, channel-diagnostic lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Electrical Circuits & Instrumentation advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven original lessons develop nodal/port/power analysis, finite feedback/bias/range, differential/common-mode/interface imbalance, filter loading/recovery, noise/covariance/uncertainty, ADC acquisition/aliasing and calibration/clipping evidence. Each has six numeric and three conceptual choices. One synthetic channel-diagnostic lab and a proposed 14-week sequence complete the increment. There are 71 new items and 32 cards; the package has 14 readings, 91 items and 48 cards. All 20 prior questions, 16 cards, six module definitions, seven assessments and the original movement-clipping/rest-drift case remain unchanged.

Separate calculations cover all 63 numeric keys, including 17 preserved ones, and 32 CSV cells. Nodal/test-port and power checks, finite-feedback bisection, passive-ladder state/energy integration, transformed noise-bandwidth integration, covariance components, calibration sensitivities, quantizer/acquisition checks and alias counterexamples add evidence. Independent fits show how clipped endpoints compromise a line from gain 100/intercept 0.10 to gain 70/intercept 0.06. A separate baseline-excess fit recovers 0.50 s under the construction. The [AI-assisted check record](reviews/ai-assisted/circuits-0.4.0.md) documents models and limits. The same AI authored checks and content; no independent or qualified human review occurred.

Four primary technical documents were retrieved as link-only references: OpenStax Kirchhoff guidance, Texas Instruments op-amp specifications, NIST combined-standard-uncertainty guidance and an Analog Devices ADC chapter. No prose, problem, figure or dataset was imported, permissions were not broadened and no DOI/PMID/NCT was added. Metadata was checked against the retrieved documents. The original text feedback map has a verbal description but no assistive-technology review. No workload was measured.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | Initial run: 1 duplicate-question error; prompt repaired; separate rerun PASS: 25 packages, 369 lessons, 2100 questions, 1216 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-circuits-2026-10-09/verification-final` | PASS: content, legacy (7), security (749 source files, 0 findings), ruff, root (2190), backend (4457 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-circuits-2026-10-09/check_grader.py` | PASS on the first run: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_circuits_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS on the first run: 576 focused checks |
| `ruff check tests/content/test_circuits_recalculations.py` | PASS on the first run; file subsequently formatted |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The first schema check rejected a generic lab multiple-select prompt because it matched an Organic Chemistry prompt. The new prompt names the gain-sweep/common-mode/drift construction; options and key did not change. Full verification started only after the separate repaired schema check passed. All numeric/CSV recalculations passed on their first run and no answer or tolerance changed. Two initial Analog Devices article probes were inaccessible; the successfully retrieved ADC chapter was selected instead. A TI filter report was inspected but is not used as a new course reference.

The citation-check command `python3 -B /workspace/.claude/skills/citation-check/scripts/refcheck.py --scan courselab-session-artifacts/codex-circuits-2026-10-09/lessons.py courselab-session-artifacts/codex-circuits-2026-10-09/data.py --json --out /workspace/courselab-session-artifacts/codex-circuits-2026-10-09/reference-id-scan.json` returned exit 1 with `nothing to verify`, because no supported identifiers were present. No registry lookup or audit file was produced, and no identifier-resolution pass is claimed. Technical-document metadata was checked directly.

The preserved Nyquist question remains a nominal two-times threshold; new discrete-phase counterexamples and learner limitations explain why exact-boundary recovery and practical filter/acquisition margins are separate. Frontend checks, Docker Compose and Playwright were not run locally for this increment; publication CI runs them. Logs remain outside git in `courselab-session-artifacts/codex-circuits-2026-10-09`.

## Previous increment: Physics II lessons, loading lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Physics: Electricity & Magnetism advances from 0.3.2 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven original lessons develop field/potential and Gauss boundaries, dielectric energy conditions, Kirchhoff/Thevenin loading, RC initial states and energy, magnetic vectors and field models, induction/RL energy and phasor measurement inference. Each new lesson has six numeric and three conceptual choices. One synthetic calibration/loading/time-constant lab and a proposed 14-week sequence complete the increment. There are 71 new items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 prior questions, 16 cards and the original high-impedance recording case remain unchanged.

Separate calculations check all 62 numeric keys, including 16 preserved ones, and all 24 CSV cells. Potential gradients, dielectric source-work ledgers, nodal balances, component RC/RL and magnetic-motion integration, finite-difference flux linkage and complex KCL/cycle-average power provide additional checks. Reference voltages identify reporting offset 0.020 V and gain 2; loaded steady amplitudes and normalized transients identify one 100 kΩ source and 1 µF input capacitance under the declared model. The [AI-assisted check record](reviews/ai-assisted/physics-em-0.4.0.md) documents checks and limits. The same AI assistant authored checks and content; no independent or qualified human review occurred.

Four primary OpenStax University Physics Volume 2 sections were retrieved as link-only references. No teaching prose, problem, figure or dataset was imported, permissions were not broadened and no new paper identifier was added. The original text connection map has a verbal description but no assistive-technology review. No workload was measured.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS before and after display repair: 25 packages, 361 lessons, 2029 questions, 1184 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-physics-em-2026-10-09/verification-final` | PASS: content, legacy (7), security (738 source files, 0 findings), ruff, root (2058), backend (4315 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-physics-em-2026-10-09/check_grader.py` | PASS on the first run: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_physics_em_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | Initial run: 545 passed, 2 display-formatting failures; repaired rerun: 547 passed |
| `ruff check tests/content/test_physics_em_recalculations.py` | PASS on the first run; file subsequently formatted |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

All numerical and CSV recalculations passed on their first run. Two existing display-format tests initially rejected a long-decimal mass and an overprecise lab prompt voltage. The lesson now displays 1.0×10⁻¹² kg, and the lab prompt uses 0.316060 V with its logarithmic solution described as approximate. No stored key or tolerance changed. Focused rerun and the complete full run pass. Two field-page probes and one initial AC-power probe returned inaccessible; only successful retrieved pages are listed as references, with the Gauss section selected and AC power retrieved on retry.

The preserved series-resistance prompt says “below” while its nominal V/I key is the equality boundary, with grading tolerance. That preserved limitation is disclosed; it establishes no real safety margin or device validation. Existing prompt-rounded numeric keys remain within their stated tolerances. Frontend checks, Docker Compose and Playwright were not run locally for this increment; publication CI runs them. Logs stay outside git in `courselab-session-artifacts/codex-physics-em-2026-10-09`.

## Previous increment: Physics I: Mechanics lessons, compliance lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Physics: Mechanics for Biomedical Engineers advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven original lessons develop vector/frame kinematics, contact/friction, work/momentum system boundaries, rotation/rolling, damping/energy balance, scalar time-dependent materials and machine-compliance inference. Each new lesson has six numeric and three conceptual choices. One synthetic reference/compliance/orientation lab and a proposed 14-week sequence complete the increment. There are 71 new items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 preexisting questions, 16 cards and the original tendon self-assessment case are preserved.

Separate calculations check all 63 numeric keys, including 17 preserved ones, and all 18 CSV cells. Finite differences check vector/frame motion; projectile energy, collision momentum, force and impulse ledgers check mechanical boundaries; radial mass quadrature and rolling energy check rotation; component ODE integration checks damped motion and accumulated dissipation, and a scalar creep balance; OLS regression checks raw displacement slopes and reference-based series correction. The synthetic lab recovers stiffnesses 2000/1000 N/m, with corrected ratio 2 rather than apparent 1.5. The [AI-assisted check record](reviews/ai-assisted/physics-mechanics-0.4.0.md) documents selected checks and limits. The same AI assistant authored checks and content; this is not qualified or independent human review.

Four primary OpenStax University Physics Volume 1 sections were retrieved as link-only factual references. No teaching prose, problem, figure or dataset was imported, permissions were not broadened and no new paper identifier was introduced. The original text free-body diagram includes a verbal description but no assistive-technology review. No workload was measured.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS on the first run: 25 packages, 353 lessons, 1958 questions, 1152 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-physics-mechanics-2026-10-09/verification-final` | PASS: content, legacy (7), security (727 source files, 0 findings), ruff, root (1941), backend (4173 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-physics-mechanics-2026-10-09/check_grader.py` | PASS on the first run: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_physics_mechanics_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS on the first run: 525 focused checks |
| `ruff check tests/content/test_physics_mechanics_recalculations.py` | PASS on the first run; file subsequently formatted |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

A pre-integration spot calculation corrected two draft transcriptions, landing time 0.851160 to 0.851148 s and range 1.702320 to 1.702297 m. No stored key existed at that point. All authored numerical keys and CSV checks passed on their first run, and no key changed. The preserved impact items use net stopping-force approximations and rounded prompt quantities within their stated tolerances; the new separate vertical-stop example explicitly separates net force from contact plus weight. No injury or equipment rating is inferred.

Two exploratory host commands included `git status --short` or `git diff` from the outer workspace and failed because it is not the repository; those read-only inspections were rerun successfully from the actual checkout. An exploratory `Get-Content` used nonexistent `test_organic_chemistry_calculations.py`; the correct `test_organic_chemistry_recalculations.py` was then read. No content, numerical, grader, lint, security or full-verification check failed. Logs remain outside git in `courselab-session-artifacts/codex-physics-mechanics-2026-10-09`. Frontend checks, Docker Compose and Playwright were not run locally for this increment; publication CI runs them.

## Previous increment: Organic Chemistry lessons, peak-calibration lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Organic Chemistry I for Life Sciences advances from 0.3.2 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven original lessons develop structure/electron flow, conformation/Fischer mapping, competing substitution/elimination, carbonyl/acyl/proton bookkeeping, enolate/aldol atom mapping, spectroscopic constraints and reaction-network evidence. Each new lesson has four numeric and five conceptual choices. One synthetic calibrated-peak/excess lab and a proposed 14-week sequence complete the increment. There are 71 new items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 preexisting questions, 16 cards and the original amide self-assessment checklist are preserved.

Separate calculations check all 40 numeric keys, including eight preserved keys, and all 21 CSV cells. Spatial determinants check the text Fischer map, formal-charge and bond-order ledgers check selected electron flows, atom/hydrogen mapping checks aldol connectivity, spin enumeration checks simple multiplets, and component ODE integration checks hydrolysis and parallel-route conservation. The lab uses a blank and pure standards to recover reporting offsets/gains before calculating pair amounts and excess. Its unequal gains are synthetic reporting factors, not claimed intrinsic UV-absorption differences between enantiomers in an achiral environment. The [AI-assisted check record](reviews/ai-assisted/organic-chemistry-0.4.0.md) documents selected checks and limits. The same AI assistant authored content and checks; this is not independent chemical or human review.

Six primary OpenStax Organic Chemistry pages were retrieved as link-only factual references. No teaching prose, worked problem, drawing or dataset was imported, source permissions were not broadened, and no new paper identifier was introduced. The original text diagram includes a verbal description; assistive-technology and qualified review are still absent.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS after one feedback-length repair: 25 packages, 345 lessons, 1887 questions, 1120 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-organic-chemistry-2026-10-09/verification-final` | PASS: content, legacy (7), security (716 source files, 0 findings), ruff, root (1832), backend (4031 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-organic-chemistry-2026-10-09/check_grader.py` | PASS on the first run: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_organic_chemistry_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS on the first run: 504 focused checks before expanding one short explanation; the full run covers that repair |
| `ruff check tests/content/test_organic_chemistry_recalculations.py` | PASS on the initial run; file subsequently formatted |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The first authoring invocation failed before content mutation because an unescaped apostrophe in a card string caused a syntax error; it was repaired before successful integration. All numerical keys and the focused tests passed on their first run. The first separate schema-validation command failed with 193 reported errors: a six-character solution explanation `C2–C3.` violated the minimum length, rejecting the bank and causing cascading unknown-reference errors. A full verification attempt using the `verification` log directory had already started before that result was inspected; its content step failed, and its remaining processes were stopped. The explanation now states the donor-alpha/acceptor-carbonyl connection; its answer/key did not change. Separate validation then passed, and the fresh complete run using `verification-final` passed all six steps. A preliminary skill-file read used the repository directory instead of the established workspace path; applicable rules were read from the workspace. The lab's wording was clarified to describe its construction amounts as declared publicly.

Both preliminary and final logs remain outside git under `courselab-session-artifacts/codex-organic-chemistry-2026-10-09`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this increment; publication CI runs them. No person reviewed the chemistry or measured workload.

## Previous increment: General Chemistry II lessons, relaxation lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. General Chemistry II advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven original lessons develop free energy and equilibrium, coupled acid mass/charge balance, empirical/mechanistic rates, reversible/sequential kinetics, electrochemical amount accounting, ligand balance and limited coordination models, and competing solubility/complexation. One synthetic reporting-background/plateau lab and a proposed 14-week sequence complete the increment. There are 71 new items and 32 cards; the package contains 15 readings, 97 items and 52 cards. Week 12 pairs two readings. All 26 preexisting question objects and 20 cards are unchanged.

Separate calculations check all 64 numeric keys, including 18 preserved keys, and all 14 CSV cells. Root finding, component ODE integration, acid ratio normalization and free-metal balance provide alternative calculations alongside conservation and domain checks. The lab distinguishes the independent blank background from the independent equilibrium plateau, fits t00/t20 and predicts reserved t60. New numeric checks request bare numbers in stated scales; ten preserved items require units, with no significant-figure/dimensional enforcement added. The [AI-assisted check record](reviews/ai-assisted/general-chemistry-2-0.4.0.md) documents methods and repairs. The same AI assistant authored content and checks; this is not independent chemical or human review.

Three primary OpenStax Chemistry 2e pages were retrieved as link-only factual references for free energy, mechanisms and coordination properties. No teaching prose, worked problem, figure or dataset was imported, source permissions were not broadened, and no new paper identifier was introduced.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 337 lessons, 1816 questions, 1088 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-general-chemistry-2-2026-10-09/verification` | PASS: content, legacy (7), security (705 source files, 0 findings), ruff, root (1730), backend (3889 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-general-chemistry-2-2026-10-09/check_grader.py` | PASS: all 97 package items earn full credit |
| `python -B -m pytest tests/content/test_general_chemistry_two_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS after presentation/assertion repairs: 503 focused checks |
| `ruff check tests/content/test_general_chemistry_two_recalculations.py` | PASS after renaming three ambiguous variables; file formatted |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

Draft length inspection prompted a substantive reversible initial-condition paragraph before integration. An arithmetic spot-check corrected displayed ln K from 38.683145 to 38.683746; the practice key was already correct. Initial lint failed on three ambiguous variable names, then passed after renaming and formatting. The first focused suite had 493 passes and ten failures: seven standard limitation headings were missing, two number-format checks found long decimal displays, and one exact floating-point comparison needed a tolerance. Standard sections, scientific-notation displays and a tolerant assertion repaired these checks; numeric keys did not change. The complete real-grader check passed all 97 items on its first run, and all numeric-key calculations passed on their first run. The full six-step local run passed on its first run. A preliminary nonexistent `cases/` path read was replaced by the manifest's preserved self-assessment entry.

Logs remain outside git in `courselab-session-artifacts/codex-general-chemistry-2-2026-10-09/verification`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this content increment; publication CI runs them. No person reviewed the chemistry or measured workload.

## Previous increment: General Chemistry I lessons, buffer lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. General Chemistry I advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven new lessons cover atom/amount/photon accounting, bonding and geometry, reaction extent, gases and model deviations, energy and calorimetry, equilibrium and activity conventions, and acid–base discrepancy checks. One synthetic buffer lab and a proposed 14-week sequence complete the increment. There are 71 new public items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 preexisting question objects and 16 cards are unchanged.

Separate calculations check all 59 numeric keys, including 13 preserved keys, and all 14 CSV summary cells. The lab distinguishes a common reporting offset, independently supplied composition, nominal inventory approximations and full ideal charge balance beyond base exhaustion. Six authored items require significant figures, three also require units; explicit backend responses exercise conversions, precision, wrong units and near misses. The [AI-assisted check record](reviews/ai-assisted/general-chemistry-1-0.4.0.md) documents methods, repairs and source-access limits. The same AI assistant authored content and checks; this is not independent chemical or human review.

Two factual references were added as link-only records with no quotation, adaptation or redistribution permissions. NIST's defining-constants page was retrieved; the official indexed IUPAC pH definition was verified, but direct page, plain-text and PDF access returned HTTP 403. This restriction is disclosed in the source record and course limitations. No full-page IUPAC access or imported teaching material is claimed.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 329 lessons, 1745 questions, 1056 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-general-chemistry-1-2026-10-09/verification` | PASS: content, legacy (7), security (694 source files, 0 findings), ruff, root (1615), backend (3747 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-general-chemistry-1-2026-10-09/check_grader.py` | PASS: all 91 package items earn full credit, including precision formatting and the repaired CSV specification |
| `python -B -m pytest tests/content/test_general_chemistry_one_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 473 focused checks before the CSV output-column repair; the full run covers the repaired specification |
| `python -B -m pytest tests/test_general_chemistry_precision.py -q -p no:cacheprovider` from `backend/` | PASS: 6 precision/unit checks |
| `ruff check tests/content/test_general_chemistry_one_recalculations.py backend/tests/test_general_chemistry_precision.py` | PASS on the initial run; both files subsequently formatted |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The first two-file focused run had 87 passes and one long-decimal display failure; photon feedback was shortened without changing its rounded key. The initial precision suite had five passes and one failure because authored kPa units were outside the current explicit unit grammar. The pressure prompt/key/tolerance now use correctly rounded pascals for the same physical result, and Pa/MPa conversions pass. The first complete real-grader check rejected the uppercase output column `mean_pH`; upload instructions and specifications now use `mean_ph`, while the supplied raw-data header `reported_pH` remains unchanged. The complete grader rerun passed all 91 items. No chemical calculation key failed, and the full six-step local run passed on its first run. A preliminary report-check invocation used unavailable bare `python`; rerunning with the configured venv interpreter passed.

Logs remain outside git in `courselab-session-artifacts/codex-general-chemistry-1-2026-10-09/verification`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this content increment; publication CI runs them. No person reviewed the chemistry or measured workload.

## Previous increment: Calculus III lessons, flux-balance lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Calculus III advances from 0.3.1 to 0.4.0 while remaining partial, unreviewed and formative-only. Seven new lessons cover vector geometry, partial and total derivatives, Hessians and feasible constraints, multiple integrals and Jacobians, line integrals and Green, surface flux and divergence, and Stokes with spatial conservation. One synthetic boundary-flux lab and a proposed 14-week sequence complete the increment. There are 71 new public items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 preexisting item objects and 16 cards are unchanged.

Separate calculations check all 62 numeric keys, including 16 preserved keys, and all 12 CSV summary checks. The lab distinguishes signed outward transfer, face-area weighting, a common offset and the source/storage assumptions required for a sink interpretation. The [AI-assisted check record](reviews/ai-assisted/calculus-3-0.4.0.md) documents methods and repairs. The same AI assistant authored content and checks; this is not independent mathematical or human review.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 321 lessons, 1674 questions, 1024 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-3-2026-10-09/verification` | PASS: content, legacy (7), security (682 source files, 0 findings), ruff, root (1516), backend (3599 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-calculus-3-2026-10-09/check_grader.py` | PASS: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_calculus_three_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 459 focused checks |
| `ruff check tests/content/test_calculus_three_recalculations.py` | PASS after style repairs and formatting |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

An authoring-script quoted-apostrophe syntax error was repaired before mutation. A provisional box total was corrected to 8 before integration by comparing faces and volume divergence. The initial lint run autofixed 13 assigned lambdas and still failed on one ambiguous variable name, then passed after its repair. The first two-file focused suite passed 88 checks. Stronger numerical methods were added before the full run; the first expanded suite then had 458 passes and one exact floating-point equality failure in parameter invariance. A tight tolerance repaired that assertion; the final suite passed 459. No authored mathematical key failed, and the full six-step local run passed on its first run.

Logs remain outside git in `courselab-session-artifacts/codex-calculus-3-2026-10-09/verification`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this content increment; publication CI runs them. No person reviewed the mathematics or measured workload.

## Previous increment: Calculus II lessons, force-work lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Calculus II advances from 0.3.2 to 0.4.0, retaining partial, unreviewed and formative-only status. Seven new lessons cover integration structure and domains, improper limits and comparison, positive and alternating series, power-series radii/endpoints, Taylor and accumulated error, and geometric/radial integrals. One synthetic force-work lab and a proposed 14-week sequence complete this increment. There are 71 new items and 32 cards; the package contains 14 readings, 91 items and 48 cards. All 20 preexisting items and 16 preexisting cards are unchanged.

Separate calculations check all 62 numeric keys, including 16 preserved keys, and all ten lab CSV cells. The lab distinguishes a known force offset, numerical sampling, input rounding and an integrated geometric-tail certificate. The [AI-assisted record](reviews/ai-assisted/calculus-2-0.4.0.md) documents methods, focused-check failures and repairs. The same AI assistant authored content and checks; these are not independent mathematical or human review.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 313 lessons, 1603 questions, 992 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-2-2026-10-09/verification` | PASS: content, legacy (7), security (670 source files, 0 findings), ruff, root (1417), backend (3457 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-calculus-2-2026-10-09/check_grader.py` | PASS: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_calculus_two_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 442 focused checks |
| `ruff check tests/content/test_calculus_two_recalculations.py` | PASS after style correction and formatting |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The initial focused two-file run had 83 passes and two display-format failures; small errors and the long logarithm bound now use scientific notation in learner-facing prose. Exact numeric keys are unchanged. A lint autofix converted one assigned lambda to a named function. The first three-file run passed 428 checks before inspection caught a missed extension of the common lesson list; the corrected list adds fourteen structural/objective checks and the final run passed 442. No mathematical key failed, and the full six-step run above passed on its first run. Logs remain outside git under `courselab-session-artifacts/codex-calculus-2-2026-10-09/verification`. Frontend checks, the Docker Compose application stack and Playwright were not run locally for this increment; publication CI runs them. No person reviewed the mathematics or measured workload.

## Previous increment: Calculus I lessons, washout lab and proposed schedule (0.4.0, 2026-10-09)

Developed with Codex assistance. Calculus I advances from 0.3.1 to 0.4.0, retaining partial, unreviewed and formative-only status. Seven new lessons cover limits and derivative definitions, composite/implicit and related rates, constrained optimization, accumulation/substitution, numerical calculus and error, local approximation/Newton iteration, and the original semilog washout case. One synthetic-data lab and a proposed 14-week sequence complete this increment. There are 71 new items and 32 cards; the package has 14 readings, 92 items and 48 cards. All 21 preexisting item objects are unchanged.

Separate calculations check all 64 numeric keys, including the 18 preexisting ones, and all 14 lab CSV cells. The lab distinguishes a known additive background from an apparent zero-background decay rate and checks a reserved late prediction. The [AI-assisted record](reviews/ai-assisted/calculus-1-0.4.0.md) documents methods, failed focused checks and authoring repairs. These checks are not human or independent scientific review.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 305 lessons, 1532 questions, 960 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-calculus-1-2026-10-09/verification` | PASS: content, legacy (7), security (660 files, 0 findings), ruff, root (1321), backend (3315 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/codex-calculus-1-2026-10-09/check_grader.py` | PASS: all 92 package items earn full credit, including the preserved symbolic item |
| `python -B -m pytest tests/content/test_calculus_one_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS: 421 focused checks |
| `python -B -m pytest tests/content/test_calculus_one_recalculations.py tests/content/test_learner_visible_number_formatting.py -q -p no:cacheprovider` | PASS after style conversion: 78 checks |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The first focused run had 77 passes and one test-string membership error; the assertion was repaired. The first lint run found 21 assigned-lambda style violations, converted to named functions before the full run. No numeric key failed, and the full verification above passed on its first run. Logs remain outside git under `courselab-session-artifacts/codex-calculus-1-2026-10-09/verification`. Frontend, the Docker Compose application stack and Playwright were not run locally for this increment; publication CI runs them. No person reviewed the content or measured workload.

## Previous increment: linear algebra lessons, sensor lab and proposed schedule (0.3.0, 2026-10-09)

Claude's four recovered drafts were corrected and extended with Codex assistance. Linear Algebra for Modeling & Robotics advances from 0.2.1 to 0.3.0, retaining partial, unreviewed and formative-only status. Seven new lessons cover rank and identifiability, projection and QR, symmetric spectra, SVD, conditioning and ridge, centered PCA, and the existing displacement case. One synthetic sensor-geometry lab and a proposed 14-week schedule complete this increment. There are 71 new public items and 32 cards; the package has 14 readings, 91 items and 48 cards. The 20 preexisting items are unchanged.

All 69 numeric item keys and four CSV cells agree with recalculation by separate matrix operations. The lab explicitly distinguishes paired opposite demonstration errors from its separate independent-noise model. The [AI-assisted check record](reviews/ai-assisted/linear-algebra-0.3.0.md) documents corrections, failed runs and limits; these checks are not human review.

| Command/check (Linux development container, Python 3.12.3) | Result |
|---|---|
| `python -B tools/validate_content.py` | PASS: 25 packages, 297 lessons, 1461 questions, 928 cards, 25 cases; 0 errors; 98 legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-linear-algebra-2026-10-09/verification-final` | PASS: content, legacy (7), security (649 files, 0 findings), ruff, root (1232), backend (3173 passed, 2 existing symbolic-builder skips) |
| `python -B /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py linear-algebra linear-algebra-` | PASS: all 91 package items earn full credit |
| `python -B -m pytest tests/content/test_linear_algebra_recalculations.py tests/content/test_new_geroscience_and_statistics_lessons.py -q -p no:cacheprovider` | PASS: 407 focused content checks |
| `python -B -m pytest tests/content/test_content_validation.py::test_private_assessment_validator_loads_and_validates_key_only_from_separate_root tests/content/test_learner_visible_number_formatting.py tests/content/test_linear_algebra_recalculations.py -q -p no:cacheprovider` | PASS: 82 regression checks |
| `python -B tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | PASS: generated report matches |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

The first full root run had 1229 passes and three failures: a stale synthetic private-fixture inventory count, a long decimal display, and an earlier literal test assertion loaded before its repair. The fresh full run above includes all corrections. Logs are retained outside git in `courselab-session-artifacts/codex-linear-algebra-2026-10-09/verification-final`. Frontend, the Docker Compose application stack and Playwright were not run locally for this increment; publication CI runs them. No person reviewed this content or measured its workload.

## Previous patch: differential equations prompt clarification (0.3.1, 2026-10-08)

Written by Codex. Three Euler-boundary prompts now ask for a nonnegative result and explain the zero value
at equality; the resonance statements item specifies the lesson's lightly damped, directly forced system.
No key, tolerance, points, option order or objective mapping changed, as checked against commit `2c930c9`.
The version and syllabus advance to 0.3.1; all counts and partial/unreviewed/formative-only labels stay the same.
Review: [differential-equations-0.3.1.md](reviews/ai-assisted/differential-equations-0.3.1.md).

- `python -B /workspace/courselab-session-artifacts/codex-resume-2026-10-08/check_prompt_patch.py`: all 92 solution specifications, options, points and objective mappings unchanged; the three linear Euler boundary factors are zero.
- `python -B tools/validate_content.py`: PASS, 0 errors, 98 legacy-depth warnings.
- `python -B /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py differential-equations differential-equations-`: all 92 items earn full credit.
- `python -B -m pytest tests/content/test_new_geroscience_and_statistics_lessons.py tests/content/test_ai_assisted_checks.py -k differential_equations -q -p no:cacheprovider`: 81 passed, 967 deselected.

These checks ran in the same Linux development container and courselab venv as the full preceding run below.
The preceding commit's CI also passed both content/backend and frontend/browser jobs. No human review.

## Previous increment: differential equations gets a proposed 14-week schedule, seven lessons and a decay-fitting lab (2026-10-08, twenty-fifth pass)

Written by an AI coding assistant. Differential Equations for Living & Engineered Systems moves from 0.2.2 to 0.3.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 4, 6 and 11 beside the original lessons; week 13 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 970 to 1,180 words with a worked example, common mistakes, nine items and four cards: forced first-order systems (steps, ramps, sinusoids, decaying inputs and pulses in a perfused chamber); resonance and damping of a spring–mass–damper; phase portraits of linear systems; logistic growth (exact solution, fitting, extrapolation); linearization and bistability in a toggle switch; stiff equations and implicit methods; and a fitted model that predicts negative counts (model structure, step size, validation).
- **Virtual lab 1**: synthetic cell counts after a growth factor is removed, three wells at each of seven times (21 rows). Eight items (a 14-cell summary upload by time, the early-window decay rate, the zero crossing and the 48 h prediction of a straight-line fit, the first-order prediction at 48 h, a data-interpretation item on the ratio of observed to predicted counts, a structured item and a multiple-select item).
- **Review record:** [differential-equations-0.3.0.md](reviews/ai-assisted/differential-equations-0.3.0.md). All 74 numeric keys in the package, including the 14 that predate this pass, agree with independent recalculation (numerical integration of the chamber, the driven oscillator, the linear flows, the logistic equation, the toggle switch and the Michaelis–Menten depletion; finite-difference Jacobians; bisection for the Euler limits), as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 71 new items earn full credit under the real grader on the first run. Seven drafting problems, including a false statement about a forecast exceeding the carrying capacity, were fixed before the commit.
- Tests: 78 recalculation and statement checks for differential equations; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 289 lessons, 1,390 questions and 896 cards.

Codex continued the staged pass on 2026-10-08, recovered Claude's completed verification, reread the new
lessons and lab, and corrected five further details documented in the review record. These include the strict
Euler stability bound (at least 251 equal steps, rather than 250), nonnegativity at the positivity boundary,
degenerate phase portraits, the capstone's distinguishable residuals, and the resonance peak's damping
condition and forcing mechanism. No answer key or tolerance changed. The existing recalculation test now
checks both sides of the integer Euler step bound. A fresh full run after those corrections passed:

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 289 lessons, 1390 questions, 896 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `bash /workspace/.claude/skills/courselab-dev/scripts/verify.sh --log-dir /workspace/courselab-session-artifacts/codex-resume-2026-10-08/de-verification` | PASS: content, legacy (7), security (637 files, 0 findings), ruff, root (1140), backend (3031 passed, 2 symbolic-builder checks skipped) |
| `python /workspace/courselab-session-artifacts/claude-resume-2026-10-08/selfcheck.py differential-equations differential-equations-` | PASS: all 92 package items earn full credit under the real grader |
| `python3 -B /workspace/.claude/skills/regen-guardrails/scripts/claims_scan.py --repo uniStemCourseSimulators` | PASS: 0 HIGH, MED or LOW findings |

Local logs are retained outside the repository in the workspace's `courselab-session-artifacts/codex-resume-2026-10-08/de-verification` directory. Not run locally: frontend checks, the Docker Compose application stack, or Playwright for this pass. Not reviewed by a person.

## Previous increment: signals and control gets a proposed 14-week schedule, seven lessons and a step-test identification lab (2026-10-08, twenty-fourth pass)

Written by an AI coding assistant. Signals, Systems & Feedback Control moves from 0.3.1 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 4, 8 and 12 beside the original lessons; week 11 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 960 to 1,290 words with a worked example, common mistakes, eight or nine items and four cards: poles, zeros, partial fractions and the final value theorem; second-order systems (damping, overshoot, a pressure line); Bode plots (decibels, phase, delay); stability margins (gain, phase and delay margins); PI control (cancellation tuning, Ziegler–Nichols, windup); sampling, aliasing and a discrete PI controller; and a sensor filter that makes a fast loop oscillate (phase lag, crossover, a safe retuning sequence).
- **Virtual lab 1**: synthetic step tests of an incubator-like chamber at three power levels, two runs of 61 samples each (366 rows). Nine items (a 9-cell summary upload, gain, delay, an interpolated 63.2% time, time constant, a PI gain, a data-interpretation item on the linearity of the gain, a structured item and a multiple-select item).
- **Review record:** [signals-control-0.4.0.md](reviews/ai-assisted/signals-control-0.4.0.md). All 73 numeric keys in the package, including the 13 that predate this pass, agree with independent recalculation (numerical integration, bisection on the complex frequency response, a DFT for the aliases and a delay-differential simulation of the loop), as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 71 new items earn full credit under the real grader on the first run. Seven drafting problems, including a dataset that was only 97.5% settled and three schema violations, were fixed before the commit.
- Tests: 78 recalculation and statement checks for signals and control; the schedule, the no-controller-settings statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 281 lessons, 1,319 questions and 864 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 281 lessons, 1319 questions, 864 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: statics and materials gets a proposed 14-week schedule, seven lessons and a fatigue-lives lab (2026-10-08, twenty-third pass)

Written by an AI coding assistant. Statics & Mechanics of Materials moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 3, 4 and 8 beside the original lessons; week 12 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 1,050 to 1,520 words with a worked example, common mistakes, eight or nine items and four cards: stress concentrations (holes, notches, the fatigue notch factor); fatigue (Basquin, Goodman, Miner); buckling of slender struts (Euler load, slenderness); principal stresses, Mohr's circle and the Tresca and von Mises criteria; beam deflection and the flexural modulus; brittle strength and the Weibull distribution; and a failure analysis and accelerated test plan for a scaffold that meets a static strength target and collapses under cyclic perfusion.
- **Virtual lab 1**: synthetic fatigue lives of 20 specimens at four stress amplitudes, with two run-outs at the cutoff (20 rows). Eight items (a 12-cell summary upload by level, the scatter at one level, a fitted slope and Basquin exponent, a data-interpretation item on the bias of two treatments of the run-outs, an extrapolated life, a structured item and a multiple-select item).
- **Review record:** [statics-materials-0.4.0.md](reviews/ai-assisted/statics-materials-0.4.0.md). All 74 numeric keys in the package, including the 17 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 68 new items earn full credit under the real grader on the first run. Eleven drafting problems, including a reversed statement, a worked example with an impossible result and a sentence on run-outs with the wrong direction of bias, were fixed before the commit.
- Tests: 78 recalculation and statement checks for statics and materials; the schedule, the no-design-basis statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 273 lessons, 1,248 questions and 832 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 273 lessons, 1248 questions, 832 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: cellular biomechanics gets a proposed 14-week schedule, seven lessons and a stiffness and ligand-density lab (2026-10-08, twenty-second pass)

Written by an AI coding assistant. Cellular Biomechanics & Mechanobiology moves from 0.2.1 to 0.3.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 5, 8 and 10 beside the original lessons; week 13 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 900 to 1,100 words with a worked example, common mistakes, seven to nine items and four cards: oscillatory rheology (storage and loss moduli); micropillar traction forces; bonds under force and the molecular clutch; cortical tension and micropipette aspiration; the Hill function and how to choose stiffness levels; applying strain to cells (engineering and true strain, Poisson contraction, strain rate); and decoupling stiffness from ligand density and mobility, which prepares the course case.
- **Virtual lab 1**: a synthetic crossed design of stiffness (three levels) and ligand density (two levels), three gels per condition and ten cells per gel (180 rows). Eight items (an 18-cell summary upload by gel and cell counts and means, main effect, ligand effect, interaction, a gel-level standard error with an interpretation, the (wrong) cell-level standard error, a structured item and a multiple-select item), four cards and a week-13 practice assessment.
- **Review record:** [cellular-biomechanics-0.3.0.md](reviews/ai-assisted/cellular-biomechanics-0.3.0.md). All 61 numeric keys in the package, including the 9 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 64 new items earn full credit under the real grader on the first run. Four drafting problems were found and fixed before the commit, including a first version of the lab data that contradicted its own point.
- Tests: 65 recalculation and statement checks for cellular biomechanics; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 265 lessons, 1,180 questions and 800 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 265 lessons, 1180 questions, 800 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: transport gets a proposed 14-week schedule, seven lessons and an oxygen depth-profile lab (2026-10-08, twenty-first pass)

Written by an AI coding assistant. Thermodynamics & Transport in Bioengineering moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 3, 9 and 12 beside the original lessons; week 8 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 900 to 1,250 words with a worked example, common mistakes, seven or eight items and four cards: transient diffusion and the error function; advection, diffusion and the Péclet number (with the mass-transfer coefficient); oxygen in a spheroid (critical radius, anoxic core and rim); Michaelis–Menten uptake and the limits of zero order; lumped heat transfer and the Biot number; residence time, wash-in and washout and tanks in series; and a perfused construct with a hypoxic center, which prepares the course case.
- **Virtual lab 1**: synthetic oxygen depth profiles in cell-laden slabs of three thicknesses (three constructs each, 81 rows). Eight items (a 12-cell summary upload, a consumption rate, a critical thickness, the depth at which oxygen reaches zero, an anoxic thickness, a single-choice item, a structured item and a multiple-select item), four cards and a week-8 practice assessment.
- **Review record:** [transport-0.4.0.md](reviews/ai-assisted/transport-0.4.0.md). All 67 numeric keys in the package, including the 17 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them (including a numerical table checked by a separate solver). All 62 new items earn full credit under the real grader on the first run. Five drafting problems were found and fixed before the commit, including a worked example whose answer was negative.
- Tests: 72 recalculation and statement checks for transport; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 257 lessons, 1,116 questions and 768 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 257 lessons, 1116 questions, 768 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: bioreactors gets a proposed 14-week schedule, seven lessons and a kLa lab (2026-10-08, twentieth pass)

Written by an AI coding assistant. Bioreactors & Tissue Culture Engineering moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 5, 9 and 12 beside the original lessons; week 7 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 950 to 1,250 words with a worked example, common mistakes, eight or nine items and four cards: Monod growth and yield; chemostat steady states, washout and cell-specific perfusion; mixing and scale-up (power, tip speed, mixing time under three criteria); shear, eddies and the Kolmogorov scale; dissolved-oxygen control and the capacity limit; factorial design of experiments (effects, interactions, noise and curvature from center points); and designing a scale-down experiment, which prepares the course case.
- **Virtual lab 1**: synthetic dynamic gassing-out curves at three agitation speeds (three runs each, 63 rows). Eight items (a 9-cell summary upload, two kLa estimates, a speed exponent with an interpretation, a supportable cell density, a probe-lag check, a structured item and a multiple-select item), four cards and a week-7 practice assessment.
- **Review record:** [bioreactors-0.4.0.md](reviews/ai-assisted/bioreactors-0.4.0.md). All 65 numeric keys in the package, including the 12 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 65 new items earn full credit under the real grader on the first run. Seven drafting problems were found and fixed before the commit, including a statement that contradicted the lesson's own numbers and a sentence whose meaning was reversed.
- Tests: 70 recalculation and statement checks for bioreactors; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 249 lessons, 1,054 questions and 736 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 249 lessons, 1054 questions, 736 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: biomaterials gets a proposed 14-week schedule, seven lessons and a degradation time-course lab (2026-10-08, nineteenth pass)

Written by an AI coding assistant. Biomaterials & Tissue Engineering moves from 0.2.2 to 0.3.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 3, 9 and 13 beside the original lessons; week 12 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (7 to 13)**, each about 1,000 to 1,200 words with a worked example, common mistakes, seven or eight items and four cards: protein adsorption, wettability and surface coverage; hydrogel networks, modulus and mesh size; polymer chain scission, molecular weight and erosion mode; vascular scaffold wall stress, buckling, flow and wall shear stress; biocompatibility evidence and the unit of analysis; cells for a scaffold (seeding, doublings, passages and a volume check); and reading a failure in a degrading vascular scaffold, which prepares the course case.
- **Virtual lab 1**: a synthetic degradation time course (seven time points, three specimens each, 21 rows) with molar mass, mass and modulus. Eight items (a 20-cell summary upload, bonds cleaved, a rate constant, a modulus half-time with an interpretation, a time to a threshold, the first day of mass loss, a structured item and a multiple-select item), four cards and a week-12 practice assessment.
- **Review record:** [biomaterials-0.3.0.md](reviews/ai-assisted/biomaterials-0.3.0.md). All 59 numeric keys in the package, including the 10 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 63 new items earn full credit under the real grader on the first run. Seven drafting problems were found and fixed before the commit, including a rate constant that would have given a wrong sense of the time scale.
- Tests: 64 recalculation and statement checks for biomaterials; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 241 lessons, 989 questions and 704 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 241 lessons, 989 questions, 704 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: statistics gets a proposed 14-week schedule, seven lessons and a nested-design lab (2026-10-08, eighteenth pass)

Written by an AI coding assistant. Probability, Biostatistics & Experimental Design moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus, which now also lists the package's fifth outcome: the four short prototype units sit in weeks 1, 4, 6 and 8 beside the original lessons; week 12 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (9 to 15)**, each about 1,000 to 1,400 words with a worked example, common mistakes, seven or nine items and four cards: sources of variability and pseudoreplication; comparing two groups (Welch and paired t statistics, intervals for a difference); power and sample size; regression, calibration and inverse prediction; permutation, bootstrap and rank-based methods; base rates, positive predictive value and replication; and planning a confirmatory study from a pilot, which prepares the course case on a pilot with p = 0.04 for one of 18 biomarkers.
- **Virtual lab 1**: synthetic nested readings (four animals per group, three readings each, 24 rows). Seven items (a 16-cell per-animal summary upload, a technical SD, two data-interpretation items that compare the reading-level and animal-level t tests, an intraclass correlation, a structured item and a multiple-select item), four cards and a week-12 practice assessment.
- **Review record:** [statistics-0.4.0.md](reviews/ai-assisted/statistics-0.4.0.md). All 57 numeric keys in the package, including the 17 that predate this pass, agree with independent recalculation, as do the lab keys against its CSV and the numbers the lessons quote without asking for them. All 58 new items earn full credit under the real grader. Six drafting problems were found and fixed before the commit, including two lab items that used a unit the grader does not support.
- Tests: 65 recalculation and statement checks for statistics; the schedule, the no-protocol statements, the syllabus outcomes and the lab keys against its CSV have tests; the inventory pins moved to 233 lessons, 926 questions and 672 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 233 lessons, 926 questions, 672 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: biochemistry gets a proposed 14-week schedule, six lessons and an enzyme-kinetics lab (2026-10-08, seventeenth pass)

Written by an AI coding assistant. Biochemistry I: Proteins, Enzymes & Metabolism moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 5, 9 and 12 beside the original lessons; week 7 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Six lessons (8 to 13)**, each about 1,000 to 1,250 words with a worked example, common mistakes, seven items and four cards: amino acids, charge and isoelectric points; protein folding and stability; glycolysis, energy charge and why AMP is a sensitive signal; mitochondrial bioenergetics (proton-motive force, ATP yield, leak); flux control, pool sizes and the layers of regulation; and reading a metabolic perturbation, which prepares the course case on a respiratory-chain inhibitor that lowers ATP and raises lactate.
- **Virtual lab 1**: synthetic replicate initial rates for an enzyme with and without a competitive inhibitor (36 rows). Seven items (a 10-cell summary upload, a double-reciprocal fit with an interpretation, apparent Km, an inhibition constant, a structured item and a multiple-select item), four cards and a week-7 practice assessment.
- **Review record:** [biochemistry-0.4.0.md](reviews/ai-assisted/biochemistry-0.4.0.md). All 63 numeric keys in the package, including the 15 that predate this pass, agree with independent recalculation, and the lab fit recovers the parameters its data were built from. All 49 new items earn full credit under the real grader. Six drafting problems were found and fixed before the commit, including a capstone sentence that contradicted its own numbers and a significant-figures request that the grader would have scored wrongly.
- Tests: 63 recalculation tests for biochemistry; the schedule, the no-protocol statements and the lab keys against its CSV have tests; the recalculation helper now uses the validator's absolute-plus-relative tolerance; the inventory pins moved to 225 lessons, 868 questions and 640 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 225 lessons, 868 questions, 640 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: physiology gets a proposed 14-week schedule, seven lessons and a scratch-assay lab (2026-10-08, sixteenth pass)

Written by an AI coding assistant. Human Physiology for Engineers moves from 0.3.2 to 0.4.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 3, 5 and 11 beside the original lessons; week 13 is a lab and week 14 a lesson that prepares the existing course case. The manifest says the schedule is not evidence of semester equivalence.
- **Seven lessons (8 to 14)**, each about 950 to 1,350 words with a worked example, common mistakes, seven or eight items and four cards: balance and feedback gain (with heat balance); membrane potential (Nernst, GHK, extracellular potassium); hemodynamics; respiratory mechanics and gas exchange (ventilation, the alveolar gas equation, compliance, shunt); skeletal muscle mechanics (length–tension, Hill's relation, power); tissue repair and closure kinetics; and compensation and reserve.
- **Virtual lab 1**: a synthetic scratch assay with a control, a migration inhibitor and a division block, four independent experiments each and five time points (60 rows). Seven items (a 9-cell summary upload, a rate with an interpretation, three ratio or speed items, a structured item and a multiple-select item), four cards and a week-13 practice assessment.
- **Review record:** [physiology-0.4.0.md](reviews/ai-assisted/physiology-0.4.0.md). All 57 numeric keys in the package, including the 17 that predate this pass, agree with independent recalculation; all 56 new items earn full credit under the real grader. Five drafting problems were found and fixed before the commit, including an inconsistent resting heat loss and a learning objective with no item.
- Tests: 57 recalculation tests for physiology (plus a check that the closed-form load for peak muscle power matches a grid search); the schedule, the no-advice statements and the lab keys against its CSV have tests; the inventory pins moved to 218 lessons, 819 questions and 612 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 218 lessons, 819 questions, 612 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: number-formatting defects fixed and common-mistakes sections backfilled (2026-10-08, fifteenth pass)

Written by an AI coding assistant. No answer key, tolerance or objective changed. Thirteen packages move up one patch version and stay `partial`, unreviewed and formative-only.

- **Number-formatting defects in learner-visible text.** Reading the earlier lessons for the backfill showed text such as "0.15000000000000002 mol/m³" and "2.0e-10 mmol per cell per hour". A scan of every reading, prompt, option, solution, card and worked-example summary found about 40 instances in eight packages (bioreactors, transport, biochemistry, calculus 2, differential equations, physics EM, statics and materials, programming). They came from early authoring batches that ran before the notation converter existed. They are rewritten as 2.0×10⁻¹⁰ and 0.15, or placed in code spans where they are Python literals (programming). One value, 1.12e+07, was rewritten as 1.125×10⁷ because the exact value is 1.125×10⁷ and rounding it to 1.12 or 1.13 would be arbitrary.
- **New guard.** `tests/content/test_learner_visible_number_formatting.py` scans readings (outside code spans) and learner-visible JSON text for raw exponent notation and long floating-point runs. It fails on the previous commit's content (2 failures) and passes now. The programming package is exempt because it teaches Python literals.
- **Common-mistakes sections** were added to 22 original lessons in ten packages that lacked one (biochemistry 5 and 6; biomaterials 5 and 6; bioreactors 5; differential equations 5; geroscience 5 to 14; organic chemistry 5; physiology 5 and 6; programming 5; statistics 6; transport 5). Each bullet names a mistake that the lesson's own text addresses. The two labs and the short statistics unit 5 have a different structure and were left alone. The earlier AI-assisted check of genetics had found the same gap there.
- Tests: two version pins (statistics 0.3.2, geroscience 0.5.2) were updated. No assertion about maturity or review changed.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 210 lessons, 762 questions, 580 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: genetics gets a proposed 14-week schedule, six lessons and an association lab (2026-10-08, fourteenth pass)

Written by an AI coding assistant. Genetics & Genomics moves from 0.4.2 to 0.5.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** (`duration.weeks`) and a regenerated syllabus: the four short prototype units sit in weeks 1, 4, 9 and 11 beside original lessons; week 12 is a lab and week 14 a follow-up design lesson with the course case. The manifest says the schedule is not evidence of semester equivalence.
- **Six lessons (10 to 15)**, each 1,000 to 1,400 words with a worked example, common mistakes, six items and four cards: epistasis, complementation and modified dihybrid ratios; X-linked inheritance with Bayesian carrier risk; nondisjunction and maternal age; mutation rates, the fluctuation test and somatic mutation; measuring gene expression with normalization and false-discovery control; and the follow-up design of an association locus (fine-mapping, allele-specific expression, perturbation).
- **Virtual lab 1**: a synthetic case–control study of 100 people in two populations, three variants, with a CSV. One variant's strong pooled signal is entirely confounded by population, one is a real association that survives stratification, and one is null. Seven items (12-cell summary upload, two data-interpretation items, two numeric items, a structured item and a multiple-select item), four cards and a week-12 practice assessment.
- **Common-mistakes sections** for lessons 5 to 8, which the earlier AI-assisted check found missing.
- **Four link-only references** (records resolved; three abstracts read; one scanned 1943 paper not read, which the lesson says).
- **Learner-facing limitations** recomputed for the package; one new limitation says the family calculations give no counselling or medical advice.
- **Review record:** [genetics-0.5.0.md](reviews/ai-assisted/genetics-0.5.0.md). All 43 new keys agree with independent recalculation and earn full credit under the real grader. Seven drafting problems were found and fixed before the commit, among them a wrong oogenesis simplification and a schema violation that the validator caught.
- Tests: 24 new numeric keys are recalculated independently (50 recalculation tests in all); the schedule, the no-advice statement and the lab's keys against its CSV (including pooled, stratified and Mantel–Haenszel odds ratios) have tests; the inventory pins moved to 210 lessons, 762 questions and 580 cards.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 210 lessons, 762 questions, 580 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | see the PROGRESS.md entry for this pass |

Not run: frontend checks, Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: reviewer guide, an AI-assisted check of genetics, and stale limitation text (2026-10-08, thirteenth pass)

Written by an AI coding assistant. The owner said friends, relatives, university contacts, freelancers, and the owner with AI could all review, and that AI with data processing would do best. The repository's standard still requires actual human review for `complete` and named, qualified, independent review for `externally reviewed`. So AI checks are recorded as a separate, labelled layer that changes no label.

- **[Reviewer guide](REVIEWER_GUIDE.md)**, a [lesson review form](review-templates/lesson-review.md) and a GitHub "Course feedback" issue form. They describe three kinds of review (reader feedback, AI-assisted check, subject-matter review), what each can change, and how a named review is recorded.
- **[AI-assisted check of genetics 0.4.1](reviews/ai-assisted/genetics-0.4.1.md).** All 23 numerical keys agree with an independent recalculation, kept as tests in `tests/content/test_ai_assisted_checks.py` together with an exact noncentral-t power calculation. No key was wrong. Six text findings were fixed in genetics 0.4.2. The most important: the perturbation lesson advised 4 replicates per group, which gives about 66% power; the exact t-test needs 6 for 80%.
- **Stale learner-facing limitations** in all 25 packages were replaced with text computed from each package: items per unit and lesson, and how many numerical answers require a unit or check significant figures or dimensions. Geroscience no longer says it lacks a 14-week schedule, statistics no longer describes "one supplemental original unit", and cell biology no longer says some objectives are unassessed. These changes are folded into the unpublished x.y.1 versions, and their history entries say so.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 203 lessons, 719 questions, 552 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | all steps PASS: root 247 passed (26 new recalculation tests); backend 1689 passed, 2 skipped; security scan 0 findings; ruff clean; legacy 7/7 |

Not run: Docker Compose, Playwright for this pass. Not reviewed by a person.

## Previous increment: browser QA of protected graded assignments, and three fixes it found (2026-10-08, twelfth pass)

Written by an AI coding assistant, after the owner asked for the protected, graded mode to be tested automatically rather than by hand. Details, commands and limits are in [QA_PROTECTED_GRADED.md](QA_PROTECTED_GRADED.md).

- **Harness.** `tools/qa/build_protected_fixture.py` builds a throwaway deployment outside the repository (genetics switched to a graded, protected policy, three QA assignments whose keys live only in a private store, a sentinel string in every private solution). `tools/qa/run_protected_e2e.sh` migrates a SQLite database and starts the API and the Vite dev server. It then runs `frontend/e2e/protected-graded.spec.ts` in Chromium. The spec is skipped in the default Compose run because the committed packages are formative-only. No committed package changed its grading mode, and no answer key was committed.
- **Defects found and fixed, each with a regression test that fails without the fix:**
  1. The grade calculation re-checked protection without the pinned source paths. Every protected graded course therefore answered 409 on its gradebook, which also hid the assessment plan and the assignment (`main.py`; `test_protected_course_gradebook_counts_private_graded_work`).
  2. Graded submissions accepted only `[a-z0-9_-]` question ids, while content ids may contain `:` and `.`. An assignment written with the usual `lesson:slug` ids could never be submitted (`schemas.py`; `test_graded_assignment_accepts_authored_colon_and_dot_question_ids`).
  3. The assignment view did not count a just-saved attempt, so the counter stayed at 0 and the form stayed open after the last allowed attempt. The server still refused the extra attempt (`GradedAssessment.tsx`; new unit test).
- **After the fixes,** both protected browser tests pass. The run covered the plan, accessibility (axe), incomplete submissions, wrong and right attempts with unit diagnosis, the attempt limit, the policy-based course grade, a human-review request, persistence after reload, refusals for past-deadline and unreleased work, and the data export. No API response or page text contained the private sentinel, `solution_spec` or `private://`.

| Command/check (this container, Python 3.12.3, Node with Vite 7, Chromium headless shell 153, 2026-10-08) | Result |
| --- | --- |
| `tools/qa/run_protected_e2e.sh` (protected spec) | first run: 3 defects; after fixes: 2 passed |
| `playwright test` (whole suite, committed content, Vite dev server instead of nginx) | 19 passed, 2 skipped (protected spec), 1 failed: the nginx-only check that `/content`, `/legacy` and `/.env` return 404, which the Vite dev server does not provide. CI runs it against nginx. |
| `verify.sh --frontend` | all steps PASS: root 221 passed; backend 1689 passed, 2 skipped; frontend 37 unit tests, lint, build (208 modules), bundle scan 0 findings; security 522 files, 0 findings; ruff clean; legacy 7/7 |

Not run: Docker Compose with a protected course, other browsers, load or security testing beyond the leak checks. Not reviewed by a person.

## Previous increment: assessments list the course outcomes they cover; syllabi brought up to date (2026-10-08, eleventh pass)

Written by an AI coding assistant, following the owner's decision that assignments can list the course outcomes they cover.

- **Outcome mapping, derived rather than asserted.** Each assessment with items now also lists the course outcomes that its own items assess: item → the lesson objective it is tagged to → that objective's `course_outcome_ids`. 255 outcome ids were added across 25 packages. Rubric-only cases list none, and neither do the 92 practice assessments of the short prototype units, whose 184 objectives are not linked to any outcome (linking them is a judgement for a subject-matter reviewer; the gap report lists them). Every course outcome is now listed by at least one assessment, so the validator's `objective-coverage` warning is gone (warnings: 123 → 98, all legacy-depth). A listed outcome means at least one item touches it, not that it is assessed in depth.
- **New validator rules.** `unsupported-outcome-mapping` rejects an outcome that none of the assessment's items assesses (including on rubric-only cases), and `syllabus-version` rejects a syllabus that does not state the manifest version.
- **Stale syllabi fixed.** 23 of 25 syllabi still said "Version: 0.1.0", listed only the four original units and described "one public formative check and two retrieval cards" per unit. They were regenerated from the manifests: current version, every lesson with its reading type and item and card counts, the current practice description and limitations. Cell biology and geroscience keep their hand-written week tables (version line updated).
- Every package moves up one patch version with a history entry (for example genetics 0.4.0 → 0.4.1, geroscience 0.5.0 → 0.5.1, cell biology 0.19.0 → 0.19.1); all stay `partial`, unreviewed and formative-only. No reading, item or key changed.
- Tests: the inventory test now asserts no objective-coverage warning; new tests check that each assessment lists exactly the outcomes its items assess, that unsupported mappings and stale syllabus versions are rejected, and that syllabi list every lesson; five version pins were updated.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 203 lessons, 719 questions, 552 cards, 25 cases; 0 errors; 98 disclosed legacy-depth warnings |
| `verify.sh` | all steps PASS: root 221 passed; backend 1687 passed, 2 skipped; security 518 files, 0 findings; ruff clean; legacy 7/7 |

Not run for this increment: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: a proposed 14-week geroscience schedule, a lifespan lab and a design lesson (2026-10-08, tenth pass)

Written by an AI coding assistant. Geroscience & Regenerative Biology moves to 0.5.0 and stays `partial`, unreviewed and formative-only.

- **Proposed 14-week schedule** in `course.json` (`duration.weeks`) and the syllabus: weeks 1 to 12 pair the compact prototype units with the original lessons; week 13 is a lab and week 14 a design lesson with the course case. The manifest says the schedule is not evidence of semester equivalence. The syllabus sections on structure, assessment and limitations were regenerated from the manifest (the previous text still described version 0.2.0 and eight units).
- **Virtual lab 1** (`labs/01-lifespan-cohort-censoring-and-survivor-bias.md`, `labs/lifespan-cohort.csv`): 24 synthetic animals, two censored at study end, and a grip-strength measure taken only in survivors. Five items (CSV summary with recalculated keys, Kaplan–Meier median, a naive-mean lower bound, structured bias reasoning, supported conclusions), four cards, one week-13 practice assessment.
- **Lesson 16, designing a credible aging-intervention study**: endpoints, Schoenfeld's event count for a survival comparison, animals needed, and safeguards (randomization, blinding, both sexes, several sites, pre-registration).
- **Test harness fix:** `backend/tests/test_authored_items.py` wrote numeric keys as raw floats, so an integer key with a three-significant-figure requirement (821) was submitted as "821.0" and failed. It now writes keys to the required significant figures, keeping trailing zeros, as a learner would. All 1,432 authored-item checks pass.
- New tests check that every geroscience lesson is scheduled exactly once, that no assessment is graded, that the package stays partial and unreviewed, and that the lab's keys match its CSV (including a recomputed Kaplan–Meier median).

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 203 lessons, 719 questions, 552 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 216 passed; backend 1687 passed, 2 skipped; security 518 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: ten research-skill lessons (2026-10-08, ninth pass)

Written by an AI coding assistant. Ten original lessons of about 820 to 900 words, each with common mistakes, a worked problem, six items and four cards: statistics (multiple testing with Bonferroni and Benjamini–Hochberg; effect sizes, confidence intervals and regression to the mean), programming (algorithmic cost and data structures; floating-point rounding and cancellation, with runnable Python snippets), geroscience (biomarker reliability, smallest detectable change and surrogate endpoints, stating no claim that any intervention changes human aging), genetics (Mendelian randomization), biochemistry (binding equilibria, ligand depletion, Hill cooperativity), physiology (Starling forces and edema), signals and control (convolution and sensor lag) and robotics (joint torque budget, encoder resolution, backlash and failure limits). Statistics, programming, biochemistry, physiology, signals and control, and robotics move to 0.3.0; geroscience and genetics to 0.4.0; all stay `partial`. 60 keys were graded to full credit. The authoring pipeline's notation converter was changed to leave fenced and inline code untouched, and a test checks that the Python snippet keeps its `1e8` literals. Two existing tests pinned the statistics and geroscience versions and were updated; their maturity and review assertions are unchanged.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 201 lessons, 708 questions, 544 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` (first run) | content, legacy, security (505+ files, 0 findings), ruff, backend (1665 passed, 2 skipped) PASS; root pytest 2 failed on version pins |
| `python -m pytest tests -q` after the pin update | 212 passed |

Not run: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: twelve lessons that link every course outcome (2026-10-08, eighth pass)

Written by an AI coding assistant. Twelve original lessons of about 810 to 910 words, each with common mistakes, a worked problem, six items and four cards, written for the 19 course outcomes that no lesson objective linked to: bioreactors (cell-culture mass balance), transport (perfusion tubing: balances, Reynolds number, pressure drop), calculus 1 (limits, continuity and net change), calculus 2 (Taylor error bounds), calculus 3 (constrained optimization and polar integrals), circuits (RC frequency response and aliasing), general chemistry 1 (polarity, partitioning and calorimetry), general chemistry 2 (Nernst equation and metal centers), organic chemistry (SN1/SN2 and stereochemistry), physics EM (induction, flow meters and current limits, with a synthetic limit that is explicitly not safety guidance), physics mechanics (centrifuge rotation) and statics (forearm equilibrium). The twelve packages move to 0.3.0 and stay `partial`. 72 keys were graded to full credit. Pre-commit checks caught three short feedback strings, three readings under 800 words, a source id not used by the package and a muscle-stress example whose synthetic area gave an implausible stress; all were fixed.

The [gap report](COURSE_GAP_REPORT.md) now shows 0 of 101 course outcomes without a linking lesson objective. The validator's `objective-coverage` warning still appears for all 25 packages: it counts a course outcome as covered only when an assessment lists the outcome id directly, which no package (including cell biology) does. Listing outcome ids on assessments is an authoring-policy decision for a reviewer, so the warning was left in place rather than silenced.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 191 lessons, 648 questions, 504 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 190 passed; backend 1545 passed, 2 skipped; security 505 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: calculus 3 and robotics lessons (2026-10-08, seventh pass)

Written by an AI coding assistant. Calculus 3 (gradients in a synthetic concentration field: partial and directional derivatives, steepest ascent, Fick's law and what fraction of the concentration differs across a cell) and robotics (planar two-link arm: forward and inverse kinematics, reachability, singularity, joint-error propagation for lab positioning), each 0.2.0 and still `partial`, with six items whose keys were graded to full credit and four cards. Every package now has at least one lesson-length original reading. Unlinked course outcomes: 19 of 101.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 179 lessons, 576 questions, 456 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 166 passed; backend 1401 passed, 2 skipped; security 493 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks, Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: biomechanics, linear algebra, physics and engineering lessons (2026-10-08, sixth pass)

Written by an AI coding assistant. Nine original lessons of about 830 to 950 words, each with a common-mistakes section, a worked problem, six items and four cards, all with synthetic values: cellular biomechanics (Hertz indentation and viscoelastic relaxation; separating substrate stiffness from ligand density with a 2×2 factorial and traction forces), linear algebra (least-squares calibration with normal equations and residuals; Markov chains for cell-state transitions), statics and materials (bending of a long bone), physics mechanics (impact forces), physics EM (the membrane as a capacitor), circuits (sensor loading and ADC resolution) and signals and control (proportional control of an incubator). Seven packages move to 0.2.0 and stay `partial`. 54 keys were graded to full credit by the real grader. Two authoring defects were caught before commit: a hint below the schema's minimum length, and prompts whose very small SI answers invited a ×10ⁿ notation the grader does not parse; those answers now use scaled units (nN, pC, MV/m). Unlinked course outcomes: 25 of 101. Only calculus 3 and robotics remain at legacy depth.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 177 lessons, 564 questions, 448 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 162 passed; backend 1377 passed, 2 skipped; security 491 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks (no frontend change), Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: chemistry and mathematics lessons (2026-10-08, fifth pass)

Written by an AI coding assistant. Eight original lessons of about 830 to 900 words, each with a common-mistakes section, a worked problem, six or seven items and four cards, all with synthetic values: general chemistry 1 (solution preparation, dilution and propagated error), general chemistry 2 (buffer design, capacity and ionization; integrated rate laws and Arrhenius), organic chemistry (acyl reactivity, side-chain ionization, glycation and a modification-versus-turnover steady state that makes no claim about any person), calculus 1 (derivatives in exponential and logistic growth), calculus 2 (integrals as accumulation, trapezoid and Simpson with an error bound, improper integrals) and differential equations (a well-mixed perfused chamber with Euler stability; equilibria, harvesting and a two-compartment eigenvalue analysis). The six packages move to 0.2.0 and stay `partial`. 49 keys were graded to full credit by the real grader. The lesson tests found two gaps before commit (a missing synthetic label and an objective with no item); both were fixed. Unlinked course outcomes: 48 of 101.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 168 lessons, 510 questions, 412 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` | all steps PASS: root 144 passed; backend 1269 passed, 2 skipped; security 482 files, 0 findings; ruff clean; legacy 7/7 |

Not run: frontend checks (no frontend change), Docker Compose, Playwright. Not reviewed by a subject-matter expert.

## Previous increment: genetics lessons 7 and 8 (2026-10-08, fourth pass)

Written by an AI coding assistant. Genetics moves to 0.3.0 (still `partial`) with two more original lessons: three-point mapping (gene order from double-crossover classes, interval distances, coefficient of coincidence and interference, Haldane's map function) and designing a controlled gene-perturbation experiment (tool choice, specificity controls including rescue, ΔΔCt quantification and its assumptions, biological versus technical replication, a normal-approximation sample size). Synthetic counts and Ct values; 12 items whose keys were graded to full credit by the real grader; 8 cards. Every genetics course outcome is now linked from a lesson objective; package-wide, 63 of 101 outcomes remain unlinked.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 160 lessons, 461 questions, 380 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `verify.sh` (root and backend pytest, security, ruff, legacy) | all steps PASS: root 128 passed; backend 1171 passed, 2 skipped; security 474 files, 0 findings; ruff clean; legacy 7/7 |

Docker Compose, Playwright and the frontend checks were not run (no frontend change). Not reviewed by a subject-matter expert.

## Previous increment: two lessons each in genetics, biochemistry, physiology and biomaterials (2026-10-08, third pass)

Written by an AI coding assistant.

- **Genetics, biochemistry, physiology and biomaterials 0.2.0** (all still `partial`). Each package gains two original lessons of about 810 to 990 words, each with a worked problem that is not a repeat of the body text, six or seven formative items and four cards: Hardy–Weinberg departures and carrier frequency; heritability and polygenic scores; enzyme kinetics and inhibition fingerprints; actual versus standard free energy, coupling and redox; oxygen delivery and the Fick principle; renal clearance; hydrogel degradation and release; scaffold porosity, stiffness and permeability. All parameters are synthetic. Numeric keys are computed in the authoring script from the prompt values, and all 49 keys were graded to full credit by the real grader before commit. No third-party source was added.
- The [gap report](COURSE_GAP_REPORT.md) was regenerated: course outcomes with no linking lesson objective fell from 79 to 65 of 101.
- Tests: the 2026-10-08 lesson checks now cover these eight lessons; inventory pins were updated to the new counts.

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 158 lessons, 449 questions, 372 cards, 25 cases; 0 errors; 123 disclosed warnings (98 legacy-depth, 25 objective-coverage) |
| `python -m pytest tests -q` | 124 passed (after the pin fix) |
| `cd backend; python -m pytest -q` | 1147 passed, 2 skipped |
| `python tools/check_security.py` | 472 source files, 0 findings |
| `ruff`, `node --test` legacy | PASS |

The first full run of `verify.sh` failed one root test because an inventory pin (401 → 450 with the private fixture) had not been updated; it was fixed and the root suite rerun. The frontend was not changed, so `--frontend` was not run. Docker Compose and Playwright were not run. No lesson was reviewed by a subject-matter expert.

## Previous increment: assessment-protection toggle, six geroscience lessons, a time-to-event lesson (2026-10-08, second pass)

Written by an AI coding assistant.

- **Assessment protection toggle.** `grading_policy.assessment_protection` is `open` (default) or `protected`; the operator variable `ASSESSMENT_PROTECTION` (`course`, `protected`, `open`) can force either. In protected mode a graded assessment must read from the private store; a public source is refused when the plan is built and when questions are served, so switching a live deployment to protected closes open graded assessments. The plan response reports the mode in force and the plan view labels it. Open mode does not make keys secret and says so. Practice items are public in both modes. Documented in `docs/DEPLOYMENT.md` and `docs/AUTHORING_GUIDE.md`; 7 backend tests and 1 frontend test.
- **Geroscience 0.3.0.** Six original lessons (genome instability and repair; proteostasis, autophagy and mitochondria; nutrient sensing and lifespan interventions; regeneration across species; reading an aging-intervention paper; evidence tiers from model to human) of about 870 to 1,200 words each, with synthetic tables, worked examples, 31 practice items, 24 cards and link-only references whose identifiers were checked on 2026-10-08 (title resolution only; claim support is a reading judgement). Their objectives are linked to the four course outcomes, so no geroscience outcome is unlinked. The lessons state that no intervention is claimed to slow or reverse human aging.
- **Transport, bioreactors and programming 0.2.0.** One original lesson each: oxygen limits in thick constructs (zero-order uptake, critical thickness, a diffusion-to-consumption ratio), sizing oxygen supply (kLa, supportable cell density, static-dish medium depth, limits of empirical correlations), and testing a scientific function (known-answer tests, float tolerances, seeds, provenance). Parameters are synthetic; each has 5 to 6 items with computed keys and 4 cards; their modules reuse the packages' existing curriculum-comparator sources.
- **Statistics 0.2.0.** One lesson on censoring, a hand-checkable Kaplan-Meier table, median survival and rate/hazard ratios, with five items and four cards.
- Tests: `tests/content/test_new_geroscience_and_statistics_lessons.py` (labelling, synthetic data, no advice phrases, outcome links, link-only sources, labels unchanged).

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 150 lessons, 400 questions, 340 cards, 25 cases; 0 errors; 123 disclosed warnings (98 legacy-depth, 25 objective-coverage) |

| `python -m pytest tests -q` | 108 passed |
| `cd backend; python -m pytest -q` | 1049 passed, 2 skipped |
| `python tools/check_security.py` | 464 source files, 0 findings |
| `ruff`, `node --test` legacy, `verify.sh --frontend` (lint, unit tests including the protection label, build, bundle scan) | PASS |

Not run here: Docker Compose and the Playwright end-to-end suite. Nothing here is reviewed; the lessons were not read by a subject-matter expert, and the references were checked for existence, not for support of each sentence.

## Previous increment: homework companions, a third lab, specifications and objective items (2026-10-08)

Written by an AI coding assistant. Foundations of Cell and Molecular Biology advances from 0.18.0 to **0.19.0** and remains `partial`, unreviewed and `formative-only`. The increment adds:

- Seven open formative homework companions (Homework 2 to 8) with synthetic datasets, a recalculated CSV summary check, a graph or data-interpretation check where it fits, structured control logic, a multiple-select item and three retrieval cards each (160 practice points in total).
- A third synthetic virtual lab (week 14, lineage-marker time course, 21 practice points) with fraction-versus-count reasoning.
- Two practice items for the lesson-3 free-energy objective, which had none.
- Specification-only documents for the midterm, cumulative final and integrative project (`content/courses/cell-biology/assessment-specs/`): draft blueprints generated from `course.json`, requirements, a draft project rubric and reviewer checklists. They contain no items, keys or scoring and have not been reviewed.
- 96 practice items, one for each lesson objective that had no assessment mapping in the 24 other packages (55 numeric, 41 single choice). Every numeric key is computed in the authoring script from the numbers in its prompt, and the item feedback carries the explanation because the legacy readings are brief.
- `tools/objective_coverage.py` and the generated [gap report](COURSE_GAP_REPORT.md). It shows that no lesson objective lacks an assessment mapping or practice item, and that 91 of 101 course outcomes are still not linked from any lesson objective, which is why the validator's `objective-coverage` warning (25) is unchanged and was deliberately not silenced.
- Tests: `tests/content/test_cell_biology_integrity.py` (links resolve, every CSV key has a recalculation, example tables equal the keys, specifications hold no keys, labels unchanged, gap report current) and `backend/tests/test_authored_items.py`, which grades every public practice item against its own key and checks that a deliberately wrong answer earns nothing (688 checks, 2 symbolic items skipped).

| Command/check (this container, Python 3.12.3, 2026-10-08) | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 140 lessons, 347 questions, 300 cards, 25 cases; 0 errors; 123 disclosed warnings (98 legacy-depth, 25 objective-coverage) |
| `python -m pytest tests -q` | 84 passed (75 before; 9 new integrity tests; inventory and schedule pins updated) |
| `cd backend; python -m pytest -q` | 936 passed, 2 skipped (248 before; the new authored-item tests) |
| `python tools/check_security.py` | 452 source files, 0 findings |
| `ruff` | clean |
| `node --test` legacy | 7 passed |
| `verify.sh --frontend` (lint, unit tests, build, bundle scan) | PASS |

Not run in this container: Docker Compose, the Playwright end-to-end suite, the production compose file. What the new material does not show: no review of any kind, no accessibility check by a person, no measured workload, no protected answer package, and no evidence that the generated synthetic datasets teach well. The practice keys are public by design.

## Previous increment: Geroscience & Regenerative Biology original lessons (2026-10-07)

Geroscience & Regenerative Biology advances to **0.2.0** and remains `partial`. Four original lessons with explicitly synthetic data follow the four preserved compact units. The package adds 15 formative items, 16 cards and 21 link-only scientific references, each checked against its PubMed title and DOI on 2026-10-07; findings are summarized qualitatively without reproducing source data. Every lesson objective now links to a course outcome. The four legacy checks are retagged to the objectives their prompts assess, and the change is recorded in each item's provenance. Every keyed answer was graded by the production grader (full credit for the key, zero for representative wrong answers, partial credit for split data-interpretation responses), and a new content test independently recalculates each numerical key from the lesson tables.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 132 lessons, 211 questions, 275 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 215 supported practice specifications |
| `python -m pytest tests -q` | 75 passed (inventory pins updated; new geroscience recalculation test) |
| `cd backend; python -m pytest -q` | 248 passed |

## Previous increment: spaced retrieval queue and unassessed objectives (2026-10-07)

Adds Alembic revision `0008` (`card_reviews`), an append-only record of each learner self-rating with the card-text SHA-256, policy version and resulting schedule. `retrieval-schedule-v1` is deterministic and unit-tested: 10-minute relearn after `again`, then 1 day, 6 days and interval × ease for `good`; `hard`/`easy` adjust interval and ease; ease stays within 1.3–3.0 and intervals are capped at 365 days. `GET /api/v1/reviews/{course}` returns due, not-yet-reviewed and later cards for lesson-published cards only; `POST /api/v1/courses/{course}/cards/{card}/reviews` requires session, CSRF and a current enrollment. Edited card text starts a new schedule. Learner export and deletion include the new rows. The gradebook now lists authored objectives with no tagged item as `no items`; the response schema accepts that status, which the uncommitted draft omitted. Ratings do not change scores, objective evidence or grades, and no retention benefit is claimed.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 128 lessons, 196 questions, 259 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `python -m pytest tests -q` (Linux dev container, Python 3.12) | 74 passed |
| `cd backend; python -m pytest -q` | 248 passed (17 new retrieval/gradebook tests, including Alembic `check` against the new metadata) |
| `ruff check backend tools tests` | PASS |
| `cd frontend; npm run lint` | PASS |
| `cd frontend; npx vitest run` | 35 passed (4 new review-queue tests) |
| `cd frontend; npm run build` | PASS |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 424 source files |
| `npm run test:legacy` | PASS |
| Compose/Playwright E2E | Not run locally: this Linux container has no Docker engine. Hosted CI runs the Compose E2E job. |

## Previous increment: protected assessment-source boundary (2026-10-06)

Added an optional protected assessment root distinct from public course content. Graded manifests can refer to `private://` sources resolved only below the configured per-course directory; Docker Compose mounts that directory read-only for server-side use. Public/private root overlap, path traversal, file or course-directory symlink escape, absent configuration and missing files fail closed. Existing enrollment snapshots pin the source SHA-256; learner APIs omit both answer specifications and private source paths. No real answer key was added, no current course uses the private source, and all 25 packages remain formative-only. This is infrastructure for future assessed coursework, not a new graded assignment or course maturity change.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 128 lessons, 196 questions, 259 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 72 passed, 2 skipped |
| `backend/.venv/Scripts/python.exe -m pytest backend/tests -q` | 229 passed, 1 skipped; one upstream Starlette/httpx deprecation warning |
| `backend/.venv/Scripts/ruff.exe check backend tools tests` | PASS |
| `cd frontend; npm run lint` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run build` | PASS: TypeScript and Vite production build (206 modules) |
| `cd frontend; $env:E2E_BASE_URL='http://localhost:8080'; npm run test:e2e` | 20 passed against the final rebuilt Compose app |
| `npm run test:legacy` | 7 passed |
| `docker compose config --quiet` | PASS |
| `docker compose -f compose.production.yaml config --quiet` | PASS with documented sample environment values |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing database volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 200 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok`; programming runner and LLM feedback disabled |
| Protected mount write probe in API container | PASS: mount is read-only |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 418 source files |
| `git diff --check` | PASS |
| Hosted GitHub Actions run [37560199350](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37560199350) | PASS: content/backend and frontend/E2E jobs |

The source resolver and API tests confirm the key is read only from the private mount, is not returned in course/lesson/assessment DTOs, and is not substituted from similarly named public files. A missing key blocks graded enrollment-plan creation. Symlink-escape tests are skipped because this Windows host does not permit creating test symlinks; lexical traversal and root-overlap rejection passed. No current catalog course is affected because none references a private source.

Published in commit `86188bbcba2828ae00fbade1a86cfa737e4b309c`; the hosted content/backend and frontend/E2E jobs completed successfully.

## Previous increment: Week 11 signaling-dynamics virtual lab (2026-10-06)

Foundations of Cell and Molecular Biology advances from 0.17.0 to **0.18.0** and remains `partial`. The new original 2–3 hour lab uses 120 explicitly synthetic pERK/total-ERK observations across six treatment conditions, five times, and four preparation blocks. Learners summarize 24 condition/time cells, plot 15 selected time points, calculate a vehicle-adjusted inhibitor effect, and distinguish rescue, vehicle, and pathway-control evidence. Four retrieval cards support spaced review. It is interactive formative practice; answer specifications are public, scores are ungraded, and the activity is not one of the course's three grade-bearing labs.

Validation reports 25 packages, 128 lessons, 196 questions, 259 cards, and 25 cases; there are zero errors and 123 explicitly disclosed limitation/depth warnings. The lesson and data do not use copied OCW or third-party figures/data. The public course package remains partial: the eight graded homework sets, one remaining lab, summative midterm/final, cumulative project, measured workload, complete objective coverage, and independent scientific/accessibility review are unfinished. Public practice answer specifications are not protected exam keys.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 128 lessons, 196 questions, 259 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests/content/test_content_validation.py -q` | 67 passed, 1 skipped |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 69 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest tests -q` | 226 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm run lint` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run build` | PASS: TypeScript and Vite production build (206 modules) |
| `cd frontend; $env:E2E_BASE_URL='http://localhost:8080'; npm run test:e2e` | 20 passed, including the Week 11 summary upload, plot, calculation, controls, and practice-only gradebook status |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing data volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 200 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 417 source files |
| `git diff --check` | PASS |
| Hosted GitHub Actions run `37555835879` | PASS: content/backend and frontend/E2E jobs |

The existing grader interface limited attempts to 20 fields, below the maximum 40 coordinates from a 20-point plot. It now accepts up to 40 fields, with regression coverage for the boundary; graph component totals use stable summation so full credit returns exactly the configured point value. The new Playwright journey validates the data-analysis flow against the live local Compose app. No arbitrary learner code is executed by this lab.

Published at commit `93f97ea1a4b9cfb973df34aa78831e39bfb0551a`; [hosted GitHub Actions run `37555835879`](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37555835879) completed successfully, with both content/backend and frontend/E2E jobs passing.

## Previous increment: Week 3 open formative homework companion (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.16.0 to **0.17.0** and remains `partial`. Week 3 includes an original 2–3 hour homework companion on protein trafficking, localization and fractionation evidence. It pairs a 12-preparation synthetic M6P-receptor dataset with five deterministic public practice items: a CSV summary, fixed-axis plot, signed contrast with a bounded inference, structured control/rescue reasoning, and route/topology multiple select. Four CC BY 4.0 retrieval cards reinforce assay limits. The autograder checks summary cells and selected structured responses; it does not grade prose, test uncertainty inference, or establish mechanism. All answer specifications are visible in this public repository, the activity is explicitly ungraded, and it does not count as one of eight required graded homework sets.

Validation at that increment reported 25 packages, 127 lessons, 192 questions, 255 cards and 25 cases, with zero errors and 123 disclosed limitation/depth warnings. Its root suite passed 68 tests with 1 skipped; backend passed 224 with the upstream Starlette/httpx deprecation warning; frontend unit tests passed 31; Playwright passed 19; and legacy migration tests passed 7. The published increment at commit `708dd2ca88f7e187afa333a4758f56e4d449fc44` passed [hosted GitHub Actions run `37551413785`](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37551413785): both content/backend and frontend/E2E jobs completed successfully.

## Previous increment: first interactive data-analysis lab (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.15.0 to **0.16.0** and remains `partial`. Week 5 now includes the first authored lab in the proposed three-activity sequence: an original 2–3 hour virtual fluorescence-data-analysis lesson, eight-row synthetic CSV, instructor rubric, and four-question formative assessment worth 13 ungraded practice points. The learner uploads per-condition counts/means, plots batch-level percentages on fixed axes, interprets imaging controls, and reports a descriptive 9-percentage-point contrast. An API change allows `lab`-typed practice assessments to use the existing answer-free, enrollment-version-pinned endpoint, still restricted to explicitly public formative items. This package does not supply microscope images, simulate equipment, execute wet-lab procedures, grade prose, or count toward a course grade.

Validation passes for 25 packages, 126 lessons, 187 questions, 251 cards, and 25 cases, with 0 errors and 123 disclosed limitation/depth warnings. The complete root suite passed **67 tests with 1 skipped**; backend passed **224** with one upstream Starlette/httpx deprecation warning; frontend unit tests passed **31**; Playwright passed **18**; and legacy-state tests passed **7**. The new browser flow opens the lab in the course reader, opens its typed lab assessment from the practice gradebook, submits a CSV summary, plots both condition means, scores four evidence choices, and checks the 9-point value. Compose rebuilt while preserving the existing database volume; API, database, and web are healthy; Alembic is `0007 (head)`; and the integration validator supports 191 practice specifications. The answer-free public DTO boundary test passes; authoring keys remain explicitly public formative practice, and no secure exam key was added. Frontend lint/format and production build pass (206 modules), Ruff passes, `git diff --check` passes, and the security-boundary scan reports 0 findings across 413 source files.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 126 lessons, 187 questions, 251 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 67 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest -q` | 224 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run lint; npm run build` | PASS: formatting/lint and TypeScript/Vite production build (206 modules) |
| `cd frontend; $env:E2E_BASE_URL='http://localhost:8080'; npm run test:e2e` | 18 passed, including upload, fixed-axis plot, and structured lab practice |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing data volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 191 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 413 source files |

The eight homework sets, two remaining lab activities, summative midterm/final, cumulative project, measured workload, comprehensive objective coverage, and independent scientific/accessibility reviews remain incomplete. The course stays partial; the virtual lab does not satisfy the missing homework, exams, or capstone.

After the current browser suite, the local synthetic database remained at 82 users, 82 enrollments, 90 attempts, and 6 progress records. The lab increment was published at commit `f485075f025e7bd97d4562ed62d1cf82cb49c79e`; [hosted GitHub Actions run `37547670931`](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37547670931) completed successfully. Week 12 passed hosted run `37540473521`. Week 14 was published at commit `a372fb31eb1d706ddc94f5e09a9c81266ad82629`; hosted run `37544794562` completed successfully.

## Previous increment: week-14 potency and integrative study design (2026-10-06)

Version 0.15.0 added two original lessons on developmental potency/lineage evidence and integrative regenerative experiment design; six mapped objectives; seven deterministic public formative questions worth 13 practice points; four retrieval cards; misconception entries; layered feedback; and link-only curriculum/scientific/ethics sources. Explicitly synthetic examples support a 22.5% construct-fraction calculation and a 13-percentage-point descriptive contrast. The lesson bounds marker identity, function, uncertainty, and translational claims; it is not a complete capstone or graded coursework. It was published at commit `a372fb31eb1d706ddc94f5e09a9c81266ad82629`; hosted run `37544794562` completed successfully.

## Previous increment: week-13 cell-cycle and cell-fate evidence (2026-10-06)

Week 13 advanced the package to 0.14.0 with two original lessons, six objectives, seven formative items (13 points), four retrieval cards, five misconception entries, and six link-only sources. Synthetic cell-cycle and cell-state data supported reasoning about DNA-content, EdU, mitotic, recovery, senescence-associated, and apoptosis measurements. The increment passed its then-current tests and was published at commit `dd7a7ff06805dd0cd5e333df109783d5c7d6c95e`; its GitHub Actions status was not available from the combined-status check.

## Previous increment: week-12 cytoskeleton, matrix, and mechanobiology (2026-10-06)

Week 12 advanced the package to version 0.13.0 with two original lessons, six objectives, seven formative questions, four retrieval cards, a synthetic hydrogel-mechanics dataset, and link-only sources. Its 64-pass/1-skip root suite, 223 backend tests, 31 frontend tests, 15 browser tests, 407-file security scan, 173-specification integration check, and healthy Compose stack passed. Hosted Actions run `37540473521` completed successfully for commit `2f0fb1c66d4e40fe2c4efa462643b6c9750f00ea`.

## Previous increment: week-10 inheritance and variant evidence (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.10.0 to **0.11.0** and remains `partial`. Week 10 adds two original lessons on inheritance/penetrance and variant-to-phenotype evidence; six mapped learning objectives; seven deterministic public formative questions worth 13 practice points; four retrieval cards; four misconception entries; layered feedback for pedigree and variant interpretation; and link-only source records for MIT OCW and NCBI Bookshelf references. Synthetic isogenic-edit data are labeled as teaching data. The new numerical answer distinguishes transmission probability from phenotype probability (50% × 80% penetrance = 40%); the evidence lesson distinguishes a predicted molecular effect from demonstrated pathogenicity. The practice set is not graded coursework. No homework set, virtual lab, midterm, final, or project is claimed complete.

Content validation passes for 25 packages, 117 lessons, 155 questions, 235 cards, and 25 cases, with 0 errors and 123 disclosed depth/objective warnings. The focused content regression set passed 5 tests; the complete root suite passed **62 tests with 1 skipped**, backend passed **223**, frontend unit tests passed **31**, Playwright passed **13**, and legacy-state tests passed **7**. Docker Compose rebuilt successfully; the API, database, and web services are healthy; existing database data was preserved; Alembic remains at `0007 (head)`; and `/api/v1/health` reports `ok`. The learner integration validator supports 159 practice specifications. The new browser journey enrolled a guest, opened the week-10 set, submitted the penetrance calculation and structured isogenic-data response, and verified deterministic feedback. Frontend lint/format and production build pass (206 modules), Ruff passes, and the security-boundary scan reports 0 findings across 403 source files. The prior week-9 GitHub Actions run completed successfully; week-10 CI will run on publication. All authored answers remain explicitly public practice specifications; no exam key was added.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 117 lessons, 155 questions, 235 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 62 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest tests -q` | 223 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run lint; npm run build` | PASS: formatting/lint and TypeScript/Vite production build (206 modules) |
| `cd frontend; npm run test:e2e` | 13 passed, including week-10 numeric and structured practice submission |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing data volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 159 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 403 source files |

The eight homework packages, three full data/virtual-lab activities, summative midterm/final, integrative project, measured workload, comprehensive objective coverage, and independent scientific/accessibility reviews remain incomplete. Weeks 11–14 are still outlines and the course remains partial.

## Previous increment: week-9 RNA processing and protein regulation (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.9.1 to **0.10.0** and remains `partial`. Week 9 adds two original lessons on RNA processing/isoform evidence and translation/protein turnover; six mapped learning objectives, each tagged to at least one practice item; original, explicitly synthetic RNA and protein datasets; eight deterministic public formative questions (14 points, including seeded variants); four retrieval cards; five misconception entries; layered instructor-style feedback; and link-only provenance for MIT OCW and NCBI Bookshelf references. The practice set is not graded coursework. No homework set, virtual lab, midterm, final, or project is claimed complete.

Content validation passes for 25 packages, 115 lessons, 148 questions, 231 cards, and 25 cases, with 0 errors and 123 disclosed depth/objective warnings. The focused content regression set passed 6 tests; the complete root suite passed **61 tests with 1 skipped**, backend passed **223**, frontend unit tests passed **31**, Playwright passed **12**, and legacy-state tests passed **7**. The CI content check and development Compose build passed; the API integration validator supports 152 practice specifications. Compose API, database, and web are healthy; existing database data was preserved, Alembic remains at `0007 (head)`, and the health endpoint reports `ok`. The new browser journey enrolled a guest, opened the week-9 set, submitted a numeric isoform fraction and a structured synthesis/turnover response, and verified deterministic feedback. The existing public DTO boundary test still passes. Frontend lint/format and production build pass (206 modules); Ruff passes. The security-boundary scan reports 0 findings across 401 source files. All authored answers remain explicitly public practice specifications; no exam key was added.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 115 lessons, 148 questions, 231 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 61 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest tests -q` | 223 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm test -- --run` | 31 passed |
| `cd frontend; npm run lint; npm run build` | PASS: formatting/lint and TypeScript/Vite production build (206 modules) |
| `cd frontend; npm run test:e2e` | 12 passed, including week-9 numeric and structured practice submission |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: API, database, and web healthy; existing data volume preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 152 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 401 source files |

The eight homework packages, three full data/virtual-lab activities, summative midterm/final, integrative project, measured workload, comprehensive objective coverage, and independent scientific/accessibility reviews remain incomplete. Weeks 10–14 are still outlines and the course remains partial.

## Previous increment: week-8 cumulative practice set (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.9.0 to **0.9.1** and remains `partial`. Week 8 now contains a self-paced 12-question cumulative practice set spanning selected outcomes from weeks 1–7. It reuses the existing openly answer-bearing formative bank, totals 31 practice points, provides immediate per-question feedback, and is explicitly labeled **ungraded and not a midterm** in the syllabus, schedule, UI, README, and crosswalk. No summative exam, protected exam key, homework sequence, or new lesson was created.

The new learner endpoint requires enrollment and an assessment pinned to the selected package version. It accepts only `type: practice`, `mode: practice` records sourced from `question-banks/practice.json`; it verifies the pinned SHA-256, checks every referenced item is explicitly marked public formative practice, verifies the point total, and returns only whitelisted question DTOs. Restricted visibility, source mutation, incorrect type/source, and unknown assessment IDs fail closed. Seeded variants keep their signed course/version/question token. The course-level gradebook UI opens these practice sets and submits through the existing immutable formative-attempt workflow. The repository's authored answer specifications remain public by design and are not secure exam content.

Validation on 2026-10-06: root suite **59 passed, 1 skipped**; backend **223 passed**; frontend **31 passed**; Playwright **11 passed**; legacy-state **7 passed**. Content validation reports 25 packages, 113 lessons, 140 questions, 227 cards, and 25 cases with 0 errors and 123 explicitly disclosed depth/objective warnings. API/content integration passes for 25 packages and 142 supported practice specifications. The source/bundle security scan reports 0 findings across 399 files. Frontend lint/format and TypeScript/Vite production build pass (206 modules). Development Compose is healthy, with existing data volumes preserved; Alembic remains at `0007 (head)` and `/api/v1/health` is healthy.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 113 lessons, 140 questions, 227 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 59 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest tests -q` | 223 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| `cd frontend; npm test` | 31 passed |
| `cd frontend; npm run lint` and `npm run build` | PASS: formatting/lint and production bundle (206 modules) |
| `cd frontend; npm run test:e2e` | 11 passed, including version-pinned week-8 practice, per-question grading, and reload persistence |
| `npm run test:legacy` | 7 passed |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: database, API, and web healthy; existing volumes preserved |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 142 supported practice specifications |
| `docker compose exec -T api alembic current` | PASS: `0007 (head)` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 399 files |

The dedicated browser journey enrolled as a guest, opened the week-8 practice set, submitted a formative response, saw feedback, reloaded, reopened the set, and saw the saved feedback. An axe WCAG 2.1 A/AA scan on the loaded practice view reported zero violations. No summative-exam flow exists to test.

## Previous increment: week-7 chromatin and transcription (2026-10-06)

Foundations of Cell and Molecular Biology advanced from 0.8.0 to **0.9.0** and remains `partial`. Week 7 adds two original developed lessons, seven deterministic formative questions, four retrieval cards, seven misconception entries, two feedback templates, mapped lesson objectives, and per-module source provenance. The short gene-expression prototype remains supplementary. Accessibility/RNA, ChIP-qPCR, and reporter examples use explicitly synthetic data. The lessons separate input, IgG/mock, positive/negative-locus, and no-template controls and distinguish chromatin accessibility, occupancy, reporter activity, direct binding, and endogenous causal evidence.

The proposed teaching block now runs through week 7; week 8 is reserved for a proposed midterm and retrieval consolidation. No week-8 exam questions, answer key, rubric, assessment record, release policy, dates, or deadlines exist. Weeks 9–14 remain outlines. The repository inventory is 25 packages, 113 lessons, 140 formative questions, 227 retrieval cards, and 25 self-assessed cases. All packages remain partial and no external reviewer is claimed.

Validation on 2026-10-06: **327 tests passed and 1 skipped** across root (59 passed, 1 skipped), backend (221), frontend unit tests (30), Playwright (10), and legacy storage (7). Content validation reports 25 packages, 113 lessons, 140 questions, 227 cards, and 25 cases: 0 errors and 123 disclosed depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content integration check passes for 25 packages and 142 supported practice specifications. The source/bundle security-boundary scan reports 0 findings across 397 files. Frontend lint/format and the TypeScript/Vite production build passed (205 modules). Rebuilt development Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database/credential volumes were preserved. Playwright now submits and grades week-7 chromatin, ChIP percent-input/control, and reporter items; the answer-specification boundary test passed.

| Current command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 113 lessons, 140 questions, 227 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `backend/.venv/Scripts/python.exe -m pytest tests -q` | 59 passed, 1 skipped |
| `cd backend; .venv/Scripts/python.exe -m pytest -q` | 221 passed; one upstream Starlette/httpx deprecation warning |
| `cd backend; .venv/Scripts/ruff.exe check .` | PASS |
| Frontend `npm run lint`, `npm test -- --run`, and `npm run build` | PASS: 30 unit tests, TypeScript build, 205 production modules |
| `npm run test:e2e` against rebuilt Compose | 10 passed, including week-7 lesson submissions and answer-specification DTO exclusion |
| `npm run test:legacy` | 7 passed |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 142 supported practice specifications |
| `docker compose exec -T api alembic current` and `/api/v1/health` | PASS: `0007 (head)`; health `ok`; programming runner and LLM feedback disabled |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: database, API, and web healthy; existing volumes preserved |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 findings across 397 files |
| `git diff --check` | PASS |

New source records link to MIT OCW 7.28x as a curriculum comparator and to NCBI Bookshelf, Haring et al.'s CC BY 2.0 ChIP-qPCR methods article, and ENCODE standards as references. The project uses links/citations only and redistributes none of their text, figures, tables, or data. Live-link probing was not repeated; the prior report records two JHU pages that return HTTP 403 to the automated client.

## Previous increment: week-6 DNA replication and repair

Foundations of Cell and Molecular Biology advanced from version 0.7.0 to **0.8.0** while remaining `partial`. Week 6 adds two original lessons, seven deterministic formative items, four retrieval cards, misconception entries, two feedback templates, objective mappings, and per-module provenance. The lessons address strand polarity and replication, model-discriminating density predictions, lesion-specific repair candidates, and interpretation limits for perturbation and rescue evidence. The UV lesion-signal series is explicitly synthetic; it is not presented as historical measurements, mutation frequency, or proof of direct catalysis.

MIT OCW 7.28x Molecular Biology is a link-only curriculum comparator. Meselson and Stahl (1958) and NCBI Bookshelf replication/repair chapters are link-only scientific references. The instructional prose and questions are original; no source text, figures, table, or dataset was copied. All packages remain partial and no reviewer is fabricated.

The inventory is 25 packages, 111 lessons, 133 formative questions, 223 retrieval cards, and 25 self-assessed cases. Weeks 1–6 now have two developed lessons each; week 4 retains its short prototype capsule and week 7 has one compact gene-expression reading. Weeks 8–14 remain outlines. Eight homework sets, three full data/lab activities, midterm, cumulative final, integrative project, measured workload, and independent academic/accessibility review remain unfinished.

Validation on 2026-10-06: **326 tests passed and 1 skipped** across root (58 passed, 1 skipped), backend (221), frontend unit tests (30), Playwright (10), and legacy storage (7). Content-authoring tests passed (56, 1 skipped). Frontend lint/format and TypeScript/Vite build passed (205 modules). Content validation reports 25 packages, 111 lessons, 133 questions, 223 cards, and 25 cases: 0 errors and 123 disclosed depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content integration check passes for 25 packages and 135 supported practice specifications. The security-boundary scan reports 0 findings across 396 files. Rebuilt development Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

| Current command/check | Result |
| --- | --- |
| `uv run --with jsonschema python tools/validate_content.py` | PASS: 25 packages, 111 lessons, 133 questions, 223 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `uv run --project backend --with pytest --with ruff --with jsonschema python -m pytest tests -q` | 58 passed, 1 skipped |
| `docker compose run --rm --no-deps api pytest -q -p no:cacheprovider` | 221 passed; upstream Starlette/httpx and Python `datetime.utcnow()` deprecation warnings |
| Frontend `npm run lint`, `npm run test`, and `npm run build` | PASS: lint/format, 30 unit tests, TypeScript build and 205 production modules |
| Playwright `npm run test:e2e` against rebuilt Compose | 10 passed, including week-6 replication/repair submissions and deterministic feedback; guest enrollment, saved progress, and answer-key DTO boundary |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 135 supported practice specifications |
| Compose health and migration | PASS: database, API, and web healthy; Alembic `0007 (head)`; API health `ok` |
| `python tools/check_security.py --bundle frontend/dist` | PASS; 0 security-boundary findings across 396 files |

Ruff (`backend/courselab`, `backend/tests`, and `tests`) and `git diff --check` passed. Link reachability was not re-run: the previous report records two JHU public pages returning HTTP 403 to the automated client. This does not affect offline schema/content validation.

## Previous increment: week-5 cell measurement and fractionation

Foundations of Cell and Molecular Biology advanced from version 0.6.0 to **0.7.0** while remaining `partial`. Week 5 adds two original lessons: conventional-light microscopy resolution, sampling, contrast, labeling controls, and colocalization limits; then differential fractionation, marker recovery, contamination, and bounded localization claims. Six deterministic practice items cover a resolution estimate, confocal contrast, colocalization inference, marker recovery, structured fraction analysis, and multi-marker design. Four spaced-retrieval cards, five misconception entries, two feedback templates, objective mappings, and source/license records were added. The bead-pair and marker-panel data are explicitly synthetic teaching data.

MIT OCW 7.016 Lecture 29 is linked as a curriculum comparator. Waters (2009), Claude (1946), and the NCBI Bookshelf methods chapter are link-only scientific or methods references. No lecture, article, chapter, figure, or data was copied or adapted. The course has no external reviewer and its review status remains unreviewed.

Weeks 1–5 now each have two developed lessons; week 4 retains its compact prototype capsule. Week 7 remains one compact gene-expression reading, and weeks 6 and 8–14 remain outlines without authored instructional sequences. The eight proposed homework sets, three full data/lab assignments, midterm, cumulative final, and integrative project are not present. All 126 practice questions are formative; the package has no course grade, semester-equivalence, credit, or prerequisite-equivalency claim. All 25 course packages remain partial; none meets the complete-course standard.

Validation on 2026-10-06: **325 tests passed and 1 skipped** across root (57 passed, 1 skipped), backend (221), frontend unit tests (30), Playwright (10), and legacy storage (7). Frontend lint/format and TypeScript/Vite build passed (205 modules). Content validation reports 25 packages, 109 lessons, 126 questions, 219 cards, and 25 cases: 0 errors and 123 disclosed depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content check passes for 25 packages and 128 supported practice specifications. Ruff and `git diff --check` pass. The source/bundle security-boundary scan reports 0 findings across 393 files. Rebuilt development Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

| Week-5 command/check | Result |
| --- | --- |
| `uv run --with jsonschema --with pytest python tools/validate_content.py` | PASS: 25 packages, 109 lessons, 126 questions, 219 cards, 25 cases; 0 errors; 123 disclosed warnings |
| `uv run --with jsonschema --with pytest python -m pytest tests -q` | 57 passed, 1 skipped |
| Backend pytest suite | 221 passed; one upstream Starlette/httpx deprecation warning |
| Frontend lint/format, Vitest, and Vite build | PASS: 30 unit tests; 205 production modules |
| Playwright against the rebuilt Compose stack | 10 passed, including week-5 numeric units, fraction rubric, saved progress, and answer-key DTO boundary |
| `docker compose exec -T api python -m courselab.check_content /content` | PASS: 25 packages / 128 supported practice specifications |
| Compose health and migration | PASS: database, API, and web healthy; Alembic `0007 (head)`; API health `ok` |
| Ruff, `git diff --check`, and `python tools/check_security.py --bundle frontend/dist` | PASS; 0 security-boundary findings across 393 files |

## Previous increment: week-4 enzyme mechanisms and kinetic inference

Foundations of Cell and Molecular Biology advanced from version 0.5.0 to **0.6.0** while remaining `partial`. Week 4 now has two substantial original lessons alongside the retained short prototype capsule: catalytic mechanisms/free-energy coupling, then initial-rate fitting and reversible-inhibitor patterns. Six new deterministic formative items cover equilibrium, coupled ΔG, Vmax at Km, model-based rate prediction, inhibitor-pattern/assay controls, and Km versus binding affinity. Four retrieval cards, misconception entries, layered-feedback templates, source records and independent numerical recalculation tests were added. The inhibitor table is explicitly synthetic and is not presented as published data.

The scope comparator is MIT OCW 5.07SC Biological Chemistry I, whose undergraduate Module I includes sessions on enzyme catalysis and enzyme kinetics/inhibition; it is linked only. Briggs and Haldane (1925) and Johnson and Goody (2011) are linked as research references. No source text, figure, problem, or dataset was copied or adapted. The course remains unreviewed.

Weeks 1–4 now each have two developed lessons; week 4 retains one additional compact prototype reading. Week 7 still has one compact gene-expression capsule; weeks 5–6 and 8–14 remain without authored lesson sequences. The eight proposed homework sets, three data/lab activities, midterm, cumulative final and integrative project are still absent. All 120 questions remain formative; no course grade or semester-equivalence claim is enabled.

Validation on 2026-10-06: root **54 passed, 1 skipped**; backend **221 passed** (one upstream Starlette/httpx deprecation warning); frontend **30 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **10 passed**, including enrollment, week-4 lesson reading, numeric unit checks, inhibitor rubric scoring and saved feedback; legacy storage tests **7 passed**. Content validation reports 25 packages, 107 lessons, 120 questions, 215 cards and 25 cases: 0 errors and 123 explicit depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content check passes for 25 packages and 122 supported practice specifications. Ruff and `git diff --check` pass. Source and bundle security-boundary scans found 0 issues across 391 files. Rebuilt Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 107 lessons, 120 questions, 215 cards, 25 cases; 0 errors; 123 disclosed depth/objective warnings |
| `python -m pytest tests/content -q` | 54 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 221 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests`; `git diff --check` | PASS |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 30 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 10 passed, including week-4 numerical and structured-inference submissions |
| `node tests/legacy/state.test.mjs` | 7 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 122 supported practice specifications |
| `python tools/check_security.py` and `python tools/check_security.py --bundle frontend/dist` | PASS: 391 files, 0 findings |
| `docker compose up --build -d --wait --wait-timeout 180`; Alembic and health queries | PASS: database, API, and web healthy; `0007 (head)`; health `ok` |

These checks verify the current software paths and authored package structure; they do not establish full-course quality, mastery, course-level human grading, or institutional equivalency.

## Previous increment: cell-biology weeks 1–3 and trafficking lessons

Foundations of Cell and Molecular Biology advanced from version 0.4.0 to **0.5.0** while remaining `partial`. Week 3 now has two substantial original lessons: organelle compartments and protein targeting, followed by protein sorting and vesicle traffic. Both lessons include worked reasoning, explicitly synthetic experimental datasets, controls, limits on causal inference, formative questions and retrieval cards. The source map links one MIT OCW scope comparator and five primary articles as link-only references; no source text, figure or data was adapted. The source schema and validator now distinguish link-only research references and prohibit treating them as adaptation permissions.

The syllabus and assessment crosswalk now identify weeks 1–3 as the only weeks with two developed lessons each. Week 4 and week 7 remain short capsules; weeks 5–6 and 8–14 remain unauthored. The course still lacks the planned eight homework sets, three laboratory/data activities, midterm, cumulative final and integrative project. All 114 practice questions remain formative, and no course grade is awarded. The course remains unreviewed and has no external reviewer. This increment does not establish semester equivalence.

Validation on 2026-10-06: root **53 passed, 1 skipped**; backend **221 passed** (one upstream Starlette/httpx deprecation warning); frontend **30 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **10 passed**; legacy storage tests **7 passed**. Content validation reports 25 packages, 105 lessons, 114 questions, 211 cards and 25 cases: 0 errors and 123 explicit depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content check passes for 25 packages and 116 supported practice specifications. Ruff passes. Source and bundle security-boundary scans found 0 issues across 389 files. Rebuilt Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 105 lessons, 114 questions, 211 cards, 25 cases; 0 errors; 123 disclosed depth/objective warnings |
| `python -m pytest tests/content -q` | 53 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 221 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests`; `git diff --check` | PASS |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 30 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 10 passed, including week 3 lessons/practice and answer-key exposure checks |
| `node tests/legacy/state.test.mjs` | 7 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 116 supported practice specifications |
| `python tools/check_security.py` and `python tools/check_security.py --bundle frontend/dist` | PASS: 389 files, 0 findings |
| `docker compose up --build -d --wait --wait-timeout 180`; Alembic and health queries | PASS: database, API, and web healthy; `0007 (head)`; health `ok` |

These checks confirm current application paths and authored package structure. They do not establish full-course quality, a security audit, course-level human grading, workload, mastery, or institutional equivalency.

## Previous increment: cell-biology scope and the first two developed weeks

Foundations of Cell and Molecular Biology advanced from version 0.3.2 to **0.4.0** without changing its `partial` maturity. The manifest and syllabus now record a proposed 14-week undergraduate scope and an outcome-to-assessment crosswalk. Weeks 1 and 2 contain four original, substantial readings (about 700–790 words each), with worked biochemical and membrane-transport examples. Weeks 4 and 7 retain brief enzyme and gene-expression capsules; weeks 3, 5–6, and 8–14 have no authored lessons. The 14-week plan is not 14 weeks of instruction and does not establish semester equivalence.

The initial weeks add explicit lesson objectives linked to the four intended course outcomes, four original deterministic practice items, four retrieval cards, a focused misconception catalog, and instructor-style feedback templates. A new Playwright flow opens the pH, protein-variant, and membrane-transport lessons, submits the associated practice responses, and checks the returned scores. All questions remain formative; solution specifications are public practice material and no live package awards a course grade. The content remains unreviewed. The proposed eight homework sets, three lab/data activities, midterm, cumulative final, and integrative project are not authored or enabled. Workload has not been measured.

New teaching text is original and under the repository's CC BY 4.0 content license. MIT OCW 7.01SC Fundamentals of Biology and 7.28x Molecular Biology are linked as curriculum comparators only; no text, figure, problem, or exam was copied or adapted. The sources are the [MIT 7.01SC syllabus](https://ocw.mit.edu/courses/7-01sc-fundamentals-of-biology-fall-2011/pages/syllabus/) and [MIT OCW terms](https://ocw.mit.edu/pages/privacy-and-terms-of-use/); the terms' license does not clear third-party assets or imply MIT endorsement.

Validation on 2026-10-06: root **54 passed, 1 skipped**; backend **221 passed** (one upstream Starlette/httpx deprecation warning); frontend **30 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **10 passed**; legacy storage tests **7 passed**. Content validation reports 25 packages, 103 lessons, 110 questions, 207 cards, and 25 cases: 0 errors and 123 explicit depth/objective warnings (98 legacy-depth, 25 objective-coverage). The API/content check passes for 25 packages and 112 supported practice specifications. Ruff passes. Source and bundle security-boundary scans found 0 issues across 387 files. Rebuilt Compose services are healthy, Alembic is `0007 (head)`, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Existing database volumes were preserved.

Both GitHub Actions jobs passed after the browser assertion was narrowed to the reader's level-one heading in [run 37516239260](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37516239260).

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 103 lessons, 110 questions, 207 cards, 25 cases; 0 errors; 123 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 54 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 221 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests` | PASS |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 30 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 10 passed, including new week 1–2 instruction and autograding flow |
| `node tests/legacy/state.test.mjs` | 7 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 112 practice specifications |
| `python tools/check_security.py` and `python tools/check_security.py --bundle frontend/dist` | PASS: 387 files, 0 findings |
| `docker compose up --build -d --wait --wait-timeout 180`; Alembic and health queries | PASS: database, API, and web healthy; `0007 (head)`; health `ok` |

These checks confirm the current software paths and authored package structure. They do not establish full-course quality, a security audit, course-level human grading, workload, mastery, or institutional equivalency.

## Previous increment: graded-assignment appeals and manual review

Alembic revision 0007 adds a one-appeal-per-submission learner workflow and a separate append-only instructor decision record. Learners can request a review of a graded result; authorized reviewers can uphold, decline, or adjust within the assignment's score bounds. The original deterministic score and feedback remain immutable. Adjusted results are surfaced as effective scores and feed the weighted gradebook. Instructor review reconstructs only answer-free question views and verifies the pinned course source and question digest; stale or unavailable specifications can only be declined. Self-review is blocked. Learner export, account deletion, reviewer anonymization, and gradebook override counts include these records.

The graded-assignment workflow still runs only against synthetic test fixtures because **none of the 25 shipped course packages contains graded assignments**. No live catalog course awards a weighted course grade. Programming assignments remain disabled, and no historical content archive is available for regrading old versions. Course maturity is unchanged: 25 partial, 0 beta, 0 complete, 0 externally reviewed.

Validation on 2026-10-06: backend **221 passed** (one upstream Starlette/httpx deprecation warning); root content/security suite **53 passed, 1 skipped**; frontend **30 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **9 passed** against the rebuilt Compose stack; legacy storage migration **7 passed**. Ruff passed. Content validation found 25 packages, 101 lessons, 106 questions, 203 cards and 25 cases: zero errors and 125 explicit depth/objective warnings. The API/content check passed for 25 packages and 108 practice specifications. The source/bundle security scan found zero issues in 382 files. Compose services are healthy, Alembic is at `0007 (head)`, both review tables exist, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. Both GitHub Actions jobs passed in [run 37511037086](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37511037086).

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages; 0 errors; 125 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 53 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 221 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests` | PASS |
| `node tests/legacy/state.test.mjs` | 7 passed |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 30 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 9 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 108 practice specifications |
| `python tools/check_security.py --bundle frontend/dist` | PASS: 382 files, 0 findings |
| `docker compose up --build -d`; `alembic current`, review-table query and `/api/v1/health` | PASS: services healthy; Alembic `0007`; both review tables exist; health `ok` |

Playwright covers guest enrollment, lesson viewing, formative submission/feedback, progress and persistence, plus existing appeal flows and protection of public question views. Graded-assignment appeal, score bounds, stale-source decline, immutable automatic scores, weighted-grade updates and anonymization are covered by backend API tests and frontend component tests on synthetic fixtures. Existing user and database volumes were preserved during rebuild. These local synthetic checks do not constitute a security audit or full course-quality review.

## Previous increment: deterministic graded-assignment submission and weighted gradebook

Alembic revision 0006 adds append-only graded submissions tied to learner enrollment, course version, assessment and attempt number. An enrolled learner receives a whitelisted question view with no answer keys, then submits a complete response for server-side deterministic grading. The API verifies the enrollment-pinned source file hash and question mapping, enforces release time, a strict deadline and attempt limits, stores scores and criterion feedback, serves learner-owned attempt history, and includes selected results in the weighted gradebook. The React workspace provides the assignment response form, immediate feedback and refreshed gradebook. Export and account deletion include the new records.

The executable submission path uses a synthetic test fixture because **none of the 25 shipped course packages currently contains graded assignments**. Consequently no live catalog course awards a weighted course grade. At the time of this increment, graded appeals/manual overrides, archived historical content and code execution were not implemented. This increment did not change course maturity: 25 partial, 0 beta, 0 complete, 0 externally reviewed.

Validation on 2026-10-06: backend **218 passed** (one upstream Starlette/httpx deprecation warning); root content/security suite **53 passed, 1 skipped**; frontend **27 unit tests passed**, lint/format and TypeScript/Vite build passed (205 modules); Playwright **9 passed** against the rebuilt Compose stack. Ruff passed after correcting import ordering in two existing utility/test files. Content validation found 25 packages, 101 lessons, 106 questions, 203 cards and 25 cases: zero errors and 125 explicit depth/objective warnings. The API/content check passed for 25 packages and 108 practice specifications. The source/bundle security scan found zero issues in 381 files. Compose services are healthy, Alembic is at `0006 (head)`, the `graded_submissions` table exists, and `/api/v1/health` is `ok`; programming and LLM providers remain disabled. GitHub Actions passed both jobs for the graded-workflow commit in [run 37505270475](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37505270475) and for its LF-normalized tree in [run 37505850315](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37505850315).

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages; 0 errors; 125 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 53 passed, 1 skipped |
| `cd backend; python -m pytest tests -q` | 218 passed; 1 upstream deprecation warning |
| `ruff check backend tools tests` | PASS |
| `node tests/legacy/state.test.mjs` | 7 passed |
| Frontend `npm run lint`, `npm test -- --run`, `npm run build` | PASS; 27 unit tests; 205 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 9 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 108 practice specifications |
| `python tools/check_security.py --bundle frontend/dist` | PASS: 381 files, 0 findings |
| `docker compose up --build -d`; PostgreSQL migration query and `/api/v1/health` | PASS: services healthy; Alembic `0006`; graded-submission table exists; health `ok` |
| GitHub Actions | PASS: both jobs passed for the graded-submission implementation and LF-normalized tree |

Playwright covers the existing guest enrollment, lesson, formative submission/feedback, progress and persistence flows; graded-assignment request/result/history behavior is covered by backend API tests and frontend component tests on a synthetic fixture. Existing user and database volumes were preserved during rebuild. These local synthetic checks do not constitute a security audit or full course-quality review.

## Previous increment: enrollment-versioned assessment plans

The course schema now supports grade categories and weights, points or equal-assignment aggregation, assignment titles/weeks, release and deadline timestamps, attempt limits, and highest/latest attempt selection. The validator rejects weight/category mismatches, duplicate IDs, graded work in formative-only packages, invalid date order, and invalid attempt rules. Alembic revision 0005 adds enrollment/version-scoped `assessment_plans` and `assessment_instances`; enrollment captures policy and assignment metadata plus a source-file SHA-256, and an explicit content-version update appends a new snapshot while preserving the old metadata. The authenticated learner plan endpoint omits internal paths, question IDs, digests, and answer keys. The course workspace displays the plan alongside the existing practice gradebook.

The weighted-grade core uses `Decimal`, is separately unit-tested for category aggregation, attempt selection/limits, missing and unreleased work, exact-deadline boundaries, late/unknown attempts, invalid scores, and repeatability. This is a calculation core only: there is not yet a graded-assignment submission/result store or a route connecting saved scores to the calculator. The visible practice gradebook remains formative. Current content stays at 25 partial courses, with no course grade configured.

Validation on 2026-10-06: **308 tests passed** across the root content/security suite (54), backend suite (213), frontend unit suite (25), Playwright (9), and legacy storage tests (7). Ruff, frontend lint/Prettier, TypeScript/Vite build (204 modules), the API/content integration checker (25 packages and 108 supported practice specifications), and source/bundle security scan (378 source files, zero findings) passed. Content validation reported 25 packages, 101 lessons, 106 questions, 203 cards and 25 cases; zero errors and 125 explicit depth/objective warnings. The rebuilt Compose stack is healthy, PostgreSQL reports Alembic `0005`, and Playwright against the real stack verifies enrollment, lesson reading, practice submission and feedback, progress/gradebook persistence, and the new no-course-grade statement. Existing persistent volumes were preserved.

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages; 0 errors; 125 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 54 passed |
| `cd backend; python -m pytest -q` | 213 passed |
| `ruff check backend tools tests` | PASS |
| Frontend `npm run lint`, `npm test`, `npm run build` | PASS; 25 unit tests; 204 modules built |
| `npm run test:e2e` against `http://localhost:8080` | 9 passed, including assessment-plan display and formative-only status |
| `node tests/legacy/state.test.mjs` | 7 passed |
| `python tools/check_security.py --bundle frontend/dist` | PASS: 378 source files, zero findings |
| `python -m courselab.check_content ../content` | PASS: 25 course packages and 108 supported practice specifications |
| `docker compose up --build -d`; PostgreSQL migration query and `/api/v1/health` | PASS: stack healthy; Alembic `0005`; assessment snapshot tables exist |

The test output includes existing Starlette/httpx and `datetime.utcnow()` deprecation warnings. The course-grade calculation is not active for any live package; assignment submission enforcement, result persistence, protected graded question delivery, and gradebook integration remain roadmap work. The hashed snapshots are metadata/version evidence, not full immutable content archives and do not support historical regrading.

## Previous increment: operator-provisioned review and variant-pinned restoration

Self-declared registration emails no longer grant reviewer access. Alembic revision 0004 adds an `is_instructor` role that defaults to false for all existing users. Only the operator CLI can grant or revoke it; operators must verify identity and authority out of band. Instructor decisions now reconstruct the saved variant and compare the question digest. The authorized API returns only the safe public question DTO, including actual options and structured-response fields; it never returns the grader key. Adjusting/upholding fails closed if the version is stale, the attempt was unpinned, or the installed specification changed. Without immutable package archives, older attempts can only be declined.

Lesson reloads now restore the learner's latest attempted variant for the current content version. A signed v2 token pins that variant while the verifier continues accepting v1 tokens; the attempt and appeal feedback therefore stay paired with the exact prompt that was answered. A same-user reload regression test covers this behavior.

Validation on 2026-10-06: **291 tests passed**—199 backend, 52 content/security, 24 frontend unit, 9 Playwright and 7 legacy migration tests. Frontend lint/Prettier, TypeScript typecheck, production build (203 modules), Ruff, content validation (25 packages, 101 lessons, 106 questions, 203 cards, 25 cases; zero errors and 125 explicit depth/coverage warnings), and source/bundle security scan (372 files, zero findings) passed. Production Compose configuration passed with validation-only placeholders. The full Compose application built and reported healthy; Alembic reached `0004 (head)`. The browser suite covered course reading, enrollment, submission, feedback and persistence; an unprivileged registrant was denied the instructor API. New browser-runner cleanup removes synthetic accounts created in each E2E run. The migration did not remove or rewrite preexisting learner records.

The first hosted workflow attempt exposed a reload-only mismatch: a newly randomized prompt replaced the question variant tied to a saved attempt, hiding its feedback in the lesson view. After variant-pinned restoration, local Playwright passed all 9 tests and [GitHub Actions run 37415386582](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37415386582) passed both jobs, including Compose startup and all Playwright checks.

Before and after E2E validation, the existing database contained 82 users, 82 enrollments, 90 attempts and 6 progress records. Five synthetic guest records from the first E2E run were identified by their creation window and removed; the final counts returned to the same baseline. The test-origin bridge `http://host.docker.internal:8080` was temporarily enabled to let the browser container reach the loopback-published app, then the API was recreated with localhost origins only. Existing database and credential volumes remained in place. These are local synthetic-data checks, not a penetration test, production deployment or security certification.

## Previous increment: product rename and progress review

The product and public GitHub repository are now **uniStemCourseSimulators**. UI, metadata, API title, normalized package names, schema namespaces, exported filename and documentation use the new identity. Existing browser notebooks are sanitized into a v3 key with retained old keys/backups; migration write failures keep readable prior data available in memory. The existing local Compose project identity is pinned in an untracked `.env` to preserve both database and credential volumes. Technical Python/database/session/configuration identifiers remain stable. No course maturity changed.

[PROGRESS_REVIEW.md](PROGRESS_REVIEW.md) assesses the six milestones against actual code/content. [ROADMAP.md](ROADMAP.md) now prioritizes reviewer identity, saved-variant/digest reconstruction, semester assessment workflows and substantive biology instruction. The review found unresolved instructor impersonation and appeal fidelity defects; passing existing tests does not resolve them. Public instructor access must remain disabled. The biology syllabus was corrected to its actual version 0.3.2 and seven-question inventory.

Local checks ran through the workspace `dev` container (Python 3.11 and Node 24); Compose uses Python 3.12. Commands inside the development container used `/tmp/uni-review/bin/python` and `/tmp/uni-review/bin/ruff` from a temporary environment installed from both requirement files. All current tests passed: **285 total**—195 backend, 52 root content/security checks, 22 Vitest, 9 Playwright and 7 legacy migration tests. The root suite had no skipped tests because SymPy was present. Its warnings include the upstream Starlette/httpx test-client deprecation. A final targeted catalog check verifies the renamed title and accessible brand.

| Command/check | Result |
| --- | --- |
| `python tools/validate_content.py` | PASS: 25 packages, 101 lessons, 106 questions, 203 cards, 25 cases; zero errors, 125 disclosed depth/objective warnings |
| `python -m pytest tests -q` | 52 passed |
| `cd backend; python -m pytest -q` | 195 passed |
| `python -m courselab.check_content ../content` | PASS: 25 packages / 108 supported specifications |
| `npm run test:legacy` | 7 passed, including both previous keys, precedence, retained backups, malformed prior values and denied writes |
| `ruff check backend tools tests` | PASS |
| Frontend `npm run lint`, `npm test`, `npm run build` | PASS; 22 unit tests, TypeScript/Vite build of 203 modules |
| `python tools/check_security.py --bundle frontend/dist` | PASS: source/bundle scan, zero findings; public DTO exclusions also exercised by E2E |
| `docker compose up --build -d --wait --wait-timeout 180` | PASS: PostgreSQL/API/web healthy; credential/migration services exit 0; Alembic `0003 (head)` |
| `E2E_BASE_URL=http://host.docker.internal:8080 npm run test:e2e` | 9 passed against the complete Compose application; enrollment, reading, submissions, partial credit, feedback, notes/progress, upgrade/export/delete, appeal and reload persistence |
| Development and production Compose configuration | PASS; fresh development default resolves to `uni-stem-course-simulators`; production checked with validation-only domain/secret placeholders |

The initial container frontend test launch encountered a Windows-installed Rollup optional dependency. `npm ci` inside the Linux development container repaired the environment without changing dependency versions; tests/build then passed. Playwright Chromium and its Linux dependencies were installed inside that development container. This earlier validation temporarily used an email allowlist for a synthetic reviewer; that authorization flaw was discovered in the later progress review and is closed by the current increment above. Only loopback web access is published.

Data continuity was checked immediately before and after container recreation, before E2E added synthetic records: 77 users, 77 enrollments, 84 attempts and 6 progress records were unchanged. No volume was removed or copied, no live database password rotated, and no learner record was rewritten for branding. The untracked environment pin contains only the existing project identity. Source scanning is a bounded automated check, not a penetration test or proof against every possible secret. Live-source probes and dependency audits were not repeated for this identity-only increment; the previously recorded JHU HTTP 403 probe limitations remain unresolved. No public HTTPS deployment or external academic review is asserted.

## Previous increment: practice-v10 fixed-axis graph-coordinate practice

The deterministic graph grader awards separate partial credit for learner-entered x and y coordinates. The statistics practice lesson supplies bounded axes, labeled points, and replicate data; learners calculate group means, enter each coordinate, and receive a live SVG preview plus a screen-reader-readable source table. Expected coordinates, tolerances and criterion evidence remain server-side. The authoring validator independently recalculates each plotted mean and checks source-coordinate mapping. This narrow profile does not grade graph choice, axis selection, uncertainty bars, interpolation, model fit, or interpretation.

The statistics package advances to version 0.1.2 and stays **partial**. Its graph task is a bounded formative exercise; it does not turn the package into a full statistics course or establish course mastery.

Final local validation for this increment: **281 tests passed, 1 skipped** across backend (195), course authoring (49 plus 1 skipped), frontend unit (22), Playwright (9), security-boundary unit tests (2), and legacy state (4). The content validator reports 25 course packages, 101 lessons, 106 questions, 203 retrieval cards and 25 cases, with zero errors and 125 explicit depth/coverage warnings. The API integration checker passed for 25 packages and 108 supported practice specifications. Ruff, frontend lint/Prettier, TypeScript/Vite production build (203 modules), and the source/bundle boundary scan (368 source files, 0 findings) passed. The npm and Python dependency audits reported no known vulnerabilities. Production Compose configuration passed with validation-only placeholder values.

`docker compose up --build -d --wait --wait-timeout 180` passed; database, API and web were healthy and the migration service exited successfully. Alembic reports `0003 (head)`, `/api/v1/health` returns `ok`, and `/api/v1/curriculum` returns 62 nodes across 8 pathways. Browser checks exercised enrollment, lesson and retrieval tools, graded submissions, feedback, saved progress, appeals, the graph plot's 2.5/3 pointwise partial credit and reload persistence, CSV credit, and accessibility. All 9 Playwright tests passed. The graph source table, SVG preview and feedback view had no detected WCAG 2/2.1 A/AA violations; public DTO tests confirm answer specifications remain excluded. The appeal E2E temporarily allowlisted its synthetic reviewer account, then restored the API to an empty allowlist. All checks use synthetic learner data and do not establish public production deployment, penetration testing or security certification.

## Previous published increment: practice-v9 bounded CSV analysis uploads

The server now grades a bounded CSV upload against an authored numeric-table specification. It accepts UTF-8 CSV with an optional byte-order mark, caps the base64 payload at 32 KiB, limits rows, columns and cell sizes, checks exact ordered headers and authored row keys, rejects duplicate or malformed data, and reuses the deterministic numeric/unit grader for each cell. Partial credit is reported per rubric check. The grader parses data only; it does not execute uploaded files or submitted code. The public lesson DTO exposes only the CSV media type and size limit.

Foundations of Cell and Molecular Biology version 0.3.2 adds an original replicate-count and mean-signal upload exercise. The content validator checks its schema, rubric mapping and point total, then independently recalculates the authored counts and means. The course remains **partial**: the upload exercise does not supply a semester of instruction, a full laboratory sequence, or general-purpose data-analysis grading.

Final local validation for this increment: **266 tests passed, 1 skipped** across backend (188), course authoring (44 plus 1 skipped), frontend unit (21), Playwright (9), and legacy state (4). The content validator reports 25 course packages, 101 lessons, 105 questions, 202 retrieval cards and 25 cases, with zero errors and 125 explicit depth/coverage warnings. The API integration checker passed for 25 packages and 107 supported practice specifications. Ruff, frontend lint/Prettier, TypeScript/Vite production build (203 modules), and the source/bundle boundary scan (367 source files, 0 findings) passed. Production Compose configuration also passed with validation-only placeholder values.

`docker compose up --build -d --wait --wait-timeout 180` passed; database, API and web were healthy and the migration service exited successfully. Alembic reports `0003 (head)`, `/api/v1/health` returns `ok`, and `/api/v1/curriculum` returns 62 nodes across 8 pathways. Browser checks exercised enrollment, lesson practice, feedback, notes, progress persistence, account flows, appeal review, CSV partial credit and persistence, accessibility scans, and absence of answer specifications from public DTOs. The appeal E2E requires a configured instructor allowlist, so the synthetic reviewer was enabled for that run and the development API was restored to the default empty allowlist afterward. These checks use synthetic data and do not establish a public production deployment, penetration test or security certification.

## Previous published increment: practice-v8 structured analytic rubric

The deterministic grader now supports two-to-twenty explicit analytic criteria mapped one-to-one to structured response fields. Criterion points must match field points and sum to the parent total. The first increment supports keyed single-choice fields and uses the existing deterministic choice grader for each criterion. Unknown fields reject the whole item; missing fields receive no points; malformed and prompt-injection text cannot earn credit. Criteria and evidence anchors stay server-side while the learner sees the prompt, options and points. No natural-language reasoning or keyword matching is scored.

Foundations of Cell and Molecular Biology version 0.3.1 adds an original four-criterion formative item on delivery controls, promoter occupancy, motif dependence, and limits on causal inference. It is mapped to the existing experimental-logic outcome and is explicitly limited to the short partial course. The syllabus and package still lack a 12–15 week schedule, substantial weekly work, laboratories, exams, and an integrative project; this increment does not change maturity.

Final local suite for this increment: **254 tests passed** (backend 177, content authoring 46, frontend unit 19, Playwright 8, legacy state 4). Content validation reports 25 packages, 101 lessons, 104 questions, 202 cards and 25 cases; zero errors and 125 explicit depth/coverage warnings. The deployed content check grades 106 supported practice specifications. Ruff, frontend lint/Prettier, TypeScript/Vite build (203 modules), and source/bundle scan (367 files, 0 findings) passed. Playwright exercised the structured response's 3/4 partial credit, criterion-level feedback, reload persistence and accessibility scan, along with the existing enrollment, data-interpretation and audited appeal paths.

`docker compose up --build -d --wait --wait-timeout 180` passed; database, API and web were healthy and the migration service exited successfully. Alembic reports `0003 (head)`, the API health endpoint reports `ok`, and the curriculum endpoint returns 62 nodes and 8 pathways. Production Compose configuration passed with validation-only placeholders. These are local checks using synthetic data; they do not establish a deployment or security certification.

## Prior increment: audited learner appeals and manual formative adjustments

Alembic revision `0003` stores each learner appeal separately from its immutable attempt and records one append-only instructor decision. An operator-configured registered-account email allowlist gates the instructor queue. A current-version appeal can be adjusted, upheld or declined; stale-version prompts cannot be scored against an unavailable question. Adjustments appear as effective formative scores while the automatic score/result remain intact. Ownership, self-review denial, CSRF, score bounds, duplicate reviews, reviewer anonymization and learner deletion have backend coverage. The interface includes a learner request form, accessible instructor queue and gradebook/history labels. This is a narrow formative appeals feature, not staffed course grading or protected examination infrastructure.

Final local checks for this increment: **244 tests passed** (backend 172, content authoring 43, frontend unit 18, Playwright 7, legacy-state 4). Frontend lint/Prettier, TypeScript/Vite production build (203 modules), Ruff, the 25-package content validator (101 lessons, 103 questions, 202 cards and 25 cases; 0 errors and 125 explicit depth/objective warnings), and the source/bundle security scan (367 files, 0 findings) passed. The full browser flow exercised enrollment, lesson practice, appeal submission, an allowlisted human score adjustment, reload persistence and gradebook display; the instructor review view had no detected WCAG 2/2.1 A/AA violations. The backend suite emitted upstream Starlette/httpx and Python `datetime.utcnow()` deprecation warnings; they did not fail tests.

`docker compose up --build -d --wait --wait-timeout 180` passed after the final rebuild. PostgreSQL, API and web reported healthy; the credential initialization and migration services exited successfully. Alembic reports `0003 (head)`, `/api/v1/health` returns `ok`, and `/api/v1/curriculum` returns 62 nodes across 8 pathways. `docker compose -f compose.production.yaml config --quiet` also passed with a synthetic hostname and validation-only secret placeholders. These checks use synthetic local accounts and do not establish a public deployment or a security audit.

The preceding data-interpretation increment passed **229 tests with 1 skipped** across backend (167), course authoring (37 plus 1 skipped), frontend unit (16), Playwright (5), and legacy state tests (4). Its inventory was 25 packages, 101 lessons, 103 questions, 202 cards and 25 cases, with zero content errors and 125 disclosed depth/coverage warnings. Its API integration check graded 105 supported practice specifications. Current incremental results follow.

## Milestone 4 curriculum-map increment

The new map contains 25 existing partial package nodes plus 37 explicit **catalog-only** subject nodes in eight pathways (62 nodes total). The JHU pathway lists organic chemistry, biochemistry, molecular biology, cell biology, and all eight requested advanced areas. Its links are curriculum references only; no Johns Hopkins teaching text or assessment was copied. The supplied catalogue URL ending in `regenerative-stem-cell-technologies-master-science/` could not be opened; the repository links the verified 2026–27 canonical catalogue page and the public degree/course page instead. This creates no affiliation, equivalency, admission, or credit claim.

The versioned schema and content validator check catalog maturity, pathway/topic coverage, package and source references, duplicate descriptions, placeholders, package/catalog ID collisions, and prerequisite cycles across both node types. The FastAPI `/api/v1/curriculum` response contains maturity and prerequisite metadata; Playwright confirmed the live endpoint serves 62 nodes and 8 pathways. The accessible catalog explorer exposes dependencies and lets learners open related partial packages while marking planned areas as not yet authored.

Validation for this increment: **235 tests passed, 1 skipped** across content authoring (40 plus 1 skipped), backend (168), frontend (17), Playwright (6), and legacy-state tests (4). Content validation reports 25 packages, 101 lessons, 103 questions, 202 cards and 25 cases; zero errors and 125 disclosed depth/coverage warnings. Ruff and frontend lint passed; the TypeScript/Vite production build passed (202 modules). The API content integration check passed for 25 packages and 105 supported practice specifications. Live health and curriculum endpoint checks passed (healthy, 62 nodes, 8 pathways, 37 catalog-only nodes). The bundle/security scan reported 0 findings across 365 files; `npm audit --audit-level=high` reported no known vulnerabilities. Docker Compose rebuilt and reported database, API and web healthy, with the migration service complete.

## Previous published increment: deterministic data interpretation

Grader policy `practice-v7` enables one composite item in a supplemental original statistics lesson. It asks for a unit-checked mean difference and a choice of the strongest evidence-bounded conclusion. Each field receives separate points; omitted fields receive zero; unknown fields reject the response; malformed or injection-like text cannot earn credit. The grader does not score prose, keyword overlap, or reasoning. Public learner DTOs include only field identifiers, prompts, options, units and points. The hidden answer specifications remain server-side and the production frontend bundle scan found no private answer markers.

The new statistics manifest is version 0.1.1 and remains **partial**. Its added lesson explains sample contrasts, uncertainty requirements and limits on causal inference, and provides two original retrieval cards that appear behind reveal controls in the lesson reader. Its source map labels the material original and MIT OCW 18.05 link-only comparator. No MIT material was copied or adapted. The public course remains a short package, not a semester course.

Current commands and results: `docker compose up --build -d --wait --wait-timeout 180` (PASS; API, web and PostgreSQL healthy; Alembic migration service exited successfully); `docker compose run --rm --no-deps api pytest -q -p no:cacheprovider` (167 passed); `python tools/validate_content.py --root .` (25 courses, 101 lessons, 103 questions, 202 cards, 25 cases; 0 errors, 125 warnings); `docker compose run --rm --no-deps api python -m courselab.check_content /content` (25 packages, 105 supported specifications passed); root `pytest tests/content` (37 passed, 1 skipped); frontend `npm run lint`, `npm test` (16 passed), and `npm run build` (PASS); `npm run test:e2e` (5 passed, including retrieval-card reveal plus data-interpretation partial-credit and persistence paths); `npm run test:legacy` (4 passed); `docker compose run --rm --no-deps api ruff check --no-cache .` (PASS); `python tools/check_security.py --bundle frontend/dist` (363 files, 0 findings); `npm audit --audit-level=high` and `uv run --project backend --with pip-audit pip-audit -r backend/requirements.txt` (0 known vulnerabilities each). The full Compose scenario exercised guest enrollment, lesson viewing, a split-field submission, feedback display, and reload persistence. The API health endpoint returned `status: ok`; Alembic reports `0002 (head)`.

## Milestone 3 incremental validation

The implementation includes multiple-select partial credit, version-pinned question digests, explicit package-version updates, numeric grader v5, reproducible authored variants, and objective evidence v1. Objective points aggregate the best score once per distinct tagged question; retry counts remain visible but cannot inflate breadth. The provisional study indicator requires three distinct questions, at least 80% coverage of tagged questions, and at least 80% of possible points on attempted questions. The API returns its policy version and thresholds; the learner view explains that a positive indicator is not a mastery certification. The numeric implementation parses a bounded, documented subset of SI and biological units into exact rational scales and seven base dimensions, converts learner values into the authored unit, combines absolute and bounded relative tolerance against the authored answer, checks optional author-provided dimensions, and enforces optional 1–12 significant-figure requirements after the value passes tolerance. Decimal precision is counted from the learner's notation; the reader exposes the required precision as accessible question metadata and explanatory helper text. Contextual `pH`, `units`, and `mol ATP` labels are exact-label-only and cannot be composed; unknown and affine units fail closed. Numeric input length, decimal magnitudes, unit expression length, token count, exponents, relative tolerance, and significant-figure policy values are bounded. The digest is omitted from learner DTOs because it fingerprints answer-bearing content. Public lesson DTOs expose required precision and the selected authored prompt/options, never answer keys. Historical attempts remain unchanged with their recorded grader version and null digest where previously absent.

Authored variants are a finite choice among explicitly written forms, selected deterministically from a signed seven-day seed token bound to course, content version, and question. The example biology bank has three distinct forms for one practice item. The API returns a whitelisted prompt/options DTO plus the opaque token; the attempt resolves and grades the matching server-side specification and records its variant ID and digest. The learner history shows that variant and its feedback details. This does not generate numeric parameter variants and does not secure public practice material as an exam bank.

The symbolic plugin uses SymPy 1.14.0 behind an AST allowlist and explicit length, depth, node-count, degree, term-count, variable-count and operation-count limits. It accepts rational arithmetic with declared variables and typed assumptions, normalizes learner `^` powers to mathematical precedence, and compares forms using targeted rational cancellation. Python calls, attributes, subscripts, undeclared names, unsupported functions and expressions outside the limits fail closed. An original quotient-rule item in Calculus I version 0.1.1 exercises alternate-form grading; the course remains partial. The item answer is excluded from its public lesson DTO, the actual Compose-backed browser submission earned formative credit and saved feedback, and injection text earned zero points. This is not a general symbolic calculus engine and it does not assess derivation or domain restrictions.

Commands for this increment included `docker compose build api`, `docker compose run --rm --no-deps api pytest -q -p no:cacheprovider`, `docker compose run --rm --no-deps api ruff check --no-cache .`, `python tools/validate_content.py --root .`, `docker compose run --rm --no-deps api python -m courselab.check_content /content`, `npm run lint`, `npm test`, `npm run build`, `npm run test:e2e`, `npm run test:legacy`, `npm audit --prefix frontend --audit-level=high`, `uv run --project backend --with pip-audit pip-audit -r backend/requirements.txt`, `python tools/check_security.py --bundle frontend/dist`, and `docker compose up --build -d`. All passed after correcting two expected test totals for the new practice item. The local Compose API and web services reported healthy; Alembic remained at `0002 (head)`.

## Previous Milestone 3 validation snapshot

The following command list, tables and notes record the earlier variant/objective-evidence increment before bounded symbolic grading was added. They are retained as a historical baseline; the current increment results are listed above.

Commands run from the repository root or its `frontend`/`backend` subdirectory as applicable:

```sh
uv run --project backend --with pytest --with ruff --with jsonschema python -m pytest -q
uv run --project backend --with pytest --with ruff --with jsonschema ruff check backend/courselab backend/tests
npm --prefix frontend run lint
npm --prefix frontend run test
npm --prefix frontend run build
npm audit --prefix frontend --audit-level=high
npm --prefix frontend run test:e2e
uv run --project backend --with pytest --with ruff --with jsonschema python tools/validate_content.py
uv run --project backend --with pytest --with ruff --with jsonschema python tools/check_security.py --bundle frontend/dist
npm run test:legacy
docker compose up --build -d --wait --wait-timeout 180
docker compose exec -T api alembic current
docker compose exec -T api python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/api/v1/health').read().decode())"
```

| Check | Result |
| --- | --- |
| Combined backend/content-security pytest | 173 passed, 1 skipped; 1 upstream Starlette/httpx deprecation warning |
| Ruff | All checks passed |
| Frontend lint/format | Passed |
| Vitest | 14 passed across 6 files |
| TypeScript/Vite build | Passed; 202 modules |
| npm audit | 0 known vulnerabilities |
| Playwright | 3 passed; guest enrollment, both choice types, a seeded variant submission, objective evidence state, feedback, notes, progress, account export/deletion, and hidden-solution checks |
| axe | No detected WCAG 2/2.1 A/AA violations in catalog, lesson, and practice gradebook views |
| Legacy state tests | 4 passed |
| Content validator | 25 courses, 100 lessons, 101 base questions, 200 cards, 25 cases; 0 errors and 125 explicit warnings |
| API content integration | 25 course packages and 103 supported specifications including authored variant forms |
| Source/bundle boundary scan | 362 files; 0 findings, including the production JavaScript bundle |
| Docker Compose/PostgreSQL | Services healthy; migration `0002 (head)`; health status `ok`; local origins only |
| Production Compose configuration | Valid with synthetic hostname, non-secret path, and validation-only token key |
| GitHub Actions | PASS for objective-evidence commit `b699162`; [workflow run](https://github.com/dylanstechmann/uniStemCourseSimulators/actions/runs/37376974796). |

The migration test confirms preexisting attempts survive with no invented specification digest. Numeric grader tests recalculate conversion and absolute/relative-tolerance boundaries for rates, compound concentration/time units, lengths, acceleration, percentages and derived units; they also check significant-figure counts across decimal/exponent notation and integer trailing zeros, a 12-figure upper bound, invalid policies, negative/zero answers, dimensions, exact-label contextual units, unknown/affine units, malformed/incompatible units, alternate micro symbols, exponent bounds, and SI case distinctions. The deployed-content integration check grades all 101 published practice specifications and verifies learner DTOs omit solution data. An API test confirms precision metadata is public while answer specifications remain private, and that an in-tolerance answer with excess precision receives a specific diagnostic. A version-upgrade API test verifies old attempts remain in history, are excluded from the new-version aggregate, and only current-version work contributes to that gradebook. For browser tests, the workspace container joined the app network and temporarily added `http://web` to its allowed-origin list; the application was then recreated with only documented localhost origins. The end-to-end flow persisted guest enrollment, lesson practice, feedback, notes and progress and verified that public lesson DTOs omit answer specifications. These checks do not amount to a penetration test or prove code-execution isolation; the arbitrary-code runner and LLM feedback providers remain disabled.

The historical Milestone 1 and 2 validation record follows. Its counts describe the state before this M3 increment.

## Baseline and milestone 1

Before changes, inspected README, LICENSE, docs, app/data/pathways, HTML and CSS. Started the unchanged static reader on localhost:4173 in the shared development container. Used the first cell-biology practice item, saved a synthetic note and reloaded; result/note persisted without console errors. [CURRENT_STATE_AUDIT.md](CURRENT_STATE_AUDIT.md) records behavior, counts and limitations.

Milestone 1 renamed the product, retained a backed-up storage migration, introduced schemas/maturity/provenance, and preserved 25 partial packages: 100 readings/questions, 200 cards and 25 cases. Integrated checks passed 34 content tests, 4 state tests and JavaScript syntax checks. Browser regression confirmed the new identity and retained state. Intermediate failures from a short robotics hint and a pytest invocation from the wrong directory were corrected. Legacy asset URLs were versioned to resolve stale module caching.

Local milestone 1 commit: `5ad7563`; published GitHub milestone 1: `ccefbba1fa721e655c83793471c3597427c4b19c`. Checkout and remote originally had separate histories. Publication uses non-forced Git Data API commits preserving the remote parent chain; local/remote commit IDs differ.

## Milestone 1 and 2 automated commands and results

The shared workspace Linux development service used Node 24/Python 3.11; runtime images use Node 24/Python 3.12. Run from the repository root, then backend as shown:

```sh
python3 -m venv /tmp/courselab-final
/tmp/courselab-final/bin/pip install -r requirements-dev.txt -r backend/requirements.txt
/tmp/courselab-final/bin/python tools/validate_content.py
/tmp/courselab-final/bin/python -m pytest tests -q
npm run test:legacy
/tmp/courselab-final/bin/ruff check backend tools tests
/tmp/courselab-final/bin/python tools/check_security.py --bundle frontend/dist
cd backend
/tmp/courselab-final/bin/python -m pytest -q
/tmp/courselab-final/bin/python -m courselab.check_content ../content
```

| Check | Actual final result |
| --- | --- |
| Content/schema validator | PASS; 25 courses, 100 lessons/questions, 200 cards, 25 cases; 0 errors |
| Explicit warnings | 100 preserved short readings; 25 incomplete outcome-coverage warnings |
| Content/security pytest | 36 passed, 79.28 seconds |
| Legacy state tests | 4 passed |
| Ruff | All checks passed |
| Source/bundle boundary scan | 356 source files; 0 findings |
| Backend pytest | 71 passed, 11.25 seconds |
| API/content integration | 25 packages and 100 supported practice specifications passed |

Backend coverage includes ownership, session/password handling, CSRF/Origin, guest conversion, export/delete, immutable attempts, malformed/injection input, units, tolerance/alternate numeric forms, unsupported specifications, restricted-question denial, hidden solution fields, and Alembic upgrade/downgrade/schema comparison. One upstream Starlette TestClient/httpx deprecation warning remains. Automated backend fixtures use SQLite; real PostgreSQL was also exercised below.

```sh
cd frontend
npm ci
npm run lint
npm run test
npm run build
npm audit --audit-level=high
npx playwright install --with-deps chromium
npm run test:e2e
```

| Check | Actual final result |
| --- | --- |
| ESLint/Prettier | PASS |
| Vitest | 9 passed in 6 files, 27.21 seconds |
| TypeScript/Vite production build | PASS; 202 modules |
| npm audit | 0 known vulnerabilities |
| Chromium Playwright | 3 passed, 5.0 seconds |
| axe catalog/lesson scans | 0 detected WCAG 2/2.1 A/AA violations in those views |

The workspace test container could not reach the loopback-bound application through `host.docker.internal`. Final Playwright joined the application's network through an untracked workspace override, used `E2E_BASE_URL=http://web`, and temporarily allowed that exact test origin. Final Compose restored default localhost/127.0.0.1 origins. CI tests on the Ubuntu host's localhost and needs no workspace override.

The initial integrated browser workflow caught a real gradebook DTO mismatch: API limitations are a string, while frontend code iterated an array. Corrected the TypeScript type/rendering, added a regression fixture, rebuilt and passed all browser tests. CRLF formatting failures were corrected with LF normalization and `.gitattributes`.

The browser flow covers guest enrollment, reading, submission/feedback, notes/read marks/bookmarks, reload persistence, gradebook/history, account conversion preserving enrollment, export and deletion. Public DTO tests exclude assessment answer/solution specifications. nginx returns 404 for authoring banks, legacy answer-bearing JavaScript and `/.env`. Bundle scans reject private assessment markers. Public authoring practice specifications remain discoverable in the repository; worked examples are intentionally public readings. No restricted production exam keys, real learner exports, API keys or database passwords are committed. These bounded scans are not a penetration test.

An initial Python audit found advisories in older Starlette/pytest dependencies. Updated to FastAPI 0.142.2, Starlette 1.7.0 and pytest 9.1.1, reran 71 backend tests and the dependency audit: no known vulnerabilities reported. [backend/DEPENDENCY_AUDIT.md](../backend/DEPENDENCY_AUDIT.md) records details. Container operating-system scanning is not included.

## Full Compose and PostgreSQL persistence

From the repository root:

```sh
docker compose up --build -d --wait --wait-timeout 180
docker compose ps
docker compose exec -T api alembic current
docker compose restart db api
docker compose up --build -d --wait --wait-timeout 180
```

Default Compose started with newly initialized named volumes under the then-current project identity and no manually supplied password. Credential initialization and Alembic exited 0; migration is `0001 (head)`. PostgreSQL/API/web became healthy. Build-time content validation passed. HTTP health reported `status: ok` and disabled programming/LLM capabilities. Only nginx localhost:8080 is published; database/API ports remain internal.

A separate browser check enrolled a guest in biology, submitted the correct first choice and received 1/1 practice points with reasoning explicitly unassessed. Saved a synthetic note and marked a lesson read. After PostgreSQL/API restart and API recreation, reload retained note, read mark, enrollment and feedback. The gradebook retained 1/4 available practice points and the saved attempt/version/time. No browser console errors appeared. This checks database persistence beyond browser storage.

The preserved legacy reader runs separately on localhost:4173 with historical synthetic note/result retained. It is excluded from the default application image because its public practice answers cannot protect restricted assessments.

## Backup, restore and production configuration

Restored a custom archive into a newly created disposable database:

```sh
docker compose exec -T db pg_dump -U courselab -d courselab --format=custom --file=/tmp/courselab-validation.dump
docker compose exec -T db createdb -U courselab courselab_restore_check_20261005
docker compose exec -T db pg_restore -U courselab -d courselab_restore_check_20261005 --no-owner --no-acl --single-transaction --exit-on-error /tmp/courselab-validation.dump
```

All exited 0. Both active/restored databases contained 2 synthetic users, 2 attempts, 2 notes and 2 progress rows. Active data was not overwritten. Removed only the disposable database/archive afterward. This is a local logical restore rehearsal, not off-host disaster recovery or application cutover validation.

`docker compose -f compose.production.yaml config --quiet` passed with a validation-only hostname and existing non-secret path. Caddy configuration validation passed in a network-disabled container with `COURSELAB_DOMAIN=example.invalid`; a formatting warning was corrected and validation rerun. No production service, certificate issuance or public HTTPS was tested. [DEPLOYMENT.md](DEPLOYMENT.md) gives migration, secret permissions, proxy/domain/HTTPS and binary-safe backup/restore commands plus hardening limits.

## Sources, migration and remaining work

28 official sources are registered. No third-party instructional assets were copied/adapted. MIT software licensing is retained with documented separate educational-content/OCW boundaries. Institutional references establish curriculum alignment only.

`python tools/validate_content.py --check-links` exited 1: 26 references were reachable; JHU degree-details and admission-requirements pages returned HTTP 403 to the probe. Official page research was possible earlier. A 403 does not establish that a link is broken, but the automated live-link gate has not passed.

`node tools/migrate_prototype.mjs` correctly refused an overwrite (expected exit 1). Rehearsals require `--output` with a fresh directory. Git whitespace checks passed.

## API route boundaries and timestamp generation (2026-10-10)

The gradebook endpoint now lives in `backend/courselab/gradebook.py`; it uses shared identity/enrollment dependencies and retains the formative evidence summary and weighted-course-grade response. Enrollment creation/version upgrades and the learner assessment-plan view live in `backend/courselab/enrollments.py`. Enrollment-pinned plan creation and immutable graded-source archiving live in `backend/courselab/assessment_plans.py`; digest-verified serialization and reviewer views live in `backend/courselab/graded_views.py`; graded question delivery, explicit public-practice delivery and submission live in `backend/courselab/graded_routes.py`, backed by the source/form service in `backend/courselab/graded_assessments.py`; graded history and appeals live in `backend/courselab/graded_appeals.py`; learner export and deletion live in `backend/courselab/learner_account.py`. `backend/courselab/main.py` owns app construction, middleware and exception handlers. `backend/courselab/db.py` generates UTC timestamps with an explicit UTC timezone before converting to the established timezone-naive UTC storage format. The full backend suite passed: 4,742 passed, 2 expected symbolic-builder skips; Ruff passed across `courselab` and `tests`. The only runtime warning is the upstream Starlette `TestClient`/httpx deprecation.

Broader local regression passed as well: Biology integrity/candidate/assembly checks (127 passed); frontend unit tests (43 passed in 13 files), type-check, lint/format and production build (209 modules); and the all-course validator (25 courses, 384 lessons, 2,233 questions, 1,276 cards, 25 cases; 0 errors, 96 disclosed depth/limitation warnings). `npm ci` reported 0 known vulnerabilities. `git diff --check` passed; Git emitted only existing line-ending normalization notices for modified files.

The assessment-candidate audit `--check` passed against the committed report. Biology remains `partial`, `unreviewed` and `formative-only`; the audit lists 15 inactive public files for 14 intended components, with candidate-specific, independent-review, workload and operator-release gates still open. The review register remains unassigned, and the workload protocol remains not collected.

The production API image now has a Docker health check that calls the existing database-backed `/api/v1/health` endpoint. Production Compose waits for the API health check before starting web and waits for web health before starting the proxy. A separate temporary Compose project started PostgreSQL, completed migrations, and reached API/database `healthy`; Alembic reported `0010 (head)`. Its uniquely named test volumes and containers were removed afterward. This makes startup order explicit; it does not add rollback, monitoring or public-deployment evidence.

## Biology course-scope audit (2026-10-10)

The current Biology manifest maps a proposed 14-week sequence. Original lesson pairs and formative practice cover instructional weeks 1–7 and 9–14; week 8 is deliberately reserved for an ungraded cumulative review, not a new lesson pair or midterm. The all-course validator passed with 25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases (0 errors; 96 disclosed depth/limitation warnings). This confirms the proposed schedule and authored instructional scope, not 14 weeks of measured workload or semester equivalence. The course remains `partial`, unreviewed and formative-only because candidate assessments have not passed independent recalculation, qualified academic/accessibility review, workload measurement, protected delivery checks and operator release.

## PostgreSQL runtime-role separation (2026-10-10)

Development and production Compose now generate/mount distinct bootstrap and API runtime passwords. A one-shot `db-roles` service provisions `courselab_app`; Alembic uses the bootstrap account, and API containers use the non-administrative runtime account. The provisioning SQL grants CRUD on existing tables and sequence usage, then sets matching default privileges for objects created by the bootstrap migration owner. A fresh uniquely named PostgreSQL 17 Compose stack reached API `healthy`, migrated to `0010 (head)`, and created a guest session through the API. PostgreSQL reported `courselab_app` as not superuser, database creator or role creator; it could not create a table in `public`. Future-grant checks passed for a temporary table and sequence, which were removed. Both Compose configurations validated with placeholder production settings. The complete backend suite passed (4,742 passed, 2 expected skips) and Ruff passed. This validates startup and database grants on a fresh local stack, not production rotation/recovery or row-level isolation; the API role still has access to all application rows and protected source archives.

## Production resource limits (2026-10-10)

The production Compose configuration sets CPU and memory bounds for PostgreSQL, API, migrations, nginx and Caddy. API/database/migration defaults are configurable in the untracked environment file; web/proxy caps are fixed in the example. The resolved production configuration validated with placeholder secrets/domain. These caps are initial operating bounds only; no representative concurrency, throughput, database-growth or resource-throttling load test was run.

## Calculus I introductory-reading expansion (2026-10-10)

Calculus I advances from 0.4.0 to 0.4.1. Its first reading now distinguishes a limit from the value assigned at a point, checks unequal one-sided limits, and works through a local square-root approximation with a second-derivative remainder bound. The existing objectives, public practice keys, item totals and schedule remain unchanged; three short prototype readings remain. The regression file passed 76 tests, including direct evaluations of the removable-hole table and Taylor error bound. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors, 95 disclosed legacy-depth warnings). The assessment-candidate report was regenerated and passed its drift check. The checks are same-AI development evidence, not qualified academic review or workload/accessibility evidence.

## Calculus I derivative-rules expansion (2026-10-10)

Calculus I advances from 0.4.1 to 0.4.2. The week-3 reading now explains product, quotient and chain rules, then follows units through exponential decay and a concentration-dependent response. Existing practice keys and assessment policy are unchanged; two compact prototype readings remain. The focused regression file passed 77 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 94 disclosed legacy-depth warnings), and the assessment-candidate report was regenerated and passed its drift check. These same-AI checks do not supply independent review or evidence of workload/accessibility.

## Calculus I optimization-domain expansion (2026-10-10)

Calculus I advances from 0.4.2 to 0.4.3. The week-6 reading now reduces a fixed-perimeter rectangle to a feasible one-variable function, checks an interior critical point against endpoint behavior, distinguishes open and closed domains, and demonstrates a dimensionally consistent area rate. Existing practice keys, objectives and item counts remain unchanged; one compact prototype reading remains. The focused regression file passed 78 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 93 disclosed legacy-depth warnings). The assessment-candidate report was regenerated and passed its drift check. These same-AI checks do not supply independent academic review or evidence of workload/accessibility.

## Calculus I integral and Fundamental Theorem expansion (2026-10-10)

Calculus I advances from 0.4.3 to 0.4.4. The week-9 reading now distinguishes signed net change from total transfer, connects accumulation and rate through both parts of the Fundamental Theorem, and recovers a final state from an initial value with consistent units. Existing practice keys, objectives and item counts remain unchanged; all fourteen scheduled readings now have expanded or original instructional text. The focused regression file passed 79 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 92 disclosed legacy-depth warnings). The assessment-candidate report passed its drift check. These same-AI checks do not supply independent academic review or evidence of workload/accessibility.

## Calculus II integration-method and improper-limit expansion (2026-10-10)

Calculus II advances from 0.4.0 to 0.4.1. The week-1 reading now demonstrates substitution, integration by parts and partial fractions, and derives convergence conditions for power integrals at infinite and finite singular endpoints. Existing practice keys and objectives remain unchanged; three compact prototype readings remain. The focused regression file passed 83 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 91 disclosed legacy-depth warnings). The assessment-candidate report passed its drift check. These same-AI checks do not provide independent academic review or evidence of workload/accessibility.

## Calculus II work-and-accumulation expansion (2026-10-10)

Calculus II advances from 0.4.1 to 0.4.2. The week-4 lesson now derives work as accumulated force over displacement, checks N·m units, and interprets the sign from force direction and bound order. Existing practice keys and objectives are unchanged; two compact prototype readings remain. The focused regression file passed 84 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 90 disclosed legacy-depth warnings). The assessment-candidate report passed its drift check. These same-AI checks do not provide independent academic review or evidence of workload/accessibility.

## Calculus II sequences-and-series expansion (2026-10-10)

Calculus II advances from 0.4.2 to 0.4.3. The week-7 lesson now distinguishes sequences and series, derives a geometric partial sum and exact tail, explains the necessary-versus-sufficient convergence distinction, and checks a Taylor remainder against a Lagrange bound. Existing practice keys and objectives remain unchanged; one compact prototype reading remains. The focused regression file passed 85 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 89 disclosed legacy-depth warnings). The assessment-candidate report passed its drift check. These same-AI checks do not provide independent academic review or evidence of workload/accessibility.

## Calculus II Taylor-error expansion (2026-10-10)

Calculus II advances from 0.4.3 to 0.4.4. The week-10 reading now builds Taylor polynomials from derivatives, checks the Lagrange remainder over the full interval, and separates finite-polynomial accuracy from infinite-series convergence. Existing practice keys and objectives remain unchanged; all fourteen scheduled readings now have expanded or original text. The focused regression file passed 86 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 88 disclosed legacy-depth warnings). The assessment-candidate report passed its drift check. These same-AI checks do not provide independent academic review or evidence of workload/accessibility.

## Robotics & Mechatronics frame-transform expansion (2026-10-10)

Robotics advances from 0.4.0 to 0.4.1. Its week-1 reading now defines labeled homogeneous transforms, validates rotation properties, demonstrates composition order and recovers coordinates with the inverse transform. Existing practice keys and objectives remain unchanged; three compact prototype readings remain. The focused regression file passed 107 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 87 disclosed legacy-depth warnings). The assessment-candidate report passed its drift check. These checks do not supply independent robotics, safety or accessibility review.

## Robotics & Mechatronics kinematics expansion (2026-10-10)

Robotics advances from 0.4.1 to 0.4.2. Its week-3 lesson now derives the two-link forward equations, checks the reachable annulus, solves both branches for one target and states joint-limit and singular-boundary qualifications. Existing questions, keys and objectives remain unchanged; two compact prototype readings remain. The focused regression file passed 108 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 86 disclosed legacy-depth warnings). The assessment-candidate report passed its drift check. These checks do not supply independent robotics, safety or accessibility review.

## Robotics & Mechatronics dynamics and actuator expansion (2026-10-10)

Robotics advances from 0.4.2 to 0.4.3. Its week-7 reading now develops the fixed-axis rotor model, torque-work-power relations, an energy consistency check, and the gearbox torque/speed/efficiency tradeoff. Existing practice keys and objectives remain unchanged; one compact prototype reading remains. The focused regression file passed 109 tests and Ruff passed. Full content validation passed (25 courses, 384 lessons, 2,233 questions, 1,276 cards and 25 cases; 0 errors and 85 disclosed legacy-depth warnings). The assessment-candidate report passed its drift check. These checks are not independent robotics, device or safety review.

GitHub Actions configuration runs content/security, backend/frontend lint/tests/builds, Compose and browser flows with diagnostics. Hosted CI passed for objective-evidence commit `b699162` in addition to the local checks above.

Milestone 3 remains in progress: broader structured/data/design rubrics, numeric parameter generation, weighted categories, robust objective mastery from diverse assessments, broader evidence-linked misconception feedback, provider interfaces and an isolated code worker still need implementation and verification. The symbolic plugin supports rational expressions only; general symbolic calculus remains unsupported. Code execution and LLM providers remain disabled. Eight pathways and a visual graph are present. Biology's proposed 14-week instructional sequence is authored, with week 8 intentionally reserved for cumulative review; accepted assessment evidence, independent recalculation/mutation coverage, accessibility, workload and qualified course-content review remain future work in milestones 4–6. [ROADMAP.md](ROADMAP.md) records exact work and production hardening gaps.


## Cell Biology cumulative-practice expansion (2026-10-10)

Biology advances from 0.35.0 to 0.36.0. Four original formative questions add practice on mutation chemistry, electrochemical driving force, Michaelis–Menten parameter interpretation, and replicate-level inference. They appear in the topic practice sets and expand the week-8 cumulative review from 12 to 16 items (35 ungraded practice points). The course remains partial, unreviewed and formative-only; no inactive candidate or grade-bearing policy changed. The content-validation file passed (85 passed, 2 skipped). Full validation passed for 25 courses, 384 lessons, 2,274 questions, 1,276 cards and 25 cases, with zero errors or warnings. The objective-coverage report was regenerated; these checks do not replace scientific, accessibility or assessment review.


## Cell Biology numeric-key author audit (2026-10-10)

A separate arithmetic pass recomputed all 20 public `numeric`-type items in Biology 0.36.0 from their prompt values and equations. All 20 values fell within their declared grader tolerances; the bank contains no randomized numeric variants. The item-by-item formulas, keys and tolerances are recorded in [the audit](reviews/cell-biology-numeric-key-audit-0.36.0.md). This is author-side verification, not independent academic or assessment review; embedded numeric tables, labs and inactive candidate packets remain outside its scope. The percentage-point item now uses context-specific `pp`, and the grader rejects `%` for that answer. A learner-DTO regression confirms that `pp` is public while the answer key remains private; the backend grading/content-repository suites passed 157 tests, with one Windows-only symlink skip and one Starlette/httpx deprecation warning.


## Cell Biology public table-key source reconciliation (2026-10-10)

A new content regression reconciles all 114 numeric summary cells across 12 public CSV-upload practice items with their source CSV rows or values printed in the prompt. It verifies replicate grouping, filters the initial-rate set at 40 μM and the lineage table at day 8, recomputes means/counts, and checks the authored tolerances. The test passed; the audit lists each practice item and source. This verifies answer-key/source consistency for those summary cells, not scientific interpretation or any inactive candidate packet, and is not independent external review.


## Cell Biology topic comparator scope map (2026-10-10)

Biology advances from 0.36.0 to **0.37.0** with a week-by-week, topic-level comparison against selected public MIT OpenCourseWare materials. The map records local lesson/activity topics, comparator topic presence, local coverage boundaries and explicit omissions. It does not establish equivalent scope, depth, teaching time, prerequisites, assessment standards, workload, credit or endorsement; it has not received qualified instructor review. The course remains partial, unreviewed and formative-only. The syllabus and assessment crosswalk link to the new map. Content validation passed for 25 courses, 384 lessons, 2,274 questions, 1,276 cards and 25 cases with zero errors or warnings. The two focused content-validation regressions passed, the public table-key source-reconciliation regression passed, the objective-coverage `--check` passed and Ruff passed for the changed test file. `git diff --check` passed; Git emitted only its existing CRLF-normalization warnings.


## Cell Biology information-flow practice and mapping correction (2026-10-10)

Biology advances from 0.37.0 to **0.38.0**. An author-side objective/item review found that the PCR positive-control item was mapped to “Trace DNA information through transcription and translation,” although it tests control purpose; it now maps to the controls objective. Two original questions add sequence-based transcription/translation and a stipulated premature-stop consequence to the information-flow objective. They appear in the lesson's week-7 topical set and the ungraded week-8 review, now 18 questions and 37 points. The bank has 143 Cell Biology questions; repository inventory is 25 courses, 384 lessons, 2,276 questions, 1,276 cards and 25 cases.

A distinct-question count across the 69 lesson objectives now finds 18 with one mapped public item, 23 with two, and 28 with three or more. This is a mapping count only, not evidence of cognitive depth, mastery or independent validation. Content validation passed with zero errors or warnings; the objective-coverage drift check passed; five focused content-validation regressions passed after updating the private-assessment expected inventory to 2,277; and the public table-source reconciliation passed. The full content-validation file produced 86 passes and two skips, with that single stale inventory assertion corrected and rerun separately. Ruff and `git diff --check` passed; Git emitted CRLF-normalization warnings.


## Cell Biology complementary practice for quantitative objectives (2026-10-10)

Biology advances from 0.38.0 to **0.39.0** with three original formative items: a qualitative comparison of protonation below and above pKa, an interpretation of matched protein abundance/folding/specific-activity measurements, and a Michaelis–Menten initial-rate prediction at `[S] = 2 Km`. Each item appears in its topical assessment and the week-8 ungraded review, which now contains 21 questions and 40 points. The Cell Biology bank now has 146 questions; repository inventory is 25 courses, 384 lessons, 2,279 questions, 1,276 cards and 25 cases.

The new kinetic key recomputes as `Vmax = 4 s⁻¹ × 20 nM = 80 nM/s`, then `v₀ = 80 × 2/3 = 53.3333 nM/s`; it falls within the declared ±0.5 nM/s tolerance. Together, the 0.36.0 and 0.39.0 author-side arithmetic audits now cover all 21 public numeric-type keys. A distinct-question count finds 15 objectives with one item, 26 with two and 28 with three or more; this count is not a claim of depth or mastery. The [incremental numeric-key audit](reviews/cell-biology-numeric-key-audit-0.39.0.md) records the calculation and scope limits.

Content validation passed (25 courses, 384 lessons, 2,279 questions, 1,276 cards and 25 cases, with zero errors or warnings), and the objective-coverage `--check` passed. Six focused content regressions and the public table-source reconciliation passed; Ruff and `git diff --check` passed. The package remains partial, unreviewed and formative-only.


## Cell Biology later-week signaling and junction practice (2026-10-10)

Biology advances from 0.39.0 to **0.40.0**. Three original formative items broaden practice on receptor occupancy versus cellular response, GPCR/RTK relay logic, and desmosome versus focal-adhesion linkages. They appear in the week-11 and week-12 topical assessments only; week 8 remains a 21-item, 40-point review over weeks 1–7. Week 11 now has nine questions and 15 points; week 12 has eight questions and 14 points. The course has 149 public items, and repository inventory is 25 courses, 384 lessons, 2,282 questions, 1,276 cards and 25 cases.

A distinct-question audit finds 12 objectives with one public item, 29 with two, and 28 with three or more. This count does not establish depth or mastery. Content validation passed with zero errors or warnings, the generated objective-coverage report passed `--check`, seven focused content regressions and the CSV table-source regression passed, and Ruff plus `git diff --check` passed. The course remains partial, unreviewed and formative-only.


## Cell Biology controls and penetrance practice (2026-10-10)

Biology advances from 0.40.0 to **0.41.0**. Three original formative items add practice in compartment-marker interpretation, splice-perturbation controls, and age-specific penetrance study design. They appear in the week-3, week-9 and week-10 topical sets only. Week 3 now has three questions and five points; week 9 has nine questions and 15 points; week 10 has eight questions and 14 points. The week-8 review remains at 21 questions and 40 points over weeks 1–7. Cell Biology now has 152 public items; repository inventory is 25 courses, 384 lessons, 2,285 questions, 1,276 cards and 25 cases.

A distinct-question audit finds nine objectives with one public item, 32 with two, and 28 with three or more. This is a mapping count only, not evidence of depth or mastery. Content validation passed with zero errors or warnings; the generated objective-coverage report passed `--check`; all nine selected content regressions passed across the focused reruns; the public table-source regression passed; Ruff passed; and `git diff --check` passed with Git's existing CRLF-normalization warnings. The course remains partial, unreviewed and formative-only.


## Cell Biology early-course molecular and transport practice (2026-10-10)

Biology advances from 0.41.0 to **0.42.0**. Three original formative questions add complementary practice on hydrophobic assembly, carrier-mediated facilitated diffusion, and interpreting a solvent-exposed protein substitution. They appear in the week-1 and week-2 topical sets and in the weeks-1–7 cumulative practice. Week 1 now has seven questions and nine points; week 2 has seven questions and nine points; the cumulative review now has 24 questions and 43 points. Cell Biology has 155 public items; repository inventory is 25 courses, 384 lessons, 2,288 questions, 1,276 cards and 25 cases.

A distinct-question audit finds six objectives with one public item, 35 with two, and 28 with three or more. This is a mapping count only, not evidence of depth or mastery. Content validation passed with zero errors or warnings; the generated objective-coverage report passed `--check`; all ten selected content regressions passed across the focused runs; the public table-source regression passed; Ruff passed; and `git diff --check` passed with Git's existing CRLF-normalization warnings. The course remains partial, unreviewed and formative-only.


## Cell Biology chromatin, RNA and linkage practice (2026-10-10)

Biology advances from 0.42.0 to **0.43.0**. Three original formative items add practice on biological versus technical replication in chromatin assays, distinct RNA-processing roles, and linkage disequilibrium versus a causal variant. They appear in the week-7, week-9 and week-10 topical sets; only the week-7 question joins the weeks-1–7 cumulative review. Week 7 now has eight questions and 14 points, week 9 has ten questions and 16 points, week 10 has nine questions and 15 points, and the cumulative review has 25 questions and 44 points. Cell Biology has 158 public items; repository inventory is 25 courses, 384 lessons, 2,291 questions, 1,276 cards and 25 cases.

A distinct-question audit finds three objectives with one public item, 38 with two, and 28 with three or more. This count is a mapping measure, not evidence of depth or mastery. Content validation passed with zero errors or warnings; the objective-coverage report passed `--check`; all 11 selected content regressions passed across focused reruns; the public table-source regression passed; Ruff passed; and `git diff --check` passed with Git's existing CRLF-normalization warnings. The course remains partial, unreviewed and formative-only.


## Cell Biology late-course practice and objective coverage floor (2026-10-10)

Biology advances from 0.43.0 to **0.44.0**. Three original formative questions add practice on distinct cytoskeletal contributions, measured cell-cycle state versus a model-predicted kinase variable, and the boundary between in-vitro lineage markers and regenerative claims. They appear in weeks 12–14 only; the week-8 review remains at 25 questions and 44 points. Week 12 has nine questions and 15 points; week 13 has eight and 14 points; week 14 has eight and 14 points. Cell Biology has 161 public items; repository inventory is 25 courses, 384 lessons, 2,294 questions, 1,276 cards and 25 cases.

A distinct-question audit now finds at least two mapped public practice items for each of the 69 lesson objectives: 41 objectives have two items and 28 have three or more. This is a coverage floor, not evidence of depth, mastery, or independent validation. Content validation passed with zero errors or warnings; the objective-coverage report passed `--check`; all 12 selected content regressions passed; the public table-source regression passed; Ruff passed; and `git diff --check` passed with Git's existing CRLF-normalization warnings. The course remains partial, unreviewed and formative-only.


## Cell Biology structured association and regenerative-evidence practice (2026-10-10)

Biology advances from 0.44.0 to **0.45.0**. Two original three-part structured questions strengthen practice on genotype–phenotype association alternatives and regenerative evidence boundaries. They distinguish association from causal-variant evidence, measured lineage markers from function, and follow-up evidence from oversight requirements. They appear in weeks 10 and 14 only: week 10 now has ten questions and 18 points, week 14 has nine questions and 17 points, and week 8 remains at 25 questions and 44 points. Cell Biology has 163 public items; repository inventory is 25 courses, 384 lessons, 2,296 questions, 1,276 cards and 25 cases.

All 69 lesson objectives retain at least two distinct mapped public questions; 39 have two items and 30 have three or more. This is a mapping measure, not evidence of depth, mastery, or independent review. Content validation passed with zero errors or warnings; all 13 selected content regressions passed across focused reruns; the public table-source regression passed; the objective-coverage report passed `--check`; Ruff passed; and `git diff --check` passed with Git's existing CRLF-normalization warnings. The course remains partial, unreviewed and formative-only.

## Cell Biology independent-review handoff (2026-10-10)

Biology advances from 0.45.0 to **0.46.0** with a consolidated review handoff linking current scope, objective coverage, validation evidence, source and numeric audits, inactive assessment candidates, reviewer dispositions, and acceptance/release gates. The document is preparatory only; no independent review, workload result, institutional decision, or release approval has occurred. Package contents and question counts are unchanged. Content validation passed (25 courses, 384 lessons, 2,296 questions, 1,276 cards and 25 cases); the full content-validation test file passed 93 tests with two skips, and the public table-key regression passed. The objective-coverage drift check, Ruff, `git diff --check`, and all handoff local-link checks passed. The course remains partial, unreviewed and formative-only.

## Cell Biology candidate index and public audit refresh (2026-10-10)

The generated public assessment-candidate report was refreshed for current package versions, and the Cell Biology candidate index now identifies package 0.46.0 while retaining the fourteen proposed components and fifteen-file historical inventory. The public audit still reports Cell Biology as partial, unreviewed and formative-only, and preserves all unresolved independent-review, workload, protected-source, and operator-release gates. `python tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md`, the candidate-audit test module (9 passed), `python tools/validate_content.py` (25 courses, 384 lessons, 2,296 questions, 1,276 cards and 25 cases; zero errors or explicit limitation/depth warnings), the objective-coverage drift check and `git diff --check` passed. The private assessment source root is not configured, so this increment provides public-artifact inventory evidence only.

## Cell Biology structured explanation-practice additions (2026-10-10)

Biology advances from 0.46.0 to **0.47.0** with three original three-point structured formative items for explanation-focused objectives in weeks 6, 7 and 9: DNA strand/fork direction, nucleosome organization and remodeling, and distinct pre-mRNA processing steps. The corresponding objectives each now have three distinct mapped public questions; across all 69 objectives, 36 have two questions and 33 have three or more. Week 6 now has 8 questions/14 points, week 7 has 9/17, and week 9 has 11/19; the week-8 cumulative review remains 25/44. The new response fields are criterion-level selected responses and do not measure free-response explanation or mastery. Correct-answer positions vary across all four choices.

Content validation passed (25 courses, 384 lessons, 2,299 questions, 1,276 cards and 25 cases; zero errors or explicit limitation/depth warnings); the candidate-audit and objective-coverage drift checks, Ruff and `git diff --check` passed. Four directly affected course regressions plus nine candidate-audit tests and the public table-key regression passed (14 total). A broad run exposed one stale week-9 count assertion; that assertion was corrected and the affected tests were rerun. All candidate review, independent scientific/assessment/accessibility, workload, protected-source and operator-release gates remain unresolved. The package remains partial, unreviewed and formative-only.

## Cell Biology objective response-format inventory (2026-10-10)

Added `tools/objective_response_modes.py` and the generated [Cell Biology response-format report](CELL_BIOLOGY_RESPONSE_MODE_AUDIT.md). It inventories distinct public questions referenced by practice-mode assessments, lists their formats for each of the package's 69 objectives, and expands structured fields such as `single_choice×3`. It does not inspect candidate keys, private sources or learner responses, and explicitly does not infer skill validity, depth, free-response proficiency, accessibility, mastery or release readiness. The review handoff links the report, and CI now checks for report drift. The tool's two regression tests passed; content validation, all three report drift checks, Ruff and `git diff --check` passed. Cell Biology remains 0.47.0, partial, unreviewed and formative-only.

## Cell Biology ungraded matrix-design exercise and schedule reconciliation (2026-10-10)

Biology advances from 0.47.0 to **0.48.0**. Added a supplemental, ungraded written-design exercise linked from the week-12 syllabus and assessment crosswalk. Learners plan a matrix comparison that distinguishes accessible ligand, time-dependent mechanics and force-transmission alternatives, then self-check controls, replication, target engagement, readouts and inference limits. Responses are not collected or scored, and no question-bank item, point total or assessment policy was added. The exercise is in a separate file because the existing week-12 lesson is hash-pinned as a prerequisite by an inactive final candidate; preserving that source keeps the public candidate audit valid. Learner-facing syllabus and crosswalk counts were corrected to the current manifest for weeks 8–14.

The focused content, response-format, candidate-audit and table-key regressions passed (16 tests). Full content validation passed (25 courses, 384 lessons, 2,299 questions, 1,276 cards and 25 cases; zero errors or explicit limitation/depth warnings). The candidate, objective-coverage and response-format report drift checks, Ruff and `git diff --check` passed. Independent review, workload measurement and all protected-source/operator release gates remain open; Cell Biology remains partial, unreviewed and formative-only.

## Current Cell Biology schedule totals are checked against the manifest (2026-10-10)

Standardized the week-8 through week-14 question/point totals in the learner syllabus and assessment crosswalk. Added `test_syllabus_and_crosswalk_weekly_assessment_totals_match_manifest`, which derives each total from the manifest's question IDs and points and fails if either public summary drifts. The 17 focused Cell Biology, response-format, candidate-audit and table-key tests passed. Content validation passed (25 courses, 384 lessons, 2,299 questions, 1,276 cards and 25 cases); the three report drift checks, Ruff and `git diff --check` passed. No course content or maturity changed.
## Current increment: review handoff for Organic Chemistry I 0.4.5 (2026-10-11)

Pinned the Organic Chemistry package and prepared a handoff for crossed-aldol atom mapping, addition/dehydration balance, unsaturation and synthetic evidence cards. The draft has no procedure or measured product claim, and a snapshot regression verifies archive identity.

| Actual command/check | Result |
| --- | --- |
| Organic Chemistry regressions, project recalculations and snapshot identity | 95 passed. |
| Public package digest | Passed: version 0.4.5; archive SHA-256 `71c83febe743d75c7883f2063135304a0545c1bc37c220d2f3fb9388024c7e96`; manifest SHA-256 `4846969c10f7d0aa73c2eea6cd9b6b527a6a0d23b9891d8818969741854c074e`; 23 files; 318,093 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The project is inactive, ungraded, synthetic and unreviewed.

## Prior increment: inactive crossed-aldol identity dossier for Organic Chemistry 0.4.5 (2026-10-11)

Added a paper-only crossed-aldol model with donor/acceptor atom mapping, separate addition and dehydration balances, formula/unsaturation checks and synthetic qualitative evidence for two candidate products. It complements the enantiomeric-excess lab and amide case.

| Actual command/check | Result |
| --- | --- |
| Organic Chemistry regressions and project recalculations | 94 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

All evidence cards are synthetic constraints and do not establish real selectivity, yield, product identity or synthesis conditions.

## Current increment: review handoff for Biochemistry I 0.4.6 (2026-10-11)

Pinned the Biochemistry package and prepared a handoff for pH-dependent charge, two-state folding, denaturant stability and ligand-depletion binding. The staged model assumptions are explicit, and a snapshot regression verifies archive identity.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions, project recalculations and snapshot identity | 8 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `4c5a3598576c03603e61a9895327674ed2e9ef22aecb23b24f73259aff6db0b2`; manifest SHA-256 `c485b61b511ee7bbafccec9a0dfc84e953bfb947eca7e24bd1eed6ddc2dffa20`; 23 files; 283,399 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The project is inactive, ungraded, synthetic and unreviewed.

## Prior increment: inactive protein-state and ligand-binding portfolio for Biochemistry 0.4.6 (2026-10-11)

Added a paper-only portfolio comparing two fictional conditions through net charge, folded fraction, active-protein ligand depletion and a conditional folded-bound threshold. It is separate from the enzyme-kinetics lab and pathway-perturbation case.

| Actual command/check | Result |
| --- | --- |
| Biochemistry regressions and project recalculations | 7 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

All parameters are fictional; the two-state and staged-binding assumptions remain unreviewed.

## Current increment: review handoff for Physics: Electricity & Magnetism 0.4.5 (2026-10-11)

Pinned the Physics E&M package and prepared a handoff for series resonance, half-power bandwidth, peak/RMS power and energy storage. The RLC candidate set is a fictional paper model, and a snapshot regression verifies archive identity.

| Actual command/check | Result |
| --- | --- |
| Physics E&M regressions, project recalculations and snapshot identity | 114 passed. |
| Public package digest | Passed: version 0.4.5; archive SHA-256 `70054adfd562b360b002a809cacad83a9580b670f35f5c0e27e40c06fbdba7d7`; manifest SHA-256 `54e74d61f90624c636584986fe7c8ae2d30d92df16a5374a1e4022198d78e663`; 23 files; 303,689 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The project is inactive, ungraded, synthetic and not an instrument design.

## Prior increment: inactive series-resonance portfolio for Physics E&M 0.4.5 (2026-10-11)

Added a paper-only design comparison for fictional ideal RLC candidates, deriving resonance, half-power points, current, dissipation and reactive-energy maxima. It supplements the phasor unit without duplicating the source-loading lab or recording case.

| Actual command/check | Result |
| --- | --- |
| Physics E&M regressions and project recalculations | 113 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed; its component values and thresholds are fictional.

## Current increment: review handoff for Robotics & Mechatronics 0.4.6 (2026-10-11)

Pinned the Robotics package and prepared a handoff for cubic trajectory timing, actuator limits, stopping clearance and energy accounting. The single-joint scenario is explicitly mathematical and fictional, and a snapshot regression verifies archive identity.

| Actual command/check | Result |
| --- | --- |
| Robotics regressions, project recalculations and snapshot identity | 115 passed. |
| Public package digest | Passed: version 0.4.6; archive SHA-256 `7a6f75d52539ec36ad01cbd3f090f33646ddcd006f6247fa8e64085899955eb2`; manifest SHA-256 `186373df37612848ff92050f17bb8dc84d0792c33520abaeac90e525ca8288a1`; 23 files; 295,355 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The project is inactive, ungraded, synthetic and not a robot safety validation.

## Prior increment: inactive trajectory timing and actuator-margin portfolio for Robotics 0.4.6 (2026-10-11)

Added a paper-only trajectory draft connecting cubic time scaling to a fictional joint's speed, gravity/inertia torque and conditional stopping-clearance limits, then closing an ideal energy ledger. Also made the existing Robotics recalculation tests read UTF-8 explicitly so they collect on Windows.

| Actual command/check | Result |
| --- | --- |
| Robotics regressions and project recalculations | 114 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The draft remains inactive, ungraded and unreviewed; it establishes no hardware performance, protective function or safety.

## Current increment: review handoff for Genetics & Genomics 0.5.5 (2026-10-10)

Pinned the Genetics package and prepared a handoff for testcross phase, three-point mapping, interference and a separate penetrance calculation. Synthetic-data and non-causality boundaries are explicit, and a snapshot regression verifies archive identity.

| Actual command/check | Result |
| --- | --- |
| Genetics regressions, project recalculations and snapshot identity | 7 passed. |
| Public package digest | Passed: version 0.5.5; archive SHA-256 `c555049c4cea022be7d3a85f64fe61ce839091099195299949cabafa5fcf3ef3`; manifest SHA-256 `c671c9e3aca8d6a5c141fbcad44c20369065343156f79d3f84cbec42b2c95b02`; 25 files; 327,314 bytes. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The digest proves identity only. The project is inactive, ungraded, synthetic and unreviewed.

## Prior increment: inactive three-point mapping and penetrance portfolio for Genetics 0.5.5 (2026-10-10)

Added a paper-only portfolio combining fictional three-point testcross classes, phase and gene-order inference, interval and outer-marker recombination, double-crossovers, sample interference, and an independent Bayes calculation under penetrance.

| Actual command/check | Result |
| --- | --- |
| Genetics regressions and project recalculations | 6 passed. |
| Content validator | Passed: 25 courses, 387 lessons, 2,299 questions, 1,276 cards, 25 cases; 0 errors or explicit limitation/depth warnings. |
| Assessment-candidate and course-gap report drift checks | Passed. |
| Ruff and `git diff --check` | Passed. |

The project remains inactive, ungraded and unreviewed. The markers and family data are fictional and establish neither causation nor anyone's risk.

## Current increment: package-pin the eight Cell Biology homework datasets (2026-10-11)

The homework packets were already delivered through manifest lesson routes and linked in their syllabus weeks. Replaced their mutable raw-GitHub CSV URLs with package-relative links and added all eight datasets to the learner resource allowlist. Current learners receive current package bytes; enrolled learners can retrieve version-matched CSVs from archived course packages. No packet content, dataset values, assessment policy, maturity or review state changed.

| Actual command/check | Result |
| --- | --- |
| Focused Cell Biology repository, API, integrity, and handoff regressions | 13 passed; 66 unrelated tests deselected. |
| Open-homework data-to-example integrity regressions | 12 Cell Biology integrity tests passed. Example means for all eight packets and worked calculations spanning kinetics, penetrance, enrichment, half-life, matrix response and cell-state contrasts are independently recomputed from source data. |
| Content validator | Passed: 25 courses, 401 lessons, 2,411 questions, 1,341 cards and 25 cases; zero errors or explicit limitation/depth warnings. |
| Frontend unit suite | 46 passed. Production build and lint passed. |
| Digest-bound audits | Candidate audit, review-evidence scaffold, objective coverage, response-mode inventory, 21 numeric recalculations and 114 table recalculations passed drift checks. The evidence register records no review sign-offs and no release authorization. |
| Public package digest | Version 0.58.0; 122 files, 2,115,110 bytes; archive SHA-256 `484572596063c1e8a8f95f9c459dae580adcf11f512dd3875bd01659f7f94a4e`; manifest SHA-256 `ae1348cd86cc84add822ae0927b4774a79f3ebf1779323a3a1bb4599af5a38de`. |
| Live external-link probe | Not verified: PubMed returned HTTP 429 for 50 links during `--check-links`. The local content validator passed without live probes. |

The package remains partial, unreviewed and formative-only. Its eight homework packets remain optional and ungraded; human review, measured workload and operator release decisions remain open.

## Robotics & Mechatronics contact-control unit (2026-10-11)

Robotics advances to 0.4.7 with a bounded week-12 treatment of position tracking, force regulation and hybrid position-force assignment for compliant contact. The spring model uses $F=k\delta$: a 2.0 mm position command yields 0.80–1.20 N for 400–600 N/m, while a 1.00 N target at 400 N/m requires 2.5 mm indentation. The lesson and six formative items state that these quasistatic calculations do not establish transient behavior, loop stability or hardware safety limits. Four retrieval cards capture the controller distinctions and model boundary.

MIT OCW [2.12 Introduction to Robotics, Fall 2005 syllabus/calendar](https://ocw.mit.edu/courses/2-12-introduction-to-robotics-fall-2005/pages/syllabus/) is the direct undergraduate comparator: sessions L12 and L13 list hybrid position-force control and compliance/end-effector design. The local lesson uses original synthetic examples and does not reproduce course materials.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 407 lessons, 2,468 questions, 1,376 cards and 25 cases; zero errors and warnings. |
| Objective coverage | 1,064 objectives and 106 outcomes; no objectives without assessment mapping, practice or an outcome link. |
| Assessment-candidate inventory and report drift checks | Regenerated and both `--check` commands passed. |
| Public Robotics package digest | Version 0.4.7; 23 files, 309,392 bytes; archive SHA-256 `ea7ae53ba96f81b1ec45b5cbb4f38292434c4691e0dd62f2b3bf7a189b400351`; manifest SHA-256 `861564dd9f9095082690ccdc5c6f49ebc506e04524d78e6dde818dcd398c0f6c`. |
| JSON syntax | Changed manifests, banks, source map and registry parsed successfully. |
| Test suite | Not run, as requested. |

The package remains partial, unreviewed and formative-only. The next repository-wide instructional batch is Circuits & Instrumentation: RLC transients, resonance and impedance.

## Human Physiology for Engineers pressure-volume and pump-work unit (2026-10-11)

Physiology advances to 0.4.7 by extending its existing week-6 hemodynamics lesson rather than adding a week. The synthetic PV-loop treatment defines loop width as stroke volume and area magnitude as external stroke work. The baseline rectangle (EDV 120 mL, ESV 50 mL, 100 mmHg mean ejection pressure) gives 70 mL and 0.933 J/beat; the stipulated perturbation (ESV 70 mL, pressure 120 mmHg) gives 50 mL and 0.800 J/beat. Four numeric items and two conceptual items are paired with one new objective and four cards. The rectangular model is explicitly separated from a measured loop integral and clinical prediction.

MIT OCW [HST.542J Quantitative Physiology: Organ Transport Systems, Spring 2004 calendar](https://ocw.mit.edu/courses/hst-542j-quantitative-physiology-organ-transport-systems-spring-2004/pages/calendar/) is the undergraduate comparator; the calendar includes cardiovascular models and the heart as a pump. The new material is original and synthetic.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 407 lessons, 2,474 questions, 1,380 cards and 25 cases; zero errors and warnings. |
| Objective coverage | 1,065 objectives and 106 outcomes; no objectives without assessment mapping, practice or an outcome link. |
| Assessment-candidate inventory and report drift checks | Regenerated and both `--check` commands passed. |
| Public Physiology package digest | Version 0.4.7; 24 files, 310,157 bytes; archive SHA-256 `c9014927ebd7a9f6b7e739a6d00f3c850eae5daaa4cacddaae38543b1b4eb4b7`; manifest SHA-256 `47e8bd6f5d28f5a090c31c0fc2e1d09aaf0105e7095a55c7422383f4dddf62f9`. |
| JSON syntax | Changed manifests, banks, source map and registry parsed successfully. |
| Test suite | Not run, as requested. Existing numeric-key and snapshot version expectations were updated. |

The course remains partial, unreviewed and formative-only; the schedule remains unmeasured, the renal-clearance project is inactive, and the package makes no clinical claim.

## Circuits & Instrumentation second-order response unit (2026-10-11)

Circuits advances to 0.4.7 with an original second-order RLC lesson grouped with the existing RC lesson in week 8. The synthetic series-RLC example uses R=20 Ω, L=10 mH and C=10 µF: f₀≈503.3 Hz, α=1000 s⁻¹, ζ≈0.316, ωd=3000 rad/s, and Q≈1.581. At 250 Hz, X≈−47.95 Ω and impedance phase≈−67.4°, so current leads voltage. Nine public formative items (six numeric, three conceptual) and four cards link to the added lesson; the package stays at 14 proposed weeks. MIT OCW 6.002 Spring 2007 is the undergraduate comparator for second-order transients, damping, impedance, filters/Q and energy/power. The lesson gives explicit ideal-component and no-hardware-specification limits.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 408 lessons, 2,483 questions, 1,384 cards and 25 cases; zero errors or warnings. |
| Circuits package digest | Version 0.4.7; 23 files, 314,714 bytes; archive SHA-256 `41889f80bae543d4ff94d17d36b501a15a3addba8aad63baee6d41c574888799`; manifest SHA-256 `ffe89d5cc03bd095ed319fa95655722c1168bdbeea1d872d6d7223b94c0a7581`. |
| Test suite | Not run, as requested. |

The course remains partial, unreviewed and formative-only; topic alignment and package identity do not establish course equivalence, scientific review or hardware suitability.

## Calculus I Mean Value Theorem unit (2026-10-11)

Calculus I advances to 0.4.7 with one original lesson integrated into week 7 and its nine formative items/four retrieval cards. The theorem is stated with its exact continuity/differentiability hypotheses; examples include failure cases, Rolle's special case, a sign-change proof of root existence paired with MVT uniqueness, and the derivative-bound inequality |f(b)-f(a)|≤M|b-a|. Manual arithmetic checks give secant slope 4 and c=2 for x² on [1,3], Rolle point c=0 for x²−1 on [−1,1], and the bound 0.1 from M=1 over length 0.1. For p(x)=x³+x−1, p(0)=−1, p(1)=1 and p'(x)=3x²+1>0, so the IVT and MVT together establish exactly one root in (0,1). MIT OCW 18.01SC Fall 2010's undergraduate Unit 2 Part C contains sessions 34–35 on introducing and using MVT; the repository's direct source map records the bounded comparator. No MIT instructional asset was imported.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 409 lessons, 2,492 questions, 1,388 cards and 25 cases; zero errors or warnings. |
| Objective coverage | Regenerated: 1,069 objectives and 107 outcomes; no unmapped, unpractised or outcome-unlinked objectives. |
| Candidate inventory | Regenerated for current public candidates; the package remains partial and no candidate is activated. |
| Public Calculus I package digest | Version 0.4.7; 24 files, 288,867 bytes; archive SHA-256 5c660c5de34e369a3caeb1881ec0298f9ca6ca0afe3959e4a597543fece9147e; manifest SHA-256 3a9efcafe060b5e353834d5a55c58d06e217c7732ebd89eb87df4bbf6d385a39. |
| Test suite | Not run, as requested. |

The package remains partial, unreviewed and formative-only; the proposed schedule has no measured workload and the comparator does not establish equivalence.

## Probability, Biostatistics & Experimental Design Bayesian parameter unit (2026-10-11)

Statistics advances to 0.4.6 with an original finite-prior parameter lesson in week 13, paired with the existing event-rate/Bayes and p-value materials. For priors (0.5, 0.3, 0.2) on Bernoulli rates (0.2, 0.5, 0.8) and training data S,S, direct recalculation gives likelihoods (0.04, 0.25, 0.64), prior-weighted evidence 0.223, posterior (20/223, 75/223, 128/223), posterior H₃:H₁ odds 6.4, next-trial predictive success probability 0.645291, and probability 0.380538 of exactly one success in a separate two-trial holdout. Under a fixed null rate 0.5, the two-sided exact p-value for two successes in two trials is 0.50; the lesson distinguishes that conditional tail probability from the posterior. All data and parameter states are synthetic.

MIT OCW 18.05 Spring 2022 is the direct undergraduate comparator: its official calendar places likelihood/MLE in Class 10, discrete Bayesian updating and predictive probabilities in Classes 11–12, and comparison of Bayes with NHST in Class 20. The local addition covers a narrower finite-prior exercise; continuous priors and beta conjugacy remain out of scope.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 410 lessons, 2,501 questions, 1,392 cards and 25 cases; zero errors or warnings. |
| Objective coverage | Regenerated: 1,072 objectives and 108 outcomes; no unmapped, unpractised or outcome-unlinked objectives. |
| Candidate inventory | Regenerated for current public candidates; no candidate was activated. |
| Public Statistics package digest | Version 0.4.6; 25 files, 358,151 bytes; archive SHA-256 1792fc3ede2767550400d1a98b820347d34db94c200622d552b55ab796433f22; manifest SHA-256 60315cbd46deb19680ba33d9ecfcda80988546f255bac77383f5a5c7fdc58c0f. |
| Test suite | Not run, as requested. |

The package remains partial, unreviewed and formative-only; the schedule has no measured workload and the comparator does not establish equivalence.

## Bioreactors sterile-boundary reasoning (2026-10-11)

Bioreactors & Tissue Culture Engineering advances to 0.4.8 with conceptual contamination-route mapping and sterility-evidence limits grouped into the existing Week 12 monitoring lesson. The synthetic example computes 1.2×10⁶ × 10⁻⁴ = 120 modeled survivors. It explicitly does not treat the calculation or no-detection in one sample as proof of whole-batch sterility or process validation. The question bank adds one numeric and two distinct single-choice checks; three cards add retrieval support.

MIT OCW 10.442 Spring 2005's official calendar places growth/product stoichiometry in sessions 11–12 and media/air sterilization in session 22. This link-only comparison supports the bounded course-level gap; no source asset or prose was imported. The local package remains focused on animal-cell/tissue-culture applications, with broader microbial/enzyme-engineering scope deferred.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 424 lessons, 2,647 questions, 1,464 cards and 25 cases; zero errors or warnings. |
| Objective coverage | Regenerated: 1,116 objectives and 114 outcomes; no unmapped, unpractised or outcome-unlinked objectives. |
| Candidate inventory | Regenerated for current public candidates; no candidate was activated. |
| Public Bioreactors package digest | Version 0.4.8; 23 files, 314,294 bytes; archive SHA-256 `5001aa825241e345df896ba4f744d5b6500b56d5c761a500342a0fbe44faff84`; manifest SHA-256 `29b0d23d5673ce822d903d77e7d2689599dc9bebc4802427a00a51648a14fa11`. |
| Test suite | Not run, as requested. |

The course remains partial, unreviewed and formative-only; this comparison does not establish equivalence or validate a real sterilization process.

## Differential Equations Fourier response (2026-10-11)

Differential Equations advances to 0.4.0. The new Week 3 material derives the odd-harmonic series of an ideal bipolar square wave and applies the first-order transfer gain and phase separately at each nω. Direct calculation gives coefficient 4/(3π) = 0.424413, fundamental output amplitude 0.548602 mM, third-harmonic gain 0.157177 and output amplitude 0.066708 mM for the displayed synthetic case. It records the midpoint value at jumps and finite partial-sum overshoot. This is one periodic-forcing application of MIT OCW 18.03SC Unit III; it does not cover the full Fourier/convolution/impulse/transfer-function scope.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 424 lessons, 2,651 questions, 1,467 cards and 25 cases; zero errors or warnings. |
| Objective coverage | Regenerated: 1,117 objectives and 114 outcomes; no unmapped, unpractised or outcome-unlinked objectives. |
| Candidate inventory | Regenerated for current public candidates; no candidate was activated. |
| Public Differential Equations package digest | Version 0.4.0; 23 files, 330,230 bytes; archive SHA-256 `19882a7fa809e6cde6f4d1428a33e36451e24c2433e3c574560dfbdc3b78e224`; manifest SHA-256 `c5f9e7ea93bdb4cd3b8dc8eec2a59f4b0638328be0e316056fa90010ff11a76a`. |
| Test suite | Not run, as requested. |

The course remains partial, unreviewed and formative-only; workload is unmeasured and this link-only comparator does not establish equivalence.

## Statics & Mechanics of Materials axial compatibility (2026-10-11)

Statics & Mechanics of Materials advances to 0.4.7. The new Week 3 section combines equilibrium, shared displacement at rigid plates and the individual bars' elastic force–deformation relations. For A=100 mm², L=400 mm, E₁=200 GPa, E₂=100 GPa and P=30 kN, stiffnesses are 50 and 25 kN/mm, common extension is 0.4 mm, forces are 20 and 10 kN, and nominal stresses are 200 and 100 MPa. Two numeric keys are independently recomputed in the existing numeric-authoring map. MIT OCW 2.001 syllabus, readings and lecture notes substantiate the comparator scope; the addition remains a limited axial example.

| Actual command/check | Result |
| --- | --- |
| Content validator | Passed: 25 courses, 424 lessons, 2,654 questions, 1,470 cards and 25 cases; zero errors or warnings. |
| Objective coverage | Regenerated: 1,118 objectives and 114 outcomes; no unmapped, unpractised or outcome-unlinked objectives. |
| Candidate inventory | Regenerated for current public candidates; no candidate was activated. |
| Public Statics & Materials package digest | Version 0.4.7; 24 files, 338,262 bytes; archive SHA-256 `87cb69a9f7a90b854cc531bb891d85dc8b9198cdf9efb449b3dd41d2fb29b2f4`; manifest SHA-256 `629d776431bcbed5480746a4136bcc5e0fa94edc7769e12bd0a4fe0568f05b3c`. |
| Test suite | Not run, as requested. |

The course remains partial, unreviewed and formative-only; the example is not an engineering design or safety basis.

## Suite repair, consistency fixes, Organic Chemistry SNAr and Linear Algebra determinants (2026-10-13)

Organic Chemistry I advances to 0.4.9. The aromaticity lesson adds an SNAr addition–elimination strand covering Meisenheimer-complex charge placement, ortho/para versus meta activation, the activated-ring leaving-group trend and the nitro group's opposite EAS/SNAr roles. It adds one objective, seven items and three cards. MIT OCW 5.12 Spring 2005 pairs EAS and SNAr in week 11, and OpenStax Organic Chemistry 16.6 is registered as a link-only reference. Linear Algebra advances to 0.3.7 with an original determinants reading grouped with eigenvalues in week 7, as MIT OCW 18.06SC Fall 2011 Unit II orders them. It adds three objectives, eleven items and four cards; every key is recomputed by exact cofactor expansion. The suite repair and the other package corrections are summarized in the progress review.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 425 lessons, 2,672 questions, 1,477 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,076 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 5,668 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,564 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. The rewritten CI smoke step is therefore unexecuted. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-151345/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Bioreactors fed-batch, Signals & Control Routh–Hurwitz/root locus and Physiology passive cable (2026-10-13)

- **Bioreactors 0.4.9: fed-batch reading.** Grouped with continuous culture in week 4; three objectives, ten items and four cards. Feed-schedule keys are recomputed by integrating the fed-batch balances with RK4, and the working-volume time is recomputed by bisection rather than from the closed form. MIT OCW 10.442 Spring 2005 is the link-only comparator.
- **Signals & Control 0.4.8: Routh–Hurwitz and root locus.** Grouped with the week-8 feedback lesson; three objectives, eleven items and four cards. The keys for the stability limit, crossing frequency, breakaway gain and ζ = 0.5 gain are recomputed from cubic roots, by bisecting on stability and on the dominant damping ratio, not from the Routh array. MIT OCW 2.004 Spring 2008 lectures 25–29 are the comparator.
- **Physiology 0.4.8: passive membrane and cable properties.** Grouped with the week-4 membrane-potential lesson; three objectives, ten items and four cards. Length-constant decay keys are recomputed with a finite-difference ladder network solved by the Thomas algorithm, and time-constant keys by time-stepping the RC equation. MIT OCW 6.021J Fall 2004 is registered as a link-only comparator.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 428 lessons, 2,703 questions, 1,489 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,098 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 5,730 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,570 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-163442/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Circuits & Instrumentation op-amp signal operations (2026-10-13)

Circuits & Instrumentation advances to 0.4.8 with an original reading grouped with the week-5 feedback lesson; it adds three objectives, thirteen items (ten numeric, three choice) and four cards, with no week added. Each new key is recomputed by a separate method rather than the lesson formula: summing and filter keys from a finite-gain (10⁹) inverting-node solution with complex impedances, the integrator ramp by quadrature of the input current, the drift time and corner frequencies by bisection on the half-power point, Sallen–Key f₀ and Q from a nodal solution at the −90° phase crossing, and the gain-bandwidth estimate from a single-pole open-loop model. A further test recomputes ten values stated in the reading. The backend unit table gains `kHz`, with conversion and case-sensitivity tests. MIT OCW 6.002 Spring 2007 remains the link-only comparator.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 429 lessons, 2,716 questions, 1,493 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no Circuits file is in a candidate digest and no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,111 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 5,758 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,572 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-165655/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Calculus II trigonometric integration (2026-10-13)

Calculus II advances to 0.4.8 with an original reading grouped with the week-2 methods lesson; it adds three objectives, eleven items (eight numeric, three choice) and four cards, with no week added. The eight new keys are recomputed by Simpson quadrature of the original integrands, not from antiderivatives. The secant item's integrable endpoint singularity is removed with the algebraic change x = 3 + t² rather than a trigonometric substitution. A further test checks ten values stated in the reading. A hard-coded practice-item count in the outcome-mapping regression was replaced with a count derived from the bank.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 430 lessons, 2,727 questions, 1,497 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no Calculus II file is in a candidate digest and no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,122 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 5,780 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,574 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-171114/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Robotics computed-torque control (2026-10-13)

Robotics advances to 0.4.8 with an original reading grouped with the week-9 dynamics lesson. It adds three objectives, eleven items (eight numeric, three choice) and four cards, with no week added. The eight new keys are recomputed from Newton–Euler point-mass dynamics rather than the Lagrangian M, h and G the reading uses, and the computed-torque mismatch residual comes from a closed-loop RK4 simulation run to rest. A further test checks the values stated in the reading, including the exact PD sag and the absence of steady error with an exact model. The first verify run (`20261013-172530`) was interrupted during root pytest when the session ended. Every step that finished had passed. The rerun below supersedes it.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 431 lessons, 2,738 questions, 1,501 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,133 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 5,802 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,576 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-193502/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Titration curves, least squares and held variables, why aging evolves (2026-10-13)

General Chemistry II advances to 0.4.8, Calculus III to 0.4.9 and Geroscience to 0.5.9. Each adds three objectives, eleven items (eight numeric, three choice) and four cards to an existing week. The recalculations use different methods from the readings:

- **General Chemistry II:** every pH comes from an exact charge-balance root at each titrant volume, not from the region-by-region shortcuts. Equivalence volumes are located as the steepest point of the computed curve.
- **Calculus III:** fits use centred (mean-deviation) slope formulas instead of the normal equations, and Hessians are taken by finite differences. Constrained derivatives come from explicit substitution and numerical differentiation instead of differentials. A direct exponential fit uses golden-section search.
- **Geroscience:** survival is integrated with Euler steps and selection strength with the trapezoid rule, instead of the closed exponential forms. Offspring totals follow a cohort year by year instead of using geometric series. The break-even boost is found by bisection. This is the first Geroscience recalculation file. Its tests also check that the three new references are link-only DOI records.

Each package also has a test of the values stated in its reading. Snapshot pins and one Geroscience dossier version pin were updated with each release.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 434 lessons, 2,771 questions, 1,513 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| `refcheck.py` (citation-check skill) on the three new DOIs | 3 resolved, 0 not found, 0 flagged; a fourth candidate DOI resolved to an unrelated paper and was not used. |
| Root pytest (`python -m pytest tests`) | 3,168 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 5,868 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,583 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-195604/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Impulse response and convolution, magnetic-field sources, multiaxial strain and pressure vessels (2026-10-13)

Differential Equations advances to 0.4.1, Physics II: E&M to 0.4.8 and Statics & Materials to 0.4.8. Each adds three objectives, eleven items (eight numeric, three choice) and four cards to an existing week. The recalculations use different methods from the readings:

- **Differential Equations:** a new file computes impulse responses by RK4 after the velocity jump and convolutions by Simpson quadrature. Gains and phase lags come from a real 2×2 solve for the particular-solution coefficients. The shared registry in `test_ai_assisted_checks.py` also checks the keys from closed forms.
- **Physics II: E&M:** fields are found by numerical Biot–Savart summation over discretized paths, and Ampère's law is applied with the enclosed current integrated over the cross-section. Torque is summed as r × (I dl × B) around a tilted loop, and turning work integrates that torque.
- **Statics & Materials:** a new file solves the isotropic stiffness relation by Gaussian elimination and finds thermal stresses by bisection on length compatibility. Vessel stresses come from integrating the pressure over a cut. The shared registry checks the keys from closed forms.

Each package also has a test of the values stated in its reading.

The first verify run (`20261013-201355`) failed one test. `test_every_differential_equations_numeric_item_is_recalculated` requires every Differential Equations key in the shared registry, and the new keys had been checked only in their own file. The keys were added to the registry, as were the Statics keys before that batch was applied. The rerun below covers all three packages.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 437 lessons, 2,804 questions, 1,525 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,221 passed, 1 skipped (first run: 1 failed, 3,191 passed, as described above). |
| Backend pytest (`cd backend && python -m pytest`) | 5,934 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,591 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-203302/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Universal gravitation and orbits, valence-bond theory and hybridization (2026-10-13)

Physics I: Mechanics advances to 0.4.9 and General Chemistry I to 0.4.10. Each adds three objectives, eleven items (eight numeric, three choice) and four cards to an existing week. The recalculations use different methods from the readings:

- **Mechanics:** keys are checked against RK4-simulated orbits. The circular speed is found by bisection so that a simulated quarter turn keeps its radius. Potential energy comes from integrating the force to infinity, and field strength from differentiating that potential numerically.
- **General Chemistry I:** explicit hybrid coefficient vectors are built and checked for orthonormality. The bent-molecule s-character comes from bisection on orthogonality, with lone-pair hybrids completed by Gram–Schmidt, and σ/π counts come from explicit bond lists.

Each package also has a test of the values stated in its reading.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 439 lessons, 2,826 questions, 1,533 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,243 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 5,978 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,595 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-205317/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Cytoskeletal filament mechanics, inverse/exponential/logarithmic derivatives (2026-10-13)

Cellular Biomechanics advances to 0.3.9 and Calculus I to 0.4.9. Each adds three objectives, eleven items (eight numeric, three choice) and four cards to an existing week. The recalculations use different methods from the readings:

- **Cellular Biomechanics:** a new file computes ⟨R²⟩ by integrating the tangent correlation along the contour. Buckling loads and lengths come from a shooting method on κy″ + Fy = 0, and the worm-like-chain force from inverting the extension. The shared registry checks the closed forms.
- **Calculus I:** the recalculation file uses bisection-solved inverse values instead of 1/f′ and centred numerical derivatives instead of the derivative formulas. (1 + 1/n)ⁿ is computed by repeated multiplication.

Each package also has a test of the values stated in its reading.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 441 lessons, 2,848 questions, 1,541 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,274 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 6,022 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,600 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-211256/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Controlled-release kinetics (2026-10-13)

Biomaterials advances to 0.3.10 with an original reading grouped with the week-6 release lesson. It adds three objectives, eleven items (eight numeric, three choice) and four cards. A new file checks the eight new keys by different methods:

- membrane flux summed over time;
- Higuchi release from a time-to-release integral solved by bisection;
- slab diffusivity by inverting the exact Crank series;
- first-order release by RK4;
- the release exponent by a log–log least-squares slope.

The shared registry checks the closed forms, and a further test checks the values stated in the reading.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 442 lessons, 2,859 questions, 1,545 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,294 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 6,044 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,603 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-212805/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Steady-flow energy balances (2026-10-13)

Thermodynamics & Transport advances to 0.4.9 with an original reading grouped with the week-10 perfusion lesson. It adds three objectives, eleven items (eight numeric, three choice) and four cards. A new file checks the eight new keys by different methods:

- a stepped free-fall calculation for efflux speed;
- integration of dP = −ρv dv across a constriction;
- integration of the parabolic profile, with bisection for laminar losses;
- bisection on a hydrostatic integral for feed height.

The shared registry checks the closed forms, and a further test checks the values stated in the reading.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 443 lessons, 2,870 questions, 1,549 cards and 25 cases; zero errors or warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| Root pytest (`python -m pytest tests`) | 3,314 passed, 1 skipped. |
| Backend pytest (`cd backend && python -m pytest`) | 6,066 passed, 2 skipped. |
| Legacy node tests | 7 passed. |
| `tools/check_security.py` (source and bundle) | 1,606 files, 0 findings. |
| Ruff | Clean. |
| Frontend lint, unit tests and build (Linux copy) | Passed; 73 unit tests in 17 files. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261013-214249/`. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## 2026-10-14: LF line-ending normalization and hash re-pin

Before committing, 352 working-copy text files had CRLF line endings, while `.gitattributes` (`* text=auto eol=lf`) stores LF. Package, manifest and candidate prerequisite hashes had been pinned against the CRLF bytes, so a fresh checkout would not have matched them. The files were converted to LF with no other content change. Current pins were then re-pinned only where the old value exactly matched the CRLF bytes of the same content: the review snapshots, candidate prerequisite hashes, the Cell Biology review-evidence register, and the regenerated candidate and Cell Biology recalculation reports. Archived versioned reports, history logs and the already-stale Biochemistry review register were left unchanged.

| Actual command/check | Result |
| --- | --- |
| Root pytest after conversion, before re-pin | 39 failed (hash pins only), 3,275 passed, 1 skipped. |
| Full verify after re-pin | Content, legacy (7), security (1,606 files, 0 findings), ruff passed; root 3,314 passed, 1 skipped; backend 6,066 passed, 2 skipped; frontend 73 unit tests passed. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file. |

Logs in `~/.cache/courselab-verify/20261014-002431/`. All packages remain partial, unreviewed and formative-only.

## 2026-10-17: CI repair after the pushed commit

GitHub run `39038660056` for `0362e21` failed in two jobs. In `content-backend`, eleven tests in the cell-biology digest, snapshot, recalculation and review-register checks expected the clean package digest `5761c217…`, while the pins held `03d27ea4…`. The local tree contained an ignored bytecode cache, `content/courses/cell-biology/assessment-specs/__pycache__/generate_project_dataset.cpython-312.pyc`. `ContentRepository.package_files` hashes every file in a package directory, so the cache changed the local digest; CI's clean checkout had no cache. In `frontend-e2e`, two Case Studio tests failed. Their screenshots were written to `../.local/`, which CI does not have, and the 390 px narrow-screen check found a horizontal overflow (scroll width 445 px) because the five course tabs in `.tabs` did not wrap.

Repairs: the stray cache was removed. `package_files` now skips `__pycache__` directories and `.pyc` files, so interpreter caches cannot change a published digest, and `test_package_archive_ignores_interpreter_caches` covers this. The cell-biology digest was repinned in the snapshot (121 files, 2,076,971 bytes), the numeric and table recalculation reports, and the review register; the old value appeared only in those four files. `.tabs` now wraps. The Case Studio screenshots go to `frontend/test-results/`, which CI uploads as the browser-validation artifact.

| Actual command/check | Result |
| --- | --- |
| Clean export of the working tree (tracked and untracked files, excluding `.local/`), root pytest | 3,314 passed, 1 skipped. |
| Clean export, `tools/validate_content.py` | PASS: 25 courses, 443 lessons, 2,870 questions, 1,549 cards, 25 cases; 0 errors. |
| Full verify, run `20261017-142735` | Content, legacy (7), security (1,606 files, 0 findings) and ruff passed; root 3,314 passed, 1 skipped; backend 6,067 passed, 2 skipped; frontend lint, 73 unit tests and build passed. |
| Local Chromium layout check, built frontend with fixtures generated from the backend's public course DTO | Before the fix: scroll width 445 px at 390 px. After: scroll width equal to the viewport at 320, 390 and 1,280 px, with no overflowing element. This checks layout only. |
| Not run | Docker Compose stack, the full Playwright suite (it needs the API stack) and the production compose file. |

To run the browser check, Chromium's system libraries were installed in the dev container with `sudo npx playwright install-deps chromium`.

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container; logs in `~/.cache/courselab-verify/20261017-142735/`. All packages remain partial, unreviewed and formative-only.

## Ordered tetrads and centromere distance (2026-10-17)

Genetics advances to 0.5.8 with an original reading in week 5, next to the three-point mapping and unordered-tetrad lesson. The MIT OCW 7.03 (Fall 2004) calendar lists L7 "Three-factor Crosses" and L8 "Tetrad Analysis" consecutively (titles only; checked 2026-10-17). The package keeps one module per lesson, so the reading is its own module, `genetics-module-18`, and `duration.weeks` schedules it in week 5 with its practice assessment. It adds four objectives, twelve items (six numeric, six choice), five cards and a practice assessment. The mapping lesson's statement that ordered tetrads lie outside the course now points to the new reading.

`tests/content/test_genetics_ordered_tetrad_recalculations.py` recomputes the six numeric keys with exact fractions from the counts in each prompt. It also compares the rule-of-three bound with the exact binomial bound 1 − 0.05^(1/600), checks that each choice key points at the only option carrying its distinguishing phrase, and checks the assessment, lesson and card links. The repository-wide Genetics table in `test_ai_assisted_checks.py` now includes the six keys, so its every-numeric-item check still covers the whole bank.

The scratch draft was corrected before it entered the package. Budding-yeast asci are unordered, so the ordered examples use *Neurospora* and *Sordaria*. A second-division ascus shows at least one exchange, not exactly one. Two-strand and four-strand double exchanges restore a first-division pattern, while three-strand doubles keep second-division segregation. Two expected-count prompts now state the single-exchange model. The reading also states the two-thirds ceiling (about 33 cM) under random, independent exchanges, and notes that Haldane's two-point correction from the mapping lesson is not the correction for second-division counts.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 444 lessons, 2,882 questions, 1,554 cards and 25 cases; 0 errors. Its first run rejected the reading as a second lesson in module 7 (one source-map identity per module), which led to the separate module. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. Genetics: 19 lessons, 55 objectives, 108 items, 71 cards; no objective without an assessment mapping or practice item. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| `claims_scan.py --repo uniStemCourseSimulators` on the eight changed package and snapshot files | 0 findings. |
| Full verify, run `20261017-164542` | Content, legacy (7), security (1,609 files, 0 findings) and ruff passed; backend 6,091 passed, 2 skipped (the 24 added cases are `test_authored_items.py` grading each of the twelve new keys for full credit and a deliberately wrong answer for none); frontend lint, 73 unit tests in 17 files and build passed. Root: 1 failed, 3,325 passed, 1 skipped. The failure was `test_genetics_schedule_places_every_lesson_once_and_stays_partial`, which hard-coded 18 Genetics lessons; it now expects 19. |
| Root pytest rerun after that fix | 3,326 passed, 1 skipped: twelve more than before the batch, from the six new-file tests and the six new entries in the repository-wide Genetics table. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; these need the host or CI. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, then `python -m pytest tests -q -p no:cacheprovider` for the rerun; Python 3.12.3 and Node 24 in the dev container. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## 2026-10-17: CI result for the repair and the Genetics batch

The CI repair (`cd31475`) and the Genetics batch (`9f23ad6`) were pushed as a fast-forward of `main`. Before the push, a `git archive` export of `9f23ad6` passed the content validator, 477 targeted root tests (cell biology, genetics, snapshots and review registers) and the full backend suite (6,091 passed, 2 skipped). GitHub Actions run `39054270414` then passed both jobs: `content-backend` in 7 min 23 s and `frontend-e2e`. The `frontend-e2e` job runs the Docker Compose stack and the Playwright suite on the CI runner, which this container cannot; it is the first evidence that the Case Studio layout and screenshot-path repairs work there. The run used the workflow file from `0362e21`, because the local commit extending the workflow needs the `workflow` token scope and was not pushed.

## Impedance models (2026-10-17)

Signals & Control advances to 0.4.9 with an original reading grouped with the week-5 second-order lesson. The MIT OCW 2.004 (Spring 2008) calendar gives component modeling lectures 5–16 (checked 2026-10-17); the reading is a compact version of the electrical and translational impedance lectures 5–7 and 9–10, plus thermal elements for the course's incubator. The calendar lists no separate compensator-design lecture, so the audit row now names the modeling block as the gap this reading addresses. The reading is its own module, `signals-control-module-16`, scheduled in week 5 after the second-order lesson, whose response measures it uses. It adds three objectives, twelve items (eight numeric, four choice), four cards and a practice assessment. The second-order lesson's limits now point to it.

`tests/content/test_signals_control_impedance_modeling_recalculations.py` recomputes the eight numeric keys without using the closed forms in their feedback:

- time constants by RK4 simulation of the step response, timed to 1 − 1/e of the known final value;
- the corner frequency by bisection on |H(j2πf)| = 1/√2;
- natural frequencies and damping ratios from the complex poles of the derived characteristic polynomial;
- the static deflection by simulating the mass–spring–damper to rest;
- the thermal capacitance by bisection on a simulated heater-step response.

The same helpers check every number the reading states, the worked example's 37.2% overshoot against a simulated step, and a three-node heater–chamber–sensor chain that rises without overshoot. The repository-wide Signals & Control table in `test_ai_assisted_checks.py` adds the eight keys as closed forms, so its every-numeric-item check still covers the bank.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 445 lessons, 2,894 questions, 1,558 cards and 25 cases; 0 errors. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. Signals & Control: 17 lessons, 47 objectives, 122 items, 60 cards; no objective without an assessment mapping or practice item. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| `claims_scan.py --repo uniStemCourseSimulators` on the nine changed package and snapshot files | 0 findings. |
| Targeted pytest (new file, snapshot, AI-assisted checks, schedule tests and the five Signals & Control regressions) | 1,434 passed. |
| Full verify, run `20261017-174617` | Content, legacy (7), security (1,612 files, 0 findings) and ruff passed; root 3,341 passed, 1 skipped (fifteen more: seven new-file tests and eight table entries); backend 6,115 passed, 2 skipped (24 more: `test_authored_items.py` grades each of the twelve new keys for full credit and a deliberately wrong answer for none); frontend lint, 73 unit tests in 17 files and build passed. |
| Registry update after the run | The 2.004 calendar entry in `content/sources/registry.json` now records the 2026-10-17 recheck (metadata only); `tools/validate_content.py` passed again. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file locally; CI runs the first two on push. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Hodgkin–Huxley action potential (2026-10-17)

Physiology advances to 0.4.9 with an original reading grouped with the week-3 excitable-cells lesson. The MIT OCW 6.021J (Fall 2004) calendar gives the Hodgkin–Huxley model lectures 20–25 and channel gating lectures 32–35 (checked 2026-10-17). The reading is its own module, `physiology-module-16`. It adds three objectives, twelve items (eight numeric, four choice), four cards and a practice assessment, and the excitable-cells lesson now points to it.

The reading's spike, threshold and refractory numbers were computed for it by simulating the classic model (squid axon, 6.3 °C, −65 mV rest; fixed-step RK4), and they agree at 0.002 ms and 0.01 ms steps. `tests/content/test_physiology_hodgkin_huxley_recalculations.py` repeats that work at 0.01 ms:

- the numeric keys by integrating each gating equation rather than using the closed forms;
- the stated rest and clamp kinetics from the rate functions, and the worked example from an integrated gate;
- the spike peak, timing, width, undershoot and gate values at the peak;
- the 1-ms and 0.1-ms thresholds, with a pulse 2% below each failing and 2% above firing;
- the two refractory intervals, with a second pulse failing 0.5 ms early and firing at the stated delay.

The simulation corrected one draft figure: n at the peak is 0.515, which rounds to 0.51, not 0.52. The repository-wide Physiology table in `test_ai_assisted_checks.py` adds the eight keys as closed forms.

Hodgkin and Huxley (1952) is a new link-only registry entry. Its DOI and PubMed record (12991237) were resolved with the citation-check script on 2026-10-17, and the title matches the claim it supports. The PMC copy is page images only, and both PMC and Europe PMC refused the PDF download, so the classic parameter values were not checked against the paper; the reading, source map and registry say so. The first citation scan misread the DOI because the link was wrapped in parentheses, so the sentence was rewritten and the scan resolves it.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 446 lessons, 2,906 questions, 1,562 cards and 25 cases; 0 errors. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. Physiology: 17 lessons, 48 objectives, 114 items, 64 cards; no objective without an assessment mapping or practice item. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated. |
| `claims_scan.py --repo uniStemCourseSimulators` on the nine changed package, registry and snapshot files | 0 findings. |
| `refcheck.py --scan` on the new reading | 1 identifier, resolves (after the sentence rewrite). |
| Targeted pytest (new file, snapshot, AI-assisted checks, schedule tests and the six Physiology regressions) | 1,438 passed before the citation rewrite; the snapshot and new-file tests passed again after it (7 passed). |
| Full verify, run `20261017-180811` | Content, legacy (7), security (1,615 files, 0 findings) and ruff passed; root 3,355 passed, 1 skipped (fourteen more: six new-file tests and eight table entries); backend 6,139 passed, 2 skipped (24 more: `test_authored_items.py` grades each of the twelve new keys for full credit and a deliberately wrong answer for none); frontend lint, 73 unit tests in 17 files and build passed. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file locally; CI runs the first two on push. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container. All packages remain partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Cell Biology final review and integrative project for learners (2026-10-19)

Cell Biology advances to 0.62.0 so that every component of its proposed 14-week plan can be worked through as ungraded practice. Week 14 gains `modules/13d-course-synthesis-and-final-review.md` and a 25-question, 53-point cumulative final review practice set; week 10 gains `assignments/integrative-project-guide.md`, an eight-culture rehearsal dataset with four open practice items (18 points), and five integrative-project milestones added to `rubrics/case-studio.json` as zero-point self-checks, with a `project` self-assessment record scheduled in week 14. Two new synthetic datasets are learner resources (`assignments/final-review-feedback-variant-clones.csv`, `assignments/project-rehearsal-cultures.csv`), and the existing project culture table becomes one. The syllabus restores its week-8 links to the two synthesis readings, and the schedule now links self-assessed project activities to the Case studio. Inactive candidates, their files and their external keys are unchanged.

Key checks before publication:

- A self-check script graded all 17 new items with the backend grader: authored keys earn full credit; deliberately wrong responses, wrong units, swapped fields, near misses and malformed text earn the stated partial or zero scores. It caught one defect, an unsupported `eq` unit on the rehearsal upload's RNA cells, which was fixed before the items were applied.
- An option-length audit found the correct option conspicuously longest in 17 of 22 choice fields; the options were rewritten so the distractors are specific, plausible misconceptions of similar length.
- `tests/content/test_cell_biology_final_review_and_project.py` (9 tests) recomputes every new key from the two CSV files and stated prompt values: the steady-state prediction from half-life and synthesis, trapezoidal pERK areas (mean of per-clone areas equals the area of the mean trajectory), EdU absolute and relative changes, penetrance with a noncarrier branch, the gel modulus, the rehearsal transformations, the pooled versus equal-culture marker percentage and the guide's worked example. It also checks the reading's clone-mean table against the CSV, catalogued misconception IDs, the separation of the rehearsal data from the candidate forms, and that the milestones remain zero-point self-checks.
- The numeric-key and table-reconciliation tools now cover 23 numeric items and 133 table checks across 14 upload items; the table test recomputes the rehearsal transformations with exact fractions.
- The 0.61.1 snapshot, review-evidence index, numeric and table reports and response-mode audit were archived with `-0.61.1` names before regeneration. The review-evidence index was regenerated from the current packet after confirming it held no review records; a 0.62.0 workload-pilot protocol repins the prospective protocol to the new digest and lists the new activities.

| Actual command/check | Result |
| --- | --- |
| `tools/validate_content.py` | Passed: 25 courses, 448 lessons, 2,923 questions, 1,569 cards and 30 cases; 0 errors and 0 warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. Cell Biology: 45 lessons, 69 objectives, 183 items, 96 cards. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated or changed. |
| `tools/course_review_evidence.py --course-id cell-biology --check docs/reviews/cell-biology-review-evidence.json` | Passed: 15 candidates, 142 unresolved candidate-gate instances, 0 review records, release not authorized. |
| `claims_scan.py --repo uniStemCourseSimulators` | 0 findings. |
| Full verify, `verify.sh --frontend` (log `cb-verify-2`) | Content, legacy (7), security (1,628 files including the built bundle, 0 findings) and ruff passed; root 3,364 passed, 1 skipped (nine more, from the new test file); frontend lint, 74 unit tests in 17 files and build passed. The backend step reported one failure: `test_case_studio.py` still pinned exactly one case per course. |
| Backend rerun after updating that pin to allow the five Cell Biology milestones | 6,174 passed, 2 skipped (35 more than before: 34 from grading the 17 new keys correct and wrong, and one new content-repository route test). |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; CI runs the first two on push. No browser walkthrough of the new pages was performed here. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container. These checks were run by an AI coding agent (Claude Code) at the owner's request. The package remains partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Biochemistry homework, reviews and project for learners (2026-10-19)

Biochemistry advances to 0.5.0 so that every component of its proposed 14-week plan can be worked through as ungraded practice. Eight packets in `assignments/` with eight synthetic CSV datasets and eight `homework` practice sets (41 items, 151 points) are scheduled in weeks 2, 4, 6, 7, 9, 10, 12 and 14. Week 7 gains `modules/26-midterm-synthesis-proteins-binding-and-enzyme-evidence.md` and an 18-question, 30-point midterm review practice set; week 14 gains `modules/27-final-synthesis-energy-carbon-redox-and-control.md` and a 28-question, 42-point cumulative final review practice set. Week 5 gains `assignments/protein-state-project-guide.md`, a one-row rehearsal condition and a four-item, 12-point rehearsal practice set; five project milestones are zero-point self-checks in `rubrics/case-studio.json`, with a `project` self-assessment record in week 8. Ten CSV files become learner resources, including the existing project condition table, and 33 retrieval cards are added. Inactive candidates, their prerequisite readings and their private drafts are unchanged.

Key checks before publication:

- A self-check script graded all 60 new items with the backend grader: authored keys earn full credit and deliberately wrong responses earn zero. Another 62 cases (near misses, too few significant figures, alternative unit forms, shortcut answers such as treating total ligand as free, partially correct multiple selections) earn the stated partial or zero scores.
- An option-length audit found the correct option conspicuously longest in 56 choice fields. The options were rewritten so the distractors are specific misconceptions of similar length, and one distractor that a 5% error could have made defensible was replaced. Two fields still flag on length only because they share a three-level classification list whose correct answer differs by statement.
- `tests/content/test_biochemistry_open_practice_routes.py` (13 tests) recomputes from the CSVs every new upload check and every new numeric key. This includes a pure-Python nonlinear least-squares refit of the Homework 4 replicate means (control Vmax 60.18 μM/min and Km 4.026 μM; α = 2.975 and K_I = 3.04 μM, against 3.96 μM from the reciprocal fits), the synthesis readings' worked numbers and the project guide's worked example. It also checks that every link in the delivered lessons resolves to a lesson route or a pinned learner resource, and that the guide and rehearsal items contain none of the condition A or B results computed from the project table.
- Candidate tests now exclude the open-practice lessons when comparing candidate coverage with the schedule, and the snapshot and project-candidate tests require candidates to stay bound to a released version (0.4.85) rather than the current one. Two regression tests that pinned the version prefix `0.4.` now require at least 0.4.0; a Biochemistry lesson-count pin moves from 27 to 38; the Biochemistry numeric recalculation table gains the four new numeric-type items; and the case-count pins allow the five milestones.
- The manifest's numeric-answer limitation was stale (81 answers and no significant-figure checks, where the bank had 86 numeric items, three of which check figures). It now states 90 numeric-type answers (56 unit-required, 34 unit-optional, 3 checking figures), 63 data-interpretation numeric fields that check figures and 9 CSV-upload items.
- The 0.4.85 snapshot is archived as `docs/BIOCHEMISTRY_REVIEW_SNAPSHOT-0.4.85.md`. The review-evidence register and the workload protocol were regenerated as empty 0.5.0 records after confirming they held no review records; their 0.4.84 versions remain archived. The response-format inventory and reviewer checklist remain pinned to 0.4.84.

| Actual command/check | Result |
| --- | --- |
| Self-check script over the ten item modules (backend grader) | 60 items and 62 extra cases passed. |
| `tools/validate_content.py` | Passed: 25 courses, 459 lessons, 2,983 questions, 1,602 cards and 35 cases; 0 errors and 0 warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. Biochemistry: 38 lessons, 75 objectives, 249 items, 146 cards; no unmapped objective or outcome. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration; no candidate was activated or changed. |
| `tools/course_review_evidence.py --course-id biochemistry --check docs/reviews/biochemistry-review-evidence.json` | Passed: 11 candidates, 88 unresolved candidate-gate instances, 0 review records, release not authorized. |
| `claims_scan.py --repo uniStemCourseSimulators` | 0 findings. |
| Full verify, `verify.sh --frontend` (log `bio-verify-1`) | Content, legacy (7), security (1,650 files including the built bundle, 0 findings), ruff, backend (6,294 passed, 2 skipped) and frontend lint, 74 unit tests in 17 files and build passed. Root pytest: 3,375 passed, 1 skipped and 2 failed: a Biochemistry lesson-count pin (27) and the Biochemistry numeric-item enumeration, both updated as described above. |
| Root pytest rerun after those updates | 3,381 passed, 1 skipped: the two updated tests now pass, and the four new numeric recalculation cases add four tests. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; CI runs the first two on push. No browser walkthrough of the new pages was performed here. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container. These checks were run by an AI coding agent (Claude Code) at the owner's request. The package remains partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.

## Genetics three-point mapping project for learners (2026-10-19)

Genetics advances to 0.6.0. Week 6 gains `assignments/three-point-mapping-project-guide.md`, the synthetic `assignments/three-point-rehearsal-counts.csv` (800 offspring, listed order E, F, G and map order F–E–G) and a five-item, 17-point rehearsal practice set; five project milestones are zero-point self-checks in `rubrics/case-studio.json`, with a `project` self-assessment record in week 7. The association lab's dataset link now resolves to `labs/case-control-genotypes.csv`, which becomes a learner resource with the rehearsal counts. The inactive project draft and its data are unchanged.

Key checks before publication:

- A self-check script graded the five new items with the backend grader: keys earn full credit and wrong responses zero. Another 12 cases (listed order taken as map order, double crossovers left out of the intervals, too few significant figures, coincidence computed from the rounded expectation, the interval sum used as the outer fraction, an unnormalized or inverted Bayes term) earn the stated partial or full scores. An option-length audit flagged no field, and correct answers were spread across option positions.
- `tests/content/test_genetics_project_route.py` (5 tests) recomputes every rehearsal key from the CSV by phase logic alone: it infers the parental and double-crossover classes and the middle marker from counts, then recomputes the interval, outer-marker, coincidence, interference and Bayes keys. It checks the guide's project table against the draft CSV and its worked recap against the lesson's own counts, and confirms that neither the guide nor the rehearsal states the project's fractions, expectation, coincidence, interference, posterior, gene order or double-crossover pair. It also checks that the lab's delivered link resolves to the pinned resource and that every guide link resolves to a lesson route or resource.
- Pins updated: the Genetics snapshot version, the Genetics lesson count (19 to 20), the global case count (35 to 40) and the per-course case map in the backend case-studio test.
- The manifest's numeric-answer limitation now states 55 numeric-type answers (one unit-required, none checking significant figures) and 10 data-interpretation numeric fields that check them; it had said two numeric answers check significant figures.
- The 0.5.8 snapshot is archived as `docs/GENETICS_REVIEW_SNAPSHOT-0.5.8.md`; the handoff lists the guide, rehearsal and lab-link checks for review.

| Actual command/check | Result |
| --- | --- |
| Self-check script over the Genetics item module (backend grader) | 5 items and 12 extra cases passed. |
| `tools/validate_content.py` | Passed: 25 courses, 460 lessons, 2,988 questions, 1,605 cards and 40 cases; 0 errors and 0 warnings. |
| `tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md` | Passed after regeneration. Genetics: 20 lessons, 55 objectives, 113 items, 74 cards; no unmapped objective or outcome. |
| `tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md` | Passed after regeneration. |
| `claims_scan.py --repo uniStemCourseSimulators` | 0 findings. |
| Full verify, `verify.sh --frontend` (log `gen-verify-1`, run with the table change below) | Content, legacy (7), security (1,654 files including the built bundle, 0 findings), ruff, root (3,386 passed, 1 skipped), backend (6,304 passed, 2 skipped) and frontend passed. |
| Not run | Docker Compose stack, Playwright end-to-end suite and the production compose file; CI runs the first two on push. No browser walkthrough of the new pages was performed here. |

Runner: `bash ~/.claude/skills/courselab-dev/scripts/verify.sh --frontend`, Python 3.12.3 and Node 24 in the dev container. These checks were run by an AI coding agent (Claude Code) at the owner's request. The package remains partial, unreviewed and formative-only; passing tests are consistency evidence, not human review.
