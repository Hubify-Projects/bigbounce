# P4 auto-2026-06-05_1517pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (9150 chars)
**Wall time**: 269.1s

---

Referee report on “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
I evaluated the statistical methodology and internal consistency: null definitions, estimator hierarchy, error propagation, arithmetic consistency of all load-bearing numbers (abstract, tables, conclusions), dimensional consistency of equations, and whether σ and p-values are consistently defined and not conflated across nulls. The claims about mask-induced leakage, equivariant classification, and MASTER deconvolution are interesting and likely important, but I found several issues that must be addressed before this work meets PRD standards.

Findings

ESSENTIAL

P4-E1 (Sec. III.C + App. A; pp. 3 and 7): Inconsistent definition of the asymmetry field Ap used in NaMaster
- Quote:
  - Eq. (3) (p. 4): “Ap = (N(p)CW − N(p)CCW)/(N(p)CW + N(p)CCW).”
  - Appendix A.a (p. 7): “The asymmetry field is Ap = (NCW − NCCW)/(NCW + NCCW) (spirals only).”
  - Appendix A.c (p. 7): “Field: scalar (spin-0) asymmetry map Ap = (NCW − NCCW)/Ntotal, with galaxy-weighted mask-mean subtraction …”
- Problem: The paper gives two contradictory definitions for Ap within the same appendix (spirals-only denominator vs. all-galaxy denominator). This is load-bearing for every MASTER result (Cℓ values, σ, and the headline −0.122σ).
- Required fix: State clearly and unambiguously which definition is used for each estimator (real-space map and NaMaster field). If the denominators differ across estimators, justify why and re-evaluate whether results are comparable. If the denominator is Ntotal in the NaMaster field, update all text and tables accordingly and re-run any analysis whose output depends on field normalization (Cℓ, σ, p-values). Include an explicit check showing that switching denominators does not alter the headline dipole conclusion (or revise the claims).

P4-E2 (Table II + Sec. IV.B; p. 4 and p. 4): Numerical/sign inconsistency in “Dev. (σ)” for CW fraction
- Quote:
  - Table II states “Dev. is (fCW − 0.5)/σ” yet reports Dev. = 9.5 for Catalog C (fCW = 0.4974 ± 0.000279).
- Problem: (fCW − 0.5)/σ = (−0.0026)/(0.000279) ≈ −9.3, not +9.5. Either the sign or the value is wrong. The body text later treats “9.5σ” without indicating the sign.
- Required fix: Correct Table II (and any downstream references) to report the signed deviation or explicitly state that absolute deviations are shown (and then correct the numerical value to match the stated rule). Ensure consistency with the appended monopole value ⟨A⟩mask,gw = −0.005294.

P4-E3 (Sec. IV.B; p. 4): Inconsistent numerical claims about “asymmetry-suppression factor”
- Quote: “The 3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53% demonstrates the dominance of the equivariant TTA processing.”
- Problems:
  - Table II gives raw CW excess +0.79% (not +2.05%). The −0.53% is the asymmetry A (2fCW − 1), not fCW − 0.5. The statement conflates metrics (fractional excess vs. asymmetry A).
  - There is no source in the paper for +2.05% in this context. If +2.05% is A for Catalog A, it would require fCW ≈ 0.51025, which contradicts Table II (0.5079).
- Required fix: Use one metric consistently. If you compare A values, give A for both tiers (e.g., 1.58% to 0.529%, suppression factor ~3.0×). If you compare fCW − 0.5, use 0.79% to −0.26%. Recompute and correct the factor (currently not 3.86× under any consistent interpretation).

P4-E4 (Multiple locations: Sec. III.A p. 3; Sec. VI p. 6; Table I p. 4): Side-by-side σ values from different nulls without immediate qualifier
- Problem: The paper establishes in the abstract and Sec. IV “Significance conventions” that σ values are not directly comparable across nulls. However, there are instances where different-null σ are juxtaposed without a local reminder, e.g.:
  - Sec. III.A (p. 3): “(i) … 0.43σ; (ii) … −0.122σ” listed together.
  - Sec. VI (p. 6): “raw Catalog A dipole (2.31σ real-space; +6.48σ pre-MASTER) …”
