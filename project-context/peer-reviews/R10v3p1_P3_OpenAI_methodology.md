# P3 R10v3p1 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `o3-2025-04-16` [FALLBACK from gpt-5]
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (3466 chars)
**Wall time**: 191.3s

---

# Referee report (Methodology — Physical Review D)

The line numbers below refer to the rendered 20-page PDF supplied for review.

--------------------------------------------------------------------
## ESSENTIAL (must be fixed before the paper can be considered)

ID | Location | Problem | Required fix
---|-----------|---------|------------
P3-E1 | §II B, p. 3, l. 34–45 | **Training / inference leakage.** The DESI auto-encoder is trained on 47 000 spectra that remain in the 22.5 M production catalogue on which anomaly scores are later quoted. The attempt to justify this with a 5-fold cross-validation of the 47 000 items is insufficient: (i) information from every training example is still available when the final model is applied, (ii) 0.87 % anomaly rate is therefore biased low, (iii) all published DESI scores are contaminated. | Reserve an unbiased DESI test set that is **never** used for either hyper-parameter tuning or threshold selection and recompute every DESI-dependent scalar (all rates, novelty fractions, score histograms and downstream Fisher forecasts) on that set.
P3-E2 | Abstract & §IV A, p. 8–9 | **“17.8 % genuine novelty fraction” is unsupported.** It is derived from only the *top-1000* DESI anomalies, yet advertised for the full 378 280-object catalogue. Extrapolation is unjustified and the number is used in the abstract and conclusions. | Either (i) perform the same 20-catalog cross-match on *all* anomalies, or (ii) clearly confine the 17.8 % statement to the 1000-object stratum everywhere (title, abstract, conclusions) and quote an uncertainty from bootstrap or binomial statistics.
P3-E3 | §II D, p. 4 & Table I | **Gate criteria are violated but catalogues retained.** Step 5 requires ≥ 50 % injection–recovery at 5 σ. LAMOST (5.8 %), Gaia (5.2 %), eROSITA (1.2 %) fail, yet their anomalies are published and used in the deduplicated headline. This breaks the declared protocol. | Either discard these three catalogues from the headline count or repeat the detector design until they pass the stated gate. All downstream numbers (378 280, 264 938, etc.) must be recomputed consistently.
P3-E4 | §V, p. 10–11 | **Fisher “positivity-respecting form” is ad hoc.** The formula 1/σ² = F₀ + c α² is introduced with no derivation or citation; the constants F₀ = 1/8.982 and c = 0.0747 are not traceable. Using it leads to the claimed 7.9 % improvement on fNL. | Provide a full derivation (or literature equation number) showing how this formula follows from the underlying Fisher matrix including the anomaly tracer, and disclose the exact data vector and covariance used to obtain F₀ and c. Otherwise remove all σ(fNL) forecasts.
P3-E5 | §V A, p. 11 | **Bayes factor calculation opaque.** The quoted Savage-Dickey B_MB/SMBHB = 7.1 × 10³ is impossible to verify: the prior on γ, the likelihood normalisation and the marginal densities are not given, nor is the kernel density bandwidth. | Supply the prior pdf, the KDE bandwidth, the numerical value of the marginal likelihood at γ = 3 and γ = 4.33, and make the MCMC chain available in ancillary files so the Bayes factor can be reproduced.
P3-E6 | Entire manuscript | **Confusion of σ from incompatible nulls.** Frequentist significances (“+1.13 σ”, “+4.61 σ”) are quoted next to Bayes factors and Fisher forecasts without an explicit warning that they are incomparable (§V mixes them in the same paragraph). This violates PRD guideline 7. | Each time two different σ measures appear, add a parenthetical statement clarifying that they arise from distinct statistical procedures and are *not* directly comparable. Remove any language that visually equates them.

--------------------------------------------------------------------
## MAJOR (substantial revision needed)

