# P3 auto-2026-06-08_1354pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (18039 chars)
**Wall time**: 517.8s

---

# Referee Report — P3: "Spectrally Unusual Sources at Scale"
## Brutal-Honesty Review for Physical Review D

---

## Overview

This is a 20-page catalog/methods paper claiming the "largest-scale" multi-survey autoencoder anomaly search (378,280 unique objects) with two attached cosmological applications (fNL forecast, NANOGrav spectral-index fit). The paper exhibits a fundamental internal tension: it simultaneously trumpets a Path-C rebuild that supposedly resolved cross-transfer artifacts, AND preserves the artifact-driven counts as the headline catalog. Multiple load-bearing scalars in the abstract cannot survive elementary arithmetic checks against the body. Three of six surveys FAIL the authors' own validation gate yet contribute to the headline. The cosmological "applications" produce results consistent with null at <1σ but are framed as positive evidence in the Conclusions.

This is not a PRD paper in its current form. Below are the findings.

---

## ESSENTIAL findings

### P3-E1 — LAMOST headline count contradicts the abstract's "21.5× compression" claim (Page 1 abstract; §III D page 6; Table I row footnote ‡)
The abstract states: *"Path-C rebuild protocol resolves cross-transfer artifacts: 21.5× LAMOST rate compression…"* and explicitly classifies LAMOST as 98% blue-excess training-bias artifact. The §III D body confirms compression is 44,075 → 2,054 at S>5 (= 21.5×).

But the **catalog headline uses LAMOST = 113,342**, an arbitrary top-1% native-percentile slice. That is **2.57× LARGER** than the cross-transfer count of 44,075 the rebuild was supposed to compress, and **55× LARGER** than the native S>5 count of 2,054 to which the "21.5× compression" actually refers. The Path-C unique headline of 378,280 therefore embeds a quantity that contradicts the rebuild's own diagnostic. Either the headline should drop to the S>5 native count (~2,054 LAMOST, headline becomes ~267,000) or the "21.5× compression" language must be retracted. As written, this is incoherent.

**Required fix:** Pick one. The current presentation cannot stand.

### P3-E2 — SDSS native count is post-hoc threshold-matched to the cross-transfer count (§III C page 5; Table I footnote ‡)
The body states: *"the top-77,905 native slice at S ≥ 0.1060 supersedes the cross-transfer count"* — but the cross-transfer count was 77,905. Selecting exactly the same N from a different score axis is threshold engineering. The abstract claims *"∼6500× SDSS rate compression after native retraining"* (consistent with the native S>5 count of 12), but the headline catalog uses 77,905, not 12. The "6500× compression" never propagates to the catalog.

This is the same defect as P3-E1 and is the central methodological problem of the paper. The abstract's compression diagnostic, the body's Path-C narrative, and the headline catalog count are mutually inconsistent.

**Required fix:** Either restate the SDSS contribution as 12 (with honest impact on the 378,280 headline), or remove "6500× compression" framing.

### P3-E3 — Three of six surveys FAIL the injection-recovery gate at 5σ but contribute to the primary catalog (§II D Step 5; §VI D (ii); Figure 7)
LAMOST (5.8%), Gaia (5.2%), eROSITA (1.2%) all fail the ≥50% gate at 5σ. The paper labels these "FAIL-with-diagnostic" using cross-validation stability as a fallback. But the gate is the gate. A "FAIL-with-diagnostic" survey contributing 113,342 + 500 + 298 = ~114,140 objects to a 378,280-object headline means **30% of the primary catalog is built on detectors that failed the validity test**. PRD cannot accept a catalog where the authors' own validation procedure rejects nearly a third of the data.

**Required fix:** Either separate the primary catalog (~264,000, PASS-only) from the exploratory tier and use the PASS-only number as the headline throughout, or justify why gate-FAIL surveys belong in a science-grade catalog at all.

### P3-E4 — "SPHEREx 3–5σ detection of fNL = −35/8 is projected" in Conclusions is not earned by this paper's measurement (§V; §VII page 14, item 5)
The empirical bias measurement is αjk = 0.19 ± 0.65 — consistent with null at 0.29σ. The Fisher-positivity-respecting form gives σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98], a 7.9% improvement explicitly noted as "<1σ significant" and "consistent with no improvement." The 3–5σ SPHEREx detection forecast cited as a "principal result" in the Conclusions is from **Heinrich et al. (2024)** under an ideal forecast that assumes σ(fNL) ≈ 0.7 from bispectrum-only forecasting — it is not a result of this work. Listing it as a "principal result" misrepresents what the paper shows.

**Required fix:** Remove the SPHEREx detection projection from "principal results." State only the central-value forecast and its <1σ significance.

