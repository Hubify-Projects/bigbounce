# P4 auto-2026-06-06_0021pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5834 chars)
**Wall time**: 303.0s

---

Referee report for “Survey-Scale Galaxy Chirality with Equivariant TTA: A −0.122σ Subsample-Mask ℓ=1 Null, a Quantifiable Monopole-Mask Leakage Channel, and Diagnostic Evidence for a Depth/Morphology-Correlated Canonical-Mask Residual on 8.47 Million DESI Legacy Galaxies (3.2 Million Spirals)”

Scope of review
- Focus: statistical and methodological rigor; internal arithmetic consistency; null definitions; estimator hierarchy; error propagation; MC sample-size adequacy; table/number tracing; overclaim checks.
- I read the entire 10-page manuscript and recomputed every quoted statistic that is traceable from the displayed numbers.

Global assessment
The paper presents a large-scale chirality catalog and an ℓ=1 dipole analysis with an overall null result on the primary estimators. The methodological intent is sound and much of the analysis framework is carefully described. However, there are multiple arithmetic inconsistencies, definition mismatches (most importantly in the definition of the analyzed field Ap), and significance-reporting conflicts that must be resolved for Physical Review D standards. Some results appear numerically inconsistent within the paper, and several statistical claims are reported with a precision that is not supported by the stated Monte Carlo sample sizes. The mask construction (canonical vs subsample mask) is not defined with sufficient clarity to allow independent reproduction of the headline estimator. I list all required fixes below.

Findings

ESSENTIAL

P4-E1 (Abstract, p.1; Sec. IV.D/Table IV, p.5)
Problem: Inconsistent z-score for the monopole-only generative null. The text/abstract claims “reproduced at 99.3% of its observed amplitude” and Table IV lists Data = 1.696×10−2, Null = (1.685±0.007)×10−2 with z = +1.68. Recomputing z = (1.696−1.685)/0.007 = 1.57, not 1.68. The 99.3% reproduction (1.685/1.696=0.9935) is correct, but the z is not.
Required fix: Correct the z-value everywhere it appears (table, abstract, main text) and ensure all derived p/z statements that depend on it are updated. Report also the uncertainty on the 99.3% ratio if you infer it from finite-MC estimates.

P4-E2 (Sec. IV.B, p.4)
Problem: Asymmetry-suppression factor and percentages are inconsistent with Table II. The text states “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%.” From Table II, Catalog A cw fraction is 0.5079 (+0.79%), and Catalog C is 0.4974 (−0.26%). These do not match +2.05% and −0.53%. The −0.53% value appears to be the galaxy-weighted mean ⟨A⟩mask,gw = −0.005294 given later (Appendix A), but that uses a different normalization (Ap divided by Ntotal, not NCW+NCCW).
Required fix: Use a single, explicitly defined asymmetry metric throughout and reconcile/replace the +2.05% and −0.53% claims with the correct numbers tied to that metric. If you choose to report galaxy-weighted-metric values, state that explicitly and stop mixing them with spirals-only metrics from Table II.

P4-E3 (Sec. IV.C eq. 3, p.4; Appendix A.a/c, p.7)
Problem: Inconsistent definition of the analyzed field. In Sec. IV.C, Ap is defined as (NCW−NCCW)/(NCW+NCCW) (spirals only). In Appendix A.c, the NaMaster field is described as Ap = (NCW−NCCW)/Ntotal (where Ntotal includes non-spirals), with a galaxy-weighted mean subtraction ⟨A⟩mask,gw = −0.005294. These are different fields and lead to different monopoles and power spectra.
Required fix: State unambiguously which field definition is used for each estimator (real-space dipole, pseudo-Cℓ, MASTER deconvolution), and ensure all numbers and tables (including Table II percentages and Appendix A quantities) are computed with the stated definition. If both definitions are used in different contexts, label them distinctly (e.g., Aspiral vs Aweighted) and never mix their numerical summaries.

P4-E4 (Sec. II.B, p.2; Appendix B.a, p.7)
Problem: Training-set arithmetic inconsistency. Reported label sources sum to 25,790 (6,637 GZ1 + 17,153 CE-ResNet + 2,000 synthetic negatives), but the paper states the combined training set contains 26,636 images.
Required fix: Reconcile the training-set composition. Provide the complete breakdown that sums exactly to the stated total, or correct the stated total. If additional sources/augmentations are counted, specify them and their counts.

