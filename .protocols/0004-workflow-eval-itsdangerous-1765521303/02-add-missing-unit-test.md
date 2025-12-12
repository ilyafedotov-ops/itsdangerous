(Protocol, step): 0004-workflow-eval-itsdangerous-1765521303, Step 2

**Done**: Added `tests/test_itsdangerous/test_url_safe.py:22` regression that feeds a fake compressed payload (`.` prefix + base64 of non-zlib data) and asserts `URLSafeSerializer.load_payload` raises `BadPayload` with an `original_error`, covering the decompress error path.

**Checks**: `uv run python -m pytest tests/test_itsdangerous/test_url_safe.py::TestURLSafeSerializer::test_load_payload_bad_compressed_data` ✓; `uv run tox -e style` ✓; `uv run tox -e typing` ✓; `uv run tox -e py3.13` ✓.

**Git**: Draft PR #3; branch `0004-workflow-eval-itsdangerous-1765521303`; commit `test: add coverage for missing case [protocol-0004/02]` (2b5b5db) pushed. Main worktree still only shows pre-existing untracked items (`.github/workflows/ci.yml`, `.gitlab-ci.yml`, `docs/ci.md`, `docs/tasksgodzilla.md`, `prompts/`, `schemas/`, `scripts/`, `worktrees/`).

**Working directory**: /home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree

**Protocol status**: Step 2 complete; ready to start Step 3 (03-run-tests-fix.md) to rerun the matrix and handle any trivial breakages.
