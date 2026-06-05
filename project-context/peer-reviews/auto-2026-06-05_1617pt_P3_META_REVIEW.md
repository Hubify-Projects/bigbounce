# P3 auto-2026-06-05_1617pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 275.5s

---

Meta-Referee report on “Spectrally Unusual Sources at Scale: A Multi‑Survey Catalog of 378,280 Path‑C Unique Anomalies …”

Below are issues that, to the best of my audit, none of the five prior referees identified. I focus on end‑to‑end derivation integrity, hidden conditioning, selection consistency, and cross‑reference/units pitfalls.

P3-META-E1
- Severity: ESSENTIAL
- Section + page: §II.D Step 5 (p.3), Fig. 7 (p.13), and throughout
- Why others missed it: Reviewers focused on listed PASS/FAIL gates but did not notice which survey is absent.
- Specific problem: The injection–recovery gate is reported for SDSS, LAMOST, eROSITA, Planck, Gaia, and NEOWISE only: “Results: 3 PASS (SDSS 64%, Planck 100%, NEOWISE 100%) and 3 FAIL-with-diagnostic (LAMOST 5.8%, Gaia 5.2%, eROSITA 1.2%) at 5σ.” DESI – the anchor survey supplying most anomalies and several headline claims – has no injection–recovery result shown anywhere (not in §II.D, not in Fig. 7, not in §III A).
- Required fix: Run and report a DESI injection–recovery test using the same plant families (continuum‑dip and emission‑line), at the catalog’s operative threshold (S>5), and state the 5σ recovery fraction with uncertainties. If infeasible, explicitly acknowledge the omission and downgrade DESI‑based claims that depend on completeness/sensitivity.

P3-META-E2
- Severity: ESSENTIAL
- Section + page: §V A (p.11), Appendix E (pp.16–17)
- Why others missed it: Prior reports questioned comparability to NANOGrav and model‑space omission but not the validity of the Savage–Dickey computation itself.
- Specific problem: The paper claims “Proper Savage‑Dickey Bayes factors against the γ‑uniform prior yield B_MB/free = 3.23 and B_SMBHB/free = 4.52×10^−4; hence B_MB/SMBHB = 7.14×10^3.” Savage–Dickey applies only to nested models under the same prior measure for the common parameters. Here, the “free‑spectrum” KDE object is a high‑dimensional binned model; the 2‑parameter power‑law templates (MB and SMBHB) are not nested within it under a common parameterization and prior. Moreover, the KDE file is a likelihood-like product, not a posterior with an explicit prior as required for Savage–Dickey.
- Required fix: Remove the Savage–Dickey Bayes factors or replace them with proper evidence ratios computed from a consistent likelihood and priors (e.g., nested sampling on the same PTA likelihood for each model) and report evidences and Bayes factors with prior definitions. If kept as an illustrative calculation, explicitly state it is not a valid Savage–Dickey application and do not present the numbers as Bayes factors.

P3-META-E3
- Severity: ESSENTIAL
- Section + page: §II.D Step 1 (p.3)
- Why others missed it: They criticized that Planck fails criterion (a) but did not question the criterion’s cross‑domain meaning.
- Specific problem: The gate “validation loss ≤ 0.30 after ≤ 100 epochs” is applied uniformly across spectroscopic spectra, tabular photometry, and CMB patches. Raw MSE magnitudes depend on feature scaling and domain (e.g., 4096‑pixel images vs 15‑feature catalogs). A fixed 0.30 MSE threshold is not dimensionless or comparable across these inputs and renders PASS/FAIL against criterion (a) meaningless.
- Required fix: Redefine the gate in scale‑free terms (e.g., validation MSE z‑score relative to a baseline, relative improvement over an identity/mean predictor, or percentile vs a null) and re‑evaluate PASS/FAIL for each survey under that unified, dimensionless criterion. Alternatively, set per‑domain gates justified by standardized, pre‑declared feature scaling.

P3-META-E4
- Severity: ESSENTIAL
- Section + page: §II.A–B (p.2), §III E–H (pp.6–8)
- Why others missed it: They assumed standard practice without checking it is stated.
- Specific problem: For tabular surveys (eROSITA 47 features, Gaia 20, NEOWISE 15), the paper minimizes an unweighted per‑element MSE but never states that inputs are standardized (zero‑mean, unit‑variance) per feature. Without explicit per‑feature normalization, large‑variance features dominate the loss and the anomaly score S, making the eROSITA/Gaia/NEOWISE rankings ill‑defined and unreproducible.
- Required fix: Specify the exact feature preprocessing for each tabular survey (centering, scaling, clipping, winsorization) and confirm BigAE was trained on standardized inputs. If not standardized, re‑train with standardization and update anomaly rankings and thresholds.

P3-META-M1
- Severity: MAJOR
- Section + page: §II.D Step 6 (p.3), §IV C (p.10)
- Why others missed it: They focused on mixing patches vs point sources, not on the positional‑error model.
- Specific problem: A fixed 5″ friends‑of‑friends matching radius is used for all surveys during 7‑way deduplication. This under‑merges catalogs with larger and heterogeneous astrometric uncertainties (e.g., eROSITA X‑ray positions frequently >5″) and over‑merges those with very small errors. The result biases downward the multi‑survey coincidence count (637) and inflates the “unique object” total.
- Required fix: Adopt survey‑specific (or per‑source) positional‑uncertainty models and use a probabilistic cross‑match (e.g., Bayesian or likelihood‑ratio) or variable matching radii. Provide a sensitivity analysis showing how the number of multi‑survey clusters and the deduplicated count change with more realistic match criteria.

