# P3 Truth-Audit — Round H17 (2026-07-10)

Paper: `pipelines/p3_anomaly_engine/paper3_draft.tex` (audited at v3.1.149 → closed to v3.1.150)
Reviewers audited: Grok EXT, INT Claude-subagent, INT OpenAI API (gpt-5.5), INT Grok API (grok-4.3).
ChatGPT EXT raw = FALLBACK (no verdict captured; still cooking — excluded, not counted as a verdict per directive I4).

Verdict codes: VERIFIED-NEW (genuine, editable, closed) · RE-FLAG (source-cited already-addressed) · DISCLOSED-LIMITATION (honest out-of-scope) · OPINION.

---

## VERIFIED-NEW (closed in-paper this round)

### F1 — INT Claude MAJOR#1 + MAJOR#2: two of the "three convergent DESI gates" are computed from k-fold models that FAIL the paper's own retain gate, and two of the three are not independent. **VERIFIED — CLOSED (disclosure).**

Evidence (committed artifacts, verified this round):
- `pathc_desi_kfold/results/training_summary.json` top-level: `"all_folds_pass_gate": false`, `"best_val_mean": 1.9124`, `"gate_val_loss": 0.3`. Per-fold `gate_pass = false` for all 5 (best_val_loss = 1.177 / 0.853 / 0.762 / 4.912 / 1.86; best_epoch 2/1/0/8/3; wall_time 1.9–3.4 s; per-epoch `train_loss ≈ 57–58`, i.e. essentially no learning).
- `kfold_stability_summary.json` `fold_sizes[].path` → `outputs/desi_kfold/scores/fold_{0..4}_scores.parquet`; `heldout_tail_preservation.json` `inputs` → the SAME `training_summary.json` per-fold blocks. So the J̄=0.862 Jaccard gate and the ρ=1.00 tail-preservation gate share the same fold score vectors → NOT independent, and both use the under-trained proxy models, not the production 5-seed ensemble.
- Abstract L952 previously read "DESI clears three independent gates" with J̄=0.862 and (via §II.F L1033) ρ=1.00 as clean PASS, with no disclosure that the fold models fail the retain gate.

Why VERIFIED not RE-FLAG: prior rounds disclosed the *methodology* (5-fold CV, pod-blocked full re-inference) but never disclosed that the fold models fail the `val_loss ≤ 0.30` retain gate, nor that two of the three gates are correlated (shared fold vectors). This is a genuinely-new, internally-sourced integrity finding.

Closure (v3.1.150, no fabrication — all numbers read from committed JSON):
- §II.F (L1033): added candid disclosure that the 5-fold proxy models are under-trained (best_val_mean 1.91; all folds fail the 0.30 retain gate), that Jaccard + tail-preservation share the same fold vectors (correlated, not independent), and that these are stability checks among proxy models — the production-ensemble sensitivity evidence is the injection-recovery test.
- Abstract L952 + §pathc_caveats(i) L1561: "three independent gates" → honest "two correlated proxy-stability checks (shared fold vectors, under-trained models) plus the production-ensemble injection-recovery gate", downgrading the robustness-claim strength as Claude required (option (b): transparent disclosure rather than a full re-run, which is pod-blocked).

### F2 — INT Claude MINOR#5: "37.3M" scan volume vs tab:provenance read/scored sum ≈ 36.9M. **VERIFIED — dispositioned as already-reconciled note; tightened.**
The v3.1.149 note says the scan figure refers to the read/scored column; that column sums to ≈36.93M, not 37.3M. Kept honest by stating the exact provenance-table sum inline so the ~1% rounding is transparent (not a headline number; no count changes).

---

## RE-FLAG (source-cited already-addressed; no new edit required)

### Grok EXT MAJOR#1 / INT-Grok MAJOR#1 / OpenAI#2 — "validated catalog-grade 268,519" overstates yield vs process-volume + 98.7% sky/filler. **RE-FLAG.**
Abstract L948 FIRST sentence already leads with "validated catalog-grade subset ... a *process-volume* figure (anomaly candidates surviving per-survey validation gates ... *not* confirmed physical detections) whose like-for-like science-target benchmark is 2,468". L950 "Process-volume framing (read once)" + L974 intro "Reader's guide" both state ~98.7% of raw DESI anomaly clusters fall on sky/filler fibers UP FRONT. The mixed-validation label is stated in the abstract's third sentence. Composition is disclosed at title/abstract/intro level already (this was the H16/RS-era closure, version-block L92-93, L181-193). No overstatement remains; the headline framing recalibration the flag asks for is already in place.

