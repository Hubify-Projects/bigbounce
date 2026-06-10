# P3 R26conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 636.8s

---

Meta-review for PRD submission “Spectrally Unusual Sources at Scale …”

Goal of this meta-review
I read the rendered PDF and all five prior referee reports. Below I list issues that, to the best of my reading, none of the five reviewers caught. I focus on subtle but consequential problems: end‑to‑end chain integrity, cross-reference logic, hidden conditioning, and missing methodological specifics that affect reproducibility.

NEW findings (not raised by the 5 prior referees)

P3-META-E1
- Severity: ESSENTIAL
- Location: §II.A (p.2) and throughout photometric/catalog survey sections (§III.E–H)
- Why others missed it: Most reviews focused on DESI/SDSS spectroscopy and Planck; feature scaling for tabular surveys wasn’t scrutinized.
- Problem: The paper never specifies how per‑feature scaling/normalization was handled for the catalog/photometric inputs (eROSITA 47 features, Gaia 20, NEOWISE 15). With an unweighted MSE loss (Eq. 1), feature scales dominate the anomaly score unless all columns are standardized. The text only says “input dimension matches the number of catalog features” and, for spectra, mentions a “common normalized input scale,” but no analogous statement (or recipe) exists for eROSITA/Gaia/NEOWISE. Without explicit scaling and imputation rules (z-score? robust-z? min–max? log transforms? one‑hot for flags? NaN handling?), both the training and the reported S values are irreproducible and potentially biased by arbitrary units.
- Required fix: Add a precise, per-survey preprocessing specification for all tabular features: transforms (log/ln), centering, variance scaling (global vs split), robust outlier handling, treatment of missing/flagged values, and any one‑hot encoding. Provide a pointer to code/DOI and a CSV schema enumerating feature names and transforms.

P3-META-E2
- Severity: ESSENTIAL
- Location: §IV.C “Friends-of-friends chain audit” (p.12) vs. earlier dedup summary on the same page
- Why others missed it: The numbers look plausible at a glance but are not reconciled explicitly.
- Problem (cross-reference inconsistency): Two different dedup summaries coexist without a tying identity:
  • “637 multi-survey coincidences … 637 multi-survey clusters + 9,576 intra-survey duplicates = 10,213 total collapsed”
  • “across all 9,553 clusters with ≥ 2 members … max pairwise separation 4.999″”
  The text never states how 9,553 relates to “637 multi-survey clusters” and to “9,576 intra-survey duplicates.” Are the 9,553 clusters the total number of multi-member clusters (multi-survey + intra-survey)? If so, how many of the 9,553 are intra‑survey clusters? Presently the reader cannot reconcile “duplicates” (a count of removed entries) with “clusters” (a count of groups).
- Required fix: Provide a single, consistent cluster accounting table: number of multi-member clusters, split into multi-survey vs intra‑survey clusters; size distribution (N=2,3,…), and show that Σ(size−1) over all clusters equals 10,213. This resolves the 9,553 vs (637, 9,576) ambiguity.

P3-META-E3
- Severity: ESSENTIAL
- Location: §III.F (p.9) and Table V footnote (p.20)
- Why others missed it: Prior reviews flagged the Planck “top‑1%” inconsistency but not the interaction between per‑patch standardization and the injection test.
- Problem (hidden conditioning): Planck patches are per‑patch standardized (subtract mean; divide by per‑patch std) before scoring. The injection‑recovery test reports 100% recovery at “5σ Gaussian-bump amplitude,” but the paper doesn’t state whether σ refers to the pre‑standardization noise or the post‑injection, post‑standardization residual variance. Because standardization renormalizes each patch, the effective amplitude (in the network’s input units) depends on whether the std is computed before or after planting. This conditioning can artificially boost recovery rates (especially for small patches where a localized bump barely changes std) or, conversely, dampen them if std is recomputed after the plant.
- Required fix: Specify exactly when σ is measured and when standardization is applied (before/after injection), and report recovery fractions under both conventions to demonstrate robustness. If only one convention is used, justify it and quantify the effect size (e.g., Δ MSE distribution across injected patches).

