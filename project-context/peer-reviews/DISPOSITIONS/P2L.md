# Canonical dispositions — P2L (P2′ Letter)

Paper: `arxiv/paper2prime_fnl_letter/main.tex` + `main.pdf`, v2L.0.1, 4 pp,
sha256 `e1501145bd314f85e54c928c579ec1e3ceb96bbdf078ba15ab02e2bb40ca4d12`.
Ledger opened 2026-09-02 at round `ROUND_2026-09-02-P2L-v2L.0.1-EXACTPDF-e1501145-R1`.
Full evidence: `INT_v3/ROUND_2026-09-02-P2L-v2L.0.1-EXACTPDF-e1501145-R1/P2L_v2L.0.1_R1_truth_audit.md`.

R1 verdicts (verbatim): Claude/Fable INT **MAJOR REVISIONS** (5M/13m) · Grok API **REJECT** ·
Gemini API **MAJOR REVISIONS** · Perplexity **ABSENT** (leg not run).
Class counts: **18 GENUINELY-NEW-REAL** (5 MAJOR / 12 MINOR / 1 NIT), 5 FALSIFIED,
2 OPINION/GENRE, 1 OUT-OF-SCOPE, 0 RE-FLAG-OF-DISCLOSED. Clean-wave count: **0** (not converged).
No P2 (parent) fingerprint matched any R1 item.

## Closed 2026-09-02 (v2L.0.2, this round) — formerly genuinely-new-real

### DP2L-01: δN uniform-density formula misprinted
- **class:** CLOSED (MAJOR) — v2L.0.2. `main.tex` L170 prints `f_{\rm NL}^\rho=(5\epsilon-7)\cdot 5/8`, which at
  ε=3/2 gives +5/16, not −55/16. Committed value (`fnl_matter_contraction_adjudication_2026_09_02.py`
  L537, JSON `uniform_density_slicing_fNL_general_eps`, brief L33) is `5(ε−7)/8 = (5ε−35)/8`.
- **fingerprint:** 5 epsilon 7, delta N, uniform density, −55/16, general epsilon formula

### DP2L-02: μ² orientation dependence is contained in the published shape function
- **class:** CLOSED (MAJOR) — v2L.0.2. `A_total − A_Li(Eq. 4.19, c_s=1) = 0`; the auditor's own fixed-angle
  expansion of the committed total polynomial returns `−35/16 + (15/16)μ²`. The abstract's
  "We report a new result" overstates. New content = the observation, per-vertex attribution, shear
  interpretation.
- **fingerprint:** orientation dependence, mu squared, 15/16, new result, Li 4.19, Cai Eq 37, novelty

### DP2L-03: forecast never states which amplitude each survey row tests; r=0.84 undefined
- **class:** CLOSED (MAJOR) — v2L.0.2. Table II's 2.6/3.7 are r-projected (r=0.84), 3.1/4.4 bare
  (`track_a3_multichannel/outputs/survey_reach_fnl.json`); r is defined only in the A3 brief and
  A3-4 flags it not yet re-derived at the −35/16 fiducial. DESI σ≈9.0 absent and uncited.
- **fingerprint:** r=0.84, shape overlap, SPHEREx separation, which amplitude, Table II, DESI sigma

### DP2L-04: reference metadata defects
- **class:** CLOSED (MAJOR) — v2L.0.2. [2] Li+2016 wrong authors/title/journal (real: Y.-B. Li, J. Quintin,
  D.-G. Wang, Y.-F. Cai, JCAP 03 (2017) 031, arXiv:1612.02036). [6] 1301.5699 is Chen, Firouzjahi,
  Namjoo, Sasaki, EPL 102 59001 — *Quantum Primordial Standard Clocks* is 1411.2349, JCAP 02 (2015) 006.
  [12] Choudhury given names wrong. [8] CaiEassonBrandenberger:2012 uncited. All verified live on arXiv.
- **fingerprint:** references, 1612.02036, 1301.5699, 1411.2349, bibliography metadata, uncited entry

