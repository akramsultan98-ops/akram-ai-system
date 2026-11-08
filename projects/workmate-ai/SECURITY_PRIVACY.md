# Security and Privacy Baseline

## Identity and authorization
- Enforce authorization on the server for every read/write.
- Scope every private query by authenticated user ID.
- Never trust user IDs, roles, plan status, or cost values supplied by the browser.
- Use secure, HTTP-only, SameSite cookies where applicable.
- Rate-limit authentication and AI endpoints.

## AI and prompt injection
- Treat user messages, pasted emails, and retrieved text as untrusted data.
- Keep system prompts and scenario instructions server-side.
- Never let model output grant permissions, modify entitlements, or execute arbitrary tools.
- Validate output schemas and apply length limits.
- Do not send unnecessary identity or profile data to AI providers.

## Sensitive content and retention
- Professional conversations may contain confidential client or employer information.
- Warn users not to paste secrets or confidential third-party data.
- Define retention and deletion rules before beta.
- Provide account/data deletion behavior.
- Avoid retaining raw email source text longer than necessary.
- Do not use user content to train public models.

## Infrastructure
- Isolate application services, database, volumes, secrets, and network from existing Hetzner workloads.
- Keep PostgreSQL private; do not expose its port publicly.
- Use separate credentials per environment.
- Store secrets outside Git and image layers.
- Configure TLS, firewall, backups, log redaction, and restore tests.
- No infrastructure changes during discovery.

## Required pre-launch checks
- Cross-user access tests.
- Session fixation and authentication checks.
- Rate-limit tests.
- Prompt injection tests.
- Data export/deletion tests.
- Log and error redaction review.
- Backup restore rehearsal.
- Dependency and container image review.