P3-META-M1
- Severity: MAJOR
- Location: §II.D (p.4–5), §VI.D(ii) (p.17)
- Why others missed it: Reviewers noted pass/fail outcomes but not the choice of gate thresholds.
- Problem (hidden conditioning/post‑hoc thresholds): The paper adopts several decision gates without justification or pre‑registration: val‑loss ≤ 0.30 within ≤100 epochs, injection‑recovery ≥ 50% at 5σ, Jaccard ≥ 0.70 (k‑fold) and ≥ 0.50 (OOD), etc. No rationale is given for these exact cut values, nor is there a multiple‑tests correction across six surveys and several morphologies. This can turn qualitative PASS/FAIL into post‑hoc declarations.
- Required fix: Document the a priori rationale for each gate (with citations or power studies), or move them to a sensitivity analysis that shows conclusions are stable under reasonable variations (e.g., ±0.05 in Jaccard, 40–60% injection threshold, 50–150 epochs). State clearly which gates are confirmatory vs exploratory.

P3-META-M2
- Severity: MAJOR
- Location: §III.H (p.9–10) and §VI.D(ii) (Fig. 10, p.17)
- Why others missed it: They noted the mask test passes “by construction” but not its impact on the PASS/FAIL summary.
- Problem (sensitivity vs geometry conflation): The NEOWISE “injection‑recovery” test is a mask‑geometry QA that necessarily yields 100% when the same mask is re‑applied, yet the results table and Fig. 10 summarize it as a PASS on equal footing with detector‑sensitivity tests (SDSS continuum‑dip and Planck bump). This is misleading: including NEOWISE as 1 of the “3 PASS” detectors overstates validated sensitivity.
- Required fix: Remove NEOWISE from the PASS count in Fig. 10 and text. Present it separately as a mask‑geometry QA, and restrict “PASS” to detector‑sensitivity tests only. Adjust the headline “3 PASS / 3 FAIL-with-diagnostic” to reflect this.

P3-META-M3
- Severity: MAJOR
- Location: §V.a (p.15)
- Why others missed it: Attention was on the Fisher mapping constants; the bias‑mapping step was not examined.
- Problem (deep chain gap: w(θ) → bias ratio): The paper asserts that a Landy–Szalay two‑point analysis “yields the bias ratio b ≡ bQSO_cand/bfull_anomaly,” then quotes bgeo and bjk values, but provides no formula or scale range showing how the LS measurement was converted to a bias ratio. In linear theory, b enters via w(θ) ∝ b^2 ξ_m(θ), so b‑ratios require assumptions about the angular window, redshift distributions, and amplitude fitting (and then a square root). Without these details, the subsequent α ≡ b−1 and the Fisher chain 1/σ^2 = F0 + c α^2 are not reproducible.
- Required fix: Provide the explicit mapping from the measured w(θ) to b (fitting range, template ξ_m, treatment of shot noise, and whether a square root was taken of an amplitude ratio). Include an equation or a citation to the exact estimator used, and deposit code/DOI to reproduce bgeo and bjk.

P3-META-M4
- Severity: MAJOR
- Location: §V.b (p.15)
- Why others missed it: Several reviewers discussed normalizations but not the statistical labeling.
- Problem (sensitivity vs precision conflation): The paper calls [3.92, 8.98] a “1σ envelope” for σ(fNL) derived by mapping ˆα ± σα through a convex transformation with clipping at α = 0. This is not a 1σ interval for σ(fNL) in any probabilistic sense; it is a transformed ±1σ band in α. Labeling it “1σ” is statistically misleading.
- Required fix: Relabel as “translated ±1σ band in α mapped into σ(fNL)” (not a 1σ interval in σ space), or present a small Monte Carlo that samples α ∼ N(0.19, 0.65^2), maps to σ(fNL), and quotes the central 68% credible interval—then use that interval consistently.

P3-META-M5
- Severity: MAJOR
- Location: §III.A (p.5)
- Why others missed it: The check looks innocuous but its design undermines the inference.
- Problem (hidden conditioning in SNR test): The score–SNR null (ρ = −0.03; p = 0.12) is computed on a “stratified subsample of 2,670 spectra, log-uniform in SNR.” This is not a random sample from the analyzed set; it intentionally distorts the SNR distribution. The p‑value therefore has no straightforward interpretation for the population, yet the text concludes “no practically significant score–SNR dependence.”
- Required fix: Recompute the correlation on (i) a true random sample from the same parent set and (ii) a weighted analysis that recovers the real SNR distribution. Report effect sizes and confidence intervals, not just p‑values, and qualify the conclusion accordingly.

