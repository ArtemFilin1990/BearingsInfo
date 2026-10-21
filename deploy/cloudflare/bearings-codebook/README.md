# EVEREST Cloudflare Worker — codebook only (staging)

This separate, not-deployed Worker snapshots 55 manufacturer-scoped code definitions from verified_manufacturer_codes.csv, keeping the source URL and OEM scope. It **does not infer ГОСТ↔ISO product interchangeability**.

- GET /health
- GET /v1/lookup?brand=SKF&code=2RSH
- POST /v1/decode {"brand":"SKF","suffix":"2RSH/C3"}
- POST /v1/compare {"left":{"brand":"NSK","suffix":"DDU"},"right":{"brand":"NTN","suffix":"LLU"}}

Every route returns auto_replace_allowed=false. No customer catalogue, pricing, CRM, 1C, databases, credentials or approval endpoints. Unknown codes and unfamiliar brands trigger review; INA does not inherit FAG suffixes.

Read-only **proof of concept**, not a substitute for PR #187 engineering gate. Cloudflare API connector was unavailable; no changes were made in Cloudflare. The worker has workers_dev:false and no routes; deployment is intentionally prevented without a new explicit route.

Run: node --test test/*.test.mjs

Primary source: data/reference/verified_manufacturer_codes.csv from PR #186. Target branch stacks on PR #188.
Cloudflare docs: https://developers.cloudflare.com/workers/wrangler/configuration/
