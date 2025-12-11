# Step 01: Scan repo tests and CI

## Briefing
- **Goal:** Understand existing tests/CI and identify one obvious small missing unit test to add.
- **Key files:**
  - `tests/` (or equivalent test directories)
  - `.github/workflows/` and other CI configs
  - `pyproject.toml`, `setup.cfg`, `tox.ini`, `noxfile.py` (if present)
- **Additional info:** Keep notes on gaps; prefer minimal scope test addition.

## Sub-tasks
1. Map tests:
   - List top-level files/dirs under `tests/` to understand suite layout.
   - Open representative test modules and fixtures/helpers to see patterns (naming, parametrization, markers).
   - Note any helper utilities or common base classes used across tests.
2. Inspect test commands:
   - Check `pyproject.toml`, `setup.cfg`, `tox.ini`, `noxfile.py` for configured test/lint/typecheck commands and dependencies.
   - Identify default test entry points (e.g., `pytest`, `tox -e test`, `nox -s tests`) and options/markers used.
3. Review CI workflows:
   - Read `.github/workflows/*` to see which jobs run tests/lint/typecheck and any env matrices or special flags.
   - Note Python versions, optional dependencies, and caching or env setup relevant to running locally.
4. Spot a missing test:
   - From the observed patterns, find one small edge/negative/boundary case not currently covered that fits existing structure.
   - Confirm the target code path and minimal fixture/helper reuse.
5. Record decision:
   - Write down the chosen test target, expected behavior, and rationale to reuse later in `log.md`.

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "feat(scope): subject [protocol-0002/01]"`. Push.
5. Report to user using the step report format above.