### P3-E5 — Figure 1 title and content contradict the abstract's quarantine of ACT (Figure 1, page 4)
Figure 1 title reads: *"Spatial distribution of all 319,443 anomalies across 8 archives"* with "ACT DR6" in the legend. The caption then states *"ACT DR6 is quarantined and excluded."* This is a direct contradiction within the figure itself. The "319,443" headline number is the cross-transfer baseline that the body explicitly says is *"preserved as a before/after diagnostic only and is not used as a science result"* (Table I caption). Putting this number on the spatial Mollweide as the headline visualization for the catalog is misleading.

**Required fix:** Replot Figure 1 with the 378,280 Path-C catalog (or the 378,080 point-source tier), remove ACT from the legend, update the title.

### P3-E6 — Out-of-distribution catalog applied to uncurated SPARCL flags >50% of spectra (§II B page 3)
The paper admits: *"applying it to a random uncurated SPARCL sweep flags > 50% of spectra (a catalog-curation effect, not a threshold artifact)."* A score threshold that flags >50% of out-of-distribution data as anomalous is not, in any meaningful sense, an anomaly detector. The "anomaly" definition is entirely conditional on the curated DESI training pool. This buries an enormous caveat — the catalog measures "things unlike the DESI training pool," not "things unlike real astrophysical populations."

**Required fix:** This must be elevated from a parenthetical buried in §II B to a prominent caveat in the abstract.

### P3-E7 — "Largest" / "141×" claim is misleading given the LAMOST tier (Page 1 abstract)
The abstract states the catalog is *"∼141× the size of the largest prior single-survey anomaly catalog"* — this uses 378,080 / 2,685. But the authors themselves recommend a *"catalog-grade subset"* of ~265,000 in the very same abstract. So the 141× headline is computed on a number the authors do not actually recommend using. Using 265,000 / 2,685 = 99×, not 141×.

**Required fix:** Use the catalog-grade subset in the headline comparison, or restate as "141× including exploratory tier."

### P3-E8 — "(Dated: June 2026)" — future date (Page 1 header)
A paper dated in the future is unprofessional for a PRD submission. The header should reflect the actual submission date.

---

## MAJOR findings

### P3-M1 — NANOGrav analysis double-counts the GW background discovery (§V A, Page 12)
Fitting a power-law to the NANOGrav 15-yr KDE free-spectrum and computing parameter-space shifts against γ=3.0 and γ=4.33 is illustrative at best. The NANOGrav collaboration's own analysis includes red noise marginalization, deterministic models, and a hierarchical likelihood that this template fit cannot replicate. The Savage-Dickey BMB/SMBHB = 7.1×10³ "decisive" label is misleading because the Bayes factor is computed against a flat γ prior with no astrophysical normalization, not against NANOGrav's published model comparisons. The authors do hedge ("neither constitutes a detection"), but the "decisive on Jeffreys' scale" labeling in the abstract pulls the other direction.

**Required fix:** Either remove the Bayes factor framing entirely or contextualize it against NANOGrav15's published model comparison numbers.

### P3-M2 — Cosmology applications do not belong in a catalog paper at this depth (§V, §V A)
The fNL forecast (§V) and NANOGrav fit (§V A) consume ~2 pages and inflate the paper's scope. Both produce null/marginal results. Both depend critically on auxiliary inputs (Heinrich et al. Fisher; NANOGrav 15-yr KDE product). The paper would be stronger restricted to the catalog plus one short cosmological motivation section. As is, the cosmology sections invite skepticism that distracts from the catalog itself.

**Recommendation:** Move cosmology to a separate paper or condense to one paragraph each.

### P3-M3 — "Catalog-grade subset" naming is inconsistent (§abstract, §VII Conclusions)
The abstract recommends a ~265,000-object subset but the Conclusions section continues to use 378,280 as the headline. The Conclusions section item 1 prominently states "378,280 unique anomalies" without mentioning that the authors' own recommended catalog-grade subset is ~70% of that.

**Required fix:** Use the recommended catalog-grade subset (~265,000) as the headline throughout Conclusions, with 378,280 as a footnote.

### P3-M4 — Figure 9 panel labels read "AE=83518", "AE=17663", etc., not anomaly scores S as defined (Page 17, Figure 9)
The figure caption claims border color = taxonomy class. Panel labels show "AE = 5731", "AE = 9240", "AE = 83518" etc. These are not the canonical S scores defined in Eq. (2) — they look like raw MSE values × 10⁵ or similar. Earlier the paper admits *"printed as 'AE' for legacy compatibility"* in §III B but never reconciles AE numerics with the S scale used everywhere else. A reader cannot map an "AE = 83518" panel to "S = ?". This breaks the paper's promise that S is the universal scale.

**Required fix:** Convert panel labels to canonical S, or display both with explicit mapping.

