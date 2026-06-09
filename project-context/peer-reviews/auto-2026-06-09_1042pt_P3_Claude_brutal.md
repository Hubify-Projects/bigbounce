# P3 auto-2026-06-09_1042pt — Brutal-honesty PRD referee with full PDF access (figures, tables, equations)

**Reviewer**: `Claude_brutal`
**Model**: `claude-opus-4-7`
**Input format**: NATIVE PDF (document block) + extended thinking 16K + pass-2 self-critique (13388 chars)
**Wall time**: 590.6s

---

# Referee Report — P3 (PRD submission)

## Overall Assessment

This is a 20-page catalog paper with two thin cosmology applications appended. The submission has multiple structural problems for PRD: (i) the principal product is an astronomical source catalog, which is not PRD-appropriate content; (ii) both nominally cosmological results (fNL forecast and NANOGrav spectral-index fit) are sub-σ effects that the paper itself concedes are consistent with no detection; (iii) half the survey blocks fail the authors' own injection-recovery gate at 5σ and are released anyway as "exploratory tiers"; (iv) the paper carries pervasive internal-bookkeeping language ("Path-C", "FAIL-with-diagnostic", "before/after diagnostic", "quarantined", "BigAE framework") that has no published referent; and (v) several headline arithmetic figures do not reproduce from the displayed inputs.

I recommend **REJECT**. Details below.

---

## ESSENTIAL findings

### P3-E1 — Headline "7.9% improvement" does not reproduce from the displayed Fisher form (Abstract, §V, Conclusions)
The abstract states: "central forecast σ(fNL) = 8.14 with 1σ envelope [3.92, 8.98] (7.9% improvement…)". Recomputing from the stated form 1/σ² = F₀ + cα² with F₀ = 1/8.98², c = 0.0747, αjk = 0.19:

- c·α² = 0.0747·0.0361 = 2.697×10⁻³
- 1/σ² = 1.5101×10⁻²
- σ = 8.137
- (8.98 − 8.137)/8.98 = **9.36%**, not 7.9%.

The 7.9% figure appears to be the canonical 5-tracer multi-tracer dense-limit improvement quoted in Appendix C ("+7.93% ideal-multi figure"), which is a different forecast (full multi-tracer with fiducial α=0.15-like scaling), not the empirical-α single-tracer-augmented forecast. The abstract, §V, and Conclusions all juxtapose 8.14, αjk=0.19, and "7.9%", which is internally inconsistent.
**Required fix:** State the correct percentage (9.4%) or correct σ(fNL); clarify whether the headline is the empirical-α single-tracer-augmented forecast or the canonical 5-tracer forecast. They are not interchangeable and the paper currently treats them as such.

### P3-E2 — Half of the survey blocks fail the authors' own validation gate yet are released as catalogs
Abstract/§II D/Fig. 7: "3 PASS (SDSS 64%, Planck 100%, NEOWISE 100%) and 3 FAIL-with-diagnostic at 5σ (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%)". LAMOST recovery at 5σ of 5.8% means **94% of true 5σ signals are missed**; the paper nonetheless publishes 113,342 LAMOST "exploratory tier" anomalies and counts them toward the headline 378,280. The Gaia tier (500 objects) and eROSITA 298-tier are equally unvalidated. Releasing catalogs that fail the authors' own pre-registered injection-recovery gate, then carrying them into the abstract headline count, is not acceptable PRD methodology.
**Required fix:** Either restrict the headline number to surveys that pass the 5σ injection-recovery gate, or remove the gate as a stated validation criterion. Pick one. The current "FAIL-with-diagnostic" framing converts a failed test into a passed one through nomenclature.

### P3-E3 — LAMOST native-retrain count is internally contradictory
§III D: "Path-C native retrain … compresses the anomaly rate 21.5× to 2,054 at S>5; top-113,342 native slice at S ≥ 0.4613 is the released LAMOST anomaly set." The paper documents that native retraining removes a 21.5× artifact (the contaminated catalog has 44,075 anomalies; the artifact-cleaned threshold-S>5 catalog has 2,054), then ships a 113,342-object catalog from the very same native model by simply moving the threshold to a top-percentile cut. This is **larger than the original artifact-contaminated catalog** (44,075). The published catalog therefore contains the cleaned 2,054 plus ~111,000 additional sources scored below the validated threshold, with no validation. The simultaneous claim that "98% blue-excess artifact compresses 21.5×" and that the released catalog is 2.6× larger than the artifact catalog is contradictory.
**Required fix:** Either release the 2,054 validated objects, or justify why expanding 55× past the validation threshold preserves any catalog quality.

