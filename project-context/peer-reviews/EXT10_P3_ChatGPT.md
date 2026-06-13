# EXT10 Harvest — P3 — ChatGPT
- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc617-2480-83e8-bf48-cc78a7bce891
- PDF md5: 8533c5a7
- Harvested: 2026-06-13 15:16 PDT

---

## Referee Report — MNRAS-style

**Manuscript:** Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and a Native-Trained Novelty Fraction from 37.3 Million Sources and Map Patches
**Version reviewed:** Paper 3 v3.1.105, PDF updated/created 2026-06-13.

---

**Recommendation: MINOR REVISIONS**

This is an unusually extensive catalogue/methodology paper. I find the main numerical claims substantially internally consistent: the 378,280 headline is correctly constructed as 378,080 point-source detections plus 200 Planck map-patch sky regions; the 7-way 5″ Friends-of-Friends deduplication arithmetic is explicitly reconciled; the Fisher-positivity correction has replaced the earlier symmetric-error form; and the NANOGrav application is presented with appropriate caveats against overinterpreting the Bayes factor.

The paper is close to publishable. The remaining issues are not, in my judgement, evidence of a broken analysis or missing load-bearing control. They are mainly clarity, presentation, and publication-readiness issues. The most important fixes are to make the data release live and citable, remove a small number of threshold/rate wording inconsistencies, and prevent the headline "378,280 anomalies" from being read as "378,280 equally validated catalog-grade astrophysical objects."

---

**BLOCKERS — must fix before publication**

**B1. Data/product release must be live, frozen, and citable.**
Location: Data Availability, p. 23.
Issue: The paper states that the Path-C catalogue, dedup manifest, score columns, schema flags, MCMC artifacts, hashes, and code are staged and "will be made public" with arXiv posting, with a Zenodo DOI to be inserted at submission. For a catalogue paper, this is publication-gating.
Proposed fix: Before acceptance, replace future-tense text with a live DOI, tagged code release, immutable manifest hash, and direct citation to the release version used for all numbers in the manuscript.

**B2. Resolve the DESI "top-1%" wording inconsistency.**
Location: Abstract; §III A; Table II; Conclusions item 1.
Issue: The paper repeatedly describes the DESI headline as a "top-1%" or "top-1% score-cut," while Table I and §II B define the DESI count as an absolute canonical-S cut at S > 5, yielding 195,829/22,504,897 = 0.87%, not 1%.
Proposed fix: Replace every "DESI top-1%" phrase with "DESI S > 5 fixed-threshold cut, 0.87% of the full stream."

**B3. Make the catalog-grade versus exploratory-tier distinction visible in the title/abstract, not only in footnotes.**
Location: Title; Abstract; Table I footnotes; Conclusions item 1.
Issue: The headline 378,280 count includes LAMOST (108,963 exploratory-tier objects) and 200 Planck sky patches rather than point sources. The recommended catalog-grade object subset is 269,117 point sources but this is too buried.
Proposed fix: Add "including exploratory LAMOST and 200 Planck map patches" to the abstract headline sentence, and state immediately after the title/abstract headline that the recommended catalog-grade object subset is 269,117 point sources.

---

**MAJORS — should fix**

**1. Table I is overburdened and mixes cross-transfer and Path-C-native quantities.** Split Table I into two tables or two column blocks: "historical cross-transfer diagnostic" and "Path-C released tier."

**2. The Cramér's V arithmetic in §IV B appears incorrect.** The text gives χ² = 376,713, N = 378,280, and k − 1 = 24,047, then reports Cramér's V ≈ 0.020, but the formula gives approximately 0.0064. Correct the numerical value or remove Cramér's V entirely.

**3. The NANOGrav Bayes factor needs a robustness statement.** Add a compact table in Appendix E giving B_mb/SMBHB under at least two γ-prior ranges and one KDE bandwidth/posterior-density sensitivity variant, or move the Bayes-factor value out of the abstract.

**4. The cross-vendor R-round closure is not visible in the PDF.** I searched the PDF text for "Grok," "Perplexity," "R-round," "VERIFIED," "STALE," and "clean-round" and did not find the requested 0 VERIFIED / 13 STALE closure record. If this closure is intended as a publication deliverable, add a one-paragraph audit appendix.

