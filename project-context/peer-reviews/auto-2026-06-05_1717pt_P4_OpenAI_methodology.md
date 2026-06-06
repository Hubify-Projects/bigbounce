# P4 auto-2026-06-05_1717pt — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (8312 chars)
**Wall time**: 305.0s

---

Referee Report (Methodology Rigor, Physical Review D)

I have read the full 10-page manuscript, checked all equations for dimensional consistency, recomputed every quoted percentage, ratio, and σ where possible from the displayed numbers, and audited the tables for internal consistency. Below I list findings, each with an ID, location (section and page), problem statement (with quoted text where appropriate), and the required fix. Severities: ESSENTIAL (blocking), MAJOR, MINOR, NIT.

ESSENTIAL

P4-E1 (Sec. IV B, p.4; Table II; also Sec. VII, p.6)
Problem: Inconsistent “global monopole” magnitudes. The text states “3.86× asymmetry-suppression factor from raw +2.05% to equivariant −0.53%.” From Table II, Catalog A cw/(cw+ccw)=0.5079 implies A=2f−1=1.58%, not 2.05%. For Catalog C, 0.4974 implies A=−0.52–0.53% (consistent). The “+2.05%” is not consistent with Table II and Eq. (A/2 mapping).
Required fix: Correct the raw asymmetry percentage (likely +1.58%) and recompute the “suppression factor” (should be ≈1.58/0.53 ≈ 2.98), or explicitly define what the 2.05% quantity is and show its derivation from numbers in the paper. Ensure all “asymmetry” values use a single definition, and add a clear conversion note between fraction offset (fCW − 0.5) and A=2fCW−1 where used.

P4-E2 (Sec. IV D, p.5)
Problem: Version-history language in body text. “were interpreted in earlier paper versions as mask-geometric leakage…” This violates journal style and the review instruction to remove internal version history references.
Required fix: Remove all references to “earlier paper versions,” “earlier drafts,” or similar internal-history language. State the present interpretation without referring to draft history.

P4-E3 (Multiple locations, e.g., Abstract p.1; Sec. IV D last paragraph p.5; Sec. VII b p.6)
Problem: Side-by-side σ values from different null procedures are juxtaposed without an explicit local reminder that they are not directly comparable (e.g., “the full-catalog real-space dipole at +0.43σ and the subsample-mask MASTER at −0.122σ,” or “post-MASTER ℓ=1 … −0.122σ; the canonical-mask post-MASTER residual is +3.64σ”). The Abstract contains the general caveat, but the manuscript does not repeat this at every juxtaposition as required.
Required fix: At every point where σ values from distinct nulls are compared or listed together, add an explicit parenthetical note (e.g., “not directly comparable; different nulls”) or present them only within a table that explicitly maps each σ to its null (as in Table I), and cross-reference that table inline.

P4-E4 (Sec. VI A, p.6)
Problem: “Fisher Poisson floor at 3σ is ∼0.29% (from σ(A/2)≈0.048% at Nspiral = 3,201,160, fsky = 0.46).” This is not reproducible from stated inputs. For simple counting near p=0.5, σ(f) ≈ 0.5/√N ≈ 0.028% (no fsky factor). Even applying fsky=0.46 as N_eff ≈ N×fsky gives σ≈0.041%, not 0.048%. The quoted fsky=0.46 is itself inconsistent with the two masks reported elsewhere (0.49005 and 0.659).
Required fix: Provide a transparent derivation for σ(A/2) that reconciles all factors (mask area, pixelization, weighting, any additional penalties). Use the actual mask used for the claimed bound, and correct the numerical values (σ and 3σ threshold) accordingly. If the 0.048% comes from a more complex Fisher analysis, include the formula and inputs.

