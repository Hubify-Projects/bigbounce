# P5 — M14-EXT truth-audit (STRICT, ledger-first) — 2026-07-12, vs v0.1.126

Second consecutive ZERO-REJECT harvest for P4+P5. Raws read VERBATIM before any
disposition:
- `M14/P5_grok_M14.md` l.1 = `VERDICT: MINOR REVISIONS` (1 MAJOR + 3 MINOR)
- `M14/P5_chatgpt_M14.md` l.1 = `VERDICT: MAJOR REVISIONS` (11 MAJOR + 2 MINOR)
  — ChatGPT floor-crack HOLDS (MAJOR not REJECT, as M3b/M6/M9/M12). Reviewers saw
  v0.1.126 (byte-unchanged). `tools/ledger_match.py` + full §3 Opus truth-audit
  vs `pipelines/p5_desi_chirality/paper/*.tex` + the canonical P5 ledger.

## ChatGPT MAJOR (11 MAJOR + 2 MINOR) — all source-cited standing re-flags
- #1 `REVISIONS ISSUES:` = parser-header noise (not a finding).
- #2 §VIII "footprint-restricted" ≠ selection-function-matched → **DP5-06** (§VIII B "Footprint ≠ selection function" para tex l.3033 states it is the geometric hole-disc∩radial union, explicitly NOT the completeness mask; mismatch in systematic_budget).
- #3 no covariate-adjusted (regression/IPW/matching) estimate → **DP5-02/-19/-06** (§VIII B "Adjustment in lieu of a full covariate regression" l.3273-3293: program-split + systematics budget as adjustment set; full logistic/IPW = disclosed DR2 future-robustness item; "we do not fabricate a regression coefficient").
- #4 post-hoc primary designation / headline estimator not in the Bonferroni-5 Table XIV family → **DP5-04/-13** (§V B sec:primary_path l.1668 + analysis-tree disclose post-hoc; consolidated Bonferroni-5 family tab:bonferroni5_family l.3454; exploratory framing abstract l.729-730).
- #5 "effective 2σ" 0.9pp envelope has no calibrated coverage; centered gives ~1.13pp → **DP5-11** (§VIII gives term list, √0.885=0.94pp, states terms approx-independent peak-excursions; ~1.1pp simultaneous family already the paper's own number — statistical-philosophy OPINION on disclosed method).
- #6 two-sample binomial independence / cosmic variance / cluster-robust needed → **DP5-10** (counting-only CI labeled "not a full systematic budget"; cluster/void-level bootstrap = disclosed OPEN-COMPUTE).
- #7 de-attenuated 2.26pp / dividing by 2a−1 only for symmetric non-differential error; void GZ1 ±3.7pp → **DP5-09/-08** (void-stratified confusion NOW computed v0.1.118, void N=933 diff −0.018 p=0.37; ±3.7pp arm corroborates-but-cannot-exclude, de-attenuation caveat STAYS — the reviewer cites the paper's OWN number).
- #8 VoidFinder any-hole union proxy / maximal-sphere 0.60pp / RSD Gaussian offsets → **DP5-16/-12** (sphere-PIS labeled "author-constructed approximation … permissive proxy" tab captions l.3310; RSD first-order Zel'dovich closure v0.1.122 bounds |shift|=0.024pp ≈40× under envelope; full VoidFinder-rerun = disclosed residual).
- #9 canonical T-Web unweighted / randoms-weighted rebuild flips ~73% / 23× void-fraction → **DP5-14** (T-Web explicitly secondary/diagnostic/not-load-bearing abstract l.718; the ~73%/~23× randoms sensitivity is the paper's OWN disclosure driving the demotion).
- #10 fundamental-physics interpretation / parity-even toy operator / no bounce forward model → **DP5-20** (App B + Conclusions label the EFT mapping "speculative … outside the empirical scope … not a derived constraint" — already relegated; the parity-even-operator objection targets the explicitly-speculative App B, same as M9).
- #11 Paper-IV dependency / placeholder arXiv / pending DOI → **DP5-21** (OPEN-VENUE; §I + §XIII + App A disclose coordinated submission; Houston-gated, not editable).
- #12 abstract/Conclusions "no room" for 2–4pp inconsistent with attenuation (2pp→~0.8pp not excluded) → **DP5-11/-09** (same disclosed-envelope + de-attenuation-caveat pair; the ~1.1pp simultaneous bound + STAYING caveat already encode this).
- #13(MIN) §III sample definition / SPECTYPE==GALAXY / QSO interlopers / "volume-limited" label / sample-flow table → **DP5-07/-22** (GALAXY-only path + z≤0.24 truncation disclosed §VIII; QSO/match-radius provenance in systematic_budget; volume-limited claim scoped to the void anchor).
- #14(MIN) presentation / 42pp / advocacy terms ("honest","clean","load-bearing") / shorten → **DP5-22/-19** (cosmetic D-round / presentation OPINION on already-tabulated content).

## Grok MINOR (1 MAJOR + 3 MINOR) — AFFIRMS the qualitative null
Closing (verbatim, raw l.10): the central claim "is supported by the
multi-algorithm DESIVAST statistics, secondary T-Web nulls, and honest
systematic envelope." The lone [MAJOR] is under a `VERDICT: MINOR REVISIONS`
header — a within-MINOR emphasis flag, not a reject-tier finding.
- #1 header noise.
- #2(MAJOR-labeled) DESIVAST path post-hoc / 0.9pp envelope among 5 correlated void defs "data-dependent" → **DP5-13/-11** (post-hoc disclosed §V B l.1668; Bonferroni-5 family-wise null is the strictly-quotable headline; 0.9pp envelope method disclosed §VIII).
- #3(MIN) systematic-envelope per-term derivations only summarized / geometry 0.60pp term → **DP5-11/-16** (term list disclosed §VIII; maximal-sphere 0.60pp membership perturbation tabulated systematic_budget).
- #4(MIN) 2.26pp de-attenuation factor 2a−1≃0.40 asserted not derived → **DP5-09/-08** (κ=0.40 GZ1 floor; void-stratified matrix computed v0.1.118; caveat disclosed abstract l.749-757).
- #5(MIN) 2.1σ T-Web filament sign-flip / Cramér's V=0.078 / BGS-leg one-paragraph consolidation → **DP5-14** (χ²/sign-flip ambiguity is the paper's OWN §VI D disclosure; T-Web secondary/diagnostic; 0.001pp leakage into primary quantified).

## Outcome
- ledger_match: Grok 4/5 auto-MATCHED; ChatGPT 12/14 auto-MATCHED — every
  UNMATCHED item Opus-adjudicated above (parser-header noise or source-cited
  re-flag). Identical disclosed-content set to M3b/M6/M9/M12.
- **0 genuinely-new reader-visible editable findings.** All RE-FLAG-DISCLOSED /
  CLOSED-BY-COMPUTE / OPEN-COMPUTE / OPEN-VENUE / OPINION.
- **clean-wave streak 5→6.**
- No bump; **v0.1.126 stands** (served md5 4458e760); `directive_g.sh` NOT run
  (no edit).
- **Cap HOLDS 80** (Grok MINOR 12 + ChatGPT MAJOR 6 + latest-EXT-Gemini MINOR 12
  = 50+30).
- **Integrity:** both raws read verbatim before disposition (Grok l.1
  `MINOR REVISIONS`, ChatGPT l.1 `MAJOR REVISIONS`); Grok's lone in-MINOR MAJOR
  recorded as MINOR verdict per its own header; no ACCEPT faked; every finding
  source-cited; no math fabricated; no version bumped.