### P3-E4 — DESI in-sample scoring "catalog-curation" handwave
§II B: "The S > 5 absolute MSE-anchored threshold applied to the full 22.5 M curated catalog yields the 0.87% anomaly rate; applying it to a random uncurated SPARCL sweep flags > 50% of spectra (a catalog-curation effect, not a threshold artifact)." A threshold that flags >50% of out-of-distribution spectra is by definition not an anomaly threshold. The "catalog-curation effect" is not derived, quantified, or independently verified; the reader is asked to accept that a 50,000% inflation in flag rate is benign. If the curated catalog and the uncurated SPARCL pull differ by a factor of >50 in flag rate at the same threshold, the threshold is not measuring what the paper claims.
**Required fix:** Reproduce the OOD flag rate, document the curation criterion, and either show that the curated subset is matched to the training pool or rescore at a curation-matched threshold. Currently this is a critical unaddressed contamination diagnostic.

### P3-E5 — Cosmology venue mismatch
The two PRD-relevant results are: (a) σ(fNL) forecast with αjk = 0.19±0.65 (consistent with zero at 0.29σ; "7.9% improvement … consistent with no improvement at <1σ"), and (b) NANOGrav γ = 2.567±0.382 with matter-bounce at +1.13σ ("marginally consistent"). Both are sub-σ, both are explicitly disclaimed in-text as non-detections. Stripped of these two appendices, the manuscript is an astronomical source catalog — appropriate for ApJS, MNRAS, or A&A. PRD requires positive cosmological inference, not a catalog with two sub-σ cosmology paragraphs.
**Required fix:** Resubmit the catalog to an astronomy journal; submit a separate, focused cosmology paper if and when there is a >2σ result.

### P3-E6 — Planck × ACT "null cross-correlation" relies on a quarantined input
§IV D presents a Planck × ACT null cross-correlation as a science finding ("an important negative result for proposed CMB anomaly detection programs"). Appendix F admits that the ACT block is a "quarantined methodological artifact" and that "§IV D relies on the cross-transfer ACT anomaly set as its input." A null result computed from a self-declared invalid input is not a science result; it is an artifact of an undertrained autoencoder. Either §IV D must be removed, or a Path-C-compliant native ACT analysis must be performed and used.

### P3-E7 — "BigAE framework" cited as if established; no reference
Throughout (abstract, §II A) the paper refers to "the BigAE autoencoder framework" as if it were a published, citable method. There is no reference; it is the author's name for a vanilla fully connected autoencoder. PRD does not accept self-coined "frameworks" presented as established without a published reference.
**Required fix:** Drop "framework" wording, describe as "a fully connected autoencoder (this work)", and remove the proper-noun framing.

### P3-E8 — Internal bookkeeping language pervades the body
"Path-C", "Path-C rebuild protocol", "before/after diagnostic", "FAIL-with-diagnostic", "exploratory tier", "quarantined", "8-way-with-ACT variant … preserved as a sensitivity-check artifact", "Path-C-final catalog", "Path-C-compliant". These are not standard terms in the literature; they are project-internal naming conventions exposed in the manuscript. The phrase "Path-C" appears dozens of times without ever being defined as anything other than "the rebuild we did". PRD prose should describe procedures by what they do, not by internal version labels.

### P3-E9 — Bayes factor "decisive" claim is prior-dominated and miscommunicated
§V A: BMB/SMBHB = 7.14×10³, "decisive on Jeffreys' scale". Savage-Dickey of two point predictions (γ=3.0 vs γ=4.33) against a uniform prior γ ∈ [0,7] yields a ratio that depends linearly on prior width. The factor is not a model-comparison statement about matter-bounce vs SMBHB; both are point predictions within the same single-parameter power-law family, and BMB/free = 3.23 is "weak" on Jeffreys. Reporting BMB/SMBHB as "decisive" without disclosing the prior-width dependence and the underlying near-flat likelihood is overclaim.

### P3-E10 — "73× like-for-like" is not like-for-like
Abstract: "the DESI-only axis (195,829 anomalies) is a ∼73× like-for-like increase" vs Liang et al. (2,685 anomalies on ~250k spectra). The present DESI sample is 22.5M spectra, ~90× larger than Liang et al.'s. The anomaly rates are similar (0.87% vs 1.07%), so the 73× ratio is *trivially* the sample-size scaling. There is no methodological improvement implied; calling this "like-for-like" misrepresents the comparison. Similarly the "141×" headline.

---

## MAJOR findings

