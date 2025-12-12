# Step 04: Finalize

## Briefing
- **Goal:** Wrap up protocol: ensure documentation/logs/context are updated, mark PR ready, and provide final report.
- **Key files:**
  - `.protocols/0004-workflow-eval-itsdangerous-1765521303/context.md`
  - `.protocols/0004-workflow-eval-itsdangerous-1765521303/log.md`
  - PR description/body
- **Additional info:** Confirm branch is clean and pushed; align PR title/body with protocol.

## Sub-tasks
1. Open `log.md` and `context.md`; confirm `Current Step` shows 04 and prior entries are complete.
2. Append final step notes to `log.md` (what/why, checks run, commit ID placeholder).
3. Update `context.md` to reflect completion: set `Current Step` to done, `Next Action` to none or handoff note.
4. Verify working tree: `git status` shows clean; `git diff main...HEAD --stat` has only intended files.
5. Run final `lint`, `typecheck`, and `test` (scope appropriate); note results for the report.
6. Ensure PR metadata is ready: update title/body if needed, switch from draft to ready.
7. Stage and commit remaining protocol artifacts (if any): `git add .` → `git commit -m "chore: finalize protocol 0004 [protocol-0004/04]"`.
8. Push branch and confirm remote is up to date.
9. Re-check `log.md` to fill in the actual commit ID after push.
10. Prepare final user report with protocol status, checks run, git state, and working directory.

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "chore: finalize protocol 0004 [protocol-0004/04]"`. Push.
5. Report to user using the step report format above.