P4-E5 (Sec. IV.D, p.5)
Problem: Version-history language in the body. “... were interpreted in earlier paper versions ...” PRD disallows internal version-history/log prose in the paper body.
Required fix: Remove all references to “earlier paper versions,” “earlier draft(s),” etc., and rewrite in timeless scientific prose (e.g., “We interpret ...”).

P4-E6 (Multiple locations, e.g., Abstract p.1; Sec. VII.b, p.6; Sec. IV.C, p.4)
Problem: Side-by-side σ values from different nulls reported without immediate caveat. The paper correctly states globally that σ values are not directly comparable across nulls. However, there are multiple local juxtapositions (e.g., “real-space dipole 0.43σ and subsample-mask MASTER −0.122σ”) that lack the explicit local qualifier.
Required fix: At every place where σ from two different null procedures are presented side-by-side, add an immediate parenthetical reminding the reader that they are not directly comparable (or append “(different nulls; see Table I)”).

P4-E7 (Abstract, p.1; Table I, p.4; Appendix A, p.7)
Problem: Mask definitions and counts are unclear/inconsistent. You use “canonical mask” and “subsample mask,” but construction rules and their relationship are not clearly defined. The phrase “strict-superset subsample mask (n=5,547,858, fsky=0.659)” calls “n” the weighted sum Nmap,weighted (Appendix A), not a raw count, which is confusing.
Required fix: Define both masks precisely in the main text: pixel-thresholds, sky cuts, and whether weights enter the mask definition. Do not use “n=” for weighted sums. Provide explicit NSIDE=64 pixel-counts for both masks, the count threshold used, and confirm fsky for both. Cross-reference these definitions in Table I and Appendix A to avoid ambiguity.

P4-E8 (Abstract p.1; Sec. IV.D/Table III p.5; Appendix A.a p.7)
Problem: Conflicting significance reporting for the same test. You quote a canonical-mask post-MASTER ℓ=1 residual of “+3.64σ (z=Δ/σnull)” alongside an empirical rank pMC=0.030 (≈1.9σ Gaussian-equivalent). For the same test statistic and null, 3.64σ implies p ~ 2.7×10−4 (two-sided), not 0.03.
Required fix: Choose one coherent significance-reporting convention per test. If you keep both, explain the difference (e.g., Gaussian moment-fit z vs empirical rank p), and do not convert both to “σ” units in parallel. Report the empirical p with its resolution (1/(NMC+1)), and avoid presenting a Gaussian-equivalent “σ” for the empirical p unless you also state which tail convention is used. Consider increasing NMC to stabilize tails if you want to quote tail-area-based σ.

P4-E9 (Sec. VI.A, p.6)
Problem: Fisher-floor derivation is insufficiently specified and uses an fsky=0.46 that is not defined elsewhere. The stated result “3σ floor ~0.29% (from σ(A/2)≈0.048% at Nspiral=3,201,160, fsky=0.46)” lacks a derivation and clear definition of “A/2.”
Required fix: Provide a short derivation with a defined estimator and noise model showing how σ(A/2) is computed (including the role of fsky). Ensure fsky matches one of your masks or justify the 0.46 value. Otherwise, correct the number.

P4-E10 (All MC-based results using NMC=500; e.g., Table I/III/IV, pp.4–5; Appendix A p.7)
Problem: Overprecision relative to MC sample sizes. You quote significances like −0.122σ and +3.64σ and small differences in Cℓ with only NMC=500. The sampling error on σnull from 500 draws is O(√2/(N−1)) ≈ 6%, which propagates into z-values at the 1–10% level. The quoted precision is not supported.
Required fix: Either (i) increase NMC to at least a few thousand for all headline numbers to stabilize σnull and tail ranks, or (ii) report significances with uncertainties that reflect finite-MC estimation error (e.g., via bootstrap on the MC samples) and round accordingly (e.g., −0.12±0.01σ is not meaningful; present pMC instead). Apply consistently to all MC-derived claims.

MAJOR

