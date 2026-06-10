# P3 auto-2026-06-08_1144pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 445.8s

---

Meta-referee report on “Spectrally Unusual Sources at Scale: …”

Goal of this meta-review
I identify issues that none of the five prior referees flagged. Each item highlights a blind spot that is systematically easy to miss (derivation-chain consistency, cross-reference contradictions, hidden conditioning, etc.).

P3-META-E1
- Severity: ESSENTIAL
- Location: Sec. II.B (pp. 2–3), Fig. 2 caption (p. 5), Sec. III.C (p. 5)
- Why others missed it: Several reviewers noted score-scale heterogeneity, but none checked the internal definition of S against its use in cross-transfer.
- Problem: Contradictory definition of the anomaly score S for cross-transfer cases. The paper defines S(x) “throughout” as z-scored MSE using μval, σval from “that survey’s training pool” (Eq. 2), but SDSS DR18 cross-transfer scores are produced with a DESI-trained BigAE that, by construction, has no “SDSS training pool” (the validation statistics are DESI’s). Text: “Throughout this paper, ‘S’ refers… where μval and σval are the mean and standard deviation of MSE on the held-out 20% validation split of that survey’s training pool.” Yet the SDSS cross-transfer panel (Fig. 2 right) and Sec. III.C rely on S from a DESI-trained model applied to SDSS. This violates the stated per-survey definition and makes “z-units” ambiguous for cross-transfer.
- Required fix: Define two score conventions explicitly: Snative(survey) with μval, σval from the survey’s own native training split, and Sxfer(source→target) with μval, σval from the source model. Label every figure/table accordingly and never call Sxfer “per-survey z-units.” Provide the exact μval, σval used for each cross-transfer result.

P3-META-E2
- Severity: ESSENTIAL
- Location: Sec. IV.D (p. 10), Appendix F (pp. 16–18)
- Why others missed it: Prior reports focused on ACT’s methodological quarantine; none examined the masking/footprint conditioning of the cross-correlation itself.
- Problem: Planck×ACT “null cross-correlation” appears to be computed without restricting to (and weighting by) the sky intersection of the two footprints and their masks. The text itself notes that Planck anomalies concentrate near the south ecliptic pole while ACT anomalies concentrate along the Galactic plane, implying minimal overlap, yet draws a scientific inference from the null. Without performing the cross-correlation strictly within the ACT footprint with matched masks (and showing the effective area), the null is dominated by non-overlap, not physics.
- Required fix: Recompute the cross-correlation only over the ACT DR6 footprint and masks (or drop the analysis). Report the common-area sky fraction, apply identical apodized masks, and quote a null derived from randoms that respect both surveys’ window functions. Make clear this is a footprint-conditioned diagnostic only.

P3-META-E3
- Severity: ESSENTIAL
- Location: Sec. IV.A, paragraph “Archival cross-match and genuine novelty fraction” (p. 9)
- Why others missed it: Reviewers challenged generalization of the 17.8% point estimate but did not count the catalog list.
- Problem: “20 curated all-sky catalogs” are claimed, but only 17–18 are actually listed: Gaia DR3; SDSS DR12/DR16 (ambiguous if counted as one or two); DESI Legacy Imaging DR9; DES DR2; Pan-STARRS1; AllWISE; CatWISE2020; 2MASS; unWISE; GALEX; Chandra; 4XMM; NVSS; VLASS; USNO-B; UCAC5; APASS. The stated “20” is not matched by the explicit enumeration.
- Required fix: Provide the exact list with a count that matches “20.” If some catalogs are combined (e.g., SDSS DR12 and DR16) or additional catalogs were used but not listed, enumerate them; otherwise correct “20” to the true number.

