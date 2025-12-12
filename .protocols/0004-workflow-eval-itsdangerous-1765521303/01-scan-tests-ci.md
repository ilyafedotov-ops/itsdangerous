# Step 01: Scan tests and CI expectations

## Briefing
- **Goal:** Understand existing tests, fixtures, and CI expectations to align the new unit test with project standards.
- **Key files:**
  - `tests/` (structure, fixtures, markers)
  - `.github/workflows/` (CI matrix, minimum Python versions)
  - `pyproject.toml` / `tox.ini` / `noxfile.py` (if present for local commands)
- **Additional info:** Focus on locating gaps where the missing unit test belongs and note any shared helpers.

## Sub-tasks
1. Snapshot test layout: list top-level entries in `tests/`; map subpackages/modules that look related to the missing test topic; note any naming conventions (e.g., `test_*.py`, class style).
2. Inspect fixtures/helpers: open `tests/conftest.py` plus any helper modules; capture reusable fixtures, factories, and common assertions to align the future test.
3. Trace CI expectations: read `.github/workflows/*.yml` to capture Python versions, matrix dimensions, and commands invoked; note any env vars or optional checks.
4. Identify local tooling: scan `pyproject.toml`, `tox.ini`, and `noxfile.py` (if present) for lint/typecheck/test commands; record preferred local invocation (e.g., `tox -e py`, `pytest`, `nox -s tests`).
5. Summarize placement guidance: decide the best target file/path for the missing test based on steps 1–2; write a one-line rationale to reuse in Step 2.
6. Log and context: add concise notes to `log.md` (paths inspected, commands to run, conventions); update `context.md` with Step 1 completion and next action for Step 2.

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "chore(protocol): record test/CI scan [protocol-0004/01]"`. Push.
5. Report to user using the step report format above.