P4-E5 (Reproducibility of primary estimator; Sec. IV C–D pp.4–5; Appendix A p.7)
Problem: The “strict-superset subsample mask” (fsky=0.659; n=5,547,858) is insufficiently specified. The main headline result −0.122σ depends on this mask and the weight definition Wp=Nall, but the paper does not precisely define how the mask is constructed (pixel thresholds? apodization? inclusion/exclusion criteria) nor provide the actual mask file.
Required fix: Precisely define the construction of the subsample mask (selection criteria, pixel thresholds, apodization kernel and radius, coordinate frame, NSIDE, any smoothing), and provide a link to the exact mask and weight maps used (with a persistent DOI). State whether the “≥10 spirals per pixel” threshold applies to this mask or only to the canonical mask.

P4-E6 (Table I, p.4; Appendix C.c p.8)
Problem: Contradictory look-elsewhere accounting for the hemisphere scan. Table I reports “hemisphere LEE (MC) … pLEE ≤ 10−4” (already look-elsewhere corrected by MC over the scan), but Appendix C says “the direct-MC look-elsewhere test … gives pLEE ≤ 10−4 … the conservative Bonferroni/BH penalty across ∼650 directions reduces post-LEE significance to <1σ.” Applying Bonferroni/BH after a max-statistic MC already includes the LEE double-counts the correction.
Required fix: Use one consistent LEE correction. If you use direct-MC max-statistics to derive pLEE, do not further apply Bonferroni/BH. If you use Bonferroni/BH, state the local p and the number of trials, and do not also report a pLEE from max-stat MC. Present a single, coherent global p-value and its conversion to σ if desired.

P4-E7 (Table III, p.5)
Problem: Bandpowers list Cℓ values that are negative (e.g., −0.248, −0.387, … in units of 10^−6 sr) alongside positive “Significance (σ)” values (+2.232, +2.626, …), but null means are not provided. Without the null means for each band, the z-scores cannot be verified, and negative deconvolved Cℓ for a variance-like quantity require explicit handling discussion.
Required fix: Add the null means for each bandpower to the table (or in text) and clearly define z≡(Cmeas−⟨Cnull⟩)/σnull including sign convention. Add one sentence explaining why negative deconvolved Cℓ can appear (unbiased estimators with finite noise may produce negative estimates) and that this does not violate positivity of the underlying spectrum.

P4-E8 (Appendix A.a, p.7)
Problem: Weight/field construction could reintroduce coupling. The field is Ap using spirals only, but weights Wp=Nall include non-spirals; the text asserts that “depth weighting does not introduce a monopole–dipole coupling because the galaxy-weighted mask-mean is subtracted,” but no demonstration is given. Given that the primary result relies on this, a short proof or robust test is required.
Required fix: Provide an explicit argument (or empirical test) showing that, with your procedure (galaxy-weighted mean subtraction and the stated mask), use of Wp=Nall does not bias the ℓ=1 estimate. A simple MC with a known injected dipole under varying depth patterns would suffice; include summary statistics or move to SM with a clear pointer.

MAJOR

P4-M1 (Abstract p.1; Sec. IV C, p.4)
Problem: Terminology inconsistency. “MASTER-deconvolved single-mode pseudo-C1” is self-contradictory: pseudo-Cℓ typically refers to the masked-sky estimator before deconvolution; after MASTER, you should refer to decoupled Cℓ or deconvolved Cℓ.
Required fix: Replace “pseudo-C1” with “deconvolved C1” or “decoupled C1” wherever applicable.

P4-M2 (Sec. VII.a–b, p.6)
Problem: Overclaim versus Shamir results: “present null disfavors the Shamir ∼2–4% detection class by a factor of ∼6–12 under our pipeline.” Your empirical 50%-recovery-at-3σ threshold is 0.75% for the observed amplitude; that implies a factor of ≈2.7–5.3 relative to 2–4%. The quoted 6–12× is not supported by your stated sensitivity.
Required fix: Recompute and revise the “factor” comparison using a quantitative amplitude limit (e.g., 95% CL upper limit under your null) on the same observable and mask. If you cannot produce a rigorous upper limit, soften the claim to a qualitative statement without numerical factor or provide a derivation.

