# Step 02: Implement workflow evaluation adjustments

## Briefing
- **Goal:** Apply code/config/test changes required by the QA prompt to satisfy the evaluation.
- **Key files:**
  - `itsdangerous/` modules impacted by QA requirements
  - `tests/` for new or updated cases
  - Any config files for tooling (e.g., `pyproject.toml`, `setup.cfg`)
- **Additional info:** Favor minimal, well-tested changes aligned with project style.

## Sub-tasks
1. Re-read the QA prompt and notes from Step 01; enumerate explicit behavior changes/edge cases required for this repo.
2. Draft planned edits in `log.md` (requirements → files/functions/tests/config) before touching code; note any open questions.
3. For each required behavior, adjust implementation under `itsdangerous/` (small commits per concern); annotate major decisions in `log.md`.
4. Add/update tests under `tests/` to cover positive/negative/boundary cases for each change; mirror existing test style/fixtures.
5. Update tooling/config files only if needed to run/tests/lint (e.g., `pyproject.toml`, `setup.cfg`, CI configs); log rationale.
6. Run targeted checks locally: relevant focused tests first, then `python -m pytest`; include any lint/typecheck command identified in Step 01.
7. Fix failures and re-run checks until green; capture notable fixes or trade-offs in `log.md`.
8. Update `context.md` with current progress, mark Step 02 completion, and set `Next Action` pointing to validation (Step 03).

## Workflow
1. Execute sub-tasks.
2. Verify: run `lint`, `typecheck`, `test` (scope as needed). Fix failures.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "feat(scope): subject [protocol-0005/02]"`. Push.
5. Report to user using the step report format above.
