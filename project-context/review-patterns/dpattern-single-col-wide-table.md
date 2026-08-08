---
pattern_id: dpattern-single-col-wide-table
status: seeded
first_seen: D1-2026-06-19
papers_observed: []
proposed_by: paper-design-round 2026-06-19
---

# dpattern-single-col-wide-table — Wide table squished into a single column

## Defect

A multi-column data table is placed in a single-column `table` float. In a
two-column revtex layout the table is squished to ~3.25 in wide, which forces
awkward column wrapping, tiny fonts, or horizontal overflow into the margin. The
compiled PDF looks broken; a reviewer reading on screen at 100% cannot read it.

## How to detect

- Visual: render the PDF page as an image (`pdftoppm -r 150 -png`) and look for
  tables where the columns are visibly crowded or the text is ≤7 pt.
- Log: `grep "Overfull .hbox" paper.log` will often fire on the same page.
- Source grep: `grep -n '\\begin{table}' paper.tex` — any table with ≥5 columns
  or ≥40-char entries is a candidate for promotion to `table*`.

## Fix

Replace `\begin{table}` / `\end{table}` with `\begin{table*}` / `\end{table*}`.
If the content still overflows in two-column-wide mode, switch the inner tabular
to `\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}…}` or `\resizebox{\textwidth}{!}{…}`.
Recompile and verify visually with pdftoppm.
