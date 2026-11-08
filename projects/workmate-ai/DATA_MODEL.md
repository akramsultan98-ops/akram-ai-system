# Conceptual Data Model

This is a domain model, not a finalized Prisma schema. Resolve naming, cardinality, retention, and indexing during Milestone 1.

## Core entities
- **User** — account identity and lifecycle.
- **UserPreference** — UI locale, explanation locale, practice locale, timezone, accessibility preferences.
- **ProfessionalProfile** — role, industry, experience band, goals, self-reported proficiency.
- **Scenario** — stable scenario identity.
- **ScenarioVersion** — immutable scenario instructions/rubric version used by a session.
- **PracticeSession** — owner, scenario version, status, start/end timestamps, language, difficulty.
- **ConversationMessage** — session, speaker, content, sequence, timestamps.
- **SessionEvaluation** — session, evaluator version, overall result, structured feedback, evidence references.
- **DimensionScore** — evaluation dimension, score, evidence, explanation.
- **MistakePattern** — owner, language, category, normalized pattern, corrected form, confidence.
- **MistakeOccurrence** — mistake pattern, session/message/evidence reference, timestamp.
- **CommunicationProfileSnapshot** — owner, version, strengths, priorities, evidence references, generated timestamp.
- **DailyExercise** — owner, source signals, exercise content, status, result.
- **EmailCoachSession** — owner, source text, purpose, tone, output, explanation, retention metadata.
- **UsageLedgerEntry** — owner, operation, provider/model, token counts, estimated cost, entitlement decision, timestamp.
- **Subscription** — provider reference, status, product/plan, renewal metadata; only after payment provider selection.

## Relationship principles
- User owns all private profile, session, mistake, exercise, and email records.
- Session references the exact scenario version and AI prompt/evaluator versions used.
- Evaluation evidence references message IDs or bounded text spans where possible.
- Mistake occurrences are append-only evidence; pattern summaries can be recomputed.
- Communication profile snapshots preserve history; current profile is derived from the latest accepted snapshot.
- Usage ledger is append-only and must not be editable by client requests.
- Payment provider identifiers are external references, not authorization credentials.

## Data minimization
Do not store unnecessary raw client correspondence. Provide deletion controls and retention rules for sessions and email content. Avoid sending user identity or unrelated profile fields to AI providers.
