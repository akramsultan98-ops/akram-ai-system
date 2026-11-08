# Localization Strategy

## Product decision
Multilingual capability is an architectural requirement from day one. Initial production locales are English and Arabic. Additional locales are added only after translation and AI-feedback quality can be evaluated.

## Independent language settings
Persist three independent user preferences:
- **UI locale:** language of navigation and controls.
- **Explanation locale:** language used to explain feedback.
- **Practice locale:** language in which the user is practicing.

Do not assume these are identical.

## UI implementation
- Keep translation dictionaries outside UI components.
- No hardcoded user-facing strings.
- Use locale-aware routing or an equivalent explicit locale strategy.
- Set document language and text direction correctly.
- Arabic must render with RTL layout, including forms, navigation, mixed numerals, and punctuation.
- Test mixed Arabic/English business terms.
- Format dates, times, and numbers using locale-aware APIs.
- Avoid concatenating translated fragments; use complete localized messages.

## AI behavior
- Scenario language and explanation language are separate inputs.
- Feedback should quote the original expression exactly and explain in the selected explanation locale.
- Preserve proper nouns, product names, amounts, dates, and commercial terms.
- Never translate user content silently when the task is correction or rewriting.
- Add locale-specific evaluation tests before enabling a new language.

## Initial release
- English UI and practice.
- Arabic UI and explanations.
- English practice with Arabic explanations.
- Arabic practice support can be enabled only after the scenario/evaluation quality is tested; do not claim equivalent coaching quality without evidence.

## Reference
Use the current Next.js App Router internationalization guidance as a starting point; select a mature localization library only after evaluating routing, server rendering, message typing, and RTL requirements.
