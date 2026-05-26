---
name: bigbounce-claims-table-sync
version: 0.1.0
description: |
  When any quantitative claim changes (f_NL number, σ, anomaly count, MCMC sample
  count, redshift, etc), grep every .tex AND every HTML/TSX page in the repo for
  the old value, replace with new in one atomic commit. Zero stale instances allowed.
  Claims-table on index.html must match paper abstract.
triggers:
  - sync claims
  - update quantitative claim
  - replace number everywhere
---

# /bigbounce-claims-table-sync — quantitative claim consistency

**Source:** CLAUDE.md "When research results change"; `feedback_site_sync_same_commit.md`
**Scope:** bigbounce-only
**Trigger:** any quantitative claim in a paper changes (number, σ value, sample count)

## What this skill does

Catches the most common drift pattern: a number gets updated in one paper but not in the abstract, not on the website, not in the dossier. Greps everywhere; replaces everywhere; verifies zero remain.

## Examples of claims that need sync

- `f_NL = -35/8` (changes if leading-order vs NLO)
- `378,280 anomalies` (changes when surveys added)
- `309,189 MCMC samples` (corrected 2026-05 from confabulated 309,789)
- `8.47M galaxies` (chirality catalog)
- `σ = 0.7` (Heinrich+2023 fNL forecast — corrected from confabulated 16.85/12.72/11.71)
- `β = 0.27°` (ALP birefringence prediction)
- Redshift values, magnitude limits, photo-z accuracy, etc.

## How to apply

1. **Identify old value + new value**:
   ```
   OLD="309,789"
   NEW="309,189"
   ```
2. **Grep everywhere** (case-sensitive, surrounding chars matter):
   ```bash
   grep -rn --include="*.tex" --include="*.html" --include="*.tsx" --include="*.md" --include="*.py" "$OLD" .
   ```
3. **For each hit**, decide: is this the same claim? (Sometimes a number appears in multiple unrelated contexts.)
4. **Replace each genuine hit** with `sed` or Edit tool per file.
5. **Re-grep** to confirm zero hits:
   ```bash
   grep -rn "$OLD" . --include="*.tex" --include="*.html" --include="*.tsx" --include="*.md"
   # should return nothing
   ```
6. **Verify claims-table on `index.html` matches paper abstract**:
   ```bash
   # Spot check key numbers from the paper abstract vs the index.html claims table
   ```
7. **Commit** with descriptive message:
   ```
   fix(claims): correct MCMC sample count 309,789 → 309,189 across all surfaces
   ```

## Special case — paper abstract is the source of truth

If the .tex abstract has the canonical number, every other surface mirrors it. If the change starts on the website and not the abstract, something is wrong — start over from the paper.

## Hard gates

- [ ] Zero instances of the old number remain (`grep` returns empty)
- [ ] `index.html` claims table matches paper abstracts
- [ ] Numbers consistent across .tex, HTML, TSX, MD
- [ ] Commit message names the specific claim that changed

## Anti-patterns

- Updating the paper .tex but not the website → claims-table on index.html lies
- Updating the abstract but not the body — they have to agree
- Replacing with sed and not re-grepping → silently leave stragglers

## Known-tricky cases

- `309,189` vs `309,789` — confabulated value lived in CLAUDE.md for weeks
- `378,280` (Path C dedup) vs `319,443` (pre-Path-C baseline) — both are real numbers but mean different things; don't conflate
- `σ = 0.7` (Heinrich+2023 canonical) vs `16.85/12.72/11.71` (confabulated, never cited a real source)

## Related
- /bigbounce-site-sync — sister skill, broader scope
- /ssot-update — SSOT carries the canonical claim
- /peer-review-truth-audit — surface where claim mismatches get caught
