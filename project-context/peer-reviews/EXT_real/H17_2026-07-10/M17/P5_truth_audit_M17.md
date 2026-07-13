# P5 EXT truth-audit — M17 (2026-07-13)

**Target:** P5 v0.1.126, byte-UNCHANGED (served md5 4458e760, 8 paths; no edit this wave).
**Raws read + verified before any verdict:** `M17/P5_grok_M17.md`, `M17/P5_chatgpt_M17.md` (+ screenshots).
**Method:** `tools/ledger_match.py` pre-triage → full Opus §3 source-cited disposition of every finding, incl. every mechanically-UNMATCHED item (matcher is conservative; prose dilution suppresses keyword recall).

## Grok EXT = MINOR REVISIONS (1 MAJ / 3 MIN)
Same in-MINOR emphasis pattern as M14 (lone MAJOR under a MINOR-REVISIONS header). ledger_match 4/5 MATCHED (the 1 UNMATCHED = `#1 "REVISIONS ISSUES:"` scaffold-header parse artifact, not a finding).

| # | sev | finding | disposition |
|---|-----|---------|-------------|
| MAJ | §V.B/abstract | post-hoc "exploratory not pre-registered" primary estimand + Bonferroni-5 family; wants front-loaded caveat that ≈0.9pp / ≈2.26pp are tightest-among-post-hoc | **RE-FLAG DP5-13** (post-hoc/garden-of-forking-paths already disclosed §V.B l.1668 + abstract l.729-730; all bounds labeled exploratory) + **DP5-11** (0.9pp envelope disclosed) |
| MIN | abstract/§VIII | RSD Zel'dovich shifts Δf_CW by only 0.024pp but DESIVAST catalog not re-derived under full nonlinear recon — state in abstract/summary | **RE-FLAG DP5-12/-22** (CLOSED-BY-COMPUTE first-order; the nonlinear-catalog-regeneration residual is the paper's OWN disclosed limitation §VIII/§XIII, abstract RSD clause) |
| MIN | abstract/§II | 2.26pp de-attenuation assumes same linear attenuation for an env-conditional signal — confirm/reference before presenting as "quantity model-builders should use" | **RE-FLAG DP5-21/-09** (Paper-IV κ=0.40 monopole justification referenced §II; symmetric-error caveat carried abstract l.749-757) |
| MIN | §VI.A/VII | 2.1σ T-Web sign-flip = selection diagnostic, no end-to-end injection-recovery mock — cross-ref when T-Web introduced | **RE-FLAG DP5-14** (T-Web explicitly secondary/diagnostic/not-load-bearing, abstract l.718; §VI D χ²/sign-flip ambiguity is the paper's own disclosure) |

**0 genuinely-new reader-visible editable.** Fresh-content re-placement/footnoting asks on already-present, already-disclosed content.

## ChatGPT EXT = REJECT (12 MAJ / 2 MIN) — verdict-word regression on byte-unchanged v0.1.126
P5's ChatGPT has been **MAJOR-modal** (M3b/M6/M9/M12/M14 all MAJOR REVISIONS). M17 = REJECT — a **verdict-word regression on byte-identical content**. ledger_match 11/14 MATCHED; the 3 mechanical UNMATCHED all Opus-adjudicated RE-FLAG below.

**pattern-066 verdict: CONFIRMED referee-word oscillation, NOT new findings.** The M17 item set is **1:1 with the H17H ChatGPT REJECT** and the M3b/M6/M9/M12/M14 ChatGPT MAJOR reads — identical disclosed-content set, zero genuinely-new items. ChatGPT has now printed REJECT (H17H, M17) and MAJOR (M3b/M6/M9/M12/M14) on the SAME byte-unchanged paper: textbook maximal-harsh-referee verdict-word floor oscillation (pattern-066), documented in H17H addendum. No content moved; the verdict word did.

| # | finding | disposition |
|---|---------|-------------|
| 1 | footprint-restricted control not selection-function-matched (union of hole discs ≠ DESIVAST/BGS mask/randoms/IPW) | **RE-FLAG DP5-06** (footprint≠selection function disclosed §VIII B l.3033) |
| 2 | Bonferroni-5 family doesn't contain the designated exact primary (57,081 vs 56,981; footprint-restricted vs unrestricted) | **RE-FLAG DP5-02/-13** (exact-membership seam CLOSED-BY-EDIT v0.1.115; post-hoc family disclosed) |
| 3 | 0.9pp bound has no CI interpretation; quadrature 0.948pp must center on +0.181pp → [−0.77,+1.13]; physical ≈2.8 not 2.26 | **RE-FLAG DP5-11** (quadrature envelope method fully disclosed §VIII; peak-excursion-vs-SD noted; statistical-philosophy OPINION) |
| 4 | binomial errors assume independence; clustered sampling → void-level/angular-block bootstrap needed | **RE-FLAG DP5-10 OPEN-COMPUTE** (counting-only CI explicitly disclosed; cluster/void bootstrap is the standing open recompute) |
| 5 | de-attenuation not justified; single global accuracy ≠ common attenuation across void/non-void | **RE-FLAG DP5-08/-09** (void-stratum confusion CLOSED-BY-COMPUTE v0.1.118 N=933 p=0.37; ±3.7pp under-power → de-attenuation caveat DP5-09 STAYS) |
| 6 (UNMATCHED 0.23) | "adjustment in lieu of full covariate regression" — needs matching/IPW/regression on primary contrast NOW not DR2 | **RE-FLAG DP5-19 + DP5-06** (§VIII B `\emph{Adjustment in lieu…}` l.3273-3293 already states the target logistic CW∼void+z+…+IPW, reports program-split + budget as the adjustment set, DR2-robustness disclosed; reviewer quotes the paper's own paragraph title) — fingerprint already enriched in H17H |
| 7 | 0.02pp RSD not established without rerunning VoidFinder on reconstructed field | **RE-FLAG DP5-12** (CLOSED-BY-COMPUTE first-order; full nonlinear catalog re-derivation = disclosed residual) |
| 8 | canonical T-Web dominated by selection (73% relabel, 23× void-fraction) — remove from evidentiary chain | **RE-FLAG DP5-14** (T-Web is secondary/diagnostic; the 73%/23× is the paper's OWN sensitivity disclosure driving demotion) |
| 9 | five void definitions don't measure a common estimand (PIS ≠ watershed native; maximal-sphere reassigns 36,181) | **RE-FLAG DP5-16** (sphere-PIS labeled author-constructed proxy; GALZONE catalog-native rows tabulated — disclosed+quantified) |
| 10 | bounce/inflation connection not demonstrated; App B non-covariant toy — remove | **RE-FLAG DP5-20** (App B labeled speculative/outside empirical scope/not-derived — already relegated) |
| 11 | load-bearing labels depend on unavailable Paper IV (placeholder arXiv, pending DOI) — co-review required | **RE-FLAG DP5-21 OPEN-VENUE** (Paper-IV coordination disclosed §I/§XIII/App A; Houston-gated, not editable) |
| 12 (UNMATCHED 0.25) | non-rejection overstated as environment independence; needs equivalence test/margin | **RE-FLAG DP5-04 + DP5-19** (abstract labels the result a Bonferroni-corrected non-detection, not equality; equivalence-margin framing is the DP5-19 presentation-preference class) |
| 13 MIN (UNMATCHED 0.12) | SPECTYPE=QSO retained in a spiral analysis — report count + rerun galaxy-only | **RE-FLAG DP5-22** (galaxy-only sensitivity is the standing disclosed cross-match/QSO item; fingerprint carries "SPECTYPE=QSO, galaxy-only sensitivity") |
| 14 MIN | excessively long/repetitive; move audit trails to supplemental | **RE-FLAG DP5-22** (length/condensation = standing cosmetic D-round item) |

**0 genuinely-new real+editable across ChatGPT.** Every MAJOR = disclosed-limitation / OPEN-COMPUTE (DP5-10) / OPEN-VENUE (DP5-21) / relegated-speculation (DP5-20) class; every MINOR = standing cosmetic re-flag.

## Verdict + bookkeeping
- **0 genuinely-new** across both legs → no bump; v0.1.126 stands (served md5 4458e760); directive_g.sh NOT run.
- **Clean-wave streak 6 → 7.**
- **Cap 80 → 74** per the EXT formula on the true `_creationTime`-latest-per-reviewer row: Grok minor-revisions (12) + ChatGPT **reject (0)** + Gemini minor-revisions (12) = 50 + 24 = **74**. This honestly reflects the ChatGPT REJECT (down from the prior ChatGPT MAJOR=6 that held cap at 80). post_verdict.sh recomputes this automatically from the latest rows; no hand-set.
- Integrity: no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.
