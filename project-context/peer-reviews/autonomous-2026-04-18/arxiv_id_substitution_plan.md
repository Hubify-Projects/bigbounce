# arXiv-ID Substitution Plan — Post-Submission Cross-Cite Rewiring

**Purpose:** Each of the 4 BigBounce papers cites 1-3 of the other 3 as "companion paper (2026)" placeholder `\bibitem` entries. Once any paper is announced on arXiv with a real ID (e.g., `arXiv:2604.XXXXX`), the other 3 papers' `\bibitem` entries must be rewritten BEFORE those papers are submitted (or submitted as replacements via arXiv's "replace" function).

**Author:** Autonomous arXiv production editor, 2026-04-18
**Depends on:** [`06_arxiv_production_editor.md`](06_arxiv_production_editor.md) submission-order recommendation (Paper 4 → Paper 1 → Paper 3 → Paper 2).

---

## Cross-cite graph (who cites whom)

Keys used across the program:
- `Golden:2026framework` — **Paper 1** (spin-torsion framework)
- `Golden:2026fnl` — **Paper 2** (f_NL SPHEREx/MegaMapper forecast)
- `Golden:2026anomaly` / `Golden:2026anomalies` — **Paper 3** (multi-survey anomaly catalog)
- `Golden:2026chirality` — **Paper 4** (chirality catalog)
- `Golden2026supplement` — Paper 1 internal reference (not a cross-cite)

```
Paper 1 (main.tex)         cites Paper 4 (Golden:2026chirality) -- §VI robustness to spin-null
Paper 2 (02_full_draft.tex) cites Paper 1 (Golden:2026framework)
Paper 3 (paper3_draft.tex)  cites Paper 1 (Golden:2026framework)
                            cites Paper 2 (Golden:2026fnl)
                            cites Paper 4 (Golden:2026chirality)
Paper 4 (chirality_catalog_paper.tex) cites Paper 1 (Golden:2026framework)
```

**Total `\bibitem` entries to rewire: 6** (Paper 1 × 1, Paper 2 × 1, Paper 3 × 3, Paper 4 × 1).

---

## Substitution table — what to edit, in which paper, at which line

### After Paper 4 is announced (recommended submission 1st — target arXiv ID `PAPER4-ID`)

| In paper | File | Line | Current `\bibitem` block | Replace with |
|---|---|---:|---|---|
| Paper 1 | `arxiv/main.bbl` (regenerated from `references.bib`) or bibitem for `Golden:2026chirality` if embedded | search `Golden:2026chirality` | Placeholder/URL-only entry in `references.bib` under `Golden:2026chirality` | `H. Golden, "No Evidence for Large-Scale Parity Violation in Galaxy Morphology: An 8.47-Million-Galaxy Chirality Catalog", arXiv:PAPER4-ID (2026).` — and rerun bibtex to regenerate `main.bbl`. |
| Paper 3 | `pipelines/p3_anomaly_engine/paper3_draft.tex` | 1058-1064 | `\bibitem{Golden:2026chirality} H.\ Golden, "A Galaxy Chirality Catalog of 8.47 Million...", companion paper (2026).` | `\bibitem{Golden:2026chirality} H.\ Golden, "No Evidence for Large-Scale Parity Violation in Galaxy Morphology: An 8.47-Million-Galaxy Chirality Catalog", arXiv:PAPER4-ID (2026).` |

Note: Paper 2 does NOT cite Paper 4 — no edit needed in Paper 2 at this step.

### After Paper 1 is announced (recommended submission 2nd — target arXiv ID `PAPER1-ID`)

