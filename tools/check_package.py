#!/usr/bin/env python3
"""Check the Danish text files.

Usage:
    python3 tools/check_package.py [PATH ...]
    python3 tools/check_package.py --english english.json [PATH ...]

PATH is a Text folder or a single .xml file (default: Text). Without --english it checks
the structure: every file parses, every row is <Replace Language="da_DK" Tag="..."> with a
<Text>, no tag appears twice, and LocalizationDatabase_Data.sql adds da_DK.

With --english (made by tools/extract_english.py from your own game) it also checks every
line against its English original: the same {codes}, [ICON_...] tokens, plural/gender
branches and no leftover notes or English (rules in tools/validate.py), and lists tags
that are missing (shown in English in the game) or unknown (not in your game version).

Exit code 0 = no errors.
"""
import argparse
import glob
import json
import os
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate  # noqa: E402

LANG = 'da_DK'


def xml_files(paths):
    for p in paths:
        if os.path.isdir(p):
            yield from sorted(glob.glob(os.path.join(p, '**', '*.xml'), recursive=True))
        else:
            yield p


def main():
    ap = argparse.ArgumentParser(description='Check the Danish Civilization VI text files.')
    ap.add_argument('paths', nargs='*', default=['Text'])
    ap.add_argument('--english', help='english.json from tools/extract_english.py')
    ap.add_argument('--show', type=int, default=30, help='how many problems to print per kind')
    args = ap.parse_args()

    errors, rows, seen = [], {}, {}
    for p in args.paths:
        sql = os.path.join(p, 'LocalizationDatabase_Data.sql')
        if os.path.isdir(p) and os.path.basename(os.path.normpath(p)) == 'Text':
            if not os.path.exists(sql):
                errors.append('%s is missing: the game will not offer Dansk' % sql)
            elif "'%s'" % LANG not in open(sql, encoding='utf-8-sig').read():
                errors.append('%s does not add %s' % (sql, LANG))
    nfiles = 0
    for f in xml_files(args.paths):
        nfiles += 1
        try:
            root = ET.parse(f).getroot()
        except ET.ParseError as e:
            errors.append('%s: not valid XML: %s' % (f, e))
            continue
        for table in root:
            for row in table:
                tag = row.attrib.get('Tag')
                where = '%s: %s' % (os.path.basename(f), tag)
                if row.tag != 'Replace' or row.attrib.get('Language') != LANG or not tag:
                    errors.append('%s: expected <Replace Language="%s" Tag="...">' % (where, LANG))
                    continue
                text = row.find('Text')
                if text is None:
                    errors.append('%s: no <Text>' % where)
                    continue
                if tag in seen:
                    errors.append('%s: tag also in %s' % (where, seen[tag]))
                seen[tag] = os.path.basename(f)
                rows[tag] = text.text or ''

    missing, unknown = [], []
    if args.english:
        english = json.load(open(args.english, encoding='utf-8'))
        for tag, da in rows.items():
            if tag not in english:
                unknown.append(tag)
                continue
            for e in validate.check(tag, english[tag]['en'], da):
                errors.append('%s: %s' % (tag, e))
        missing = sorted(t for t, v in english.items() if v['en'].strip() and t not in rows)

    print('%d files, %d Danish rows' % (nfiles, len(rows)))
    if args.english:
        print('%d English tags in your game are not translated (shown in English)' % len(missing))
        for t in missing[:args.show]:
            print('  missing', t)
        print('%d Danish rows have no English tag in your game (other game version or a mod)' % len(unknown))
        for t in unknown[:args.show]:
            print('  unknown', t)
    if errors:
        for e in errors[:args.show * 10]:
            print('ERROR', e)
        print('FAILED: %d error(s)' % len(errors))
        sys.exit(1)
    print('OK')


if __name__ == '__main__':
    main()
