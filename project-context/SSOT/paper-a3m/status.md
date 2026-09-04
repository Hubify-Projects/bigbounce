---
title: "Paper A3M SSOT — Multi-channel consistency of the matter-bounce prediction at f_NL = -35/16"
type: ssot
paper: A3M
last_updated: 2026-09-04 — v3M.0.9. R3 truth-audit closure C1–C10 (transmitted-amplitude LSS reach, δN_c derivation appendix, induced-GW IR-slope correction, numeric/definitional fixes); see "v3M.0.9" section below. Readiness held at 75. Prior: v3M.0.8 (2026-09-04), three closed science-gate results integrated (method-independent f_NL cross-check, bounce cubic term, lab-own-spectrum PBH null); see "v3M.0.8" section below. Prior: v3M.0.7 (2026-09-02), R2 CLOSED (round ROUND_2026-09-02-A3M-v3M.0.4-EXACTPDF-d86f484f-R2VERIFY): 9 pp, md5 67e1510e2b300ec683ed2e288ef1aefe, sha256 e7ae9d324de41822728e01d2161aba71dd15fd255dd4d2b4247b3b5122e6de24, 0 undef refs, 0 overfull hboxes >10pt (largest 2.7pt). Per directive R2 the convergence budget (2 rounds) is now consumed — REVIEW ROUNDS STOP on this paper; residue is genre/length/venue. See "R2 closure (2026-09-02)" section below for verdicts, the science decision, and the item-to-edit table. Prior: v3M.0.4, R1 CLOSED: 8 pp, md5 b98ee16e11d106c96ac593480857112b, sha256 d86f484f5d4f83fb7b4a339cced6a9c4bf9482f5f5bc206a55bdbfe2270e277c. v3M.0.3, PBH compaction-function channel integrated: 7 pp, md5 9f7afea9e22a7816168fc7638fc8a753. v3M.0.2, 6 pp, md5 8f17a2dc877c0b58982e91a8dea0fa1b. Ledger #1 correction: fixed §II wording from "OPEN" to CLOSED per NEXT_SCIENCE_LEDGER.md row 1 (only the Bianchi-I shear cross-check remains open).
canonical_source: research/track_a3_multichannel/paper/main.tex
canonical_pdf: research/track_a3_multichannel/paper/main.pdf (12 pp / 0 undef refs / md5 925198c7ddc3485b9a6285a38995fe94)
version: v3M.0.9 (2026-09-04, R3 closure C1–C10 — see "v3M.0.9" section below)
registry_id: A3M (project-context/draft_paper_registry.json)
review_profile: PRD-REGULAR
target_journal: Physical Review D (regular article)
headline_pct: not-yet-reviewed (agent gates: science 25 / evidence 25 / review-convergence 25 (R1+R2 closed, rounds stop per directive R2) / packaging 20 = ~95; awaiting Houston's final personal review for 100 per directive P)
submission_status: draft, R2-closed — CONVERGENCE STATEMENT: rounds stop after v3M.0.5 per directive R2 (2/2 consumed); residue genre/venue

## R2 closure (2026-09-02) — FINAL, rounds stop

**Round:** `ROUND_2026-09-02-A3M-v3M.0.4-EXACTPDF-d86f484f-R2VERIFY` (8 pp
v3M.0.4, sha256 `d86f484f5d4f83fb7b4a339cced6a9c4bf9482f5f5bc206a55bdbfe2270e277c`,
verified). **Verdicts (diagnostic only, per directive H/H-refined):**
Claude Fable INT — MINOR REVISIONS (0 MAJOR / 9 MINOR); Grok API `grok-4.3`
— REJECT (3 ESSENTIAL / 3 MAJOR / 2 MINOR / 1 NIT); Gemini API
`gemini-3.1-pro-preview` — MAJOR REVISIONS (4 ESSENTIAL / 4 MAJOR / 3
MINOR-NIT); Perplexity — ABSENT (not run). 0 BLOCKERs, all legs. **Audit
class counts:** 29 raw findings → 16 GENUINELY-NEW-REAL (1 MAJOR + 10 new
MINOR + 5 carried R1 minors: m04, m09, m11, m12, m15), 6
RE-FLAG-OF-DISCLOSED, 3 FALSIFIED, 6 OPINION/GENRE. R1 closure verification
on the exact PDF: 17/20 items CLOSED as specified, 1 PARTIAL (DA3M-02,
precision residual → DA3M-R2-04), 5 unaddressed (m04/m09/m11/m12/m15 —
omissions, not mis-closures); no closure introduced a new factual error; no
number failed recomputation.

**Orchestrator science decision for DA3M-R2-01 (recorded verbatim):** "Run a
real injection–recovery test at γ = 13/3 (and γ = 3) through the SAME 30-bin
free-spectrum pipeline used for the refit... with the same likelihood/bins/
priors as the refit, N ≥ 1 realization each (more if minutes allow), record
recovered γ ± σ and the pull, commit the script + JSON + a reproducibility
manifest, and restate §IV C truthfully with the real numbers." Executed as
option (b) — the stronger close: `research/track_a3_multichannel/pta_injection_30bin_2026_09_02.py`
reuses `model_log10rho`/`log_prior` and the 30-bin/T_obs=16.03yr/prior
geometry verbatim from `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py`;
the real NANOGrav KDE density grids (Zenodo 8060824) are not present on this
machine (they require the RunPod workspace), so a synthetic per-bin Gaussian
density (σ=0.22 dex) centered on a noisy injected observation is substituted
— disclosed explicitly in the paper and the manifest. Recovery is by exact
dense 2D grid (1200×900) posterior marginalization of the identical
log_prior+log_likelihood rather than emcee ensemble sampling: a preliminary
emcee run showed near-zero acceptance on this strongly-degenerate 2D ridge (a
known ensemble-sampler failure mode, not evidence of bias); the dense grid is
an exact, faster computation of the same posterior for 2 parameters. Results
(5 realizations each, `pta_injection_30bin_2026_09_02.json`): γ_true=13/3
(4.3333) → mean recovered 4.328, mean pull **−0.026σ**; γ_true=3.0 (control)
→ mean recovered 3.015, mean pull **+0.068σ**. Both consistent with unbiased
recovery at well under 0.1σ. §IV C rewritten to state these real numbers and
explicitly retract the prior claim that a different (6-bin, Gaussian-χ²,
γ=3.2-injected) validation was "the identical pipeline" injected at 13/3.

**Item → edit table:**

| Canonical item | Sev | Edit in v3M.0.5 |
|---|---|---|
| DA3M-R2-01 (§IV C misdescribes injection artifact) | MAJOR | §IV C (`\label{sec:pta_validity}`) rewritten with the real 30-bin injection-recovery result (γ=13/3: −0.026σ mean pull; γ=3 control: +0.068σ), script+JSON+manifest committed |
| DA3M-R2-02 (Eq. 8 σ² term dropped) | MINOR | Both occurrences (ceiling definition + non-monotonicity discussion) now state the leading-term-only numbers explicitly and give the full σ=0.1 values (0.1215/0.2036, ratio 1.68) |
| DA3M-R2-03 (Ω_DM=0.674 is Planck h) | MINOR | Footnote added: value as printed in Choudhury et al. Eq. (66), coincides with Planck h, cancels in the ratio / absorbed by calibration — no result changes |
| DA3M-R2-04 (13/3 Savage–Dickey precision) | MINOR | Table II 4.5e−4 → 5e−4; text 7.1e3/+3.85 → ≈7e3/+3.9±0.2, one-s.f. rule now consistent |
| DA3M-R2-05 (duplicated §VII C clause) | MINOR | Duplicate "settling the factor of two" clause removed |
| DA3M-R2-06 (undefined D1–D5 labels) | MINOR | "(deviation D1 above)" and "(D1–D5)" replaced with plain-prose descriptions |
| DA3M-R2-07 (refit 3.1–4.6σ mislabel) | MINOR | Split into explicit 3.1σ (official posterior) / 4.63σ (refit) with conditioning stated; L370 quadrature σ=0.53 now labelled |
| DA3M-R2-08 (bare/projected inversion) | MINOR | Reworded: bare significance does not depend on the (not-yet-derived) shape-overlap projection |
| DA3M-R2-09 (abstract DESI prior omission) | MINOR | Abstract now states both merger (−3.6, 0.16σ) and universality (+3.5, 0.77σ) priors with the not-directly-comparable caveat |
| DA3M-R2-10 (r=0.84 numeral unsourced) | MINOR | Numeral dropped (r<1, qualitative statement kept); no result depends on it |
| DA3M-R2-11 (no frozen-release DOI) | MINOR (packaging) | Reproducibility statement notes commit-pin pending Zenodo minting (Houston-only click-list action); P2 theory lineage cited at its archived Zenodo record 10.5281/zenodo.21461881 |
| DA3M-m04 (Table II "archived record" self-reproduction wording) | MINOR (carried) | Reworded: "self-reproduction run of the same script against the same chain," not an independent check |
| DA3M-m09 (Cai ×2 algebraic line unnamed) | MINOR (carried) | Localized to Cai et al.'s Eqs. (38)–(40), f_NL=(20/3)A/Σk³ |
| DA3M-m11 (ζ(∂ζ)² row leading-order qualifier) | MINOR (carried) | Table I footnote: "Zero at leading order O(k²S²)" |
| DA3M-m12 (r complex, text says \|r\|≫1) | MINOR (carried) | r=−9iA²I_∞/k³ stated explicitly (A2_TRANSMISSION_BRIEF_2026-09-02.md:94), complex in general |
| DA3M-m15 ("nested factor" undefined) | MINOR (carried) | Clarified: nested Savage–Dickey factors (point restrictions within the refit's free-γ model) vs. their model ratio |

**CONVERGENCE STATEMENT:** rounds stop after v3M.0.5 per directive R2 (2/2
convergence-budget rounds consumed); the remaining ledger is genre/length/
venue (abstract trim to PRD length, bibliography DOIs, AI-disclosure
placement, `.tex` header hygiene, optional Fig. 1 inset, Zenodo minting) and
belongs to the P-round, not a further review round.

**arXiv tarball (v3M.0.5):** `project-context/SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.5.tar.gz`,
sha256 `cd2ce1ef7c38746a9e8f59db371378bcc74b624a54406ca6f0c74611742522ab`. Contains
`main.tex` + `pbh_compaction_fnl.png` (inline `\bibitem` bibliography, no
separate .bbl). Smoke-tested: extracted standalone and recompiled 4-pass,
0 undefined refs, 9 pp, 544139 bytes — matches the served PDF.

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

## Final review 2026-09-02 (orchestrator)
REVISE then DEFER submission; readiness cap 70 (Convex). See `SSOT/FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md`.

## REVISE executed 2026-09-02 → v3M.0.6

Both agent-doable items from `FINAL_REVIEW_RECOMMENDATIONS_2026-09-02.md`
§A3M were executed:

1. **Abstract cut to PRD length.** 450 words → 307 words. No quantitative
   claim or evidential-strength qualifier was dropped — every number
   (γ=2.567±0.382, 1.14σ/0.55σ, γ=13/3 at 3.1σ, γ=5 zero of 320,000 samples,
   A(-35/16)/A(-35/8)=1.732[1.610,1.809], the PBH non-monotonicity note, the
   DESI DR1 dual-prior numbers, SPHEREx 3.13σ at σ_fNL=0.7) and every
   qualifier ("not quotable", "not directly comparable", "pending... not yet
   re-derived", "no channel is in tension") survives verbatim or
   near-verbatim; explanatory framing (why the bounce is a testable
   alternative, grading conventions) was already present in the Introduction
   and was left there rather than duplicated in the abstract.
2. **30-bin injection on real NANOGrav KDE grids — NOT RESTORED.**
   `pipelines/p3_pta_mcmc/free_spectrum_real_2026-05-01/emcee_freespec.py`
   loads the real grids from `/workspace/p3_realfreespec/kde/30f_fs{hd}_ceffyl/
   {freqs,log10rhogrid,density}.npy` (Zenodo 10.5281/zenodo.8060824), an
   ephemeral RunPod `/workspace` path — those exact files were never mirrored
   to a durable store. Searched: (a) local disk —
   `~/Desktop/CODE_YOU/bigbounce_datasets` and a repo-wide find for
   `ceffyl`/`30f_fs*` — zero hits; (b) HuggingFace `bamfai/*` datasets (7
   repos: bigbounce-mcmc, galaxy-chirality-catalog, bigbounce-anomaly-catalog,
   astra-desi-edr-mirror, p1b-mcmc-diagnostics, p1b-namaster-artifacts,
   p1b-alp-chains) — no file matching kde/ceffyl/freespec/pta/30f_fs in any
   repo's file list; (c) Backblaze B2 bucket `bigbounce`
   (`s3.us-west-004.backblazeb2.com`, 74,388 objects scanned) — zero keys
   matching kde/ceffyl/freespec/30f_fs; the only `mcmc/` prefix hits are the
   unrelated `w0wa_quintom` cosmological-parameter chains. **Conclusion: the
   real KDE grids are not restorable from any of the three checked stores**
   (they predate the 2026-06-26 ALWAYS-backup directive). §IV.C of the paper
   is left as-is (synthetic-per-bin-density injection, disclosed as such in
   the script and paper text); this is recorded as the missing artifact for
   ledger row A3-3. **Next action if this is to be closed:** re-download the
   Zenodo 8060824 KDE pack directly (no RunPod dependency needed — it is a
   public Zenodo record) to `pipelines/p3_pta_mcmc/kde_real/`, back it up to
   HF+B2 immediately per the ALWAYS-backup directive, then re-run
   `pta_injection_30bin_2026_09_02.py` against the real grids.

**Hygiene (this commit):** `\paperVersion` v3M.0.6, `\date`/`\paperTimestamp`
September 2, 2026 (unchanged, already current); 4-pass pdflatex, 0 undefined
refs, 0 overfull hboxes >10pt; pdftoppm -r 60 all 9 pages visually spot-checked
(pp. 1, 5) — clean two-column layout, no overflow; PDF md5
`3888085edc5c493fcd2a45c8c386576d` (sha256
`db87efa9fcc74f31e3dc8ae5aa3a6296f63536a5c2adaf59f7d28a133b3b2e20`), 9 pages,
mirrored byte-identical to `site/public/papers/a3_multichannel_arxiv_v3M.0.6.pdf`
and `public/papers/a3_multichannel_arxiv_v3M.0.6.pdf`; arXiv tarball
`SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.6.tar.gz` sha256
`c762345fbddd6c38844490c0d975536fc6d50cf4c53a258c5798398becc838b4`, standalone
extract+recompile smoke test PASS (0 undefined refs, 9 pages). Readiness
composition unchanged at this step (still capped by the open DEFER-submission
science gate per the 2026-09-02 final review; abstract/injection were
editorial-hygiene REVISE items, not science-gate closures).

## v3M.0.7 (2026-09-02) — REVISE item CLOSED: real-KDE injection validation

**Closure of the "30-bin injection on real NANOGrav KDE grids — NOT
RESTORED" item above.** The grids were never on an ephemeral RunPod path
alone — they are a public Zenodo data product. Queried
`https://zenodo.org/api/records/8060824`: one file,
`NANOGrav15yr_KDE-FreeSpectra_v1.0.0.zip` (6,571,028 bytes, sha256
`b461125ff9d384761ec4647756587c42067723c6980ef3c633b178012a4d91d8`),
containing five KDE variants; `30f_fs{hd}_ceffyl/` matches
`emcee_freespec.py`'s `ROOT` exactly (`freqs.npy`, `log10rhogrid.npy`,
`density.npy` shape `(1,30,10000)`, `bandwidths.npy`). Downloaded and
extracted to
`~/Desktop/CODE_YOU/bigbounce_datasets/nanograv15yr_kde_2026-09-02/`
(outside the repo); per-file sha256 recorded in
`outputs/pta_injection_30bin_realkde_2026_09_02.manifest.json`. Packed
cache uploaded to HuggingFace `bamfai/bigbounce-aug-011-clean-rerun` under
`external/nanograv15yr_kde/` (zip + sha256 manifest) so this artifact is
mirrored this time, closing the ALWAYS-backup gap that caused the original
loss:
<https://huggingface.co/datasets/bamfai/bigbounce-aug-011-clean-rerun/blob/main/external/nanograv15yr_kde/NANOGrav15yr_KDE-FreeSpectra_v1.0.0.zip>.

`research/track_a3_multichannel/pta_injection_30bin_realkde_2026_09_02.py`
reuses `model_log10rho`/`log_prior` verbatim from `emcee_freespec.py` and
builds the injection by re-centering each bin's REAL observed KDE curve
(shape/width/skew preserved exactly) along the log10_rho axis onto the
model prediction for a chosen injected `(gamma_true, log10_A_true)` — since
a real dataset's true signal is unknown, this re-centering is the only way
to get a ground-truth injection test out of the real KDE data without
simulating an entirely new PTA dataset from scratch. 5 realizations per
gamma_true (1 full 30-bin + 4 bootstrap bin-resamples), dense 2D grid
posterior marginalization (identical to the prior script's method).

**Results** (`outputs/pta_injection_30bin_realkde_2026_09_02.json`):
γ_true=13/3 (4.3333) → mean recovered 4.336, mean pull **+0.016σ**;
γ_true=3.0 (control) → mean recovered 3.005, mean pull **+0.033σ**. Both
well under 0.1σ, consistent with unbiased recovery, and tighter than the
prior synthetic-Gaussian-density result (−0.026σ / +0.068σ, retained as a
secondary cross-check line per Houston's science decision). §IV C
(`\label{sec:pta_validity}`) restated with the real-KDE numbers as the
primary line; the synthetic-density result is now the secondary
cross-check sentence.

**Hygiene (this commit):** `\paperVersion` v3M.0.7, `\date`/`\paperTimestamp`
September 2, 2026; 4-pass pdflatex, 0 undefined refs, 0 overfull hboxes
>10pt (one pre-existing 2.7pt hbox unrelated to this edit); pdftoppm all 9
pages rendered and pp. 4–5 (the edited section + neighboring page) visually
spot-checked — clean two-column layout, no overflow, real-Zenodo citation
and pull numbers render correctly. PDF md5 `f27a62098e5a673fa16b24d68e70da96`
(sha256 `b0f2ab22558b3c80a777362f8891c13e0af6ff6a7fb0190f90d47679f820e31f`), 9
pages, 543,764 bytes, mirrored byte-identical to
`site/public/papers/a3_multichannel_arxiv_v3M.0.7.pdf` and
`public/papers/a3_multichannel_arxiv_v3M.0.7.pdf`. Convex `paperVersions:bump`
+ `activityFeed:add` written for `paper-a3m`. Readiness raised 70 → 75
(science item genuinely closed with real data; still short of Houston's
final personal review for 100 per directive P).

arXiv tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.7.tar.gz` sha256
`f4ecb9aec805527688961130ac41b35aaccbed02d62fea9cf25c5c9993ec2681`, rebuilt
from scratch in /tmp (main.tex + pbh_compaction_fnl.png, inline
`thebibliography` — no .bbl staleness risk), standalone extract+recompile
smoke test PASS (0 undefined refs, 9 pages).

## v3M.0.8 (2026-09-04) — three closed science-gate results integrated

**Sources (all committed, pre-existing to this bundle):**
`research/theory_audit/fnl_bianchi_separate_universe_2026_09_03.md`,
`research/theory_audit/fnl_monopole_adjudication_2026_09_03.md`,
`research/cubic_bounce_transmission/A2_TRANSMISSION_BRIEF_2026-09-02.md` §8
(+ `lane_a_vertex_table/`, `lane_b_numerical/`, `lane_c_comparison/`),
`research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.md`.

**(1) Method-independent squeezed-limit confirmation — Sec. II rewritten
("Cross-check by a different route: closed").** The classical $\mathcal
O(k^0)$ super-Hubble solution, organized by a shift decomposition
([L] local / [K] shear-curvature, cancels / [X] shift, carries the
quadrupole and $+5/4$ monopole / [S] sourced, suppressed), reproduces the
in-in $-35/16$ result exactly and independently of the in-in commutator
expansion. $\delta N_c=(1-\epsilon/3)\zeta$ (derived from the Friedmann
equation at fixed $\phi$) resolves the gap to every separate-universe
$\delta N$ value as an identity, not an open discrepancy. A companion
Bianchi-I check confirmed the shear alone gives identically zero monopole,
ruling that route out on its own and motivating the shift-decomposition
resolution. Eq. label `eq:deltaNc` added.

**(2) Bounce's own cubic term computed — new Sec. III.A.** Scheme S1
(geometric/dressed-metric): $\Delta f_{\rm NL}^{\rm bounce}=-(5/24)\rho_B$,
confirmed to $3\times10^{-4}$ by an independent finite-$k$ numerical in-in
evaluation. Combined with the pre-existing linear transmission bound:
$f_{\rm NL}^{\rm after}\in[-0.65,-0.50]$ across three backgrounds
(Quintin-type $-0.501$, LQC $-0.651$, poly $-0.555$), valid for
$k\eta_B\lesssim10^{-2}$ within scheme S1; scheme S2 does not regulate
(reported as a non-result). Literature comparison: no contradiction with
Quintin et al. 2015 (different term, same sign); not comparable as computed
with Agullo, Bolliet & Sreenath 2017 (scheme-limited, quantum-geometric
dressing not contained).

**(3) Lab's own predicted spectrum in the PBH channel — new Sec. IV.C.**
The lognormal stand-in of Sec. IV.B is supplemented (not replaced) with the
lab's own CMB-anchored $\Delta_\zeta^2(k)$ fed into the same compaction
machinery unmodified: a clean null, $f_{\rm PBH}=0$ exactly, $7.0$ orders of
magnitude short of the required amplitude at every mass scale
($10^{15}\,$g–$10^4\,M_\odot$). Required-amplitude ratio
$A(-35/16)/A(-35/8)$ widens from $1.732\pm0.050$ to $1.7$–$1.9$ for this
spectrum shape. FIRAS check: lab's own spectrum $\mu=1.65\times10^{-8}$
(safely allowed); required early-SMBH-seed amplitude FIRAS-excluded by
$\sim10^3$ if broadband, excluded even narrow for seeds $\ge10^4\,M_\odot$.

**What was deliberately NOT changed.** The Sec. VI (Channel III, LSS)
survey-reach table (`survey_reach_fnl.py` / `outputs/survey_reach_fnl.json`)
was NOT recomputed at $f_{\rm NL}^{\rm after}$: it never applied a
transmission factor (uses the pre-bounce $-35/16$ directly, as it did in
every prior version), and the new scheme-S1 transmission result is validated
only for $k\eta_B\lesssim10^{-2}$ — the PBH-scale regime — not for the
CMB/LSS pivot scale ($k\sim0.05\,{\rm Mpc}^{-1}$) Channel III uses, which
sits far outside that band. Applying $T_{\fnl}$ there without establishing
validity would be unsupported extrapolation, not a hygiene fix; this gap is
now explicit in the paper (Discussion, "Next steps" item (ii)) rather than
silent.

**Abstract.** Rewritten to state all three closures; 306 words (cap 307 per
this SSOT's prior v3M.0.6 trim).

**Hygiene (this commit).** `\paperVersion` v3M.0.8, `\date`/`\paperTimestamp`
September 4, 2026; 4-pass pdflatex, 0 undefined refs (one benign
`OMS/cmtt/m/n` font-shape warning, pre-existing pattern, not an undef ref);
0 overfull hboxes >10pt (one pre-existing 2.7pt hbox, unrelated to this
edit, carried from v3M.0.7); pdftoppm all 10 pages rendered at 55dpi and
visually spot-checked (pp. 1, 3, 4, 7, 8, 9 — abstract, new §II, new §III.A,
new §IV.C, Discussion) — clean two-column layout, no overflow, no path
overflow. Page count grew 9→10pp from the new content. PDF md5
`0c61d2ab760a14e0ff27ca560585bcbf` (sha256
`8cf429e002d44c97308ccc994c9378a93b066e094de865d48f850d5e72291b9a`), 10
pages, 564,544 bytes, mirrored byte-identical to
`site/public/papers/a3_multichannel_arxiv_v3M.0.8.pdf`,
`site/out/papers/a3_multichannel_arxiv_v3M.0.8.pdf`, and
`public/papers/a3_multichannel_arxiv_v3M.0.8.pdf` (three-way md5 check:
compile == served == Convex, all `0c61d2ab760a14e0ff27ca560585bcbf`).
Convex `paperVersions:bump` (paperSlug `paper-a3m`) + `activityFeed:add`
written; `sitePdfPath` confirmed updated on readback.
`site/src/data/papers.ts`, `site/src/data/live-status.ts`,
`site/src/data/publish.ts`, `site/src/data/reviewTimeline.ts` updated in the
same bundle. Readiness held at **75** (unchanged — this bundle closes
science items but the orchestrator sets readiness after a verification
board, per this SSOT's standing convention).

arXiv tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.8.tar.gz`
sha256 `ad3680401e0c016965d5876d3148282d820369c3d075c3f518ac09082b09743e`,
rebuilt from scratch in `/tmp` (main.tex + pbh_compaction_fnl.png, inline
`thebibliography`, same convention as v3M.0.7), standalone extract+recompile
smoke test PASS (0 undefined refs, 10 pages).

**Not sourced from a committed file (disclosed).** None — every number
above traces to the four source files listed at the top of this section.

## R3 closure decision C1 (orchestrator, Fable 5.1, 2026-09-04)

**Decision C1 = (a) PROPAGATE.** Verbatim: "The scheme-S1 super-Hubble transfer (validity kη_B ≲ 1e−2, an upper bound on k) is satisfied most easily at the LSS/CMB pivot, so the transmitted amplitude f_NL^after = T·f_NL^pre + Δf_NL^bounce is the paper's observable prediction for every channel. Table IV carries f_NL^after rows for −35/16 and −35/8 on all three backgrounds with bare significances at σ = 0.7/0.5/1.0; the pre-bounce row stays as a clearly-labelled secondary ('assuming T_fNL = 1'). The abstract's 'this channel alone discriminates the two amplitudes, with SPHEREx reaching 3.13σ' is replaced by the transmitted statement (SPHEREx bare 0.7–0.9σ for −35/16, 1.2–1.7σ for −35/8 — no discrimination at current reach). The §VII A 'far outside that validated window' sentence is deleted as false. No exemption (b) is claimed: no physical IR cutoff on S1 exists in the lab's computation." Basis: A3M_v3M.0.8_R3_TRUTH_AUDIT_2026-09-04.md DA3M-R3-01 (Fable M1 ≡ Gemini E4); VISION.md R6 (claims at evidential strength). Consequence: the Track-A headline becomes a transmission-corrected prediction plus a multi-channel consistency map; the −35/16 vs −35/8 factor-two is not separable by SPHEREx at the transmitted amplitude. Closure C1–C10 → v3M.0.9.

## v3M.0.9 (2026-09-04) — R3 closure C1–C10

C1(a) PROPAGATE executed exactly as recorded in the section above. C2–C10
executed per `project-context/peer-reviews/INT_v3/A3M_v3M.0.8_R3_TRUTH_AUDIT_2026-09-04.md`
§5. Summary of what changed: §III states the true `kη_B` direction (upper
bound on k, satisfied most easily at large scales) and the false "far
outside that validated window" sentence is deleted; Table IV gains
`f_NL^after` rows (values re-derived by `survey_reach_fnl.py`, cross-checked
against the auditor's precomputed values exactly: 0.7–0.9σ / 1.2–1.7σ at
SPHEREx bispectrum-only); the bounce-energy condition is restated correctly
(`T_B ≳ 1e8–1e10 GeV` at the smallest PBH mass, with the 7-decade-shortfall
argument for why the null verdict is unaffected); a new Appendix A
transcribes the δN_c derivation, [L]/[K]/[X]/[S] table, general-ε formulas,
and Bianchi-I argument from `research/theory_audit/fnl_monopole_adjudication_2026_09_03.md`
§§1–4 (no new science); the induced-GW IR-slope claim is corrected (causal
floor is `f^3`/γ=2, Cai, Pi & Sasaki PRD 102, 083528 (2020), arXiv:1909.13728,
added to the bibliography; γ=3 here follows from the bounce's specific
source spectrum, Papanikolaou Eq. 30+8); three numeric corrections (19–39%,
`n_s−1=12w/(1+3w)`, `0≤T_fNL<1/2`); eight definitional/labelling fixes;
directive-Q1 revision-history sweep (verified: `grep -nE 'research/|earlier
draft|supersed|had to be redone|prior version' main.tex` returns hits only
in reproducibility-statement/appendix-attribution context); Cai bookkeeping
equation numbers added (Li et al. Eq. 4.19 shape function, Eq. 5.1
amplitude); abstract restores the PBH perturbativity/non-monotonicity
caveats dropped in v3M.0.8, trimmed to 304 words (≤307-word PRD cap).

**Script re-runs (committed).** `research/track_a3_multichannel/survey_reach_fnl.py`
extended with `f_NL^after` rows (`outputs/survey_reach_fnl.json` re-emitted);
`research/track_a3_multichannel/inlab_delta2_zeta_2026-09-03.py` fixed and
re-run (`outputs/inlab_delta2_zeta_2026-09-03.json` re-emitted, `w` moves
−0.00293→−0.00290 as predicted, all tabulated `Δ²_ζ` values unchanged at
quoted precision); `research/cubic_bounce_transmission/lane_b_numerical/LANE_B_NUMERICAL_2026-09-03.md`
corrected 28–39%→19–39% to match.

**Hygiene (directive G).** `\paperVersion` v3M.0.8→v3M.0.9, `\date`/
`\paperTimestamp` → September 4, 2026 (today). 4-pass `pdflatex`, 0 undefined
references, 0 overfull `\hbox` > 10pt (all four transient overfulls from the
new Table IV / Appendix A tables fixed with `\scriptsize` + narrower
`p{}`-columns and `\allowbreak` on one long path). Pages grew 10→12. Page 1
(abstract), page 2 (Cai bookkeeping), page 9 (Table IV / Discussion), and
page 10 (Appendix A) visually spot-checked at ~55 dpi — clean two-column
layout, no overflow, no path overflow. PDF md5
`925198c7ddc3485b9a6285a38995fe94` (sha256
`6c543e5e9885c6db58e07576482ed6f283b0307ad1499c6309a4651d3c26fb1a`), 12
pages, 605,681 bytes, mirrored byte-identical to
`site/public/papers/a3_multichannel_arxiv_v3M.0.9.pdf` and
`public/papers/a3_multichannel_arxiv_v3M.0.9.pdf` (three-way md5 check:
fresh compile == served == Convex, all `925198c7ddc3485b9a6285a38995fe94`).
Convex `paperVersions:bump` (paperSlug `paper-a3m`) written (mutation id
`k5784scqrpaftj6jgra8b22rjx8ds5v2`). `site/src/data/papers.ts`,
`site/src/data/live-status.ts`, `site/src/data/publish.ts`,
`site/src/data/reviewTimeline.ts` updated in the same bundle. Readiness held
at **75** (unchanged — this bundle is a science-decision closure; the
R2-budget allows one more verification round before the next readiness
decision).

arXiv tarball `SSOT/arxiv_tarballs/a3_multichannel_arxiv_v3M.0.9.tar.gz`
sha256 `d295ded8593acd723bfe560be6e7ae895feed1464c96fed8c3377b3d87574509`,
rebuilt from scratch in `/tmp` (main.tex + pbh_compaction_fnl.png, inline
`thebibliography`, same convention as v3M.0.8), standalone extract+recompile
smoke test PASS (0 undefined refs, 12 pages).

**Not sourced from a committed file (disclosed).** None — every number
above traces to the source files named above or to the R3 truth audit.
