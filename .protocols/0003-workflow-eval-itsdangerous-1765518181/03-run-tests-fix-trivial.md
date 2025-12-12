# Step 3: Run tests and fix trivial issues

## Briefing
- **Goal:** Execute full/targeted test suite per CI expectations; address trivial failures (minor code/test fixes) to reach green.
- **Key files:**
  - `tests/` and related source files for fixes
  - CI scripts/config if adjustments needed for local parity
- **Additional info:** Limit to trivial fixes; document anything non-trivial as open issue.

## Sub-tasks
1. Re-open `context.md` to confirm current step/branch and ensure Step 2 changes are committed/clean.
2. Review CI workflow notes (from Step 1) to select the closest local command(s) (e.g., `pytest` with any flags/markers); acknowledge any matrix-only jobs that won't be run locally.
3. Run the selected test command(s) from repo root; capture failing test names/messages for reference.
4. Apply only trivial fixes for failures (typos, missing imports, obvious small logic/test adjustments); if a fix would be non-trivial, log it instead of changing code.
5. Re-run the impacted test command(s) until they pass locally; if something cannot be fixed trivially or reproduced locally, record the exact failure and why it remains.
6. Update `log.md` with commands run, failures observed, fixes made, and any remaining/non-trivial issues or environment gaps.
7. Update `context.md` to set `Current Step` to `4`, `Status` to `In Progress`, and include a concise `Next Action` describing the first task for Step 4.

## Workflow
1. Execute sub-tasks.
2. Verify: ensure `pytest` (and lint/typecheck if required) pass locally; document any skipped/unsupported checks.
3. Fix/record:
   - Add to `log.md` what/why (fixes and test outcomes).
   - Update `context.md` for next step.
   - Check cleanliness vs `main`.
4. Commit: `git add .` then `git commit -m "chore: tests green with trivial fixes [protocol-0003/03]"`. Push.
5. Report to user using the step report format.
