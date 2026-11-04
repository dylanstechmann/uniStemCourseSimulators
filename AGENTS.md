# Repository work scope

This guidance supplements the shared workspace instructions. The owner's direct instructions take precedence.

- Treat uniStemCourseSimulators as a repository spanning university-level science, mathematics, engineering, computing and biomedicine. General continuation requests apply to the repository as a whole. A single-course request can narrow a particular batch; do not turn it into an indefinite course-only goal.
- Select a bounded batch with concrete learner outcomes and acceptance checks. Use `docs/COURSE_SCOPE_AUDIT.md` and the active queue in `docs/ROADMAP.md`. Rotate substantive instructional work across subject families unless dependencies or an explicit user priority justify staying in one course.
- Compare actual readings, worked examples, practice and activities with the relevant official MIT OpenCourseWare syllabus/calendar. Record the course code, edition and direct source URL. Distinguish covered, shallow, absent and deliberately deferred topics. Counts, 14-week labels and comparator links alone are not evidence of comparable course depth.
- Keep each package within a defensible university-course boundary. Shared prerequisites belong in their own courses; applied biomedical examples should reinforce the subject's foundations. Interdisciplinary packages may need several comparators and an explicit narrower scope.
- Author original instruction and problems. Preserve attribution and honest partial/unreviewed status. Topic alignment does not establish scientific review, university equivalence, accreditation or endorsement.
- Bundle necessary versions, hashes, snapshots and generated reports with the instructional or functional change. Do not choose a version-label correction, report regeneration, additional near-duplicate case, or empty review scaffold as the next substantive milestone without a verified learner-facing defect.
- Preserve historical assessment/review evidence, but keep current README and roadmap concise. Put progress history in the progress/review records; do not repeatedly restate it in the active work queue.
- Once relevant checks pass, continue to the next substantive task. Repeat checks only for a new change, failure or unresolved concern. Do not manufacture reviewer sign-offs or keep extending a course while waiting for human review.
- Use one editing agent in the working tree. Parallel read-only research or review is allowed; the editing agent integrates findings and performs mutations sequentially.

## Agent tooling (portable across harnesses)

<!-- agent-toolbox:installed -->

This repo vendors its agent tooling (no secrets inside) so Claude Code,
Cline, Codex, OpenCode, Kilo Code, Kimi Code and Grok share one setup:

- `.mcp.json` — project MCP servers:
  `scholar` (PubMed, OpenAlex, Semantic Scholar, CORE, ORCID, Crossref),
  `web` (Exa, Brave, Jina, Firecrawl), `github` (read-only, token via
  `gh auth token`), `context7` (library docs), `playwright` (browser).
- `opencode.json` — the same servers for OpenCode;
  `AGENT_TOOLS.md` has merge snippets for Codex / Cline / Kilo Code and
  CLI fallbacks for Kimi / Grok.
- `.claude/skills/` — project skills: citation-check, courselab-dev, literature-search, web-research, secrets-guard.
- Keys: `~/.config/ai-keys.env` via the `agentkeys` loader — never in git,
  MCP config or chat. Run `secrets-guard` (`--staged`) before committing.