P3-META-M2
- Severity: MAJOR
- Section + page: §IV D (p.10) and Appendix F (pp.16–18)
- Why others missed it: They flagged over‑interpretation but not the geometric triviality and quarantine dependence.
- Specific problem: The Planck×ACT “null cross‑correlation” is drawn using ACT anomalies from a checkpoint that “fails both gate criteria” (Appendix F) and, by the paper’s own description, the two anomaly sets concentrate on largely disjoint sky regions (south ecliptic pole vs Galactic plane). A null overlap under disjoint footprints is tautological and provides no information about shared physics or systematics.
- Required fix: If this result is retained, restrict to the common sky footprint with a joint mask, characterize the expected random overlap under that mask, and repeat the test using a validated ACT anomaly set (native retrain). Otherwise, remove the cross‑correlation claim.

P3-META-M3
- Severity: MAJOR
- Section + page: §IV A (p.9: “b. Expected false‑match rates”) and §III A (p.4)
- Why others missed it: They checked the 460 all‑catalog expectation but not the top‑10k sub-sample consistency.
- Specific problem: The SIMBAD 5″ false‑match rate is estimated as P_false ≈ 2.36×10^−3 per source. On the quoted top‑10,000 DESI anomalies, the expected number of random SIMBAD matches is ~24; the observed is “0.2%” = 20. Thus the observed SIMBAD matches in the top‑10k are consistent with pure chance; the paper nonetheless uses “only 0.2% in SIMBAD” rhetorically to suggest unmatched novelty.
- Required fix: State explicitly that the SIMBAD matches in the top‑10k are consistent with random coincidence at 5″ and should not be treated as astrophysical identifications. Either reduce the match radius or add multi‑catalog/photometric confirmation to validate true matches in that subset.

P3-META-M4
- Severity: MAJOR
- Section + page: §II.D Step 4–5 (p.3), §III H (p.8), Fig. 7 caption (p.13)
- Why others missed it: They noticed missing curves in Fig. 7 but not the heterogeneity of what “injection” means.
- Specific problem: NEOWISE’s reported “1000/1000 = 100% (gate PASS)” is not a signal‑injection recovery; it is a mask‑toggling test of an ecliptic‑latitude cut (“ecliptic‑pole mask”). This is not comparable to the spectral/photometric signal‑injection gates used elsewhere and defeats the purpose of a unified sensitivity gate.
- Required fix: Replace the NEOWISE mask toggle with a true feature‑space injection test (e.g., W1/W2 color or flux perturbations) evaluated against the same anomaly threshold; report recovery vs amplitude and re‑evaluate PASS/FAIL consistently across surveys.

P3-META-m1
- Severity: MINOR
- Section + page: §IV C, Fig. 6 panels (a,b) and surrounding text (pp.10–11)
- Why others missed it: They flagged that the example is below anomaly threshold; they did not flag the logical implication for the text’s claim.
- Specific problem: The paper calls the three pairs “the highest‑confidence cross‑survey detections.” Match 1 is not an anomaly in either survey (scores 3.2 and 2.8), so by the paper’s own definition it is not part of the anomaly catalog and should not be presented as a “cross‑survey detection” in that context.
- Required fix: Remove Match 1 from the “highest‑confidence cross‑survey detections” list or explicitly relabel it as a non‑anomalous cross‑match shown only as a reconstruction sanity check.

P3-META-m2
- Severity: MINOR
- Section + page: §III A (p.4), §IV A (p.9)
- Why others missed it: They focused on aggregate novelty fractions rather than the internal logic of the claim.
- Specific problem: The text leverages the “0.2% in SIMBAD” for the top 10k DESI anomalies to imply exceptional novelty, while also computing a random‑match expectation that essentially equals the observed match count. The narrative should not imply that “few SIMBAD matches” is evidence of discovery when it matches the null.
- Required fix: Rephrase the novelty discussion for the top‑10k to emphasize that SIMBAD non‑matches there are expected given survey coverage and the chosen match radius; defer genuine novelty discussion to the multi‑catalog (CDS X‑Match) analysis only.

## Meta-review recommendation
REJECT

## Rationale and confidence
Across the union of six reviews, I count well over a dozen independent ESSENTIAL/MAJOR blockers: unresolved figure references; inconsistent and sometimes dimensionally erroneous Fisher formulations; contradictory σ(fNL) baselines and improvements; opaque “catalog-grade subset” accounting; implausible training times; HEALPix/pixel‑count/doF mismatch; “20 catalogs” vs. an 18‑item list; cross‑survey examples below threshold; threshold heterogeneity; and now, additionally, the lack of any DESI injection–recovery test, a non‑applicable Savage–Dickey calculation, a domain‑dependent gate applied as a universal MSE cutoff, a fixed 5″ dedup radius ignoring survey‑specific astrometry, and a NEOWISE “injection” that is actually a mask toggle. Given this blocker set and the breadth of corrections required (methodological, statistical, and editorial), I have low confidence the present manuscript would survive external peer review without a substantial, method‑level revision and re‑analysis.