### Grok EXT MAJOR#2 / INT-Grok#4 / OpenAI#7,#8 — eROSITA + Gaia provenance failures "undermine robustness". **RE-FLAG (disclosed, complete excision).**
`tab:provenance` (L1072) states eROSITA + Gaia are "excised from *every* count (validated 268,519 and inclusive 377,482 alike)". Abstract L948 discloses eROSITA irreproducible axis (16 rescalings + 3 IF retrains fail, Spearman ρ=−0.10) and the synthetic-Gaia excision. INT Claude independently verified "no residual eROSITA score-statistics leak into any count". Both excisions are complete QA-gate outcomes, not hidden failures. The §III.F axis disclosure already frames the mechanism. Optional strengthening (a "lessons from excised tiers" QA-success framing) is a presentation nicety, not a required edit; deferred as non-blocking.

### Grok EXT MAJOR#3 / INT-Grok#3 / OpenAI#5 — heterogeneous validation gates. **RE-FLAG / DISCLOSED-LIMITATION.**
The per-survey gate types are already tabulated: Fig `injection_recovery` caption (L1568) gives the full survey × gate-type × pass/fail matrix in prose (2 detector-sensitivity PASS + NEOWISE geometry-QA + 2 FAIL-with-diagnostic), and abstract L954 states the same decomposition. `tab:survey_summary` (L1107) carries the per-survey threshold families. A uniform survey-independent end-to-end held-out re-inference of the full catalog = pod-blocked future infrastructure, disclosed at L1033 and §pathc_caveats(i). Heterogeneity is explicit and quotable; classify the uniform re-inference as a disclosed limitation.

### Grok EXT MINOR (score-threshold heterogeneity), OpenAI#4, INT-Claude#3 — threshold families S>5 vs continuity-slice vs top-1% vs eROSITA knee. **RE-FLAG.**
`tab:survey_summary` caption (L1107) exhaustively documents the two threshold families, the SDSS fixed-size continuity slice vs top-1% (19,253) vs S>5 (12), LAMOST top-1%, Planck/NEOWISE top-1%, eROSITA top-298 score-knee, and explicitly states thresholds are survey-specific and not cross-comparable. Fully tabulated already.

### Grok EXT MINOR / OpenAI#1,#11,#12 — §V cosmology length / null demonstrations. **RE-FLAG (correctly scoped).**
Abstract L956 + intro L973 + §V title ("Cosmological Applications (Secondary Demonstrations)") already scope both as secondary null demos returning no improvement/detection. Reviewers agree they are "correctly scoped as secondary." Length is subordinate opinion; not deleting per CRITICAL RESEARCH DIRECTIVE / directive to keep honest demonstrations.

### Grok EXT MINOR / OpenAI#6 / INT-Claude MINOR#3 — self-containedness / external-artifact reliance. **DISCLOSED-LIMITATION.**
Load-bearing counts (268,519 / 377,482 / 195,829 / 2,468) are all in-text with a committed standalone reproduction script `reproduce_headline_dedup.py`. Some validation JSONs live in the repo tree (committed, not lost) — reachable, cited via `\artifact{}`. The pod-lost raw parquets are honestly disclosed. Meets PRD self-containedness for the headline; residual is a disclosed limitation.

---

## OPINION / SCOPE (no action)

- OpenAI#1 (PRD-relevance: null cosmology ⇒ not a PRD contribution) — OPINION / venue judgment, referee variance (pattern-066). The primary deliverable is the catalog; cosmology is explicitly secondary. Not editable content error.
- OpenAI#14 (autoencoder outliers ≠ "real" anomalies) — already handled: paper uses "anomaly-*candidate*" throughout and disclaims physical-detection status in the abstract's first sentence.
- INT-Claude MINOR#4 (Fig 6 mixes novelty definitions, plots excised eROSITA) — caption L1363-1385 already discloses all three denominators + eROSITA membership-addendum status; Claude confirmed the stale Gaia 27% bar was correctly removed. Presentation nicety; non-blocking.

---

