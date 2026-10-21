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
