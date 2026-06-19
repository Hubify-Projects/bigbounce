---
pattern_id: dpattern-colorbar-label-overlap
status: seeded
first_seen: D1-2026-06-19
papers_observed: []
proposed_by: paper-design-round 2026-06-19
---

# dpattern-colorbar-label-overlap — Colorbar tick labels overlap the colorbar or adjacent panel

## Defect

In a matplotlib figure, the colorbar is placed too close to the main axes or to
an adjacent subplot panel. Tick labels on the colorbar overlap with axis tick
labels or bleed into the adjacent panel. This is only visible in the rendered
PDF — reviewing the `.tex` cannot catch it.

## How to detect

- Visual only: pdftoppm render at ≥150 dpi, zoom into colorbar region.
  Overlap is visible as two text strings occupying the same pixel region.
- Cannot be caught from source alone; the `.tex` `\includegraphics` call gives
  no information about internal figure layout.

## Fix

In the generating Python script:
```python
# Add padding between colorbar and axes
fig.colorbar(im, ax=ax, pad=0.02)   # increase pad (default 0.05 is often too small)

# Or use a dedicated axes for the colorbar
from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
fig.colorbar(im, cax=cax)
```
After fixing, regenerate the PNG, confirm it lands in the directory the `.tex`
reads from (`dpattern-figure-dir-desync` check), recompile, and pdftoppm the
page to visually confirm the overlap is gone.