### P3-M5 — DESI 5σ "+4.61σ SMBHB disfavor" framing implies positive evidence, not null (§V A; abstract)
The paper writes "SMBHB γ=4.33 at +4.61σ" as if it were evidence against SMBHB. But this is purely a parameter-shift on a hand-fit power-law to a marginalized product. NANOGrav15 itself reports the data are *consistent with* SMBHB to within their model comparison. A +4.61σ "disfavor" computed by a different procedure is not comparable to NANOGrav's actual model comparison and should not be cited as a tension with SMBHB.

**Required fix:** Either explicitly state that this +4.61σ is not equivalent to NANOGrav's model comparison framework, or remove.

### P3-M6 — Sigma values from different null procedures juxtaposed without "not directly comparable" qualification
The paper repeatedly juxtaposes:
- Genuine novelty fraction 17.8% from CDS X-Match (a single-sample point estimate at top-1000)
- SIMBAD-unmatched 58.8% (database coverage, not novelty)
- Injection-recovery 5σ recovery percentages (gate-defined statistical thresholds)
- NANOGrav +1.13σ and +4.61σ (parameter shifts on KDE marginal)
- αjk 0.29σ (jackknife consistency with null)

These are five different σ definitions. The paper has caveats individually but not at every juxtaposition. The abstract presents them as if they were a coherent significance summary.

**Required fix:** Add explicit "not directly comparable" qualification at every juxtaposition.

### P3-M7 — Per-survey native architecture for SDSS, LAMOST not specified in main text (§II A page 2)
The paper says architecture is "adapted per survey" but only specifies the spectroscopic family generically. The CMB native convolutional autoencoder is fully described, but the SDSS and LAMOST native models — which are critical to the rebuild — are only described as "fresh BigAE." Do they share architecture with the DESI BigAE? Different latent dim? Different hyperparameters? The paper defers to "companion data repository" for architecture diagrams. For a PRD methods paper, the architecture must be in-paper.

**Required fix:** State explicitly that SDSS native, LAMOST native are identical architecturally to the DESI BigAE (if true), or specify differences.

### P3-M8 — Single-tracer DESI QSO baseline σ(fNL) = 8.98 vs σ(fNL)^std = 8.43 in Table VII (§V; Appendix C Table VII)
Section V says σ(fNL)^std = 8.98 is the single-tracer DESI QSO baseline. Table VII row at α=0.15 gives σ(fNL) = 8.43 (6.1% improvement). But the abstract gives σ(fNL) = 8.14 with [3.92, 8.98] envelope and σ(fNL)^std = 8.98. So the baseline appears twice (8.98 in abstract, 8.98 in §V text) and Table VII's α=0 row is missing. Table VII rows at α = 0.05, 0.10, 0.15 are presented as if they were the same as the αjk = 0.19 ± 0.65 forecast, but they are computed under the linear approximation that the paper itself disclaims at §VI D (i): "the local-linear propagation σ(fNL) ≈ 8.98 − 3.66α fails inside the 1σ interval α ∈ [−0.46, +0.84]." Table VII therefore uses a propagation rule the paper acknowledges is wrong.

**Required fix:** Recompute Table VII under the Fisher-positivity-respecting quadratic form. Add the α=0 baseline row.

### P3-M9 — Equation E1: spectral template missing units check (Appendix E page 15)
Eq (E1): log10 ρi = ½[2 log10 A − log10(12π²) + (γ−3) log10 f_yr − γ log10 f_i − log10 T_obs]. The 2 log10 A normalizes correctly inside the bracket only if ρ is already in s², but T_obs and f are mixed time/frequency. Without explicit units for ρ, A, f_i, T_obs this equation is unverifiable. Most PTA template papers express this as power-spectral density in units of s³ or HD-correlated cross-power.

**Required fix:** State units explicitly.

### P3-M10 — Reference [33] mislabeling acknowledged but uncorrected (Page 19)
The bibliography entry for Heinrich et al. literally states "*bibkey label retained as Heinrich2023 for arXiv-submission-year continuity*" — this is internal versioning prose that has leaked into the published bibliography. A PRD bibliography should not contain references to its own bibkey choices.

**Required fix:** Remove the bibkey-retention prose. Just cite cleanly.

---

## MINOR findings

### P3-m1 — SDSS DR18 "anomaly rate 3.38%" vs DESI 0.87% comparison is meaningless (§III C, §VI B)
The paper acknowledges this in §VI B but still juxtaposes the rates in Table I as if comparable. The 3.38% number is explicitly a cross-transfer artifact — yet appears as the headline SDSS rate in Table I.

### P3-m2 — "Spectra/s" throughput figures for native models in Table V are post-hoc estimates (Page 16)
Footnote acknowledges that throughput figures are for "H200 inference on the final native-retrained checkpoints" but training was on A100. Inconsistent hardware reporting.

### P3-m3 — "73× like-for-like increase" is not like-for-like (Page 1 abstract)
Liang et al. used a normalizing flow autoencoder with a different threshold methodology on DESI EDR. This work uses a deterministic autoencoder with absolute MSE-anchored threshold on DESI DR1. Calling this "like-for-like" is wrong.