P3-META-E4
- Severity: MAJOR
- Location: Sec. II.D Step 1 (p. 3) vs. Sec. II.B (p. 2) and Sec. III.A (pp. 4–5)
- Why others missed it: Timing/throughput inconsistencies were flagged, but not the training-set-size contradiction baked into the protocol text.
- Problem: The Path-C Step 1 statement says “A fresh BigAE is trained on a 2–5×10^5-spectrum … subset of each survey’s own data.” This contradicts Sec. II.B and Sec. III.A, which repeatedly state DESI is trained on 47,000 spectra. The “for each survey” language is thus incorrect at least for DESI and possibly others.
- Required fix: Provide a table of actual training-set sizes per survey and change the Step-1 description to reflect reality (e.g., “2–5×10^5 for SDSS/LAMOST; 4.7×10^4 for DESI”). Ensure all reported validation μval, σval values are tied to the correct training pools.

P3-META-M5
- Severity: MAJOR
- Location: Sec. II.D Step 6 (p. 3), Sec. IV.C (p. 10)
- Why others missed it: Deduplication arithmetic was checked; the graph-theoretic implication of FoF linking was not.
- Problem: Friends-of-friends (union-find) at 5″ can bridge multiple near-threshold pairs across different surveys, creating clusters whose diameter greatly exceeds 5″. This can spuriously merge neighboring distinct sources and inflate “multi-survey coincidences” (637). No maximum pairwise separation per cluster, per-survey offset distribution, or robustness-to-bridging test is reported.
- Required fix: Report the maximum and median intra-cluster separations and the per-survey positional offsets within clusters; add a sensitivity test using connected-components constrained by a maximum cluster diameter (e.g., requiring all pairwise distances ≤ 5″, not just single-link edges). Alternatively use a weighted bipartite match per pair and prevent multi-edge percolation.

P3-META-M6
- Severity: MAJOR
- Location: Sec. IV.C (p. 10)
- Why others missed it: The total dedup compression was validated, but the large intra-survey-duplicate count was not interrogated.
- Problem: “637 multi-survey coincidences + 9,576 intra-survey duplicates = 10,213 total collapsed.” The paper never explains the origin or survey breakdown of the 9,576 intra-survey duplicates, which is surprising given DESI uses coadds and the other catalogs are supposedly source-level. Without a breakdown, it is unclear whether these are genuine repeat observations, pipeline deblends, or bookkeeping errors.
- Required fix: Provide a per-survey breakdown of intra-survey duplicates, with causes (repeat spectra, multi-epoch catalog entries, tile overlaps, artifact flags), and quantify how many unique astrophysical objects they represent pre/post deduplication.

P3-META-M7
- Severity: MAJOR
- Location: Sec. IV.A (p. 9)
- Why others missed it: Reviewers questioned generalization of the 17.8% novelty rate but not the appropriateness of a uniform 5″ cone for all catalogs.
- Problem: The “20-catalog” cross-match uniformly uses a 5″ cone for all archives, including radio surveys (NVSS, VLASS) and X-ray (Chandra, 4XMM), where positional uncertainties and true multi-wavelength offsets can exceed 5″ or be systematically offset from optical centroids. Using 5″ for all inputs risks inflating the “absent from all major catalogs” fraction.
- Required fix: Redo the multi-catalog match with catalog-appropriate radii (e.g., 10–15″ for NVSS; PSF-matched likelihood ratio for radio/IR morphologies; off-nucleus AGN/ULX handling in X-ray), or explicitly state the catalogs for which 5″ is inappropriate and exclude them from the 17.8% claim. Provide a sensitivity analysis showing how the novelty fraction changes with radius per catalog.

P3-META-M8
- Severity: MINOR
- Location: Sec. II.B (p. 2), Sec. III.B (p. 5), Appendix D (p. 16)
- Why others missed it: UMAP taxonomy was discussed, but its stability diagnostics were not tied to its later usage as a “family” label.
- Problem: Appendix D concedes that “kNN-preservation and cross-seed Spearman FAIL as expected for sparse high-dimensional outlier clouds,” yet the same UMAP/HDBSCAN embeddings are used to define ten astrophysical “families.” If neighborhood preservation is unstable across seeds, the taxonomy is not reproducible at the family level.
- Required fix: Either (i) demonstrate that family assignments are stable across seeds (e.g., adjusted Rand index across runs), or (ii) reframe the taxonomy as illustrative rather than catalog-grade, and avoid using it to support quantitative family counts in the main text.