P4-M3 (Table I and text multiple places, p.4–5; Appendix A, p.7)
Problem: Finite-MC precision. Many σ values and tail probabilities are quoted with high precision (e.g., +3.64σ, +6.097σ, p=0.030) from NMC=500 null realizations. The uncertainty on σnull from 500 draws is ≈6% (sqrt(2/(N−1))), which propagates to z. Tail z>6 cannot be reliably validated with 500 draws.
Required fix: Either (a) increase MC realizations (e.g., ≥5,000) for all reported NaMaster σ and bandpower nulls to stabilize σnull and allow stable tail estimates, or (b) accompany each σ with an uncertainty due to finite-MC (and avoid quoting >3σ tails from 500 draws). For p-values, report binomial CIs (e.g., Clopper–Pearson) given the finite NMC resolution.

P4-M4 (Sec. IV C.a, p.4)
Problem: Unsupported σ claim. “Catalog A (raw) shows … +6.48σ pre-MASTER pseudo-Cℓ in the lowest bandpower.” No numeric values or null definition are provided for this specific claim; not tabulated.
Required fix: Provide the measured pseudo-Cℓ value, its null mean and σnull for the “lowest bandpower,” and define the band exactly (ℓ range, bin edges), so the +6.48σ can be verified.

P4-M5 (Sec. III C, p.3; Appendix B.c, p.7)
Problem: Justification for restricting to Z2 TTA. The D4 validation is done on two ≈2,000-galaxy holdouts, finding small mean shifts but 21.4% argmax flips. At sub-percent cosmological sensitivity, the global impact of rotation equivariance needs to be bounded on the full dataset, not small holdouts.
Required fix: Provide a quantitative bound (on the full sample or a statistically representative large subset) on the difference between Z2-TTA and D4-TTA in the derived sky maps/dipole estimator. E.g., compare the real-space dipole amplitude and C1 under Z2 vs D4, with uncertainties, to demonstrate negligible impact on the headline result.

P4-M6 (Appendix A.a; Table II; Sec. IV B, pp.4–7)
Problem: Mixed use of “fraction offset” and “A” without a conversion note. Example: ⟨A⟩mask,gw = −0.005294 (−0.5294%), while Table II reports the fraction difference −0.26%. Both are internally consistent (A=2f−1), but the text alternates without explicitly reminding the reader.
Required fix: Insert a one-line note early in Sec. IV defining A and its relationship to fCW and use consistent units thereafter; whenever “%” is used, state whether it is A (full asymmetry) or fraction offset from 0.5.

P4-M7 (Appendix A.b–c, p.7; Table III p.5)
Problem: Binning description incomplete. You state single-ℓ bins (nlb=1) for the headline ℓ=1; subsequently, Table III lists bandpowers for ℓeff=4,9,14,19,24. The exact bin definitions for these bandpowers (ℓ ranges [2,6], …) are shown in the table, but the NaMaster bin configuration used to generate those bands is not described (e.g., nlb=5 with start at ℓ=2).
Required fix: Add the exact bin configuration used for the canonical-N recompute (start ℓ, bin width nlb) to Appendix A for full reproducibility.

P4-M8 (Appendix C.c, p.8; Table IV, p.5)
Problem: Inconsistency in hemisphere scan grid. Appendix C says hemispheres tested at 10° increments (~650 directions). Table IV lists “NSIDEdir=8.” NSIDE=8 has 768 pixels; a 10°-increment grid has a different count. This matters for LEE.
Required fix: Specify the exact grid used (HEALPix NSIDE or polar steps), the number of trial directions in the scan, and ensure consistency between text and table. Adjust the LEE accounting if the number of trials changes.

MINOR

P4-N1 (Sec. V.B, p.5)
Problem: “CE-ResNet achieves cw/ccw = 0.998.” Ambiguous (ratio or fraction?). Likely ratio close to unity.
Required fix: Clarify as “cw/ccw ratio = 0.998 (i.e., 49.9%/50.1%)” or equivalent.

P4-N2 (Data Availability, p.9)
Problem: URLs broken across lines (“galaxy- chirality- catalog”) with inserted spaces/hyphens; these will not resolve.
Required fix: Provide stable, copy-pasteable URLs or DOIs (no spaces/hyphens introduced by line breaks). Optionally add a Zenodo DOI.

