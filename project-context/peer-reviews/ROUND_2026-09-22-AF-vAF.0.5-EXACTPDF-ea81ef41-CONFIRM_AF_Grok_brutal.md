# AF ROUND_2026-09-22-AF-vAF.0.5-EXACTPDF-ea81ef41-CONFIRM — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `pipelines/p1_highz_tracers/anomaly_flagship_draft/main.pdf` sha256=ea81ef413503d25291853a2be714226d3b47fe680ead2f01727aaabe961140ca pages=18
**Review packet(s)**: `439a2ddfa9349de8f4db539758caa4bb5dcb423b6ee1b05477d27f3959073918, 90893c5bc95ff1722ea478de43aa3aa0d7386b2e86740c6960617cd28748112e`
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 112.0s

---

**Referee Report — ApJS-CATALOG profile (adversarial read)**

**AF-E1 (ESSENTIAL)** — Abstract, p.1 and Sec. V.D (p.7–8): The abstract states the recovery benchmark “clears none of its pre-declared bars” and that “no class is recovered at its pre-declared bar.” Table VII (p.8) shows exactly this (0/5 classes at the >10×/≥5-match threshold; only 1 BAL quasar at 3.3×). The abstract claim is therefore numerically correct but the paper never states the effect size of the null result (maximum observed enrichment 3.3× on N_ref=5,285; 95% upper limit 12.5% recovery on the smallest class). This is an uncomputed quantitative claim. Required fix: add the explicit upper-limit statement and the Wilson-interval numbers to the abstract sentence.

**AF-E2 (ESSENTIAL)** — Sec. VI.A (p.9) and Fig. 7/Table VIII (p.10): The taxonomy is constructed on (S, α, δ) via PCA→UMAP→HDBSCAN. The paper itself states the families are “a stratification of the candidate list rather than physical classes” and that “right ascension is periodic at 360°; naive Euclidean distance… splits objects near α≈0.” The silhouette test (V12) is negative (−0.0162 vs. −0.0244 null). Presenting 8 “families” as a deliverable when the method is dominated by the input score and sky position is a structural overclaim. Required fix: either drop the taxonomy or re-cluster on latent variables only and re-label as “score-tier strata.”

**AF-E3 (ESSENTIAL)** — Abstract + Sec. VII.B (p.11–12) and Table XI/Fig. 9 (p.13–14): The abstract lists “a named follow-up set.” Four FT-A targets are presented; one (TARGETID 39628216868014338, z=5.194) is refuted in the same paper by Legacy Survey DR10 forced photometry (g=4.33 nmmgy, 94.7th percentile). The abstract therefore advertises a set that the body immediately partially invalidates. Required fix: remove the refuted object from the named list or move the entire FT-A tier to an “open test” section and do not headline it in the abstract.

**AF-E4 (ESSENTIAL)** — Sec. II.B and Table I (p.2–3): The provenance chain is sealed under one run contract. However, the landing receipt date in the manifest (PHASE3.V2.LANDING_2026-09-03.md) post-dates the paper date (21 Sep 2026). The reproducibility manifest is referenced but the DOI placeholder “[PLACEHOLDER: Zenodo DOI…]” remains unresolved. This is a provenance-surface inconsistency that prevents a standalone reader from verifying the exact artifacts.

**AF-M1 (MAJOR)** — Sec. I and p.1–2: The paper is 18 pages for a catalog of 1,244 objects whose dominant property is that >99.5% of fibers above S=3 are sky/non-science (Fig. 1). ApJS catalog papers of comparable length deliver either substantially larger samples or astrophysically validated classes. The present contribution is a null benchmark + descriptive (non-physical) taxonomy. Recommended maximum length: 10–12 pages.

**AF-M2 (MAJOR)** — Sec. V.C (p.7) and Fig. 6 (p.9): The score is shown to be driven by the blue-arm residual (R²=0.78). The paper correctly notes this is instrumental. No quantitative statement is given for how much of the released catalog would be removed by a simple blue-arm quality cut. This is an uncomputed robustness claim.

**AF-M3 (MAJOR)** — Table VII (p.8): Reference samples for four of the five classes are tiny (≤84 objects). The statement “no class is recovered” therefore has very low statistical power for those classes. The 95% upper limits should be reported per class, not only the aggregate 12.5% figure.

**AF-M4 (MAJOR)** — Sec. VI.B (p.9–10) and Table IX (p.11): Family 0 contains 302 objects (45% of the unmatched set) yet spans 350° in RA. The “families” are therefore largely survey/programme strata. The paper acknowledges this but still tabulates them as scientific output.

**AF-N1 (MINOR)** — Multiple locations: The date “September 21, 2026” appears in the header and metadata. This is a future date relative to any real submission; it should be corrected or justified as a placeholder.

**AF-N2 (MINOR)** — Sec. IV.B (p.4): The statement “there is no visible trend of score with redshift” is supported only by visual inspection of Fig. 3 (right). A Spearman coefficient or binned median test should be reported.

**AF-N3 (NIT)** — Fig. 1 caption and Table III (p.4): The y-axis label “sky/non-science (%)” and the table header “Sky/non-science” are used interchangeably with “non-science fibres.” Minor terminology inconsistency.

**AF-N4 (NIT)** — Abstract: “the top 5.7×10^{-5}” is given to two significant figures. The exact ratio 1,244 / 21,793,550 = 5.71×10^{-5}. The rounding is harmless but should be written 5.71×10^{-5} for consistency with the body.

**Summary recommendation: REJECT**

The paper is an admirably honest null-result data release whose central validated claims are (1) that a reconstruction-error score on DESI spectra is dominated by one camera arm and (2) that the selected sample contains almost no previously catalogued unusual objects. These facts are useful infrastructure, but they do not meet ApJS standards for a standalone catalog or taxonomy paper. The taxonomy is explicitly non-physical, one of the four headline follow-up targets is refuted in the same manuscript, the benchmark has negligible power on four of five reference classes, and the manuscript length is disproportionate to the incremental scientific return. The work would be appropriate as a short data-release note or methods appendix, not as an 18-page ApJS article.