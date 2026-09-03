# Final author/visual review recommendations — 2026-09-02 (orchestrator, Fable 5.1)

Directive P composition: science closure 25 + evidence/reproducibility 25 +
automated review convergence 25 + packaging/PDF hygiene 20 = 95 when all four
agent gates hold; 100 only with Houston's per-paper sign-off (quote in SSOT).
Publishing mechanics (endorsement, venue submission, journal review) are a
separate phase and never subtract from the score.

## P4′ — `pipelines/p4prime_chirality_test/paper/` v4P.0.5 (ApJS) — **APPROVE** (agent gates), readiness → 95
- Boards: R1 (Claude major / Grok reject / Gemini reject) → 20 items closed;
  R2 (Claude major / Grok reject / Gemini major) → 21 closed incl. the
  primary-support monopole resolved from committed artifacts and a real
  Neyman-inversion 95% CL limit (0.75%); R3 verification (Claude minor /
  Grok reject / Gemini minor) → 7 editorial items closed. Truth-audits found
  no arithmetic or measurement-layer error in any round. Rounds stop (R2).
- Visual pass (pages 1, 2, 7, 11 at 55 dpi + full render): two-column
  AASTeX clean, no overflow, tables legible, Fig. 3 error bars readable,
  references resolve to DOIs/URLs; the P5 source is cited at its served URL
  with an honest "no DOI" note.
- Framing check: abstract names the detection-power floor (0.98%) and the
  CL limit (0.75%) with their exact meanings, concedes Shamir 2022's larger
  primary sample, and states that Popławski's papers give no quantitative
  amplitude. No bounce claim. Directive Q1 clean.
- Packaging: arXiv tarball `SSOT/arxiv_tarballs/paper4prime_chirality_test_arxiv_v4P.0.5.tar.gz`
  sha256 fbab03801b63483b86006095a3f86d0e4511f64766b90649a76548583fd51c92,
  standalone recompile PASS; PDF md5 f0d874e93cebf95f86e408f780f002e0 mirrored;
  Convex k576j98m….
- REVISE (abstract cap) executed 2026-09-02 → v4P.0.5: abstract trimmed to
  246 words, no science change; tarball rebuilt and re-verified.