### P3-m4 — Trustworthiness 0.9797 ± 5×10⁻⁵ stability claim (Appendix D page 15)
A trustworthiness of 0.98 with σ = 5×10⁻⁵ across 20 seeds is suspiciously stable for a stochastic embedding. The "kNN-preservation and cross-seed Spearman FAIL" caveat partly disclaims this but the main claim is presented in body as if validated.

### P3-m5 — UMAP "3 latent-space populations" (Page 5) vs "14 clusters" (Figure 3 title) (§III C; Figure 3)
Body text says "3 latent-space populations" but Figure 3 title reads "77,905 anomalies (score > 5.0), 14 clusters, 99.4% clustered." Either 3 or 14 — the text and figure must agree.

### P3-m6 — "Single author" Independent Researcher (Page 1 affiliation)
A 20-page PRD-targeted multi-survey catalog paper with single author independent researcher affiliation is unusual. Acknowledgments section lacks any collaboration credit despite using DESI, SDSS, eROSITA, etc. proprietary archives. This is allowable but PRD will scrutinize.

### P3-m7 — "Data availability: private pending arXiv acceptance" (Page 14)
The catalog is on HuggingFace but locked. Reviewers cannot verify catalog contents. PRD will require open data before acceptance.

### P3-m8 — Heinrich et al. citation arXiv:2311.13082 should be checked for σ(fNL) ≈ 0.7 claim
The 3-5σ SPHEREx detection significance "uncertainty range reflects systematic degradation budget" is a non-trivial extrapolation. The cited paper's σ(fNL) ≈ 0.7 needs verification.

### P3-m9 — TIC 374313355 "score = 49.5" claim (§IV C; Figure 6)
A score of 49.5 is roughly 10× the catalog threshold S>5. Is this score on the canonical S scale? The figure caption says "SDSS anomaly score = 49.5" but the SDSS native catalog is top-percentile (S ≥ 0.1060). The number 49.5 cannot be on the same scale. Likely the cross-transfer score is shown. Caption is misleading.

### P3-m10 — "Score = 11.5" NEOWISE top anomaly (Figure 4 page 8)
Same issue — what score scale? NEOWISE uses top-1% selection so what does 11.5 mean? Need explicit unit/scale.

### P3-m11 — eROSITA cross-validation "81.5%" inconsistency (Table I footnote § page 7; §III E page 6; §VI D)
Footnote § states "81.5% (7582/9303)" recovers the top-1% reference, but 7582/9303 = 81.5%. The 298-source published headline (S > 0.259) has 284/298 = 95.3% overlap with the IF top-9303. The arithmetic is consistent but the relationship between three different eROSITA selection layers (298 / 9303 / 930,203) is poorly motivated and reads as post-hoc.

---

## NITS

### P3-n1 — "(Dated: June 2026)" — future date already covered in E8 but should be globally fixed.

### P3-n2 — Footnote markers ♡, ♠, ¶, †, ‡, §, ∥, ⋆ all in Table I caption is symbol soup. Convert to numbered footnotes.

### P3-n3 — Inconsistent capitalization: "BigAE" vs "BIGAE" appears mixed.

### P3-n4 — "Path-C" jargon is internal. Explain on first use as "native-retraining protocol with 6-step validation."

### P3-n5 — Section §VI D (ii), (iii)... numbering exists but only (i), (ii) shown — where are (iii)–(j) in main text? They appear in Table IV but not consistently referenced.

### P3-n6 — Page count: 20 pages for a catalog paper with significant methodology issues and tangential cosmology is excessive. Recommended max: 12 pages.

---

## Summary recommendation

**REJECT**

The paper has a genuine empirical contribution (37M sources scanned, large autoencoder catalog), but the presentation is internally incoherent on its central claims. The "Path-C rebuild" compression diagnostics are showcased prominently in the abstract while the catalog headline preserves the very counts the rebuild was supposed to compress (LAMOST 113,342 is 2.57× LARGER than the cross-transfer baseline the abstract says was "21.5× compressed"; SDSS 77,905 is exactly equal to the cross-transfer count even though native S>5 gives 12). Three of six surveys FAIL the authors' own validation gate yet contribute ~30% of the catalog. Figure 1 contradicts the abstract on quarantine. The Conclusions list a SPHEREx 3-5σ detection projection that is not earned by this paper's measurement (which is consistent with null at <1σ). The NANOGrav "+4.61σ disfavor" of SMBHB is computed by a different procedure than NANOGrav's own model comparison and should not be presented as a tension. The paper requires structural reconceptualization — decide which catalog you are publishing, retract claims not earned by the measurements, separate cosmology applications into a dedicated paper, and resolve the Figure 1/Table I/abstract inconsistencies — before resubmission. None of these issues is cosmetic.

---

## PASS 2 — self-critique findings (what initial review missed)

