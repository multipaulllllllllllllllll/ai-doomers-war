# Technical Specification - AI Doomer Wars Wiki

**Project:** `~/ai-doomer-wiki` - an Obsidian-style research wiki compiled to a static HTML site (GitHub Pages).
**Reviewed:** 2026-09-19 (commit `d91a78e`) | **Repo:** `https://github.com/multipaulllllllllllllllll/ai-doomers-war`

## 1. Overview

The wiki documents the "AI Doomer Wars": the people, companies, funding networks, and events around AI-safety discourse, evaluation-industry scandals, and regulatory-capture accusations (Sep 2026). Two deliverables share one data model:

1. A graph of cross-linked entity sheets (people, organizations) browsable as a static site.
2. A long-form narrative hub (`AI-Doomer-Wars-Wiki.md`) with raw research logs under `research/`.

Design invariants:
- Markdown is the single source of truth; HTML is a generated artifact (idempotent regeneration).
- Everything committed: raw search results land in `research/YYYY-MM-DD.md` BEFORE sheet edits (backup-first).
- No frameworks, no dependencies - stdlib Python + hand-written CSS.

## 2. Architecture

```
 ~/ai-doomer-wiki/                    (SOURCE OF TRUTH - not git-tracked as a whole)
   characters/NNN-name.md   53         - person sheets (frontmatter + body)
   companies/NNN-name.md    24         - org sheets
   research/YYYY-MM-DD.md    2         - daily raw-capture logs
   AI-Doomer-Wars-Wiki.md  ~1k lines   - narrative hub (markdown only, not in repo)
   convert_sheets.py       418 LOC     - the compiler (stdlib Python, zero deps)
   site/                               - git repo root, published as-is to GitHub Pages
     chars/*.html    53    (generated)
     companies/*.html 24   (generated)
     *.html *.css          (HAND-MAINTAINED: index, characters, companies, about, style)
     characters/ companies/ research/ *.md   (mirrored sources, committed)
     .git/ -> multipaulllllllllllllllll/ai-doomers-war @ main
```

Pipeline: `edit .md -> clear __pycache__ -> python3 convert_sheets.py -> cp md into site/
-> hand-sync index pages -> git commit/push -> Pages live in 2-5 min`.
The compiler reads ONLY `../characters` + `../companies` and writes ONLY `site/chars` +
`site/companies`. Everything else in `site/` is manual and must never be rebuilt blindly.

## 3. Data Model (entity sheets)

Filename: `NNN-slug.md`; `NNN` = stable graph id (never reused after deletion unless the
entity is truly replaced), `slug` = kebab-case, unique. Output URL:
`site/chars/<NNN-slug>.html` (type: character) or `site/companies/<NNN-slug>.html`
(type: company). The numeric prefix is stripped from all cross-reference keys.

Frontmatter (custom YAML-subset; field census across 77 sheets):

| field | req | type | notes |
|---|---|---|---|
| `type` | yes | `character`\|`company` | routes output dir |
| `name` | yes | scalar | display name; doubles as link key |
| `role` | chars | scalar | header subtitle |
| `full_name`, `aliases`, `short_name` | no | scalar/list | link aliases |
| `tags` | yes | inline list `[a, b]` | sidebar chips |
| `involvement` | yes | `\|` multiline | sidebar excerpt (first 300 chars) |
| `relationships` | yes | block mapping key: [list] | edge labels -> sidebar links |
| `sources` | no | inline list | sidebar Sources |

Parser limitations (deliberate, ~50 LOC custom YAML subset):
- Supports: scalars (quotes stripped), inline lists, one-level block mappings, `|`
  multiline scalars. Does NOT support: nested lists, folded `>`, anchors, comments
  inside frontmatter, unquoted `{`/`[` in values.
- Malformed frontmatter -> silent fallback to first-line `Name - Role`; sheet still
  renders but sidebar/links degrade. Validation: run compiler and diff sheet counts.

## 4. Compiler - `convert_sheets.py`

Three passes:

**Pass A - `build_name_map()`**: scans all sheets' frontmatter; registers five key
variants per entity (`name`, `slug`, hyphenated-name, numeric-stripped slug,
hyphenated variant) -> `../chars|companies/<slug>.html`. This map powers every
cross-reference. Keys are matched case-insensitively after space/underscore -> hyphen
normalization in `resolve()`.