P4-N3 (Sec. II.A, p.2)
Problem: The δ=+32° demarcation between DECaLS and BASS+MzLS is given without explicit citation at that point.
Required fix: Add an inline citation to Dey+2019 [8] where this boundary is described.

P4-N4 (Table I caption, p.4)
Problem: “each galaxy is counted once” in Nmap,weighted can be misleading since Wp sums counts; while duplicates across pixels do not occur with HEALPix on static sky, clarify that each catalog object contributes to a single pixel’s Wp.
Required fix: Rephrase: “Nmap,weighted equals the sum over pixels of Wp (each catalog object contributes to exactly one pixel).”

P4-N5 (Appendix A.c, p.7)
Problem: Notation “C 2 2◦ apodization” is unclear; appears to be “cosine-squared 2° apodization.”
Required fix: Replace with “cosine-squared apodization with 2° radius” or define notation.

P4-N6 (Sec. IV B, p.4)
Problem: Slight numeric mismatch: “9.5σ from 0.5000” for Catalog C fraction 0.4974 ± 0.000279 gives ≈9.3σ. Small, but keep consistent rounding.
Required fix: Adjust to “≈9.3σ” or recompute σ with the exact binomial variance at p=0.4974 if that yields 9.5σ and state it.

NIT

P4-NIT1 (Throughout)
Problem: Minor capitalization/style inconsistencies (“cw/ccw” vs “CW/CCW”; “peq” vs “P_eq”). 
Required fix: Standardize capitalization and symbol formatting.

P4-NIT2 (Sec. III B, p.3)
Problem: Dropout “d=0.3”/“d=0.2” shorthand may be unclear outside ML audience.
Required fix: Spell out “dropout probability 0.3/0.2.”

P4-NIT3 (Appendix B, p.7)
Problem: Use of “Z2” and “D4” without first defining the groups in text.
Required fix: Add a brief parenthetical: “Z2 (horizontal reflection), D4 (dihedral group of square rotations/reflections).”

Additional checks

- Dimensional analysis: All equations are dimensionless or use standard Cℓ units (sr) appropriate for scalar fields; OK.
- Counts and fractions: Class counts on p.3 (18.78%, 18.99%, 62.23%) sum to 100%; spiral fraction 37.78% of 8,474,531 equals 3,201,160; OK.
- HEALPix: NSIDE=64 → Npix=49,152 and pixel area ~0.839 deg²; OK.
- Table IV ratio: (3.48−1.69)/0.41=4.37 vs reported +4.42; small rounding difference; acceptable once you specify rounding.
- C1 deconvolved null: From Sec. IV.C.b, (1.494−1.546)/0.429=−0.1219 → −0.122σ; OK.
- “99.3%” reproduction by monopole-only null: 1.685/1.696=0.9935; OK.

Length and scope

The paper is 10 pages and focuses on a single methodological conclusion (null ℓ=1 on a defined mask) plus a systematic analysis of a canonical-mask residual. The length is not excessive for PRD, provided the ESSENTIAL/MAJOR issues above are addressed and some clarifications are added for reproducibility (mask definition, MC sizes, LEE accounting, and internal numeric consistency).

## Summary recommendation
MAJOR REVISIONS

The core methodology is potentially sound and the main null result appears plausible, but there are several essential corrections needed before publication: (i) resolve numeric inconsistencies (notably the 2.05% vs 1.58% asymmetry and the Fisher floor derivation), (ii) correct the double LEE accounting and table labeling, (iii) fully specify the “subsample” mask and weights used for the headline estimator, (iv) present bandpower null means to justify z-scores, and (v) tighten the use and juxtaposition of σ from different nulls. Some claims (e.g., 6–12× disfavoring Shamir) need quantitative revision. Increasing MC sizes or reporting uncertainties is also required for quoted significances, especially in the tails. With these fixes, the paper could meet PRD methodological standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (Fresh-eyes audit)

ESSENTIAL

