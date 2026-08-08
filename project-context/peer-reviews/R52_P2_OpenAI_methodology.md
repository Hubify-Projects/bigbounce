# P2 R52 — Physical Review D methodology referee with full PDF access

**Reviewer**: `OpenAI_methodology`
**Model**: `gpt-5-2025-08-07`
**Input PDF**: `/Users/houstongolden/Desktop/CODE_YOU/bigbounce/site/public/papers/paper2_fnl_forecast_v1.7.70.pdf` md5=99e6426c pages=29
**Input format**: NATIVE PDF (Files API + Responses) + reasoning_effort=high + pass-2 self-critique (5939 chars)
**Wall time**: 248.1s

---

Referee report for Physical Review D (methodology/statistics)

Manuscript: Testing the Matter Bounce with Primordial Non-Gaussianity: A SPHEREx Sensitivity Recast with a MegaMapper Outlook
Pages: 29

Overall scope of review
- Focus: methodology rigor — estimator definitions, derivation chains, internal arithmetic, error propagation, statistical validity, reproducibility.
- I audited all quoted scalars in the abstract and conclusions against the body and recomputed reported ratios/sigmas from supplied numbers.
- I inspected equations for dimensional consistency, figure/table captions for consistency, and references for traceability of quoted numbers.

High-level assessment
The paper presents a sensitivity recast of SPHEREx (and a qualitative MegaMapper outlook) for detecting a specific matter-bounce prediction fNL = −35/8. The author explicitly treats this as a recast (not a fresh end-to-end survey forecast), propagating a template-overlap factor r and a systems budget into previously published σ(fNL) results. Many caveats are written clearly, derivations are generally careful, and internal arithmetic largely checks out. However, there are several essential methodological clarifications and a few places where the text relies on heuristic choices without enough formalism to meet PRD’s standards for methodology/statistics. In addition, some reproducibility and provenance details are missing (DOI placeholder), and one cross-check (the injection–recovery test) is described in a way that is internally inconsistent about its noise weighting.

Below is a complete list of findings.

Findings

ESSENTIAL (must fix for PRD acceptance)

P2-E1 (Data & Code availability; pp. 24–25, “DATA AND CODE AVAILABILITY”)
- Problem: The repository DOI is a placeholder: “archived at Zenodo (DOI inserted at submission)”. There is no frozen, citable release with a version tag/commit hash. The paper’s conclusions (r values, Bayes-factor tables, null-space scans) rely on scripts named in the text.
- Required fix: Provide a minted, permanent DOI (e.g., Zenodo) that points to a frozen release (tagged commit) of the exact code and artifacts used to produce the results in the paper. List the repository URL, tag, and abbreviated commit hash in the paper. Verify that all named files (e.g., null space analysis.py; c9g bf table recompute.py; phase3 bispectrum shape overlap.json) exist in that release and reproduce the stated numbers.

P2-E2 (Injection–recovery test methodology; §II A/B (end), p. 5–6)
- Problem: The injection–recovery description is internally inconsistent about noise weighting and creates confusion about why rmeasured = 0.90 ± 0.01 exceeds the CMB-Fisher overlap r = 0.876:
  • The text states “adds isotropic Gaussian noise with the published SPHEREx photometric-z power spectra as the diagonal noise covariance” and then describes the setup as “effectively CMB-like weighting.”
  • A 2D, KSW-type, flat-sky estimator on tiled patches with SPHEREx photo-z “noise” is not CMB-like weighting and is not a 3D galaxy-bispectrum pipeline. It is unclear what multipole range, pixelization, binning, or sky tiling were used, and how 3D LSS statistics were collapsed to 2D.
- Required fix: Precisely specify the injection–recovery setup:
  • Geometry (patch size, number of patches, pixel resolution, multipole/k-range).
  • Noise model (what exactly is used from “SPHEREx photometric-z power spectra,” units, how it enters a 2D diagonal covariance; any beam/window).
  • Estimator details (filtering, separable templates, mask handling, normalization).
  • Explain why this setup yields rmeasured > rCMB and reconcile with the r weighting differences. If this is only a didactic Fisher-space test rather than a realistic LSS pipeline, either (i) move it to an appendix and label it as a consistency check with quantitative limitations, or (ii) replace it with a fully consistent 3D galaxy-bispectrum mock test (preferred).

