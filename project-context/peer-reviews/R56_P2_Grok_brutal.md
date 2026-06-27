# P2 R56 — Adversarial journal referee with PDF rendered as images (sees figures)

**Reviewer**: `Grok_brutal`
**Model**: `grok-4.3`
**Input PDF**: `/private/tmp/R56_P2/02_full_draft.pdf` md5=592c7849 pages=28
**Input format**: NATIVE PDF (rasterized to PNG images, 150 DPI) + pass-2 NO_NEW
**Wall time**: 297.3s

---

**Referee Report**

**Paper:** P2  
**Journal:** Physical Review D

**ESSENTIAL findings**

P2-E1 (Abstract, p. 1; Sec. IV, p. 9). The abstract headline range “2.6–5σ” after the full systematic budget is not supported by a single, consistently applied procedure. The 5.2–5.5σ figure uses the noise-weighted central value r = 0.84 with only the Heinrich et al. baseline; the 2.6σ floor requires the simultaneous application of the 30 % b_φ widening + GR marginalization (σ_GR = 1.0) that is presented only as an “illustrative stress test” in Sec. VII and Table IV. These two numbers cannot be juxtaposed without an explicit statement that they are not directly comparable. Required fix: replace the abstract range with the single most conservative all-in number that appears in the body (≈ 2.6σ) or remove the combined range entirely.

P2-E2 (Abstract, p. 1; Sec. VI, pp. 11–14; Table II). The abstract Bayes-factor envelope “BF ≈ 9–14” is taken from the r → 1 (no-rebooking) endpoint of the noise-weighted distribution. The body (Table II, caption and Sec. VI.C) shows that the physically realized value after template mismatch is r ≈ 0.84, which lowers every entry by ≈ 15–20 %. The quoted abstract range therefore does not correspond to the calculation that is actually used for the detection significance. Required fix: either recompute the entire Bayes-factor table at the headline r = 0.84 or delete the BF numbers from the abstract.

P2-E3 (Sec. II, pp. 3–5; Sec. III.B, p. 8). The 10 000-sample null-space scan yields a 16th–84th percentile range r ∈ [0.70, 0.99] under uniform weighting, yet the headline forecasts adopt only the median r = 0.84–0.85. No figure or table propagates the full width of this distribution into the final σ(f_NL) or BF values. The quoted 2.6–5σ and BF ranges are therefore point-estimate results, not marginalised results. Required fix: either marginalise over the coefficient ensemble or state explicitly that all quoted significances are conditional on the median coefficient vector.

P2-E4 (Abstract, p. 1; Sec. IV, p. 9). The abstract states that the analysis is “a SPHEREx sensitivity recast”. The body never recomputes the Heinrich et al. multi-tracer Fisher matrix; it only rescales an external number by the template-overlap factor r. This is not an independent forecast. The abstract must not imply otherwise.

**MAJOR findings**

P2-M1 (Length). The manuscript is 28 pages. The incremental methodological content (quantification of a single template mismatch + illustrative Bayes-factor comparison) does not justify this length. Recommended maximum: 12–14 pages.

P2-M2 (Sec. VI, Table II). The Bayes-factor results are shown for four different prior widths and two different competitor priors. The abstract and Sec. VI headline nevertheless quote a single “recommended” column (σ_theory = 1.0, broad multifield). The extreme prior sensitivity (BF varies from 4 to 17) is not reflected in the abstract or in the main-text summary sentence on p. 11.

P2-M3 (Sec. VII, Table IV). The consolidated systematic budget adds GR marginalisation and b_φ widening in quadrature after the fact. No joint marginalisation over all nuisance parameters is performed, and the paper never demonstrates that the additive-quadrature approximation remains valid once the full covariance is restored.

P2-M4 (Fig. 2, p. 11; Sec. IV). The error bars on the MegaMapper bars are stated to be “illustrative 3–7σ design uncertainty”. No quantitative mapping from instrument parameters to those bars is supplied, rendering the comparison with SPHEREx non-reproducible from the published material.

**MINOR findings**

P2-m1 (Sec. II.C, p. 6). Assumption (d) (“faithful cubic-order transmission”) is verified only at linear order in Ref. [1]. The paper repeatedly states that the prediction is “robust across the bounce class” while acknowledging that a full cubic-order calculation is absent. The wording should be changed to “conditional on assumption (d) verified only at linear order”.

P2-m2 (Eq. 7, p. 9). The heuristic scaling δC/C_Gauss ∼ f_NL² Δ_ζ²(k)/N_modes is presented without a derivation or reference to a prior derivation. A one-sentence justification or citation is required.

P2-m3 (Data Availability statement, p. 24). The release DOI is given, but the commit hash for the exact version of the repository used to produce the tables and figures in the submitted manuscript is not stated. Add the frozen hash.

**NIT findings**

P2-n1. Several figure captions (Figs. 2, 5) contain parenthetical remarks that belong in the text (“see Sec. VII”). Move to body.

P2-n2. The phrase “stress-test branch only” appears twice (pp. 2 and 6) with slightly different wording; standardize.

**Summary recommendation**

**MAJOR REVISIONS**

The manuscript is a careful but narrowly incremental recast whose central numerical claims in the abstract are not reproducible from the calculations that are actually performed once all stated caveats and prior sensitivities are applied simultaneously. The length is excessive for the added content. The required fixes are (i) alignment of every abstract headline number with the single most conservative, fully propagated result in the body, (ii) explicit marginalisation or clear qualification of the template-coefficient uncertainty, and (iii) substantial shortening. Until these are addressed the paper does not meet the evidentiary standard expected by Physical Review D.