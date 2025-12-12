# 0003 — workflow-eval-itsdangerous-1765518181

## ADR-style Summary:
- **Context**: Need structured end-to-end workflow for post-QA-relax evaluation on itsdangerous repo using TasksGodzilla protocol artifacts.
- **Problem Statement**: Ensure tests/CI landscape is understood, add missing unit coverage, run tests and fix trivial issues, and finalize with clean commits and protocol hygiene.
- **Decision**: Follow a multi-step protocol with setup, discovery of tests/CI, targeted test addition, execution/fixes, and a finalization sweep.
- **Alternatives**: Ad-hoc changes without protocol; skipping discovery; manual notes without context/log files.
- **Consequences**: Repeatable workflow, traceable changes, reduced risk of missed checks, clear documentation; added upfront planning overhead.

---

## High-Level Plan:
This section is a **contract**; do not change during implementation.

- **[Step 0: Prepare and lock plan](./00-setup.md)**: Create and commit protocol artifacts.
- **[Step 1: Scan tests and CI](./01-scan-tests-ci.md)**: Enumerate tests, fixtures, helpers, CI matrix, and identify target areas for coverage.
- **[Step 2: Add missing unit test](./02-add-missing-unit-test.md)**: Implement the needed unit test(s) based on findings, align with project style.
- **[Step 3: Run tests and fix trivial issues](./03-run-tests-fix-trivial.md)**: Execute relevant suites; address trivial failures; ensure green.
- **[Step 4: Finalize](./04-finalize.md)**:
  * Mark PR Ready
  * Close out work

---

## Protocol Workflow (How to execute)
Follow `High-Level Plan` and this cycle for each step.

- **PROJECT_ROOT**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous
- **CWD (worktree)**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree
- **Protocol folder**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree/.protocols/0003-workflow-eval-itsdangerous-1765518181

All work happens in the worktree (CWD).

### A. Before a new step (restore context)
1. Read `Current Step` from `context.md`.
2. Open the step file (e.g., `01-scan-tests-ci.md`).
3. Ensure previous changes are committed.

### B. During the step (execute)
1. Do the sub-tasks in the step file.
2. Do **not** change plan files (`plan.md`, `XX-*.md`). They are the contract.
3. Follow Generic Principles below.

### C. After the step (verify & fix)
1. Run checks: `typecheck`, `lint`, `test`. Fix until green.
2. Add a `log.md` entry describing what and why (include commit ID).
3. Rewrite `context.md` for the next step.
4. Verify `main` has no stray files from our branch. Commit with `type(scope): subject [protocol-0003/YY]`. Push.
5. Report to the user in the format:
<report_format>
(Protocol, step):

**Done**: what/where/why (also in Log).

**Checks**: which ran (lint/typecheck/test), pass/fail, why.

**Git**: PR link; current branch; commit message; push status; main-branch cleanliness check.

**Working directory**: absolute CWD path.

**Protocol status**: where we are and what’s next.
</report_format>

---

## Generic Principles (MUST follow, shared)
- Balance & simplicity; avoid overengineering.
- No legacy; greenfield decisions allowed.
- Respect coding standards/linters/formatters/JSDoc.
- Keep docs current (Memory Bank), atomic.
- Quality tests: positive/negative/boundaries; reuse helpers.
- Detail & decomposition: plans executable without this chat.

---

## Reference Materials
- Existing tests under `tests/` for patterns/fixtures.
- CI config under `.github/workflows/` to understand matrix and required checks.
- Project docs/README for contributor guidelines.
