# Step 04: Finalize

## Briefing
- **Goal:** Prepare PR for review, ensure artifacts are up to date, and close out the protocol.
- **Key files:**
  - `.protocols/0005-workflow-eval-itsdangerous-1765524374/`
  - PR description/body
- **Additional info:** Include final status and any follow-up items.

## Sub-tasks
1. Gather state:
   - Open `.protocols/0005-workflow-eval-itsdangerous-1765524374/log.md` and `context.md`; note current step and pending items.
   - List workspace status (`git status`) to identify untracked/uncommitted files.
2. Verify protocol artifacts:
   - Ensure `log.md` has entries for this step’s work (what/why, commit IDs once known).
   - Ensure `context.md` reflects final state for Step 04 prior to closing (current step set, next action pending completion).
3. Update PR text:
   - Pull latest PR body template if any; include summary of changes, tests run, and known issues.
   - Mark PR as ready for review in the hosting platform (or note action if manual).
4. Branch and cleanliness checks:
   - Confirm branch name matches protocol branch; ensure no uncommitted changes remain unless intentional.
   - Verify `main` has no stray files from this branch (git worktree status or `git status` on main).
   - Push branch to remote; confirm remote branch exists.
5. Finalize context:
   - Update `context.md` to mark protocol complete and set next action (e.g., awaiting review/merge).
   - Append final log entry capturing completion and push status.
6. Commit and push docs:
   - Stage updated protocol/docs (`git add .` scoped to intended files).
   - Commit with `git commit -m "chore(protocol): finalize protocol docs [protocol-0005/04]"`.
   - Push to remote.
7. Report to user:
   - Prepare report per required format (Done/Checks/Git/Working directory/Protocol status) with PR link and test summary.
   - Share report.

## Workflow
1. Execute sub-tasks in order; keep worktree clean.
2. Verify: run `lint`, `typecheck`, `test` as needed for confidence; address any failures before finalizing.
3. Fix/record:
   - Add to `log.md` what/why (including non-obvious decisions and commit IDs).
   - Update `context.md`: increment `Current Step` if applicable, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "chore(protocol): finalize protocol docs [protocol-0005/04]"`. Push.
5. Report to user using the step report format above.
