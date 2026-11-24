#!/usr/bin/env python3
"""Synchronize only the timeline press teaser from the current press HTML.

Run before publishing and after any legacy chronology rebuild. Never regenerate
jensen-press.html from the historical 48-piece source to fix teaser counters.
Use --check for a read-only publication gate.
"""
import argparse
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re

class Inventory(HTMLParser):
    def __init__(self):
        super().__init__()
        self.section = None
        self.counts = dict.fromkeys(('reporting', 'editorial', 'signed'), 0)
        self.outlets = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section':
            self.section = attrs.get('id')
        if tag == 'article':
            assert self.section in self.counts, self.section
            self.counts[self.section] += 1
            self.outlets.add(attrs['data-outlet'])

    def handle_endtag(self, tag):
        if tag == 'section':
            self.section = None


def sync(root, check=False):
    press = (root / 'jensen-press.html').read_text()
    inventory = Inventory()
    inventory.feed(press)
    n, outlets = sum(inventory.counts.values()), len(inventory.outlets)
    assert f'Browse {n} pieces from {outlets} outlets' in press
    for key, count in inventory.counts.items():
        assert f'href="#{key}"><b>{count:02}</b>' in press
    jump_match = re.search(r'<div id="browse" class="jumps">(.*?)</div>', press, re.S)
    assert jump_match is not None, 'Missing standalone section navigation'
    jumps = jump_match.group(1)
    jumps = jumps.replace('href="#', 'href="jensen-press.html#')
    path = root / 'index.html'
    before = path.read_text()
    pattern = r'<aside class="press-feature">.*?</aside>'
    matches = list(re.finditer(pattern, before, re.S))
    assert len(matches) == 1, 'Expected exactly one press teaser'
    old = matches[0]
    heading_match = re.search(r'<small>.*?</small><h3>.*?</h3>', old.group(), re.S)
    assert heading_match is not None, 'Missing timeline press heading'
    heading = heading_match.group()
    teaser = f'<aside class="press-feature">{heading}<p>{n} pieces from {outlets} outlets. Jump to a section:</p><div class="jumps">{jumps}</div></aside>'
    after = before[:old.start()] + teaser + before[old.end():]
    assert after[:old.start()] == before[:old.start()]
    assert after[old.start() + len(teaser):] == before[old.end():]
    print(f'{n} pieces; {outlets} outlets; sections={inventory.counts}')
    if check:
        assert before == after, 'Timeline press teaser is stale; run this script without --check'
        print('PASS: timeline teaser matches standalone article inventory')
    elif before != after:
        path.write_text(after)
        print('Updated only the timeline press teaser')
    else:
        print('Already synchronized')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    sync(Path(__file__).resolve().parents[1], args.check)
