# Agriculture, Construction and Closed-Loop Habitats review handoff

This handoff targets Agriculture, Construction and Closed-Loop Habitats package version 0.1.0 and the shared `habitat-ledger` study tool. The package and calculator remain partial, unreviewed and formative-only; no reviewer, operator decision or approval is recorded. Current agent-run evidence is collected in the [validation report](VALIDATION_REPORT.md).

## Delivered review scope

- Review the eight lesson routes, 48 public practice items, 24 retrieval cards and six zero-point self-assessment cases against the package's stated interdisciplinary-survey boundary, objective/outcome mappings and recommended prerequisites.
- Compare the actual readings and activities with the link-only MIT, USDA, NASA and primary-science references in the [scope crosswalk](../content/courses/agriculture-construction-habitats/scope-crosswalk.md) and [source map](../content/courses/agriculture-construction-habitats/source-map.json). Counts and links do not establish course depth or equivalence.
- Independently recalculate the PPFD/DLI, photoperiod, energy, water, inventory, construction-dependency and outage examples and all 24 numeric public answers. Recompute the synthetic CSV residuals row by row without treating reused scenarios as independent physical replicates.
- Check that plant editing remains evidence literacy without operational editing instructions; construction remains conceptual without site-specific design instructions; water work supplies no nutrient prescription; and habitat accounting makes no habitability or life-support claim.
- Review the optional project route, synthetic audit lab, six zero-point cases, accessible alternatives and proposed workload. No case score establishes practical competence, professional authorization or graded mastery.

## Habitat ledger checks

The public tool's defaults are PPFD 200 μmol/m²/s, photoperiod 16 h/day, lighting 120 W, other continuous equipment 80 W, water demand 40 L/day, recovered water 30 L/day and reservoir 120 L. Independently confirm DLI 11.52 mol/m²/day, lighting energy 1.92 kWh/day, total equipment energy 3.84 kWh/day, water makeup 10 L/day, recovery 75% and reservoir endurance 12 days. Other equipment is accounted for over 24 hours.

Exercise input scaling, reset, zero PPFD/equipment, missing/nonfinite and negative values, photoperiod above 24 hours, recovered water above demand, and numeric overflow. At full recovery the tool must omit endurance instead of reporting infinity; at zero demand it also omits the undefined recovery percentage. Confirm the related-course links to this package, Biochemistry I and Circuits & Instrumentation. The calculator is daily accounting only: it is not crop-yield prediction, HVAC analysis, nutrient prescription or life-support certification.

## Author-side evidence and its limits

The focused content regression recomputes every public numeric answer and synthetic CSV residual, exercises the deterministic graders, and checks source links, mappings and explicit boundaries. Frontend unit/component regressions cover the registry, formulas, validation and full-recovery behavior; the completed credential-free Playwright journeys cover catalog/pathway discovery, every public lesson and case route, synthetic resources and calculator behavior. These are AI-assisted consistency checks, not independent agricultural, biological, structural, controls or life-support review. See the dated validation entry and the actual-run record below for commands and results.

## Actual browser verification (2026-11-26)

The earlier unrun Playwright status is superseded by an actual credential-free run. Docker was unavailable, so the documented explicit SQLite development fallback and standalone Vite server were migrated through Alembic 0012 and bound only to `127.0.0.1:8000` and `127.0.0.1:5173`. Repository Playwright 1.63.0 launched cached Chrome for Testing 155.0.8059.12 (revision 1247) through ignored local cache aliases. No browser/dependency installation, authentication or external account was used.

| Check | Actual result |
| --- | --- |
| `PLAYWRIGHT_BROWSERS_PATH=/workspace/uniStemCourseSimulators/frontend/node_modules/.cache/ms-playwright E2E_BASE_URL=http://127.0.0.1:5173 npx playwright test e2e/habitat-survey.spec.ts` from `frontend/` | **2 passed in 14.3 s**. |
| Discovery and routes | Catalog search and keyboard-opened curriculum pathway reached the package; all eight lesson routes rendered their expected reading evidence, six practice items and three retrieval cards each. Public practice controls remained disabled without enrollment. |
| Synthetic resources and cases | Both CSV resources returned `text/csv` bytes identical to the authored files and retained `synthetic-original`; all six zero-point case prompts/checklists rendered with editing disabled and no unauthenticated save control. |
| Habitat ledger | Defaults, keyboard calculation, scaling, reset, full recovery without endurance, excessive recovery, negative/missing inputs, photoperiod above 24, overflow and zero light/equipment behaved as asserted. All three related-course links were present. |
| Keyboard/accessibility/privacy | Pathway disclosure, retrieval-card disclosure and calculation worked by keyboard. Four axe scans covering the expanded pathway catalog, representative lesson, case studio and calculated ledger reported **zero WCAG 2.1 A/AA violations**. Both tests observed **zero non-GET API requests**. |
| Final focused frontend/content checks | `npx vitest run src/studyTools.test.ts src/components/StudyTools.test.tsx`: **34 passed in 9.91 s**. `npm run lint` and `npm run typecheck`: PASS. `.venv/bin/python -B -m pytest tests/content/test_agriculture_construction_habitats_package.py -q`: **10 passed in 7.85 s**. |

Pre-final browser attempts exposed test-only defects: ambiguous workspace/lesson heading locators, unsupported role-based `summary` lookup and non-verbatim evidence strings. The spec now scopes the actual workspace headings, uses native `summary` selectors and asserts the authored text. No product code was changed and no assertion was weakened to obtain the final pass. Automated checks are not a substitute for the independent review below.

## Review record to complete only after review

After review actually occurs, record reviewer name and qualifications, date, package version and exact artifacts examined, concrete findings and dispositions. Keep separate decisions for scientific and engineering correctness, instructional design, assessment, accessibility, workload and release. Do not infer approval from test results, generated reports or package hashes.
