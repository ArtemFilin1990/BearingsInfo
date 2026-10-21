# BRI — GitHub Actions runner diagnosis and FastAPI Docker validation
Date: 2026-10-21. Source: authenticated GitHub API + Render deployment/log API.

## GitHub Actions — BLOCKED BEFORE RUNNER STEPS

- Repository: public `ArtemFilin1990/BearingsInfo`; canonical default branch: `main`.
- Minimal `.github/workflows/runner-diagnostic.yml` runs on `ubuntu-24.04`. It requires no checkout, no dependencies, no Docker, no Python project code, and no repository secrets.
- Test run: https://github.com/ArtemFilin1990/BearingsInfo/actions/runs/39523854061
- Diagnostic job ID: `118973818734`; API returned `conclusion=failure`, `steps=null`, `logs_url=null`.
- The rerun API succeeded in accepting a retry; attempt 2 also concluded `failure`, before runner steps.
- Other Python/validation workflows display the same 2–3 second failure and empty steps.
- GitHub check-runs recorded two annotations per failed job but this connected GitHub API cannot read the annotation URLs. **Specific platform error text is unverified**. Do not assert a billing issue without reading those annotations.

## Required GitHub owner action

1. Open the diagnostic run above and inspect the **two annotations** on `runner-diagnostic` (not just the empty job logs). Record the exact message.
2. Check repository Settings → Actions → General: workflow permissions, allowed Actions, policy to use GitHub-hosted standard runners.
3. Check personal GitHub Settings → Billing and licensing → Actions budgets/spending limits, payment holds and account restrictions. This repository is public, so standard GitHub-hosted Linux runners are normally free; account-level billing/entitlement problems are nevertheless possible.
4. If UI shows runner-start billing/entitlement denial despite valid settings, open a GitHub Support ticket referencing the diagnostic URL and job ID. Do not authorize a paid runner or higher spending limit as a workaround without explicit approval.
5. After restoring runner allocation, rerun the diagnostic and `Bearings API Runtime Smoke`, then review existing CI, pytest/coverage, Ruff/Black, Mypy, pip-audit and Docker tests at the **same commit SHA**.
6. Only after required checks are green should PR #190 and the stacked PR #191 be considered for merge. Branch protection/admin controls were not changed by these PRs.

GitHub's public status page lists Actions as operational at review time; a historical Oct 19 outage has been resolved. This does not determine whether the individual account is restricted.

## Docker startup — VALIDATED ON REAL RENDER BUILDS

### Staging API-only Dockerfile
- Dockerfile: `deploy/docker/Dockerfile.api`.
- Workspace: Артем; plan: `free`; branch: `fix/everest-fastapi-docker-health-20261021`.
- Render service: https://dashboard.render.com/web/srv-dbc0pem1egvs73935510
- Deploy `dep-dbc0scrbc2fs73asi210`: `live`.
- Logs show: Uvicorn starts on 0.0.0.0:10000, application startup complete, GET / returns 200. No databases were modified.

### Root Dockerfile (the original broken container)
- Dockerfile: `Dockerfile`.
- Render service: https://dashboard.render.com/web/srv-dbc0sfe1egvs7393fji0
- Deploy `dep-dbc0sge1egvs7393fnm0`: `live`.
- Logs show: Uvicorn on 0.0.0.0:10000, application startup complete, GET / returns 200.
- Startup changed from `CMD ["python", "manage.py"]` (which exited code 1 without a subcommand) to proper FastAPI ASGI `uvicorn main:app --app-dir src/api`.
- Docker Compose uses the root Dockerfile command, publishes 8000:8000, and no longer mounts nonexistent `./scripts`.

### API safety
- `BEARINGS_CORS_ORIGINS` allows only explicit browser origins; no wildcard plus credentialed requests.
- `/analogs/{bearing_code}/export` returns 503 and `auto_replace_allowed=false` until the engineering approval backend is connected; the previous invented `compatibility=100%` record is removed.
- Staging data indices `data/autocomplete_dict.json` and `data/document_index.json` were **not seeded**. Logs confirm at least the autocomplete index missing. The health route checks that the web process starts, not whether the catalog search is fully populated.
- The new Python smoke regression tests and GitHub Docker workflow are committed but **not executed by GitHub Actions** because runner dispatch is blocked. Do not report their success.
- GitHub Actions validation/build, branch protection, dependency audit and full search-index readiness remain separate acceptance criteria.

## Scope and safety

- Neither default branch nor running Goodwin, 1C, Bitrix24 or Cloudflare D1 was changed.
- Both Render staging services have auto-deploy disabled. They are separate from production and consume free-tier resources.
- PR #191 is stacked on PR #190; both remain draft pending genuine CI execution and review.
