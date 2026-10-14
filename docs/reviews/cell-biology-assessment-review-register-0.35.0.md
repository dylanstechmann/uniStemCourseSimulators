# Biology 0.35.0 assessment review register

**Status:** preparation form only. No reviewer is assigned and no candidate has passed independent or qualified review. Completing this register records review evidence; it does not activate an assessment or authorize a grade.

## Review boundary

Review the exact public candidate version listed below and the corresponding protected source through an approved private channel. The public [assessment candidate audit](../ASSESSMENT_CANDIDATE_REPORT.md) records public artifact hashes and unresolved gates. At the start of each review, record the exact public and private source hashes used. Any content, key, tolerance, scoring rule, form, or dataset change invalidates sign-off for that candidate until the changed version is reviewed again.

Do not place answer keys, learner data, identity information, or sensitive reviewer comments in Git. Record only the review status, public artifact identity, finding IDs, and non-sensitive disposition here. Keep detailed private key comparisons in the approved restricted location and link them by evidence ID, not by copying answers.

Reviewers must be independent of the candidate author for the role they sign. Record relevant qualifications, conflicts, method, scope, and date. One person may sign more than one role only when their qualifications support each role and the role-specific work is recorded separately. Same-author calculations, automated checks, and this blank register are not independent review.

## Required review dimensions

- **Numerical and key review:** independently derive every keyed value from the stated observations and assumptions; check units, rounding, significant figures, tolerances, categorical alternatives, point allocation, both fixed forms, and the exact form-to-key binding.
- **Subject-matter review:** verify scientific accuracy, learning-objective alignment, dataset/control interpretation, causal language, and the limits the instructions place on conclusions.
- **Assessment design review:** judge blueprint coverage and cognitive demand, whether the item evidence supports the stated objective, clarity and sufficiency of instructions, scoring validity, and treatment of written reasoning left outside machine scoring.
- **Accessibility and fairness review:** inspect keyboard and screen-reader paths, text alternatives for tables/plots, language and assumed background, timing and retry expectations, and whether the task creates avoidable barriers. Record tested methods and any untested modes.
- **Human-scoring review, where applicable:** evaluate the proposed rubric, performance-level distinctions, grader calibration procedure, disagreement resolution, and appeal path. Machine-check points are not a substitute for these criteria.

The separate [workload pilot protocol](cell-biology-workload-pilot-0.35.0.md) covers course-wide learner-time evidence. A candidate's review is not complete merely because its machine-scored portion has been checked; the frozen course plan and workload pilot must also be addressed before release.

## Author-side public-data preflight

The answer-free regression in `tests/content/test_cell_biology_candidate.py` now checks all 15 public inactive candidate DTO files representing 14 intended components, including the preserved final revision, the eight homework datasets, three limited lab tables, both cumulative exams, and both integrative-project tables. The checks cover form parity, named preparation/condition/time structure, finite values, and declared denominator or count bounds where applicable. Latest author-side run on 2026-10-10: **105 passed**; Ruff passed; the all-course content validator reported 25 courses, 384 lessons, 2,270 questions, 1,276 cards and 25 cases with no errors or warnings; candidate-audit and objective-coverage report drift checks passed.

Reproduce with `pytest -q tests/content/test_cell_biology_candidate.py`, `ruff check --no-cache tests/content/test_cell_biology_candidate.py`, `python tools/validate_content.py --root . --json`, `python tools/assessment_candidates.py --check docs/ASSESSMENT_CANDIDATE_REPORT.md`, and `python tools/objective_coverage.py --check docs/COURSE_GAP_REPORT.md`. These are same-author public-artifact checks. They do not read or recalculate protected keys, establish numerical correctness, substitute for candidate-specific review, or change any status in the register below.

## Candidate register

Set each status to `not assigned`, `in progress`, `revise`, or `signed`. Leave it `not assigned` until a qualified, independent reviewer accepts the role. Record the evidence ID and date for every sign-off. `Signed` means the reviewer signed the exact version and no unresolved blocking findings remain; it is not operator release approval.

| Component | Candidate version | Public review packet | Numerical/key | Subject matter | Assessment design | Accessibility/fairness | Human scoring |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Homework 1 | 0.20.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/homework-01-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Homework 2 | 0.21.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/homework-02-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Homework 3 | 0.22.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/homework-03-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Homework 4 | 0.23.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/homework-04-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Homework 5 | 0.24.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/homework-05-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Homework 6 | 0.25.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/homework-06-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Homework 7 | 0.26.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/homework-07-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Homework 8 | 0.27.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/homework-08-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Midterm | 0.28.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/midterm-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Lab 1 limited check packet | 0.30.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/lab-01-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Lab 2 limited check packet | 0.31.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/lab-02-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Lab 3 limited check packet | 0.32.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/lab-03-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Cumulative final v2 | 0.35.0 | [Candidate](../../content/courses/cell-biology/assessment-specs/final-v2-candidate.md) | not assigned | not assigned | not assigned | not assigned | not assigned |
| Integrative project | 0.33.0 | [Portfolio](../../content/courses/cell-biology/assessment-specs/integrative-project-portfolio.md) | not assigned | not assigned | not assigned | not assigned | not assigned |

The superseded final v1 packet (0.29.0) is preserved for history and is not the candidate under review. Lab rows describe limited machine-check packets; they do not stand for complete laboratory assessment or wet-lab instruction.

## Reviewer and artifact record

Copy one block per reviewer and role. Keep detailed comments and answer comparisons in the restricted review record; use neutral finding IDs here.

```text
Candidate/component:
Candidate version:
Public handout SHA-256:
Public DTO/data SHA-256:
Protected source SHA-256 (digest only):
Reviewer name or approved identifier:
Role signed:
Relevant qualifications:
Independence/conflict statement:
Review date:
Methods and scope:
Evidence record ID:
Status: not assigned / in progress / revise / signed
Blocking finding IDs still open:
Follow-up version and review date, if revised:
```

For each finding, record its ID, component/item ID, severity, category, recommended action, owner, target date, resolved version, and the independent reviewer who verified closure. Do not record a keyed answer in the public register.

## Course-level release gate

Before any candidate is treated as accepted graded work, the course owner must confirm that all applicable candidate reviews are signed on the exact frozen artifacts, all blocking findings are closed, the human-scored work has an approved rubric and grading/appeal process, the course-wide workload pilot has been analyzed, and candidate-specific protected delivery, archived source verification, retake, accommodation, and operator procedures are ready. The platform's archive path has synthetic coverage, but the actual inactive Biology candidate sources have not been pinned or verified through it. Record the separate operator decision and its authority. Until then the candidates stay inactive and the course stays partial and formative-only.

Current register state: **no reviewers assigned; no sign-offs; no release decision.**
