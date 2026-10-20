# uniStemCourseSimulators

This is a personal hobby and learning project. Code and educational drafts were developed with substantial assistance from AI coding tools.

Repository: [dylanstechmann/uniStemCourseSimulators](https://github.com/dylanstechmann/uniStemCourseSimulators). See the [progress review](docs/PROGRESS_REVIEW.md) for delivered features, material findings and prioritized remaining work. The software includes local study tools and a graded-assignment prototype; the requested semester-depth courses are still unfinished. Foundations of Cell and Molecular Biology (0.62.1) and Biochemistry I (0.5.1) are the first packages whose whole proposed 14-week plans can be worked through end to end as ungraded practice. Genetics & Genomics (0.6.0), Calculus I (0.5.0), Physics: Mechanics (0.5.0), Statics & Mechanics of Materials (0.5.0), General Chemistry II (0.5.0), Programming & Numerical Methods (0.5.0), Biomaterials & Tissue Engineering (0.4.0) and Bioreactors & Tissue Culture Engineering (0.5.0) now have learner routes for every component they lay out, including their projects, but none has a homework or exam sequence. All ten remain partial and unreviewed. Instructor access is granted to registered accounts by an operator after out-of-band identity verification. Practice score changes are blocked unless the saved question and variant digest still match.

Interactive, source-grounded courses across science, mathematics, engineering, computing, and biomedicine.

An independent open-source learning platform under development. It does **not confer academic credit**, accreditation, degrees, or university prerequisite equivalency. Pathway mappings do not establish admission eligibility or transfer credit. Institutional references identify scope comparators; they do not imply affiliation or endorsement.

## Current course maturity

| Status | Packages | Meaning |
| --- | ---: | --- |
| catalog-only | 0 | Catalog metadata only |
| outlined | 0 | Structured plan without developed teaching |
| partial | 25 | Prototype packages with short readings and formative checks; depth varies |
| beta | 0 | Developed course awaiting required review/gates |
| complete | 0 | All full-course gates satisfied |
| externally reviewed | 0 | Qualified named reviewer examined a specified version |

**No current package meets the complete-course standard.** The repository contains 25 partial packages with 467 lessons, 3,019 formative questions, 1,626 retrieval cards and 75 self-assessed case prompts. These counts measure authored material; they do not establish semester depth, measured workload, scientific review or university equivalence.

The packages span life sciences, chemistry, mathematics, physics, statistics, computing and engineering. Original readings, worked examples, synthetic datasets and practice are available in each subject, with uneven coverage and depth. See the [package inventory](#package-inventory), [measured content gaps](docs/COURSE_GAP_REPORT.md), and [MIT OpenCourseWare scope audit](docs/COURSE_SCOPE_AUDIT.md) for the current boundaries and priorities. Detailed development history belongs in the [progress review](docs/PROGRESS_REVIEW.md).

Development now proceeds across the repository in bounded instructional batches. The next priorities address foundational course gaps identified against official MIT OpenCourseWare syllabi and calendars. New material is original and attributed; references compare scope and expectations without claiming affiliation, copied course delivery, or equivalent credit. Metadata and review-report refreshes are bundled with substantive changes.

The curriculum map adds **37 catalog-only subject nodes** and **8 pathway maps** beside the 25 partial course packages. Catalog-only entries describe planned study areas and dependencies; they contain no authored lessons and cannot be enrolled in. Mapped prerequisite order is planning guidance and does not establish university equivalency.

See [the audit](docs/CURRENT_STATE_AUDIT.md), [quality standard](docs/CONTENT_QUALITY_STANDARD.md), and [remaining work](docs/ROADMAP.md).

## Package inventory

| Course | Domain | Status |
| --- | --- | --- |
| [Biochemistry I: Proteins, Enzymes & Metabolism](content/courses/biochemistry/course.json) | Biochemistry | partial |
| [Biomaterials & Tissue Engineering](content/courses/biomaterials/course.json) | Bioengineering | partial |
| [Bioreactors & Tissue Culture Engineering](content/courses/bioreactors/course.json) | Bioengineering | partial |
| [Calculus I: Differential and Integral Calculus](content/courses/calculus-1/course.json) | Mathematics | partial |
| [Calculus II: Integration, Series & Applications](content/courses/calculus-2/course.json) | Mathematics | partial |
| [Calculus III: Multivariable & Vector Calculus](content/courses/calculus-3/course.json) | Mathematics | partial |
| [Foundations of Cell and Molecular Biology](content/courses/cell-biology/course.json) | Life sciences | partial |
| [Cellular Biomechanics & Mechanobiology](content/courses/cellular-biomechanics/course.json) | Bioengineering | partial |
| [Electrical Circuits & Instrumentation](content/courses/circuits/course.json) | Electrical engineering | partial |
| [Differential Equations for Living & Engineered Systems](content/courses/differential-equations/course.json) | Mathematics | partial |
| [General Chemistry I](content/courses/general-chemistry-1/course.json) | Chemistry | partial |
| [General Chemistry II](content/courses/general-chemistry-2/course.json) | Chemistry | partial |
| [Genetics & Genomics](content/courses/genetics/course.json) | Life sciences | partial |
| [Geroscience & Regenerative Biology](content/courses/geroscience/course.json) | Life sciences | partial |
| [Linear Algebra for Modeling & Robotics](content/courses/linear-algebra/course.json) | Mathematics | partial |
| [Organic Chemistry I for Life Sciences](content/courses/organic-chemistry/course.json) | Chemistry | partial |
| [Physics: Electricity & Magnetism](content/courses/physics-em/course.json) | Physics | partial |
| [Physics: Mechanics for Biomedical Engineers](content/courses/physics-mechanics/course.json) | Physics | partial |
| [Human Physiology for Engineers](content/courses/physiology/course.json) | Life sciences | partial |
| [Programming & Numerical Methods for Bioengineering](content/courses/programming/course.json) | Computing | partial |
| [Robotics & Mechatronics](content/courses/robotics/course.json) | Mechanical engineering | partial |
| [Signals, Systems & Feedback Control](content/courses/signals-control/course.json) | Electrical engineering | partial |
| [Statics & Mechanics of Materials](content/courses/statics-materials/course.json) | Mechanical engineering | partial |
| [Probability, Biostatistics & Experimental Design](content/courses/statistics/course.json) | Quantitative methods | partial |
| [Thermodynamics & Transport in Bioengineering](content/courses/transport/course.json) | Bioengineering | partial |

## Run locally

Install Docker with Compose, then from the repository root:

```sh
docker compose up --build
```

Open http://localhost:8080. Startup generates a database credential in a private Docker volume, starts PostgreSQL, applies Alembic migrations and serves the React reader through a same-origin API proxy. No API key, database password, cloud account or `.env` is required for a fresh development installation. Existing installations must preserve their Compose project identity before updating to the renamed defaults; see [rename migration](docs/DEPLOYMENT.md#product-rename-and-existing-data). `.env.example` documents optional settings. Ports bind to localhost; HTTP cookies are a development setting. Production needs HTTPS and operator-supplied secrets.

## Tested learning system

- React/TypeScript reader with public catalog, explicit maturity/limitations, syllabus, lesson objectives and prerequisite lists. Lesson Markdown renders tables (remark-gfm) and LaTeX mathematics with KaTeX (remark-math and rehype-katex, MIT licensed), loaded as a separate chunk only for text that contains math.
- FastAPI/Pydantic with PostgreSQL SQLAlchemy/Alembic, server guest sessions, account registration/login/logout and guest-to-account preservation.
- Enrollment, private notes, bookmarks and learner-marked reading progress stored on the server; the React notebook searches saved note text across current enrolled courses and links each result back to its lesson. Lesson pages include self-assessment retrieval cards with revealable answers.
- Immutable choice, numeric, symbolic, data-interpretation, structured-rubric, fixed-axis graph-coordinate and bounded CSV-table **formative practice** attempts with diagnosis, hints, next steps, lesson links, and independent criterion scores. The graph exercise plots learner coordinates against supplied replicate data and awards coordinate-level credit; it does not grade axis choice, uncertainty bars, interpolation or interpretation. A cell-biology upload scores replicate counts and means from UTF-8 CSV as inert data with cell-level credit. It does not run uploaded files or grade free-form reasoning; correct results do not establish sound reasoning or mastery.
- Course-level public formative practice sets delivered from version-pinned manifests through answer-free API DTOs. The week-8 cell-biology cumulative rehearsal is labeled ungraded and not a midterm, and the week-14 cumulative final review (25 questions, 13 of them new integrative items on a synthetic clone dataset) is labeled ungraded and not a final exam; weeks 9–14 also have topic practice sets. Biochemistry has eight open homework practice sets, a week-7 midterm review and a week-14 cumulative final review practice set, each labeled ungraded and not an exam, plus a project rehearsal. Their authoring keys remain openly visible in the repository and are not secure exam materials.
- Separate formative practice gradebook and configured weighted-assignment gradebook, attempt/feedback history and an objective-level study indicator based on distinct items, published thresholds and best reviewed formative scores. Graded submissions are deterministic, version/source-pinned, and limited to a strict deadline. Learners can request one human review per formative or graded attempt; operator-provisioned instructors can record a separate score adjustment while the automatic result stays immutable. Graded adjustments affect the weighted calculation and appear in learner history. None of the 25 current packages contains graded work, so none displays a course grade.
- Spaced retrieval review: enrolled learners self-rate revealed retrieval cards, the server schedules each card with a documented deterministic interval rule, and a course Review queue lists due, new and upcoming cards. Ratings are self-assessments and never change practice scores or objective evidence.
- Learner JSON export and confirmed account deletion, keyboard focus/skip link, larger text/high-contrast controls and safe Markdown rendering, including tables.
- Docker development/production examples, reverse proxy, CI and automated content/security-boundary tests.

Single-choice, multiple-select, numeric, bounded symbolic-expression, narrow data-interpretation, structured-rubric, fixed-axis graph-coordinate and constrained CSV numeric-table graders are deterministic. The same supported response formats can be used in versioned graded-assignment submissions; question DTOs omit answer keys, source files are SHA-256 checked, and the API enforces release, attempt and strict-deadline rules. A separate read-only private assessment mount supports server-only `private://` answer packages; no current course references one, and no graded assignment is shipped. When a graded plan is pinned, the exact source bytes are also stored in a private database archive keyed by course version, assignment and digest. Instructor appeals reconstruct the original prompt and form from that archive, including after a course update; non-decline decisions fail closed if its digest or saved grader specification cannot be verified. Database backups therefore contain answer keys and require the same access controls as private assessment files. The automatic score is never rewritten. The tested graded flow uses synthetic fixtures: current catalog packages contain no graded assignments. Numeric grading supports constrained unit conversions, dimensional checks, absolute and relative tolerances, and significant figures. Symbolic grading compares rational expressions through a restricted grammar; it does not execute Python or accept arbitrary SymPy syntax. Structured items map criteria to exact keyed responses; they do not score prose or keyword overlap. The graph grader scores coordinates on fixed axes and does not assess axis choice or scientific interpretation. CSV uploads are size-limited, parsed as UTF-8 and scored only against authored numeric output cells; file contents are never executed. Practice attempts and graded assignments pin question/source specifications. Alembic 0011 also stores a deterministic snapshot of every public course-package file at enrollment and version upgrade, with per-file SHA-256 values and same-version edit rejection; private answer sources are excluded, and existing enrollments are not automatically backfilled. The operator-only report/apply command can recover a legacy archive only with an independently verified package SHA-256; a version-string match alone is insufficient. Enrolled learners can browse saved versions and open them in a read-only view that uses answer-free course and lesson DTOs. Numeric parameter generation, broader data rubrics, arbitrary CSV analysis, historical regrading from archived course-package versions, protected exams and isolated code execution remain unfinished. Instructors receive access only through the operator CLI. This does not make public practice questions secure exams. Course-version changes preserve historical records. Unsupported specifications fail explicitly. Code execution and LLM providers are disabled. The eight pathway maps and broad catalog layer are planning aids. Every week of the proposed fourteen-week biology schedule has authored lessons; eight open homework companions, three synthetic labs, week-8 and week-14 cumulative reviews, and an optional integrative project (a guide, rehearsal practice and five Case studio milestone self-checks) provide ungraded practice. Reviewed graded homework/lab packages, summative exams and a graded project remain unfinished. See [the roadmap](docs/ROADMAP.md).

## Preserved local study tools

The React reader now includes six scientific calculators under **Study tools**, available without enrollment: dilution, buffer pH, enzyme kinetics, RC charging, diffusion timescale, and Ohm's law. Each shows units and model assumptions and links to related courses. Calculator scratch work is ungraded.

The React **Case studio** also exposes the authored prompts and self-check criteria across all 25 partial courses. Enrolled learners can save a private written response and checklist marks; drafts stay bound to the course version and prompt, remain available in account exports, and do not affect grades. Archived cases are read-only.

The previous calculators, cards, case self-assessment and browser notebook remain preserved in `legacy/`; the React reader now has its own searchable notebook over server-saved lesson notes. To use the old reader separately:

```sh
python -m http.server 4173 --directory legacy
```

Open http://localhost:4173. Valid previous storage is copied to a uniStemCourseSimulators key with a retained backup. Browser scores stay unverified; they are not silently imported as server grades. The default web image does not serve the legacy reader or authoring answers. The separate local reader intentionally exposes its public practice solutions and is unsuitable for secure exams.

## Repository boundaries and checks

| Directory | Purpose |
| --- | --- |
| `frontend/` | React/TypeScript application, Vitest and Playwright |
| `backend/` | FastAPI, SQLAlchemy, Alembic and Pytest |
| `content/` | Original Markdown, schemas, manifests, public authoring specifications and provenance |
| `legacy/` | Preserved static teaching/study reader |
| `tools/` | Content validation and credential/bundle checks |
| `docs/` | Audit, design, quality, deployment and validation evidence |

No third-party instructional assets have been imported. Public repository authoring solutions remain discoverable; a production operator must store restricted exam keys privately. Learner DTOs and default frontend bundles exclude assessment answer specifications and unreleased solution feedback. Educational worked examples remain public readings.

```sh
pip install -r requirements-dev.txt -r backend/requirements.txt
python tools/validate_content.py
python -m pytest tests -q
npm run test:legacy
cd backend
python -m pytest -q
ruff check .
cd ../frontend
npm ci
npm run lint
npm test
npm run build
npx playwright install --with-deps chromium
npm run test:e2e
```

Start Compose before E2E. Run `python tools/check_security.py --bundle frontend/dist` from the root after building. `python tools/validate_content.py --check-links` performs network probes; two JHU pages currently deny the automated client with HTTP 403, so live-link validation is **not fully passed**. Offline schema/content validation passes with 98 explicit legacy-depth warnings for the short prototype readings. Detailed commands, test counts and boundaries are in [VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md). Browser QA of the protected, graded mode, which runs outside Docker against a throwaway fixture, is described in [QA_PROTECTED_GRADED.md](docs/QA_PROTECTED_GRADED.md). Production guidance: [DEPLOYMENT.md](docs/DEPLOYMENT.md).

## Contributing and licensing

Read [CONTRIBUTING.md](CONTRIBUTING.md). To review a lesson, or to understand what reader feedback, AI-assisted checks and subject-matter review can each change, read the [reviewer guide](docs/REVIEWER_GUIDE.md); AI-assisted check records are in [docs/reviews/ai-assisted](docs/reviews/ai-assisted/README.md). Software retains MIT. Educational licensing is separate in [LICENSE-CONTENT](LICENSE-CONTENT) and [content/SOURCES_AND_LICENSES.md](content/SOURCES_AND_LICENSES.md). Historical MIT grants remain valid. Adapted OCW material requires applicable CC BY-NC-SA 4.0 attribution/ShareAlike conditions and asset-level checks; JHU catalogs are alignment references only.

Security: [SECURITY.md](SECURITY.md). Test evidence: [docs/VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md).
