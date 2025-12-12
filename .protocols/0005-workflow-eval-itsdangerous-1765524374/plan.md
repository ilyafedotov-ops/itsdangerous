# 0005 — workflow-eval-itsdangerous-1765524374

## ADR-style Summary:
- **Context**: Execute an end-to-end workflow evaluation for itsdangerous using the bundled QA prompt, ensuring protocol artifacts, implementation, and validation are tracked.
- **Problem Statement**: We need a structured plan to run the workflow evaluation, apply any necessary adjustments, and validate outcomes while keeping the repository workflow clean and auditable.
- **Decision**: Use protocol 0005 to create a dedicated worktree/branch, document steps, implement required changes/tests, and validate via lint/test before finalizing.
- **Alternatives**: Ad-hoc updates without protocol tracking; skipping dedicated validation; working directly on main. Rejected due to traceability and safety concerns.
- **Consequences**: Clear traceability, reproducible steps, and auditable changes; slight upfront overhead to maintain protocol artifacts.

---

## High-Level Plan:
This section is a **contract**; do not change during implementation.

- **[Step 0: Prepare and lock plan](./00-setup.md)**: Create and commit protocol artifacts.
- **[Step 1: Discover requirements and baseline](./01-discovery.md)**: Review QA prompt, current code/tests, and establish baseline checks.
- **[Step 2: Implement workflow evaluation adjustments](./02-implementation.md)**: Apply code/config/test changes needed for the evaluation.
- **[Step 3: Validate and document results](./03-validation.md)**: Run test/lint suite, capture outcomes, and document.
- **[Step 4: Finalize](./04-finalize.md)**:
  * Mark PR Ready
  * Close out work

---

## Protocol Workflow (How to execute)
Follow `High-Level Plan` and this cycle for each step.

- **PROJECT_ROOT**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous
- **CWD (worktree)**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree
- **Protocol folder**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree/.protocols/0005-workflow-eval-itsdangerous-1765524374

All work happens in the worktree (CWD).

### A. Before a new step (restore context)
1. Read `Current Step` from `context.md`.
2. Open the step file (e.g., `01-step-name.md`).
3. Ensure previous changes are committed.

### B. During the step (execute)
1. Do the sub-tasks in the step file.
2. Do **not** change plan files (`plan.md`, `XX-*.md`). They are the contract.
3. Follow Generic Principles below.

### C. After the step (verify & fix)
1. Run checks: `typecheck`, `lint`, `test`. Fix until green.
2. Add a `log.md` entry describing what and why (include commit ID).
3. Rewrite `context.md` for the next step.
4. Verify `main` has no stray files from our branch. Commit with `type(scope): subject [protocol-NNNN/YY]`. Push.
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
- Repository docs and README under `README.rst`.
- Existing tests under `tests/` for guidance on patterns.
- QA prompt bundle (as provided in task context).