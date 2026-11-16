# Contributing / Bidrag

Corrections from Danish players are the most useful help: a line that reads oddly, a wrong
term, or text that is cut off on screen.

## Report a problem

Open an [issue](https://github.com/Emport1/civ6-danish-translation/issues/new/choose) with:
- a screenshot, or where in the game the text appears,
- the Danish text as it is, and what it should say.

Danish or English are both fine.

## Fix it yourself

1. Find the line: search the Danish text in `Text/da_DK/Danish_*.xml`. Each line looks like
   ```xml
   <Replace Language="da_DK" Tag="LOC_UNIT_SETTLER_NAME">
       <Text>Nybygger</Text>
   </Replace>
   ```
2. Change only the text between `<Text>` and `</Text>`. Keep these exactly as they are:
   - `{...}` codes, e.g. `{1_Amount : number #}` or `{LOC_DISTRICT_CAMPUS_NAME}`; in plural
     codes such as `{2_Turns : plural 1?{2_Turns} tur; other?{2_Turns} ture;}` translate only
     the words.
   - `[ICON_...]`, `[NEWLINE]`, `[COLOR_...]` and `[ENDCOLOR]` tokens.
   - XML escapes: `&amp;`, `&lt;`, `&gt;`.
3. Use the words in [docs/STYLE.md](docs/STYLE.md) and [docs/TERMS.md](docs/TERMS.md), so a
   unit or building has the same name everywhere.
4. Run the checker (Python 3, no extra packages):
   ```
   python3 tools/check_package.py
   ```
   For a full check against your own game's English text:
   ```
   python3 tools/extract_english.py "<folder with Base and DLC>" english.json
   python3 tools/check_package.py --english english.json
   ```
   `english.json` is Firaxis' text: keep it on your computer (it is in `.gitignore`).
5. Open a pull request.

## Files

| Path | What it is |
|---|---|
| `Text/LocalizationDatabase_Data.sql` | Registers the language `da_DK` ("Dansk") with English as fallback |
| `Text/da_DK/Danish_*.xml` | The translation, sorted by tag |
| `extras/mods/` | Danish text for 13 user-interface mods |
| `tools/validate.py` | The line checker (codes, icons, plural/gender branches, leftover English) |
| `tools/check_package.py` | Checks the files, optionally against your game's English |
| `tools/extract_english.py` | Reads the English text from your installed game |
| `docs/STYLE.md`, `docs/TERMS.md` | Style guide and glossary |
| `docs/translator-brief.md` | The instructions each translation chunk was made with |