### P3-M1 — Fig. 1 caption contradicts figure content
Fig. 1 title: "Spatial distribution of all 319,443 anomalies across 8 archives". Legend includes ACT DR6 (gray). Caption: "ACT DR6 is quarantined and excluded." If ACT is excluded, the count is 319,243 (319,443 − 200 ACT patches). The figure depicts what the caption claims is excluded.

### P3-M2 — Single-author claim of "largest multi-archive anomaly detection campaign to date"
A single independent researcher claiming the largest-ever multi-archive (DESI + SDSS + LAMOST + eROSITA + Planck + Gaia + NEOWISE + ACT) anomaly catalog needs much stronger validation than what is presented. There is no independent reproduction, no team of co-authors with archive-specific expertise, no co-PI from any of the seven collaborations. PRD-grade multi-survey claims typically have author lists from the surveys involved or at minimum an MOU-level documented arrangement. This must be disclosed; the data-rights situation for some of these archives (particularly DESI DR1 internal data products and eROSITA-DE) requires explicit acknowledgement.

### P3-M3 — Genuine novelty fraction is a single-sample point estimate
Abstract claims "genuine novelty fraction of ∼17.8%" with the parenthetical "single-sample point estimate at the top-1,000 score stratum; full-catalog rate empirically untested". A single, untested, stratum-specific point estimate is not a "novelty fraction"; it is one bin of an unmeasured function. The 17.8% should not be elevated to the abstract without bootstrap uncertainties or independent stratum measurements. The 82.2%/17.8% split also depends entirely on the 20-catalog selection.

### P3-M4 — Three "highlighted" DESI×SDSS matches are thin discovery
§IV C: 637 multi-survey 5″ coincidences, of which the paper highlights three: (a) a known z≈1.55 QSO (not a discovery), (b) TIC 374313355 (already in TESS Input Catalog), (c) an "uncataloged BAL QSO at z ≈ 0.86" with no independent confirmation, no follow-up spectroscopy, no published characterization. The discovery claim rests on the authors' own redshift fit and their own absence-from-Milliquas check. For PRD, one un-followed-up object is not a discovery.

### P3-M5 — eROSITA injection recovery 1.2% then XV-stability 81.5%: incompatible
§III E and §VI D claim that the eROSITA injection-recovery is 1.2% at 5σ (essentially a complete failure) but that IsolationForest cross-validation stability is 81.5%. These cannot both characterize the same detector behavior. The first says the detector is blind; the second says it is stable. The resolution is that the IF stability is measuring agreement-with-self, not sensitivity. The paper conflates the two and reports 81.5% as a redemption metric. It is not.

### P3-M6 — Spatial uniformity χ² test acknowledged as dominated by footprints
§IV B: χ² = 143,936, dof = 38,329, χ²ν = 3.76 — then immediately disclaimed: "the significant χ²ν = 3.76 is dominated by the inhomogeneous footprints of the seven retained archives rather than intrinsic astrophysical clustering". If the test is dominated by footprint, do not report it. Currently the headline number is in the body before the disclaimer.

### P3-M7 — α_jk = 0.19 ± 0.65 implies no constraint
The empirical bias enhancement is consistent with zero at 0.29σ and the 1σ interval [−0.46, +0.84] contains both no-improvement (α=0) and modest-improvement values; the 95% interval is [−1.08, +1.46]. The "central forecast 7.9% improvement" is selected from a posterior that overwhelmingly favors zero. Reporting a central improvement as the headline rather than the posterior is inappropriate; PRD readers will reasonably read the abstract as a forecast of multi-tracer benefit when the data show none.

### P3-M8 — SDSS native-retrain "compresses 6500×" is presented as success
§III C: cross-transfer flags 77,905 SDSS anomalies; native retrain at S>5 yields 12 — described as "∼6500× anomaly-rate reduction confirming catalog-calibration domain shift". The published SDSS catalog is then 77,905 anomalies selected at a top-percentile cut on the native model, *not* at S>5. This is the same problem as LAMOST (P3-E3) at smaller scale: the validated cut yields 12, the released cut yields 77,905. Pick one.

### P3-M9 — Table I caption load-bearing footnotes contradict main row
Footnote ‡ states SDSS Path-C native at S>5 is 12 sources; column shows 77,905. Footnote ¶ says "Path-C native-retrained counts are the canonical results; cross-transfer counts are preserved as the before/after baseline. Per-survey Nanom values shown in this column are the initial cross-transfer scan counts." Then the same column is used to compute the 388,493 sum, which is described in the Path-C unique row immediately below as the Path-C native total. The table mixes cross-transfer and native counts depending on which row sums are needed.