P4-M1 (Table III, p.5)
Problem: Bandpowers report a “Significance (σ)” with measured Cℓ values, but null means are not shown. Some Cℓ are negative while reported significances are positive (e.g., ℓeff=9: Cℓ=−0.248×10−6, “+2.232σ”), which is confusing without the null mean.
Required fix: Add the null mean ⟨Cℓ⟩null per bandpower (or report ΔCℓ = Cℓ−⟨Cℓ⟩null) so the sign and magnitude of the “significance” are interpretable.

P4-M2 (Appendix A.a, p.7; Sec. IV.D, p.5)
Problem: Claim that monopole subtraction reduces C1 from 2.30×10−5 to 1.51×10−5 (~34%) yet “increases σ from +1.85 to +3.64” is counterintuitive and currently unsupported by numbers. No null means/widths are shown for both cases to justify how significance increases while power drops.
Required fix: Provide the corresponding null mean and σnull for both with- and without-monopole subtraction cases, and show explicitly how the z-values change. If different masks/nulls are involved, state that explicitly.

P4-M3 (Appendix A.c, p.7)
Problem: Ambiguous apodization notation “C 2 2◦ apodization.”
Required fix: Replace with a clear description, e.g., “cosine-squared apodization with a 2° apodization scale.”

P4-M4 (Sec. V.B, p.5)
Problem: Ambiguity in CE-ResNet comparison metric: “cw/ccw = 0.998.” It is unclear whether this is a ratio of counts or a cw fraction of 0.499.
Required fix: Use the same metric throughout your paper when comparing balance (preferably cw fraction fCW or Δf≡fCW−0.5), and rephrase CE-ResNet’s result in your metric for apples-to-apples comparison.

P4-M5 (Sec. IV.C.a, p.4)
Problem: “isotropic-null bootstrap” for the real-space dipole is not sufficiently specified. It is unclear what is resampled (galaxies or pixels), whether the mask is preserved, and how the dipole estimator is defined and normalized.
Required fix: Define the real-space dipole estimator, how uncertainties are obtained (bootstrap scheme), what is held fixed, and how p-values are read off. If the bootstrap is pixel-based, specify the pixelization and minimum counts per pixel used.

P4-M6 (Throughout Sections IV–VII)
Problem: Inconsistent nomenclature for null procedures: “label-shuffle null,” “per-pixel random-label permutation null,” “per-pixel-shuffle null,” “random-label null” appear to refer to similar but not necessarily identical procedures.
Required fix: Standardize the naming and provide a single subsection defining each null precisely (what is permuted, at what granularity, what weights are preserved), and use the standardized terms consistently.

P4-M7 (Sec. IV.B, p.4)
Problem: Claim of spatial uniformity (“all 7 equatorial coordinate slabs within 0.5% of 50/50”) is not substantiated in the text/tables.
Required fix: Provide a small table (or supplemental table) listing the slab-by-slab cw fractions with uncertainties, or include a figure.

P4-M8 (Appendix D.a–f, p.9)
Problem: Cross-spectrum “rℓ=2 = −0.65 with σ = −2.89” lacks a clear definition of r and the null/MC used to compute σ.
Required fix: Define rℓ (normalization, field pairing, pseudo-Cl or deconvolved), state the null model and NMC, and whether the significance is one- or two-sided.

P4-M9 (Figures)
Problem: The paper contains only tables; for a methods-heavy cosmology analysis, lack of figures (mask visualizations, Cℓ curves with null bands, Ap maps) hinders auditability and clarity.
Required fix: Add at least: (i) the two masks (canonical and subsample) with fsky and pixel thresholds; (ii) the ℓ=1 anchor spectrum point with null band; (iii) the low-ℓ bandpower spectrum (with null means and bands); (iv) possibly the cross-spectrum diagnostic at ℓ=2.

MINOR

P4-N1 (Table II, p.4)
Problem: Deviations in σ appear slightly inconsistent with recomputation (e.g., 28.8σ vs ~28.3σ for 0.5079 with σ=0.000279).
Required fix: State the exact σ formula used (binomial with p or p≈0.5 approximation) and round consistently. Alternatively, provide 2–3 significant figures uniformly.

