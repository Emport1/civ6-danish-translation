# Translator brief

The instructions every translation chunk was made with (one chunk = about 36,000 characters of English, `c.json`; the result was `c.da.json`).

---

Goal: Translate the game text strings in `c.json` from English into natural, high-quality Danish (Civilization VI localization). This is one small part of a larger project; the game's names and labels are already translated.

Context:
- `c.json` has `strings` (id -> English text), `tags` (id -> the game's internal tag, telling you what the string is) and `glossary` (English game term -> its already-decided Danish name).
- `STYLE.md` is the binding style guide (voice, capitalization, strict format rules, core terminology). Read it fully first.
- `TERMS.md` lists further terminology decisions. Use the glossary and TERMS.md so every game object is called exactly what the game calls it elsewhere (inflect normally in Danish sentences: "Nybygger" -> "en nybygger" in running text).
- `validate.py` checks the translation.
- The reader is an adult Danish player who is not a gaming expert. Write fluent, idiomatic Danish; encyclopedia (Civilopedia) articles should read like good Danish popular history, not a word-for-word rendering.

Do:
1. Read STYLE.md, TERMS.md and c.json.
2. Write `c.da.json`: a JSON object mapping every id to its Danish text (UTF-8, real æ/ø/å). Translate every string completely.
3. Run `python3 validate.py c.json c.da.json` and fix every reported problem until it prints OK.

Done means: `c.da.json` exists and validate.py prints OK.

Don't: change ids or c.json, add notes inside translations, use Task subagents, edit STYLE.md/TERMS.md/validate.py, or write other deliverables.

At the end: one sentence: validator result and anything you were unsure about.