### P3-M10 — Validation MSE values cited without normalization context
§II D step 1: "validation loss ≤ 0.30" gate. The Planck native autoencoder has val_loss = 0.4437, which FAILS criterion (a), but is admitted under criterion (b). Spectroscopic native retrains pass at 0.0311, 0.0329. The val_loss is per-element MSE — its absolute magnitude depends entirely on the input normalization, which is not consistently documented across survey blocks. A 0.30 gate that is met for one normalization and not another is not a gate.

### P3-M11 — Fig. 9 image gallery has labels like "AE=83518" with no definition
Fig. 9 panel labels include "AE=5.30", "AE=83518", "AE=9240". The caption does not define "AE". In §III B these are documented as Z-arm sub-scores rₐ (not total anomaly scores S) — but the panel labels just say "AE", and one value is 83,518, which the body says cannot be the total score for the S>5 catalog (max ≈ 25.2). Either the gallery shows objects outside the catalog, or the labels are misleading. Fix the labels.

### P3-M12 — NANOGrav: Gaussian-approx ± std-dev vs quantile widths
§V A: "γ = 2.567 ± 0.382 (Gaussian-approximation: posterior mean ± sample standard deviation; equivalent quantile summary γ = 2.591₋₀.₂₈₇⁺⁰·²⁹¹". The two widths differ by ~30%. The paper uses ±0.382 for the +1.13σ matter-bounce test. The choice of which uncertainty to quote determines whether the deviation is +1.13σ or +1.43σ. Pick the correct uncertainty for a parameter-shift test (the quantile-based asymmetric width is more honest) and recompute.

### P3-M13 — "B-dominant" 22.7% of DESI anomalies flagged as "calibration-suspect"
§VI C: "the ∼44,000 DESI B-dominant anomalies (22.7%) are flagged as calibration-suspect; confirmation via photometric color selection is needed." Nearly a quarter of the headline DESI catalog is admitted-unverified. This should be disclosed in the abstract.

---

## MINOR findings

### P3-Mi1 — Fig. 2 left panel score axis
The left panel histogram cuts off at S=25 but the abstract names a peak structure; the three labeled outliers are at 24.5, 24.6, 25.2 — overlapping labels make the figure unreadable at those scores. Replot with separated labels.

### P3-Mi2 — Table V "ACT DR6" row retained despite quarantine
Table V lists ACT DR6 with 32-dim latent, 540K params, 7.0 s training. The footnote acknowledges this is the cross-transfer baseline. If ACT is quarantined, the table should either remove this row or visually mark it as such (strikethrough, grey, etc.).

### P3-Mi3 — Reference [33] bibkey commentary in PDF
Reference [33] reads "Heinrich, O. Doré, and E. Krause … [publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]". This is bibliography-internal bookkeeping that should not appear in the published reference list. Strip the bracketed bibkey commentary.

### P3-Mi4 — Acceptance fraction 0.632 is suspiciously high for emcee
§V A: emcee 32 walkers, 10k production, acceptance 0.632, τ ≈ 58 samples/walker. emcee typical acceptance for well-tuned posterior is 0.2–0.5. 0.63 with this autocorrelation suggests under-mixing on a narrow likelihood; report the Gelman-Rubin R̂ or equivalent multi-chain diagnostic.

### P3-Mi5 — "Independent OOD validation on 100k unseen DESI spectra retrieved via NOIRLab SPARCL (seed distinct from the training pool)" but then >50% flag rate
The OOD test (100k spectra) is presented as a successful validation ("Jaccard 0.732, PASS"), but the SPARCL random uncurated sweep flags >50%. These two statements together suggest the 100k OOD set was sampled from the same curation domain as the training pool, in which case it is not a true OOD test. Clarify the sampling procedure.

### P3-Mi6 — eROSITA Table III "IF raw score" 34,182 next to "SBigAE" 1.084
Table III: column SBigAE values in [0.4, 1.1] alongside SIF,raw values in the 10⁴ range. The footnote explains these are different scales, but presenting them side-by-side invites confusion. Either separate into two tables or normalize.

### P3-Mi7 — αGS = +1.83 ± 2.03 gives 1σ envelope down to σ(fNL) = 0.94
§V last paragraph: "αGS,jk = +1.83 ± 2.03 (σ(fNL)GS = 1.95 central, 1σ envelope [0.94, 8.98])". This is an extraordinary improvement claim — single-tracer DESI baseline 8.98 reduced to 0.94 (9.6× improvement) — buried in a single sentence at the end of §V with "consistent with no improvement at <1σ" tacked on. Either this is a real result (in which case it is the headline of the paper) or it is a fluctuation on a 1122-object subsample (in which case it does not belong). Currently it is presented as marginalia and reads as cherry-picking.