P2-E3 (Template-overlap weighting definitions; §III B, pp. 8–9)
- Problem: The central template-overlap factor r = 0.84 ± 0.02 under “SPHEREx-like” and “LSS/SDB (1/k^2)” weighting drives the main detection-significance results but the precise weighting functions and domains are not fully specified in the paper. Phrases such as “SPHEREx-like weighting” and “five region-masked variants” are too vague for independent reproduction from the text alone.
- Required fix: Provide compact, explicit definitions in the paper (main text or an appendix) of every weighting used to compute r:
  • The exact functional forms of the Fisher weights (e.g., w(k1,k2,k3) ∝ Slocal^2 × [noise kernel], what noise kernel is used, the dependence on redshift bins if any).
  • The k-range, triangle-domain cuts, and the measure used (uniform/log-uniform), including x3,min, kmin/kmax, and the survey effective volume factors if used.
  • A table listing the numeric r for each weighting case (CMB-Fisher, 1/k^2, SPHEREx-like, uniform), so that readers do not have to infer from prose.

P2-E4 (Bayes factor: Gaussian bounce prior; §VI C, pp. 12–16; Tables II–III)
- Problem: You say the BF entries for Gaussian bounce prior are computed by “prior-convolved marginal” and by closed-form CDF integration, but you never write the actual formula. Without it, Table II’s Gaussian-prior numbers are not independently reproducible from the text.
- Required fix: Add the explicit analytic expression for the bounce-model marginal likelihood under a Gaussian prior on fNL. For a Gaussian prior N(μ0, σtheory^2) and Gaussian likelihood N(fobs; fNL, σ^2), show that the marginal is N(fobs; μ0, σ^2 + σtheory^2), then give the closed-form BF expression analogous to Eq. (9) with σeff → √(σ^2 + σtheory^2). Confirm in-text that the numerical values in Table II follow from this expression.

P2-E5 (Abstract-last drift and headline claims; Abstract pp. 1–2; §IV/VII pp. 10, 20)
- Problem: The abstract states the “bispectrum-only 5.2–5.5σ optimistic and 2.6–5σ realistic ranges as the headline forecast.” In the body, the 2.6–5σ band relies on an ad hoc additive-in-quadrature combination (bϕ prior widening + GR nuisance) explicitly labeled as a “transparent scoping choice” (not a joint Fisher). PRD requires that abstract claims reflect demonstrated (not prospective) methodology.
- Required fix: In the abstract and conclusions, explicitly label the 2.6–5σ “realistic” range as obtained from an additive-in-quadrature systematic budget, not from a full joint Fisher analysis, and note that correlations could move the result either way. Alternatively, provide a compact joint Fisher or profile-likelihood calculation for bϕ and GR nuisances consistent with the bispectrum observable to substantiate the headline.

MAJOR (significant revision)

P2-M1 (Heuristic covariance correction; §IV, Eq. (7), p. 10)
- Problem: The paper quotes a quantitative bound “δC/C ≲ 5 × 10−4” from a heuristic ζ-field scaling without plugging a survey volume or shell width. While you do call it “heuristic,” the quoted number appears precise.
- Required fix: Either (i) provide the actual numerical inputs (Vsurvey, δk, k) used to produce the bound and compute the value, or (ii) remove the numeric 5×10−4 and keep the qualitative statement that the correction is negligible for σ ≈ 0.7 given fNL ≈ −4.4.

P2-M2 (Length vs. contribution; overall)
- Problem: At 29 pages, the paper is long for a sensitivity recast whose core technical deliverables are: (i) a template-overlap quantification r, (ii) a systems budget applied to a published σ(fNL), and (iii) a closed-form Bayes-factor exercise.
- Required fix: Consider consolidating/relegating long narrative passages (e.g., repeated caveat language, extended background on QSFI/Higuchi bounds, and duplicate explanations of the factor-of-two issue) to appendices, keeping the core methodological content. A target length of ~18–20 pages would be appropriate without loss of substance.

P2-M3 (Injection–recovery sky fraction statement; §II A/B, p. 5–6)
- Problem: The text applies a 1/√fsky argument to a 2D flat-sky KSW-style test on tiled patches and then (correctly) notes it does not transfer to 3D galaxy bispectrum. As written, this paragraph risks confusing readers about whether any mask/noise inhomogeneity were actually modeled.
- Required fix: Tighten the language to avoid suggesting quantitative degradation for LSS. State clearly that no mask was applied, the test is 2D only, and remove the 1/√fsky estimate unless you show a direct calculation in the exact 2D setup used.

