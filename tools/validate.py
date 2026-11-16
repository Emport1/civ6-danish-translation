#!/usr/bin/env python3
"""Check a Danish translation of game strings against the English source.

Usage: python3 validate.py chunk.json out.json
chunk.json: {"strings": {tag: english, ...}, ...}   out.json: {tag: danish, ...}
Prints OK, or one line per problem (fix them and run again).
"""
import json
import re
import sys
from collections import Counter

SQUARE = re.compile(r'\[[A-Za-z_][A-Za-z0-9_]*(?::[^\]\s]+)?\]')
HEAD = re.compile(r'\{\s*([A-Za-z0-9_.]+)')
KEYWORD = re.compile(r'\{\s*[A-Za-z0-9_.]+\s*:\s*([A-Za-z]+)')
NUMBER_EXPR = re.compile(r'\{\s*[A-Za-z0-9_.]+\s*:\s*number[^{}]*\}')
NOTE = re.compile(r'\((?:this|note|translat|no translation|proper noun|already)[^)]*\)|translator|oversætters note|'
                  r'\bas an ai\b|cannot be translated|does not require translation|needs to be translated|'
                  r'natural-sounding|i will provide|please provide|please translate|here is the|what text|'
                  r'would you like me|in danish|to danish|danish does not|same in danish|literal translation', re.I)
EN_WORDS = re.compile(r'\b(the|and|with|your|this|that|from|have|will|their|which|when|into|been|were)\b', re.I)


def top_level_exprs(s):
    out, depth, start = [], 0, None
    for i, ch in enumerate(s):
        if ch == '{':
            if depth == 0:
                start = i
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0 and start is not None:
                out.append(s[start:i + 1])
            if depth < 0:
                return None
    return out if depth == 0 else None


def selectors(expr):
    m = re.match(r'\{\s*[A-Za-z0-9_.]+\s*:\s*(plural|gender)\b', expr)
    if not m:
        return Counter()
    body = expr[m.end():-1]
    sels, depth, seg = Counter(), 0, ''
    for ch in body:
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
        if depth == 0 and ch == '?':
            tok = re.split(r'[;\s]', seg)[-1]
            sels[(m.group(1), tok)] += 1
            seg = ''
            continue
        if depth == 0 and ch == ';':
            seg = ''
            continue
        if depth == 0:
            seg += ch
    return sels


def check(tag, en, da):
    errs = []
    if not isinstance(da, str):
        return ['not a string']
    if en.strip() and not da.strip():
        return ['empty translation']
    if Counter(SQUARE.findall(en)) != Counter(SQUARE.findall(da)):
        errs.append('[...] tokens differ: english %s / danish %s' % (
            sorted(Counter(SQUARE.findall(en)).elements()), sorted(Counter(SQUARE.findall(da)).elements())))
    en_heads, da_heads = Counter(HEAD.findall(en)), Counter(HEAD.findall(da))
    en_kw, da_kw = Counter(KEYWORD.findall(en)), Counter(KEYWORD.findall(da))
    gender_only = 'gender' in en_kw
    if gender_only:
        # gender article templates may be reduced to an other? branch: heads may appear fewer times
        if set(en_heads) != set(da_heads):
            errs.append('{...} variable names differ: english %s / danish %s' % (sorted(en_heads), sorted(da_heads)))
    elif en_heads != da_heads:
        errs.append('{...} variable names/counts differ: english %s / danish %s' % (
            sorted(en_heads.elements()), sorted(da_heads.elements())))
    if en_kw != da_kw:
        errs.append('{... : keyword} differs: english %s / danish %s' % (dict(en_kw), dict(da_kw)))
    if Counter(NUMBER_EXPR.findall(en)) != Counter(NUMBER_EXPR.findall(da)):
        errs.append('number expressions must be copied exactly: %s' % NUMBER_EXPR.findall(en))
    en_top, da_top = top_level_exprs(en), top_level_exprs(da)
    if da_top is None and en_top is not None:
        errs.append('unbalanced { } braces')
    elif en_top is not None:
        en_sel, da_sel = Counter(), Counter()
        for e in en_top:
            en_sel += selectors(e)
        for d in da_top:
            da_sel += selectors(d)
        if not gender_only and en_sel != da_sel:
            errs.append('plural branch selectors differ: english %s / danish %s' % (dict(en_sel), dict(da_sel)))
        if gender_only and any(k[0] == 'gender' for k in en_sel) and ('gender', 'other') not in da_sel:
            errs.append('gender expression needs an other? branch')
    if NOTE.search(da) and not NOTE.search(en):
        errs.append('looks like a translator note/explanation inside the text: remove it')
    plain = re.sub(r'\{[^{}]*\}|\[[^\]]*\]', ' ', en)
    if da.strip() == en.strip() and len(plain) > 30 and len(EN_WORDS.findall(plain)) >= 2:
        errs.append('identical to the English text: translate it')
    elif len(plain) > 60 and len(EN_WORDS.findall(re.sub(r'\{[^{}]*\}|\[[^\]]*\]', ' ', da))) >= 6:
        errs.append('still contains many English words: translate fully')
    return errs


def main():
    src = json.load(open(sys.argv[1], encoding='utf-8'))
    strings = src['strings'] if 'strings' in src else src
    try:
        out = json.load(open(sys.argv[2], encoding='utf-8'))
    except Exception as e:  # noqa: BLE001
        print('out.json is not valid JSON: %s' % e)
        sys.exit(1)
    problems = []
    for tag in strings:
        if tag not in out:
            problems.append('%s: missing' % tag)
    for tag in out:
        if tag not in strings:
            problems.append('%s: not in the source (remove it)' % tag)
    for tag, en in strings.items():
        if tag in out:
            for e in check(tag, en, out[tag]):
                problems.append('%s: %s' % (tag, e))
    if problems:
        print('\n'.join(problems[:200]))
        if len(problems) > 200:
            print('... %d more problems' % (len(problems) - 200))
        print('FAILED: %d problem(s) in %d strings' % (len(problems), len(strings)))
        sys.exit(1)
    print('OK: %d strings' % len(strings))


if __name__ == '__main__':
    main()
