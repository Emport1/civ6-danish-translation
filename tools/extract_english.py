#!/usr/bin/env python3
"""Extract the English text of an installed Civilization VI into a JSON file.

Usage:
    python3 tools/extract_english.py "<game folder>" english.json

<game folder> is the folder that contains Base/ and DLC/, for example
"C:\\Program Files (x86)\\Steam\\steamapps\\common\\Sid Meier's Civilization VI".

The output maps every text tag to {"en": text, "file": path}. When several packs define
the same tag, the version the game uses with Gathering Storm wins: Expansion2 (Gathering
Storm), then Expansion1 (Rise and Fall), then other DLC, then the base game; scenario and
game-mode packs rank lowest. This is the English the Danish package was translated from,
and what tools/check_package.py compares against.

The English text belongs to Firaxis/2K: keep english.json on your own computer and do
not commit it.
"""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

OTHER_LOCALE = re.compile(
    r'(?:^|[/_])(de_DE|es_ES|fr_FR|it_IT|ja_JP|ko_KR|pl_PL|pt_BR|ru_RU|zh_Hans_CN|zh_Hant_HK)(?:[/.]|$)')
LOW_PRIORITY_PACK = re.compile(r'Scenario|Mode$|TreeRandomizer|Royale', re.I)
ENGLISH_TABLES = ('EnglishText', 'BaseGameText', 'FrontEndText')


def priority(rel):
    parts = rel.split('/')
    if parts[0] == 'Base':
        p = 20
    else:
        pack = parts[1] if len(parts) > 1 else ''
        if pack == 'Expansion2':
            p = 50
        elif pack == 'Expansion1':
            p = 40
        elif LOW_PRIORITY_PACK.search(pack):
            p = 10
        else:
            p = 30
    name = parts[-1]
    if re.search(r'Expansion2|XP2', name):
        p += 5
    elif re.search(r'Expansion1|XP1', name):
        p += 3
    return p


def english_text_files(game):
    base = os.path.join(game, 'Base', 'Assets', 'Text', 'en_US')
    for root, _, files in os.walk(base):
        for f in sorted(files):
            if f.lower().endswith('.xml'):
                yield os.path.join(root, f)
    for root, _, files in os.walk(os.path.join(game, 'DLC')):
        rel_root = os.path.relpath(root, game).replace(os.sep, '/')
        if '/Text/' not in rel_root + '/':
            continue
        for f in sorted(files):
            rel = rel_root + '/' + f
            if f.lower().endswith('.xml') and not OTHER_LOCALE.search(rel):
                yield os.path.join(root, f)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    game, out_path = sys.argv[1], sys.argv[2]
    if not os.path.isdir(os.path.join(game, 'Base')):
        sys.exit('No Base folder in %r: give the folder that contains Base and DLC.' % game)
    versions = {}
    files = unreadable = 0
    for full in english_text_files(game):
        rel = os.path.relpath(full, game).replace(os.sep, '/')
        try:
            root = ET.parse(full).getroot()
        except ET.ParseError:
            unreadable += 1
            continue
        files += 1
        prio = priority(rel)
        for table in root:
            for row in table:
                if row.tag not in ('Row', 'Replace'):
                    continue
                lang = 'en_US' if table.tag in ENGLISH_TABLES else row.attrib.get('Language')
                tag = row.attrib.get('Tag')
                if lang != 'en_US' or not tag:
                    continue
                text = None
                for child in row:
                    if child.tag == 'Text':
                        text = child.text or ''
                if text is None:
                    text = row.attrib.get('Text', '')
                versions.setdefault(tag, []).append((prio, rel, text))
    corpus = {}
    for tag, vs in versions.items():
        best = max(vs, key=lambda v: v[0])
        corpus[tag] = {'en': best[2], 'file': best[1]}
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(corpus, fh, ensure_ascii=False, indent=0, sort_keys=True)
    print('%d English tags from %d files -> %s' % (len(corpus), files, out_path))
    if unreadable:
        print('%d files could not be parsed and were skipped' % unreadable)


if __name__ == '__main__':
    main()
