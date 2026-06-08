# P3 auto-2026-06-08_1354pt — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 self-critique (2016 chars)
**Wall time**: 68.1s

---

**Referee Report**

**P3-E1 (ESSENTIAL, Abstract + §I p.1, §V p.10)**  
The abstract states “An empirical Landy–Szalay bias measurement on the 5,384 QSO-candidate sample yields \(\alpha_{jk}=0.19\pm0.65\) (<1\(\sigma\) from null); inserting this into the Fisher-positivity-respecting form … gives a central forecast \(\sigma(f_{NL})=8.14\) with 1\(\sigma\) envelope [3.92,8.98] (7.9% improvement …)”. The body (§V) repeats the identical sentence. The quoted 7.9% improvement is obtained only after inserting a value statistically indistinguishable from zero; the paper never states that the improvement itself is <1\(\sigma\). This is a direct violation of PRD standards on reporting of marginal results. Required fix: remove the percentage improvement claim or qualify it at every occurrence with “statistically insignificant (<1\(\sigma\))”.

**P3-E2 (ESSENTIAL, Table I footnote † + §III D p.3)**  
LAMOST DR10 contributes 44,075 anomalies (0.39% rate) of which 98% are explicitly identified as blue-excess training artifacts. The Path-C “native retrain” still releases this tier as an “exploratory” catalog. No quantitative decontamination or down-weighting is applied before the 7-way deduplication that produces the headline 378,280 count. The multi-survey catalog therefore contains a known ~44k-object contaminant population whose inclusion is not justified by any science requirement. Required fix: either excise the LAMOST tier from the primary catalog or demonstrate that the artifact population does not propagate into the 378,080 point-source headline number.

**P3-E3 (ESSENTIAL, §II D + Table I)**  
The paper employs two incommensurate selection thresholds: (i) fixed canonical \(S>5\) for DESI, (ii) survey-specific top-percentile cuts (e.g., \(S>0.1060\) for SDSS, \(S>0.4613\) for LAMOST) for the remaining surveys. No global mapping between these thresholds is provided, nor is any statement that the resulting anomaly populations are statistically comparable. The 378,280 “Path-C unique” number is therefore an inhomogeneous union. Required fix: adopt a single, explicitly justified selection function across all surveys or publish separate homogeneous sub-catalogs.

**P3-E4 (ESSENTIAL, §IV A p.9 + Fig. 5)**  
The “genuine novelty fraction” of 17.8% is obtained from a single unweighted draw of the top-1,000 DESI anomalies cross-matched against 20 external catalogs. No bootstrap, jackknife, or magnitude-dependent completeness correction is shown. The number is presented in the abstract and §I as a headline result. Required fix: replace with a properly uncertainty-quantified estimate or remove the claim.

**P3-M1 (MAJOR, §III F p.6 + Table I)**  
Planck CMB contributes exactly 200 patches selected by a fixed top-1% cut on a cross-transfer model that failed both native-retrain gates. The paper states these 200 patches are retained “as a sensitivity-check artifact.” Their inclusion in the 378,280 headline count is therefore methodologically inconsistent with the Path-C protocol applied to every other survey. Required fix: move the 200 patches to a separate supplementary table or demonstrate that they satisfy the same validation criteria as the spectroscopic surveys.

**P3-M2 (MAJOR, §V A p.10)**  
The Fisher forecast uses a single-tracer baseline \(\sigma(f_{NL})^{\rm std}=8.98\) derived from the DESI QSO sample alone. The multi-tracer improvement is then quoted relative to this number. However, the multi-tracer covariance matrix is never published, nor is the precise linear combination of tracers that yields the quoted 8.14 value. Reproducibility is impossible from the supplied material. Required fix: deposit the full Fisher matrix and the exact tracer weights.

**P3-M3 (MAJOR, Fig. 2 right panel + §III C)**  
The SDSS DR18 anomaly-score distribution spans twelve orders of magnitude (\(S=5\) to \(1.9\times10^{11}\)) because the DESI-trained BigAE is applied out-of-distribution. The paper acknowledges the dynamic-range artifact yet still includes the 77,905 SDSS objects in the deduplicated catalog. No quantitative assessment of how many of these extreme scores are simply domain-shift outliers is provided. Required fix: either restrict the SDSS contribution to a well-calibrated percentile or publish a domain-shift diagnostic.

**P3-N1 (MINOR, throughout)**  
Multiple surveys use different latent-space dimensionalities (128 for spectra, 16 for photometry, 32 for ACT) without a unified justification or ablation. This is a minor but unnecessary source of heterogeneity.

**P3-N2 (NIT)**  
Axis labels on Fig. 2 (right) omit units on the probability-density axis; minor cosmetic fix.

**Summary recommendation**  
**MAJOR REVISIONS**  

The manuscript presents a technically impressive data-reduction pipeline but fails to meet PRD standards on statistical homogeneity, artifact control, and honest reporting of marginal results. The three essential issues (incommensurate selection thresholds, inclusion of a 98%-artifact LAMOST tier, and an overstated 7.9% \(f_{NL}\) improvement that is <1\(\sigma\)) each independently require substantial revision. Until these are corrected the headline catalog number and cosmological claim cannot be accepted.

---

## PASS 2 — self-critique findings (what initial review missed)

**P3-E5 (ESSENTIAL, Abstract + §V p.10)**  
The claimed “7.9% improvement” in \(\sigma(f_{NL})\) is arithmetically inconsistent with the two numbers supplied in the same sentence: \((8.98-8.14)/8.98=9.35\%\). No other baseline or rounding convention is stated that would produce 7.9%. Required fix: correct the percentage (or remove it) and propagate the change to every occurrence.

**P3-M4 (MAJOR, §III F + Table I footnote †)**  
The Planck CMB tier (200 patches) is produced by a cross-transfer model whose native-retrain validation loss (\(\approx2\times10^4\)) fails both Path-C gate criteria by >60\(\sigma\). The paper nevertheless folds these 200 objects into the headline 378,280 count while simultaneously labeling them a “sensitivity-check artifact.” This violates the uniform Path-C protocol applied to all other surveys. Required fix: move the Planck tier to a supplementary table or demonstrate that it satisfies the same quantitative gates used for the spectroscopic surveys.

**P3-m1 (MINOR, Fig. 2 caption + §III C p.5)**  
Fig. 2 (right) caption states the SDSS distribution spans “twelve orders of magnitude” from \(S=5\) to \(1.9\times10^{11}\). The body text repeats the identical claim. Both are correct, but the probability-density axis is unlabeled (no units or normalization), making the plotted curve impossible to interpret quantitatively. Required fix: add explicit axis label and normalization statement.

**P3-N3 (NIT, Table I last row)**  
The Path-C unique total is listed as 37,272,042 sources yet the arithmetic sum of the seven native-retrain columns is 37,292,042 (difference of exactly 20,000). The discrepancy is not footnoted. Required fix: reconcile or explain the 20 k offset.

NO ADDITIONAL FINDINGS beyond the four items above. All other classes (dimensional consistency of displayed equations, cross-reference accuracy, null-procedure comparability qualifiers, appendix–main-text numerical match, etc.) were already covered by the issues identified in the initial review.