### DP2L-05: load-bearing claims on mutable blob/main links, underived
- **class:** CLOSED (MAJOR) — v2L.0.2. `ζ_ρ=2ζ_c`, `T=[1−ρ]/2`, `0<T≤1/2`, 0.165–0.409 carry no derivation and no
  frozen artifact. Refs [13]–[15] are `blob/main` URLs.
- **fingerprint:** blob/main, mutable link, zeta_rho = 2 zeta_c, transmission bound, DOI pin, self-contained

### DP2L-06…DP2L-18 (MINOR/NIT) — CLOSED v2L.0.2, DP2L-18 retained as intentional house style
abstract 2.6–3.7 composite (06) · DESI row σ/citation/0.24σ (07) · "isoceles" (08) ·
"§ 2311.13082" (09) · version-history prose (10) · μ²-source sentence vs Table I (11) ·
"amplitude-normalization step" over-localised (12) · δK sign convention (13) ·
"Li et al. inherit" wording (14) · Table I caption defines f^sq(μ) (15) ·
title "the exact local" (16) · 1.64× vs 2.48× (17) · house-style stamps + ref project tags (18).

## Standing non-real dispositions (re-flag these on sight)

- **DP2L-F1 — FALSIFIED:** "abstract asserts a post-bounce observable" (Grok E1/E4). The abstract states
  transmission is "bounded, not resolved", `0<T≤1/2`, and that the bounce cubic term is not computed.
- **DP2L-F2 — FALSIFIED:** "placeholder / future-dated arXiv IDs" (Grok N2). All nine cited eprints
  fetched live and real. SKILL Rule 3 future-date-confab class.
- **DP2L-F3 — FALSIFIED:** "0.16σ implies σ_fNL≈13.7" (Grok A1). 0.16σ is the tension of −2.1875 with
  DESI DR1's central −3.6 at σ≈9.0, not a template separation.
- **DP2L-F4 — FALSIFIED:** "1.64× contradicts 0.409/0.165=2.48" (Gemini M4). 1.64 = 0.409/0.250 on the
  same LQC background (A2 brief L125), exactly as the parenthetical says.
- **DP2L-F5 — FALSIFIED (severity):** "no per-vertex integrands, unverifiable" (Grok M1). Table I plus
  the committed script supply every vertex; residual is the DOI pin → DP2L-05.
- **DP2L-O1 — OUT-OF-SCOPE:** "compute the bounce cubic vertex or delete §V" (Grok E1). A new-research
  demand against a scope the Letter states honestly.
- **DP2L-G1 — OPINION/GENRE:** preprint version tag and dated author block (Grok E3/N1). Directive-G
  internal stamps; strip in the journal-submission build only.

## Venue disposition (R1, auditor recommendation)

Not a PRD **Letter**. Recommend a regular PRD article (fallback: a Comment on Cai *et al.* 2009 if
scoped to the factor of two alone). Reasons: the genuinely-new content is a
correction/confirmation once DP2L-02 is stated honestly; Li+2016 already prints −35/16 and
Quintin+2015 §III.3 already quotes −35/16 (verified live, ar5iv 1508.04141); the most interesting
physics (§IV bounce transmission) is explicitly uncomputed; and closing DP2L-02/03/05 needs 2–4 pages
a Letter does not have. Full reasoning in the R1 audit §4.


## Closure note — 2026-09-02

All 18 GENUINELY-NEW-REAL items (DP2L-01…18) closed in `main.tex`/`references.bib` for v2L.0.2. See `project-context/SSOT/paper-2l/status.md` ("R1 closure — 2026-09-02 (evening)") for the item-by-item edit table, and `project-context/PAPER_LINEAGE_2026-08-05.md` ("Decision record — 2026-09-02 (evening)") for the scope decision folding this Letter's content into the A3 multi-channel paper's theory section. Convergence budget spent: one round run (directive R2) — no further review rounds planned for this Letter.
