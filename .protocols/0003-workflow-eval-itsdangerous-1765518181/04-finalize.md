# Step 4: Finalize

## Briefing
- **Goal:** Final protocol wrap-up: ensure documentation/state is current, PR ready, and no stray work remains.
- **Key files:**
  - `.protocols/0003-workflow-eval-itsdangerous-1765518181/context.md`
  - `.protocols/0003-workflow-eval-itsdangerous-1765518181/log.md`
  - PR description/body if edits needed
- **Additional info:** Confirm branch status, push, and mark PR ready.

## Sub-tasks
1. Read `.protocols/.../log.md` and `.protocols/.../context.md`; verify prior steps are captured.
2. Update `context.md` fields (`Last Action Summary`, `Next Action`, status indicators) to reflect step completion intent.
3. Check git status; if not clean, `git diff` to understand pending changes; ensure only intended files are staged later.
4. If any files were edited after last checks, run quick essential checks (lint/typecheck/test) as appropriate for touched files; note results.
5. Open PR description/body (if exists); ensure it mentions protocol `0003` and current state; edit if missing.
6. Mark PR ready for review (remove draft flag) in the hosting platform UI/CLI.
7. Append final entry to `log.md` summarizing completion, PR readiness, checks run/results, and commit hash placeholder if not yet committed.
8. Update `context.md`: set `Current Step` to `4` or `done`, `Status` to `Complete`, and `Next Action` to "Await review/merge".
9. Stage doc/protocol updates: `git add .protocols/0003-workflow-eval-itsdangerous-1765518181/log.md .protocols/0003-workflow-eval-itsdangerous-1765518181/context.md` (and PR description file if tracked).
10. Commit remaining documentation updates with `chore(protocol): finalize documentation [protocol-0003/04]`; ensure working tree is clean afterward.
11. Push branch; confirm remote status shows PR ready and up to date; verify `main` has no stray files from our branch.
12. Prepare final report to user using required step report format.

## Workflow
1. Execute sub-tasks.
2. Verify: run quick checks only if files were touched since last green run; ensure PR reflects latest commits and is marked ready.
3. Fix/record:
   - Add to `log.md` what/why (final state, PR ready, checks).
   - Update `context.md` to completion state (status complete, next action).
   - Check cleanliness vs `main` and remote push status.
4. Commit: `git add .` then `git commit -m "chore(protocol): finalize documentation [protocol-0003/04]"`. Push and mark PR ready.
5. Report to user using the step report format.
