# Step 1: Analyze requirements and baseline

## Briefing
- **Goal:** Confirm scope for the end-to-end eval with code-side QA downgrade; understand current QA expectations and relevant code/test areas.
- **Key files:**
  - `README.rst`, `CHANGES.rst`, `CONTRIBUTING.rst` (or similar docs)
  - `setup.cfg`/`pyproject.toml` for tooling
  - `tests/` and `src/itsdangerous/` for current behavior
- **Additional info:** Capture any assumptions about the downgrade and potential risk areas.

## Sub-tasks
1. Review repo docs (README/CONTRIBUTING/CHANGES) for QA/testing standards and project expectations.
   - Open `README.rst`, `CONTRIBUTING.rst`, and `CHANGES.rst` (or equivalents) and note documented QA/testing practices, supported Python versions, and release expectations.
   - Extract any stated requirements for linting, type checking, test coverage, or release criteria and record them as baseline QA expectations.
2. Inspect existing CI/test config (e.g., `pyproject.toml`, `setup.cfg`, GitHub workflows) to understand current QA posture.
   - Locate and read `pyproject.toml`, `setup.cfg`, and any `.github/workflows/*.yml` to enumerate configured linters, type checkers, test runners, and required commands.
   - Note default commands/targets (e.g., `pytest` options, `ruff`/`flake8`, `mypy`/`pyright`) and whether they are gated in CI.
3. Identify code areas likely impacted by QA downgrade; note key modules in `src/itsdangerous/` and related tests in `tests/`.
   - List main modules/packages under `src/itsdangerous/` and their responsibilities; map corresponding test modules in `tests/`.
   - Highlight areas with stricter validation or edge-case handling that could be sensitive to a QA downgrade.
4. Determine the expected downgrade effect (e.g., reduced checks, altered thresholds) and document assumptions.
   - From steps 1–3, articulate what “QA downgrade” likely means here (e.g., fewer linters, relaxed test scope, lower strictness) and any constraints to preserve.
   - Capture explicit assumptions/risks and open questions to carry into implementation.
5. Update `log.md` with findings and decisions; adjust `context.md` for next step preparation.
   - Summarize key findings, assumptions, and risks in `log.md` with references to files reviewed.
   - Set `context.md` to reflect completion of Step 1, identify the next action for Step 2, and note any dependencies or follow-ups.

## Workflow
1. Execute sub-tasks in order, capturing notes as you go.
2. Verify: run `lint`, `typecheck`, `test` if needed to establish a baseline; record commands and results if executed.
3. Fix/record:
   - Add to `log.md` what/why (non-obvious decisions).
   - Update `context.md`: increment `Current Step`, set `Next Action`.
   - Check `main` for stray files from our branch.
4. Commit: `git add .` then `git commit -m "feat(protocol): analysis notes [protocol-0006/01]"`. Push.
5. Report to user using the step report format above.
