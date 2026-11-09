# Implementation Plan

[Overview]
Add a single new instructional module, **"Frames and machines"**, to the `statics-materials` course package, bumping it from `0.7.0` to `0.8.0` to fill the explicitly-deferred gap immediately following the planar-truss work on the current `statics-trusses` branch.

This is a **content-authoring batch** (Markdown reading + JSON manifest/question-bank/source-map updates + tests + review-record refresh). No backend/frontend runtime code changes, no new external dependencies, and no schema changes are required. The change continues the MIT OCW 2.001 (Fall 2006) comparator sequence: after the delivered truss readings (lessons 20 and 21, MIT lectures 3 / 9 / 10), the next topic in that sequence is frames and machines, whose members are *not* two-force members. This is the single most defensible "next" step: `statics-materials` currently states in its own `intentionally_omitted` list that "Friction (2.001 lecture 4), frames and machines, space trusses and matrix stiffness analysis are not taught", and its syllabus notes "broader truss/frame and nonlinear beam analysis remain thin".

Bounded scope: **one new module** (one reading, 4 objectives, 8 practice items, 4 retrieval cards). Friction, space trusses, and matrix stiffness analysis remain explicitly deferred for later batches (they keep a presence in `intentionally_omitted`).

[Types]
No new or modified type definitions, interfaces, or data structures in application code. All data lives in existing JSON (already covered by `content/schemas/course.schema.json`, `question.schema.json`, `source.schema.json`) and one new Markdown reading. The only "type-like" work is authoring new JSON objects that conform to the existing schemas:
- New `lesson_objectives` entries (shape: `{id, description, bloom, course_outcome_ids}`).
- New question objects using the existing `single_choice` / `multiple_select` / `numeric` / `data_interpretation` question types.
- New retrieval-card objects (shape: `{id, lesson_id, front, back, objective_ids, license}`).
[Files]

New files:
1. `content/courses/statics-materials/modules/18-frames-and-machines.md`
   - Original reading (>=700 words, matching the lesson-length invariant enforced in `tests/content/test_statics_semester_expansion.py`), CC-BY-4.0, AI-assisted, all loads/dimensions synthetic.
   - Follow the structure of `modules/16-planar-trusses-joints-and-sections.md`: a `**Status:**` line, `## Learning objectives`, body sections, `## Common mistakes`, and `## Scope and sources`.
   - Content outline:
     a. **Two-force vs multi-force members** — contrast with trusses: a member between two frictionless pins carrying only end forces is a two-force member (axial only); otherwise the member also carries bending/shear.
     b. **Frames vs machines** — frames are stationary multi-member structures whose members carry bending; machines transform an input force/torque into an output (pliers, toggle clamp, wheelbarrow).
     c. **Frame analysis procedure** — (1) identify any two-force members; (2) solve the whole-structure free-body for support reactions; (3) dismember at pins, applying equal-and-opposite pin forces; (4) check each member's equilibrium.
     d. **Worked frame example** — a synthetic three-member frame (e.g. an L-shaped lever pinned to ground with one diagonal two-force link), with a full numeric solution (reactions, pin forces) stated in the reading and reproducible.
     e. **Machine example / mechanical advantage** — a synthetic toggle or lever machine with a numeric input-to-output force (mechanical advantage = output/input).
     f. **Common mistakes** — treating a multi-force member as axial; forgetting equal-and-opposite pin forces; never checking a member that carries moment; guessing a member is two-force because it "looks like a bar".
   - `## Scope and sources` names MIT OCW 2.001 Fall 2006 as a link-only scope comparator, states what is *not* taught (friction, space trusses, matrix stiffness analysis), and carries license/attribution wording.

