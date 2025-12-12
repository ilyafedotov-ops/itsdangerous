(Protocol 0003, Step 1):

**Done**: Mapped tests under `tests/test_itsdangerous/` (encoding, signer, serializer, timed, url_safe; class-level fixtures, partial factories, freezegun, parametrized cases; no `conftest.py`). Reviewed CI workflows/matrix (tox via uv on Py3.10-3.13 + PyPy3.11 with Windows/Mac legs on 3.13, separate typing and pre-commit jobs, plus publish/lock). Chose coverage target for next step: `TimestampSigner.validate` with `max_age` expiration should return `False` on expired signatures (not currently covered). Logged findings in `.protocols/0003-workflow-eval-itsdangerous-1765518181/log.md` and advanced context in `.protocols/0003-workflow-eval-itsdangerous-1765518181/context.md`.

**Checks**: Not run (documentation/log updates only).

**Git**: Draft PR #2; branch `0003-workflow-eval-itsdangerous-1765518181`; commit `chore(protocol): record discovery for tests/ci [protocol-0003/01]`; pushed successfully; working tree clean vs main.

**Working directory**: `/home/ilya/Documents/dev-pipeline/projects/github.com/pallets/itsdangerous/worktrees/tasksgodzilla-worktree`

**Protocol status**: Ready for Step 2 — add the missing unit test around `TimestampSigner.validate` max-age expiration (see `02-add-missing-unit-test.md`).
