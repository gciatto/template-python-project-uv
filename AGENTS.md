# AGENTS.md

Notes for coding agents and contributors. User-facing usage (setup, commands, release
secrets, Renovate) lives in `README.md`; do not duplicate it here.

## Layout

```
src/uv_python_project_template/   the package (renamed by rename-template.sh)
  __init__.py   package code and its logger
  main.py       `main()`, the `[project.scripts]` entry point
test/           pytest unit tests (note: `test/`, not `tests/`)
scripts/        githooks.py: installs/removes local Git hooks (poe install-hooks)
.github/workflows/
  check.yml     static-checks + coverage, then tests on ubuntu/windows/macos x Python 3.10-3.13,
                then deploy.yml
  deploy.yml    semantic-release (dry run off main/master and on the initial commit)
  init.yml      one-shot: renames the template in repos created from it, then deletes itself
```

## Commands

```bash
uv sync                               # env + dev tools
uv run poe test                       # pytest
uv run poe static-checks              # compileall, ruff format --check, ruff check, mypy
uv run poe static-fixes               # ruff --fix + ruff format
uv run poe coverage && uv run poe coverage-report
uv run poe install-hooks [HOOK...]    # local hooks in .git/hooks (default: all)
uv run poe uninstall-hooks [HOOK...]  # removes only hooks it installed
```

Hooks (`scripts/githooks.py`, never tracked): `pre-commit` runs static-checks,
`conventional-commits` rejects non-Conventional-Commit subjects, `no-ai-signature` rejects
AI assistants' signatures (Claude, Codex, Copilot, ... trailers or "Generated with" footers),
`pre-push` runs static-checks + tests. The two message checks share `.git/hooks/commit-msg`,
one tagged line each. Foreign hooks are never overwritten. `--no-verify` skips them once.

## Conventions

- Commits follow Conventional Commits (`<type>[(scope)][!]: <description>`); semantic-release
  derives the next version from them, so pick the type carefully (`feat` = minor, `fix` =
  patch, `!` = major; `chore`/`docs`/`style`/`test`/`ci` don't release).
- No AI-assistant signatures in commit messages or PR descriptions.
- `static-checks` and tests must pass before committing.
- Ruff: line length 100, target py310. Code must run on Python 3.10 (the lowest version in
  the CI matrix and `requires-python`; keep the three in sync).
- Manage dependencies with `uv add` / `uv add --dev`, never by hand-editing `uv.lock`.
- Tests must not hit the network.

## Releases

Conventional Commits drive semantic-release (`release.config.mjs`), which runs
`uv version <next> && uv build`, then `uv publish` (to TestPyPI while the repo name contains
`template`). `pyproject.toml` is the only version source; never bump it by hand.
`CHANGELOG.md` is generated.
