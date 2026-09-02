---
title: "Paper A3M SSOT — Multi-channel consistency of the matter-bounce prediction at f_NL = -35/16"
type: ssot
paper: A3M
last_updated: 2026-09-02 — CREATED. v3M.0.2, 6 pp, md5 8f17a2dc877c0b58982e91a8dea0fa1b, sha256 0cbb10215ef286eadf6c21fc9b91b0d551763cfba2c76c0c03a4973319b85e4a, 0 undef refs, 0 overfull hboxes >10pt. Ledger #1 correction: fixed §II wording from "OPEN" to CLOSED per NEXT_SCIENCE_LEDGER.md row 1 (only the Bianchi-I shear cross-check remains open).
canonical_source: research/track_a3_multichannel/paper/main.tex
canonical_pdf: research/track_a3_multichannel/paper/main.pdf (6 pp / 0 undef refs / md5 8f17a2dc877c0b58982e91a8dea0fa1b)
version: v3M.0.2 (2026-09-02, ledger #1 wording fix)
registry_id: A3M (project-context/draft_paper_registry.json)
review_profile: PRD-REGULAR
target_journal: Physical Review D (regular article)
headline_pct: not-yet-reviewed (agent gates: science 25 / evidence 0 / review-convergence 0 / packaging 20 = ~45; no INT/EXT board run yet)
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
   (γ = 2.567 ± 0.382, reproduced from the committed NANOGrav chain), PBH
   abundance (Press–Schechter, new arithmetic; compaction-function row left
   as an explicit "in progress" placeholder per A3-1, no invented numbers),
   and LSS survey reach (DESI DR1 + SPHEREx, cited σ values).
4. §VII discussion + reproducibility statement listing every manifest under
   `reproducibility/manifests/experiments/` (a3-*, p2-fnl-*, p2-a2-*).

**Open gates (not closed by this creation commit):**
- PBH compaction-function redo (item A3-1) — concurrent lane computing into
  `research/track_a3_multichannel/outputs/`; Table II row stays a marked
  placeholder until real numbers land.
- A2 transmission second half — the bounce's own cubic self-interaction term
  is cited (Agullo–Bolliet–Sreenath 2017) but not computed; item on
  next-steps list.
- One full INT review board (Claude Opus INT + Grok API + Gemini API) has not
  yet run on this exact PDF; no EXT sweep yet. Readiness stays at the
  agent-gate composition (~45%) until a review round runs.

**Not edited by this commit (per lineage decision + task scope):** P2L
(`arxiv/paper2prime_fnl_letter/main.tex`), P2
(`research/focused_paper_source_integration/`), and the A3 brief
(`research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md`).
