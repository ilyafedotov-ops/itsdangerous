# 0002 — workflow-eval-itsdangerous-1765486760

## ADR-style Summary:
- **Context**: Need to evaluate tests/CI for itsdangerous, add a small missing unit test if obvious, and run checks with minimal changes.
- **Problem Statement**: Ensure repo test/CI coverage is understood, add a minor missing test, and verify workflows/spec stay valid with minimal footprint.
- **Decision**: Follow a staged protocol: inspect CI/tests, add one small test, run checks, and finalize with minimal changes.
- **Alternatives**: Skip adding tests (would not meet task); restructure CI/tests heavily (too risky for scope).
- **Consequences**: Clear, minimal plan; small code impact; ensures QA alignment and traceable steps.

---

## High-Level Plan:
This section is a **contract**; do not change during implementation.

- **[Step 0: Prepare and lock plan](./00-setup.md)**: Create and commit protocol artifacts.
- **[Step 1: Scan repo tests and CI](./01-repo-scan.md)**: Review tests and CI workflows, identify an obvious missing small unit test.
- **[Step 2: Add minimal missing unit test](./02-add-test.md)**: Implement the chosen small test with minimal code changes.
- **[Step 3: Run tests and fix trivial issues](./03-run-tests.md)**: Execute tests, address trivial failures, ensure spec validity/QA alignment.
- **[Step 4: Finalize](./04-finalize.md)**: Final verification, tidy context/log, and prepare handoff.

---

## Protocol Workflow (How to execute)
Follow `High-Level Plan` and this cycle for each step.

- **PROJECT_ROOT**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous
- **CWD (worktree)**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree
- **Protocol folder**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree/.protocols/0002-workflow-eval-itsdangerous-1765486760

All work happens in the worktree (CWD).

### A. Before a new step (restore context)
1. Read `Current Step` from `context.md`.
2. Open the step file (e.g., `01-repo-scan.md`).
3. Ensure previous changes are committed.

### B. During the step (execute)
1. Do the sub-tasks in the step file.
2. Do **not** change plan files (`plan.md`, `XX-*.md`). They are the contract.
3. Follow Generic Principles below.

### C. After the step (verify & fix)
1. Run checks: `typecheck`, `lint`, `test`. Fix until green.
2. Add a `log.md` entry describing what and why (include commit ID).
3. Rewrite `context.md` for the next step.
4. Verify `main` has no stray files from our branch. Commit with `type(scope): subject [protocol-0002/YY]`. Push.
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
- Project docs, README, CONTRIBUTING, existing tests, CI workflows under `.github/workflows/`.
- Prior commits/tests for patterns.