ID | Location | Problem | Required fix
---|-----------|---------|------------
P3-M1 | Abstract & p. 5 (Fig. 2 right) | The SDSS cross-transfer run produces scores up to 1.9 × 10¹¹, nine orders of magnitude larger than any native run. This is presented as “a feature, not a bug”, yet later a native SDSS model is trained and *different* scores are released. The reader cannot tell which set is used in Table I or the deduplication. | Retain only one SDSS anomaly definition. Remove the cross-transfer numbers from all headline statistics or move them to an appendix marked “diagnostic only”.
P3-M2 | §III F, p. 6 | Planck auto-encoder still fails criterion (a) (val loss = 0.4437 > 0.30) but is allowed because it passes the injection test. Yet ACT (Appendix F) that also fails criterion (a) is rejected. The logic is inconsistent. | State *one* quantitative performance threshold for CMB models (e.g. val-loss < 0.3 or ≥ 50 % recovery) and apply it consistently to Planck *and* ACT. If ACT is removed, explain how Planck passes the same threshold.
P3-M3 | Eq. (1), p. 2 | MSE defined without an explicit normalisation by spectral variance. Surveys have vastly different noise levels; comparing raw pixel squared errors across them makes cross-survey S values meaningless. | Either (i) normalise each wavelength pixel by its per-spectrum pipeline variance before computing MSE, or (ii) justify mathematically why raw flux units are comparable between DESI and, e.g., LAMOST.
P3-M4 | Table III, p. 8 | The Isolation-Forest “raw score” scale is arbitrarily printed to five significant figures although tree ensemble scores have no absolute meaning. The comparison 95.3 × enrichment is therefore meaningless. | Quote only rank-based overlap statistics (e.g. Jaccard) or provide a calibration that maps IF raw scores to probabilities.
P3-M5 | §IV B, p. 9 | χ² uniformity test over the sky ignores the highly non-uniform survey masks yet a χ²_ν = 3.76 is interpreted as astrophysical. The test is invalid. | Replace by a HEALPix-weighted Monte-Carlo that draws random points from each survey’s completeness map, or remove the χ² claim.
P3-M6 | §II C, p. 3 | GPU throughput numbers (e.g. 1 142 spectra s⁻¹) are reported to three significant digits without uncertainty or reproducibility environment. | Quote them to two significant digits and add the CUDA, PyTorch and driver versions.

--------------------------------------------------------------------
## MINOR (should be addressed but not publication-blocking)

ID | Location | Problem | Required fix
---|-----------|---------|------------
P3-m1 | Table I footnote ♡, p. 7 | Three different SDSS thresholds are reported (S > 5, S ≥ 0.2051, S ≥ 0.1060). This is extremely confusing. | Present one definitive SDSS threshold in the main text; put the others in a separate “sensitivity” appendix.
P3-m2 | §II B, p. 2 | Using the letter “S” for the anomaly score and “z” for spectroscopic redshift is good, but later (p. 5, Fig. 2) the symbol “AE” is introduced without definition. | Define “AE” the first time it appears or replace by S.
P3-m3 | §VI C, p. 12 | “B-dominant contamination: the ∼ 44 000 DESI B-dominant anomalies … are flagged as calibration-suspect” yet they remain in the public catalogue. | Flag them explicitly in the released table or provide a filter column.
P3-m4 | References | Several arXiv links are missing the prefix “arXiv:” (e.g. Ref. [33] lists arXiv:2311.13082 in text but not in the bibliography). | Standardise reference format to PRD style.

--------------------------------------------------------------------
## NIT (cosmetic)

ID | Location | Problem | Fix
---|-----------|---------|----
P3-n1 | p. 13, Table IV caption | “SUpercedes” typo. | Replace by “supersedes”.
P3-n2 | p. 14, §VII bullet 1 | “141× the largest prior single-survey catalog [11]; DESI-only is a 73× like-for-like increase.” 73× is already included in 141×. | Rephrase to avoid implied double counting.

--------------------------------------------------------------------
## Page-count

