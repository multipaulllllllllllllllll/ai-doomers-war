# Runbook - AI Doomer Wars Wiki

Operational procedures for `~/ai-doomer-wiki`. Companion: `technical-spec.md`.
All commands assume paths exactly as written; shell metacharacters in commit messages
need single quotes (`'$70B'`), never double.

## R1. Add a new entity sheet

1. Pick the next id: `ls characters/ | sort -V | tail -1` (chars) / same in `companies/`.
   Reusing a deleted id is allowed only to replace that entity.
2. Create `characters/NNN-slug.md` (or `companies/`) with required frontmatter:
```
---
type: character
name: \"Full Name\"
role: \"Position, Org\"
tags: [a, b, c]
relationships:
  key_label: [other-sheet-name-or-slug, ...]
involvement: |
  Two to six sentences of dense factual summary.
sources: [\"@handle, YYYY-MM-DD\"]
---

# Full Name

## Summary
...body: H2 sections, tables, `[[wiki-links]]`, fenced diagrams...
```
3. Reference existing entities ONLY by sheet name/slug so links resolve.
4. Add the pill/card to the index page (R5). Add back-links in related sheets'
   `relationships:` (graph is bidirectional by convention).

## R2. Research-first update cycle

1. Search (xurl full path): `/home/yollama/.local/bin/xurl search \"query\" -n 20`
   - Zero-result and exit-1 responses are common; retry with shorter terms; no `site:`.
2. Append raw findings to `research/YYYY-MM-DD.md` (create dir with `mkdir -p` first -
   it may not exist on a fresh checkout). This file is the crash-recovery backup.
3. Only then edit sheets; keep every claim attributed to a named handle/post/date.

## R3. Rebuild & deploy

```bash
cd ~/ai-doomer-wiki
rm -rf __pycache__ *.pyc                      # stale module shadowing
python3 convert_sheets.py                     # expect: 53 chars + 24 companies + Done.
cd site
cp ../characters/*.md characters/ && cp ../companies/*.md companies/
cp ../research/*.md research/ && cp ../AI-Doomer-Wars-Wiki.md .   # hub mirror
git add -A && git status --short | wc -l      # non-zero == real changes
git commit -m 'short factual description' && git push
```
Verify after 2-5 min: curl a changed page, check for expected new string.

## R4. Rename / delete a sheet

1. `git mv`/`rm` in the SOURCE dir, then `rm` the matching `site/chars|companies/*.html`
   AND the mirrored `*.md` - the compiler never deletes; ghosts stay published.
2. Rebuild (R3). Then index sync (R5) and grep stale hrefs:
   `grep -rl 'OLD-slug' site/ | grep -v characters/ | grep -v companies/`
3. Check `resolve()` fallout: new `href="#"` count must not increase (R6).

## R5. Sync index pages (manual, no automation)

characters.html: one `<a class="pill pill-X" href="chars/NNN-slug.html">Name</a>` inside
the matching group; keep `N people` subtitle and footer counts current.
companies.html: rebuild card grid from frontmatter when >2 sheets change - pattern:
parse existing `entity-card` blocks, add hand-roles dict for new sheets, splice between
`<div class="entity-grid">` and the footer div (a working recipe exists in session
history; preserve exact 6-space indentation so the See Also-strip regex elsewhere stays valid).
Verify: `diff <(grep -o 'href="chars/[^"]*' characters.html | sort -u) <(ls chars/*.html | sed 's|^|href="|' | sort -u)`.

## R6. Health audit (run after any structural change)

```bash
cd ~/ai-doomer-wiki/site
# 1. counts agree (source == html == mirror == index)
for d in chars companies; do echo "$d: $(ls $d/*.html | wc -l)"; done
ls ../characters/*.md ../companies/*.md | wc -l
# 2. dead sidebar links (unresolved relationship keys)
grep -l 'href="#"' chars/*.html companies/*.html | wc -l
# 3. raw wiki-link leakage
grep -rc '\[\[' chars/*.html companies/*.html | grep -v ':0' || echo clean
# 4. ghost pages: html without md source
comm -13 <(ls ../companies/*.md ../characters/*.md | xargs -n1 basename | sort) \
         <(ls chars/*.html companies/*.html | xargs -n1 basename | sed s/.html// | sort)
```
Expected steady state: 53/24 counts equal in all views; leakage `clean`; ghosts empty;
dead-link list contains only intentional placeholders (peter-singer, toby-ord etc.).

## R7. Diagram maintenance

Never hand-align connectors. Write a one-shot generator: fixed lane-center columns,
`start = center - len(text)//2`, branch spans as explicit `range` fills, then paste the
output block into the sheet between ``` fences. Check: every `v` below a label is at that
label's center column; every `^` above a label likewise (a python assert pass is cheap).

## R8. Troubleshooting

| symptom | cause | fix |
|---|---|---|
| diagram lines squashed/wrapped | content outside fences, or `white-space` overridden | fence it; keep `pre.diagram{white-space:pre}` |
| half-width connectors | non-mono fallback drew box glyphs | style.css pre.diagram stack |
| page 404 after push | propagation | wait 5 min; then verify file is committed (`git ls-files`) |
| sidebar shows plain text for a rel | key not in name_map | match spelling to a sheet `name`/slug exactly |
| stale HTML for deleted sheet | compiler never deletes | R4 step 1 |
| xurl exit 1 | malformed/over-filtered query | shorten query; drop `site:` |
| browser can't launch | Chrome profile lock | use xurl + curl; never fight the lock |

## R9. Rollback / recovery

- Site: `cd site && git revert <sha> && git push` (or `git reset --hard origin/main`
  if unpushed). Never rewrite pushed history.
- Sheets lost locally: markdown mirrors in `site/{characters,companies,research}/` are
  the last-pushed copy - restore `cp site/characters/NNN-x.md characters/`.
- Whole workspace lost: clone the repo; mirrors + generated HTML rebuild everything
  except uncommitted sheet edits since last push (that is what research logs exist for).

## R10. Quick reference

- Site: https://multipaulllllllllllllllll.github.io/ai-doomers-war/
- Repo: github.com/multipaulllllllllllllllll/ai-doomers-war (main, Pages legacy /)
- Inventory: 53 characters, 24 companies, 2 research logs, hub ~1k lines
- Compiler: `~/ai-doomer-wiki/convert_sheets.py` (418 LOC, stdlib only)
- xurl: `/home/yollama/.local/bin/xurl`
- Runbook last reviewed: 2026-09-19
