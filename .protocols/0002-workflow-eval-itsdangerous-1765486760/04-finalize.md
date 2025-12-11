# Step 04: Finalize

## Briefing
- **Goal:** Perform final verification, tidy protocol docs, and prepare for handoff/PR readiness.
- **Key files:**
  - `.protocols/0002-workflow-eval-itsdangerous-1765486760/context.md`
  - `.protocols/0002-workflow-eval-itsdangerous-1765486760/log.md`
  - PR description/metadata
- **Additional info:** Ensure context/log are up to date; ensure branch is clean and pushed.

## Sub-tasks
1. Re-read prior step outputs to confirm planned scope is complete and no pending TODOs remain.
2. Run final sanity checks (`lint`, `typecheck`, `test`) needed for confidence; capture results.
3. If any check fails, apply minimal fixes; re-run the relevant check(s) until green.
4. Update `.protocols/0002-workflow-eval-itsdangerous-1765486760/log.md` with a concise final summary, including check results and commit references.
5. Update `.protocols/0002-workflow-eval-itsdangerous-1765486760/context.md`: set `Current Step` to `done/complete`, set `Status` to `Ready for Review`, and record `Next Action` (e.g., review/merge).
6. Verify working tree cleanliness: `git status` must be clean after staging; ensure no untracked/extra files.
7. Ensure the latest commits are pushed to the remote branch; confirm PR state (draft/ready) matches readiness.
8. Prepare the final user report per the required format, including checks run, git/PR status, and working directory path.

## Workflow
1. Execute the sub-tasks in order, starting with re-reading prior outputs.
2. Run required checks (`lint`, `typecheck`, `test`); address failures minimally and re-run until passing.
3. Record updates:
   - Append final notes to `log.md` (what changed, why, check outcomes, commit IDs).
   - Update `context.md` with final status fields and next action.
   - Confirm `main` has no stray files from this branch.
4. Stage and commit any remaining tracked changes with `git add .` and `git commit -m "feat(scope): subject [protocol-0002/04]"`; push to remote.
5. Draft and deliver the final report to the user using the specified step report format.
