# EXT22 External-Review Consolidation — Truth Audit

**Round:** EXT22 (confirm round on R52-closed PDFs)
**Date:** 2026-06-26
**Auditor:** Opus director + 6 parallel per-paper audit lanes
**Input:** 18 EXT22 reports (P1A/P1B/P2/P3/P4/P5 × {chatgpt, grok, gemini})
**Priors:** R52_*_TRUTH_AUDIT.md, EXT21_CONSOLIDATION.md
**Dispatch result:** all 18 legs returned MINOR REVISIONS or ACCEPT — 0 MAJOR, 0 REJECT, 0 BLOCKER.

Calibration rules applied: pattern-061 (judge by in-text Recommendation, ignore
dispatch tags), pattern-062 (reviewers may flag already-fixed items — check
CURRENT source), pattern-063 (math/coefficient "garbled" findings default to
extraction-artifact FALSIFIED until checked against SOURCE .tex). Standard
June-2026 dating / arXiv 25xx-26xx validity / deliberate-placeholder /
labeled-allowance / catalog-extensiveness calibration.

---

## Per-paper disposition

### P1A — `arxiv/paper1a_ech_nogo.tex` — **1 NEW VERIFIED (MINOR)**

**NV-P1A-1 — Discussion §XII.B states a closure mechanism not in the body (MINOR).**
- **L2698–2701:** "The condensate route fails because the scalar/pseudoscalar
  channel is **repulsive at $\gamma=0.274$ and subcritical**. The one-loop route
  fails because all Barbero–Immirzi dependence resides in the four-fermion vertex,
  **which does not contribute at one loop**."
- **Defect:** The body closes Route 1 by **Planck/amplitude suppression**, not by
  channel repulsiveness/subcriticality. `\subsection{Route 1 (NJL four-fermion
  contact): closed by Planck suppression}` (L1628); $\rho_{\rm NJL}\sim
  4\times10^{-81}\,$eV$^4$, ~69 orders below $\rho_\Lambda$ (L1662). A repo-wide
  grep for `repulsiv|subcritical|critical coupling|attractiv` returns ZERO hits in
  the P1A physics body — the NJL channel-attractiveness/subcriticality argument
  appears nowhere except this Discussion sentence. The sentence also contradicts
  its own preceding summary line (L2694–2696): "R1 closes via the standard
  published derivation; R2–R3 close at the amplitude level under
  explicitly-labeled scaling/ansatz assumptions." For a channel-level *closure*
  paper, the Discussion asserting a different closure reason than the body is a
  genuine inconsistency (pattern-036-adjacent: Discussion claim not supported by
  the body derivation). VERIFIED.
- **Proposed edit** (file:line `arxiv/paper1a_ech_nogo.tex` L2698–2701):
  - current → "The condensate route fails because the scalar/pseudoscalar channel
    is repulsive at $\gamma=0.274$ and subcritical. The one-loop route fails
    because all Barbero-Immirzi dependence resides in the four-fermion vertex,
    which does not contribute at one loop."
  - proposed → "The condensate route is closed at the amplitude level
    (Sec.~\ref{sec:r1_njl}): the NJL contact term is Planck-suppressed
    ($\rho_{\rm NJL}\sim n_\psi^2/\MPl^2 \approx 4\times10^{-81}\,$eV$^4$, ${\sim}69$
    orders below $\rho_\Lambda$) and parity-even. The one-loop route is
    amplitude-closed under the explicitly-labeled EFT scaling ansatz."
  - **Tier: MINOR.** Closure agent: verify `\ref{sec:r1_njl}` resolves (it does,
    L1629) and do NOT introduce a `sec:r2_oneloop` ref unless that label exists
    (body label is `sec:oneloopfull`, L1538) — safest to phrase the one-loop clause
    without a cross-ref as above.
- Tally: ~18 already-covered (R52 F1/F2/F3/F7/F9/F11, EXT21) + falsified/opinion
  (Fig 1 D-round, parity reword, "prediction→class-test" already at L828/L950,
  Table I footnote, Bianchi/non-metricity L2454, extraction artifacts); 1 new
  verified MINOR.

### P1B — `arxiv/paper1b_mcmc_companion.tex` — **CLEAN (0 new verified)**
~20 already-covered (R52 MAJOR#1 w0wa relabeling fully applied L1467; NaMaster
pinning; Table II overlap-uncorrected header; Fig 3 MC-bias caption;
Ωa-prior/posterior readout L2463/L2568). 2 FALSIFIED pattern-063 extraction
artifacts (Gemini "σ→0" — source `\sigma` renders correctly L1104/1467; Gemini
"$n_s$=3.965" — source L1438 `$0.965\pm0.006$`, PDF layout artifact). ~8
opinion/polish (abstract length, typo, convention notes). Expected confirm-round
outcome — all substantive defects were already closed in R52+EXT21.

