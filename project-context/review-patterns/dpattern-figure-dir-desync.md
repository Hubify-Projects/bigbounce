---
pattern_id: dpattern-figure-dir-desync
status: seeded
first_seen: D1-2026-06-19
papers_observed: [P5]
proposed_by: paper-design-round 2026-06-19
---

# dpattern-figure-dir-desync — Regenerated figure written to wrong directory (silent persistence failure)

## Defect

A figure-generation script writes the new PNG (or PDF) to `figures/` while the
`.tex` source's `\includegraphics` path resolves to `paper/` (or vice versa).
The recompile succeeds — because the OLD figure file is still present in
`paper/` — but the D-round visual fix never reaches the compiled PDF. The paper
looks unchanged after the fix.

**First confirmed case**: P5 D1 2026-06-19. Script `11_make_p5_paper_figures.py`
wrote output to `pipelines/p5_desi_chirality/figures/` while the `.tex` in
`pipelines/p5_desi_chirality/paper/` used `\graphicspath{{./}}` and expected
PNGs in `paper/`. The regenerated figures were invisible to pdflatex.

## How to detect

After any figure-generation step:

```bash
# Check where the script writes
grep -n 'savefig\|imsave\|write_image' <script>.py

# Check where the .tex reads from
grep -n 'graphicspath\|includegraphics' paper.tex

# Confirm the file timestamps match
ls -lt figures/ paper/*.png | head -20
```

If `savefig` path ≠ `\includegraphics` path root, this pattern is firing.

## Fix

Either (a) update the generation script to write into the directory the `.tex`
expects, or (b) add a post-generation `cp figures/*.png paper/` step, or (c)
adjust `\graphicspath` to point at the correct output directory. After the fix,
verify that the file timestamp in the target directory is newer than the old
file, then recompile and pdftoppm-render the affected pages to confirm the new
figure is visible.

## Mandatory silent-persistence check (from `/paper-design-round` Phase 3)

After EVERY figure regeneration, before declaring a D-round fix complete:
1. Confirm the new file's mtime in the directory `\includegraphics` reads from.
2. Recompile from scratch (not cached).
3. pdftoppm the affected page and visually confirm the new content is present.
