---
name: bigbounce-paper-pdf-mirror
version: 0.1.0
description: |
  Mirror a compiled paper PDF to every hosting path: public/papers/ (legacy
  static site) and site/public/ (Next.js site). Both must serve the same PDF.
  If only one is updated, one of the two site surfaces shows the stale PDF.
triggers:
  - mirror pdf
  - copy paper pdf
  - publish pdf
---

# /bigbounce-paper-pdf-mirror — publish PDF to all hosting paths

**Source:** AGENTS.md "Publishing PDFs to the Website"; AGENT_RULES.md §4.2
**Scope:** bigbounce-only
**Trigger:** after `/pdf-restamp-bundle` recompile

## What this skill does

Copies a freshly-compiled PDF to every mounting path so both the legacy static HTML site and the new Next.js site serve the same version.

## The hosting paths

| Path | Served by | Audience |
|------|-----------|----------|
| `public/papers/<paper>.pdf` | Legacy static HTML pages (paper.html, galaxy-explorer.html) | Existing inbound links |
| `site/public/papers/<paper>.pdf` | Next.js site at `site/` | New default audience |
| `arxiv/<paper>.pdf` | source of truth (compiled artifact) | — |

## Copy commands

```bash
# After /paper-compile-revtex completes
PAPER=p5_desi_chirality
SRC=arxiv/${PAPER}.pdf   # or pipelines/p5_desi_chirality/paper/${PAPER}.pdf for P5

# Mirror to both
cp "$SRC" public/papers/${PAPER}.pdf
cp "$SRC" site/public/papers/${PAPER}.pdf

# Verify file sizes match
ls -l "$SRC" public/papers/${PAPER}.pdf site/public/papers/${PAPER}.pdf
```

## Per-paper canonical source + mirror map

| Paper | Source | Mirror to |
|-------|--------|-----------|
| P1A | `arxiv/paper1a_ech_nogo.pdf` | `public/papers/`, `site/public/papers/` |
| P1B | `arxiv/paper1b_mcmc_companion.pdf` | `public/papers/`, `site/public/papers/` |
| P2 | `research/focused_paper_source_integration/02_full_draft.pdf` | both |
| P3 | `pipelines/p3_anomaly_engine/paper3_draft.pdf` | both |
| P4 | `pipelines/p2_chirality/chirality_catalog_paper.pdf` | both, plus `public/images/chirality/` |
| P5 | `pipelines/p5_desi_chirality/paper/p5_desi_chirality.pdf` | both |

## Hard gates

- [ ] PDF copied to ALL hosting paths for the paper
- [ ] File sizes match across copies (within rounding)
- [ ] md5 / sha256 matches between source and mirrors
- [ ] No stale PDF lingering at any path

## Anti-patterns

- Updating only `public/papers/` → Next.js site (the new default) still serves stale
- Updating only `site/public/` → existing inbound links still hit stale
- Forgetting to recompile before mirror → mirroring an old PDF

## Verification snippet

```bash
for path in arxiv/${PAPER}.pdf public/papers/${PAPER}.pdf site/public/papers/${PAPER}.pdf; do
  if [ -f "$path" ]; then
    echo "$(md5 -q "$path")  $path"
  else
    echo "MISSING  $path"
  fi
done
# All hashes should match
```

## Related
- /pdf-restamp-bundle — the bundle this is part of
- /paper-compile-revtex — the recompile this depends on
- /bigbounce-site-sync — refresh HTML/Next.js metadata around the mirrored PDF
