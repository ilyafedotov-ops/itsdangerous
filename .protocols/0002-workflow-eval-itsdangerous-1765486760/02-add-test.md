# Step 02: Add minimal missing unit test

## Briefing
- **Goal:** Implement the selected small missing test using existing test patterns.
- **Key files:**
  - Relevant `tests/...` file(s) per Step 1 findings
  - Any fixtures/helpers referenced
- **Additional info:** Keep changes minimal; avoid refactors; reuse fixtures/utilities.

## Sub-tasks
1. Re-read `context.md` to confirm the chosen missing test and target module.
2. Open the target `tests/...` file and locate nearby patterns to mirror (naming, fixtures, markers).
3. Draft the new test case following the existing style; use existing fixtures/helpers where possible.
4. If the test needs data/setup, add the smallest fixture/helper tweak necessary in the same area; avoid cross-file refactors.
5. Ensure imports are minimal and ordered per project convention; keep formatting consistent.
6. Run the most-focused test target (e.g., `pytest tests/path/test_file.py -k <name>`) to confirm the new case works before broader checks.
7. Note in `log.md` what was added and why, including any helper tweaks.

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "feat(scope): subject [protocol-0002/02]"`. Push.
5. Report to user using the step report format above.
