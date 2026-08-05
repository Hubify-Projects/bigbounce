# P1C status — current authoritative section

**Current candidate:** draft-extraction v1C.0.1 · 2026-08-05 ·
`arxiv/paper1c_nogo_survey/main.tex`

**Status: NEW DRAFT — not yet in the review pipeline.** No readiness
percentage is claimed. This is a compiled, registered manuscript with zero
review rounds, zero automated-convergence evidence, and zero packaging/venue
work — do not read it against the 6-candidate readiness contract (science 25 +
evidence 25 + convergence 25 + packaging 20 + Houston sign-off 5) until real
gates have actually run.

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

15 pp, 0 undefined refs, compiled clean 2026-08-05
(`arxiv/paper1c_nogo_survey/main.pdf`, 474,242 bytes). Mirrored byte-identical
to `site/public/papers/paper1c_nogo_survey_v1C.0.1.pdf` and
`public/papers/paper1c_nogo_survey_v1C.0.1.pdf` (md5
`eb73f83fbe9843b2e4effc32a4f5914b`, all three copies match).

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

1. Internal read-through (Houston or delegated agent) confirming the
   extracted catalog reads correctly as a standalone paper, independent of
   P1U/P1A framing
2. INT board (Claude Opus INT leg + Grok API + Gemini API, per directive N
   routing) — first review round, first real findings
3. D/P rounds (visual + packaging) only after INT/EXT convergence, per the
   standard readiness ladder (R-rounds converge -> 96 -> D-round -> 98 ->
   P-round -> 99 -> Houston sign-off -> 100)

Until gate 1 runs, this file should not grow a readiness number, a version
bump beyond editorial fixes, or a "converged" claim.