### P3-Mi8 — "the published catalog headline of 298 sources" vs "9,303 IF reference set"
§III E: the published eROSITA catalog is 298 sources at S>0.259. The IF cross-validation uses a 9,303 top-1% reference. The "284/298 = 95.3% overlap" reports overlap of the 298 in the 9,303, which is a one-way containment, not symmetric agreement. The Jaccard of (298, 9,303) sets at 284 overlap is 284/(298+9303-284) = 0.030, not 95.3. Be explicit which metric is being reported.

### P3-Mi9 — Companion data repository links private "pending arXiv acceptance"
Data availability: "private pending arXiv acceptance; public upon acceptance". This is fine for arXiv but PRD requires the data to be available at peer review for the referee. Currently the referee cannot verify any of the catalog claims, MCMC chains, or model weights.

### P3-Mi10 — "Hubify Projects" / "bamfai" / "bigbounce" repository names
The github/HuggingFace URLs (Hubify-Projects/bigbounce, bamfai/bigbounce-anomaly-catalog) tie the catalog to project branding rather than a stable archival identifier (Zenodo DOI). Provide a permanent DOI.

### P3-Mi11 — Page count
20 pages for a catalog whose two cosmology applications are explicitly <1σ. Recommended max for a focused cosmology methods paper at PRD: ~12-15 pages. If recast as catalog + appendix forecasts, more like 10 pages, which then belongs at ApJS or MNRAS anyway.

---

## NIT findings

### P3-N1 — "DESI DR1 documentation" reference [1] is not a citable reference
Reference [1] reads "DESI Collaboration, 'The DESI Data Release 1,' 2025, DESI DR1 documentation." This is not a publication; cite the actual DR1 paper (DESI Collaboration 2024 or the DR1 catalog paper).

### P3-N2 — "Houston Golden, Independent Researcher, Los Angeles, California, USA"
Contact email "houston@hubify.com" is a company email; affiliation says independent researcher. Disclose any conflict.

### P3-N3 — Repeated "Path-C" — replace with descriptive term
Suggest "native-retrain protocol" or similar throughout.

### P3-N4 — "(NOTE: 'z-scored' here is the statistics term…)" in body
The footnote-style parenthetical in §II B explaining the z-score / redshift terminology should be a numbered footnote, not inline body.

### P3-N5 — Fig. 6 panel (d) score 49.5 vs (c) score 8.1 same object
The 6× score change between epochs for "TIC 374313355" is striking; consider showing the difference spectrum or noting the flux level explicitly. The caption says "consistent with a stellar flare or accretion event" — TESS variable + 6× spectral change at different epochs is more consistent with intrinsic variability than novel astrophysics.

### P3-N6 — Acknowledgment of computational resources
"Computations were performed on an NVIDIA H200 GPU pod via RunPod" — fine, but consider acknowledging that the analysis used a single GPU rental, which is relevant context for the "largest ever" framing.

---

## Summary recommendation

**REJECT**

This manuscript is a catalog release with two sub-σ cosmology vignettes. The catalog itself has substantial methodological problems — half the survey blocks fail the authors' pre-registered injection-recovery gate at 5σ but are released anyway as "exploratory tiers" and counted in the headline 378,280; the LAMOST and SDSS native-retrain "validation" produces catalogs 55× and 6500× larger than the validated S>5 cut would yield; the DESI in-sample/OOD flag-rate discrepancy (0.87% vs >50%) is unaddressed; "Path-C", "BigAE framework", and "FAIL-with-diagnostic" are internal project terminology presented as established methodology. The cosmological results — αjk = 0.19±0.65 (consistent with zero at 0.29σ; central "7.9% improvement" does not arithmetically reproduce from the stated form, see P3-E1) and a NANOGrav matter-bounce shift of +1.13σ — are explicitly disclaimed as non-detections in-text. PRD is not the appropriate venue. The catalog portion belongs in ApJS or MNRAS after the validation-gate and native-retrain-threshold contradictions are resolved; the cosmology applications do not currently support an independent PRD submission. Independently of venue, the arithmetic inconsistencies (P3-E1, P3-E3, P3-M9), the methodological inconsistencies (P3-E2, P3-E4, P3-E6), and the pervasive internal bookkeeping language (P3-E8) would require a complete rewrite before any journal could accept this.

---

## PASS 2 — self-critique findings (what initial review missed)

# Referee Report — P3 (PRD submission), SECOND PASS

After re-reading with the checklist above, I find additional issues. The first pass focused on top-level structural problems; this pass focuses on arithmetic reproducibility, figure-body consistency, and cross-reference integrity. The findings below are **new** (not duplicates of the initial review).

