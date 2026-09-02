---
title: "Paper A3M SSOT — Multi-channel consistency of the matter-bounce prediction at f_NL = -35/16"
type: ssot
paper: A3M
last_updated: 2026-09-02 — v3M.0.4. R1 CLOSED (round ROUND_2026-09-02-A3M-v3M.0.3-EXACTPDF-7e35caa0-R1): 8 pp, md5 b98ee16e11d106c96ac593480857112b, sha256 d86f484f5d4f83fb7b4a339cced6a9c4bf9482f5f5bc206a55bdbfe2270e277c, 0 undef refs, 0 overfull hboxes >10pt (largest 2.7pt). See "R1 closure (2026-09-02)" section below for verdicts, decisions, and the item-to-edit table. Prior: v3M.0.3, PBH compaction-function channel integrated: 7 pp, md5 9f7afea9e22a7816168fc7638fc8a753. v3M.0.2, 6 pp, md5 8f17a2dc877c0b58982e91a8dea0fa1b. Ledger #1 correction: fixed §II wording from "OPEN" to CLOSED per NEXT_SCIENCE_LEDGER.md row 1 (only the Bianchi-I shear cross-check remains open).
canonical_source: research/track_a3_multichannel/paper/main.tex
canonical_pdf: research/track_a3_multichannel/paper/main.pdf (8 pp / 0 undef refs / md5 b98ee16e11d106c96ac593480857112b)
version: v3M.0.4 (2026-09-02, R1 closure)
registry_id: A3M (project-context/draft_paper_registry.json)
review_profile: PRD-REGULAR
target_journal: Physical Review D (regular article)
headline_pct: not-yet-reviewed (agent gates: science 25 / evidence 25 / review-convergence 0 / packaging 20 = ~70; R1 closed, R2 verification pass authorized next)
submission_status: draft, R1-closed — R2 verification pass next (directive R2: 1 of 2 convergence-budget rounds consumed)

## R1 closure (2026-09-02)

**Round:** `ROUND_2026-09-02-A3M-v3M.0.3-EXACTPDF-7e35caa0-R1` (7 pp v3M.0.3,
sha256 `7e35caa0...`). **Verdicts (diagnostic only, per directive H/H-refined):**
Fable INT — MAJOR REVISIONS (7 MAJOR / 16 MINOR); Grok API `grok-4.3` —
REJECT (3 ESSENTIAL / 3 MAJOR / 2 minor); Gemini API `gemini-3.1-pro-preview`
— MAJOR REVISIONS (2 ESSENTIAL / 1 MAJOR / 2 MINOR); Perplexity — ABSENT
(not run). **Audit class counts:** GENUINELY-NEW-REAL 20 (7 MAJOR/ESSENTIAL +
13 MINOR); RE-FLAG-OF-DISCLOSED 5; FALSIFIED 8 (incl. 2 sub-claims + 3
self-falsified by the Fable leg); OPINION/GENRE 3. No BLOCKERs, no fabricated
math found — the theory core (§II, −35/16, Table I) survived two independent
recomputations.

**Orchestrator science/scope decisions (recorded verbatim):**
- **D1 (PTA).** State NANOGrav's OFFICIAL 14-bin free-spectrum/HD posterior
  γ = 3.2 (+0.6/−0.6, 5–95% interval, arXiv:2306.16213) as the primary
  comparison; the lab's 30-bin refit (γ = 2.567 ± 0.382; synthetic-injection
  validation recovers γ = 3.19) is the secondary analysis. Both sets of
  tensions vs γ=3 and vs 13/3 are quoted (official-posterior SMBHB tension
  ≈ 3.1σ, matching NANOGrav's own "99% credible boundary" language, computed
  in `research/track_a3_multichannel/pta_gamma_reproduce.py`). Every Bayes
  factor/σ that extrapolates the KDE into the unsampled tail (B(γ=5),
  "6.37σ") is dropped from the abstract in favor of stating 0 of 320,000
  samples lie at γ ≥ 5.
- **D2 (transmission).** The transmission statement becomes a
  handoff-scheme-conditional bound: "under a handoff at the NEC boundary with
  cubic sourcing frozen thereafter, 0 < T ≤ 1/2" (assumption A4 explicit);
  "universal" is deleted; the honest note that the bounce's own cubic term is
  not computed is retained.
- **D3 (PBH).** The compaction-function ratio
  A(−35/16)/A(−35/8) = 1.732 [1.610, 1.809] is kept as a result (not demoted
  to illustration), with its regime of validity added (anti-correlated J>1
  branch; 1.2|f_NL|σ_r ≈ 0.7–1.5 non-perturbative excursion range) and an
  explicit one-sentence disclosure of the 55-decade non-monotonicity of
  f_PBH(f_NL).

**Item → edit table:**