# P3 — Second-Pass Review (Fresh Eyes)

I went back through this paper with the audit categories you specified. My initial review caught the structural defects but missed several arithmetic inconsistencies and stale-number issues. Here are the new findings.

---

## NEW ESSENTIAL findings

### P3-E9 — The "7.9% improvement" headline is arithmetically incompatible with σ(fNL) = 8.14 (Abstract; §V; §VII Conclusions item 5)

The abstract states: *"central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement consistent with no improvement at <1σ; σ(fNL)^std = 8.98 single-tracer baseline)"*.

Direct arithmetic: (8.98 − 8.14)/8.98 = **9.35%**, not 7.9%.

I checked alternative computations to find 7.9%:
- σ² space: (1 − 8.14²/8.98²) = 17.8% — no.
- Linear scaling at α=0.19: σ = 8.98 − 3.66×0.19 = 8.285. (8.98 − 8.285)/8.98 = **7.74% ≈ 7.9%** ✓

So the **7.9% improvement is computed under linear scaling** (the form §VI D (i) explicitly says "fails inside the 1σ interval"), while **σ(fNL) = 8.14 is computed under the quadratic Fisher-positivity-respecting form**. The two are inconsistent calculations from different formulas, presented together as if mutually derivable. The headline improvement number does not correspond to the headline σ value. This propagates through the abstract, §V, and the Conclusions.

**Required fix:** Either restate as 9.4% (matching σ=8.14) or restate σ as 8.28 (matching 7.9%). Pick one consistent calculation throughout.

### P3-E10 — Figure 8 Fisher baselines (11.71, 12.72) are incompatible with §V's σ(fNL)^std = 8.98 (Appendix C, page 15)

Figure 8 caption: *"Multi-tracer Fisher σ(fNL) vs. tracer number density n̄ for the canonical 5-tracer configuration of §V. The dashed gray line marks the dense-tracer limit (σ(fNL) = 11.71); the dotted dark-red line marks the single-tracer baseline (σ(fNL) = 16.85)."*

The Fig 8 text reports four σ(fNL) values:
- Ideal (dense limit) = **11.71**
- Baseline multi-tracer = **12.72**
- Single-tracer baseline = **16.85** (dotted line)
- Penalty range 12.56–13.35

None of these match §V's headline:
- §V single-tracer baseline = **8.98**
- §V multi-tracer central = **8.14**

Figure 8 claims to be the "canonical 5-tracer configuration of §V" but uses a completely different Fisher with baselines roughly **2× larger**. The paper provides no reconciliation — these are simply two different Fisher analyses presented as if they were one.

The "+1.27% over baseline-multi 12.72" and "+7.93% ideal-multi figure" framing in Appendix C use the 11.71/12.72 numbers, while §V's headline "7.9% improvement" uses the 8.98 baseline. The "+7.93%" in Fig 8 caption coincidentally matches 7.9% in §V — but they are computed from different baselines (12.72→11.71 vs 8.98→8.14) and should not match.

**Required fix:** Reconcile. Either Fig 8 is from a different analysis (state explicitly and label distinctly) or its baselines must be corrected to match §V's 8.98/8.14.

### P3-E11 — §VI D caveats (iii), (iv), (v) referenced but never enumerated (§VI D; Table I footnote §; §VI D (ii); Table IV)

The text body of §VI D enumerates only:
- (i) DESI in-sample training–test overlap
- (ii) Injection-recovery synthesis

But other parts of the paper reference:
- "§VI D caveat (v)" — Table I footnote § (twice), and Page 13 "(Gaia 41% stability, eROSITA 81.5%; §VI D (v))"
- "§VI D (iv)" — Figure 7 caption: "(see caveat (iv))"
- "§VI D (f)" — Page 7 Table I footnote § text: "Empirical intersection (§VI D (f))"
- "§VI D (e)" — Page 11 §V c systematics: "(plane-parallel monopole, sub-% of b; §VI D (e))"
- "§VI D (j)" — Page 11 §V: "(§VI D caveat (j))"

The footnote (j) and (f) and (e) presumably refer to Table IV rows (a)–(j). But (iii), (iv), (v) (apparently lowercase roman numerals continuing from (i), (ii) in §VI D body) are referenced and **do not exist anywhere in the paper**.

This is a broken cross-reference web — either Table IV row letters were meant to be cited consistently throughout (in which case "(v)" should be "(e)" or similar), or §VI D body should enumerate (iii)–(v). Either way the reader cannot find content that is repeatedly cited.

**Required fix:** Reconcile the numbering schemes. Every footnote in Table I and every parenthetical in the body must map to an existing item.

### P3-E12 — "OOD control-vs-control 0.874 (PASS)" in Conclusions has no body provenance (§VII Conclusions item 6, page 14)