---

## ESSENTIAL findings (new)

### P3-E11 — The aggregate "58.8% SIMBAD-unmatched" figure is not reproducible
Table I and §IV A juxtapose per-survey SIMBAD-unmatched rates and an aggregate "58.8%". Weighting per-survey rates by anomaly counts (using cross-transfer counts as the table column shows):

- DESI: 0.99 × 195,829 = 193,871
- SDSS: 0.90 × 77,905 = 70,115
- LAMOST: 0.50 × 44,075 = 22,038
- eROSITA: 0.68 × 298 = 203
- NEOWISE: 0.45 × 436 = 196
- Gaia: 0.27 × 500 = 135
- **Total unmatched = 286,558 / 319,043 (excl. Planck N/A) = 89.8%**

I cannot reproduce 58.8% from any natural weighting of the per-survey rates as published. The aggregate appears in the abstract, in Fig. 5's dashed reference line, and in Table I. Either the per-survey rates or the aggregate is wrong.

### P3-E12 — Fig. 3 shows 14 HDBSCAN clusters; body claims 3
§III C body: "UMAP/HDBSCAN clustering of the top-50,000 cross-transfer anomalies yields **3** latent-space populations (Fig. 3)". Fig. 3 title text: "77,905 anomalies (score > 5.0), **14 clusters**, 99.4% clustered". Caption says "Two minority clusters (blue, orange)". Three numbers don't agree (3 vs 14 vs the 2+1 implied by the caption). Additionally, body says "top-50,000" but the figure scores 77,905. The figure cannot be both the body's claim and what's drawn.

### P3-E13 — Abstract claims "20 curated all-sky catalogs"; body lists 17
Abstract: "Extended archival cross-matching … against **20 curated all-sky catalogs** via CDS X-Match". §IV A parenthetical: "(Gaia DR3, SDSS DR12/DR16, DESI Legacy Imaging DR9, DES DR2, Pan-STARRS1, AllWISE, CatWISE2020, 2MASS, unWISE, GALEX, Chandra, 4XMM, NVSS, VLASS, USNO-B, UCAC5, APASS)". Counting commas yields **17** entries (or 18 if SDSS DR12 and DR16 are counted separately). The 17.8% novelty fraction headline is conditioned on the number of comparison catalogs, so this is a load-bearing discrepancy.

### P3-E14 — "265,000 catalog-grade subset" does not reproduce from the stated surveys
Abstract: "the recommended catalog-grade subset is **∼265,000** unique objects (DESI + SDSS + eROSITA + Gaia + NEOWISE)". Summing native+masked counts:

- DESI 195,829 + SDSS 77,905 + eROSITA 298 + Gaia 500 + NEOWISE 419 = **274,951**

Even after applying full proportional 5″ dedup compression (~2.6%), the result is ~267,700, not 265,000. The 265K figure is not derivable from the stated inputs. The paper centers the "recommended catalog-grade" recommendation on a number that doesn't reproduce.

### P3-E15 — Three incompatible fNL forecast methodologies are conflated as one
The paper presents at least three different forecast methods, all labeled as σ(fNL):

1. **§V Fisher form**: 1/σ² = 1/8.98² + 0.0747·α². At α=0.20 → σ = **8.06**, improvement 10.2%.
2. **Appendix C Table VII linear scaling** from α=0.15 fiducial. At α=0.20 → σ = **8.25**, improvement 8.1%.
3. **Appendix C Fig. 8 multi-tracer** with single-tracer baseline σ = **16.85**, dense limit σ = 11.71, baseline-multi σ = 12.72.

The §V Fisher form and Appendix C linear scaling give different σ at the same α (off by ~2.4% at α=0.20). The Fig. 8 single-tracer baseline (16.85) does not equal the §V single-tracer baseline (8.98) — they differ by a factor of ~1.9. The abstract's "7.9% improvement" is the Appendix C dense-vs-realistic-multi-tracer figure (12.72→11.71 = 7.94%), the σ=8.14 value is the §V single-tracer-augmented figure, and these are being presented as the same forecast. The paper is mixing forecasts on different baselines.

---

## MAJOR findings (new)