P2-M4 (Clarify weighting-scheme count; §III B, p. 8)
- Problem: The text switches between “10 weighting schemes,” “the three noise-weighted values,” and “five region-masked variants,” but only four actual numbers are subsequently used for r. This is confusing.
- Required fix: List all weighting schemes tried, which ones contribute to the quoted r range, and which are exploratory. Present a small table of schemes and the resulting r.

P2-M5 (Figure 4 and 5 axis units and quantitative setup; §VII A–B, pp. 16–17)
- Problem: The captions say “σ(fNL) vs. minimum accessible wavenumber” and show curves for SPHEREx SDB/MegaMapper SDB; however, the exact k-units, kmin values sampled, and assumed volumes/redshift distributions are not specified in text near the figure.
- Required fix: Add to the captions or main text: units (k in h Mpc−1), the kmin/kmax range tested, redshift binning, number density assumptions, and how the curves were computed (Fisher kernel and priors on bϕ). Ensure that the figure can be interpreted without guessing.

P2-M6 (Abstract model-comparison claim vs. curvaton prior; Abstract p. 1–2; §VI)
- Problem: The abstract headline BF ≈ 9–14 (noise-weighted booking) is fine for the broad [−15, +15] competitor; but, since the text argues that the curvaton-natural prior is [−5, +5], the abstract should also mention the corresponding lower BF ≈ 4–7 (as you do in the body).
- Required fix: Amend the abstract’s model-comparison sentence to include the curvaton-natural prior BF range, or explicitly say that the quoted 9–14 corresponds to the broad multifield prior and that curvaton-natural narrows it to ≈ 4–7.

MINOR (address, but not blocking)

P2-m1 (Eq. (2) notation; §II A, p. 3)
- Problem: “BNL = (10/3) P/AT i k^3_i …” has ambiguous typesetting for Σi k_i^3.
- Required fix: Replace “i k3_i” with an explicit Σi k_i^3 or ∑i k_i^3 to avoid ambiguity.

P2-m2 (Equation (9) readability; §VI C, p. 12–13)
- Problem: The CDF arguments are written as (fmax NL + 35/8)/σeff etc., which is correct for variable-of-integration fNL, but non-standard presentation can confuse readers.
- Required fix: Add a one-line derivation showing the change of variable y = (fNL − fobs)/σeff so that the +35/8 shift is transparent.

P2-m3 (SPHEREx timeline in abstract; p. 1)
- Problem: Statements like “launched March 2025, primary survey through ∼ 2027…” are programmatic and may become stale.
- Required fix: Move specific schedule details to a footnote or remove entirely, as they do not affect the methodology.

P2-m4 (Claims of “no prior quantification” of the overlap; §III B, p. 9)
- Problem: The sentence “literature search confirming no prior quantification of this overlap (2009–2024)” reads like a novelty claim without a citation survey.
- Required fix: Either remove the novelty phrasing or qualify it (“to our knowledge”) without implying a comprehensive survey.

P2-m5 (Typo/formatting)
- Problem: Occasional heavy internal-bookkeeping phrasing appears in the body (“headline,” “bookkeeping endpoint,” “rebooking”). This is stylistically odd for PRD.
- Required fix: Consider streamlining to more standard phrasing where feasible.

NIT (cosmetic)

P2-n1 (Duplicate explanatory phrases)
- Problem: The “single time-ordering intermediate; not a physical bispectrum” disclaimer recurs verbatim in several places.
- Fix: Retain once in Appendix A and once in the main text; trim elsewhere.

P2-n2 (Hyphenation and symbols)
- Problem: Inconsistent hyphenation for “post-systematic-budget,” “scale-dependent bias,” etc.
- Fix: Normalize hyphenation.

Arithmetic and consistency spot-checks

- r range and significance: Using σ(fNL) = 0.7 and fNL = 4.375, the significance |f| r / σ gives:
  • r = 0.829 → 5.18σ; r = 0.876 → 5.48σ. Your “5.2–5.5σ” range matches.
- GR quadrature cases (Table IV): σeff = √(0.7^2 + 1.0^2) = 1.22; significance 3.675/1.22 ≈ 3.01σ; tabulated as ~3.0σ — consistent.
- “All combined” bϕ 30% + GR 1.0: σeff = √(0.9^2 + 1.0^2) = 1.345; significance 3.675/1.345 ≈ 2.73σ; tabulated as ~2.7σ — consistent.
- Null-space 16th percentile r = 0.75: 4.375 × 0.75/0.7 = 4.69σ; quoted ≈ 4.7σ — consistent.
- PR4/NPIPE recast: σrecast = 5.0/0.876 ≈ 5.71; distance from −4.375 is 4.275/5.71 = 0.75σ — consistent.
- Bayes factor delta prior, W = 30, σeff = 0.7: 30/(√(2π)×0.7) ≈ 17.10; quoted 17.10 — consistent.
- Bayes factor delta prior, σeff = 0.833: 14.37; quoted 14.36 — consistent.

