# P4 R24conf — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 697.2s

---

META-REVIEW (focus: blind spots none of the 5 referees caught)

P4-META-E1
- Severity: ESSENTIAL
- Location: Table III caption (p. 9) and surrounding text in Sec. IV.C–D
- Why missed: Prior reviews focused on cross-null comparability and 3.64σ vs 7.93σ, not on the shot-noise normalization itself.
- Problem: The manuscript states “the analytic binomial shot-noise floor for this field is Nℓ=1 ≈ 2.0×10−6, consistent with the null means above.” But Table III shows two different ℓ=1 null means that bracket this value widely: apodized/weighted case ⟨C1⟩ ≈ 1.93×10−6 (consistent) vs canonical/unapodized ⟨C1⟩ ≈ 0.57×10−6 (inconsistent by a factor ≈3.4). The text does not specify which field/mask/weight the 2.0×10−6 “analytic floor” refers to, and it is not “consistent with the null means above” in the canonical case.
- Required fix: State explicitly that the analytic floor is computed for a particular field/weight (e.g., Ap with Wp=Nall on the apodized footprint) and provide the corresponding expression. Either (i) give separate analytic expectations for each field/mask/weight combination used (apodized Wp=Nall and canonical binary), or (ii) remove the single-number “floor” and present only the empirically estimated null means with uncertainties, clearly tied to each configuration.

P4-META-E2
- Severity: ESSENTIAL
- Location: Appendix A.b (p. 13) and Sec. IV.C.b (p. 7)
- Why missed: Reviewers questioned cross-estimator consistency but not the numerical stability of the ℓ=1 deconvolution itself.
- Problem: The paper performs MASTER deconvolution at ℓ=1 with a C2 apodized, weighted, patchy footprint. At ℓ=1 the mode-coupling matrix is notoriously ill-conditioned on patchy masks, and NaMaster documentation cautions stability at the lowest multipoles. The paper quotes large significances at ℓ=1 but provides no condition-number, eigenmode, or stability diagnostic for the ℓ=1 row, nor any regularization/sanity check (e.g., jackknife masks) that the decoupling is numerically stable and not dominated by near-singular coupling.
- Required fix: Report the conditioning of the ℓ=1 block of the coupling matrix (e.g., smallest singular value, condition number), show that the deconvolved C1 is stable under modest apodization-length changes and/or sub-footprint jackknifing, and add a brief note/citation demonstrating unbiasedness under the stated weighting. If instability is found, relegate ℓ=1 deconvolution to Supplemental diagnostics and avoid quoting it as a quantitative “σ” without stability certification.

P4-META-M1
- Severity: MAJOR
- Location: Appendix C (p. 15) and Table I caption (p. 4)
- Why missed: Others noted “double correction” but not the statistical validity of the second correction itself.
- Problem: The hemisphere look-elsewhere analysis uses (i) a max-statistic Monte Carlo null over 648 directions (which already accounts for the directional trials) and then applies (ii) a Benjamini–Hochberg (BH) or Bonferroni pass over the same 648 directions. BH/FDR assumptions (independence or positive dependence) do not hold for this highly correlated directional grid; applying BH post hoc after a max-stat null is statistically ill-posed and yields an uninterpretable “extra penalty.”
- Required fix: Use one principled family-wise framework only. Keep the direct-MC max-statistic null (already correct for directional LEE) and drop the subsequent BH/Bonferroni across dependent directions. If you wish to show both, clearly state BH is invalid in this dependent setting and provide it only as an upper-bound heuristic in Supplemental Material.

P4-META-M2
- Severity: MAJOR
- Location: Sec. VI.A (p. 11) and Appendix B.e (p. 15)
- Why missed: Prior reviews accepted the g = 2a − 1 mapping in passing, without checking its applicability conditions.
- Problem: The conversion from observed to “true” underlying amplitude A_true via A_obs = g·A_true with g = 2a − 1 assumes symmetric misclassification strictly between CW and CCW (no triage to “not spiral”) and equal error rates for both classes. The paper does not validate these conditions on the independent GZ1 cross‑match (where three-class confusion is substantial). Using g = 2a − 1 without verifying symmetric CW↔CCW errors (and without quantifying the effect of “not spiral” leakage) can bias the inferred A_true threshold (quoted ~1.88%).
- Required fix: On the disjoint GZ1 cross‑match, report the 2×2 CW/CCW confusion restricted to cases you classify as spiral, quantify asymmetry in false rates, and show how triage to “not spiral” alters the amplitude transfer. If symmetry is violated, replace g with the appropriate 2×2 confusion-matrix scaling, propagate uncertainties, and update the A_true mapping (or drop it and keep only observed-space A50/A95).

P4-META-M3
- Severity: MAJOR
- Location: Sec. IV.B (p. 5)
- Why missed: Reviewers focused on the presence/absence of a dipole, not on conditioning introduced by the slab partition.
- Problem: The “spatially uniform across 7 equatorial coordinate slabs” test uses equal-spiral-count slabs. Because “spiral” membership itself depends on classifier confidence and sky depth, this partition conditions on the variable of interest and can mask depth/morphology-induced gradients. An equal-area slab test (or area-uniform HEALPix super-pixels) would be a more neutral uniformity check.
- Required fix: Repeat the slab uniformity analysis with fixed-area slabs (or fixed NSIDE super-pixels), independent of local spiral yield, report per-slab fCW with binomial errors, and compare with the equal-count result. If differences emerge, discuss their interpretation and any bias they imply for the “uniformity” conclusion.

