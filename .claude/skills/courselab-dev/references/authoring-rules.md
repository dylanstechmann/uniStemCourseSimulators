# Authoring, grading and source rules (uniStemCourseSimulators)

Condensed from the repository's own documents on 2026-10-07. The documents are authoritative; if this
file disagrees with them, follow the documents and fix this file. Paths are inside the course repo.

- `CONTRIBUTING.md`: teaching and assessments belong in `content/`; follow `docs/AUTHORING_GUIDE.md`; attach
  provenance; run validation. Do not copy paid or unlicensed teaching. Public catalogs inform scope only.
  Software changes need tests. Grading changes need alternate correct answers, wrong units, near misses,
  malformed inputs and misleading keyword responses. Use fixed seeds and synthetic learner data.
- `docs/CONTENT_QUALITY_STANDARD.md`: maturity ladder catalog-only, outlined, partial, beta, complete,
  externally reviewed. Every package is partial today. The ten full-course gates cover schema and
  dependencies, 12 to 15 weeks of workload, substantial original explanation, objective coverage through
  practice, homework, labs, midterm, final and project, grader mutation and recalculation checks,
  provenance and licences, placeholder and duplicate detection, accessibility, test coverage, and actual
  human review. Missing evidence counts as failure. Counts cannot substitute for depth.
- `docs/AUTHORING_GUIDE.md` (the field-level contract; the JSON Schemas in `content/schemas/` are normative):

## Layout and lesson links
- A course lives in `content/courses/<id>/`: `course.json`, `syllabus.md`, `modules/`, `question-banks/`
  (`practice.json`, `retrieval-cards.json`), `rubrics/`, `source-map.json`.
- Lessons link cards with `card_ids`. Cards are self-assessment, not scored attempts. Each card carries
  objective IDs and the applicable content licence.
- Use stable IDs and acyclic prerequisites. Objectives describe observable performance (interpret a
  perturbation, compare controls, calculate transport, justify a mechanism with uncertainty).

## Assessment schedules and policies
- Optional assessment fields: `title`, `week`, `category_id`, `release_at`, `due_at`, `attempt_limit`,
  `attempt_scoring` (`highest` by default, or `latest`). Timestamps are ISO 8601 with a timezone (UTC `Z`
  preferred). A due time equal to now is still open; a missing submission becomes zero only after it.
- A `lab`, `simulation` or `data-analysis` assessment may use `mode: practice` with public practice items.
  Its points are practice points, never graded lab credit.
- Keep `mode: formative-only`, an empty category list and only practice or self-assessment modes until a
  complete, reviewed graded package exists.
- A `graded-course` policy needs non-empty unique categories whose decimal weights sum to exactly 1, and at
  least one graded assessment per category. `category_aggregation` is `points` or `assessment-average`.

## Private (protected) assessments
- Keep learner-facing instructions and datasets in the public package. Keep `solution_spec` and
  answer-bearing feedback in the protected store, referenced as `private://assignments/<file>.json`, located
  under `<private-root>/courses/<course-id>/assignments/` and mounted through
  `COURSELAB_PRIVATE_ASSESSMENTS_PATH` (see `docs/DEPLOYMENT.md`).
- The plan records a checksum at enrolment. Missing or changed source content blocks grading.
- Never commit the answer file, including on a temporary branch.

## Question types
- Symbolic items: `type: symbolic`, a plain-string `expression`, a unique list of declared `variables`, and an
  `assumptions` map from declared names to booleans. Rational arithmetic only (`2*x`, parentheses, integer
  powers such as `x^2`). No function calls, no arbitrary SymPy syntax. Test equivalent forms and near misses.
  Limits are in `docs/AUTOGRADER_DESIGN.md`.
- Authored variants: `randomization` with `seeded: true`, `generator_id: authored-variants-v1`, and
  `variants`. The unmodified question is the `base` form. Each variant needs a stable unique `id`, a distinct
  substantive `prompt`, a complete `solution_spec` and targeted `feedback`. The validator merges shared
  fields and validates every resolved spec. Learners receive only the selected prompt and a signed
  seven-day token; attempts record the variant ID and digest.
- `data_interpretation` items: declare each field in `response_fields` (stable ID, response type, prompt,
  positive points; choice fields need at least two options). Add a `solution_spec.field_specs` entry for each
  field ID. Field points must sum to the parent question's points. Partial credit is per field. The grader
  checks numbers and explicit choices only, never free-text reasoning or plots.

## Quality gates to respect
- Preserved partial seeds have a brevity exception only while partial. Newly authored placeholders,
  duplicated readings or questions, and trivial teaching are rejected. Do not add filler to pass counts.
- Complete promotion needs every gate, independent numerical checks, accessibility checks, current source
  links, and actual human review by a named qualified person of a specified version. Never invent review,
  outcomes, accreditation or credit equivalence. Workload estimates must not imply credit equivalence.

## Sources and licences
- `content/sources/registry.json` holds the source records (`url`, `accessed_at`, `license`, `reuse_mode`,
  `permissions`, `attribution_requirements`). Most third-party sources are `link-only`. Linking is not
  redistribution permission.
- Register an asset before reusing it. Do not paste OCW or other licensed text into lessons.
- Every new PMID, DOI or NCT identifier: verify with the `citation-check` skill, then record the access date.
  A Crossref or PubMed notice (for example an expression of concern) is a reason to pause and tell the owner
  before a lesson relies on that paper. Do not silently delete or rewrite the lesson.

## Learner data and secrets
- Synthetic learner data only. No learner exports, `.env` files, database passwords or production assessment
  secrets in git or chat. `tools/check_security.py` scans tracked source and the built bundle.
- Learner DTOs and default frontend bundles must exclude `solution_spec` and unreleased feedback.
- Report vulnerabilities privately as described in `SECURITY.md`; do not open a public issue.