The paper is 20 pages + 3 dense technical appendices. For a methodology catalogue whose cosmological content is an order-of-magnitude *forecast*, not a measurement, 12–14 pages would suffice. I recommend moving all diagnostic plots (Figs. 2, 3, 7, 8, 9) and the ACT appendix to a separate data-release note.

--------------------------------------------------------------------
## Summary recommendation

**MAJOR REVISIONS**

The manuscript presents an impressively large cross-survey anomaly catalogue, but the statistical methodology does not yet meet PRD rigour. Training/test leakage, violation of the authors’ own quality-gate, an ad hoc Fisher formula, and an unverifiable Bayes factor must all be corrected. Once the essential issues are fixed and the analysis is repeated on a truly independent data set, the work may merit publication.

---

## PASS 2 — self-critique findings (what initial review missed)

Additional findings after second-pass audit
===========================================

Only *new* issues are listed below.  IDs continue the numbering
scheme of the original report.

--------------------------------------------------------------------
ESSENTIAL (must be fixed)
--------------------------------------------------------------------
ID | Location | Problem | Required fix
---|-----------|---------|------------
P3-E7 | § IV A & Fig. 5 | **Arithmetic error in the 58.8 % SIMBAD-unmatched headline.** Weighting the per-survey fractions in Table I by the listed anomaly counts gives 89.6 % (DESI 0.99, SDSS 0.90, LAMOST 0.50, eROSITA 0.68, NEOWISE 0.45, Gaia 0.27).  The printed 58.8 % cannot be reproduced. | Recalculate the aggregate fraction from the published numbers or show the alternative weights actually used.  Update every place (abstract, conclusions, Fig. 5 caption) where 58.8 % appears.
P3-E8 | § V, eq. un-numbered (“1/σ(fNL)² = F₀ + c α²”) & Table VII | **Dimensionally inconsistent constant and propagated mis-computations.** For α = 0 the reference σ(fNL) is 8.98, therefore F₀ must be 1/8.98² = 0.0124, *not* 1/8.98.  The text states the latter but the numbers in Table VII appear to use the former for α ≥ 0.15 and something else for α ≤ 0.10 (e.g. α = 0.05 should give σ ≈ 8.92, not 8.80). | (i) Correct F₀ in the paper, (ii) recompute every σ(fNL) entry in Table VII and all quoted “7.9 %” or similar improvements, (iii) check that c was obtained with the same definition of F₀.
P3-E9 | Multiple (e.g. § II A p. 2 l. 36; § III B p. 5 l. 25) | **Broken internal cross-references.** “Fig. ??” and “Table ??” placeholders remain in the final PDF. | Resolve all missing \ref’s before resubmission; PRD will not accept manuscripts with unresolved references.

--------------------------------------------------------------------
MAJOR (substantial revision needed)
--------------------------------------------------------------------
ID | Location | Problem | Required fix
---|-----------|---------|------------
P3-M7 | Table I, “Total (cross-transfer)” row | The row sum 319 443 secretly **includes** the 200 ACT anomalies even though the ACT survey is absent from the table body and is said to be “quarantined”.  Readers cannot reconstruct the total. | Add an explicit ACT line with its counts (and val-loss failure note) or remove the ACT contribution from the total so every figure is auditable from the visible rows.

--------------------------------------------------------------------
MINOR (should be addressed)
--------------------------------------------------------------------
ID | Location | Problem | Required fix
---|-----------|---------|------------
P3-m5 | Throughout, e.g. § II A p. 2 l. 36; § III B p. 5 l. 25 | Several occurrences of “Fig. ??” / “Table ??” remain.  These were not flagged in the first review. | Replace each placeholder by the correct figure or table number once the cross-reference is fixed.

--------------------------------------------------------------------
Explanation
-----------
The second-pass checklist focused on arithmetic consistency,
internal references and dimension checks.  
Most values in Tables I and IV are arithmetically self-consistent,
but the SIMBAD aggregate, the Fisher constants, and several
cross-references do not survive scrutiny.  The new ESSENTIAL items
P3-E7 and P3-E8 directly affect headline claims in the abstract and
conclusions and therefore must be corrected.