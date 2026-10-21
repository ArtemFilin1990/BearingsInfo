# BearingsInfo: factual CI and deployment audit — 2026-10-21

Source: GitHub API inspection of `ArtemFilin1990/BearingsInfo` at `main` HEAD `af9368cae30af8083d0683d96c7d4bf02497c864`.
This report distinguishes GitHub API evidence from unexecuted checks.

## Verified facts

- GitHub REST repository metadata: `default_branch=main`; `master` absent from branch list, and REST `contents/...ref=master` returned HTTP 404. **BRI-001 main-vs-master divergence is not reproduced**. No branch switch proposed.
- `manage.py` is a custom data-management CLI with `validate/extract/normalize/test/report/sources/help` subcommands, **not Django's manage.py**. Root requirements declare FastAPI and Uvicorn. **Do not run `manage.py check --deploy`**: it is not a Django application.
- `src/api/app/api.py` defines a FastAPI app and `src/api/main.py` includes an API router. Its launch paths and imports should be tested in runtime.
- Root Dockerfile uses a non-root `appuser` (contrary to potential root-container inference), but its default `CMD ["python","manage.py"]` has no CLI argument, so `manage.py` returns exit 1. `docker-compose.yml` uses the same default command plus restart unless-stopped. **Confirmed boot contract defect; fix in a separate service-runtime PR.**
- `src/api/main.py` configures `allow_origins=["*"]` and `allow_credentials=True`. Review allowed origins for the actual externally exposed API, and add CORS regression tests.
- `.github/workflows/ci.yml` ran scripts that rewrite `data/nomenclature.csv` before validating duplicates, potentially masking source errors.
- `.github/workflows/pr-checks.yml` contained `mypy ... || true`, a read/write deduplication command, and an unconditional comment containing a green checkmark even when a job failed.
- `.github/workflows/security.yml` used `pip-audit ... || true` for both audit invocations, making known-vulnerability reports non-blocking.
- `.github/workflows/seed-database.yml` automatically ran on `main` pushes to `data/**`, executing remote Cloudflare D1 writes; original checkout explicitly referenced `main` rather than the checked run's SHA. Fixed only in the PR.
- `.github/workflows/release.yml` builds data archive from `data/ schemas/`; repository root has no `schemas/` directory (it has `data/schemas/`). Requires a scoped release-fix PR.
- GitHub repository size metadata: `466412` KB; this is not an exact measured .git clone size.
- GitHub Actions on latest main SHA showed failed `CI` and `Articles structure validation` runs. Runner logs were not obtained. Do not infer test failures from status alone.
- Branch protection fetch returned HTTP 403 for this GitHub App and rulesets list returned `[]`. Required-check enforcement **not independently verified**, regardless of branch list metadata.

## Scope of this safety PR

1. CI no longer normalizes or deduplicates checked source data. Existing duplicate-key validation is retained; pip environment is checked.
2. PR validation no longer rewrites data or ignores Mypy failures; misleading green comments removed; token permissions reduced to `contents:read`.
3. One dependency vulnerability audit call now returns non-zero on findings, rather than silently passing.
4. Cloudflare D1 seed changes to **manual-only**, defaults to **dry-run**, and requires **explicit `confirm_remote_write=true` together with `dry_run=false`** for a remote operation. The previously hard-coded checkout of `main` is removed.
5. `tests/test_ci_workflow_guards.py` verifies these safety invariants.

No merge, remote database write, API deploy, branch switch, DNS changes or production change is authorized by this PR.

## Follow-up tasks (separate PRs)

- **BRI-DEPLOY-01 / P0:** Fix container startup for the validated FastAPI entrypoint; test `/health`, Docker build/run, SIGTERM and non-root runtime; define secrets and indexes; review CORS.
- **BRI-RELEASE-01 / P1:** Fix `schemas/` archive path in release workflow, test generated archives and tag/SHA provenance. Verify actual Pages settings with repository admin; do not delete any static workflow without evidence.
- **BRI-CI-02 / P0:** Obtain failing CI logs; establish baseline for unit tests, Ruff/Black/Mypy/coverage/security; scope and measure required checks on `main`. Implement branch protection manually with authorized repository admin.
- **BRI-DATA-01 / P0:** Review every mutating script, D1 schema, backup/restore, idempotent seed and provenance. New analogues should be candidates, never confirmed from unreviewed secondary sources.
- **BRI-DEPS-01 / P1:** Pin resolved dependencies using one documented resolver; run `pip-audit`, `pip check` and compatibility tests without asserting unsupported CVEs.
- **BRI-SIZE-01 / P1:** Identify historical large blobs before any migration to LFS/R2; do not rewrite history by default.

## Evidence limitations

This session could inspect the GitHub tree/files/workflows using an authenticated GitHub connector. A separate `git ls-remote` in the container failed due to environment DNS resolution; full repo checkout, complete coverage, Mypy, pip-audit, Docker build and complete workflows were **not executed** for this audit. Code-level conclusions above follow inspected source text, not hypothetical execution.