| In paper | File | Line | Current `\bibitem` block | Replace with |
|---|---|---:|---|---|
| Paper 2 | `research/focused_paper_source_integration/02_full_draft.tex` | 1040 (and `\cite` call sites at 889, 909) | `\bibitem{Golden:2026framework}` placeholder entry | `\bibitem{Golden:2026framework} H.\ Golden, "Spin-Torsion Cosmology and the Search for Geometric Dark Energy", arXiv:PAPER1-ID (2026).` Also update `focused_paper_refs.bib` entry for `Golden:2026framework` to include the arXiv ID. |
| Paper 3 | `pipelines/p3_anomaly_engine/paper3_draft.tex` | 1043-1048 | `\bibitem{Golden:2026framework} H.\ Golden, "Spin-Torsion Cosmology: A Framework for the Quasi-Matter Bounce", companion paper (2026).` | `\bibitem{Golden:2026framework} H.\ Golden, "Spin-Torsion Cosmology and the Search for Geometric Dark Energy: A Null Result...", arXiv:PAPER1-ID (2026).` |
| Paper 4 | `pipelines/p2_chirality/chirality_catalog_paper.tex` | 1040-1044 | `\bibitem{Golden:2026framework} H.~Golden, "Spin-Torsion Cosmology: Fourteen Structural Barriers...", BigBounce Research (2026), \url{https://bigbounce.hubify.app}.` | `\bibitem{Golden:2026framework} H.~Golden, "Spin-Torsion Cosmology and the Search for Geometric Dark Energy", arXiv:PAPER1-ID (2026).` Also regenerate `chirality_catalog_paper.bbl` via bibtex. |

Because Paper 4 is submitted FIRST (before Paper 1 is announced), Paper 4's `\bibitem{Golden:2026framework}` will be submitted with the URL-placeholder entry. After Paper 1 is announced, Houston should submit a REPLACE on Paper 4 with the rewired bibitem. arXiv's replace mechanism preserves the original submission date; there is no penalty. Alternatively: if Houston is willing to wait for Paper 1 to be announced first, Paper 4 can be submitted after Paper 1 and the rewire is pre-submission — simpler but changes submission order.

### After Paper 3 is announced (recommended submission 3rd — target arXiv ID `PAPER3-ID`)

| In paper | File | Line | Current | Replace with |
|---|---|---:|---|---|
| Paper 2 | `research/focused_paper_source_integration/02_full_draft.tex` | (not a direct cite — per SSOT `P2-XREF-AUDIT`, Paper 2 does NOT cite Paper 3. Skip.) | — | — |

No `Golden:2026anomaly` or `Golden:2026anomalies` cite exists in Paper 2 per SSOT audit. Paper 3's announcement does not trigger any Paper 2 edit.

**However:** if Houston discovers during Paper 2 review that a Paper 3 reference belongs in §4 or §5 (tracer-sample language), add it after Paper 3 arXiv ID is known. Track as optional `P2-ADD-PAPER3-CITE` task.

### After Paper 2 is announced (recommended submission 4th — target arXiv ID `PAPER2-ID`)

| In paper | File | Line | Current | Replace with |
|---|---|---:|---|---|
| Paper 3 | `pipelines/p3_anomaly_engine/paper3_draft.tex` | 1050-1056 | `\bibitem{Golden:2026fnl} H.\ Golden, "SPHEREx / MegaMapper Multi-Tracer $\fnl$ Forecast...", companion paper (2026).` | `\bibitem{Golden:2026fnl} H.\ Golden, "Testing the Matter Bounce with Primordial Non-Gaussianity: SPHEREx and MegaMapper Forecasts", arXiv:PAPER2-ID (2026).` |

Because Paper 3 is submitted BEFORE Paper 2 in the recommended order, Paper 3 carries the placeholder at submission and Houston must issue a REPLACE on Paper 3 after Paper 2 is announced.

No Paper 1 or Paper 4 edits triggered by Paper 2's announcement (neither cites Paper 2).

---

## Replace schedule (ordered)

| Step | After which paper is announced | Papers to REPLACE (via arXiv `replace` form) | Papers to rewire before submission | Papers with now-stale cross-cites that need update |
|---:|---|---|---|---|
| 1 | Paper 4 | — | Paper 1 (before its submission: rewire `Golden:2026chirality` → PAPER4-ID) | — |
| 2 | Paper 1 | Paper 4 (rewire `Golden:2026framework` → PAPER1-ID, REPLACE) | Paper 3 (before submission: rewire both `Golden:2026framework` + `Golden:2026chirality`) | — |
| 3 | Paper 3 | — | Paper 2 (before submission: rewire `Golden:2026framework` → PAPER1-ID; no Paper 3 cite needed per SSOT) | — |
| 4 | Paper 2 | Paper 3 (rewire `Golden:2026fnl` → PAPER2-ID, REPLACE) | — | All four cross-cites now resolve to real arXiv IDs. |