- Residual (not blocking, for Houston's read): (i) P5 has no Zenodo DOI —
  mint one as a new version under the P4 concept or as its own record before
  ApJS submission (click-list); (ii) the "Draft version" AASTeX header is
  standard and disappears at submission.
- Next phase: astro-ph.GA endorsement (CLVMAQ) → arXiv → ApJS portal
  (fields in `SSOT/PORTAL_KITS_2026-09-02.md`).

## ECH Note (P1N) — `arxiv/paper1bc_ech_note/` v1N.0.5 (CQG, article type Paper) — **APPROVE** (agent gates), readiness → 95
- Boards: R1 (Claude major / Grok reject / Gemini reject; Gemini's sign and
  Fierz claims FALSIFIED against the settled theory-audit artifacts) → 19
  closed incl. three regressions vs P1C v1C.0.16; R2 (Claude major / Grok
  reject / Gemini major) → 23 closed incl. two errors INHERITED from the
  frozen P1C (8π coefficient, O5 parity), four science/scope decisions
  recorded; R3 verification (Claude major / Grok reject / Gemini major) →
  15 closed, seven of them regressions the R2 closure had introduced, now
  guarded by machine-checkable assertions
  (`research/theory_audit/p1n_r3_checks_2026_09_02.py`). Rounds stop (R2).
- Visual pass (pages 1, 6 at 55 dpi + full render): revtex two-column clean,
  equations legible, no overflow; no directive-Q1 language in the PDF (the
  three matching strings are tex comments).
- Framing check: the Popławski identification is stated as the γ→∞
  reduction with the finite-γ suppression and trace-vector dominance made
  explicit; the fourteen barriers carry honest tags (derived / argued /
  heuristic); the abstract promises a channel-level, not operator-level,
  closure. No mistake-narration.
- Packaging: tarball `SSOT/arxiv_tarballs/paper1bc_ech_note_arxiv_v1N.0.5.tar.gz`
  sha256 26f215d635b2e577c32b7869a5129681109b601250fa054c90ba7c817659a33a,
  standalone recompile PASS; PDF md5 6836eb995effef298cca6830b1beda7c; Convex
  k572az66….
- REVISE (abstract cap) executed 2026-09-02 → v1N.0.5: abstract trimmed to
  298 words (CQG word cap), no science change; tarball rebuilt and re-verified.
- Residual for Houston's read: (i) DP1N-58 — no Zenodo DOI exists yet for
  the P1C survey or the theory-audit artifacts; mint a new version under the
  P1A concept (21481837) before CQG submission (click-list); (ii) the
  internal erratum note on P1C v1C.0.16 (8π) stays internal; P1C is not
  re-issued.
- Next phase: gr-qc endorsement (HYEJ7S) → arXiv → CQG ScholarOne as a
  Paper (the ≤2500-word Note form does not fit).

## P2′ — `arxiv/paper2prime_fnl_letter/` v2L.0.2 — **DEFER** (archived theory record; content folded into A3)
- R1 board (Fable major / Grok reject / Gemini major) and truth-audit: the
  Letter's −35/16 is already printed by Li+2016 (Eq. 4.19) and quoted by
  Quintin+2015; its genuine contribution (independent from-scratch
  confirmation, the located ×2 in Cai+2009, δN reconciliation) is a
  confirmation and does not carry a standalone Letter. Defects closed
  honestly in v2L.0.2; scope decision recorded in PAPER_LINEAGE; content now
  §II–III of the A3 multi-channel paper (`research/track_a3_multichannel/paper/`
  v3M.0.2). No submission; optional future Comment on Cai+2009.

## A3 multi-channel paper (A3M) — `research/track_a3_multichannel/paper/` v3M.0.5 (PRD regular article) — **REVISE then DEFER submission**, readiness → 70
- Boards: R1 (Fable major / Grok reject / Gemini major) → 20 items closed with
  decisions D1–D3 (official NANOGrav posterior primary, tail Bayes factors
  dropped; transmission bound handoff-conditional; PBH ratio kept with regime
  and non-monotonicity disclosed); R2 verification (Fable minor 0 MAJOR /
  Grok reject / Gemini major) → 16 items closed incl. a real γ=13/3 and γ=3
  injection through the 30-bin likelihood (pulls −0.03σ / +0.07σ) replacing
  a misdescribed validation; Gemini's PBH-formula claim FALSIFIED by re-run.
  Automated review CONVERGED; rounds stopped (R2 budget 2/2).
- Visual pass (pages 1, 5 at 55 dpi + full render): two-column clean, tables
  and equations legible, no overflow.
- Framing: honest to a fault — every channel stated at its evidential
  strength; the joint statement claims consistency, not detection.
- Packaging: tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.5.tar.gz`
  sha256 cd2ce1ef…, standalone recompile PASS; Convex k57fxwc5….
- REVISE (agent-doable next session): abstract ~600 words → PRD length;
  re-run the 30-bin injection on the real NANOGrav KDE grids (restore from
  HF/B2) so the validation no longer relies on a synthetic per-bin density.
- DEFER submission until the science gate closes: the method-independent
  f_NL cross-check (Bianchi-I separate universe), the bounce's own cubic term
  (ledger #2 second half), and an in-lab Δ²_ζ for the PBH channel (A3-1b).
  Readiness 70 = evidence 25 + convergence 25 + packaging 20 + science 0 of
  25 (gate open) — the science items are the vision's next work, not
  editorial.
- This is the Track-A submission candidate; the astro-ph.CO endorsement
  (LRZHC4) is reserved for it.

