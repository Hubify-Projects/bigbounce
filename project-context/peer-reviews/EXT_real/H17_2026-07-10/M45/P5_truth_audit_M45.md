# P5 — M45 EXT truth-audit (skeptical, independent; auditor NOT told any convergence conclusion)

**Paper:** P5 DESI-chirality (`pipelines/p5_desi_chirality/paper/`), v0.1.127 — BYTE-UNCHANGED since prior waves (no edit this round).
**Raws read verbatim:** `M45/P5_grok_M45.md`, `M45/P5_chatgpt_M45.md`.
**Ledger:** `project-context/peer-reviews/DISPOSITIONS/P5.md` (27 D-ids; M43 = immediately-prior wave).
**ledger_match DRAFT (reference only):** Grok 2/5 auto-MATCHED, ChatGPT 1/13 auto-MATCHED — low auto-match rate is the known dilute-prose artifact; every finding source-cited below.

## Verdict lines (quoted verbatim, line 1 of each raw)
- **Grok:** `VERDICT: MINOR REVISIONS` (P5_grok_M45.md l.1). Closing (l.10): "The central claim of a catalog-native, classifier-label non-detection … is supported by the focal estimate, its interval, and the consistent nulls across sensitivities." → closing AFFIRMS the null.
- **ChatGPT:** `(1) VERDICT: MAJOR REVISIONS.` (P5_chatgpt_M45.md l.1). Closing (l.31): "Yes—within the manuscript's stated scope, the evidence supports the limited claim that this exploratory analysis finds no statistically significant dependence…" → concedes the scoped null.

## Provenance confirmation (paper-signature grep)
Both raws review the CORRECT paper — signatures present: DESIVAST, VoidFinder, T-Web, GALZONE, Δf_CW / f_CW, Paper IV, 2a−1, Bonferroni, cluster-sandwich NSIDE=4, focal estimand. Real assistant content, correct PDF, no wrong-paper/mislabel.

## DP5-26 held-absent check (artifact-range fix STAYS HELD)
`grep -niE '\[A1\]|\[A32\]|\[A34\]|artifact-range|A1--A32|\[A33\]'` over BOTH P5 raws → **NONE (exit 1, count 0).** Semantically re-verified: neither raw mentions the artifact-index range descriptor. **DP5-26 (v0.1.127 artifact-range fix) STAYS HELD — the reader-visible [A1]--[A32] range is gone and no fresh EXT read re-flags it.**

## Finding-by-finding disposition

### Grok (MINOR REVISIONS) — 5 findings (1 header non-finding + 4 real)
| # | finding | sev | D-id | verdict | source-cited justification |
|---|---------|-----|------|---------|-----------------------------|
| 1 | "REVISIONS ISSUES:" | — | — | **NON-FINDING** | Parser-header fragment (verdict-line scaffold), not a finding. |
| 2 | Focal GALZONE/VoidFinder hole-union hierarchy selected post-hoc after venue review/data inspection; post-selection of the most-null path undermines evidential priority of headline Δf_CW=+0.00125636 | MAJOR (in-MINOR tag) | **DP5-13** | RE-FLAG | Post-hoc primary-path designation + garden-of-forking-paths disclosed §V B `\label{sec:primary_path}` l.1668 + `tab:analysis_tree` l.1848 ("no timestamped plan predates the data"); abstract labels all bounds exploratory l.729-730. In-MINOR MAJ-tag under a MINOR-REVISIONS header = pattern-066 in-MINOR emphasis. |
| 3 | Logistic Eq.4 B-splines / NSIDE=4 cluster sandwich SE=0.00341274 p=0.71277 shown for one clustering variant; fuller specification-robustness table needed | MINOR | **DP5-10** | RE-FLAG | Spatial-covariance sensitivity closed-by-compute (v0.1.128) for the specified DESIVAST nearest-maximal clustering; the "one variant" limitation is the disclosed residual (DP5-10 body: "does not prove independence under all dependence structures"). Alternative-spec robustness = the same disclosed OPEN-COMPUTE axis. |
| 4 | No global family-wise / FDR bound across focal + 5 DESIVAST variants + 9 T-Web cells + scans; "no environmental dependence" rests on per-family not experiment-wide control | MINOR | **DP5-04 (+DP5-13)** | RE-FLAG | Bonferroni-5 primary family consolidated `tab:bonferroni5_family` §VIII D l.3454 (DP5-04); the few-dozen-trial analysis tree + post-hoc multiplicity are disclosed (DP5-13, §V B l.1668, abstract l.729-730). Experiment-wide-vs-per-family = framework-organization preference on disclosed content. |
| 5 | Secondary T-Web void bin (n=428, f_CW=0.4836) flagged survey-shell contaminated + non-load-bearing but should move to appendix/remove | MINOR | **DP5-14** | RE-FLAG | T-Web explicitly secondary/diagnostic/not-load-bearing (abstract l.718); the n=428 survey-shell demotion is the paper's OWN disclosure (DP5-14). Grok's earlier identical de-emphasize-n=428 minor was closed by a one-line demotion note (see M-history). Relegation = presentation OPINION, no science defect. |

