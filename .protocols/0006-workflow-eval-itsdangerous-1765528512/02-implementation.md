QA downgrade applied: pyproject now treats warnings as non-fatal and lightens typing gates (non-strict mypy, basic pyright, dropped verifytypes) in `pyproject.toml`; added `tests/test_itsdangerous/test_warnings.py` to codify warning tolerance; documented the relaxed QA posture in `CHANGES.rst`; protocol state/log updated in `.protocols/0006-workflow-eval-itsdangerous-1765528512/{log.md,context.md,quality-report.md}`.

**Checks**
- `uv run --locked tox run -e style` (pass)
- `uv run --locked tox run -e typing` (pass)
- `uv run --locked tox run -e py3.13` (pass)

**Git**
- Draft PR #5, branch `0006-workflow-eval-itsdangerous-1765528512`.
- Commit `dc17a50` `feat(protocol): apply QA downgrade changes [protocol-0006/02]` pushed.
- Working tree clean.

**Working directory**
- `/home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree`

**Protocol status**
- Step 2 complete; ready to start Step 3 (`03-validation.md`) for validation and documentation.
