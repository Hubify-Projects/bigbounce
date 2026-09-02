---
title: "Paper A3M SSOT — Multi-channel consistency of the matter-bounce prediction at f_NL = -35/16"
type: ssot
paper: A3M
last_updated: 2026-09-02 — v3M.0.3. PBH compaction-function channel (item A3-1) integrated: 7 pp, md5 9f7afea9e22a7816168fc7638fc8a753, 0 undef refs, 0 overfull hboxes >10pt (largest 2.7pt). Press-Schechter first-pass placeholder row replaced with the real compaction-function result — ordering REVERSES (f_PBH(-35/16) < f_PBH(-35/8) at every grid point; first pass had it backwards). Prior: 2026-09-02 CREATED. v3M.0.2, 6 pp, md5 8f17a2dc877c0b58982e91a8dea0fa1b. Ledger #1 correction: fixed §II wording from "OPEN" to CLOSED per NEXT_SCIENCE_LEDGER.md row 1 (only the Bianchi-I shear cross-check remains open).
canonical_source: research/track_a3_multichannel/paper/main.tex
canonical_pdf: research/track_a3_multichannel/paper/main.pdf (7 pp / 0 undef refs / md5 9f7afea9e22a7816168fc7638fc8a753)
version: v3M.0.3 (2026-09-02, PBH compaction-function channel integrated)
registry_id: A3M (project-context/draft_paper_registry.json)
review_profile: PRD-REGULAR
target_journal: Physical Review D (regular article)
headline_pct: not-yet-reviewed (agent gates: science 25 / evidence 25 / review-convergence 0 / packaging 20 = ~70; no INT/EXT board run yet)
submission_status: draft, unreviewed — first INT/EXT board pending

# A3M status — current authoritative section

**Origin.** Executes the lineage decision recorded in
`project-context/PAPER_LINEAGE_2026-08-05.md`, "Decision record — 2026-09-02
(evening): P2′ Letter → theory section of the A3 multi-channel paper": the P2′
Letter's genuine contribution (an independent from-scratch in-in confirmation
of −35/16, not a new discovery) is folded into this paper's theory section
rather than standing as its own PRD Letter.

**What A3M contains:**
1. §II "The exact matter-contraction amplitude" — folded from
   `arxiv/paper2prime_fnl_letter/main.tex` v2L.0.2: setup + validation
   (de Sitter and ultra-slow-roll limits), the per-vertex table (Table I),
   the located ×2 discrepancy with Cai et al. 2009, consistency with
   Li et al. 2016 Eq. 4.19, and the δN/comoving reconciliation
   (ζ_ρ = 2ζ_c at linear order). Ledger item #1 (independent second-method
   adjudication of the factor of two) is CLOSED per NEXT_SCIENCE_LEDGER.md
   row 1 — the from-scratch in-in computation of Table I IS the independent
   route and reproduces −35/16; the δN cross-check reconciles a distinct
   uniform-density quantity, not a second adjudication. The one remaining
   open sub-item is a Bianchi-I separate-universe cross-check of the shear
   response (v3M.0.2 fix, 2026-09-02, corrects v3M.0.1's erroneous "OPEN"
   wording).
2. §III "Transmission through the bounce" — the linear bound
   0 < T_fNL ≤ 1/2 across three bounce backgrounds/two mode-function
   conventions, with the bounce's own (uncomputed) cubic term flagged via
   Agullo–Bolliet–Sreenath 2017.
3. §IV–VI — the A3 skeleton's real channel numbers: PTA slope
   (γ = 2.567 ± 0.382, reproduced from the committed NANOGrav chain); PBH
   abundance via the compaction-function formation criterion (item A3-1,
   CLOSED at ratio-level 2026-09-02) — the first-pass Press–Schechter result
   is kept as context but its ordering is explicitly reversed in-paper: at
   fixed curvature amplitude f_PBH(-35/16) < f_PBH(-35/8) at every point of a
   27-point (Δ, r_p, C_th) grid; the robust output is the required-amplitude
   ratio A(-35/16)/A(-35/8) = 1.732 [1.610, 1.809] (std 0.050), NOT a
   quotable f_PBH (it moves >100 dex with the unreconstructible spectrum
   shape, per PBH_COMPACTION_NOTE_2026-09-02.md); and LSS survey reach
   (DESI DR1 + SPHEREx, cited σ values).
4. §VII discussion + reproducibility statement listing every manifest under
   `reproducibility/manifests/experiments/` (a3-*, including
   a3-pbh-compaction-fnl.json, p2-fnl-*, p2-a2-*).

**PBH gate status:** CLOSED as ratio-level result; abundance not quotable.
Real compaction-function computation supersedes the Press-Schechter first
pass; the amplitude ratio (Eq. 9 of the paper) is the one number this channel
supports until the primordial spectrum is predicted in-lab (open items below).

**Open items (not closed by this commit):**
- A3-1b — in-lab prediction of the matter-bounce contraction-phase curvature
  spectrum, to replace the lognormal stand-in and turn the PBH amplitude
  ratio into a quotable abundance.
- A3-1c — resolve the γ_cr ≲ 0.85 enhancement-branch discrepancy against
  Choudhury et al. 2025 (unresolved: depends on their unreconstructible
  spectrum shape).
- A3-1d — extend the PBH grid to a mass-integrated abundance (their Eq. 66)
  rather than the single M_H = 10^20 g point.
- A2 transmission second half — the bounce's own cubic self-interaction term
  is cited (Agullo–Bolliet–Sreenath 2017) but not computed; item on
  next-steps list.
- One full INT review board (Claude Opus INT + Grok API + Gemini API) has not
  yet run on this exact PDF; no EXT sweep yet. Readiness stays at the
  agent-gate composition (~70%) until a review round runs.

**Not edited by this commit (per lineage decision + task scope):** P2L
(`arxiv/paper2prime_fnl_letter/main.tex`), P2
(`research/focused_paper_source_integration/`), and the A3 brief
(`research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md`).
