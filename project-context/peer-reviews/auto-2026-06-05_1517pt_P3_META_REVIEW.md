# P3 auto-2026-06-05_1517pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 553.7s

---

Meta-referee report — new issues not caught by the five prior reviewers

P3-META-E1
- Severity: ESSENTIAL
- Location: Sec. II.D Step 6 (p. 3) and Sec. IV.C (p. 9–10)
- Why others missed it: Prior reviews discussed duplicate-handling and random-coincidence estimates but did not address epoch-dependent astrometry.
- Problem: The 7-way deduplication and the “genuine novelty” cross-matches use a fixed 3–5″ radius without any proper-motion correction across decades-separated surveys (SDSS: ~2000s; Gaia/NEOWISE: 2010s–2020s; DESI: 2020s). High–proper-motion sources can move >5″ over these baselines, inflating the “unique-object” count and the “novelty” rate (missed matches) and depressing the multi-survey coincidence count.
- Required fix: Recompute deduplication and archival cross-matches with epoch-aware positions (Gaia proper motions propagated to the relevant epochs) and use catalog-appropriate radii. Quantify how many “unique” objects merge under PM-aware matching and update the 378,280 and 17.8% figures accordingly (with uncertainties).

P3-META-E2
- Severity: ESSENTIAL
- Location: Sec. IV.D (p. 10) vs. Appendix F (p. 16–18)
- Why others missed it: Reviews flagged over-generalization and lack of a quantitative test but not the footprint contradiction.
- Problem: The paper asserts “ACT anomalies concentrate along the Galactic plane” to motivate a null Planck×ACT cross-correlation. This is inconsistent with ACT DR6’s sky footprint (which does not generally cover the Galactic plane) and contradicts the manuscript’s own example ACT anomaly at (l, b) ≈ (277°, +21°) in Appendix F. The claim is thus both footprint-inconsistent and internally contradictory.
- Required fix: Correct the sky-coverage statement. Show the actual ACT anomaly sky histogram against the ACT DR6 footprint/mask and provide a quantitative overlap test (metric, null, p-value). Remove the “Galactic plane contamination” rationale unless supported by ACT coverage/masks.

P3-META-E3
- Severity: ESSENTIAL
- Location: Sec. III.F (p. 6) and Table V (p. 15)
- Why others missed it: Reviewers questioned timing and score scales but not sample independence.
- Problem: Potential training/test leakage for Planck CMB. The model is “trained on 2×10^5 galactic-plane-masked SMICA patches,” while “Input: 20,000 SMICA patches” are scored, with no statement that these 20,000 are strictly disjoint from the 200,000 training patches (in sky location and random seeds). Overlap would bias reconstruction errors and the 100% injection-recovery at 5σ.
- Required fix: Document the tiling/patch-indexing and enforce disjoint training/validation/test splits at the HEALPix-pixel/patch level. If leakage occurred, re-train/evaluate with disjoint sets and update the Planck anomaly list and gate status.

P3-META-M1
- Severity: MAJOR
- Location: Sec. II.B (p. 2) and Sec. III.B (p. 5)
- Why others missed it: Several reviews noted undefined per-band scores but not the normalization bias.
- Problem: The per-band residuals rB, rR, rZ are “computed over the blue/red/NIR subsets” but no formula specifies whether each is normalized by the number of bins in that arm. The three DESI arms span unequal wavelength ranges (and, after downsampling to 496 features, unequal numbers of bins). Without per-arm normalization, “band dominance” is biased by arm length.
- Required fix: Provide explicit definitions, e.g., rB = (1/NB)∑(x−x̂)^2 over blue-arm bins, etc., and confirm the dominance classification is invariant to arm length. If not, recompute per-arm scores with proper normalization and update counts that rely on rB/rR/rZ comparisons.

P3-META-M2
- Severity: MAJOR
- Location: Sec. IV.A “Archival cross-match…” (p. 9)
- Why others missed it: Prior reviews questioned run details but not coverage conditioning.
- Problem: The “20 curated all-sky catalogs” list includes several that are not all-sky (e.g., NVSS, VLASS, Chandra, 4XMM) or have strong footprint/selection heterogeneity. A flat 5″ cone search across these catalogs without accounting for coverage/footprint and survey depth can overstate “genuine novelty” (absent because it’s off-footprint is not “novel”).
- Required fix: For each catalog, apply a mask for sky coverage and depth (where applicable) and compute novelty conditional on coverage. Report the 17.8% figure with coverage-corrected denominators and per-catalog radii; provide sensitivity to the match radius and footprint masks.