P4-E9 (Field definition inconsistency; Sec. IV.C Eq. (3) p.4 vs Appendix A.c p.7)
Problem: Contradictory definitions of the asymmetry field Ap. In Sec. IV.C, Eq. (3) defines Ap = (NCW−NCCW)/(NCW+NCCW) (spirals-only denominator), and Appendix A.a reiterates “spirals only.” But Appendix A.c states “Ap = (NCW − NCCW)/Ntotal,” i.e., denominator includes non-spirals (NS), directly contradicting Eq. (3) and A.a. The reported monopole ⟨A⟩mask,gw = −0.005294 matches the spirals-only definition, not the all-galaxies denominator.
Required fix: Resolve the inconsistency unambiguously. State a single, consistent Ap definition in both main text and Appendix A. If any results used the all-galaxies denominator, re-run and update all affected numbers. If all results used spirals-only, correct Appendix A.c and explicitly note the denominator choice wherever Ap appears.

P4-E10 (Primary real-space dipole estimator reproducibility; Sec. IV.C.a p.4)
Problem: The real-space dipole estimator (+0.43σ, p=0.30) lacks a precise definition. It is unclear how the dipole vector is estimated from pixelized Ap (weighting, mask handling, mean subtraction), what weights were used per pixel, and how the isotropic-null bootstrap was implemented (resampling scheme, preservation of depth pattern, number of galaxies per pixel, etc.).
Required fix: Provide the explicit estimator: e.g., weighted least squares of Ap onto the three Y1m, or a vector-sum estimator, including the exact pixel weights, treatment of the global monopole, and mask handling. Describe the bootstrap procedure sufficiently to reproduce p=0.30 (resampling unit, number of resamples, whether galaxy depths/weights are preserved).

P4-E11 (Falsification criterion lacks derivation; Abstract p.1; Sec. VII.d p.6)
Problem: The statement “A future survey detecting a chirality dipole at σ>5 with amplitude ≳0.75% at ≥10^7 galaxies would falsify the present null” is not quantitatively justified in the text. No scaling of σ with N, fsky, classification noise g, or depth weighting is shown to support “≥10^7 galaxies.”
Required fix: Provide a quantitative derivation linking amplitude, number of galaxies, sky fraction, and classification dilution (g = 2a−1) to the σ threshold. If the “≥10^7” arises from a specific mock or Fisher model, show the formula and inputs. Otherwise, remove or soften the specific N requirement.

MAJOR

P4-M9 (Mixed masks and nulls in a single table; Table III p.5)
Problem: Table III combines a subsample-mask ℓ=1 single-mode (fsky=0.659) with bandpowers computed on the canonical mask (fsky≈0.491), but presents them in one table under a single header. This risks cross-comparison of σ values from different masks and nulls. The caption text also uses “canonical single-mode ℓ=1 … (subsample mask),” which is internally confusing.
Required fix: Split the results by mask into separate tables or add a clear, prominent row-level annotation of the mask and null used for each entry. Remove the word “canonical” from the row describing the subsample-mask result. Add a reminder that σ from different nulls/masks are not directly comparable at the point of juxtaposition (or cross-reference Table I mapping).

P4-M10 (Unspecified “38 bandpowers” in joint χ2; Table III p.5; Appendix A p.7)
Problem: The caption reports “Joint χ2/dof (38 bandpowers) = 161.2/38,” but Table III only lists 6 entries (ℓ=1 single mode + 5 bandpowers) and the binning scheme used to reach 38 bandpowers is not described anywhere.
Required fix: Specify the exact bandpower binning yielding 38 dof (start ℓ, end ℓ, bin width, any ℓ cuts), list or provide a link to the full set of bandpowers used in this χ2, and state the null mean and covariance used to compute the χ2.

P4-M11 (Unphysical tail z-values; Appendix D.f p.8–9)
Problem: The WLS template fit section reports extreme z-values (e.g., z = −264.5; zboot ≈ −18.1) for the “interpretation (i)” amplitude. Such magnitudes are not credible without a thorough treatment of covariances, mask-induced mode coupling, and finite-MC uncertainty, and are inconsistent with the rest of the manuscript’s conservative stance.
Required fix: Avoid quoting |z|≫10. Report confidence intervals (e.g., 68%/95%) on Adipole under both naive and block-bootstrapped covariances, and discuss the limits qualitatively. If you must report a z, cap it at a reasonable value or present the corresponding p-value floor given finite sample size and modeling assumptions.