P3-META-m9
- Severity: MINOR
- Location: Sec. IV.B (p. 10)
- Why others missed it: HEALPix dof mismatch was noted by one reviewer, but not the implicit assumption behind the χ2 test statistic construction.
- Problem: The χ2 uniformity test uses counts over “38,330 HEALPix pixels (Nside = 64)” with dof set equal to the number of populated pixels minus one, but without stating the expected counts per pixel or rescaling for the highly non-uniform selection function. Reporting χ2ν = 3.76 without an explicit expected vector per pixel (by survey footprint) renders the statistic largely uninterpretable.
- Required fix: Either replace the χ2 with a footprint-weighted test (simulate expected counts per pixel given each survey’s targeting map and area coverage) or remove the χ2ν value and keep only the non-correlation claims (Galactic latitude, dust), which are less sensitive to footprint modeling.

P3-META-m10
- Severity: MINOR
- Location: Sec. III.B (p. 5), Fig. 9 caption (p. 17)
- Why others missed it: Others flagged the “AE” label mismatch; none noted the contradictory explanation across sections.
- Problem: Sec. III.B says “Panel labels report the per-arm Z-arm sub-score rZ (printed as ‘AE’ for legacy compatibility).” In Fig. 9 the “AE” values span 10^3–10^5, which cannot be the z-scored rZ ~ O(1–10). This is not just a label mismatch; the explanatory sentence itself is wrong.
- Required fix: Correct the statement in Sec. III.B to match the plotted quantity (e.g., raw per-arm residual sum), and do not refer to it as rZ. If rZ is important, replot using the true rZ with an appropriate scale.

P3-META-n11
- Severity: NIT
- Location: Sec. II.C (pp. 3–4), Sec. III.F (p. 6), Table V (p. 15)
- Why others missed it: Several flagged implausible train times; none pointed out the unresolved inconsistency between the <10 s “GPU time” claim and the listed inference throughputs across patch counts.
- Problem: The claim “The CMB and photometric surveys each required < 10 seconds of GPU time” cannot simultaneously hold for eROSITA (930,203 sources at 122k/s ≈ 7.6 s) and Gaia (50,000 at 40k/s ≈ 1.25 s) and Planck (20,000 patches at 8,000/s ≈ 2.5 s) unless this excludes data I/O and CPU preprocessing; the text does not say so here, whereas it does elsewhere for other timing claims.
- Required fix: Add an explicit statement in Sec. II.C that “GPU time” here refers to forward inference time only (excludes I/O/preprocessing), listing the per-survey measured GPU-forward time and wall-clock time to prevent misinterpretation.

Meta-review recommendation
MAJOR REVISIONS

Rationale: In addition to the substantial issues raised by the five prior referees, the items above expose (i) a definitional inconsistency in the anomaly score under cross-transfer, (ii) a footprint-conditioning flaw in the Planck×ACT “null,” (iii) a miscount in the “20-catalog” novelty audit, (iv) a protocol-text contradiction on training set sizes, (v) an untested risk of FoF bridging in the 5″ dedup that can merge distinct sources, and (vi) a uniform 5″ cross-match radius that likely biases the 17.8% novelty figure for radio/X-ray catalogs. These points affect headline claims (novelty fraction, cross-survey coincidences, and methods validity) and must be fixed.

Given the union of all six reviews, I count at least 8–10 essential or major blockers (Fisher-forecast constant/units; SDSS “top-1%” mislabeling; unresolved figure references; data/code availability; Planck×ACT misuse and masking; timing/training inconsistencies; novelty aggregation math; thresholds taxonomy and S definition; dedup bridging; catalog-list miscount; radius choice in cross-matching). My confidence that the paper would survive external PRD peer review after thorough revision is moderate: the data product is potentially valuable, but the manuscript needs a comprehensive consistency pass, clearer, pre-registered methods, and a more conservative presentation of cosmological “applications.”