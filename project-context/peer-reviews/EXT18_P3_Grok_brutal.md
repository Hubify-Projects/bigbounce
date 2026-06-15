# P3 EXT18 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_2025/bigbounce/pipelines/p3_anomaly_engine/paper3_draft.pdf` md5=4a8c1172 pages=30
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (2570 chars)
**Wall time**: 121.0s

---

**Referee Report for P3 (Physical Review D)**

**P3-E1 (ESSENTIAL)** — Page 1 (abstract), line ~15: "a Native-Trained Novelty Fraction from 37.3 Million Sources". The body (Table I, p. 9) shows the Path-C unique headline is 378,280 objects drawn from 37,272,042 processed sources after all cuts. The abstract figure is not recomputed from the displayed inputs and mixes the cross-transfer baseline (37.29 M) with the final deduplicated Path-C total. Required fix: replace with the exact traceable number or add an explicit footnote.

**P3-E2 (ESSENTIAL)** — Page 1, "Dated: June 13, 2026". A future date appears in the rendered PDF. This is internal versioning language that must be removed.

**P3-E3 (ESSENTIAL)** — Page 1 (abstract) and §V (p. 17–18): the multi-tracer \(\sigma(f_{NL})\) improvement is quoted as 6.1 % (8.14 vs 8.98) with the claim that it is "consistent with no improvement at \(0.29\sigma\)". The paper never states the effect size (fractional amplitude of the improvement relative to the single-tracer baseline) at every juxtaposition of the two numbers. The two \(\sigma(f_{NL})\) values are derived from different null procedures (fixed-\(\alpha\) vs empirical \(\alpha_{jk}\)) and are not directly comparable without the explicit qualifier required by instruction 7.

**P3-E4 (ESSENTIAL)** — Page 6, Table I footnote ¶ and p. 9: the 378,280 headline count is obtained only after a 7-way 5″ deduplication whose reproducibility script is referenced but not supplied in the manifest. The standalone-reader test fails: the argument is not self-contained.

**P3-M1 (MAJOR)** — Page 1 and §III D (p. 5): 98 % of the LAMOST cross-transfer anomalies are flagged as a "training-bias artifact". The paper retains the LAMOST tier as "exploratory" yet still includes its objects in the headline 378 k count. This is a material contamination that must be removed from the primary catalog or the catalog must be explicitly stratified.

**P3-M2 (MAJOR)** — Page 18, Fig. 9 and §V B: the NANOGrav \(\gamma = 2.567 \pm 0.382\) is presented as "marginally consistent" with the matter-bounce prediction \(\gamma = 3.0\). The Savage-Dickey factor \(B_{MB/SMBHB} = 7.14 \times 10^3\) is prior-dependent and the paper does not show the result under the flat prior used for the headline claim. Effect-size statement missing.

**P3-M3 (MAJOR)** — Page 30 (Table VI) and §II B: training times and throughputs are given, but the exact commit hash of the production `bigbounce` weights used for the released catalog is not frozen. Provenance surface audit fails.

**P3-M4 (MAJOR)** — Page 3, Fig. 1 and §III A: the UMAP embedding is colored by anomaly score, yet the 83 "Exemplar-Set" objects are force-included. This violates the claim that the representation is unsupervised. The figure caption does not disclose the contamination.

**P3-N1 (MINOR)** — Throughout: repeated use of internal project nomenclature ("Path-C", "BigAE", "production recipe") without a one-sentence definition on first use in the main text.

**P3-N2 (MINOR)** — Page 9, Table I: the SIMBAD-unmatched column mixes two different radii (5″ for most surveys, 3″ for the pooled run). Units and selection functions are not uniform.

**P3-N3 (NIT)** — Page 1: "largest-scale application … of which we are aware" is a hedge that should be replaced by a quantitative comparison to Liang et al. (2023) and Baron & Poznanski (2017) with explicit source counts.

**Summary recommendation**  
**MAJOR REVISIONS**

The manuscript presents an ambitious multi-survey anomaly catalog whose scale is genuinely new. However, the paper contains multiple load-bearing quantitative claims in the abstract and cosmological sections that cannot be recomputed from the displayed numbers, an internal future date, an incompletely documented deduplication step, and a training-bias artifact that contaminates the headline sample. The Fisher-forecast improvement is presented without the required effect-size qualifier at every juxtaposition. These are not cosmetic issues; they prevent a reader from verifying the central results. A revised version that (i) removes or stratifies the LAMOST tier, (ii) freezes all production weights and scripts with DOIs, (iii) supplies the exact recomputed abstract scalars, and (iv) adds the missing effect-size statements could be reconsidered, but the current version does not meet PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

**P3-E5 (ESSENTIAL)** — Page 2, §I: “The point-source tier is ~141× the size of the prior single-survey anomaly catalog [11]”. The arithmetic 378 280 / 2 685 ≈ 141 uses the *full* Path-C headline (including the 200 Planck patches). The immediately following sentence correctly states the point-source-only subset is ~73× (195 829 / 2 685). The 141× claim therefore mixes incompatible populations; the multiplier is not reproducible from the point-source benchmark cited.

**P3-E6 (ESSENTIAL)** — Page 9, Table I, final Path-C row: the headline 378 280 is stated to be the deduplicated total after the 7-way 5″ FoF step, yet the table supplies neither the pre-deduplication object count nor the exact number of intra-survey collisions removed. The arithmetic that produces 378 280 from the per-survey native-retrain columns cannot be verified from the displayed numbers.

**P3-M5 (MAJOR)** — Page 18, §V B and Fig. 9 caption: the multi-tracer central value 8.14 is obtained with the *empirical* \(\alpha_{jk}=0.19\) while the single-tracer baseline 8.98 is the fixed-\(\alpha=0\) result. The two numbers are therefore generated under different null procedures; the paper never states that they are “not directly comparable” at the location where the 6.1 % improvement is first quoted.

**P3-M6 (MAJOR)** — Page 3, Fig. 1 caption vs. §II B: the caption asserts the embedding is produced by an “unsupervised representation,” yet the same caption states that the 83 Exemplar-Set objects “are force-included in the embedding.” The body text never reconciles the contradiction between the unsupervised claim and the supervised contamination of the displayed map.

**P3-N4 (MINOR)** — Page 6, Table I footnote † and §III F: the Planck native-retrain count is given as 200 after the \(|b_{\rm ecl}|<80^\circ\) mask, but the cross-transfer baseline row lists 200 *before* any mask. The two 200s are therefore not the same quantity; the table does not flag the distinction.

**P3-N5 (MINOR)** — Throughout §V and Appendix C: every Fisher forecast is performed on the *redshift-binned* 40 192-tracer subsample, yet the headline \(\sigma(f_{\rm NL})\) numbers are presented without reminding the reader that they apply only to this restricted subset and not to the full 378 k catalog.

NO ADDITIONAL FINDINGS beyond the six listed above. All other classes (dimensional consistency of displayed equations, internal cross-reference targets, figure-axis vs. body units, appendix–main-text numerical match) were already covered by the initial review or contain no further discrepancies.