- Required fix: At every juxtaposition of σ from different nulls include an explicit, local note that they are not directly comparable (e.g., parenthetical “different nulls; not directly comparable”). Alternatively, list them in separate sentences with the null specified each time. This is a PRD requirement for statistical clarity.

P4-E5 (Sec. IV.C.a; p. 4): Inconsistent σ and p-value for the real-space dipole
- Quote: “the fitted dipole has amplitude significance 0.43σ (p = 0.30 from the isotropic-null bootstrap, NMC = 10,000).”
- Problem: If σ is the standard deviation from the same bootstrap null, 0.43σ corresponds to a two-sided Gaussian p ~ 0.66, not 0.30. If the distribution is non-Gaussian/skewed, explain how σ is computed and why p and “σ” do not correspond in the usual way.
- Required fix: Report either (i) only the empirical p-value and omit the Gaussianized σ, or (ii) provide a mapping from amplitude to p to σ under the bootstrap distribution and explain the discrepancy. As written, the two numbers are mutually inconsistent under the stated null.

P4-E6 (Abstract p. 1; Sec. IV.D p. 4–5): “Earlier paper versions” language
- Quote: “were interpreted in earlier paper versions as mask-geometric leakage …”
- Problem: Version-history language must not appear in the manuscript.
- Required fix: Remove all references to earlier paper versions. Rewrite the sentence to state the current interpretation only.

P4-E7 (Abstract p. 1; Appendix A p. 7): “Subsample mask” definition is unclear/contradictory; “strict-superset subsample mask”
- Problem: The term “strict-superset subsample mask” is contradictory and the analysis mask construction is not rigorously defined. The primary headline result hangs on this mask (fsky = 0.659; Nmap,weighted = 5,547,858), yet readers cannot reconstruct it.
- Required fix: Provide a precise, reproducible definition of the “subsample mask”: selection criteria for pixels/objects (e.g., min counts, quality cuts), its relationship to the canonical mask (subset/superset?), and why it is justified as the “headline” estimator footprint. Include a mask-making figure or an explicit algorithm and a mask file hash.

MAJOR

P4-M1 (Null definitions; throughout): Ambiguity between “per-pixel shuffle,” “random-label permutation,” and “binomial monopole-only” nulls
- Problem: The paper uses several distinct null procedures (per-pixel random permutations; per-pixel binomial draws with pglobal; isotropic bootstrap). Which null is used for which line in Tables I–IV is not always explicit, and the terms are used interchangeably (“per-pixel-shuffle null,” “direct-MC,” etc.).
- Required fix: Add a clear subsection enumerating all null procedures with precise definitions and list, for each estimator in Tables I–IV, exactly which null was used. State what moments (mean, σ) and rank p were estimated from how many MCs and their seeds. Keep terminology consistent across the paper.

P4-M2 (Table III p. 5; Appendix A p. 7): Bandpower significances reported without null means; signs inconsistent with Cℓ signs
- Problem: Several rows report positive “Significance (σ)” where Cℓ is negative (e.g., ℓeff = 9: Cℓ = −0.248×10−6 with +2.232σ). Without listing null means, the sign convention and calculation cannot be checked.
- Required fix: Add the null mean Cℓ for each bandpower (or at least state whether significance is computed as (Cmeas − ⟨Cnull⟩)/σnull), and ensure the sign is interpretable. Provide a brief rationale for why negative Cℓ with positive σ occurs (e.g., negative null mean due to mask leakage).

P4-M3 (Sec. VI.A; p. 6): Derivation of the “Fisher Poisson floor” and σ(A/2) ≈ 0.048% is not documented
- Quote: “The Fisher Poisson floor at 3σ is ∼ 0.29% full-amplitude (from σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46).”
- Problem: For independent galaxy counts, σ(A/2) ≈ 1/(2√Nspiral) ≈ 0.028%. The manuscript inflates this to 0.048% with a brief mention of fsky. The mapping from fsky and pixelization to this σ is not provided, and later an extra 5–8% penalty is assigned for edge-on contamination. As written, the “Fisher” number looks ad hoc.
- Required fix: Provide an explicit derivation (or Fisher forecast expression) that shows how pixelization, fsky, and any weighting lead to σ(A/2) ≈ 0.048% from Nspiral = 3.2M. If classification noise or depth weighting enters, say so, and rename this quantity accordingly (it is not a pure Poisson Fisher floor then).