Conclusions item 6: *"DESI 5-fold Jaccard stability J̄ = 0.862 (PASS); OOD control-vs-control 0.874 (PASS)."*

The 0.862 matches §II B and §VI D (i). But **0.874 appears nowhere else in the paper**. The §II B Out-of-Distribution validation reports *"production-vs-5-seed-control is J̄_prod×ctrl = 0.732 (gate ≥ 0.50, PASS)"*. The Conclusions value 0.874 is neither 0.862 nor 0.732 — it's a new number with no derivation.

**Required fix:** Either remove 0.874, replace with 0.732 (the actually-reported OOD value), or add the source of 0.874 to §II B / §VI D.

---

## NEW MAJOR findings

### P3-M11 — Figure 2 and Figure 3 legends use cross-transfer counts that the abstract claims were "compressed" (Figures 2, 3, pages 5–6)

Figure 2 left legend: *"LAMOST DR10 (44,075)"*. But the abstract claims the rebuild produced 21.5× compression and the catalog headline uses LAMOST = 113,342 (per P3-E1). Figure 2 thus displays the pre-rebuild count.

Figure 3 title: *"SDSS DR18 Spectral Anomalies — UMAP+HDBSCAN ... 77,905 anomalies (score > 5.0), 14 clusters"*. But the abstract claims 6500× compression to the native-retrained tier. Figure 3 displays the pre-rebuild count.

Both figures are described in §III text as the cross-transfer baseline preserved as "before/after diagnostic." But this is not stated in the figure captions themselves, and the figures are presented as the SDSS/LAMOST anomaly visualizations of the paper. Casual readers will read the figures as the catalog's headline anomaly populations.

**Required fix:** Either add prominent "PRE-REBUILD" markers to the figure titles, or replot with the native-retrained anomaly sets.

### P3-M12 — "14 clusters" in Figure 3 title vs "3 populations" in §III C body (Figure 3 title; §III C page 5)

§III C body: *"UMAP/HDBSCAN clustering of the top-50,000 cross-transfer anomalies yields 3 latent-space populations (Fig. 3), dominated by cool dwarfs (84%)."*

Figure 3 title shows: *"77,905 anomalies (score > 5.0), 14 clusters, 99.4% clustered."*

3 vs 14 clusters is irreconcilable. Either HDBSCAN found 14 clusters that get aggregated into 3 populations (in which case body should say "14 clusters grouping into 3 physical populations") or these are different runs with different parameters.

**Required fix:** Specify the cluster→population aggregation rule.

### P3-M13 — "5,384 QSO-candidate sample" undefined in main text (§V page 10)

§V states: *"A Landy–Szalay angular two-point analysis on the full 5,384 QSO-candidate sample"*. This number 5,384 appears nowhere else. The 195,829 DESI anomaly catalog includes only 0.037% QSO-class objects (per §III A), giving ≈ 73 QSOs in the published catalog, not 5,384. So either:
- 5,384 is a separate QSO-candidate selection layer not described, or
- It includes broader categories (high-z candidates, AGN), or
- It comes from a different cut entirely.

Without explicit definition, the central cosmology measurement (αjk = 0.19 ± 0.65) is not reproducible.

**Required fix:** Define how 5,384 QSO candidates are selected from the 195,829 anomaly catalog.

### P3-M14 — "Gold+Silver subset" of 1,122 objects undefined (§V page 11; Figure 8 page 15)

§V references *"the 1,122-object Gold+Silver subset"* and Figure 8 shows tracer densities for "anomaly_gold" and "anomaly_silver". These categories appear nowhere in the catalog construction (§III A–H), the Path-C rebuild (§II D), or any earlier section. They are presented as if defined but are not.

**Required fix:** Define Gold/Silver tier criteria explicitly. Without this, the σ(fNL)^GS = 1.95 result (substantial improvement over 8.98 baseline) is non-reproducible.

### P3-M15 — DESI wavelength band edges stated in §II B do not match standard DESI arm boundaries (§II B page 2)

The paper defines: *"blue (3600–6200 Å), red (6200–8200 Å), and near-infrared (8200–9800 Å) subsets"*. Standard DESI arm boundaries are approximately B (3600–5930), R (5660–7720), Z (7470–9824), with overlap regions. The paper's stated edges (3600/6200/8200/9800) place band breaks where DESI does not have them and ignore the actual arm overlaps. The B-dominant vs R-dominant vs Z-dominant classification (Table VI) depends critically on which band a given pixel is assigned to.

**Required fix:** Either state these are author-defined nominal band-binning windows (not actual DESI arm boundaries) or correct to the real boundaries.

### P3-M16 — Anomaly score scales mixed across figures without conversion (Figures 4, 6, 9; §III)

- Figure 4: NEOWISE top anomaly "score = 11.5"
- Figure 6 panel (d): TIC 374313355 "score = 49.5"
- Figure 9 panel labels: "AE = 83518", "AE = 17663", "AE = 9240", etc.