### ChatGPT (MAJOR REVISIONS) — 13 findings (1 header non-finding + 7 MAJOR + 5 MINOR)
| # | finding | sev | D-id | verdict | source-cited justification |
|---|---------|-----|------|---------|-----------------------------|
| 1 | "REVISIONS. ext_P5_M45 (2) ISSUES:" | — | — | **NON-FINDING** | Parser-header + tag-echo fragment, not a finding. |
| 2 | Central claim depends on unpublished companion Paper IV classifier labels; referees cannot assess label quality/calibration until Paper IV is public+citable | MAJOR | **DP5-21** | RE-FLAG | Paper-IV dependency = OPEN-VENUE, disclosed §I "Independence from Paper IV internals" + §XIII "Relation to Companion Paper IV" + App A (public-inspectable labels + coordinated submission). Houston-gated venue barrier, not an editable defect. |
| 3 | Focal released-parent hierarchy changed after data inspection = exploratory not preregistered; p-value not confirmatory-strength; stronger exploratory/confirmatory separation needed | MAJOR | **DP5-13** | RE-FLAG | Post-hoc/exploratory designation disclosed §V B l.1668; abstract labels all bounds exploratory l.729-730. Same axis as Grok #2. |
| 4 | Numerous env definitions / T-Web grids / DESIVAST variants / membership defs / weighting / footprint / CV before selecting focal estimand; no rigorous framework for analytical-flexibility→evidential-strength | MAJOR | **DP5-13 (+DP5-04)** | RE-FLAG | Multiplicity/forking-paths disclosed (DP5-13, §V B l.1668 + `tab:analysis_tree` l.1848); Bonferroni-5 family consolidated (DP5-04, l.3454). Qualitative-vs-rigorous multiplicity framework = same disclosed axis. |
| 5 | Cluster-sandwich covariance uses coarse NSIDE=4 sky blocks; nearest-void-maximal clustering only as sensitivity; not justified as capturing true LSS spatial dependence | MAJOR | **DP5-10** | RE-FLAG | Spatial-covariance sensitivity closed-by-compute (v0.1.128; cluster SE 0.00232807 vs binomial 0.00231659, ratio 1.005, null preserved); DP5-10 discloses the closure is limited to the specified clustering and "does not prove independence under all dependence structures." Same as Grok #3. |
| 6 | Discussion still compares classifier-label null with cosmological parity-violation literature; comparisons should be softened since observable is not a physical handedness measurement | MAJOR | **DP5-08/-09 (+DP5-20)** | RE-FLAG | Classifier-label→physical-chirality scope disclosed; the 2a−1 physical-bound overreach was REMOVED in v0.1.128 (DP5-09 now "descriptive transfer context only, not a physical constraint") and the toy-EFT/parity bridge removed (DP5-20, v0.1.128). Parity-literature framing = the already-relegated speculative-App-B / physical-interpretation-scope class. |
| 7 | T-Web sections document known deficiencies (selection contamination, survey-shell, randoms-reassignment, under-resolved Rs=10, ASTRA/DESIVAST disagreement); condense/relegate | MAJOR | **DP5-14** | RE-FLAG | T-Web secondary/diagnostic/not-load-bearing (abstract l.718); ~73% reassignment / ~23× void-fraction are the paper's OWN randoms-weighted disclosures driving the demotion (DP5-14). Condense = presentation OPINION. |
| 8 | References internal artifacts/JSON/scripts/frozen RCs/Git commits not yet under immutable DOIs/release tags; PRD requires reproducibility | MAJOR | **DP5-18 (+DP5-21)** | RE-FLAG | DAS added v0.1.114 (DP5-18; DESI DR1 iron, DESIVAST VAC, HF catalog, DOI pointer); the pending-Zenodo-DOI + coordinated-submission is the OPEN-VENUE Paper-IV class (DP5-21, Houston-gated). Immutable-DOI-at-submission = disclosed venue item. |
| 9 | Manuscript substantially longer than necessary; robustness checks repeated; move sensitivity studies to appendices/supplementary | MINOR | **DP5-22** | RE-FLAG (OPINION) | Editorial-length / condensation D-round class (DP5-22 fingerprint: "extreme length, repeated caveats, condensation"). Presentation OPINION, no science change. |
| 10 | Multiple related statistics (σ_from_half, σ_pred, σ_vs_monopole, z_Δ, permutation p, cluster-sandwich); notation hard to follow despite glossary | MINOR | **DP5-19 (+DP5-22)** | RE-FLAG (OPINION) | Statistical-framework "overcomplicated" simplification preference = DP5-19 (two-sample contrast IS the primary estimand; extra σ diagnostics disclosed as supporting, not competing primaries); notation legibility = DP5-22. Presentation OPINION. |
| 11 | Caveats/methodological qualifications repeated across Intro/Results/Discussion/Limitations/Conclusions; consolidate | MINOR | **DP5-22** | RE-FLAG (OPINION) | Repeated-caveats/condensation D-round class (DP5-22). Presentation OPINION. |
| 12 | Cosmic variance, RSD, classifier uncertainty acknowledged but not in a unified uncertainty framework; concise discussion of what is/isn't in the CI would help | MINOR | **DP5-11 (+DP5-12)** | RE-FLAG | The ≈0.9pp heterogeneous non-probabilistic sensitivity summary is disclosed (DP5-11, "not a CI or exclusion threshold; calibrated joint interval still absent"); RSD bounded first-order (DP5-12, v0.1.122). "Unified framework / what's in the CI" = the same disclosed uncertainty-philosophy axis. |
| 13 | Most figures adequate but several sensitivity-analysis figures could move to supplementary | MINOR | **DP5-22** | RE-FLAG (OPINION) | Figure-legibility / move-to-supplementary D-round class (DP5-22). Presentation OPINION. |

## Genuinely-new count & streak decision
- **Genuinely-new real+editable findings: 0.** Every real finding is a source-cited re-flag of a standing DP5 D-id (post-hoc/multiplicity DP5-13/-04; spatial-covariance DP5-10; T-Web DP5-14; Paper-IV/DOI DP5-21/-18; physical-interpretation DP5-08/-09/-20; presentation/notation DP5-22/-19/-11/-12). Two header non-findings (Grok #1, ChatGPT #1).
- **No finding could NOT be source-cited** — zero genuinely-new candidates. Nothing forced; every mapping cites a D-id + section/line.
- **DP5-26 held-absent: YES.**
- **Item set matches M34/M37/M41/M43 disclosed-content set** (footprint/post-hoc/multiplicity/covariance/T-Web/Paper-IV/physical-interp/presentation) — cross-run stability, 0 genuinely-new.
- **directive_g.sh: NOT run** (byte-unchanged v0.1.127, no edit).
- **Integrity:** verdict words recorded as-is (Grok MINOR / ChatGPT MAJOR); no ACCEPT faked; no finding dismissed without a source-cited verdict; no fabrication.

### STREAK DECISION: P5 clean-wave streak 6 → 7 (seventh consecutive clean wave on post-DP5-26 v0.1.127).
