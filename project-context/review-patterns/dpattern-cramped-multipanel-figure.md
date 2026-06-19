---
pattern_id: dpattern-cramped-multipanel-figure
status: seeded
first_seen: D1-2026-06-19
papers_observed: []
proposed_by: paper-design-round 2026-06-19
---

# dpattern-cramped-multipanel-figure — Multi-panel figure cramped in one column

## Defect

A figure with 2–4 side-by-side panels is placed in a single-column `figure` float.
Each panel is compressed to ~1.5 in wide, making axis labels, tick values, and
legend text illegible at print scale. The figure communicates nothing to a reader
who does not zoom in.

## How to detect

- Visual: pdftoppm render — any figure where legend or axis text is visually
  indistinguishable at 150 dpi is cramped.
- Source grep: `grep -n 'subfloat\|subfigure\|includegraphics.*width=0\.[0-9].*includegraphics'`
  — two or more `\includegraphics` on adjacent lines inside a single `figure` env.

## Fix

Promote to `figure*` (full text-width). Also consider: increase the individual
panel `width=` fractions to fill the text width, enlarge font sizes in the
generating script (matplotlib `rcParams['font.size'] = 12` minimum for print),
and rerun the figure script to regenerate at the new size. Verify the new PNG
reaches the directory the `.tex` `\includegraphics` reads from (see
`dpattern-figure-dir-desync`).