P3-META-M3
- Severity: MAJOR
- Location: Sec. II.A–B (p. 2) vs. Fig. 6 captions (p. 11)
- Why others missed it: Reviews flagged missing feature scaling for catalogs, but not spectral flux normalization.
- Problem: Spectral preprocessing for DESI/SDSS/LAMOST lacks a stated flux normalization scheme (continuum scaling, per-arm throughput correction, variance normalization). Yet Fig. 6 shows “Norm. flux,” implying unreported preprocessing steps that materially affect MSE and thus S.
- Required fix: Document the full spectral preprocessing pipeline (continuum normalization, per-arm scaling, variance weighting, clipping) with equations and release the scalers. Reassess that S thresholds and cross-survey comparisons are invariant to these choices.

P3-META-M4
- Severity: MAJOR
- Location: Sec. IV.A (p. 9), list of catalogs
- Why others missed it: Focus was on methodology and arithmetic, not catalog versioning.
- Problem: The CDS X-Match set includes “SDSS DR12/DR16” for archival identification, while the anomalies partly come from SDSS DR18. Using older SDSS releases misses later identifications and can inflate the “novelty” fraction.
- Required fix: Repeat the archival cross-match against the latest available SDSS photometric/spectroscopic releases (DR18/DR19 as appropriate) and update the 82.2% identification / 17.8% novelty figures accordingly.

P3-META-M5
- Severity: MAJOR
- Location: Sec. IV.A (p. 9)
- Why others missed it: They asked for parameters but not catalog-appropriate radii.
- Problem: A single 5″ match radius is inappropriate for several catalogs listed (e.g., NVSS beam ≈45″; VLASS ≈2.5″ synthesized beam; Chandra sub-arcsec). Under-sized radii for large-beam catalogs will undercount matches and inflate “novelty.”
- Required fix: Use catalog-appropriate radii (or likelihood-ratio matching) per survey and report novelty as a function of radius choice. Provide a table of radii and positional error models used for each catalog in the 20-catalog set.

P3-META-m1
- Severity: MINOR
- Location: Sec. II.A (p. 2)
- Why others missed it: They did not inspect the implied binning across arms.
- Problem: Input dimension is 496 for “three-arm spectra downsampled by a factor of 16,” yet no arm-wise bin counts are given. Because the arm wavelength ranges are unequal, the mapping from wavelength to 496 bins and the partition into (B,R,Z) subsets (for rB,rR,rZ) is under-specified and not reproducible.
- Required fix: Specify the exact per-arm bin counts after downsampling (NB, NR, NZ) and the wavelength edges used to construct the 496-dimensional vector so that per-arm MSEs can be reproduced.

P3-META-m2
- Severity: MINOR
- Location: Sec. IV.A (p. 9), “Expected false-match rates”
- Why others missed it: They focused on arithmetic correctness, not modeling assumptions.
- Problem: The SIMBAD false-match estimate assumes a uniform sky density nSIMBAD ≈ 3.0×10^−5 arcsec^−2. This ignores large spatial gradients in SIMBAD density (e.g., Galactic plane, survey footprints), so the quoted 0.24% expected false-match rate for DESI could be significantly biased.
- Required fix: Recompute false-match expectations with a spatially varying n(α,δ) (e.g., HEALPix-binned densities) and report a range or uncertainty on the expected false-match count.

P3-META-m3
- Severity: MINOR
- Location: Sec. III.H and Step 4 of Sec. II.D (pp. 8 and 3)
- Why others missed it: They accepted the mask wording at face value.
- Problem: The NEOWISE “mask injection-recovery: 1000/1000 = 100% (gate PASS)” conflates a geometry cut with an anomaly-detection injection test. No source-level signal is injected; passing this “injection-recovery” is tautological and not comparable to other surveys’ source-injection gates.
- Required fix: Relabel the NEOWISE test as a systematics-geometry validation rather than injection-recovery, and do not count it as a PASS of the same gate applied to DESI/SDSS/LAMOST. If a true source-injection test exists for NEOWISE, report it separately.

## Meta-review recommendation
REJECT

Given the union of all six reviews, there are multiple independent essential errors and inconsistencies touching the core headline metrics (novelty fraction methodology and coverage conditioning), the cross-survey CMB interpretation (ACT footprint contradiction), potential training/test leakage in the Planck tier, and incomplete or biased definitions for per-band scoring and deduplication across time-variable astrometry. The blocker count is high (≥10 essential/major issues across the reviews), and several require re-analysis rather than editorial fixes. My confidence that the current manuscript would survive external peer review outside the authors’ ecosystem is low; it needs a substantial methodological overhaul, clarified and reproducible cross-matching/coverage handling, and removal or rewriting of several claims before resubmission (likely to a data/methods journal rather than PRD).