P4-M4 (Sec. IV.D; Appendix A p. 7): Reporting “+3.64σ (moment-ratio)” with NMC = 500
- Problem: With only 500 MC, moment-based σ estimates have ~3% relative uncertainty; the rank pMC = 0.030 (15/500) corresponds to ~1.9σ Gaussian-equivalent, not 3.64σ. While the text notes both z and p, the abstract and tables prominently quote +3.64σ, which is potentially misleading.
- Required fix: Either (i) increase NMC to at least ~10,000 for robust tail estimation if you wish to quote a “σ” substantially larger than 2, or (ii) de-emphasize the “σ” and report only the empirical pMC with uncertainty (e.g., 0.030 ± 0.008), plus the test statistic value.

P4-M5 (Appendix D.f; p. 8): Unclear and numerically suspect WLS “z” values (−264.5, −18.1)
- Quote: “Abest_dipole = 4.55×10−3 … interpretation (i) reference amplitude 1.7% at z = −264.5 … block-bootstrap inflates σ by 14.7×, reducing z to ≈ −18.1.”
- Problem: These “z” values are implausibly large in magnitude, and the sign convention is unclear (fitting a positive Abest but quoting negative z for a larger reference amplitude). As written, this cannot be audited.
- Required fix: Define the test statistic precisely and report confidence intervals (e.g., Abest ± σ, 95% CI) rather than enormous z-values. If you are computing a hypothesis test at a fixed Aref, state the model, covariance, and resulting p-value; avoid meaningless negative “σ”.

P4-M6 (Appendix A; p. 7): “Monopole subtraction reduces C1 … and increases σ from +1.85 to +3.64”
- Problem: This is a counterintuitive statement (reduced amplitude but higher significance) without showing the underlying null σ or means. It may be correct if σnull shrinks more than C1, but cannot be verified.
- Required fix: Provide the numerical C1, ⟨Cnull⟩, and σnull before and after monopole subtraction to justify this claim.

MINOR

P4-m1 (Sec. IV.D; p. 5): Notation “σ = −2.89” for cross-spectrum anti-alignment
- Quote: “rℓ=2 = −0.65 with σ = −2.89 against permutation null.”
- Problem: σ should not be negative. This should read “z = −2.89σ” or “significance −2.89σ.”
- Required fix: Correct the notation.

P4-m2 (Appendix D.c; p. 8): Unexplained notation “C(Ap×ntotal)”
- Problem: The factor “ntotal” is undefined here (is this the depth weight Wp = Nall?). 
- Required fix: Define the cross-spectrum fields explicitly (e.g., Ap vs. depth proxy Wp) and use consistent symbols.

P4-m3 (Sec. VII Data Availability; p. 9): Broken/ambiguous URLs
- Quote: “https://huggingface.co/dataset s/bamfai/galaxy- chirality- catalog”
- Problem: The URL includes spaces and is likely not valid.
- Required fix: Provide correct clickable URLs (no spaces) and, ideally, DOIs or permanent archive links. Include exact commit hashes or release tags for code and data files used to produce the figures/tables.

P4-m4 (Appendix A; p. 7): “C 2 2◦ apodization” formatting
- Problem: The apodization specifier is unclear (“C 2 2◦”). 
- Required fix: Clarify the apodization scheme (e.g., cosine apodization with 2° scale). Provide the exact NaMaster call or formula.

P4-m5 (Appendix B.d; p. 7–8): Ambiguous calibration acceptance statement
- Quote: “T7 confidence calibration (qualitative, < 50% at confidence > 0.9)”
- Problem: The criterion and result are unclear. What does “< 50% at confidence > 0.9” mean?
- Required fix: Clarify the calibration diagnostic (e.g., reliability diagram, ECE/Brier score), thresholds, and pass/fail result.

