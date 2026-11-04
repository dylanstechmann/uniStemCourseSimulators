---
name: courselab-dev
description: Work on uniStemCourseSimulators (its earlier folder is lattice-biomed-academy). Runs the CI-equivalent checks without Docker (content validator, root and backend pytest, legacy node tests, security scan, ruff, React lint, tests and build in a Linux copy) and carries the course's authoring, grading, source and honesty rules. Use when editing content/courses, question banks, rubrics, modules, the source registry, docs, backend or frontend code, grading logic or Alembic migrations, before committing to that repo, and whenever asked whether a course or package is complete, reviewed, graded or ready.
---

# uniStemCourseSimulators

A personal hobby and learning project, developed with substantial AI assistance (README, CONTRIBUTING).
It is not a university course and confers no credit. All 25 course packages are `partial` and unreviewed.
Keep it that way unless a real, named, qualified reviewer examined a specific version.

## Verify
```bash
bash ${CLAUDE_SKILL_DIR}/scripts/verify.sh               # content, legacy, security, ruff, root + backend pytest
bash ${CLAUDE_SKILL_DIR}/scripts/verify.sh --frontend    # also React lint, unit tests, build, bundle scan
bash ${CLAUDE_SKILL_DIR}/scripts/verify.sh --list
```
- The full run takes about 5 minutes (root pytest is the long pole). Start it in the background and read the table when it finishes.
- Logs go to `~/.cache/courselab-verify/<time>/`. The venv is `~/.cache/venvs/courselab`, pinned from `requirements-dev.txt` and `backend/requirements.txt`.
- The frontend is copied to `~/.cache/node-copies/courselab-frontend` and installed there with `npm ci`, so nothing is written into the mounted repo.
- Baseline on 2026-10-07, this container, Python 3.12.3: content validator exits 0 with two known warning kinds (legacy-depth 98, objective-coverage 25); root pytest 75 passed; backend pytest 248 passed; security scan 428 files, 0 findings; ruff clean. A different count means tests were added or removed, or something broke. Find out which before reporting anything as passing.
- Not run here: `docker compose up`, the Playwright end-to-end suite (`frontend/e2e`), and the production compose file. These need the host or CI. Say so in every report.

## Rules that apply to every change
- Solutions never reach learners. `solution_spec`, answer keys and answer-bearing feedback stay out of learner DTOs, frontend imports and the default bundle. `tools/check_security.py --bundle` checks for leaks; do not add its marker strings to public content.
- Protected assessments are referenced as `private://...` and live outside the repo. Never create, commit, or paste answer files, even on a temporary branch.
- No credentials, `.env` files, learner exports, database passwords or assessment secrets in git or chat. `.env.example` is the documented template.
- Status and review labels describe a specific version. Do not raise a package's maturity, write `complete` or `externally reviewed`, or invent a reviewer. Preserved partial seeds never qualify.
- Placeholder, TODO/TBD, duplicated or trivial teaching is rejected by the validator. Do not add filler to reach a count.
- Third-party material is link-only unless `content/sources/registry.json` grants quotation or adaptation (`reuse_mode`, `permissions`). Do not paste OCW or other licensed text. Public catalogs only set scope.
- Verify every new PMID, DOI, NCT or paper link with the `citation-check` skill before it goes into a lesson, card or registry entry. Record the access date.

## Grading and assessment changes
- Grading code needs tests for alternate correct answers, wrong units, near misses, malformed inputs and misleading keyword answers. Use fixed seeds and synthetic learner data.
- Practice points are never labelled as course grades. Keep `formative-only` until a complete, reviewed graded package is provisioned.
- Authoring details (symbolic grammar, variants, data-interpretation fields, assessment schedules, private sources) are in `references/authoring-rules.md`. The normative field contracts are the JSON Schemas in `content/schemas/`.

## Git and reporting
- Commit or push only when asked. One coding agent per working tree; check `git status` first and leave changes you did not make alone.
- `lattice-biomed-academy` is the earlier history of this project: its HEAD commit `e532a16` is an ancestor of this repo's HEAD. Work in `uniStemCourseSimulators` unless told otherwise.
- Edits under `.github/workflows/` need the `workflow` token scope, which this container's `gh` lacks. Save a patch and say so.
- CONTRIBUTING asks that passed and failed commands be recorded. Put the exact command and result in your report, and list what was not run.
- For wording in the course (advice-to-a-person, overclaims, disclosure), run `claims_scan.py` from the `regen-guardrails` skill with `--repo uniStemCourseSimulators`. Its teaching-content exemptions are already set.

## Files
- `scripts/verify.sh`: the check runner described above.
- `references/authoring-rules.md`: condensed authoring, grading and source rules with pointers to the full documents.
