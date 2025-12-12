# 0004 — workflow-eval-itsdangerous-1765521303

## ADR-style Summary:
- **Context**: Evaluate and adjust the itsdangerous project with an end-to-end workflow: understand tests/CI, add a missing unit test, validate by running tests, and finalize.
- **Problem Statement**: We need to ensure test coverage by adding a missing unit test and confirm health via local test execution, while following protocolized steps.
- **Decision**: Work in an isolated worktree/branch using a fixed stepwise protocol with commits per step and clear logging.
- **Alternatives**: Ad-hoc changes without structured steps; updating code without logs/commits per step; skipping local test execution.
- **Consequences**: Provides reproducible history and predictable progress; slightly slower due to process overhead; easier review and handoff.

---

## High-Level Plan:
This section is a **contract**; do not change during implementation.

- **[Step 0: Prepare and lock plan](./00-setup.md)**: Create and commit protocol artifacts.
- **[Step 1: Scan tests and CI expectations](./01-scan-tests-ci.md)**: Inspect test suite layout, fixtures, and CI configuration to understand expectations and focus areas.
- **[Step 2: Add missing unit test](./02-add-missing-unit-test.md)**: Implement the required new test using project patterns and helpers.
- **[Step 3: Run tests and fix trivial issues](./03-run-tests-fix.md)**: Execute relevant test matrix locally; address trivial breakages if any.
- **[Step 4: Finalize](./04-finalize.md)**:
  * Mark PR Ready
  * Close out work

---

## Protocol Workflow (How to execute)
Follow `High-Level Plan` and this cycle for each step.

- **PROJECT_ROOT**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous
- **CWD (worktree)**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree
- **Protocol folder**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree/.protocols/0004-workflow-eval-itsdangerous-1765521303

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
4. Verify `main` has no stray files from our branch. Commit with `type(scope): subject [protocol-0004/YY]`. Push.
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
- Project docs/tests under `docs/` and `tests/` for patterns.
- CI configs (`.github/workflows/`, `tox.ini`, `pyproject.toml`) to mirror expectations locally.
