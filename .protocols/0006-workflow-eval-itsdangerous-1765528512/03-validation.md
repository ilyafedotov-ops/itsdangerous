# Step 3: Validate, test, and document

## Briefing
- **Goal:** Ensure the downgraded QA changes are validated with appropriate tests/checks and documented outcomes.
- **Key files:**
  - Test reports/logs
  - `log.md`, `context.md`
  - Any updated documentation files
- **Additional info:** Capture evidence of checks; note any residual risks or follow-ups.

## Sub-tasks
1. Confirm `context.md` shows this step as current; skim prior `log.md` entry to understand scope and expectations.
2. Identify the concrete commands for this repo’s `lint`, `typecheck`, and `test`/`pytest` (or tox equivalent); note any required env vars or virtualenv activation.
3. Run `lint` with full output captured (copy key pass/fail details for later logging).
4. Run `typecheck` with full output captured.
5. Run `test`/`pytest` (full or scoped as appropriate) with output captured.
6. For any failure: inspect error, apply minimal fix, and rerun the specific suite until green or clearly blocked; document residual failures with reasons.
7. Summarize validation outcomes (pass/fail, scope, notable fixes, residual risks) in `log.md` and reference the commit hash you intend to ship.
8. Update `context.md` with current status/results and set the next action to Step 4 (finalization).
9. Ensure working tree is clean, stage relevant files, and prepare the commit with the prescribed message; verify the branch is ready to push.

## Workflow
1. Execute sub-tasks in order (prep → commands → lint/typecheck/test → fixes → docs).
2. Verify: run `lint`, `typecheck`, `test`; fix failures or document why blocked.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "chore(protocol): validation results [protocol-0006/03]"`. Push.
5. Report to user using the step report format above.
