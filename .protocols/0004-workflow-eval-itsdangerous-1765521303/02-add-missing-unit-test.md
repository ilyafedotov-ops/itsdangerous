# Step 02: Add missing unit test

## Briefing
- **Goal:** Implement the missing unit test following existing patterns to cover the identified gap.
- **Key files:**
  - `tests/...` (target module and related fixtures)
  - Project module(s) under test (e.g., `itsdangerous/...`)
- **Additional info:** Reuse fixtures/helpers; keep style consistent with neighboring tests.

## Sub-tasks
1. Reopen findings from Step 1 to identify the exact behavior lacking coverage (module/function/path and scenario).
2. Locate the matching test module under `tests/` (or closest neighbor); if absent, select an appropriate package path and filename to add.
3. Inspect neighboring tests for style (fixtures, markers, parametrization, helper imports) to mirror patterns.
4. Write the new test case(s) capturing the missing behavior, including assertions for expected outcome and any edge/negative variant identified.
5. Ensure imports and fixtures align with project conventions; add/adjust minimal helpers only if required.
6. Run focused pytest on the specific file or test node to confirm the new test executes: e.g., `python -m pytest tests/path/to/file.py::TestNameOrFunction`.
7. If failures occur, refine the test (and only minimal code under test if strictly necessary) until the focused run passes.
8. Stage changes for review (`git status` sanity check).

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "test: add coverage for missing case [protocol-0004/02]"`. Push.
5. Report to user using the step report format above.