P4-m6 (Conclusions d; p. 7): “≥107 galaxies” very likely means 10^7
- Problem: Missing superscript caret; reads as 107.
- Required fix: Replace by “≥ 10^7 galaxies.”

NIT

P4-n1 (Throughout): Consistency of “NaMaster/pymaster” capitalization and hyphenation
- Required fix: Use a consistent style (e.g., NaMaster, pymaster).

P4-n2 (Sec. V.B; p. 5): Citation-based claims like “1.6× CE-ResNet’s scale”
- Suggestion: Add the explicit CE-ResNet spiral sample size in the text to make the ratio auditable without reading [7]. You already mention ~1.95M; OK to keep but ensure consistency.

P4-n3 (Appendix A; p. 7): Units on Cℓ
- Table III lists “(sr)” while Table IV has no units. 
- Required fix: State units everywhere and ensure they are consistent.

P4-n4 (Sec. IV.D; p. 5): “strict-superset subsample mask” phrasing
- Required fix: Rephrase to a non-contradictory description once the mask is properly defined (see P4-E7).

Assessment of length
At 10 pages (no figures), the manuscript is dense but on the long side relative to the core methods results. After addressing the essential/major issues, you could streamline by moving several diagnostic digressions (e.g., some of Appendix D’s detailed numbers and Appendix C’s auxiliary diagnostics) to a longer supplemental, while keeping (i) explicit null definitions, (ii) estimator hierarchy and mask definitions, and (iii) the minimal set of tables to support the headline claims. A target of 8–9 pages main text plus appendices seems reasonable.

## Summary recommendation
MAJOR REVISIONS

Justification: The paper tackles an important methodological issue and, in principle, presents a careful analysis with multiple nulls and controls. However, there are essential internal inconsistencies (most critically the contradictory definition of the asymmetry field Ap used in the MASTER pipeline), numerical/sign mismatches in Table II, inconsistent σ/p reporting for the real-space estimator, and insufficiently specified mask/null definitions that affect the headline claim. These must be corrected and, where needed, analyses re-run with the clarified definitions. Once the essential and major issues are fixed and all load-bearing numbers (abstract, tables, conclusions) are made internally consistent and reproducible, the work could be suitable for PRD.

---

## PASS 2 — self-critique findings (what initial review missed)

P4-E8 (Sec. II.B; p. 2): Training-label count mismatch
- Quote: “We assemble training labels from three sources: (1) GZ1: 6,637; (2) CE-ResNet: 17,153; (3) Synthetic: 2,000… The combined training set contains 26,636 images.”
- Problem: 6,637 + 17,153 + 2,000 = 25,790, not 26,636. The extra 846 images are unaccounted for.
- Required fix: Reconcile the counts. Either correct the per-source tallies or explain the additional images (e.g., augmentations counted as separate samples, de-duplication offsets, or a fourth source).

P4-E9 (Abstract p. 1 vs. App. E.b p. 9 and Sec. VI.A p. 6): Inconsistent “high-confidence” (HC) threshold and sample size
- Quote: Abstract: “471 049 high-confidence per-spiral after peqCW > 0.9.” Appendix E.b and elsewhere discuss HC thresholds of 0.6 and 0.8; Sec. VI.A injection-recovery uses N = 471,049 HC-spiral subsample but no threshold is restated.
- Problem: The HC definition (0.9 vs 0.6/0.8) is inconsistent, yet N = 471,049 is tied to the falsification criterion and injection-recovery. Readers cannot reconstruct the HC sample.
- Required fix: State a single, precise HC threshold for the N = 471,049 subsample everywhere it appears (abstract, methods, VI.A, App. E). If different HC tiers are used, give each N and threshold and ensure the injection-recovery/falsification criterion references the correct one.

P4-E10 (App. C.c; p. 8): Incorrect look-elsewhere correction magnitude
- Quote: “maximum asymmetry 3.05σ… direct-MC pLEE ≤ 10−4… Bonferroni/BH across ∼650 directions reduces post-LEE significance to < 1σ.”
- Problem: Bonferroni-corrected p ≈ 650 × 10−4 = 0.065 (assuming independence; BH is typically less conservative), corresponding to ≈1.5σ two-sided, not < 1σ. The text understates the post-LEE significance.
- Required fix: Correct the family-wise (or FDR) adjusted p-value and its σ-equivalent. State the correction used (Bonferroni vs BH), the effective number of trials (and how it was estimated), and the resulting adjusted significance.

