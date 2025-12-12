# 0006 — workflow-eval-itsdangerous-1765528512

## ADR-style Summary:
- **Context**: Need a structured protocol to run an end-to-end evaluation of the project with a code-side QA downgrade requirement.
- **Problem Statement**: Ensure evaluation tasks and QA adjustments are executed reproducibly with clear checkpoints and documentation.
- **Decision**: Use protocol 0006 with a worktree-based workflow, stepwise plan, and disciplined logging.
- **Alternatives**: Ad-hoc execution without protocol; single-branch workflow without worktree isolation.
- **Consequences**: Clear reproducibility, auditable steps, and minimized risk of missed QA adjustments.

---

## High-Level Plan:
This section is a **contract**; do not change during implementation.
- **[Step 0: Prepare and lock plan](./00-setup.md)**: Create and commit protocol artifacts.
- **[Step 1: Analyze requirements and baseline](./01-analysis.md)**: Confirm task scope, review existing QA expectations, and establish baselines.
- **[Step 2: Apply code-side QA downgrade changes](./02-implementation.md)**: Implement required adjustments and ensure alignment with downgrade intent.
- **[Step 3: Validate, test, and document](./03-validation.md)**: Run checks/tests, capture results, and update logs/context.
- **[Step 4: Finalize](./04-finalize.md)**: Prepare PR status, confirm protocol completion, and summarize outcomes.

---

## Protocol Workflow (How to execute)
Follow `High-Level Plan` and this cycle for each step.

- **PROJECT_ROOT**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous
- **CWD (worktree)**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree
- **Protocol folder**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree/.protocols/0006-workflow-eval-itsdangerous-1765528512

All work happens in the worktree (CWD).

### A. Before a new step (restore context)
1. Read `Current Step` from `context.md`.
2. Open the step file (e.g., `01-analysis.md`).
3. Ensure previous changes are committed.

### B. During the step (execute)
1. Do the sub-tasks in the step file.
2. Do **not** change plan files (`plan.md`, `XX-*.md`). They are the contract.
3. Follow Generic Principles below.

### C. After the step (verify & fix)
1. Run checks: `typecheck`, `lint`, `test`. Fix until green.
2. Add a `log.md` entry describing what and why (include commit ID).
3. Rewrite `context.md` for the next step.
4. Verify `main` has no stray files from our branch. Commit with `type(scope): subject [protocol-0006/YY]`. Push.
5. Report to the user in the format:
(Protocol, step):

**Done**: what/where/why (also in Log).

**Checks**: which ran (lint/typecheck/test), pass/fail, why.

**Git**: PR link; current branch; commit message; push status; main-branch cleanliness check.

**Working directory**: absolute CWD path.

**Protocol status**: where we are and what’s next.

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
- Project docs in README and CONTRIBUTING (if present).
- Existing tests and CI configurations in repository.