Dimensional checks

- Eq. (3)–(4): Δb ∝ fNL/M(k,z) with M(k,z) = 2k^2 T(k)D(z)/(3ΩmH0^2). This matches the standard normalization (dimensionless M; Δb dimensionless) and is dimensionally consistent.

Figures and tables

- Figure 2 caption clearly labels the naive 6.25σ bar as “shown only for reference, not used in any headline,” satisfying the “not directly comparable” requirement when naive and template-corrected sigmas appear side-by-side.
- Table I values (−35/8, −255/64, −9/4) are numerically consistent with the listed decimals.
- Table IV (systematic budget) arithmetic checks out as per recomputations above.

Bibliography spot-checks

- Heinrich et al. (2024) PRD 109, 123511: σ(fNL) ≈ 0.7 for SPHEREx bispectrum — matches the citation claims.
- Planck PR4/NPIPE (2025) A&A 702 A204: fNL central value and σ consistent with the quoted number.
- Dalal et al. (2008), Seljak (2009), McDonald & Seljak (2009) correctly cited for SDB/multi-tracer context.

Standalone-reader test

- Most symbols are defined on first appearance; however, the Bayes factor with Gaussian bounce prior needs an explicit formula (see P2-E4). The injection–recovery test needs a self-contained description (see P2-E2). The definition of all overlap weights (see P2-E3) is needed for reproducibility without relying on the repository.

Effect sizes and practical significance

- The paper consistently translates forecast σ into detection significance for |fNL| = 4.375 (stated amplitude); the effect size (overall fractional amplitude change via r) is given. No additional effect-size metrics are necessary here.

## Summary recommendation
MAJOR REVISIONS

The paper is careful and internally consistent on most arithmetic and caveats, and the central recast logic is sound. However, PRD-level methodological rigor requires (i) a frozen DOI with exact code and artifacts, (ii) a clarified and internally consistent injection–recovery methodology, (iii) explicit definitions for the weighting schemes that determine r, and (iv) an explicit analytic expression for the Gaussian-bounce-prior Bayes factor. In addition, the abstract should explicitly qualify that the 2.6–5σ “realistic” band comes from an additive-in-quadrature systematic budget (unless a joint Fisher is provided). Addressing these items, and tightening length by moving some extended background and duplicate caveats to appendices, would bring the manuscript up to PRD standards.

---

## PASS 2 — self-critique findings (what initial review missed)

NEW FINDINGS (second-pass audit)

P2-E6 (Equation (2) dimensional inconsistency; §II A, p. 3)
- Problem: Eq. (2) defines BNL ∝ P/AT × 1/Σi k_i^3, and then immediately argues “P has degree 9, the prefactor of Eq. (1) removes degree 6, and the Σk^3 denominator removes the remaining degree 3,” implying BNL is dimensionless. That degree counting is only correct if AT is in the numerator, not the denominator. With the printed P/AT, one gets BNL ∝ (k1 k2 k3)^2/(Σ k^3), i.e., degree 3 (not dimensionless) after cancellation of P — contradicting both the narrative and the intent that BNL depend on P via AT. This looks like an inversion typo (AT/P was intended). 
- Required fix: Correct Eq. (2) so that BNL ∝ AT/(Σi k_i^3) (with the 10/3 factor as stated). Ensure the surrounding paragraph’s degree-count argument matches the printed formula, and verify all downstream numbers/plots used this corrected form.

P2-M7 (Shot-noise degradation contradiction; §IV, “Shot-noise caveat,” p. 10–11)
- Problem: The paragraph begins “a simple Poisson estimate gives a ∼ 15–30% degradation,” then immediately computes σshot/σCV ≈ √(1+1/(nP0)) with nP0 ≈ 0.1, yielding √11 ≈ 3.3× — a 230% inflation, not 15–30%. The text later attributes the 15–30% to “effective degradation at the squeezed-limit modes” but the opening sentence conflates the two and is numerically contradictory.
- Required fix: Separate clearly: (i) the formal Poisson-limited scaling (3.3× in the stated example), and (ii) any empirically measured “effective” degradation from a bispectrum estimator that downweights high-k modes. Provide a quantitative mock or citation to justify the 15–30% figure, or remove it.

