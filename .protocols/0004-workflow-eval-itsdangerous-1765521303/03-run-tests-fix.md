# Step 03: Run tests and fix trivial issues

## Briefing
- **Goal:** Execute relevant test suites locally and address any trivial failures introduced by changes.
- **Key files:**
  - `tests/`
  - Any modified project files
- **Additional info:** Focus on minimal fixes aligned with existing patterns; avoid scope creep.

## Sub-tasks
1. Confirm the relevant test targets from Step 1 (e.g., `python -m pytest tests`) and note any markers/versions needed for parity with CI.
2. Run the primary test command covering the new test; capture failing test names and error snippets.
3. For each failure, apply the smallest viable fix (imports, fixtures, assertions, typing) without changing behavior beyond the test intent.
4. Re-run the same test command to ensure fixes worked; repeat until the targeted suite is green.
5. If any failures remain non-trivial, document them clearly for follow-up (test name, failure message, suspected cause).
6. Record outcomes and commands in `log.md`; update `context.md` to set Step 4 as next.

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "chore: stabilize tests [protocol-0004/03]"`. Push.
5. Report to user using the step report format above.
