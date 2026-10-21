# EVEREST BearingsInfo API runtime smoke

The root Dockerfile is still intended for the data-management CLI and must not be treated as the FastAPI server. This isolated Dockerfile starts the actual ASGI application.

Build and run locally (from repository root):

```bash
docker build -f deploy/docker/Dockerfile.api -t everest-bearings-api:staging .
docker run --rm -p 10000:10000 -e PORT=10000 everest-bearings-api:staging
curl --fail http://127.0.0.1:10000/health
```

Public API has no OEM indices or verified analogue approvals unless data is loaded by a separate reviewed workflow. `/analogs/{code}/export` currently returns 503 to prevent invented 100% compatibility.

CORS is same-origin by default. `BEARINGS_CORS_ORIGINS` is a comma-separated explicit allowlist of allowed browser origins; wildcard `*` is rejected.

This Dockerfile does not require PostgreSQL credentials, Bitrix24, 1C or Cloudflare tokens. It runs as non-root user 10001. Health response is `{"status":"healthy"}`.

GitHub Actions diagnostic: `.github/workflows/runner-diagnostic.yml` has no checkout and no package install. If that workflow completes in 2–3 seconds without job steps or logs, troubleshoot Actions runner scheduling/billing/repository settings rather than altering Python tests.

App code: `src/api/main.py`, `src/api/app/api.py`. This is FastAPI, not Django.

## Isolated read-only nomenclature lookup for Hermes / Goodwin

`Dockerfile.catalog-readonly` offers a separate, **private staging** API without
depending on GitHub Actions, PostgreSQL, Supabase, external cron jobs or paid
resources. During `docker build` it runs the normalizer's regression tests,
materializes the full 42,585-row / 74-brand SQLite snapshot and refuses a
duplicate-containing or promoted snapshot. Nothing is imported into production.

From the repository root:

```bash
python -m unittest discover -s tools/scripts/everest_catalog -p 'test_*.py' -v
docker build -f deploy/docker/Dockerfile.catalog-readonly -t everest-catalog-readonly .
```

Configure `CATALOG_API_TOKEN` in the **Render Environment** for a new, isolated
Docker web service (minimum 32 random characters). Do not commit or paste it
into chat. Do **not** point a production service at this Dockerfile without a
separate rollout review. The service fails to start without the token and runs
as non-root. Its Docker context is the repository root; the Dockerfile path is
`deploy/docker/Dockerfile.catalog-readonly`.

Routes:

| Route | Authentication | Response |
|---|---|---|
| `GET /health` | none | Liveness only |
| `GET /v1/staging/status` | `Authorization: Bearer <token>` | Row/brand counts, source blob SHA, ruleset, `ALL_UNVERIFIED` |
| `GET /v1/staging/search?q=ШС12&limit=20&brand=SKF` | `Authorization: Bearer <token>` | Prefix/exact matching; 1–50 rows; no prices or unapproved analogue fields |

Hermes may use the search response only to say that a designation **appears
in the unverified source**. It must never present it as an authenticated
technical specification, interchangeable bearing, stock availability or a
customer-ready selling price. Official catalog verification and commercial
pricing must be built as separately authorized services with independently
fresh data. Never expose this internal bearer token to end-user clients.

There is no automatic schedule here: a **new container build** refreshes the
staging snapshot after the source CSV is updated. This avoids GitHub Actions
without creating a paid Render Cron Job. The image can be tested on an isolated
service first; the existing BearingsInfo FastAPI and Hermes deployments remain
untouched.
