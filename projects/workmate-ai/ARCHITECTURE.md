# Proposed Technical Architecture

## Status
Proposed architecture for founder review. No framework or infrastructure has been verified for the application itself.

## Deployment boundary
The existing `akram-ai-system` repository is a knowledge/operating-system repository. WORKMATE AI product specifications live under `projects/workmate-ai/`. The deployable application should be a separate repository or an explicitly approved isolated application directory with its own deployment lifecycle. Do not deploy this documentation repository as the product.

## Proposed stack
- Next.js App Router + TypeScript.
- PostgreSQL.
- Prisma ORM.
- Tailwind CSS and shadcn/ui, subject to design review.
- Authentication solution selected after evaluating session security and deployment constraints.
- AI provider adapter so model/provider can change without rewriting product domains.
- Structured validation (e.g. Zod) at all external boundaries.
- Docker-based deployment on isolated Hetzner resources.
- Managed or self-hosted analytics/error monitoring selected after privacy and cost review.

## Logical modules
1. Identity and account.
2. User profile and preferences.
3. Localization.
4. Scenario catalog and versioning.
5. Roleplay sessions and messages.
6. Evaluation.
7. Mistake Bank.
8. Communication DNA.
9. Daily practice.
10. Email coaching.
11. Subscription entitlements and usage ledger.
12. Analytics and operational telemetry.

## Request flow
Browser → Next.js server boundary → authorization and validation → domain service → AI provider adapter (when needed) → schema validation → persistence → response.

AI output is never trusted directly for authorization, billing, ownership, or database mutation.

## AI operation separation
- Roleplay responder: produces the next counterpart turn.
- Evaluator: analyzes a completed or checkpointed conversation.
- Profile updater: converts validated evaluation evidence into structured signals.
- Exercise generator: creates targeted practice from validated signals.
- Email coach: rewrites while preserving intent and facts.

## Operational principles
- Modular monolith; no microservices.
- No Kubernetes.
- No Redis/queue until a measured requirement exists.
- Short bounded sessions and explicit context windows.
- Persist structured profile signals rather than replaying full chat histories.
- Rate limits, quotas, timeouts, retries with limits, and idempotency for billable operations.
- Separate secrets and environment variables per environment.
- Separate database/schema, service identity, volumes, and network exposure from unrelated Hetzner projects.
- No public database port.
- Backups and restore tests before production data.

## Decisions still required
- Exact application repository strategy.
- Existing Hetzner resource allocation and reverse-proxy conventions.
- Authentication provider.
- AI provider/model choices and fallback policy.
- Payment provider for an Egypt-based founder.
- Email delivery provider.
- Monitoring and analytics tools.