### P2 — `research/focused_paper_source_integration/02_full_draft.tex` — **CLEAN (0 new verified)**
Candidate (Table IV photo-z caption row, ChatGPT EXT22) DOWNGRADED on director
review: the lane's premise rested on the caption claiming to consolidate "all
systematic contributions … in one place," but L972 actually reads "Consolidated
systematic budget for the SPHEREx bispectrum detection of $\fnl$" — no
exhaustiveness claim (misquote → falsified premise). Photo-z is a subdominant
(~5%, σ 0.70→0.74) effect already explained in body §systematics; the caption is
already maximally long and a second reviewer (M4) complained it is *too* long.
Adding to it is polish at best → OPINION, not a closure edit. All other ~17
findings already-covered (R52 DO-NOW #4/#6/#7/#9/#17) or falsified (Table II
"illustrative" sentence already at L580; covariance-sign clause already at L578).

### P3 — `pipelines/p3_anomaly_engine/paper3_draft.tex` — **CLEAN (0 new verified)**
~17 already-covered (R52-B catalog-grade tiers; R52-N DESI calibration-suspect
L1091(3); R52-G fNL two-normalization L1037; eROSITA downstream-consequence
sentence already verbatim L857; convexity parenthetical L1037; Table V item (f)
"not independent cross-method confirmation" L719/L1108). 2 FALSIFIED pattern-063
(Tab:bf_robustness footnotes syntactically correct L1356–1388; §V.A "garbled set
notation" — source L1117 correct `\sigma(f_{\rm NL})\in\{...\}`). 3
opinion/out-of-scope/additive (split Table I, dataset-card README, float32 note).

### P4 — `pipelines/p2_chirality/chirality_catalog_paper.tex` — **1 NEW VERIFIED (POLISH)**

**NV-P4-1 — Same statistic quoted as +3.3σ and +3.29σ (POLISH/internal consistency).**
- The [0.5,0.6) confidence-bin signal (1.87M galaxies) is written **+3.3σ** at
  L701 (body) and L900 (App C opening), but **+3.29σ** at L912 (App C
  per-imaging-leg detail, "full-catalog $[0.5,0.6)$ confidence bin $+3.29\sigma$").
  Same bin, two roundings. VERIFIED, but trivial (3.3 is the 2-sig-fig rounding of
  3.29) — polish-tier, not substantial rework.
- **Proposed edit** (`chirality_catalog_paper.tex`):
  - L701: `$+3.3\sigmaunit$ signal` → `$+3.29\sigmaunit$ signal`
  - L900: `the $+3.3\sigmaunit$ in the $1.87$M-galaxy` → `the $+3.29\sigmaunit$ in the $1.87$M-galaxy`
  - **Tier: POLISH** (optional; safe single-token consistency fix).
- Tally: ~14 already-covered (R52 V1–V8); 2 falsified (Gemini "does oes not" typo
  has no source match; archival DOI already TRULY-BLOCKED); remainder opinion.

### P5 — `pipelines/p5_desi_chirality/paper/p5_desi_chirality.tex` — **CLEAN (0 new verified)**
~14 already-covered (R52 V1/C1/C3/C4/C5; EXT21 M2). FALSIFIED/STALE: ChatGPT
"Fig 6 maximal-voids panel misplaced" — reviewer miscounted figures (single-panel
`fig:healpix_skymap` §VI.E L1742 vs 2-panel `fig:voids_vs_chirality` §VIII.F
L2653, correctly placed); Gemini "RSD boundary-crossing differential omitted" —
explicitly present L2071–2079; Fig 8 label overlap already fixed v0.1.83. Rest
opinion/NIT (σ-subscript spacing flagged by Gemini itself as PDF artifact).

---

## Per-paper one-line summary

- **P1A:** 1 new VERIFIED [MINOR: §XII.B Discussion L2698–2701 states NJL/one-loop closure mechanisms not in the body — align to Planck/amplitude-suppression].
- **P1B:** clean.
- **P2:** clean (Table IV photo-z candidate downgraded — caption misquote, OPINION).
- **P3:** clean.
- **P4:** 1 new VERIFIED [POLISH: +3.3σ vs +3.29σ for the same [0.5,0.6) bin — fix L701/L900 to +3.29σ].
- **P5:** clean.

Net across the portfolio: **1 MINOR + 1 POLISH new-verified item, 0 MAJOR, 0 BLOCKER.**

---

## CONVERGENCE VERDICT

**POLISH-TIER CONVERGENCE REACHED — `/cascaded-r-rounds` exit bar met.**

Three review passes on the same R52-closed PDFs (INT R52 + EXT21 + EXT22) have
now produced **0 MAJOR / 0 BLOCKER** with a strictly decreasing residual: EXT22,
the confirm round, surfaces only **1 MINOR (P1A prose/closure-mechanism
alignment) + 1 POLISH (P4 rounding)** across all six papers — both single-edit,
zero-science-rework, low-risk. Every other EXT22 finding resolved to
already-covered, extraction-artifact (pattern-063), opinion, or stale-already-fixed
(pattern-062). This is the textbook signature of convergent silence: independent
external vendors re-confirming the existing closures rather than finding new
substance.

**The portfolio does NOT need another full close+review cycle.** Recommend:
apply NV-P1A-1 (MINOR) and optionally NV-P4-1 (POLISH) as a single
EXT22-closure commit bundle (with the mandated `reviewTimeline.ts` entry), then
proceed to D-round/P-round packaging per the readiness ladder. No EXT23
confirm round is warranted — it would re-confirm the same convergence at cost.