### P3-M14 — Fisher envelope [3.92, 8.98] uses α=0 as the upper bound
The "1σ envelope σ(fNL) ∈ [3.92, 8.98]" with αjk = 0.19 ± 0.65 has the upper end at α=0 (not α=-0.46), because 1/σ² = F₀ + cα² is even in α with global max at α=0. The 1σ interval on α is [-0.46, +0.84]; mapping this to σ via the Fisher form gives σ ∈ [3.92, 8.98] only if you take max σ over the interval (which lands at α=0, **outside** the prior on α's sign in a multi-tracer context where α=0 corresponds to no bias enhancement). The envelope as quoted obscures that the upper bound is at α=0 — the very null hypothesis being tested. A more honest envelope is asymmetric:

- σ at α=-0.46: 5.95
- σ at α=+0.19: 8.14
- σ at α=+0.84: 3.92

The current "envelope" includes the unphysical-for-this-test α=0 endpoint. This needs explicit treatment.

### P3-M15 — "5,384 QSO-candidate sample" never derived
§V opens "An empirical Landy–Szalay angular two-point analysis on the **full 5,384 QSO-candidate sample**". Nowhere in §III or §IV is a 5,384-object QSO-candidate subsample derived. The number appears with no provenance. (The DESI anomaly catalog contains 0.037% QSO-flagged anomalies = ~72 of 195,829; the high-z candidates discussed in §III B are 12; the gold+silver mentioned later is 1,122. None of these is 5,384.)

### P3-M16 — Section VI D shows only caveats (i)–(ii); references throughout cite (iii)–(v)
The body of §VI D in the manuscript contains exactly two labeled caveats: "(i) DESI in-sample training–test overlap" and "(ii) Injection-recovery synthesis". The text elsewhere cites "§VI D caveat (v)" (Table I footnote ‡ and §III E), "§VI D caveat (j)", "§VI D (f)", "§VI D (e)". These caveats are not present in the main-text Section VI D. Table IV has caveats labeled (a)–(j), but Table IV labels are not (i)–(v). The cross-references are broken or refer to material in the companion repository as if it were in the paper.

### P3-M17 — SDSS native re-score uses 1,925,279 spectra, not the 2,304,830 in Table I
Table I shows SDSS DR18 total = 2,304,830 spectra. Table I footnote ‡: "SDSS native re-score complete across **1,925,279** DR18 spectra". This is a 16.5% reduction (379,551 spectra) with no documented quality cut, no explanation, and no impact assessment on the published top-77,905 anomaly slice. If the cut removes 16.5% of the input pool, the rates reported in Table I (3.38%, etc.) are not on a common denominator with the cross-transfer rates.

### P3-M18 — Eq. 2 standardization cannot be uniform if eROSITA tops at S=1.08 while DESI reaches S=25.2
Eq. 2 defines S as per-survey z-scored validation residual: by construction the validation distribution has unit variance. The threshold "S > 5" corresponds to 5σ above the validation mean. The DESI catalog has scores reaching S=25.2 (5σ tail), but Table III shows eROSITA top-5 with maximum S = **1.084** (less than 1σ above the validation mean). If the standardization were really uniform, eROSITA's anomalies would not be anomalies in any normal sense. Either the eROSITA "S" is on a different scale than Eq. 2 (in which case the §II B "throughout this paper, S refers without exception to" statement is wrong), or the validation distribution is so heavy-tailed that 5σ-equivalents are <1σ on the standardized axis — which would invalidate the threshold interpretation across the paper.

### P3-M19 — Jaccard 0.70 PASS gate appears nowhere as a pre-registered threshold
The DESI 5-fold cross-validation reports "J̄ = 0.862 (≥ 0.70 gate, PASS)". The threshold 0.70 has no published reference, no pre-registration in any earlier version, and no statistical justification given. Choosing the gate threshold after observing the test statistic invalidates the gate. The same concern applies to the production-vs-control gate at "≥ 0.50, PASS" (J=0.732).

### P3-M20 — Fig. 8 multi-tracer baseline (16.85) contradicts §V baseline (8.98)
§V states "single-tracer DESI QSO baseline is σ(fNL)^std = 8.98". Fig. 8 caption: "dotted dark-red line marks the single-tracer baseline (σ(fNL) = 16.85)". These are nominally the same quantity computed on the same data and differ by a factor of 1.88. The paper does not flag, reconcile, or explain the discrepancy. Either the appendix forecast and the main-text forecast are on different sky/redshift coverage, or one of the numbers is stale from an earlier version.

---

## MINOR findings (new)

### P3-Mi12 — OOD sample size inconsistent (100k vs 103k)
§II B: "independent OOD validation on 100k unseen DESI spectra". §VI D (i): "independent 103,000-spectrum OOD holdout (seed 20,260,501)". Same test, two stated sizes.

### P3-Mi13 — MCMC diagnostics conflate ESS and 50τ-per-walker
Appendix E: "ESS ≈ 5,500 (> 50τ per walker, convergence satisfied)". These are two different convergence criteria. ESS ≈ 5,500 is total across all walkers (5,500/32 ≈ 172 per walker, which is just ~3τ per walker). The "50τ per walker" criterion is satisfied by the chain length (10,000 > 50·58 = 2,900), but that's a chain-length criterion, not an ESS criterion. The phrasing implies both are satisfied for the same reason; they're not.

### P3-Mi14 — "PASS" gate is plant-morphology-conditional
Fig. 7 caption admits the SDSS continuum-dip is 64% (PASS) while the emission-line plant is **7.2%** (effectively a complete fail), and LAMOST is 5.8% continuum-dip vs **0.6%** emission-line. The headline "PASS" for SDSS is conditioned on the plant choice; if the gate had been pre-registered with emission-line plants, both surveys would fail. The choice of plant morphology should have been pre-registered, not selected ex-post.

### P3-Mi15 — χ² p-value not stated explicitly
§IV B: "χ² = 143,936, dof = 38,329, χ²_ν = 3.76". The associated p-value is below machine precision but the paper does not say so. With χ²/dof = 3.76 at this many dof, this is ~330σ from the null — which underlines that the test is dominated by selection-function effects (as the paper notes), but the missing p-value would have made the absurdity transparent immediately.

### P3-Mi16 — "Gaussian-approximation" σ vs "asymmetric 68% CI" for NANOGrav choice
§V A uses ±0.382 (Gaussian-approximation std) to compute "+1.13σ" matter-bounce deviation. If the asymmetric upper-half quantile width (+0.291) is used instead — which is more appropriate when testing a value above the posterior mean (γ=3.0 > γ_post=2.567) — the deviation is (3.0−2.567)/0.291 = **+1.49σ**, not +1.13σ. The paper uses the larger (Gaussian) uncertainty to make the bounce prediction look more consistent than it is. The SMBHB +4.61σ figure has the same issue: with +0.291 upper width, SMBHB sits at (4.33−2.567)/0.291 = **+6.06σ**. Pick a consistent uncertainty and recompute.

### P3-Mi17 — Reference list mixes year conventions
Reference [33] embeds an inline editorial comment ("[publication-year 2024; bibkey label retained as Heinrich2023 for arXiv-submission-year continuity]") in the bibliography. This is internal versioning leakage. Already noted in initial review (P3-Mi3) but flagging that the comment also reveals the paper carries forward a citation key from a prior version — the manuscript has been substantially revised, and other "stale numbers" in the body (P3-M20, P3-A14) are consistent with incomplete revision.

---

## NIT findings (new)

### P3-N3 — "Path-C" used as adjective, noun, and version label without definition
"Path-C rebuild", "Path-C unique", "Path-C-compliant", "Path-C-final", "Path-C protocol", "Path-C native retrains", "Path-C systematics mask". Across 20 pages, "Path-C" appears ~60 times and is never explicitly defined as anything other than "the retraining pass we did". A reader unfamiliar with the project's internal naming has no anchor.

### P3-N4 — eROSITA Table III "SBigAE 1.084" with "S > 0.259" cut
The published catalog cut "S > 0.259" admits all 298 sources; the table shows top-5 with S_BigAE down to 0.439 (rank 5). If 298 sources span S ∈ [0.259, 1.084], the catalog is a very compressed score-knee tail — but the §III E text frames the 1.084 top object as a striking outlier. The dynamic range is small; "top anomaly" framing is misleading.

### P3-N5 — TIC 374313355 — coordinates not given
The cross-survey "discovery" target TIC 374313355 has no RA/Dec listed in the body, only the TIC ID. PRD readers cannot independently look up this object without coordinates.

---

## Summary of new findings vs initial review

The initial review focused on structural issues (cosmology venue, gate-failure publication, internal naming). This pass found **5 additional ESSENTIAL issues** (3 of which are arithmetic non-reproductions of headline numbers: 58.8%, 20 catalogs, 265K subset), **7 additional MAJOR issues** (broken cross-references, missing derivations, inconsistent baselines across the same forecast), and **6 additional MINOR/NIT issues**. The two-pass total is roughly **30+ distinct issues** for a 20-page submission.

The new arithmetic findings (P3-E11–E15, P3-M14, P3-M17, P3-M20, P3-Mi16) collectively indicate that the manuscript has been revised across multiple iterations without reconciling numbers between sections. Several headline figures in the abstract are not derivable from the body, and at least three separate fNL forecast methodologies are presented as a single result.

**Recommendation stands: REJECT.** A revision would require not just a response to individual findings but a full numerical reconciliation pass across abstract, tables, figures, main text, and appendices.