---
pattern_id: dpattern-missing-structure-schematic
status: seeded
first_seen: D1-2026-06-19
papers_observed: []
proposed_by: paper-design-round 2026-06-19
---

# dpattern-missing-structure-schematic — Section with no figures reads as a wall of text/equations

## Defect

A section that presents a multi-step analysis pipeline, a theoretical framework,
or a comparative summary contains only text and equations — no diagram, flowchart,
or schematic. A reader cannot grasp the structure at a glance. External reviewers
(and the D-round visual pass) flag these sections as "crying out for a figure."

## How to detect

- Visual: in the rendered PDF, a section spanning >1.5 columns contains only
  inline equations or prose with no float.
- Source: identify sections with dense equation blocks:
  ```bash
  grep -c 'begin{equation\|begin{align\|begin{eqnarray' paper.tex
  # Then grep the surrounding section headings
  ```
- The D-round Opus sub-agent explicitly hunts these (addendum opportunities).

## Fix

Add a schematic figure:
- **Pipeline diagram**: a simple `tikzpicture` or an external PNG box-and-arrow
  diagram illustrating the analysis stages.
- **Summary table**: if the section compares N methods/models, a `table*`
  comparison is often clearer than prose.
- **"Money figure"**: a single plot that makes the headline result legible at
  a glance (Houston's phrase: "a money figure that makes the result legible").

Prefer generating the figure from committed code so it is reproducible. Place
it as `figure*` if it spans both columns.