2. `tests/content/test_statics_materials_frames.py`
   - Mirrors `tests/content/test_statics_materials_trusses.py`: re-solves every numeric key from closed-form equilibrium (exact `Fraction` arithmetic where geometry is exact), then checks the reading's stated values and grades each authored key via `courselab.grading.grade` / `AttemptRequest`.
   - Test functions:
     - `test_worked_example_and_reading_statements()` — recompute the frame reactions/pin forces and the machine mechanical advantage; assert the exact strings appear in `modules/18-frames-and-machines.md`.
     - `test_choice_items_accept_only_their_key()` — for each `single_choice`/`multiple_select` item of lesson `statics-materials-22`, assert only the authored key grades correct.
     - `test_schedule_scope_and_status()` — assert lesson `statics-materials-22` is scheduled in week 1, `MANIFEST["version"] == "0.8.0"`, maturity `partial`, review `unreviewed`, grading `formative-only`, that each question's `objective_ids` cover the lesson's four objectives, that there are exactly 4 retrieval cards, and that the reading contains the link-only-comparator and "not taught" status sentences.
Existing files to modify:
1. `content/courses/statics-materials/course.json`
   - `version`: `"0.7.0"` -> `"0.8.0"`.
   - `history`: append a `0.8.0` entry (date `2026-11-06`) summarizing the new frames-and-machines module; keep every prior entry unchanged.
   - `lesson_objectives`: add `statics-materials-22-objective-1` .. `-4` (below `-21-objective-4`), each with `bloom` and `course_outcome_ids` pointing at existing outcome `statics-materials-outcome-1` (plus `-2` where bending stress appears).
   - `modules`: append `statics-materials-module-22` (mirror `statics-materials-module-20`): one lesson `statics-materials-22` with `title`, `reading` = `modules/18-frames-and-machines.md`, `objectives` = the four new ids, `worked_example` = one-line summary of the numeric keys, `question_ids` = the 8 new ids, `card_ids` = the 4 new ids.
   - `duration.weeks`: add `"statics-materials-22"` to the **week 1** `lesson_ids` (`["statics-materials-1","statics-materials-6","statics-materials-20"]` -> append `"statics-materials-22"`). Rationale: frames/machines belongs to the equilibrium-of-assemblies cluster taught right after trusses. (Alternative week 2 rejected: it holds distributed loads, a different theme.)
   - `intentionally_omitted`: rewrite the item "Friction (2.001 lecture 4), frames and machines, space trusses and matrix stiffness analysis are not taught; truss readings use ideal pin-jointed, small-displacement models." to remove "frames and machines" while **retaining the literal substring `Friction (2.001 lecture 4)`** (a test asserts it), e.g. "Friction (2.001 lecture 4), space trusses and matrix stiffness analysis are not taught; truss and frame/machine readings use ideal pin-jointed, two-force-member, small-displacement models."
   - `limitations`: update the two trailing entries that mention "frames and machines ... are not [taught]"/"remain beyond these examples" to reflect that frames/machines are now taught while friction/space-trusses/matrix-stiffness/nonlinear beam behavior remain open. Keep the "all synthetic, no design basis/test protocol/safety advice" language intact.

2. `content/courses/statics-materials/question-banks/practice.json`
   - Append 8 questions with ids `statics-materials-22:<slug>` (e.g. `two-force-member`, `frame-reactions`, `pin-forces`, `machine-output`, `mechanical-advantage`, `member-moment`, `consistency-check`, `model-limits`), assign `objective_ids` so every objective has direct practice evidence, `visibility: "public-practice-authoring"`, `provenance.kind: "original"`.
   - Mix types across the 8 items: `single_choice`, `multiple_select`, `numeric`, and at least one `data_interpretation` (with `response_fields`/`field_specs` carrying numeric `answer` + `tolerance`) so the test can grade exact keys. Avoid raw exponent notation or float artifacts in `prompt`/`feedback` text (enforced by `tests/content/test_learner_visible_number_formatting.py`).

3. `content/courses/statics-materials/question-banks/retrieval-cards.json`
   - Append 4 cards `statics-materials-22-card-1` .. `-card-4` with `lesson_id: "statics-materials-22"`, each `front`/`back` linked to one of the four objectives.

4. `content/courses/statics-materials/source-map.json`
   - Append a module entry `statics-materials-module-22` with `lesson_id: "statics-materials-22"`, `reading: "modules/18-frames-and-machines.md"`, `source_ids: ["mit-2001-syllabus","mit-2001-readings"]`, `relationship: "original-instruction-with-link-only-scope-comparators"`, `original_content: true`, `license: "CC-BY-4.0"`, and a `modifications` note stating the reading is original with no source text/diagram/problem/data imported.

