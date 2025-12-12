# Step 2: Add missing unit test

## Briefing
- **Goal:** Implement the chosen missing unit test(s) with alignment to existing style and fixtures.
- **Key files:**
  - Target source module(s) under `src/itsdangerous/`
  - Target test file(s) under `tests/` (create/update as needed)
  - Supporting helpers/fixtures if required
- **Additional info:** Keep scope small and focused; adhere to project testing conventions.

## Sub-tasks
1. Re-read `context.md` and prior step notes to confirm the exact gap to cover (module, function/method, edge case) and identify the intended target test file.
2. Inspect the target source and existing related tests to document expected behavior, inputs/outputs, and boundary conditions; note any shared fixtures or helpers to reuse.
3. Decide placement: extend the existing test module if style matches; otherwise create a small new test module in `tests/` following naming and import patterns.
4. Implement the new unit test(s) with deterministic data; keep assertions specific; use existing fixtures/helpers; prefer parametrization over duplication when appropriate.
5. If the test needs setup support, add minimal/localized fixture or helper updates (no broad refactors); keep changes confined to the affected test module.
6. Ensure code style/format aligns with project conventions (imports order, naming, docstrings if used).
7. Run focused tests for the touched area: `pytest tests/<path-to-target>`; iterate until the new test passes.
8. Re-run the focused test after any fixes; ensure no unintended warnings/regressions.
9. Update `.protocols/.../log.md` describing the new test, the coverage gap it addresses, and key decisions.
10. Update `.protocols/.../context.md`: set `Current Step` to `3`, `Status` to `In Progress`, and record the `Next Action` for Step 3 with a brief summary.

## Workflow
1. Execute sub-tasks.
2. Verify: run focused `pytest` for touched areas; add lint/format if project demands (e.g., `ruff`, `flake8`, `black` if configured).
3. Fix/record:
   - Add to `log.md` what/why (test rationale and design choices).
   - Update `context.md` for next step.
   - Check cleanliness vs `main` (only intended updates).
4. Commit: `git add .` then `git commit -m "test: add coverage for <area> [protocol-0003/02]"` (replace `<area>` with specific target). Push.
5. Report to user using the step report format.
