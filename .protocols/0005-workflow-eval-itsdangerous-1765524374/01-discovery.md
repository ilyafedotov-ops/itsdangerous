# Step 01: Discover requirements and baseline

## Briefing
- **Goal:** Understand the QA prompt requirements, current implementation, and test baseline to scope changes.
- **Key files:**
  - `README.rst`
  - `itsdangerous/` package modules relevant to QA prompt
  - `tests/`
- **Additional info:** Identify any existing tooling/config (lint, formatting) to align with.

## Sub-tasks
1. Locate the bundled QA prompt under the protocol folder; read fully and extract acceptance criteria, constraints, and target behaviors into `log.md`.
2. From the QA prompt, list the specific features/APIs implicated and any open questions; capture in `log.md`.
3. Read `README.md` (and any linked quickstart/usage sections) to understand expected usage patterns related to the QA prompt.
4. Identify and skim core modules in `src/itsdangerous/` matching the scoped features (e.g., serializer/signer modules); note current behavior and edge cases in `log.md`.
5. Survey `tests/` for files covering the scoped behavior (use `rg` to find references); record what is already covered and any notable gaps.
6. Inventory tooling/config: check `pyproject.toml` (and other configs if present) for lint/test/typecheck commands; write the go-to commands in `log.md`.
7. If dependencies are missing, install per repo instructions; then run baseline tests from CWD with `python -m pytest` (or documented default). Record pass/fail details in `log.md`.
8. Update `context.md` with a concise findings summary, baseline test result, current step completion, and planned focus for implementation.
9. Keep code untouched in this step; only `log.md` and `context.md` should change.

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "feat(scope): subject [protocol-0005/01]"`. Push.
5. Report to user using the step report format above.