5. `content/courses/statics-materials/syllabus.md`
   - Add the new reading to the week-1 row: `...; [Frames and machines: multi-force members, dismembering frames and mechanical advantage](modules/18-frames-and-machines.md)`.
   - Update the "Current limitations" paragraph (remove "broader truss/frame ... remain thin"; reflect that frames/machines are now taught while friction/space-trusses/matrix-stiffness remain deferred).
   - Update the final inventory line ("21 reading/activity routes, 128 public practice items, 75 retrieval cards") -> 22 / 136 / 79.

6. `content/sources/registry.json`
   - In both `mit-2001-syllabus` and `mit-2001-readings`, add `"statics-materials-module-22"` to `mapped_modules`.
   - Extend `mit-2001-syllabus` `third_party_notes` to record the re-read OCW calendar lecture number/title for frames/machines (after re-reading the calendar; the existing note records titles 3/9/10). Sources stay link-only comparators.

7. `docs/STATICS_MATERIALS_REVIEW_HANDOFF.md`
   - Append a "Review target 0.8.0" paragraph describing the frames-and-machines reading and the specific keys a reviewer should recompute (frame reactions, pin forces, machine mechanical advantage, two-force vs multi-force identification), mirroring the existing "Review target 0.7.0" paragraph.

8. `docs/STATICS_MATERIALS_REVIEW_SNAPSHOT.md` (generated)
   - Regenerate via `python tools/course_package_digest.py --course-id statics-materials` and paste the new `content_version` (0.8.0), `package_sha256`, `manifest_sha256`, `file_count`, `archive_bytes` into the pinned fields. Required because `tests/content/test_statics_materials_review_snapshot.py` asserts the snapshot matches the digest.

9. Bookkeeping docs (after all checks pass): `docs/ROADMAP.md`, `docs/PROGRESS_REVIEW.md`, `docs/VALIDATION_REPORT.md`, `docs/COURSE_PLAN_COMPLETION.md` and the `README.md` inventory counts — update the statics-materials version note and running lesson/item/card totals to match the validator inventory. Keep concise; do not restate history into the active queue.
Tests to modify:
10. `tests/content/test_statics_materials_trusses.py`
    - Line ~184: `assert MANIFEST["version"] == "0.7.0" ...` -> `"0.8.0"`.
    - The `intentionally_omitted` assertion (line ~192) continues to pass as long as the literal `Friction (2.001 lecture 4)` substring is preserved.