Per §II B, the canonical S score is z-scored MSE residual normalized by validation σ_val. The DESI catalog headline runs 5.0 to 25.2 (Figure 2).

So:
- NEOWISE "score = 11.5" — what scale? NEOWISE uses top-1% selection, not absolute S. Is 11.5 a NEOWISE-native S? Not stated.
- SDSS "score = 49.5" — SDSS native runs to S = 0.1060 at top-1% (per §III C). 49.5 is the cross-transfer score (Fig 2 right shows SDSS cross-transfer extending to 10¹¹). But Figure 6 doesn't label this as cross-transfer.
- Figure 9 "AE = 83518" — admitted as "legacy" in §III B but no S mapping shown.

The promise of §II B is that S is the canonical universal scale; the figures violate this promise repeatedly.

**Required fix:** Convert all figure score labels to canonical S, or print both with explicit mapping rule.

### P3-M17 — Figure 8 vertical lines labeled "P3 anomaly_gold" and "P3 anomaly_silver" (Figure 8 page 15)

"P3" is presumably "Path-3" or perhaps the paper's internal version label. This internal-development jargon should not leak into a published figure. (Combined with P3-n4 from the initial review on "Path-C" jargon.)

**Required fix:** Replace "P3" with descriptive labels.

### P3-M18 — eROSITA selection layers not reconciled in body (§III E; Table I footnote §; Table III)

Three eROSITA selection counts coexist:
- 298 = canonical S > 0.259 catalog headline (top 0.03%)
- 9,303 = IF top-1% reference set
- 930,203 = full DR1 input

Body text says *"284 of 298 canonical-S top-298 sources (95.3%) are also in the IsolationForest top-9,303"*. Reasonable.

But Table III displays the top-5 sources with BOTH columns S_BigAE (1.084, 0.815, etc.) AND S_IF,raw (34,182; 16,270; etc.). The S_IF,raw scale (10³–10⁴ range) does not correspond to a top-1% cut that would yield 9,303 objects from a 930,203 sample — that would require a percentile cut, not an absolute IF score. So how is 9,303 derived from IF scores ranging 0–35,000?

**Required fix:** Specify whether 9,303 is a top-1% rank cut or an absolute score cut on S_IF,raw, and which IF score corresponds to the boundary.

---

## NEW MINOR findings

### P3-m12 — Spearman ρ = −0.03, p = 0.12 with N=2670 implausibility check (§III A page 4)

For Spearman with N = 2,670, the standard error on ρ is ≈ 1/√(N−1) = 0.0194. So ρ = −0.03 is at z = −1.55, two-sided p ≈ 0.121. **Consistent** with the stated p = 0.12. ✓ OK — this one passes the audit but I report the check for completeness.

### P3-m13 — Anomaly z-distribution: anomalies peak at z ~ 0.75 vs normal at z ~ 0.93 (§III A page 4)

If anomalies are dominated by high-z Gunn–Peterson absorption (per the §III B QSO candidates), why would the anomaly redshift distribution peak at LOWER z than normal spectra? This appears physically inverted. Probably the "z ~ 0.75 peak" includes the bulk of multi-band anomalies (galaxies), and the high-z tail of QSO candidates is a small overlay. Worth a clarifying sentence.

### P3-m14 — "120,000 parameters (photometric)" vs Table V "70K-120K" inconsistency (§II A vs Table V)

§II A: *"Total parameter count: ∼120,000 (photometric) to 660,000 (spectroscopic)"*. Table V: NEOWISE 70K, Gaia 80K, eROSITA 120K, BigAE spectroscopic 660K. So photometric range is 70K–120K, not "∼120,000". Minor inconsistency.

### P3-m15 — Table I caption "ACT contributes zero" and "subtracts exactly 200" arithmetic (Table I caption, footnote ∥)

*"ACT's 200 patches contributed zero positional overlaps with the other seven surveys (the Planck×ACT null cross-correlation, §IV D, confirms this), so excluding ACT subtracts exactly 200 from both the input sum and the unique-object count."*

The cross-transfer baseline of 319,443 includes ACT's 200, so 319,443 − 200 = 319,243. But the cross-transfer baseline 319,443 vs Path-C unique 378,280 differs by +58,837, dominated by the LAMOST native re-score (+69,267), Planck native re-score (already in cross-transfer), NEOWISE mask (−17), and dedup (−10,213). Let me verify:

195,829 + 77,905 + 113,342 + 298 + 200 + 500 + 419 = 388,493 (Path-C native sum, no ACT)
388,493 − 10,213 dedup = 378,280 ✓

Cross-transfer sum (with ACT): 319,443
Cross-transfer without ACT: 319,243

The shift from 319,243 to 388,493 is dominated by LAMOST going 44,075 → 113,342 (+69,267). 319,243 + 69,267 = 388,510, off by 17 (the NEOWISE mask 436→419 = -17). 388,510 - 17 = 388,493. ✓

