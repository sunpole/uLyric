# uLyric

**AI-assisted toolkit for Russian poetry and song lyrics.**

uLyric is a rule and agent system designed for a ChatGPT Project where the user can work in ordinary Russian without learning technical commands.

## What it helps with

Rhymes, line rewriting, rhythm, syllables, natural Russian, poem analysis, song adaptability, biblical references, theological consistency, preservation of author voice, and stylistic review.

## User experience

The user simply writes:

> «Рифмы к слову “сердце”. Только сильные.»

or:

> «Переделай строку, но последнее слово не трогай.»

or:

> «Проверь этот стих по Библии и по ритму, пока ничего не исправляй.»

The internal routing stays hidden.

## Architecture

`00_MASTER_AGENT.md` → `AGENTS.md` → task-specific modules → `QA_CRITIC`.

Canonical rules are stored in this repository. `ALL_IN_ONE.md` is generated automatically from the individual source files.

## ChatGPT Project setup

For the ChatGPT Project, use the compact Project Source Pack:
- `00_MASTER_AGENT.md`
- `AGENTS.md`
- `ALL_IN_ONE.md`
- `PROJECT_INSTRUCTIONS_COPY.txt`
- `VERSION.md`
- `20_USER_GUIDE.md`

Paste the contents of `PROJECT_INSTRUCTIONS_COPY.txt` into Project Instructions.

GitHub is the canonical development source, while the attached Project files are a reliable fallback if GitHub is unavailable.

## Version

See [VERSION.md](VERSION.md) and [CHANGELOG.md](CHANGELOG.md).

## License

MIT.
