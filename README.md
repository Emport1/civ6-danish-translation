# Civilization VI på dansk

Danish translation of **Sid Meier's Civilization VI**. It adds **Dansk** as an extra display
language: all 32,280 text lines of the base game, Rise and Fall, Gathering Storm, the New
Frontier Pass and the Leader Pass. That covers menus, tooltips, the tutorial, advisors,
leader dialogue and the whole Civilopedia. The game's own files are not changed.

[Dansk](#dansk) · [English](#english) · [Contributing](CONTRIBUTING.md)

---

## Dansk

**Det får du**
- Menuer, værktøjstip, vejledningen, rådgiveren, ledernes replikker og hele Civilopedia på dansk.
- Stemmerne er stadig engelske, for spillet har ingen danske stemmer. Lederne taler som altid
  deres eget historiske sprog, og det, de siger, vises som dansk tekst.
- Tekst, som pakken ikke har (fx fra en senere opdatering), vises på engelsk.

**Installation (Windows)**
1. Hent `civ6-dansk-<version>.zip` under
   [Releases](https://github.com/Emport1/civ6-danish-translation/releases/latest), og pak den ud.
2. Åbn mappen `Dokumenter\My Games\Sid Meier's Civilization VI`, hvor også `Saves` og `Mods`
   ligger. Tager OneDrive backup af Dokumenter, ligger den under `OneDrive\Dokumenter`.
3. Kopiér mappen `Text` fra zip-filen ind i den mappe. Bagefter skal disse filer findes:
   - `...\Sid Meier's Civilization VI\Text\LocalizationDatabase_Data.sql`
   - `...\Sid Meier's Civilization VI\Text\da_DK\Danish_01.xml` (til og med `Danish_09.xml`)
4. Start spillet, og vælg **Options → Language → Display Language → Dansk (Danmark)**.
   Luk spillet helt, og start det igen: teksten indlæses kun, når spillet starter.

**Afinstallation:** vælg et andet sprog, eller slet mappen `Text` igen.

**Mac og Linux:** ikke testet. Spillet læser sandsynligvis den samme `Text`-mappe ved siden af
`Mods`-mappen (Mac: `~/Library/Application Support/Sid Meier's Civilization VI/Sid Meier's Civilization VI/`,
Linux: `~/.local/share/aspyr-media/Sid Meier's Civilization VI/`). Skriv gerne et issue, hvis
det virker eller ikke virker.

**Mods:** dansk tekst til 13 populære brugerflade-mods ligger i [`extras/mods`](extras/mods).

**Fundet en fejl?** Opret et [issue](https://github.com/Emport1/civ6-danish-translation/issues/new/choose)
med et skærmbillede, eller ret den selv (se [CONTRIBUTING.md](CONTRIBUTING.md)).

---

## English

**What you get:** every text line of Civilization VI in Danish, including all expansions and
DLC packs, as an extra language next to the 12 official ones. Voices stay English (there is
no Danish voice). Lines the package lacks, for example after a game update, fall back to
English.

**Install (Windows):** download `civ6-dansk-<version>.zip` from
[Releases](https://github.com/Emport1/civ6-danish-translation/releases/latest) and copy its
`Text` folder into `Documents\My Games\Sid Meier's Civilization VI\` (the folder that holds
`Saves` and `Mods`). In the game choose **Options → Language → Display Language → Dansk
(Danmark)**, then quit and restart: text loads only at game start. To uninstall, pick another
language or delete the `Text` folder.

Mac and Linux are untested; the same `Text` folder next to the `Mods` folder should work there.

**How it works:** Civilization VI reads `Text\LocalizationDatabase_Data.sql` and
`Text\<locale>\*.xml` from the user folder at startup. The SQL file registers the language
`da_DK` with English as fallback, and the XML files hold one
`<Replace Language="da_DK" Tag="...">` row per text line.

### How the translation was made

The game's English text (base game + every DLC, the version Gathering Storm uses) was
translated with Claude Opus 5.5 in 113 chunks:
- Names of game objects first, so every unit, building and wonder has one fixed Danish name
  everywhere.
- A binding style guide ([docs/STYLE.md](docs/STYLE.md)) and a glossary
  ([docs/TERMS.md](docs/TERMS.md)).
- Every line was then checked by [tools/validate.py](tools/validate.py): the same `{codes}`,
  `[ICON_...]` tokens and plural/gender branches as the English, and no leftover English or
  translator notes. All 32,280 lines pass.

The package has been played on Windows (menus, the tutorial and normal games, including
LAN games). Not every line has been proofread by a person yet, so corrections are very
welcome.

### Credits

- [Mallock/babel-fish-civ](https://github.com/Mallock/babel-fish-civ): its 2023 Danish AI
  translation is where this project started. We measured it, repaired it and finally
  retranslated everything; none of its lines remain, but it showed that a Danish Civ VI was
  possible.
- [HendriXML/Civilization-6-Dutch-Translation](https://github.com/HendriXML/Civilization-6-Dutch-Translation)
  and [fredzgreen/Civilization6_SwedishTranslation2](https://github.com/fredzgreen/Civilization6_SwedishTranslation2)
  showed how to add a new language through the user `Text` folder.

### Legal

Unofficial fan translation, not affiliated with or endorsed by Firaxis Games, 2K or
Take-Two Interactive. Sid Meier's Civilization VI and its English text are © Take-Two
Interactive Software and its subsidiaries. This repository contains only the Danish text and
the tools used to make and check it; no game files and no English game text. The project's
own work is released under the [MIT License](LICENSE).