P4-N2 (Sec. IV.C.b, p.4–5; Table III)
Problem: Reporting Cℓ in units “×10^−6 (sr)” is correct, but state explicitly in the caption that these are deconvolved Cl for a dimensionless spin-0 field so that Cl has units of sr.

P4-N3 (Appendix C.c, p.8)
Problem: Look-elsewhere correction language: “Bonferroni/BH across ~650 directions” is vague.
Required fix: Provide the exact number of tested directions and the BH procedure parameters; state whether Bonferroni or BH was adopted for the quoted family-wise p-value.

P4-N4 (Data Availability, p.10)
Problem: URLs appear with line-break hyphens/spaces (“galaxy- chirality- catalog”).
Required fix: Ensure URLs are correct and machine-copyable in the final manuscript (no inserted spaces). Provide DOIs/Zenodo where possible.

P4-N5 (Appendix A.a, p.7)
Problem: Use of “seed: numpy.random.seed(42)” for the nulls is fine, but consider noting that key results are insensitive to seed choices (already implied by multiple tests but could be made explicit).

P4-N6 (Appendix B.c, p.7–8)
Problem: Very small samples for D4-TTA validation (N=1,558 and 1,988) and reporting argmax flip rates with percent-level precision may overstate stability.
Required fix: Either expand the sample or soften the precision (e.g., report with one decimal place and stress that these are qualitative checks).

Other checks
- Bibliography entries appear plausible and correctly attributed by year/journal for key references; however, please double-check [7] wording vs your “cw/ccw” metric (P4-M4).
- The abstract’s “falsification criterion” appears somewhat overstated given the strong dependence on your pipeline/null; suggest softening (optional, but recommended).

Page length
- 10 pages is reasonable for the scope, provided the above clarifications and a minimal figure set are added.

## Summary recommendation
MAJOR REVISIONS

While the core methodology and the main null result are promising, the manuscript has multiple essential inconsistencies (field-definition mismatch, training-set arithmetic, significance misreporting, mask-definition ambiguity) and several major clarity and reporting issues. These must be corrected for the analysis to be auditable and for the statistical claims to meet PRD standards. With these fixes (and addition of minimal figures), the paper could be reconsidered.

---

## PASS 2 — self-critique findings (what initial review missed)

ADDITIONAL FINDINGS (fresh-eye pass)

ESSENTIAL

P4-E11 (Abstract p.1; Sec. IV.C.a p.4)
Problem: p–z inconsistency for the real‑space dipole. The abstract and Sec. IV.C.a state “+0.43σ (p=0.30, isotropic-null bootstrap, NMC=10,000)”. A two-sided Gaussian p=0.30 corresponds to z≈1.04σ; even a one-sided mapping gives z≈0.52σ, not 0.43σ. As written, p and z are mutually inconsistent for this test.
Required fix: Report either z or p consistently with a clearly stated tail convention, and ensure they match numerically. If the bootstrap p is not converted via a Gaussian mapping, state the conversion rule (or drop the σ-equivalent).

P4-E12 (Abstract p.1; Sec. VI.A p.6; Appendix E.b p.9)
Problem: Ambiguous and inconsistent definition of the “high-confidence” sample. The abstract mentions “471,049 high-confidence per-spiral after peqCW > 0.9”, but Sec. VI.A uses this N for injection-recovery without restating the exact cut, and Appendix E.b discusses HC-broad-0.6 (peq>0.6) and HC-strict (peq>0.8) that do not match the abstract’s peqCW>0.9. It is unclear whether “high-confidence” thresholds refer to max-class confidence, a CW-only threshold, or spiral-only confidence.
Required fix: Define the HC sample(s) unambiguously in one place (which probability, which class channels, and which threshold). Ensure the abstract’s threshold matches the body, or adjust the abstract text. If different HC cuts are used for different tests, label them distinctly and use consistent Ns.