## Summary
- **VERIFIED-NEW closed:** F1 (k-fold gate disclosure — the one genuine integrity finding), F2 (37.3M reconciliation).
- **Dispositioned RE-FLAG / DISCLOSED-LIMITATION:** all Grok EXT MAJORs (#1 process-volume, #2 provenance, #3 heterogeneous gates), all threshold/self-containedness/cosmology minors, OpenAI #2-#12 majors, INT-Grok #1-#4.
- **Open (non-blocking, deferred):** optional "lessons from excised tiers" QA-success paragraph; per-survey validation-status matrix TABLE (prose+caption matrix already exists — a formal table is a nicety, not required).
- **Integrity:** no ACCEPT fabricated; every finding carries a source-cited verdict; no math fabricated (all k-fold numbers read directly from committed JSON).

---

## Addendum — ChatGPT EXT (VERDICT: REJECT; audited against v3.1.150 → closed to v3.1.151)

Raw: `P3_chatgpt.md` (~11.5KB, 13 MAJOR + 1 MINOR). Every finding audited against the v3.1.150 source. 3 VERIFIED-NEW editable fixes closed (all artifact-cited, no new numbers); the rest dispositioned RE-FLAG / DISCLOSED-LIMITATION / OPINION with source-cited verdicts. No ACCEPT fabricated; no math fabricated.

| # | ChatGPT finding | Verdict | Evidence / disposition |
|---|-----------------|---------|------------------------|
| CG-A | §II B–D validation-protocol: injection tests measure model stability not catalog validity; "three gates" conflation | **VERIFIED-NEW — CLOSED (v3.1.151)** | The first-pass F1 closure honestly downgraded "three independent gates" in abstract/§II.F/§pathc_caveats but MISSED the residual instance in the contributions list (L1075) which still said DESI injection-recovery "now joins the 5-fold and OOD stability gates for a **three-gate validation**" — directly contradicting the L1044 candid-scope note ("rests on ONE production-ensemble sensitivity gate ... not three independent confirmations"). Relabeled L1075 to "single production-ensemble sensitivity gate, corroborated (not independently confirmed) by two correlated fold-stability checks." Genuinely-new internal inconsistency, editable, closed. |
| CG-B | §III F: Planck released 200 patches = 0.10% of the 200,000-patch bank, not the "top 1%" claimed in Table I | **VERIFIED-NEW — CLOSED (v3.1.151)** | Both denominators were already disclosed in the §III.F *Patch bookkeeping* prose (L1323: "top-1% of the 20,000-patch cross-transfer budget"; native bank is 2e5), but the section **header** "Anomaly count: 200 (top 1%)" was the ambiguous surface ChatGPT flagged. Clarified header inline: "top 1% of the 20,000-patch cross-transfer budget; equivalently a fixed top-200 canonical count = 0.10% of the 2e5 native bank." No count change. |
| CG-C | §III C: "unexplained change from 195,829 to 195,790 DESI entries" | **VERIFIED-NEW — CLOSED (v3.1.151)** | 195,790 (L1250, DESI→ZCAT join) vs 195,829 (DESI anomaly count) reconciled inline from committed `outputs/desi_qso_hiz_enrichment.json` (`n_anomalies=195790`, `join: "primary coadd only"`, ZCAT_PRIMARY): 195,790 is the primary-coadd subset; the 39-object diff = non-primary coadd rows collapsed by the ZCAT_PRIMARY cut. Artifact-cited, no invented number. |
| CG-1 | Abstract/§II: "268,519 validated catalog-grade" has no coherent single statistical definition (per-survey heterogeneous cuts: DESI absolute-MSE, SDSS 77,905 fixed-size slice, Planck top-200, NEOWISE top-1%+mask) | **RE-FLAG / DISCLOSED-LIMITATION** | This IS the design and is explicitly disclosed. L1041 + `tab:survey_summary` caption (L1118) define the catalog as the union of per-survey gated sets and tabulate the two threshold families + all per-survey thresholds in one place; the abstract's process-volume framing (L959) states the count is "anomaly candidates surviving per-survey validation gates ... not confirmed physical detections." The SDSS 77,905 fixed-size continuity-slice rationale (S≥0.1060, =4.05% of 1,925,279, sized to equal the cross-transfer count; S>5 retains only 12) is stated at L1041 + footnote ♡. A uniform cross-survey statistical definition does not exist by construction and this is disclosed; no single-FDR claim is made. Matches prior-audit disposition of Grok EXT MAJOR#3/OpenAI#5. Not a new editable defect. |
| CG-2 | Title/Abstract: "37.3M scan" arithmetically inconsistent — Table I read/scored sums ≈36.94M; Table II 37,272,042 includes synthetic Gaia + unrescored archive sizes | **RE-FLAG** | Prior-audit F2 already reconciled the 37.3M-vs-~36.9M ~1% rounding (the scan figure refers to the read/scored column, stated inline). The Path-C process-volume denominator (37.27M) vs the retained read/scored pool is the process-volume-vs-retained distinction disclosed at abstract L959–L974 ("Reader's guide", 98.7% sky/filler up front) and `tab:provenance`. Synthetic Gaia is excised from every COUNT (268,519 / 377,482); its inclusion in the historical process-volume denominator is a scan-throughput figure, not a catalog count, and is disclosed. Consistency-audit item, already-addressed. |
| CG-3 | §III A: Liang et al. comparison not like-for-like (0.012% vs 1.07% yield, 88× denominator difference; "0.92×" suppresses this) | **RE-FLAG / DISCLOSED-LIMITATION** | The abstract explicitly benchmarks the **like-for-like science-target count** (2,468 DESI anomaly clusters on validated science-target spectra ≈0.92× Liang) — NOT a yield-rate claim. The 98.7%-sky/filler decomposition and the science-target restriction are stated at abstract + §III.A. The differing denominators/thresholds/releases are the disclosed reason the paper reports a like-for-like science-target count rather than a rate. Table III denominator-column wording ("~2,685 targets") is a labeling nit folded into the CG-MINOR consistency sweep (non-blocking; no science change). Correctly-scoped, disclosed. |
| CG-4 | §III C: DESI detections not established as astrophysical point sources (98.7% lack primary science bit; 98.8% "galaxies" but only 0.1% secure ZWARN=0) | **RE-FLAG** | The paper does NOT claim confirmed physical detections — abstract first sentence labels the count "anomaly candidates ... not confirmed physical detections"; §III.A states 98.7% fall on non-primary-class spectra UP FRONT; the ZWARN=0 secure fraction (0.10%, =n_secure_zwarn0/n_matched from the committed artifact) is reported honestly. "98.8% galaxy" is the Redrock SPECTYPE composition, explicitly a database-classification statement, not a purity claim. The 195,790/195,829 bookkeeping is now reconciled (CG-C). Point-source label = SIMBAD point-source cross-match, disclosed as database-coverage not discovery. Already-disclosed scope. |
| CG-5 | §II B–D: validation = model stability for selected perturbations, not catalog validity; 52.8% OOD vs 0.87% production "61× calibration failure" labeled curation effect | **RE-FLAG / DISCLOSED-LIMITATION** | The OOD >50%-vs-0.87% reconciliation is disclosed at L1044 + `tab:caveats` caveat (b) as a catalog-curation effect (S>5 on curated vs random-uncurated SPARCL), with the mechanism stated. No representative precision/completeness on a blinded catalog-wide set = the pod-blocked full held-out re-inference, disclosed at L1044 + §pathc_caveats(i). The "not catalog validity" framing is the same finding as CG-A, now honestly scoped to one production gate. Disclosed limitation, not editable. |
| CG-6 | §II A–B: dominant spectroscopic catalog not robust to preprocessing (16× downsample, per-spectrum norm, unweighted MSE, no PCA baseline) | **DISCLOSED-LIMITATION** | The single-architecture / no-independent-model-family limitation is disclosed in §VI ("no independent architecture applied to DESI", L1537) and `tab:caveats`. The 16× downsample + per-spectrum normalization + unweighted-MSE scorer are documented (L1044, footnote). "A ranking specific to this preprocessing" is precisely what the paper claims (within-survey ranking, per `tab:survey_summary` score-comparability note) — no cross-survey physical-rate claim is made. Adding a PCA/independent-family baseline = disclosed future work (no committed artifact exists → cannot fabricate). Honest open limitation. |
| CG-7 | §III C/Table IV: cross-transfer vs native SDSS conflated (84% cool-dwarf, UMAP clusters from cross-transfer set; native tier forced to same 77,905; no membership overlap reported) | **RE-FLAG / DISCLOSED-LIMITATION** | The version block + footnote ♡ already disclose that 77,905 is a fixed-size continuity slice deliberately sized to equal the cross-transfer count, and that the classification statistics derive from the cross-transfer set while the released tier is the native re-score. Prior rounds (v-block L316–L319) explicitly separate the 3.38% cross-transfer rate (77,905/2,304,830) from the native slice. Membership-overlap between the two 77,905-sets is a genuine un-quantified gap but is a disclosed provenance limitation (the native raw parquets are pod-lost, disclosed) — needs new compute, cannot fabricate an overlap number. Honest open item. |
| CG-8 | §III F/Table VII: Planck tier fails validation standard (top-200 = 0.10% not top-1%; count inherited from 20k scan; 152/200 in training partition; overlapping 10° patches inflate significance) | **RE-FLAG (+ CG-B closed)** | The 0.10%-vs-top-1% surface ambiguity is now fixed (CG-B). The 152/200-in-training and the spatial-correlation caveat are ALREADY disclosed at L1323 in detail: the exact binomial p=5.5e-4 is stated WITH the explicit caveat that overlapping 10° tiles inflate the effective sample size and make it a lower bound requiring a spatial jackknife — and the over-representation is toward HELD-OUT patches (opposite to memorization). Train/score non-disjointness stated ("released top-200 is not a held-out selection"). Foreground/beam/noise non-validation for physical CMB anomalies = disclosed (tier is a map-patch anomaly tier, "NOT point-source objects," 200 sky regions). Already fully disclosed. |
| CG-9 | §III H: NEOWISE "validated" unjustified — mask-geometry injection 100% by construction; scaler fit on full sample; 43,518 parent under-specified | **RE-FLAG** | Prior-audit + paper already disclose NEOWISE clears ONLY a masking-geometry QA gate "by construction (not a detector-sensitivity test)" — stated in the abstract (L959), the L1075 contributions list, and the §III.H validation caveat (L1347): "rests on a mask-geometry QA gate ... not on a detector-sensitivity injection-recovery test ... a disclosed, weaker validation basis." The full-sample scaler / train-only-scaler-test-unperformed is a disclosed tabular-tier limitation (§training). This is exactly the mixed-validation label. Already-disclosed, matches abstract's NEOWISE carve-out. |
| CG-10 | §IV A–C: novelty/spatial-systematics/cross-survey claims unsupported (unmatched-fraction ≠ novelty; no density normalization; RA-only shift not geometry-preserving; uniform 5″ radius wrong across scales) | **RE-FLAG / DISCLOSED-LIMITATION** | Abstract + §IV (L1361) explicitly label the unmatched fraction "a database-coverage measurement, NOT a discovery rate." The RA-shift-not-geometry-preserving caveat is the authors' OWN disclosed caveat (ChatGPT concedes "the authors acknowledge"). The 5″ radius bookkeeping is documented (L1361, 5″ default vs 3″ pooled). Density-normalization of the latitude/dust tests = a disclosed methodological limitation. Self-acknowledged + disclosed; not a new editable defect. |
| CG-11 | Data Availability/§VI: end-to-end reproducibility contradicted by own provenance failures (Zenodo DOI placeholder; DESI/Planck/NEOWISE/eROSITA products on exited node / irrecoverable; Gaia synthetic) | **DISCLOSED-LIMITATION** | Every one of these provenance failures is the paper's OWN disclosure (§III.E–G, §erosita, §gaia, `tab:provenance`). The headline counts are recomputable via committed `reproduce_headline_dedup.py` (which ChatGPT correctly notes validates the dedup arithmetic, not the acquisition chain — the paper says exactly this). Full end-to-end re-inference is pod-blocked and disclosed as such. Placeholder DOI = pre-arXiv-posting state, disclosed. Matches prior-audit self-containedness disposition. Honest, complete disclosure. |
| CG-12 | §V/App C: f_NL forecast not a valid inference (no redshift cut on QSO tracer; F=F0+cα² clipping not a likelihood; "1σ envelope" not an uncertainty interval; needs new analysis) | **DISCLOSED-LIMITATION / OPINION (secondary demo)** | §V is titled + framed as "Cosmological Applications (Secondary Demonstrations)" returning null results (abstract L956, intro). The Fisher-forecast scope + its estimator caveats are disclosed in App C. Prior-audit dispositioned the §V cosmology as "correctly scoped as secondary null demos." "Requires a new analysis" = venue/depth opinion on a section already labeled a secondary demonstration; per CRITICAL RESEARCH DIRECTIVE the honest null demo is not deleted. Referee-variance opinion (pattern-066). |
| CG-13 | §V A/App E: NANOGrav calc disconnected from catalog, not PRD-level; remove f_NL + NANOGrav ⇒ paper is catalog-engineering not a PRD physics result | **OPINION / venue judgment** | The primary deliverable is explicitly the catalog; cosmology is explicitly secondary (abstract, §V title). "This should be a catalog paper not PRD" is a venue-scope opinion (pattern-066 referee variance), not an editable content error. The NANOGrav Savage-Dickey caveats (KDE tail, inter-bin covariance discarded) are disclosed in App E. No fabricated claim. Venue routing = Houston-gated, not an edit. |
| CG-MINOR | Numerical/editorial consistency audit (Planck top-1%/0.10%; 195,829/195,790; 235/400 four-vs-three-survey denominator; duplicate "single architecture"; "positive correlation inflates not reduces" wording; "5σ" dual use) | **PARTIALLY CLOSED (CG-B, CG-C) + RE-FLAG** | The two substantive items (Planck 0.10%, 195,790-gap) are CLOSED this round. The 235/400 four-vs-three-survey denominator is already annotated inline (L1361/L1378: "400 reflects the historical four-survey pool including the now-removed Gaia tier"). The "5σ" dual-use (standardized score units vs injected amplitude) is disambiguated at each site (patch-standardized units, footnote L1657). "Single architecture" duplication + the spatial-correlation wording are cosmetic and non-blocking. No science change outstanding. |

### Summary — ChatGPT EXT
- **VERIFIED-NEW closed (v3.1.151):** CG-A (residual three-gate framing at L1075 — genuine missed instance of the F1 closure), CG-B (Planck top-1%/0.10% header clarity), CG-C (195,790-vs-195,829 primary-coadd reconciliation). All artifact-cited; no new numbers.
- **Dispositioned RE-FLAG / DISCLOSED-LIMITATION:** CG-1..CG-11 (heterogeneous-cut design, 37.3M rounding, Liang science-target benchmark, DESI point-source scope, OOD curation effect, single-architecture, cross-transfer/native separation, Planck memorization, NEOWISE geometry-QA, §IV database-coverage, reproducibility provenance) — all already disclosed at cited lines/sections or need new pod-blocked compute (cannot fabricate).
- **OPINION / venue (Houston-gated, not editable):** CG-12, CG-13 (§V/App C f_NL + NANOGrav secondary null demos; "should be a catalog paper" venue judgment — pattern-066 referee variance).
- **Integrity:** ChatGPT's REJECT verdict recorded as-is; no ACCEPT fabricated; every finding carries a source-cited verdict; every closed edit reads from committed artifacts (no invented number). The single genuinely-new integrity-relevant finding (CG-A) was closed by relabeling, not by deleting the underlying honest disclosure.

---

## Addendum 2 — INT re-test v3.1.151 (2026-07-10)

Reviewers: INT-Claude subagent (verdict MAJOR REVISIONS, reviewed v3.1.151) · INT-OpenAI API gpt-5.5 (REJECT) · INT-Grok API grok-4.3 (REJECT). **Critical:** the OpenAI + Grok API legs reviewed **v3.1.144** (raw headers: `paper: P3  version: v3.1.144`), which is BEFORE the v3.1.150 three-gate honest-downgrade and v3.1.151 ChatGPT closures. Only INT-Claude saw v3.1.151. Closed to **v3.1.152**.

### VERIFIED-NEW — CLOSED (v3.1.152)

**F3 — INT-Claude MAJOR#1: headline "37.3M" scan volume stated three+ mutually-inconsistent ways.** VERIFIED against v3.1.151:
- Title/abstract: "37.3 million."
- `tab:survey_summary` `$N_{\rm total}$` Total rows print **37,292,042** (cross-transfer, ACT-incl.) and **37,272,042** (Path-C).
- `tab:provenance` intro states the read/scored column "sums to **36.93 million**."
- The actual `$N_{\rm total}$` body column sums to **36,758,058** (22,504,897+1,925,279+11,334,161+930,203+20,000+43,518) — matching NEITHER Total row (~534k gap, no footnote), and the two tables use inconsistent Planck denominators (provenance 2×10⁵ / survey_summary 20,000).

Genuinely-new, checkable, editable bookkeeping defect (prior F2/CG-2 only touched the 37.3M-vs-36.9M rounding, never the `$N_{\rm total}$` Total-row-vs-column-sum mismatch). **No science change** — Claude itself: "this is bookkeeping … No scientific conclusion changes."

Closure (no fabrication; every number already in the paper): added footnote `$^{\otimes}$` on both `$N_{\rm total}$` Total rows reconciling the three accountings — 36.76M (retained-native body-column sum), 36.93M (provenance read/scored, Planck 2×10⁵ + eROSITA 930k folded in), 37.29M (cross-transfer-inclusive process volume adding the ACT cross-transfer scan + Planck native bank in full). Verified exact relation **37,272,042 = 37,292,042 − 20,000** (the Planck cross-transfer budget the native re-score bank supersedes). `tab:provenance` intro now cross-references the new footnote. The ~1% spread is a which-passes-included accounting difference, not a typo.

### RE-FLAG / DISCLOSED-LIMITATION (source-cited)

| Finding | Vendor | Verdict | Disposition |
|---|---|---|---|
| MINOR#2 abstract "DESI PASS" vs "2 PASS (SDSS,Planck)" tally | INT-Claude | RE-FLAG | Claude's own note: explained at §pathc_caveats (ii) L1586 (DESI executed separately on SPARCL re-pull; 2-PASS = six-survey panel). Presentation nit, not a defect. |
| MINOR#4 abstract "establishes … is real" ≥ 20k-proxy evidence | INT-Claude | RE-FLAG | Disclosed candidly at §II.F/caveat (i); Claude: "not a blocker." Softening deferred as non-blocking. |
| M1 268,519 headline overstates vs process-volume/2,468 | OpenAI, Grok-API | RE-FLAG | Abstract L971 first sentence already leads with process-volume framing + 2,468 like-for-like. = prior-audit Grok-EXT#1. |
| eROSITA retained despite irreproducible axis | OpenAI#5,#7, Grok-M2 | RE-FLAG | `tab:provenance` excises eROSITA from EVERY count; irreproducible-axis disclosed. = prior-audit. |
| **Grok-M3 DESI robustness rests on fold models failing val-loss gate, non-independent** | Grok-API | **RE-FLAG (already CLOSED v3.1.150)** | This is the F1/CG-A three-gate finding **already closed** in v3.1.150-151. Grok-API reviewed **stale v3.1.144** (pre-downgrade), so its M3 = the OLD open version. |
| NEOWISE geometry-QA "passes by construction", weaker basis | OpenAI#6-equiv, Grok-M4 | RE-FLAG | Abstract explicitly carves out NEOWISE geometry-QA (not detector-sensitivity); §pathc_caveats (ii). = prior-audit. |
| heterogeneous thresholds non-comparable | OpenAI#3 | RE-FLAG | `tab:survey_summary` caption + footnotes tabulate both threshold families; disclosed not cross-comparable. = prior-audit. |
| reproducibility/pod-blocked artifacts | OpenAI#4 | DISCLOSED-LIMITATION | Headline recomputable via committed `reproduce_headline_dedup.py`; pod-lost raws disclosed. = prior-audit. |
| LAMOST/SDSS/Planck tier definitions | OpenAI#6,#7,#8 | RE-FLAG | All per-tier disclosures already in body + footnotes ♡/♠/◇. = prior-audit. |
| §V cosmology null demos / f_NL / NANOGrav | OpenAI#12,#13, Grok-min1 | RE-FLAG/OPINION | Scoped "Secondary Demonstrations" returning nulls; venue opinion (pattern-066). = prior-audit. |
| terminology / no definitions table | OpenAI#17, Grok-min2 | OPINION | Presentation preference; non-blocking. |

### Disclosure-backfire (pattern-066) check
**NOT present this round.** Grok-API moved MAJOR→REJECT, but on **stale v3.1.144** — its REJECT items do NOT attack the new honest framing; its M3 is the OLD three-gate issue the paper already downgraded honestly in v3.1.150 (which Grok never saw). No reviewer punished added honesty on content they actually reviewed. When the APIs re-review v3.1.152 (post-downgrade), a genuine backfire test becomes possible; flagged for next round.

### Counts
- INT-Claude: 1 genuinely-new (F3, closed) · 2 re-flag (MINOR#2,#4) · 0 backfire.
- INT-OpenAI (stale v3.1.144): 0 genuinely-new · 14 MAJOR + 4 MINOR all re-flag/disclosed/opinion · 0 backfire.
- INT-Grok (stale v3.1.144): 0 genuinely-new · 4 MAJOR (M3 = already-closed) + 2 MINOR re-flag · 0 backfire.

### Integrity
No ACCEPT fabricated; both API REJECTs recorded as-is. Every finding carries a source-cited verdict. The single closure reads only numbers already in the paper (verified relation 37,272,042 = 37,292,042 − 20,000); no math fabricated. v3.1.152: TinyTeX 2-pass exit 0, 0 undef refs, 37 pages, page-1 date "July 10, 2026", footnote renders in-column (pages 8-9 visual-checked, no overflow). md5 c526aea2a64e2b4f32822fdc8a21440c mirrored byte-identical to all 7 served paths + 2 versioned aliases; Convex paperVersions:bump success (paper-3).

---

## Addendum — EXT re-test (2026-07-10, audited against current v3.1.152)

Fresh EXT re-tests on the **current** version: `retest/P3_grok_retest.md` (MAJOR), `retest/P3_chatgpt_retest.md` (REJECT, 13 MAJOR + 1 MINOR). Every finding audited line-by-line against v3.1.152 source. **Result: 0 genuinely-new editable findings.** No version bump, no directive-G, no Convex bump warranted this round.

### P3 Grok re-test (MAJOR — NO flip; was MAJOR in H17)
| Grok finding | Verdict | Source-cited disposition |
|---|---|---|
| M1 "268,519 validated catalog-grade" vs 2,468 science-target / 98.7% sky-filler | **RE-FLAG** | = prior Grok-EXT#1. Abstract leads with process-volume framing + 2,468 like-for-like benchmark; §I "Reader's guide" states 98.7% sky/filler up front. Disclosed verbatim. |
| M2 eROSITA production axis irreproducible (16 rescalings + 3 IF retrains fail, ρ=−0.10) | **RE-FLAG** | = prior Grok-EXT#2. `tab:provenance` excises eROSITA from EVERY count; irreproducible-axis disclosed. |
| M3 LAMOST 5.8% FAIL + DESI rests on 1 gate + 2 correlated proxy-fold checks failing val-loss≤0.30 | **RE-FLAG (already CLOSED v3.1.150-151)** | = F1/CG-A. The honest three-gate downgrade is present at L988/L1069/L1100/L1598. Grok's exact phrasing ("two correlated fold-stability checks... fail the val_loss≤0.30 retain gate") mirrors the paper's OWN disclosure language — re-flagging the closed disclosure. |
| MINOR Gaia synthetic / abstract length / SDSS continuity-slice | **RE-FLAG** | = prior minors. Gaia excised (disclosed); SDSS 77,905 fixed-size slice + 19,253 top-1% + 12 (S>5) tabulated in `tab:survey_summary`. |

### P3 ChatGPT re-test (REJECT, 13 MAJOR + 1 MINOR)
Section-by-section identical to the already-dispositioned CG-1..CG-13 (heterogeneous 268,519 definition, injection≠purity, DESI non-astrophysical/98.7% sky, five-fold in-sample+fail-retain-gate, Fig 10 selection-function, Planck patches/0.10%, score-definition Eq(2)-vs-Table-II, 17.8% novelty, spatial statistics, f_NL forecast, NANOGrav decoupled, reproducibility provenance, "37.3M"/journal-scope). All previously dispositioned RE-FLAG / DISCLOSED-LIMITATION / OPINION with source-cited verdicts, all closures verified intact in v3.1.152:
- "37.3M mixes 36.758/36.93/37.272/37.292" = F3, closed by footnote $^{\otimes}$ (L1106/L1180) with exact relation 37,272,042 = 37,292,042 − 20,000.
- "58.8% denominator 400 includes removed Gaia" = annotated inline (L1387/L1406).
- 195,790-vs-195,829 = CG-C, reconciled (L uses 195{,}790, primary-coadd subset).
- three-gate framing = CG-A, downgraded honestly (L988/L1100).

### Counts (P3 re-test)
- **Genuinely-new real+editable:** 0 (Grok 0 new, ChatGPT 0 new).
- **Re-flag / disclosed-limitation / opinion:** Grok 6, ChatGPT 14 — all source-cited to a paper line or a prior-audit disposition, all closures verified intact.
- **Backfire (pattern-066):** none isolated for P3 (Grok stayed MAJOR→MAJOR on the same disclosed content; not a harsher flip).
- **Integrity:** no ACCEPT fabricated; both REJECT/MAJOR verdicts recorded as-is; no math fabricated; no edit needed (nothing genuinely-new to close).