P3-META-M6
- Severity: MAJOR
- Location: §IV.D (p.13)
- Why others missed it: Planck×ACT discussion focused on ACT quarantining, not on logical inference.
- Problem (unsupported inference from a geometry-driven null): The text states the Planck×ACT positional cross-correlation is null and concludes this is “consistent with … CMB patch anomalies dominated by survey-specific systematics rather than primordial signals.” Because the two inputs occupy largely disjoint sky regions and one tier (ACT) is quarantined and undertrained, the null carries almost no discriminating power between “systematics” vs “cosmology.” The inference is therefore not supported by the test design.
- Required fix: Remove the physical interpretation or explicitly state that the null is geometry‑driven and non‑diagnostic. If a diagnostic is desired, supply a like‑for‑like cross‑correlation within a common sky footprint with equally trained models.

P3-META-m1
- Severity: MINOR
- Location: §V (Fig. 9 caption and text around it) and §III.B (p.6)
- Why others missed it: Prior reviews focused on abstract clarity and σ normalizations.
- Problem (ambiguous cross‑survey S comparability): The paper occasionally juxtaposes S distributions across surveys (e.g., DESI vs LAMOST in Fig. 3 left), but S is per‑survey standardized (Eq. 2) and only comparable across surveys when both use the same trained model/validation scale. The caption partly clarifies for SDSS (cross‑transfer vs native), but there is no blanket warning that S values across different native retrains are not on a shared scale—risking misinterpretation of cross‑survey histogram comparisons elsewhere.
- Required fix: Add a one‑sentence global caveat near Eq. (2) and in multi‑survey plots: “Because S is per‑survey standardized on that survey’s validation pool, absolute S values are not comparable across independently trained surveys.”

P3-META-n1
- Severity: NIT
- Location: Table I (both “Total (cross-transfer, ACT-incl.)” and “Path‑C unique (primary)” rows)
- Why others missed it: One reviewer flagged the Path‑C total “Rate” as misleading; the same critique applies to the cross‑transfer “Rate.”
- Problem: The catalog‑level “Rate (%)” implies a measured fraction but aggregates fixed‑count/fixed‑percentile tiers (Planck, Gaia, NEOWISE; and, post‑retrain, Planck top‑200/200k). The cross‑transfer total “0.86%” has the same interpretability problem as the Path‑C “1.01%.”
- Required fix: Drop the total‑row “Rate (%)” entries or mark them “N/A (heterogeneous fixed‑count inputs; not a measured rate).”

Meta-review recommendation
MAJOR REVISIONS

Given the union of the six reviews, the paper needs several essential/major corrections before it meets PRD standards. Beyond already‑flagged issues (eROSITA selection axis, Planck selection fraction after native retrain, Fisher-mapping constant and numerical example, abstract/history language, SDSS thresholding, pooled SIMBAD metric, figure normalization), this meta‑review adds three ESSENTIAL items (tabular-feature scaling, dedup cluster bookkeeping, and Planck injection/standardization conditioning) and several MAJOR clarifications (gate pre‑registration, NEOWISE “PASS” summary, w(θ)→bias mapping, “1σ” labeling, SNR‑correlation sampling, and Planck×ACT inference). Addressing these will materially improve reproducibility and interpretability.

Blocker count and survivability
Across all six reviews, I count at least 6–8 true blockers: (i) eROSITA selection reproducibility; (ii) Planck selection‑fraction inconsistency; (iii) Fisher F0 dimensional error and numeric example; (iv) version‑history/internal‑log language in the main text; (v) SDSS primary‑threshold clarity; and, from this meta‑review, (vi) missing feature‑scaling specifics for tabular surveys; (vii) dedup cluster bookkeeping; (viii) Planck injection/standardization conditioning. My confidence is moderate that, once these are fixed with clear code/DOIs and tightened presentation, the paper would survive external peer review: the underlying contribution is significant, but careful revision is required to meet PRD’s methodological and reproducibility bar.