# MVP Scope and Acceptance Criteria

## Included

### 1. Account and onboarding
- Registration, login, logout, and account deletion.
- Job role, industry, proficiency estimate, and goals.
- Separate preferences for UI locale, explanation locale, and practice locale.
- English and Arabic translations; Arabic RTL.

**Acceptance:** a user can complete onboarding, change each language preference independently, and see the correct locale and direction after refresh/login.

### 2. Baseline assessment
- Short text-based professional communication assessment.
- Clearly labeled as an estimate, not a certified language test.
- Initial strengths and improvement areas tied to actual responses.

**Acceptance:** assessment produces schema-valid output with evidence snippets and no unsupported claims.

### 3. Text roleplay
Initial scenarios:
1. Negotiating a Higher Price.
2. Handling a Difficult Client.
3. Presenting a Proposal.
4. Following Up with a Client.
5. Handling a Sales Objection.

Each scenario has counterpart role, context, objective, difficulty, constraints, and completion criteria.

**Acceptance:** user can start, continue, and end a session; messages persist; AI counterpart follows scenario behavior and does not expose internal instructions.

### 4. Feedback
Rubric dimensions:
- Grammar accuracy.
- Vocabulary and expression.
- Clarity.
- Professional tone.
- Naturalness.
- Persuasiveness.
- Scenario objective achievement.

**Acceptance:** each claim links to observed text or is clearly marked as a general recommendation. The evaluator distinguishes correctness errors from optional stylistic improvements.

### 5. Mistake Bank and Communication DNA
- Store observed patterns and corrected examples.
- Count recurrence across sessions.
- Maintain evidence and confidence.
- Summarize strengths and priorities.

**Acceptance:** a profile update cannot be based solely on unsupported model assertions; user can inspect and delete their records.

### 6. Daily practice
- Short text exercise selected from recent validated weaknesses.
- Completion and outcome recorded.

**Acceptance:** generated exercise references a real profile signal or user-selected goal.

### 7. Professional Email Coach
- User pastes text and selects purpose/tone.
- Return improved draft and key explanations.
- Preserve factual meaning and commitments.

**Acceptance:** no new dates, prices, promises, recipients, or factual claims are introduced.

### 8. Progress and usage
- Session count, activity, recent rubric trends, recurring mistakes.
- AI usage ledger with provider/model, operation, token counts when available, estimated cost, and request status.
- Configurable plan/usage limits.

**Acceptance:** quota is enforced server-side and ledger records are attributable to the authenticated user.

## Explicitly excluded
- Voice input/output and transcription.
- Live meeting copilot.
- Native iOS/Android apps.
- Enterprise/team admin.
- Social features and public profiles.
- Video avatars.
- Courses or marketplace.
- Complex gamification.
- Automated outbound email sending.
- Payment collection until provider eligibility, payouts, and webhook behavior are verified.

## MVP release gate
Do not call the MVP launch-ready until:
- core roleplay and evaluation tests pass;
- English and Arabic UI flows pass, including RTL;
- authorization and data deletion tests pass;
- AI cost metering and usage caps work;
- privacy/retention behavior is documented;
- 20–30 target users have tested the product;
- feedback quality and repeat-use signals have been reviewed.
