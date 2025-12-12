# Step 4: Finalize

## Briefing
- **Goal:** Confirm protocol completion, PR readiness, and clear next steps for reviewers.
- **Key files:**
  - `context.md`, `log.md`
  - PR description
- **Additional info:** Ensure the branch is clean, pushed, and that documentation/logs reflect final state.

## Sub-tasks
1. Re-read prior step files and `context.md` to verify all steps (00–03) are marked done; note any gaps to address.
2. Update `log.md` with a concise final entry: what changed, tests run/results, commit ID, remaining risks.
3. Update `context.md` to reflect final status: set `Current Step` to 04, `Status` to Complete, `Next Action` to monitoring/follow-up, and record branch/commit info.
4. Open the PR draft/description; ensure it references the protocol folder (`.protocols/0006-workflow-eval-itsdangerous-1765528512`), summarizes changes, and lists checks run.
5. Set PR to “Ready for Review” (if applicable) and ensure reviewers/labels are appropriate.
6. Run a final cleanliness check: `git status --short` for stray/untracked files; inspect `main` for stray files from our branch per protocol.
7. Push the branch; confirm remote is up to date.
8. Prepare the final user report per required format (Done, Checks, Git, Working directory, Protocol status).

## Workflow
1. Execute sub-tasks in order, capturing notes for `log.md` and `context.md`.
2. Verify: run final `lint`/`test` if confidence needs confirmation; record outcomes.
3. Fix/record:
   - Add to `log.md` final summary and test results.
   - Update `context.md`: set `Status` to `Complete`, `Next Action` to monitoring or follow-up, include branch/commit identifiers.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "chore(protocol): finalize workflow [protocol-0006/04]"`. Push.
5. Report to user using the step report format above.
