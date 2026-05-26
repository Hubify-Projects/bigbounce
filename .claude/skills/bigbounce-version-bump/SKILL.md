---
name: bigbounce-version-bump
version: 0.1.0
description: |
  Bump paper version atomically: \paperVersion + \paperTimestamp + \date{} in
  the .tex + version.json at repo root. Semver rules: patch=minor edits,
  minor=substantive section adds, major=restructure. All 4 items in same commit.
  pypdf-verify page 1 reflects new metadata.
triggers:
  - bump paper version
  - version bump
  - update version.json
---

# /bigbounce-version-bump — paper version + metadata cascade

**Source:** AGENTS.md "Versioning"; AGENT_RULES.md §4.2; CLAUDE.md "Paper Compilation"
**Scope:** bigbounce-only
**Trigger:** publication-worthy change to any of the 6 papers

## What this skill does

Cascades a version bump through all 4 places it has to land. If any one of them lags, the PDF page 1, the site, and the SSOT will disagree.

## The 4 items (all same commit)

| Item | File | Format |
|------|------|--------|
| `\paperVersion` | `<paper>.tex` | `v1B.0.22` (paper-specific prefix) |
| `\paperTimestamp` | `<paper>.tex` | `2026-05-26 14:32 PT` |
| `\date{...}` | `<paper>.tex` | matches timestamp + version string |
| Version JSON | `version.json` at repo root | `{"version": "...", "date": "..."}` per paper |

## Semver rules

| Bump | When | Example |
|------|------|---------|
| **patch** (last digit) | Minor edits, typos, R-round closures | v1B.0.22 → v1B.0.23 |
| **minor** (middle digit) | Substantive section add, new figure, new appendix | v1B.0.22 → v1B.1.0 |
| **major** (first digit) | Restructure, new methodology, major scope change | v1A.0.35 → v2A.0.0 |

## Paper-specific version prefixes

| Paper | Prefix | Example |
|-------|--------|---------|
| Paper 1A (ECH no-go) | `v1A.` | `v1A.0.35` |
| Paper 1B (MCMC companion) | `v1B.` | `v1B.0.22` |
| Paper 2 (f_NL forecast) | `v1.7.` (no letter) | `v1.7.33` |
| Paper 3 (anomaly catalog) | `v3.1.` | `v3.1.62` |
| Paper 4 (chirality catalog) | `v1.0.` | `v1.0.128` |
| Paper 5 (DESI chirality) | `v0.1.` | `v0.1.31` |

## How to apply

1. **Pick the bump level** (patch / minor / major) based on what changed.
2. **Update `\paperVersion`** in the .tex preamble or first-page metadata block.
3. **Update `\paperTimestamp`** to current PT time.
4. **Update `\date{...}`** to match the timestamp + version string format.
5. **Update `version.json`** at repo root — schema:
   ```json
   {
     "papers": {
       "p1a": {"version": "v1A.0.35", "date": "2026-05-26 14:32 PT"},
       "p1b": {"version": "v1B.0.22", "date": "2026-05-26 14:32 PT"},
       ...
     }
   }
   ```
6. **Recompile** (via `/paper-compile-revtex`).
7. **pypdf verify** page 1 has new values:
   ```python
   import pypdf
   p = pypdf.PdfReader('arxiv/<paper>.pdf')
   page1 = p.pages[0].extract_text()
   assert 'v1B.0.22' in page1
   assert '2026-05-26' in page1
   ```
8. **Commit all 4 items + recompiled PDF** in single commit.

## Hard gates

- [ ] All 4 items synchronized
- [ ] Semver bump level matches the change scope
- [ ] pypdf-verified page 1 reflects new metadata
- [ ] `version.json` schema valid

## Related
- /pdf-restamp-bundle — the bigger bundle that calls this
- /paper-compile-revtex — recompile after bump
- /bigbounce-site-sync — site mirror
- /commit-message-atomic — `feat(paper-N vX.Y.Z): …`