OK arithmetic checks. Minor finding withdrawn.

### P3-m16 — Trustworthiness 0.9797 ± 5×10⁻⁵ implausibly low variance (Appendix D page 15)

A UMAP trustworthiness of 0.98 with σ = 5×10⁻⁵ across 20 random seeds implies standard error 1×10⁻⁵. That is extraordinarily tight for a stochastic embedding optimization. Either the seeds aren't actually independent, or the variance estimate is wrong. The "kNN-preservation and cross-seed Spearman FAIL" hedge in the same paragraph suggests the embeddings actually do differ substantially between seeds, contradicting the σ = 5×10⁻⁵ stability claim. (Repeats P3-m4 from initial review with quantitative reasoning.)

### P3-m17 — Page 5 stratification by DESI TARGETTYPE: 22.5M total but only 6.5M with TARGETTYPE classification (§III A page 4)

*"Across the 6.5 million spectra in DESI DR1 that carry a validated TARGETTYPE classification ... the remaining ∼16 million spectra are unclassified filler targets, sky fibers, or calibration exposures excluded from this per-class breakdown."*

If 16M of 22.5M are sky fibers/calibration/filler, that's 71% unclassified. Sky and calibration are clearly non-scientific. So the headline "22.5M scanned" includes many target categories where "anomaly" is meaningless or where sky-background reconstruction is what's being measured. The 0.87% anomaly rate on 22.5M is partially diluted by these. Worth a more prominent caveat.

### P3-m18 — Bibliography duplication: refs [13] Wands and [14] Cai both cited for fNL = −35/8

Page 10 §V: *"The matter-bounce prediction fNL = −35/8 = −4.375 [13, 14, 35]"*. Reference [13] is Wands 2010 on "Local non-Gaussianity from inflation" — this is a general fNL review for inflation, not specifically matter-bounce. The −35/8 prediction is from Cai et al. [14] and Wilson-Ewing [35]. Citing [13] for this number is wrong.

---

## NEW NITS

### P3-n7 — Fig 7 footnote: "*FAIL-with-diagnostic: gate not cleared but companion XV metric confirms detector stability (eROSITA 81.5%, Gaia 41%, LAMOST 9.7× cont./em.)"

"9.7× cont./em." conflates a ratio (continuum/emission improvement) with an XV stability metric. The other two are stability percentages. Misleading parallel structure.

### P3-n8 — Page 13: "Six injection-recovery gates: 3 PASS ... and 3 FAIL-with-diagnostic"

Six surveys do injection-recovery in Fig 7: SDSS (cont. + em.), LAMOST (cont. + em.), Planck native, NEOWISE mask, eROSITA, Gaia. That's 6 distinct surveys but 8 injection-recovery curves shown in Fig 7. The "6 gates" framing is approximate.

### P3-n9 — §V c "δb is broken by the multi-tracer technique" — undefined δb

"δb" presumably means bias-parameter uncertainty. Not defined on first use.

### P3-n10 — Page 11 §V: "general-relativistic projection corrections (O(H²/k²))"

Should be 𝓗²/k² (conformal Hubble), not H²/k². Standard notation in cited Bonvin & Durrer, Challinor & Lewis.

### P3-n11 — Table III "Top 5 eROSITA anomalies with SIMBAD novelty status" — all 5 labeled "Novel"

If all 5 are novel, the "SIMBAD" column adds no information. Either include some non-novel comparison or drop the column.

---

## Summary of second-pass findings

| Class | Count |
|-------|-------|
| Essential | 4 (E9–E12) |
| Major | 8 (M11–M18) |
| Minor | 7 (m12–m18) |
| Nit | 5 (n7–n11) |

**The dominant new issue is arithmetic incoherence in the cosmology section.** The 7.9% improvement vs σ=8.14 inconsistency (E9) and the Fig 8 / §V baseline mismatch (E10) together mean that the cosmology forecast — already weakened by the αjk = 0.19 ± 0.65 null — is computed by **at least two different Fisher recipes that are not reconciled**, with the headline number computed by a recipe (linear scaling) that the paper itself disclaims as invalid inside the relevant α interval. This reinforces my initial recommendation to remove or substantially scope down the cosmology applications.

**The §VI D caveat-numbering breakdown (E11)** and **the 0.874 stale number (E12)** suggest the paper went through significant revision late in production without consistent re-checking of cross-references. The Fig 2/3 cross-transfer-count legends (M11) and the Fig 3 cluster-count mismatch (M12) are similar evidence of partial rewrites that didn't propagate.

**Combined with the initial review's findings (P3-E1 through P3-M10):** the original rejection recommendation stands and strengthens. The paper requires a unified internal recomputation pass before resubmission — every number in the abstract, every figure label, every Fisher baseline, every caveat reference must be re-verified to derive from the same calculation chain.