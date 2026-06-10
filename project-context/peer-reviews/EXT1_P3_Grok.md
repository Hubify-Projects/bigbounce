# EXT1 P3 — Grok Heavy referee report
**Provider**: grok.com web app · effort **Heavy** (Team of Experts)
**Chat**: https://grok.com/project/e6c9ce77-4f86-4d94-b440-1062a78171c1?chat=de56f195-4cae-4dc6-bc3e-f9dbf4de9b54
**PDF**: paper3_anomaly_catalog_v3.1.87.pdf (md5 acde55ca) · **Harvested**: 2026-06-10T16:45 PDT

---

Thought for 1m 0s

Referee Report: MNRAS-style (target: MNRAS or PRD/JCAP)

Manuscript: "Spectrally Unusual Sources at Scale: A Multi-Survey Catalog of 378,280 Path-C Unique Anomalies and Native-Trained Novelty Fractions from 37.3 Million Sources and Map Patches" (v3.1.87, 26 pp.)

Recommendation: MAJOR REVISIONS

The manuscript presents the largest multi-survey autoencoder anomaly catalog to date and a serious attempt at methodological rigor via the Path-C native-retrain protocol. The scale (37.3 M sources/patches → 378 280 unique anomalies) is genuinely impressive, the transparency on gate FAILs and artifacts is exemplary, and the cosmological applications are appropriately caveated as forecasts/illustrative (no detection claims). However, the current draft is not publication-ready. Core reproducibility issues (especially eROSITA), inconsistent tiering in the headline number, and residual over-statement of “discovery rate”/novelty must be fixed before acceptance. The Fisher-positivity handling and NANOGrav re-fit are handled correctly (no blockers there).

