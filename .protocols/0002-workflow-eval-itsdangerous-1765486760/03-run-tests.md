# Step 03: Run tests and fix trivial issues

## Briefing
- **Goal:** Execute test suite (or scoped subset per CI), address trivial failures, and ensure spec validity/QA alignment with minimal changes.
- **Key files:**
  - Test files touched
  - CI configs if adjustments needed for parity
- **Additional info:** Only trivial fixes (e.g., typos, tiny adjustments); avoid scope creep.

## Sub-tasks
1. Identify CI-aligned test entrypoint(s) from `.github/workflows/` or tooling config (pytest/tox/nox); pick the scope that covers the new test and impacted areas first.
2. Mirror CI environment setup (venv activation, dev deps/extras install, env vars) before running tests.
3. Execute the scoped test command; if fast, also run the full CI-equivalent command. Capture command(s) used.
4. For each failure, confirm it is trivial, apply minimal fix (typos, small assertion/import tweaks), and avoid refactors.
5. Re-run the previously failing subset, then the full command to ensure green.
6. Record commands, failures/fixes, and any deviations from CI expectations in `log.md`.

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "feat(scope): subject [protocol-0002/03]"`. Push.
5. Report to user using the step report format above.
