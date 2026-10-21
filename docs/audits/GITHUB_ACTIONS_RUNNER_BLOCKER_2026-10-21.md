# GitHub Actions: hosted-runner provisioning blocker — 2026-10-21

## Confirmed independent of application code

Repository: `ArtemFilin1990/BearingsInfo`, public; canonical default branch `main`.

Diagnostic workflow: `.github/workflows/runner-diagnostic.yml`. One ubuntu-24.04 job, one shell command (`echo`, `python --version`, `git --version`), no checkout, dependencies, environment secrets, or deployment.

- Run: https://github.com/ArtemFilin1990/BearingsInfo/actions/runs/39523854061
- Run ID: `39523854061`
- First job ID: `118973818734`; rerun job ID: `118976239519`.
- Result: `failure` within seconds, `steps=null`, `logs_url=null`; rerun also fails before starting.
- Job log fetch resulted in 404 `BlobNotFound`; there is no evidence that a Python step executed.
- Many unrelated jobs (Articles validation, JSON lint, Python matrix, and this minimal diagnostic) fail within a few seconds with empty steps at the same time.
- This **does not prove billing is the cause**. Public repositories should have free standard GitHub-hosted runner minutes; account-level controls, policy/abuse restrictions or provisioning faults remain possible.
- GitHub App lacks access to the required settings endpoints and run annotations. The exact account-side denial message remains unknown.

## Required manual account-side verification (no payment changes without owner consent)

1. Open https://github.com/ArtemFilin1990/BearingsInfo/settings/actions → General. Verify **Allow all actions and reusable workflows** (or an equivalent authorized allowlist), runner restrictions, and permission to use standard GitHub-hosted runners.
2. In the account which owns the repository (ArtemFilin1990), open **Settings → Billing & licensing** and check GitHub Actions usage, payment holds, spending limits and budgets. The repository is public; normal standard-hosted runner usage is free, so an account error would need investigation.
3. Check https://www.githubstatus.com/ for an ongoing runner incident.
4. Inspect https://github.com/ArtemFilin1990/BearingsInfo/actions/runs/39523854061 for a job-level red banner or failure annotation such as billing/runner allocation; copy its exact text.
5. If these settings are normal, contact GitHub Support: https://support.github.com/contact with Run ID, Job ID, timestamps, `steps=null` and log `BlobNotFound`. Request investigation of hosted-runner provisioning/account entitlements. Support may need internal runner telemetry.
6. Only after the minimal `runner-diagnostic` reaches an actual `Runner allocated` step, require it to pass and then fix any real Python/quality failures in CI on the same SHA. Do not weaken tests to hide this infrastructure failure.

## Verified alternative build checks

Separate Render staging Docker on commit `82529878e4a52516f2e0e9280f6dfdfd7a2b8e18` executed six FastAPI route/CORS/analogue regression tests **during Docker build**: `6 passed, 1 warning` and image deployed `live`, deploy `dep-dbc1bdcs728c73dl8b4g`.

- https://dashboard.render.com/web/srv-dbc0pem1egvs73935510
- https://everest-bearings-fastapi-smoke-20261021.onrender.com/

Root Dockerfile also built and deployed `live` previously, deploy `dep-dbc0sge1egvs7393fnm0`:
- https://dashboard.render.com/web/srv-dbc0sfe1egvs7393fji0

**Render verification does not replace successful GitHub Actions required checks and does not authorize merging PR #190/#191.** Production Goodwin, 1C, Bitrix24, Cloudflare D1 unchanged.
