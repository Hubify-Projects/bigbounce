# AF ROUND_2026-09-22-AF-vAF.0.7-EXACTPDF-8982c1d8-BOARD — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` sha256=8982c1d8e1e0fac155aa27909a71300c1ee68bc2cfded6c6f944f019985c4023 pages=18
**Review packet(s)**: `b9aca4cd46cee659faac9d334a886e28f7893e4af5e787ded6ea9ee840c063f0, cc4d1eb7448d23ce606ec8f82524d6b66372d6ebea15d7eddb0975b681d98933`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 121.5s

---

**Referee Report**

**Paper:** "A provenance-sealed DESI DR1 anomaly-score candidate catalogue: selection, validation, and a null known-object recovery benchmark" (ApJS candidate)

**Findings (adversarial audit against ApJS-CATALOG standards)**

**AF-E1 (ESSENTIAL, p.1, abstract & §I)**  
Abstract states the released catalogue is "the top 5.7×10^{-5} of the science-target population" and presents it as a usable anomaly-score catalogue. Body (§III.B, Table III, Fig. 1) shows >99.5% of objects above S>3 are sky/non-science fibres before the provenance gate; the final 1,244 objects remain dominated by the same instrumental tail. The abstract claim is stronger than the calibrated body statement that the tail is "not a faintness or short-exposure artefact" but is "essentially uncorrelated with exposure quality" while being "almost entirely explained by the blue-arm reconstruction residual" (R²=0.78). Required fix: rewrite abstract to state the instrumental origin explicitly and remove any implication of astrophysical anomaly utility.

**AF-E2 (ESSENTIAL, p.1 & §V.D)**  
Abstract and §I claim a "null known-object recovery benchmark". Table VII shows 95% upper limits of 0.019%–0% recovery for all five reference classes (N_ref=27–5,285); the rarest class (SLSN hosts) has an upper limit of 12.5%. No effect-size or practical-significance statement accompanies the headline recovery fractions. The benchmark demonstrates the selection has negligible power to recover any published unusual class. Required fix: either drop the benchmark as a selling point or state in the abstract that the selection recovers no known class above the pre-declared bar.

**AF-E3 (ESSENTIAL, p.1 header & throughout)**  
Header contains "Dated: September 22, 2026 (vAF.0.7)". Multiple internal-audit tags and version strings appear in the rendered PDF. These are not part of a published ApJS article. Required fix: remove all version-control strings, round identifiers, and future dates from the visible document.

**AF-E4 (ESSENTIAL, §IV.B, §V.C, Fig. 6)**  
The anomaly score S is shown to be a direct affine function of the b-camera residual (ρ_s= +0.527, p~10^{-89}); the other two cameras contribute negligibly once b is included. The paper correctly identifies this but still releases the catalogue as an "anomaly-score" product. No quantitative statement of how much variance remains after removing the b-arm term is given in the abstract or §I. Required fix: state in the abstract and introduction that the released score is dominated by a single spectrograph arm residual.

**AF-M1 (MAJOR, §VI, Tables VIII–IX, Fig. 8)**  
The 23-cluster/9-family taxonomy is derived from (S,α,δ) sky-position embedding only. The latent-space silhouette test (§VI.C) yields –0.0183 against a 50-draw permutation null of –0.0309±0.0059; the observed value is negative, confirming the families are not separated in the model’s own 128-dimensional latent space. The paper labels them "descriptive strata, not physical classes" but still presents Tables VIII–IX and Fig. 7 as core results. Required fix: move the taxonomy to an appendix or remove it; it does not survive the paper’s own latent-space test.

**AF-M2 (MAJOR, §VII.B, Table XI, Fig. 9)**  
Four FT-A z≥4 candidates are highlighted. One (TARGETID 39628216868014338, z=5.194) is refuted by Legacy Survey photometry (g=4.33 nJy at 94.7th percentile while the break requires darkness in g). The other three remain undecided because the released schema omits inverse-variance columns. The paper records this as "one refuted, three undecided". No population-level inference is possible. Required fix: remove the FT-A tier from the named follow-up set or relegate it to an explicit "failed test" subsection.

**AF-M3 (MAJOR, §V.D & abstract)**  
The known-object recovery benchmark uses N_ref=27–5,285 objects per class inside the DR1 footprint. The paper states the benchmark "has little power" and "excludes only a strong recovery signal". No comparison to any published outlier-detection recovery rate on comparable spectroscopic samples is provided. The null result is presented as a positive feature ("validated data release") rather than a limitation of the method. Required fix: add a direct comparison to at least one external reconstruction-error or isolation-forest recovery benchmark on DESI-like data.

**AF-M4 (MAJOR, §III.B & Fig. 1)**  
The provenance gate (OBJTYPE=TGT, COADD_FIBERSTATUS=0, TARGETID>0) is applied before the score cut. Above S>3 the sky/non-science fraction already exceeds 99.5% and rises monotonically. The gate is therefore the dominant filter; the score cut adds little additional purity. The paper acknowledges this ("a property of the substrate") but still titles the work an "anomaly-score candidate catalogue". Required fix: retitle or reframe to make the dominance of the provenance gate explicit in the abstract and introduction.

**AF-N1 (MINOR, multiple tables)**  
Several tables (e.g., Table IV) list "unpopulated placeholder" columns (classification, discovery_potential) with no values. These are cosmetic but should be dropped or explicitly marked "reserved".

**AF-N2 (MINOR, §IX)**  
Reproducibility manifest lists SHA-256 hashes but the landing-receipt date (2026-09-03) post-dates the manuscript date (2026-09-22). Minor bookkeeping inconsistency.

**AF-NIT1–NIT3**  
Minor caption typos, axis-label font inconsistencies in Fig. 5, and one duplicated phrase in the validation-contract table header.

**Summary recommendation**  
**REJECT**

The paper is a meticulously documented negative result: the released score is overwhelmingly instrumental, the recovery benchmark has negligible power, the taxonomy fails its own latent-space test, and one of the four highlighted high-redshift candidates is already refuted by public photometry. ApJS catalogue standards require a demonstrated, reproducible selection that yields a usable sample for downstream science; this work instead supplies an infrastructure release whose primary scientific content is "this selection does not work for the intended purpose". The honest framing does not compensate for the absence of a positive, astrophysically motivated selection function or any object that survives public-data scrutiny as a genuine anomaly. The manuscript would require a fundamental reframing (and new data) to meet ApJS acceptance criteria.