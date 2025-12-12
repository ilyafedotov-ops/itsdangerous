# Step 0: Prepare and lock the plan

## Briefing
This is a technical step: commit plan files, publish the branch, and open a PR/MR. These actions must be done before reporting to the user.

## Sub-tasks
1. **Create and save** all protocol artifacts (`plan.md`, `context.md`, `log.md`, `00-setup.md`, and all future step files) in `.protocols/0003-workflow-eval-itsdangerous-1765518181/`.
2. **Make the first commit** with these files to branch `0003-workflow-eval-itsdangerous-1765518181` using `feat(protocol): add plan for 0003-workflow-eval-itsdangerous-1765518181 [protocol-0003/00]`.
3. **Create Draft PR/MR** on GitHub or GitLab with title `WIP: 0003 - workflow-eval-itsdangerous-1765518181` and body referencing `.protocols/0003-workflow-eval-itsdangerous-1765518181/`.
4. **Update `context.md`**: set `Current Step` to `1`, `Status` to `In Progress`, update `Next Action` for Step 1.
5. **Save** the updated `context.md` **without committing** (it will be in the next step’s commit).

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` if required by project defaults (none expected here); ensure no unintended changes.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .protocols/0003-workflow-eval-itsdangerous-1765518181` then `git commit -m "feat(protocol): add plan for 0003-workflow-eval-itsdangerous-1765518181 [protocol-0003/00]"`. Push branch and open draft PR/MR.
5. Report to user using the step report format.