P4-E13 (Sec. IV.C.a p.4; Appendix E.b p.9)
Problem: Contradictory real-space dipole significances for the full Catalog C. Sec. IV.C.a reports a “simple dipole” of 0.43σ (null: isotropic bootstrap), while Appendix E.b states “Catalog C-full +4.31σ monopole-preserving dipole.” The paper does not define a “monopole-preserving dipole” estimator in the main text, and the 10× difference in σ for ostensibly similar dipole measurements on the same catalog is not reconciled.
Required fix: Define the “monopole-preserving dipole” estimator precisely (data vector, mean subtraction, weighting, bootstrap scheme) and explain why its σ differs from the “simple dipole” by an order of magnitude. If different nulls are used, state so explicitly and avoid juxtaposing σ values without an immediate caveat and explanation.

MAJOR

P4-M10 (Abstract p.1; Sec. IV.D p.5)
Problem: Null-procedure conflation within a single phrase. The abstract describes the canonical-mask residual as “+3.64σ (z=Δ/σnull; empirical rank pMC=0.030; 500-MC binomial per-pixel-shuffle null).” A “binomial” generative null and a “per-pixel random-label shuffle” null are distinct procedures; the phrase implies both at once.
Required fix: Specify exactly which null was used to compute z and pMC for the +3.64σ canonical result. If both nulls were run, report them separately with separate statistics and do not conflate terminology in the same parenthetical.

P4-M11 (Abstract p.1; throughout)
Problem: Misuse of “pseudo-Cℓ” wording for deconvolved spectra. The abstract calls the headline result a “MASTER-deconvolved single-mode pseudo-C1.” Once MASTER-deconvolved, it is no longer a pseudo-Cℓ.
Required fix: Rename consistently as “deconvolved C1” (reserve “pseudo-Cℓ” for the raw, mask-coupled spectra prior to deconvolution).

P4-M12 (Appendix D.g p.9; Abstract p.1)
Problem: Signed “σ” reported (e.g., “σ = −2.89” for rℓ=2) without a clear sign convention. A negative σ is unconventional and ambiguous: does the sign indicate anti-alignment of r or simply that Cmeas<⟨Cnull⟩?
Required fix: Define the sign convention for z-scores on cross-spectra and bandpowers. Prefer reporting |z| with a separate statement about the sign of r or ΔCℓ, or explicitly define z = sign(Δ)·|Δ|/σnull and use it consistently.

MINOR

P4-N7 (Sec. VII.d p.6)
Problem: Ambiguous scientific-notation formatting. “≥107 galaxies” is ambiguous as “at least 107 galaxies” instead of “≥10^7 galaxies.”
Required fix: Typeset as 10^7 (or 1e7) to avoid ambiguity.

P4-N8 (Appendix C.c p.8)
Problem: Quoting pLEE ≤ 10−4 without noting MC resolution. With NMC=10,000, the minimum resolvable p is 1/(NMC+1)=9.999×10−5.
Required fix: Report pLEE with the MC-resolution caveat (e.g., “pLEE ≤ 1/(NMC+1) ≈ 10−4”) and, if desired, increase NMC to tighten the bound.

P4-N9 (Appendix B, Table V p.8)
Problem: Unclear phrasing for T7 (“confidence calibration (qualitative, < 50% at confidence > 0.9)”). As written, the condition is ambiguous and hard to interpret.
Required fix: Clarify the intended metric (e.g., “fraction of objects with calibrated confidence >0.9 whose predicted class is incorrect < 50%” or provide an ECE/mECE value). If qualitative only, soften precision and explain the diagnostic intent.

P4-N10 (Multiple places)
Problem: Exactness claims that are by-construction rather than empirical (e.g., “flip-swap correlation = 1.000”). While true algorithmically for the TTA protocol, phrasing as a measured statistic can mislead.
Required fix: Rephrase to note that flip-equivariance is enforced by construction through the inference protocol (and optionally report numerical verification to finite precision).

Explanation
I focused on fresh classes of inconsistencies not captured in the first review. The most critical new items are the p–z mismatch for the real-space dipole (P4-E11), the inconsistent/undefined “high-confidence” sample thresholds including the 471,049-sample usage (P4-E12), and the contradictory real-space dipole significances for the same catalog stemming from an undefined “monopole-preserving dipole” estimator (P4-E13). I also flagged null conflation within a single clause (P4-M10), misuse of the “pseudo-Cℓ” term for deconvolved spectra (P4-M11), and ambiguous signed-σ reporting (P4-M12). Additional minor notational and reporting clarifications are listed under P4-N7–N10.