| Canonical item | Sev | Disposition | Edit in v3M.0.4 |
|---|---|---|---|
| A3M-R1-01 (PTA official posterior undisclosed) | MAJOR | GENUINELY-NEW-REAL | §IV rewritten: official 14-bin posterior primary (new Table II columns z_official), 30-bin refit secondary with injection-validation subsection; abstract updated |
| A3M-R1-02 (γ=5 tail-extrapolated BF/6.37σ) | MAJOR | GENUINELY-NEW-REAL | Dropped B(γ=5)/"6.37σ" claim from abstract; Table II now reports "n/a" for γ=5 Bayes factor with 0-samples-at-tail note in caption/text |
| A3M-R1-03(b) ("universal" transmission bound) | MAJOR | GENUINELY-NEW-REAL (03a re-flag-of-disclosed) | §III: added explicit assumption (A4), removed "universal", added end-time-independence reconciliation sentence |
| A3M-R1-04(b,c) (PBH non-monotonicity/robust scope) | MAJOR | GENUINELY-NEW-REAL (04a re-flag-of-disclosed) | §V B: added "Regime of validity" + "Non-monotonicity" paragraphs; abstract/§VII scope "robust" to shape-only |
| A3M-R1-05 (4 contradictory factor-of-two statements) | MAJOR | GENUINELY-NEW-REAL | §II C/D rewritten to one consistent statement ("adjudicates within the in-in method"); "CLOSED" removed; §VII joint statement matches |
| A3M-R1-06 (r=0.84 unsourced) | MAJOR | GENUINELY-NEW-REAL | §VI B: r=0.84 now explicitly sourced to the P2 Fisher forecast (item A3-4 open); r-projected significances dropped from Table IV and abstract, bare significance only |
| A3M-R1-07 (Ref. [7] wrong ID+journal) | MAJOR | GENUINELY-NEW-REAL | Bibliography fixed: arXiv:1712.08148, Phys. Rev. D 97, 066021 (2018) |
| A3M-R1-08 (internal issue-tracker tags in body) | MAJOR | GENUINELY-NEW-REAL | All `item A3-N`/"CLOSED"/"flagged in the prior version" tags stripped from body prose (kept in this SSOT); in-body GitHub URLs/commit hash and long SHA-256 consolidated into the Reproducibility statement with line-break-safe formatting |
| R1-m01 (Fig. 1 caption "(top)/(bottom)" vs 1 panel) | MINOR | GENUINELY-NEW-REAL | Caption rewritten to describe the actual single f_PBH-vs-A panel |
| R1-m02 (1.14σ Gaussian-approx on bounded marginal) | MINOR | GENUINELY-NEW-REAL | Labelled Gaussian-approximate; P(γ>3)=8.97% quoted from chain |
| R1-m03 (ESS convention unstated) | MINOR | GENUINELY-NEW-REAL | τ=(58.1,58.0) and ESS=N/max(τ) convention stated |
| R1-m06 (perturbativity range not split per candidate) | MINOR | GENUINELY-NEW-REAL | Per-candidate ranges (0.54–1.01 at −35/16, 1.09–2.02 at −35/8) now quoted |
| R1-m07 (γ_cr discrepancy fiducial unnamed) | MINOR | RE-FLAG-OF-DISCLOSED | One clause naming the −35/8 fiducial added |
| R1-11/A3M-R1-11 (A* normalization missing) | MINOR | GENUINELY-NEW-REAL | A* = 0.131446 printed in §V B and figure caption |
| R1-12/A3M-R1-12 (DESI prior non-comparability) | MINOR | GENUINELY-NEW-REAL | Explicit non-comparability clause + asymmetric errors named in §VI A |
| R1-13 (Li 2016 vs 2017 year) | MINOR | GENUINELY-NEW-REAL (mislabelled MAJOR by Gemini) | Abstract now says Li et al. (2017), matching bibliography |
| A3M-R1-01a/01b (Fable sub-claims) | — | FALSIFIED | Not adopted (causal bin attribution, 1.9σ figure) |
| R1-09 (future-dated header) | — | FALSIFIED | No change (training-cutoff artifact) |
| R1-m19/m20 (arithmetic/formatting artifacts) | — | FALSIFIED | No change |
| A3-1b/c/d, A3-2, A3-3 | — | out-of-round (open science) | Unchanged; remain on next-steps list, not required for R1 closure per directive R2 |

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
- R1 review board (Fable INT + Grok API + Gemini API; Perplexity absent) ran
  on v3M.0.3 and is CLOSED as of v3M.0.4 (see "R1 closure" section above).
  R2 verification pass on the new exact PDF is authorized next; no EXT sweep
  yet. Readiness stays at the agent-gate composition (~70%) until R2 confirms
  0 genuinely-new-real findings.

**Not edited by this commit (per lineage decision + task scope):** P2L
(`arxiv/paper2prime_fnl_letter/main.tex`), P2
(`research/focused_paper_source_integration/`), and the A3 brief
(`research/track_a3_multichannel/A3_MULTICHANNEL_BRIEF_2026-09-02.md`).