11. `tests/content/test_statics_semester_expansion.py`
    - Line ~203: `MANIFEST["version"] == "0.7.0"` -> `"0.8.0"`.
    - Line ~206: `len(scheduled) == len(set(scheduled)) == 23` -> `24` (one new scheduled lesson).
    - `len(NEW) == 12` (line ~202) and the `range(16, 20)` loop are unaffected (lesson 22's ids use the `statics-materials-22:` prefix, outside the `1[6-9]:depth-` regex).

12. `tests/content/test_statics_materials_review_snapshot.py`
    - `assert actual["content_version"] == "0.7.0"` -> `"0.8.0"`.

13. `tests/content/test_ai_assisted_checks.py`
    - Extend the shared numeric-recalculation registry (the dict near line ~2196 holding `statics-materials-20:degree-of-indeterminacy`, `statics-materials-20:end-post`, `statics-materials-21:member-elongation`) with the new lesson-22 numeric keys, recomputed independently from the authored formulas.

[Functions]

New functions (in the new test file only — no production code):
- `solve_frame(...)` in `tests/content/test_statics_materials_frames.py`: builds and solves the linear equilibrium system for the synthetic frame with exact `Fraction` arithmetic (analogous to `solve(...)` in `test_statics_materials_trusses.py`); asserts the system is determinate and consistent.
- `machine_advantage(...)` in the same file: computes the synthetic machine's output/input force ratio from moment balance.
- Test functions `test_worked_example_and_reading_statements`, `test_frame_equilibrium_recomputed`, `test_choice_items_accept_only_their_key`, `test_schedule_scope_and_status`.

Modified functions: none in application code. Only assertion literals (versions/counts) change in existing tests plus the registry dict in `test_ai_assisted_checks.py`.

Removed functions: none.

[Classes]
No class changes. The content pipeline already represents a new lesson through the existing `courselab.content.ContentRepository` (backend/courselab/content.py) without code modification.

[Dependencies]
No new packages, no version changes, no file moves/deletes, no configuration updates. The work is confined to authored JSON/Markdown and pytest files that already run in the existing environment.

[Testing]

Validation commands (run inside the project's dev Compose service per workspace guidance — `python .agent-containers/workspace.py shell uniStemCourseSimulators`; `/workspace` is the repo root there):
- `python tools/validate_content.py` — offline schema/content validation (must report zero errors).
- `python -m pytest tests -q` — root content tests (includes the new + modified test files).
- `cd backend && python -m pytest -q` — backend suite (should be unaffected; confirms no regression).
- `ruff check .` — lint.
- `python tools/course_package_digest.py --course-id statics-materials` — used to regenerate the review snapshot hashes.

Acceptance criteria (all must hold):
1. `validate_content.py` reports zero errors and zero new limitation/depth warnings.
2. `test_statics_materials_frames.py` passes: every numeric key recomputed from equilibrium, every choice/multi-select key grades only its authored answer, the reading states the checked numbers, and `version == "0.8.0"`.
3. The version assertions in the three existing test files are reconciled to `0.8.0`, and the scheduled-lesson count becomes 24.
4. `test_statics_materials_review_snapshot.py` passes against the regenerated snapshot (hash/count match).
5. `test_ai_assisted_checks.py` passes with the new lesson-22 registry keys.
6. Full root `pytest` and backend `pytest` are green; `ruff check .` is clean.
7. No learner-visible text contains raw exponent notation or float artifacts (number-formatting test).

Environment note: the host `/usr/bin/python3` in this container has a broken stdlib (`json` imports fail); run all suites in the project container (or a Python with an intact stdlib, e.g. `backend/.venv`).

[Implementation Order]
1. Author `modules/18-frames-and-machines.md` (original reading); in parallel, work out the exact synthetic frame/machine numbers by hand (exact fractions where geometry permits) to lock the keys.
2. Add the 4 `lesson_objectives`, the `statics-materials-module-22` module entry, the week-1 schedule slot, and the `version`/`history` bump in `course.json`.
3. Add the 8 questions to `practice.json` and the 4 cards to `retrieval-cards.json` using the locked keys.
4. Add the `source-map.json` module entry and update `content/sources/registry.json` (`mapped_modules` + re-read calendar note for the frames/machines lecture title).
5. Update `syllabus.md` (week-1 row, limitations, inventory counts).
6. Update `intentionally_omitted` and `limitations` in `course.json` (drop "frames and machines", preserve the `Friction (2.001 lecture 4)` literal).
7. Write `tests/content/test_statics_materials_frames.py`.
8. Reconcile the three existing test files (version `0.8.0`, scheduled count `24`) and extend the `test_ai_assisted_checks.py` registry.
9. Run `validate_content.py` and the targeted content tests; fix any schema/format errors.
10. Regenerate `docs/STATICS_MATERIALS_REVIEW_SNAPSHOT.md` from `course_package_digest.py`; update `docs/STATICS_MATERIALS_REVIEW_HANDOFF.md` with a 0.8.0 paragraph.
11. Run the full root + backend suites and `ruff check .`; then update the bookkeeping docs (ROADMAP.md, PROGRESS_REVIEW.md, VALIDATION_REPORT.md, COURSE_PLAN_COMPLETION.md, README.md counts) to match the validator inventory.
12. Commit on the `statics-trusses` branch with a message in the established style (e.g. "Teach frames and machines in Statics & Mechanics of Materials (0.8.0)") after running `secrets-guard --staged`.