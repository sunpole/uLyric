# Changelog

## 2.1.0 — 2026-08-27

- Preserved and formalized the strongest UX from early real use: full-poem diagnostic analysis before rewriting.
- Added default first-pass analysis for complete poems pasted without a specific command.
- Added explicit detection of strongest/weakest stanzas, strong images, composition and what should be preserved.
- Fixed rhyme-core logic: compare from the stressed vowel onward; do not reject good rhymes because of consonants before the stressed vowel.
- Added regression case `позовёт — запоёт` as a strong exact masculine rhyme.
- Added regression case preventing overrating `равниной — пустыне` as a strong rhyme.
- Added real-test safeguards for `сердце`: do not inflate requested counts with repeated inflections or the same final rhyme word with extra words in front.
- Clarified that “only strong” may include strong exact and strong inexact rhymes with honest labels.
- Added a persistent “рифмы посложнее” preference for the current poem.
- Distinguished “рифмы посложнее”, “глубже” and “поэтичнее” as different tasks.
- Added protection against replacing depth with generic elevated vocabulary and clichés.
- Strengthened rejection of unnatural Russian constructions created only for poetic effect.
- Added version-history behavior: previous user lines may be compared and restored, but must remain clearly attributed to the user.
- Added lightweight Bible-link recognition for clearly Christian poems while keeping full theology checks opt-in.
- Expanded the regression suite from 32 to 49 cases using real project conversations.
- Updated output templates and end-user guide for analysis-first work.

## 2.0.0 — 2026-08-27

- Added `00_MASTER_AGENT.md` as the human-friendly entry point.
- Added natural-language enable/disable modes.
- Added `BIBLE_CHECK` for references, context and theology.
- Added `AI_STYLE_CHECK` with an explicit no-false-watermark rule.
- Added context isolation for new poems in old chats.
- Added feedback loop for natural user corrections.
- Added source/GitHub failure recovery.
- Added a short end-user guide.
- Expanded the regression test suite to 32 cases.
- Updated AGENTS routing and automatic ALL_IN_ONE generation.
- Prepared a smaller Project Source Pack for ChatGPT Projects.

## 1.0.0

Initial agent architecture for rhyme, rhythm, semantics, line construction, editing and QA.