P4-E11 (Abstract p. 1): Contradictory terminology “MASTER-deconvolved single-mode pseudo-C1”
- Problem: “Pseudo-Cℓ” refers to the masked (coupled) spectrum before deconvolution, while “MASTER-deconvolved” refers to the decoupled estimate. Calling a deconvolved result a “pseudo-C1” is self-contradictory for the headline observable.
- Required fix: Replace “pseudo-C1” by “C1” (deconvolved) in the abstract and throughout wherever appropriate. Reserve “pseudo-Cℓ” for pre-deconvolution quantities.

P4-E12 (App. E.b; p. 9 vs. Sec. IV.C.a; p. 4): Inconsistent dipole significance for the full equivariant catalog
- Quote: App. E.b: “Catalog C-full +4.31σ monopole-preserving dipole collapses to +0.62σ (HC-broad-0.6) and +0.87σ (HC-strict).” Main text Sec. IV.C.a: “the fitted dipole has amplitude significance 0.43σ.”
- Problem: The same dataset (Catalog C-full) is described as 0.43σ and 4.31σ depending on context. “Monopole-preserving dipole” is undefined and appears to be a different estimator.
- Required fix: Define precisely what “monopole-preserving dipole” means and how it differs from the main “fitted dipole” (null, estimator, weighting, and mask). If it is not comparable, avoid juxtaposition. Ensure the headline claim only references the clearly defined estimator.

P4-E13 (Table II; p. 4): Additional arithmetic mismatches in “Dev. (σ)” for Catalogs A and B
- Problem: Using the table’s stated rule Dev. = (fCW − 0.5)/σ with σ = 0.000279:
  - A: (0.5079 − 0.5)/0.000279 ≈ +28.3, not 28.8.
  - B: (0.5040 − 0.5)/0.000279 ≈ +14.3, not 14.6.
- Required fix: Correct the reported values and/or state rounding conventions that reconcile the discrepancies. Ensure consistency across the text (also fix the Catalog C sign/value per P4-E2).

P4-M7 (Table I; p. 4): Mixed units/metrics in the “σ” column
- Problem: The “σ” column lists σ-values for rows (i)–(iii), but row (iv) lists pLEE ≤ 10−4 (a p-value), not a σ. This mixes statistical metrics in a single column labeled “σ”, risking misinterpretation.
- Required fix: Split the column into “Test statistic” and “p-value/σ” or add a dedicated p-value column. Report σ and p consistently for every estimator (or clearly mark N/A). Include the null for each row (see also P4-M1).

P4-M8 (Abstract p. 1; App. A.a; p. 7): Misleading notation “n = 5,547,858” for a weighted sum
- Quote: Abstract: “(n = 5,547,858, fsky = 0.659)”; App. A.a: “Nmap,weighted = Σp∈mask Wp = 5,547,858 where Wp = N(p)all.”
- Problem: The abstract’s “n” looks like a count but is actually a sum of per-pixel weights (galaxy counts, including non-spirals) over a mask. This is not the number of galaxies analyzed nor the number of spirals and can be misread.
- Required fix: Replace “n” by “ΣWp” or “Nmap,weighted” in the abstract and define it on first use. Also report the corresponding number of unique galaxies within the mask to avoid confusion.

P4-M9 (Table III; p. 5 vs. App. A.b; p. 7): Bandpower counting inconsistency
- Quote: Table III shows 1 single-ℓ entry and 5 bandpowers; later the table caption notes a “Joint χ2/dof (38 bandpowers) = 161.2/38 = 4.24.”
- Problem: The manuscript presents 6 rows but claims a χ2 over 38 dof, without listing those 38 bandpowers, binning scheme, or their Cℓ values. This cannot be reproduced or audited.
- Required fix: Provide the full set of bandpowers used in the χ2 (bin edges, Cℓ, ⟨Cnull⟩, σnull), or move the χ2 to the appendix with a complete table. Ensure consistency with the binning defined in App. A.b.