BLOCKERS (must be fixed before publication)
§III E (eROSITA DR1) + Table I footnote + Table III + catalog data product
The production score-knee threshold (0.259) and top-298 membership list cannot be reproduced from any released score axis (raw MSE, canonical S, IsolationForest, or any monotone rescaling). The paper correctly discloses this (including the non-monotone Spearman ρ = −0.10 on top-5 and the committed raw-score artifact), but a catalog that cannot be re-thresholded or re-ranked by downstream users is not usable.
Fix: Either (a) release the exact production IsolationForest or raw-score axis used for the 0.259 knee (or the committed artifact file) as the canonical eROSITA column, or (b) drop the eROSITA tier from the headline catalog-grade subset and re-label the 298 sources as “exploratory (irreproducible axis)”. Update every occurrence of the 378 280 headline and the 269 k catalog-grade figure accordingly. This is non-negotiable for a catalog paper.
§I abstract + §III + Table I + §VII conclusions – headline number
The 378 280 figure mixes three reliability tiers: (i) fully validated (DESI + SDSS native + Planck native + NEOWISE masked), (ii) exploratory (Gaia DR3 41 % XV-stability, LAMOST FAIL), (iii) Planck map patches (sky regions, not point sources). The text repeatedly clarifies this, but the abstract and conclusions still lead with “378 280 Path-C Unique Anomalies” without immediate qualification.
Fix: Adopt the explicit 269 317 (or 269 117 point-source) catalog-grade number as the primary headline in abstract, introduction, Table I, and conclusions. Retain 378 280 only as “extended exploratory + map-patch tier”. Add a one-sentence abstract sentence: “The catalog-grade point-source subset (269 117 objects after excluding the LAMOST exploratory tier and map patches) is ∼100× larger than the largest prior single-survey catalog.”
§IV C deduplication arithmetic + audit
The 10 213 collapsed = 637 multi-survey clusters + 9 576 intra-survey duplicates is correctly stated and audited (cluster-size histogram sums exactly; max intra-cluster separation ≤ 4.999″). However, the sensitivity sweep over 3″/5″/7″ radii and the FoF chain audit are buried in §IV C.
Fix: Move the full deduplication provenance (including the exact 9 553-cluster histogram and radius-sweep results) to a new Appendix (or Table I footnote) with the committed JSON artifact cited. Explicitly state that the 5″ radius is a conservative compromise given NEOWISE PSF ∼6″.
MAJORS (should fix)
§IV A novelty assessment
The SIMBAD-unmatched fractions (58.8 % aggregate, 99 % DESI top-10 k) are correctly called database-coverage metrics, not discovery rates. The genuine novelty fraction (17.8 % ± 1.2 % Wilson on DESI top-1 000 vs 20 all-sky catalogs via CDS X-Match) is the right number, but it is introduced late and the abstract still quotes the SIMBAD figure implicitly via “novelty fractions”.
Fix: Lead every novelty discussion with the 17.8 % figure; relegate SIMBAD percentages to a diagnostic paragraph. Add a clear statement that full-catalog novelty extrapolation remains untested.
§V cosmological applications (Fisher forecast)
The α_jk = 0.19 ± 0.65 (jackknife dispersion), central σ(f_NL) = 8.14, de-biased value exactly 8.98, and asymmetric 1σ envelope [3.92, 8.98] under the positivity-respecting form 1/σ²(f_NL) = F_0 + c α² are all correct and transparently caveated. The earlier symmetric ±2.37 form is properly retracted. However, the 9.4 % “improvement” language still appears without immediate “consistent with zero at < 1σ” qualifier in the abstract/intro.
Fix: Delete or rephrase every occurrence of “9.4 % improvement” to “central-value forecast of 9.4 % tightening (consistent with no improvement at < 1σ)”. Retain the envelope and de-biasing language.
§V A NANOGrav re-fit
The KDE free-spectrum emcee posterior (γ = 2.567 ± 0.382, +1.13σ vs matter-bounce γ = 3.0, +4.61σ vs SMBHB γ = 4.33, Savage-Dickey B_MB/SMBHB = 7.14 × 10³) is correctly reported with full MCMC provenance and prior-sensitivity disclaimer. The B factor is prior-sensitive by construction (explicitly stated).
Fix: None required on numbers; however, move the entire NANOGrav paragraph to an Appendix labelled “Illustrative application” and add a sentence in §V: “These are illustrative consistency checks only; neither constitutes a detection or tension claim.”
§VI D Path-C residual caveats (esp. eROSITA/Gaia/LAMOST gates)
The 3 PASS / 3 FAIL-with-diagnostic decomposition and the explicit admission that NEOWISE mask injection-recovery is a geometry QA check (passes by construction) are excellent. However, the paper still includes the FAIL-tier objects in the headline count.
Fix: Explicitly label Gaia and LAMOST as “exploratory only” in every summary table and move them out of the catalog-grade subset (already partially done for LAMOST).
MINORS (polish)
Abstract and §I: replace every occurrence of “378 280” with the catalog-grade number when referring to point-source science use; clarify Planck 200 are map patches, not objects.
§II B a (tabular preprocessing): the Gaia 20-feature lineage-inferred scaler note is honest but should be moved to a footnote or appendix; readers should not have to hunt for it.
Figure captions (esp. Fig. 2, 3, 7, 8, 10): ensure all score axes are explicitly labelled “cross-transfer” vs “native” where relevant.
§IV B χ² spatial test: the p-value 15.7 is dominated by footprint geometry (correctly caveated); either drop the statistic or provide the per-survey selection-function model as supplementary material.
References: all arXiv 25xx/26xx IDs are valid (current date June 2026); no action needed.
Typo-level: “NANOGrav” → consistent capitalization; “fNL” vs “f_NL” (use LaTeX consistently); several “an earlier draft” disclosures are good but can be consolidated.
Strengths (≥3)
Unprecedented scale and genuine multi-survey cross-validation via native retrains (Path-C protocol is a real methodological advance).
Extraordinary transparency: every gate FAIL, training-bias artifact, irreproducible axis, and de-biasing step is explicitly flagged with committed artifacts and reproducibility scripts promised.
Cosmological applications are rigorously conservative (Fisher positivity respected, <1σ null result, illustrative NANOGrav re-fit with full MCMC provenance and prior-sensitivity disclaimer). No over-claims.
Public data release commitment (catalog, weights, scripts) and companion repository references throughout.

Overall: The science is exciting and the engineering is careful. With the blockers addressed (primarily eROSITA reproducibility and consistent tiering of the headline number), this becomes a landmark catalog paper suitable for MNRAS/PRD. I recommend resubmission after MAJOR REVISIONS; I am happy to re-review.

Signed: External Referee (June 2026)

97 sources




Heavy
Attach to message
Drop here to add files to your message
Upgrade to SuperGrok