**5. The eROSITA and Gaia provenance caveats should be surfaced in the machine-readable schema.** Require release columns such as tier_validity, score_axis_status, preprocessing_provenance, and recommended_for_downstream_science.

---

**MINORS — polish**

- Title is too long and slightly misleading: consider "A Multi-Survey Anomaly Catalogue from 37.3 Million Astronomical Sources and Map Patches."
- Abstract is overlong and reads partly as a response log: shorten by moving implementation audit details to a "Version audit / reproducibility" appendix.
- Avoid reporting total "anomaly rates" for mixed fixed-count/fixed-percentile tiers; replace total-row rate cells with "bookkeeping only" or an em dash.
- Add a small on-figure label to Fig. 3: "S axes are survey-specific; compare shapes only."
- Move some footnote content into main text: add a short "Catalogue tiers" subsection before Table I.
- Use "sky regions" consistently for Planck instead of "unique anomalies."
- State whether DESI B-dominant anomalies are included in the recommended follow-up list.
- Replace "decisive" with "decisive under the stated idealized reference model" wherever space allows.

---

**Strengths**

- Scale and ambition: The paper scans 37.3 million sources/map patches across DESI, SDSS, LAMOST, eROSITA, Planck, Gaia, and NEOWISE, and explicitly quarantines ACT rather than forcing it into the headline.
- Excellent audit transparency: The manuscript discloses failed gates, lineage-inferred preprocessing, score-axis irreproducibility, fixed-count tiers, and non-catalog-grade components.
- Deduplication reconciliation is strong: The 5″ FoF arithmetic, radius sweep, chain audit, and multi-survey/intra-survey split are much better documented than in many catalogue papers.
- The Fisher forecast is now statistically safer: The paper uses the positive-definite F0+cα² form, explicitly notes convexity/noise bias, and avoids claiming a multi-tracer detection.
- Methodological lesson is valuable: The LAMOST failure is not merely a nuisance; it is turned into a useful warning about training-set representativeness in unsupervised anomaly detection.
- Novelty fraction is responsibly reframed: The paper distinguishes SIMBAD absence from genuine novelty and quotes the 17.8% DESI top-1000 multi-catalog novelty fraction.

---

**Specific scrutiny requested**

**378,280 anomalies headline:** Internally consistent. My concern is not arithmetic but presentation: the 378,280 headline includes LAMOST exploratory entries and Planck sky patches, so the 269,117 catalog-grade point-source subset should be emphasized more strongly.

**7-way 5″ positional FoF dedup arithmetic (10,213 = 637 + 9,576):** This is checked and convincing. The follow-up cluster-size reconciliation and chain audit are strong: 9,553 multi-member clusters, zero transitive bridges beyond 5″, and exactly 637 clusters spanning two surveys.

**Fisher-positivity caveats:** The corrected form 1/σ²(fNL) = F0 + cα² is now the operative one. The text explicitly rejects the local-linear propagation across α = 0 and gives the proper envelope [3.92, 8.98]. This resolves the earlier symmetric ±2.37-style issue.

**σ(fNL) = 8.14 central at α = 0.19 ± 0.65, <1σ from null:** Internally consistent. The paper correctly says the central improvement is noise-driven and consistent with no improvement at <1σ.

**v3.1.71 cross-vendor R-round: 0 VERIFIED, 13 STALE:** I do not find this closure record in the PDF. I also do not see any obvious surviving live claim that contradicts the requested closure, but a referee cannot verify the clean-round deliverable from the manuscript alone. Add a one-paragraph audit note or supplementary artifact reference.

**NANOGrav 15-yr γ and Bayes factor:** The γ arithmetic is correct: γ = 2.567 ± 0.382 places γ = 3.0 at +1.13σ and γ = 4.33 at +4.61σ. The Savage-Dickey ratio ≃ 7.14×10³ is properly described as decisive only relative to the idealized circular-orbit SMBHB reference. A small robustness table would make this safe to retain in the abstract.

---

**Final recommendation**

MINOR REVISIONS. The analysis appears publication-worthy after publication-gating release actions and a set of clarity fixes. I do not see a need for substantial scientific rework, but I would not accept the paper in its current form until the data release is live and the threshold/headline wording is corrected.
