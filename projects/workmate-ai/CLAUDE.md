# WORKMATE AI — Claude Code Project Rules

## Project identity
WORKMATE AI is a focused AI coach for professional communication, initially serving Sales & Account Managers and adjacent client-facing roles.

Read these before proposing implementation:
- `README.md`
- `PRODUCT_BRIEF.md`
- `MVP_SCOPE.md`
- `ARCHITECTURE.md`
- `DATA_MODEL.md`
- `AI_SYSTEM_DESIGN.md`
- `LOCALIZATION.md`
- `SECURITY_PRIVACY.md`
- `ROADMAP.md`
- `RISKS_AND_OPEN_QUESTIONS.md`

## Non-negotiable decisions
- Text-first MVP. Voice is explicitly deferred.
- Multilingual architecture from day one; English and Arabic are the first supported locales.
- The user can independently select interface language, native/explanation language, and practice language.
- Arabic must support correct RTL layout.
- Initial audience is Sales & Account Managers, not all language learners.
- Build a modular monolith; no microservices or Kubernetes.
- Hetzner is the hosting direction, but no server changes or deployment until the existing environment is inspected and approved.
- Keep the product app separately deployable. This repository is an AI operating-system/knowledge repository, not automatically the application root.
- Never commit secrets, API keys, live customer messages, or credentials.

## Engineering rules
- Inspect before editing. Do not assume a framework, package manager, database, deployment topology, or installed service.
- Distinguish verified facts, assumptions, and proposed decisions.
- Do not expand MVP scope without explicit founder approval.
- Do not claim a feature is implemented unless code and tests prove it.
- Validate all AI outputs against schemas. Treat model output as untrusted input.
- Enforce authenticated user ownership server-side for every private record.
- Keep prompts versioned and testable.
- Track token usage and estimated cost for every AI operation.
- Prefer simple, reversible changes. Never perform destructive infrastructure or database operations without explicit approval.
- Before implementation, present the plan and affected files. After implementation, run relevant checks and report exact results.
- Do not add voice capture, speech-to-text, text-to-speech, live meeting assistance, or video avatars to the MVP.

## Milestone 0 mode
Discovery and documentation only. Do not generate application code, install dependencies, provision services, change DNS, alter firewall rules, modify Docker stacks, or deploy.