P2-M8 (ℓ-space Fisher “validation” is not commensurate with LSS bispectrum; §III B, pp. 8–9)
- Problem: The ℓ-space Fisher overlap uses CAMB Cℓ with a Planck noise model to validate a 3D galaxy-bispectrum template overlap r. This CMB-based test is not commensurate with the SPHEREx 3D LSS bispectrum weighting and selection. While you call it a “validation,” the comparability is weak and risks over-claiming.
- Required fix: Reframe this as a cross-check only, move details to an appendix, and explicitly state its limited interpretability for the 3D LSS bispectrum. Alternatively, replace with a 3D Fisher overlap using the SPHEREx bispectrum covariance.

P2-M9 (Figure 5 vs body inconsistency on bϕ sensitivity; §VII B, p. 17)
- Problem: Figure 5 (left) shows a flat red dashed line at σ(fNL)=0.7 for the SPHEREx bispectrum across bϕ prior widths, suggesting no dependence. The body text says the bispectrum is “less sensitive to bϕ than SDB, but not independent,” and quotes 20–50% degradations when bϕ is relaxed. The figure and text conflict.
- Required fix: Either (i) plot the bispectrum σ(fNL) curve vs. bϕ-prior width (20–50% widening) to match the prose, or (ii) annotate the dashed line as the “UMF-fixed baseline (no bϕ marginalization)” and add a second curve showing the degraded σ(fNL) when bϕ is free.

P2-M10 (Undefined bars in Fig. 2; §V, p. 11)
- Problem: Figure 2 includes MegaMapper bars labeled “conservative” and “single-tracer,” but the text never defines the exact assumptions (areas, number densities, priors, or σ(fNL)) behind these two bars.
- Required fix: Add a concise definition in the caption or main text for these two bars (assumed σ(fNL), priors, redshift ranges, and whether bϕ/GR degradations are included).

P2-m6 (“Four-corner” Bayes-factor grid wording vs. Table II content; §VI C, pp. 12–16)
- Problem: The prose repeatedly refers to a “four-corner” grid (delta vs. Gaussian bounce prior × narrow vs. broad competitor priors), but Table II and text also discuss Gaussian σtheory = 0.5 and 2.0, i.e., more than four entries. This is mildly confusing.
- Required fix: Clarify in one sentence that the “four-corner” grid is the baseline, and additional σtheory rows (0.5, 2.0) extend the grid for sensitivity testing.

P2-m7 (Units/conventions for Eq. (4); §III A, p. 7)
- Problem: With k quoted in h Mpc−1 and H0 in s−1 (or km s−1 Mpc−1), M(k,z) can be confusing without a unit convention. The text assumes c = 1 implicitly.
- Required fix: State the unit convention explicitly (e.g., c = 1; H0 expressed in h Mpc−1 units consistent with k), or cite a reference that uses the identical normalization.

P2-m8 (Appendix A.2 table label vs. content; p. 28)
- Problem: The header “A.2 Time-ordering sensitivity Fisher table” calls Table V a “Fisher table,” but the table reports detection significances (not a Fisher matrix).
- Required fix: Rename to “Time-ordering sensitivity of the SPHEREx significance” (drop “Fisher”).

P2-m9 (Triangle index ordering consistency; §II A, Table I vs. grid definition)
- Problem: The triangle grid is defined with k1 ≤ k2 ≤ k3, but the folded benchmark in Table I and parts of the text sometimes take k1 as the largest side (k1 = 2k, k2 = k3 = k). This can confuse readers about which index labels the “squeezed” or “hard” modes.
- Required fix: Add a sentence that benchmark listings may not adopt the k1 ≤ k2 ≤ k3 ordering, and define explicitly which side is “long/short” when quoting limits.

P2-m10 (Justify “CMB-Fisher weighting ∝ k^2”; §III B, p. 8)
- Problem: The statement that “CMB Fisher weighting” corresponds to w ∝ k^2 is non-standard and unexplained.
- Required fix: Provide a brief derivation or citation that motivates this k-space surrogate for ℓ-space CMB Fisher weighting, or relabel it as an ad hoc sensitivity check rather than “CMB Fisher.”

Explanation
This second-pass audit focused on items routinely missed on first review: a key dimensional inconsistency in Eq. (2); a contradictory shot-noise paragraph; a CMB-based “validation” that is not actually commensurate with the 3D LSS bispectrum; and a figure/text mismatch on bϕ sensitivity. Additional minor clarifications on units, labels, and wording will further improve methodological clarity and reproducibility.