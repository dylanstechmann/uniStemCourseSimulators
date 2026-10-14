# Biochemistry I review snapshot

This record pins the current public course package for independent review. It is regenerated for each authoring increment and does not imply acceptance or release.

- **Course package:** `biochemistry` 0.4.84
- **Public package archive SHA-256:** `b650c42d64a583e2828de5e588b646a0b9316b967332042a8d629b485fda28eb`
- **Manifest SHA-256:** `cba02bb31072d88e073e4bf444771e5071743a2cc62a4b8c7f94d4fb82089751`
- **Archive inventory:** 70 files, 1,119,349 bytes
- **Calculated:** 2026-10-11
- **Reproduce:** `uv run --project backend python tools/course_package_digest.py --course-id biochemistry`

The package contains eight inactive homework candidates, a 12-case midterm, a 52-case cumulative final, a five-deliverable human-scored project candidate, and two synthetic-data virtual labs. Virtual lab 2 works through protein and activity totals, specific activity, recovery and enrichment for every synthetic fraction, while stating that one observation per fraction cannot estimate replicate variability. The week-7 kinetics lab header now matches package 0.4.84, and a regression recomputes every displayed replicate mean and both reciprocal fits from its linked CSV. The week-6 free-energy reading now defines the reaction quotient using dimensionless activities and checks its ATP, coupling, redox and equilibrium examples. The week-4 binding reading now derives the ligand-depletion quadratic, checks free and bound amounts against mass balance, and states the model assumptions. The week-7 kinetics CSV is served as a package-pinned learner resource, and its 2–3 hour duration is labeled an unvalidated author estimate. Private answer and scoring drafts remain outside the public package; every assessment candidate remains inactive. Final case 52 calculates the stoichiometric urea amount from a synthetic nitrogen load and distinguishes ATP molecules from high-energy phosphate equivalents. The digest proves package identity only; it is not biochemical review, instructional approval or release evidence.