P4-M10 (Sec. VI.A; p. 6): Stale/inconsistent fsky in “Fisher Poisson floor”
- Quote: “σ(A/2) ≈ 0.048% at Nspiral = 3,201,160, fsky = 0.46.”
- Problem: The paper elsewhere uses fsky = 0.49005 (canonical) and 0.659 (subsample). The origin of fsky = 0.46 is unexplained and likely stale. This feeds directly into the 3σ ≈ 0.29% detectable amplitude claim.
- Required fix: Use a single, justified fsky appropriate for the specific estimator and dataset, or show how different fsky values enter a formal Fisher calculation. Update the 0.048% and 0.29% numbers accordingly (see also P4-M3).

P4-m7 (Table IV; p. 5): Minor arithmetic mismatches in reported z
- Problem: For the pre-MASTER pseudo-C(ℓ=1)ℓ: z = (1.696 − 1.685)/0.007 ≈ 1.57, not 1.68. For hemisphere max|A|: (3.48 − 1.69)/0.41 ≈ 4.37, not 4.42.
- Required fix: Correct the z values or provide exact underlying (non-rounded) means/σnull used for z to justify the reported numbers.

P4-m8 (Sec. III.B; p. 3 and App. B.a; p. 7): Ambiguous evaluation descriptors for accuracy
- Quote: “Headline 93.7% three-class accuracy (with augmentation active); post-hoc evaluation without augmentation yields 94.9%.”
- Problem: “With augmentation active” is unclear for evaluation (train-time augmentation? flip/rotation TTA? stochastic test-time augmentation?). The two numbers differ materially.
- Required fix: Specify the exact evaluation protocol for each number (dataset, splits, augmentations/TTA used, seeds). If one is on the training/validation set and the other on a held-out set, say so.

P4-m9 (App. C.b; p. 8): Undefined symbol “σiso”
- Quote: “NGP (b>0) gives σiso = +0.47; SGP (b < 0) gives +2.02.”
- Problem: “σiso” is not defined, and the null used is not stated for these σ values.
- Required fix: Define σiso (which null, what statistic, one- or two-sided) and include the corresponding p-values for clarity.

P4-m10 (App. E.b; p. 9): Undefined term “monopole-preserving dipole”
- Problem: This term is not defined elsewhere and appears to produce σ values that differ drastically from the “fitted dipole.”
- Required fix: Define the estimator precisely (map normalization, monopole treatment, weighting, null) or avoid using a new term for a one-off diagnostic.

P4-n5 (Abstract, Secs. IV.D/VII; multiple): “removes the leakage” wording vs residual
- Problem: Phrases like “MASTER … removes the leakage” conflict with later statements that a +3.64σ residual remains on the canonical mask.
- Required fix: Reword to “substantially mitigates mask-coupled leakage” and explicitly note the residual on the canonical mask versus the null on the subsample mask.

P4-n6 (Sec. II.A; p. 2): Minor wording nit
- Quote: “includes unique dr8 id identifiers”
- Required fix: Use “unique DR8 identifiers” (avoid “id identifiers”).

P4-n7 (Abstract/App. A; notation): Mixed use of “n” for counts and weighted sums
- Problem: Using “n” in the abstract to mean ΣWp is nonstandard.
- Required fix: Reserve “n” for object counts; use “ΣWp” or “Nmap,weighted” for weighted sums, and define once.

Explanation
These issues are in addition to those already identified (P4-E1–E7, P4-M1–M6, P4-m1–m6, P4-n1–n4). They focus on new arithmetic inconsistencies (training set size; Table II A/B rows; Table IV z-values), a look-elsewhere correction error, contradictory/statistically ambiguous terminology (pseudo-Cℓ vs deconvolved Cℓ; undefined “monopole-preserving dipole”; undefined σiso), table/notation clarity (mixed “σ”/p-values in Table I; using “n” for a weighted sum), and a likely stale fsky in the Fisher-floor calculation. Addressing these will materially improve reproducibility and statistical rigor.