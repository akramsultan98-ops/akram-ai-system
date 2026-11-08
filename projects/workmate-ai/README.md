# WORKMATE AI

**Status:** Milestone 0 — Discovery  
**Product type:** Global consumer SaaS / AI professional communication coach  
**Initial audience:** Sales & Account Managers  
**Initial interface and practice languages:** English and Arabic  
**Voice:** Deferred; architecture must allow it later  
**Hosting direction:** Existing Hetzner VPS, isolated deployment

## Purpose
WORKMATE AI helps client-facing professionals improve communication through realistic business roleplay, evidence-based feedback, a persistent mistake bank, and personalized practice.

## Repository boundary
This folder is the product's source-of-truth for product decisions, architecture, specifications, prompts, and delivery planning inside the Akram AI System repository. It is not the deployable application root. Application source must remain independently deployable and must not be mixed into the root operating-system repository without an explicit architecture decision.

## Current MVP
1. Onboarding and communication goals.
2. Text-based roleplay for five sales/account-management scenarios.
3. Structured post-session feedback.
4. Personal Mistake Bank.
5. Evidence-backed Communication DNA.
6. Short personalized daily practice.
7. Professional Email Coach.
8. Basic progress view and usage metering.

## Milestones
- [x] Repository and project boundary inspected.
- [x] Discovery branch created.
- [ ] Founder review of discovery documents.
- [ ] Milestone 1 implementation plan approved.
- [ ] Application repository and deployment boundary finalized.

## Key documents
- `CLAUDE.md` — project-specific instructions for Claude Code.
- `PRODUCT_BRIEF.md` — product proposition and target audience.
- `MVP_SCOPE.md` — explicit in/out scope and acceptance criteria.
- `ARCHITECTURE.md` — proposed system architecture.
- `DATA_MODEL.md` — conceptual database model.
- `AI_SYSTEM_DESIGN.md` — roleplay, evaluation, and memory design.
- `LOCALIZATION.md` — multilingual and RTL requirements.
- `SECURITY_PRIVACY.md` — security and privacy baseline.
- `ROADMAP.md` — staged execution plan.
- `RISKS_AND_OPEN_QUESTIONS.md` — assumptions, risks, and unresolved decisions.
