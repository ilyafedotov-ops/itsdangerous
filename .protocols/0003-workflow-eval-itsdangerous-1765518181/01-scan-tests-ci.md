# Step 1: Scan tests and CI

## Briefing
- **Goal:** Understand existing tests, helpers, fixtures, and CI workflows; identify missing coverage area for upcoming unit test.
- **Key files:**
  - `tests/` tree (structure, helpers, fixtures)
  - `.github/workflows/` for CI matrix/required jobs
  - `pyproject.toml` / `setup.cfg` for test deps and tooling
- **Additional info:** Focus on discovering a realistic target area for coverage aligned with task description.

## Sub-tasks
1. Inventory tests
   - List top-level packages/modules under `tests/` (use `ls` or `find`).
   - Note any `conftest.py`, fixtures, factories, and shared helpers.
   - Capture parametrization patterns and notable markers (e.g., `pytest.mark` usage).
2. Identify CI config
   - Open each file in `.github/workflows/`; note job names, triggers, required checks.
   - Record matrix details: Python versions, OS, optional extras.
   - Extract test commands (pytest flags, coverage, environment variables).
3. Spot coverage gaps and select target
   - From test inventory, note modules with few/no tests or edge cases untested.
   - Cross-check with source modules to pick a small, well-scoped function/class needing a unit test.
   - Write down why the chosen target matters (behavior to verify, regression risk).
4. Record findings
   - Append summaries to `.protocols/0003-workflow-eval-itsdangerous-1765518181/log.md`: test layout, CI matrix, chosen target, rationale.
5. Update context
   - Edit `.protocols/0003-workflow-eval-itsdangerous-1765518181/context.md`: set `Current Step` to `2`, `Status` to `In Progress`, `Next Action` to start Step 2, and summarize discoveries in `Last Action Summary`.

## Workflow
1. Execute sub-tasks in order.
2. Verify: no code changes expected; if incidental edits happen, revert or justify. No tests required here.
3. Fix/record:
   - Add to `log.md` what/why (selected coverage target and rationale).
   - Update `context.md` for next step.
   - Check cleanliness vs `main` (only intended updates to logs/context).
4. Commit: `git add .protocols/0003-workflow-eval-itsdangerous-1765518181` then `git commit -m "chore(protocol): record discovery for tests/ci [protocol-0003/01]"`. Push.
5. Report to user using the step report format.
