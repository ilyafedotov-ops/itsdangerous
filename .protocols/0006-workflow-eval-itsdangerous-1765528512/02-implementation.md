# Step 2: Apply code-side QA downgrade changes

## Briefing
- **Goal:** Implement required code or configuration changes reflecting the QA downgrade while keeping behavior intentional and documented.
- **Key files:**
  - `src/itsdangerous/` modules impacted by downgrade
  - `tests/` for adjusting expectations or coverage
  - Tooling configs (`pyproject.toml`/`setup.cfg`, CI workflows) if QA settings change
- **Additional info:** Keep changes minimal and reversible; ensure documentation reflects any reduced guarantees.

## Sub-tasks
1. Re-read Step 1 outputs (analysis notes, `context.md`, any backlog items) to confirm which behaviors/guarantees are being downgraded, which modules are in scope, and the acceptance criteria for this step.
2. Implement code/config changes for the downgrade:
   - Enumerate impacted areas in `src/itsdangerous/` and adjust logic to relax validations or guarantees per Step 1 findings.
   - If QA settings rely on tooling (linters/type-checkers/CI thresholds), tune the relevant config files to match the downgraded expectations.
   - Keep a concise change log (working notes) mapping each downgrade decision to the files touched.
3. Update or add tests in `tests/` to align with the downgraded behavior:
   - Modify assertions/fixtures to reflect the new expectations; remove/mark overly strict tests (xfail/skip) only where justified.
   - Add coverage for the downgraded paths to document intended behavior boundaries.
4. Adjust documentation/comments to note the downgraded QA scope when user-facing or developer-facing behavior changes:
   - Update `README`, `CHANGES`/`CHANGELOG`, or inline docstrings/comments where the downgrade affects guarantees or guidance.
5. Run targeted checks and stabilize:
   - Use project-standard commands for `lint`, `typecheck`, and `pytest` (consult `pyproject.toml`/CI configs for the canonical invocations).
   - Fix failures; rerun until green. Capture any known residual issues with rationale.
6. Finalize step artifacts:
   - Update `log.md` with what changed and why (cite files/decisions); update `context.md` for the next step.
   - Ensure no stray files under `main`; stage and commit with the prescribed message; push if required.

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test`; fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "feat(protocol): apply QA downgrade changes [protocol-0006/02]"`. Push.
5. Report to user using the step report format above.
