---
pattern_id: dpattern-inline-artifact-path-clutter
status: seeded
first_seen: D1-2026-06-19
papers_observed: []
proposed_by: paper-design-round 2026-06-19
---

# dpattern-inline-artifact-path-clutter — Raw file paths typeset in \texttt{} overflow the column

## Defect

Artifact paths like `\texttt{pipelines/p5\_desi\_chirality/scripts/11\_make\_p5\_paper\_figures.py}`
are written inline with raw `\texttt{}`. In a two-column revtex layout these
long strings overflow the column boundary, producing an overfull `\hbox` warning
and visible text bleeding into the adjacent column or the margin. The compiled
PDF looks broken at those lines.

## How to detect

```bash
# Find raw \texttt{} with path-shaped content (slashes or underscores)
grep -n '\\texttt{[^}]*[/_][^}]*}' paper.tex

# Check the log for overfull hbox on the same lines
grep -n 'Overfull .hbox' paper.log
```

## Fix

Replace inline `\texttt{long/path}` with the project's `\artifact{}` macro (or
define one):
```latex
\newcommand{\artifact}[1]{\texttt{\small\path{#1}}}
```
`\path{}` (from the `url` package) allows line-breaking at `/` and `_` characters.
Alternatively, move long paths into a footnote, a dedicated "Data availability"
section, or a `\url{}` hyperlink. Recompile and confirm zero overfull `\hbox`
on those lines.
