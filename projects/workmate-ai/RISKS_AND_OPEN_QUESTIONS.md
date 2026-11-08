# Risks, Assumptions, and Open Questions

## Verified repository facts
- Existing repository: `akramsultan98-ops/akram-ai-system`.
- Default branch: `main`.
- Repository is public and currently contains operating-system documentation and project folders, not a product application.
- Root `CLAUDE.md` defines global operating rules; it must not be overwritten for this product.
- Existing stack context mentions Hetzner, Ubuntu, Docker, n8n, Claude, and GitHub, but does not verify current capacity or deployment topology.

## Approved decisions
- Initial audience: Sales & Account Managers.
- Multilingual architecture from day one.
- Initial locales: English and Arabic.
- Voice: later; excluded from MVP.
- Hosting direction: existing Hetzner, isolated.
- Product repository boundary: documentation under this repository; application must be independently deployable.

## Assumptions requiring validation
- Next.js + TypeScript + PostgreSQL + Prisma is the preferred application stack.
- Text roleplay can create enough perceived value before voice is available.
- The first five scenarios represent frequent, high-value user situations.
- Users will trust feedback if evidence is shown and style suggestions are separated from errors.

## Critical open decisions
1. Which separate GitHub repository will contain deployable application code, and who creates it?
2. What is the current Hetzner capacity, Docker topology, reverse proxy, DNS, and backup status?
3. Which authentication solution best fits the product and data model?
4. Which AI provider/models meet quality, latency, data-handling, and cost constraints?
5. Which locales beyond English and Arabic are launch priorities?
6. Can Arabic-language roleplay and evaluation meet quality requirements, or should Arabic initially be UI/explanation only?
7. Which payment provider supports an Egypt-based business/founder, payouts, refunds, and tax/compliance needs?
8. What retention period should apply to conversation and email content?

## Main risks and mitigations
- **Generic feedback:** build a human-reviewed evaluation test set and require evidence per correction.
- **False scoring:** label scores as coaching indicators; permit insufficient-evidence results.
- **Weak repeat use:** prioritize daily practice from recurring errors; measure D7/D30 retention.
- **AI cost growth:** bounded sessions, model routing, quotas, usage ledger, and per-user limits.
- **Privacy leakage:** data minimization, server-side authorization, retention/deletion controls, and log redaction.
- **Scope creep:** enforce MVP exclusions and milestone gates.
- **Infrastructure blast radius:** separate deployment resources and no Hetzner changes before inspection.
- **Multilingual quality gaps:** locale-specific QA; do not equate translation availability with coaching quality.

## Founder approvals needed before Milestone 1
- Confirm application repository strategy.
- Approve proposed stack or list constraints.
- Approve first release language behavior, especially Arabic practice vs Arabic explanations.
- Approve Hetzner isolation plan after inventory review.
