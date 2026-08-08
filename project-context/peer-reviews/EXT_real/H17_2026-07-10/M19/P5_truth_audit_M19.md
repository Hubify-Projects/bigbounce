# P5 EXT truth-audit — M19 (2026-07-13)

**Target:** P5 v0.1.126, byte-UNCHANGED (served md5 4458e760, 8 paths; no edit this wave).
**Raws read + verified before any verdict:** `M19/P5_grok_M19.md`, `M19/P5_chatgpt_M19.md` (+ screenshots).
**Method:** `tools/ledger_match.py` pre-triage → full Opus §3 source-cited disposition of every finding, incl. every mechanically-UNMATCHED item (matcher is conservative; prose dilution suppresses keyword recall).

## Grok EXT = MINOR REVISIONS (0 MAJ / 3 MIN)
ledger_match 3/4 MATCHED (the 1 UNMATCHED #1 = `"REVISIONS ISSUES:"` scaffold-header parse artifact, not a finding). Same in-MINOR emphasis pattern as M14/M17.

| # | sev | finding | disposition |
|---|-----|---------|-------------|
| 2 | MIN | Title "Three-Algorithm Void Null Test" vs the five-definition Bonferroni-5 family (VoidFinder + V2-REVOLVER/VIDE + GALZONE/ZONEVOID) — retitle "Multi-Algorithm/Five-Definition" | **RE-FLAG DP5-04** (five-definition family disclosed §V.B/§VIII; title-vs-body terminology re-flag, cosmetic) |
| 3 | MIN | add one abstract sentence that the primary-estimand + DESIVAST-anchor choice was made after inspecting T-Web/Tempel-FoF/ASTRA, to preempt post-hoc concern | **RE-FLAG DP5-13** (post-hoc "exploratory not pre-registered" + garden-of-forking-paths already disclosed §V.B l.1668 + abstract l.729-730; front-loading a disclosed caveat) |
| 4 | MIN | Table XI quadrature envelope needs one para justifying term-independence + why quadrature not linear sum + that the envelope applies to observed Δf_CW pre-de-attenuation | **RE-FLAG DP5-11** (0.9pp quadrature envelope method disclosed §VIII; a justification-paragraph ask on a disclosed method) |

**0 genuinely-new reader-visible editable.** Grok's own line: central null "is supported." Fresh-placement/footnoting asks on already-present, already-disclosed content.

## ChatGPT EXT = REJECT (10 MAJ / 2 MIN) — 2nd CONSECUTIVE verdict-word regression on byte-unchanged v0.1.126
P5's ChatGPT has been **MAJOR-modal** (M3b/M6/M9/M12/M14 all MAJOR) then printed **REJECT at M17** on byte-identical v0.1.126 (M17 already confirmed pattern-066 on the first slip). **M19 = REJECT AGAIN — 2nd consecutive** on the same byte-unchanged content. ledger_match 10/12 MATCHED; the 2 mechanical UNMATCHED all Opus-adjudicated RE-FLAG below.

**pattern-066 verdict: CONFIRMED (2nd consecutive) referee-word oscillation, NOT new findings.** The M19 item set is **1:1 with the M17 ChatGPT REJECT and the M3b–M14 ChatGPT MAJOR reads** — identical disclosed-content set, zero genuinely-new items. ChatGPT has now printed REJECT (H17H, M17, M19) and MAJOR (M3b/M6/M9/M12/M14) on the SAME byte-unchanged paper: textbook maximal-harsh-referee verdict-word floor oscillation, now stable at REJECT for two consecutive reads without any content change. No content moved; the verdict word did.

| # | finding | disposition |
|---|---------|-------------|
| 1 (UNMATCHED 0.25) | 101,863 hole spheres called "interior" but DESIVAST flags ~1,489 interior VoidFinder voids, >60% edge; recompute with edge flag, report interior/edge separately; maximal-sphere-only ≠ hole-union estimand | **RE-FLAG DP5-01/-16** (primary-estimand definition CLOSED-BY-EDIT v0.1.114/115; maximal-sphere-vs-hole-union is the disclosed author-constructed-proxy seam DP5-16; edge/interior split = the standing footprint-sensitivity disclosure) |
| 2 | "footprint-restricted" control ≠ DESIVAST mask / BGS selection / randoms; concedes fibre-assign/depth/radial unmatched yet calls it "same-selection-function" | **RE-FLAG DP5-06** (footprint ≠ selection function disclosed §VIII B l.3033) |
| 3 | Bonferroni-5 family doesn't contain the designated primary (exact footprint-restricted +0.0018 vs the family's k=20 unrestricted +0.0007); tree omits exact-vs-k20/footprint-vs-unrestricted/etc | **RE-FLAG DP5-01/-13** (exact-membership seam CLOSED-BY-EDIT v0.1.115; post-hoc family disclosed exploratory) |
| 4 | 0.9pp "honest 2σ envelope" not a defined CI (binomial half-width + peak-excursions treated as independent Gaussian, partial double-count); shouldn't be advertised as 95% coverage without end-to-end mock | **RE-FLAG DP5-11** (quadrature envelope method fully disclosed §VIII; peak-excursion-vs-SD noted; the separate Bonferroni ~1.1pp interval is the formally-interpretable companion; statistical-philosophy OPINION) |
| 5 (UNMATCHED 0.22) | two-proportion SEs treat galaxies as independent Bernoulli despite shared voids/regions/imaging; label-shuffle destroys dependence; needs block jackknife/cluster-robust | **RE-FLAG DP5-10 OPEN-COMPUTE** (counting-only CI explicitly disclosed "not a full systematic budget"; cluster/void-level bootstrap = the standing disclosed recompute) |
| 6 | no covariate adjustment on the load-bearing DESIVAST contrast (only secondary T-Web adjusted; DESIVAST regression deferred to DR2); program-fraction balance ≠ covariate balance | **RE-FLAG DP5-03/-19** (§VIII B "Adjustment in lieu…" l.3273-3293 states the target logistic + reports the adjustment set + DR2-robustness disclosure; reviewer quotes the paper's own paragraph) |
| 7 | de-attenuation by 2a−1 identified only under nondifferential symmetric sensitivity; void human-label validation N=933 several-pp-wide can't validate sub-percent; hard-argmax + NS-exclusion adds unmodelled selection; ~20–21% D4 instability | **RE-FLAG DP5-08/-09** (void-stratum confusion CLOSED-BY-COMPUTE v0.1.118 N=933 p=0.37; ±3.7pp under-power → de-attenuation caveat DP5-09 STAYS disclosed) |
| 8 | canonical T-Web dominated by selection (640× shell-mean, 73% relabel, ~23× void-fraction under randoms-rebuild); rebuild or remove; can't supply 25 h⁻¹Mpc scale to DESIVAST | **RE-FLAG DP5-14** (T-Web secondary/diagnostic/not-load-bearing abstract l.718; the 640×/73%/23× is the paper's OWN sensitivity disclosure driving demotion) |
| 9 | RSD bound = fixed-catalog sensitivity diagnostic (0.024pp), not a bound — needs realistic mocks + full void re-finding; shouldn't enter Table XI as a systematic | **RE-FLAG DP5-12** (CLOSED-BY-COMPUTE first-order Zel'dovich; full nonlinear catalog re-derivation = disclosed residual §VIII/§XIII) |
| 10 | bounce/inflation interpretation not quantitative (no transfer function); App B toy is parity-EVEN not odd (both ∇φ·∇ρ and L̂·∇ρ pseudoscalars → product parity-even), dims/norm unspecified; remove App B | **RE-FLAG DP5-20** (App B labeled speculative/outside empirical scope/not-derived — already relegated; the parity-parity restatement targets a disclosed toy already flagged non-load-bearing) |
| 11 | load-bearing labels depend on unpublished companion (arXiv placeholder, DOI pending); linked model doc internally inconsistent (CW+CCW≠spirals; 1σ-vs-9.5σ); freeze under immutable DOI/hash + Paper IV co-available | **RE-FLAG DP5-21 OPEN-VENUE** (Paper-IV coordination + DOI freeze disclosed §I/§XIII/App A; Houston-gated pre-submission, not editable) |
| 12 MIN | DESIVAST has two families (VoidFinder + V2), REVOLVER/VIDE are two V2 prunings not three algorithms; fix terminology; condense 42pp | **RE-FLAG DP5-04/-16** (family terminology disclosed; length/condensation = standing cosmetic D-round item) |