**Pass B - line renderer `md_to_html()`** (stateful, per line):
| construct | rule |
|---|---|
| ` ``` ` fences | buffered verbatim -> `<pre class="diagram">` (whitespace-exact; this is the ASCII-diagram fix - fences are exempt from every other transform) |
| `#..####` | h1..h4 (leading h1 of body stripped; name is already in the page header) |
| `\| ... \|` | GFM tables; separator rows skipped; first data row assumed header only when styled |
| `- `/`* ` | lists; `1. ` ordered |
| `>` | blockquote |
| `[[slug]]` | entity pill link via name_map (list items intentionally not linked - parked) |
| `**bold**`, `` `code` `` | inline |
| `---` | hr; also: everything under an H2/H3 literally named `See Also` is stripped from final HTML (post-regex in main loops - deprecated convention) |

**Pass C - `make_sheet_html()`**: emits full page (nav, back-link, H1+role, body,
sidebar: tags / relationships / 300-char involvement / sources, footer). Unresolved
relationship targets render `href="#"` (visible-but-dead; audit with:
`grep -l 'href="#"' site/chars/*.html site/companies/*.html`).

## 5. Hand-Maintained Site Pages (NOT generated)

| file | layout | sync duty when sheets change |
|---|---|---|
| `index.html` (317 LOC) | hero + dated `timeline-item` cards (`data-phase` early/mid/late - only these styled) + structure section | add cards for new cycles; keep hero numbers in sync with sheets |
| `characters.html` (128) | grouped pill browser (`entity-browser`, 1 column; groups=Roles with `pill pill-lab/pol/funder/media/...`) | add/remove one `<a class="pill" href="chars/NNN-slug.html">` per change |
| `companies.html` (157) | `entity-grid` cards (`entity-card/ec-name/ec-role/ec-tags`) | rebuild card list from `.md` frontmatter; hand-roles for legacy cards are kept in a dict when regenerating |
| `about.html` (61) | prose + GitHub links | update counts |
| `style.css` (363) | dark theme via `:root` vars (bg/card/text/muted/accent + per-entity accents) | `pre.diagram`: `white-space:pre; overflow-x:auto; box-drawing-safe mono stack @ .78rem` |

## 6. ASCII Diagram Specification

- Fenced ``` blocks only. Rendered `pre.diagram` -> strict 1 cell = 1 char.
- Box-drawing glyphs only (box draw chars); NO tabs; spaces for indent.
- Authoring must be COLUMN-COMPUTED, not eyeballed: build rows on a grid
  (lane centers e.g. A=8, B=34, C=58), center labels with
  `col - len//2`, then verify: connector chars (`v-` below a label, `^-` above)
  must land on the label's center column. The EA + NPT diagrams were rebuilt this
  way on 2026-09-19; Tallinn's tree is column-independent.

## 7. Deployment

- GitHub Pages (legacy), source: `/` on `main`, branch `site/.git`. No CI, no build step
  on GitHub - the build happens locally and outputs are committed.
- Propagation 2-5 min after push. Smoke check:
  `curl -s https://multipaulllllllllllllllll.github.io/ai-doomers-war/companies/022-effective-altruism.html | grep -c 'pre class="diagram"'`
- Markdown mirrors (`site/characters/`, `site/companies/`, `site/research/`) exist so the
  GitHub tree renders sources natively; they are plain copies, safe to overwrite wholesale.

## 8. Known Gaps & Risks (accepted)

1. **`AI-Doomer-Wars-Wiki.md` hub is not mirrored into the repo** - single-copy risk.
   Mitigation: copy it into `site/` each sync (added to runbook).
2. **Index pages drift silently** - no automation checks that pills/cards match the
   sheet set. Runbook step "verify index" (diff hrefs vs `ls`).
3. **Stale artifacts on rename/delete** - compiler never deletes; manual `rm` of both
   `.html` (and old `.md` mirrors) required, else ghost pages stay published.
4. **`See Also` strip regex is brittle** (matches exact indentation) - convention is now
   "do not write See Also sections"; removal is permanent for new content.
5. **Zero-result/failed searches are normal** (xurl); record gaps in the research log.
6. `__pycache__` can shadow - clear before each run (documented command).
7. No tests; verification is count-diff + `href="#"` audit + spot vision check.

## 9. Compliance & Style Constraints

- Cite everything to named handles/posts; unverified claims stay labeled as claims.
- Stick to the AI topic (no off-domain tangents) per standing instruction.
- Backup-first: raw search output -> markdown -> sheets -> compile -> push.