P4-META-M4
- Severity: MAJOR
- Location: Sec. II.B (p. 2), Appendix B (pp. 14–15), Sec. IV.D (pp. 8–10)
- Why missed: Others noted training details and CE‑ResNet dependence, but not the circularity this creates for label‑shuffle diagnostics.
- Problem: Two-thirds of the training labels are CE‑ResNet pseudo‑labels drawn from the same parent survey domain as the evaluation set. If CE‑ResNet carries large‑scale survey systematics, the ViT will inherit them. The primary diagnostic nulls (per‑galaxy label‑shuffle, per‑pixel permutation) randomize the model’s own outputs; they do not test independence from CE‑ResNet‑imprinted survey gradients. This weakens the claim that label‑shuffle nulls independently vet survey‑systematics leakage.
- Required fix: Provide one of the following: (i) a control model trained only on GZ1 labels (no CE‑ResNet pseudo‑labels) and re‑run the key diagnostics to show the same conclusions, or (ii) cross‑check that the large‑scale modes of CE‑ResNet predictions are uncorrelated (post‑mask) with your Ap field, or (iii) explicitly state this limitation and refrain from using shuffle‑based diagnostics as evidence of full systematics independence.

P4-META-m1
- Severity: MINOR
- Location: Appendix B.d (p. 14)
- Why missed: Reviewers accepted the “metadata leakage” phrasing without probing its sufficiency.
- Problem: Test T5 uses simple correlations r(pCW, RA) and r(pCW, Dec) < 0.10 as a leakage guard. RA/Dec are coordinate-dependent and, on a patchy mask, small marginal correlations can coexist with strong leakage along rotated axes or low-ℓ spherical harmonics. This test is too weak to rule out directional metadata leakage.
- Required fix: Replace T5 with a spherical-harmonic regression of pCW on Yℓm up to low ℓ (e.g., ℓ ≤ 3), or use a rotation-invariant test (e.g., max over random great-circle projections), and report the largest coefficient and its null distribution.

P4-META-m2
- Severity: MINOR
- Location: Appendix A.c and Table VI (p. 13)
- Why missed: Prior reviews noted fsky labeling but not the normalization domain ambiguity.
- Problem: The definition of feff_sky uses means over all Npix (including zeros outside the mask), whereas many analyses report mask-restricted feff_sky. The manuscript mentions both and lists mask-restricted “factors,” but Table VI aggregates a mixture without a clear rule, risking misuse when comparing rows.
- Required fix: Standardize: report geometric fsky (binary) and, in a separate column, feff_sky computed over the masked pixels only (explicitly defined). Note in captions which one is used where (e.g., MASTER uses the exact coupling matrix; feff_sky is descriptive only).

P4-META-m3
- Severity: MINOR
- Location: Sec. IV.C.a (p. 6)
- Why missed: Others focused on weighting and null choices, not uncertainty on direction.
- Problem: The real‑space dipole fit quotes an amplitude and significance but no uncertainty on the dipole direction (l, b). Even under a null, reporting the typical directional uncertainty (from the null distribution) is standard to show the dipole axis is unconstrained.
- Required fix: Add the 68% or 95% containment for the recovered axis under the null (e.g., from permutations), or simply state that the direction is unconstrained at the quoted significance and provide a typical angular spread.

P4-META-m4
- Severity: MINOR
- Location: Sec. IV.C.a (p. 6) “monopole cannot bias the uniform-weight real-space dipole estimator”
- Why missed: Prior reviews accepted the constant‑monopole generative test at face value.
- Problem: The statement is correct for an additive constant monopole, but the paper’s own systematics discussion emphasizes multiplicative depth/morphology coupling. A uniform-weight fit can be biased by pixel‑dependent multiplicative effects even after fitting a constant m. The generative test with a constant binomial p does not probe this.
- Required fix: Add a calibrated stress test: inject a pure monopole modulated by a realistic depth proxy (e.g., pCW = p0·[1+ε·(Nall/⟨Nall⟩−1)]) with ε spanning observed levels, and show the real-space dipole fit remains unbiased within uncertainties; otherwise qualify the claim to “constant monopoles only.”

P4-META-n1
- Severity: NIT
- Location: Sec. III.C (p. 4–5) and Fig. 2 caption
- Why missed: One reviewer caught D4 vs Z2 usage inconsistency; none noted the narrower point below.
- Problem: The text asserts “flip-swap correlation = 1.000 by construction.” That is true only for the combined equivariant outputs (original+flip) treated as a single prediction; phrasing can be misread as a measured property of the network’s raw pre-TTA outputs.
- Required fix: Rephrase to “the combined equivariant protocol yields identical outputs for an image and its mirror after swapping CW/CCW (a code-path check), so the flip‑swap correlation of the equivariant outputs is 1.000 by construction; this is not a property of the raw network.”


Meta-review recommendation
MAJOR REVISIONS

Union-of-reviews assessment
- Blockers: Counting the union of all six reviews, there are multiple ESSENTIAL/Major items: harmonizing/clarifying ℓ=1 estimators and nulls; adding a formal 95% upper limit; clarifying injection protocols and axis priors; removing internal “artifact” prose; resolving canonical 3.64σ vs 7.93σ numerics; fsky labeling; training/validation clarity; plus the new shot-noise inconsistency and ℓ=1 stability checks. I estimate ≥10 substantive fixes across methodology presentation and diagnostics.
- Confidence of survival under external peer review: Moderate to high once these are addressed. The core real‑space null result appears robust; most issues are presentation/diagnostic rigor, estimator bookkeeping, and a few missing stress tests. With a harmonized, self-contained revision and the added stability/shot-noise clarifications, the paper should withstand external (non-lab) refereeing.