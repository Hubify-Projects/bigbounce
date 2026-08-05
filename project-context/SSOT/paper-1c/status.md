# P1C status — current authoritative section

**Current candidate:** draft v1C.0.2 · 2026-08-05 ·
`arxiv/paper1c_nogo_survey/main.tex`

**Status: INTERNAL READ-THROUGH DONE → CLOSURES LANDED (v1C.0.2). Next
gate: full INT board.** The 2026-08-05 internal referee read-through of
v1C.0.1 (exact-PDF-bound, sha 847fb143;
`project-context/peer-reviews/INT_v3/ROUND_2026-08-05-P1C-v1C.0.1-EXACTPDF-847fb143-INTERNAL-READTHROUGH/`)
returned 9 MAJOR + 11 MINOR, verdict major-revisions. All 20 findings are
dispositioned in the round's `CLOSURE_NOTES_v1C.0.2.md`; the closures landed
as v1C.0.2 (figure/list rebuild to 0 overfull boxes, Fierz
convention/discrepancy note, kappa-vs-imported-kappa~ convention split,
41→61-order fix, B14→Branch H assignment propagated, division-of-content
paragraph vs published P1A, R2/R3 reframed as historical-route amplitude
budgets). No readiness percentage is claimed — zero INT/EXT board rounds,
zero convergence evidence, zero packaging/venue work; do not read it against
the 6-candidate readiness contract until real board gates have run.

## What this is

"A Structural No-Go Survey of Minimal Spin-Torsion Routes to Dark Energy and
Bounce Phenomenology." A systematic survey of 7 foundation mechanism classes
(A-G) and 6 observational branches (H, J, L, M, N, O), collapsing to 13
distinct mechanism-class constraints across 14 catalog entries, closing four
candidate dark-energy routes (R1-R4). Companion to P1A: cites P1A's
torsion-elimination (Route 1) and zero-spin-branch transparency results
rather than re-deriving them.

## Provenance

Extraction, not new derivation. Source: `arxiv/paper1_unified.tex`
`sec:barriers` (the frozen 6,898-line pre-split P1U draft — table
`tab:barriers`, TikZ figure `fig:barrier_map`, per-barrier `\item[B1]`...`[B14]`
prose), retired from the reader-visible paper at the 2026-07-14 P1 split
(`project-context/peer-reviews/INT_v3/ROUND_2026-07-13-M44-NONANTHROPIC/P1_SPLIT_CLOSURE.md`)
because M44 non-Anthropic external review found P1U's broad four-route
rhetoric outran what was tightly derived — the closure cut rather than
relabeled, but the barrier content itself was never invalidated and
`paper1_unified.tex` was explicitly not edited. Ancestor derivation:
`research/paper1_salvage_alp/01_salvage_map.md`, `05_claims_table.md`,
`final_verdict.md` (2026-03-17). A standalone source write-up also exists at
`research/focused_paper_source_integration/paper3_barriers_ech_transparency.tex`/`.pdf`.

Decision record: `project-context/PAPER_LINEAGE_2026-08-05.md` Sec. 4(a) and
its "Decision record — 2026-08-05" (agent-executed under Houston's explicit
full delegation, item 1: "No-go survey paper: RESURRECT"). Extraction is a
pure-contribution reframe under directive Q1 — the paper's thesis is the
no-go survey itself, not a narration of the P1 split.

## Registry

`project-context/paper_registry.json` → `companion_manuscripts.P1C`.
`tex_path`/`pdf_path` both under `arxiv/paper1c_nogo_survey/`. Not one of the
six campaign-roster papers (P1A, P1B, P2, P3, P4, P5) tracked in the
readiness contract table.

## Compile state

v1C.0.2: 16 pp, 0 errors, 0 undefined refs, 0 overfull hboxes, compiled
clean 2026-08-05 (`arxiv/paper1c_nogo_survey/main.pdf`). Mirrored
byte-identical to `site/public/papers/paper1c_nogo_survey_v1C.0.2.pdf` and
`public/papers/paper1c_nogo_survey_v1C.0.2.pdf` (md5
`3293e7244ab0705f6aabbef6e10f11ee`, all three copies match). Prior v1C.0.1
mirrors retained. `/latex-audit` visual pass run on the recompile (figure
page, barrier-list page, App-B page rendered and inspected; no column
overflow, no box overprint).

## What has NOT happened (explicit, so nobody assumes otherwise)

- No INT review round (Claude/Grok/Gemini or otherwise)
- No EXT review round (ChatGPT/Grok/Gemini browser sweep)
- No truth-audit, no finding dispositions
- No readiness percentage computed or claimed
- No Convex `paperVersions` row, no `rRounds`/`externalReviews` entries
- No Zenodo DOI, no venue kit, no arXiv submission prep
- Not added to `papers[]` in `site/src/data/papers.ts` (would imply the
  version-chip/PDF-mirror/publication-path machinery every roster paper
  carries); surfaced instead as a `bounce-theory` program `supportingLinks`
  entry labeled "In preparation," matching the P1B-MCMC-companion precedent
  (commit `cbe93641`)

## Next gates (in order)

1. ~~Internal read-through~~ DONE 2026-08-05 (9 MAJOR + 11 MINOR, all
   dispositioned; closures landed as v1C.0.2 — see
   `ROUND_2026-08-05-P1C-v1C.0.1-EXACTPDF-847fb143-INTERNAL-READTHROUGH/CLOSURE_NOTES_v1C.0.2.md`)
2. INT board (Claude Opus INT leg + Grok API + Gemini API, per directive N
   routing) — first full review round on the v1C.0.2 PDF
3. D/P rounds (visual + packaging) only after INT/EXT convergence, per the
   standard readiness ladder (R-rounds converge -> 96 -> D-round -> 98 ->
   P-round -> 99 -> Houston sign-off -> 100)

Open deferred item (from the read-through closure): the Fierz-convention
reconciliation between the monolith's App-B presentation (Itzykson–Zuber
matrix + eq:AAdecomp coefficients) and the released
`fierz_lemma_check.py`/published-P1A Nieves–Pal convention is DEFERRED to a
dedicated convention audit; v1C.0.2 discloses the difference in-paper and no
longer claims script verification of the printed display. Until the INT
board runs, this file should not grow a readiness number or a "converged"
claim.