**Total arXiv `replace` operations across the program: 2** (Paper 4 replace, Paper 3 replace). Each takes ~10 min via arXiv web form + 1 announcement cycle.

**Program end-state:** all 4 papers cite each other by arXiv ID. No placeholders.

---

## Operational notes

1. **arXiv `replace` mechanism:** goes to arxiv.org/submit → "Replace" → select paper → upload revised tarball → new version number (v2, v3, ...). Original submission date and paper number are preserved. No penalty.
2. **Timing:** arXiv announces once per day (20:00 UTC). Budget 1 business day between submissions to get the previous paper's arXiv ID before submitting the next.
3. **Shortcut:** If Houston wants to ship all four in one week, submit Papers 1 + 4 + 3 + 2 back-to-back on Day 1 with placeholder entries, then issue 3 `replace` operations on Days 2-5 once IDs are assigned. Net cost: 3 replaces instead of 2, but saves 3-4 business days of waiting. **This is the fastest path.**
4. **What to NOT do:** Don't edit `\bibitem{Golden:2026xyz}` keys themselves — keep the bibkey stable so the `\cite` calls in the body never need updating. Only edit the entry text (title, arXiv ID).
5. **bbl regeneration:** Papers 1 and 4 use `.bbl` files generated by bibtex from a `.bib`. After editing the `.bib` entry, rerun `bibtex BASE && pdflatex BASE && pdflatex BASE` on-pod to regenerate the `.bbl`. Ship the new `.bbl` in the replace tarball.
6. **Paper 2 Paper-3-cite decision:** SSOT says Paper 2 does NOT implicitly cite Paper 3 (the multi-tracer language in §4/§5 is about SPHEREx/MegaMapper as-designed, not about discovered anomaly tracers). Houston should re-confirm during final read; if he wants to add a reference to Paper 3 after it's announced, add `\cite{Golden:2026anomaly}` at the relevant §4/§5 paragraph and include a new bibitem. Optional — not part of this rewiring plan.

---

## Checklist to track completion

- [ ] **After Paper 4 ID assigned** (`PAPER4-ID = arXiv:____`):
  - [ ] Paper 1 `references.bib`: update `Golden:2026chirality` entry
  - [ ] Paper 1 regenerate `main.bbl` via bibtex
  - [ ] Paper 1 rebuild tarball (if not yet submitted) — only needed if Paper 1 is still pending submission
  - [ ] Paper 3 `.tex` L1058-1064: rewire bibitem
- [ ] **After Paper 1 ID assigned** (`PAPER1-ID = arXiv:____`):
  - [ ] Paper 2 `focused_paper_refs.bib`: update `Golden:2026framework` entry
  - [ ] Paper 2 regenerate `.bbl` via bibtex
  - [ ] Paper 3 `.tex` L1043-1048: rewire bibitem
  - [ ] Paper 4 `.tex` L1040-1044: rewire bibitem
  - [ ] Paper 4 regenerate `chirality_catalog_paper.bbl` via bibtex
  - [ ] Paper 4 REPLACE on arXiv (if already submitted)
- [ ] **After Paper 3 ID assigned** (`PAPER3-ID = arXiv:____`):
  - [ ] No automatic edits (Paper 2 optional — Houston decision)
- [ ] **After Paper 2 ID assigned** (`PAPER2-ID = arXiv:____`):
  - [ ] Paper 3 `.tex` L1050-1056: rewire bibitem
  - [ ] Paper 3 REPLACE on arXiv
- [ ] **Program complete:** all four papers cross-cite by real arXiv ID. Update `project-context/SSOT/index.md` with all four IDs. Update `paper.html` and `activity.html` on the website.