**0 genuinely-new real+editable across ChatGPT.** Every MAJOR = disclosed-limitation / OPEN-COMPUTE (DP5-10) / CLOSED-BY-COMPUTE-residual (DP5-08/-12) / OPEN-VENUE (DP5-21) / relegated-speculation (DP5-20) class; every MINOR = standing cosmetic re-flag.

## Verdict + bookkeeping
- **0 genuinely-new** across both legs → no bump; v0.1.126 stands (served md5 4458e760); directive_g.sh NOT run.
- **Clean-wave streak 7 → 8.**
- **Cap → 74** per the EXT formula on the true `_creationTime`-latest-per-reviewer row: Grok minor-revisions (12) + ChatGPT **reject (0)** + Gemini minor-revisions (12) = 50 + 24 = **74**. Holds at 74 (the ChatGPT REJECT contribution was already 0 at M17); post_verdict.sh recomputes automatically — no hand-set.
- **pattern-066 documentation:** M19 is the **2nd consecutive** P5 ChatGPT REJECT on byte-identical v0.1.126 (M17 confirmed the first). Item set 1:1 with M17 REJECT + M3b–M14 MAJOR reads = confirmed stable maximal-harsh-referee verdict-word floor.
- Integrity: no ACCEPT faked; no finding dismissed without a source-cited verdict; no math fabricated.
