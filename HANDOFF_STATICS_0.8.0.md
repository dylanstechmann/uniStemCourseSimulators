# Handoff — Statics & Mechanics of Materials 0.8.0 (frames and machines)

This file preserves the state of an in-progress batch so a fresh session can resume without re-investigating.

## What was done (all applied to the working tree, NOT committed)

Taught **frames and machines** in `content/courses/statics-materials`, bumping the package `0.7.0 -> 0.8.0` on branch `statics-trusses`.

- New reading: `content/courses/statics-materials/modules/18-frames-and-machines.md`
  (multi-force vs two-force members; dismembering a frame; toggle-clamp mechanical advantage).
  Worked keys: frame link force **F = −5 kN** (compression, 3-4-5 link), pin reactions **A_x = −3 kN**, **A_y = +4 kN**
  (8 kN load, beam A(0,0)-B(3,0), link B(3,0)-C(6,4)); toggle **mechanical advantage 8/3**, 30 N input -> 80 N clamp.
- New lesson id `statics-materials-22` / module `statics-materials-module-22`, scheduled in **week 1**.
- `practice.json`: +8 items (`statics-materials-22:*`); `retrieval-cards.json`: +4 cards.
- `course.json`: version 0.8.0, +4 objectives, +module, +week-1 slots, +`statics-materials-22-practice` assessment,
  history entry (2026-11-06), updated `intentionally_omitted`/`limitations` (kept "Friction (2.001 lecture 4)" literal),
  numerical-answer counts 151->156.
- `source-map.json` and `content/sources/registry.json` updated (module-22 mapped to mit-2001-syllabus / mit-2001-readings).
- `syllabus.md`: week-1 row, version line, limitations, inventory 22 routes / 136 items / 79 cards.
- New test: `tests/content/test_statics_materials_frames.py`.
- Regen on drift-checked reports: `docs/STATICS_MATERIALS_REVIEW_SNAPSHOT.md`,
  `docs/ASSESSMENT_CANDIDATE_REPORT.md`, `docs/COURSE_GAP_REPORT.md`.
- Test files reconciled from 0.7.0 -> 0.8.0 / lesson count 23 -> 24:
  `test_statics_materials_trusses.py`, `test_statics_semester_expansion.py`,
  `test_statics_materials_project_route.py`, `test_new_geroscience_and_statistics_lessons.py`,
  `test_statics_materials_review_snapshot.py`, `test_ai_assisted_checks.py` (added 2 numeric registry keys).
- Docs updated: `README.md` (inventory 680 lessons / 3,971 questions / 2,308 cards, 2026-11-06),
  `docs/COURSE_PLAN_COMPLETION.md`, `docs/PROGRESS_REVIEW.md`, `docs/STATICS_MATERIALS_REVIEW_HANDOFF.md`.

## Validation (all green, run in /tmp/unistem-test-venv)

- `python tools/validate_content.py` -> PASS (28 courses, 680 lessons, 3,971 questions, 2,308 cards, 164 cases; 0 errors).
- Full root suite: `python -m pytest tests -q` -> **4724 passed, 1 skipped** (26:06).  [log: /tmp/final_tests.log]
- Backend suite: `python -m pytest -q` (in `backend/`) -> **8381 passed, 2 skipped**.
- `ruff check` on changed test files -> clean. `git diff --check` -> clean.

## Environment note

The host `/usr/bin/python3` has a broken stdlib (no `json`); use `/tmp/unistem-test-venv/bin/python`
(pytest 9.1.1, jsonschema, referencing, backend deps all present). `courselab` is importable via `tests/conftest.py`.

## Remaining step

Commit the change on `statics-trusses`, e.g.:
`git add -A && git commit -m "Teach frames and machines in Statics & Mechanics of Materials (0.8.0)"`
(optionally run `secrets-guard --staged` first).

Untracked (decide whether to include): `implementation_plan.md` (this planning doc) — the `.local/` dir
is pre-existing local preview assets and should stay out of the commit.
