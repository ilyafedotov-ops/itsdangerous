# Step 03: Validate and document results

## Briefing
- **Goal:** Ensure all changes meet QA requirements with full validation and documentation.
- **Key files:**
  - `tests/`
  - `log.md`
  - `context.md`
- **Additional info:** Capture test outputs and any known limitations.

## Sub-tasks
1. Ensure dev deps ready: from CWD, install extras if needed (`python -m pip install -e .[dev]`).
2. Run static checks if configured (e.g., `ruff check`, `python -m mypy`); capture pass/fail notes.
3. Run full test suite from CWD: `python -m pytest`; note command, env, versions, and failures.
4. If any check/test fails: debug, patch code/tests, rerun affected checks until green.
5. Record validation summary in `log.md`: commands run, outcomes, versions, notable decisions/limitations.
6. Update `context.md`: mark Step 03 complete, set next step to finalize, include pending follow-ups if any.

## Workflow
1. Execute sub-tasks in order; rerun failing checks after fixes.
2. Verify: confirm lint/typecheck/test are green; ensure `git status` clean aside from intentional changes.
3. Fix/record:
   - Append to `log.md` what/why, including outputs or summaries.
   - Update `context.md`: set `Current Step` to 04, `Next Action` to finalize/report.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "chore(scope): validation results [protocol-0005/03]"`. Push if applicable.
5. Report to user using the step report format above.