P4-M12 (Inadequate metadata-leakage test; Appendix B.d p.7)
Problem: Test T5 uses simple linear correlation r(pCW, RA/Dec), but RA is a circular variable and Dec is not a sufficient proxy for spherical systematics. This can miss leakage patterns (e.g., low-ℓ spherical harmonics, survey leg structure).
Required fix: Replace or supplement T5 with a spherical-harmonic leakage test (e.g., regression of pCW onto low-ℓ Yℓm or onto known footprint templates) and report the resulting coefficients and uncertainties. Alternatively, use circular statistics for RA and explicitly test for low-ℓ structure.

P4-M13 (Ambiguous performance metrics; Appendix B.a p.7)
Problem: “Headline 93.7% three-class accuracy (with augmentation active); post-hoc evaluation without augmentation yields 94.9%.” It is unclear whether these are train/validation/test metrics, on which split, and whether augmentation refers to training-time or evaluation-time transforms. As written, the no-augmentation result being higher than with augmentation suggests evaluation protocol ambiguity.
Required fix: Clearly report accuracy/recall/precision on the held-out validation split only, with and without test-time augmentation, and state the dataset sizes. If reporting training-set metrics, label them explicitly and do not mix them with validation results.

P4-M14 (LEE p-value resolution limit; Table I p.4; Appendix C.c p.8)
Problem: The reported hemisphere-scan pLEE ≤ 10^−4 is at the resolution floor for NMC=10,000. No binomial CI is provided. This precision issue is separate from the earlier double-counting concern and needs its own qualification.
Required fix: State pLEE= k/NMC with Clopper–Pearson CI and emphasize the resolution limit. If stronger precision is needed, increase NMC.

MINOR

P4-N7 (Minor rounding mismatches in Table II; p.4)
Problem: The reported “Dev. (σ)” values do not exactly match the listed fractions and σ. For Catalog A: (0.5079−0.5)/0.000279 ≈ 28.3 (paper lists 28.8). For Catalog B: ≈14.3 (paper lists 14.6). For Catalog C, you already address a similar mismatch elsewhere; please also fix A and B for consistency.
Required fix: Recompute and update the “Dev. (σ)” entries with consistent rounding and the exact σ used.

P4-N8 (Terminology clarity; Table III caption p.5)
Problem: The phrase “canonical single-mode ℓ=1 … (subsample mask)” is confusing; “canonical” elsewhere denotes the fsky≈0.49 mask, not the subsample mask at fsky=0.659.
Required fix: Replace with “subsample-mask single-mode ℓ=1” (or similar) to avoid confusion.

P4-N9 (Bias test T7 wording; Appendix B.d p.7)
Problem: “T7 confidence calibration (qualitative, < 50% at confidence > 0.9)” is unclear as written.
Required fix: Rephrase T7 to precisely state the expected and observed calibration behavior (e.g., “well-calibrated probabilities: fraction of correct labels among predictions with p>0.9 is ≥90%”). If only qualitative, say so explicitly and remove the “< 50%” fragment.

P4-N10 (Versioned artifacts)
Problem: Data/code links do not include commit hashes or DOIs for masks/weight maps and analysis outputs.
Required fix: Add a Zenodo (or equivalent) DOI for all key artifacts (masks, weight maps, bandpower files, MC outputs) and cite the exact git commit hashes used to produce the headline numbers.

Explanation

The most critical new issue is the internal contradiction in the definition of the asymmetry field Ap between the main text and Appendix A.c; this impacts the core Cℓ analysis and must be corrected and documented. Additional reproducibility gaps (real-space dipole estimator), table construction confusion (mixing masks in Table III without crystal-clear labeling), and over-precise tail z-values in Appendix D also require attention. Minor numeric and wording cleanups are listed to tighten consistency.