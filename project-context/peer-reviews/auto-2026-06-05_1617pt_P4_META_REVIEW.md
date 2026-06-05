# P4 auto-2026-06-05_1617pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 325.7s

---

Meta-review: new issues none of the five referees caught

P4-META-E1
Severity: ESSENTIAL
Section + page: IV.D (Monopole+Mask Leakage Generative Null), page 4–5; Table IV, page 5
Why others missed it: Prior reviewers noticed field/denominator ambiguity but did not trace it into the Monte Carlo generative step.
Specific problem: The generative null is described as “N = 500 realizations in which the per-pixel CW count is drawn from Binomial(ntotal, pglobalCW) on the exact canonical mask.” In this paper the asymmetry field A_p is defined on spirals only (NCW+NCCW in Eq. 3), but here ntotal is not defined and, in context with Appendix A where Nall denotes CW+CCW+NS, it reads as total classified sources, not spirals. If ntotal=Nall was used, the null draws CW counts against a denominator that includes non-spirals, which is inconsistent with the field being analyzed and can artificially boost the apparent success of the leakage reproduction (the quoted 99.3%).
Required fix: Explicitly define ntotal and re-run the generative null with ntotal=Nspiral(p). Report side-by-side results for ntotal=Nspiral vs ntotal=Nall and quantify the impact on the “99.3% reproduction” and all Table IV statistics. If ntotal was in fact Nspiral, state it unambiguously and correct the text.

P4-META-E2
Severity: ESSENTIAL
Section + page: III.A (Declared Analysis Hierarchy), IV.C–D (Dipole analysis and nulls), pages 3–5
Why others missed it: They flagged “null not specified” but not the deeper conditioning problem.
Specific problem: The per-pixel random-label permutation null and the hemisphere LEE tests condition on the realized, classifier-derived spiral counts per pixel and on the post-classification pixel selection (pixels with ≥10 spirals). This “null” therefore bakes in sky-dependent classification systematics (depth, seeing, NS-vs-spiral assignment) and the MNAR pixel-selection boundary, implicitly lowering the variance relative to an isotropic-sky null. Several conclusions (e.g., pMC=0.030 for the canonical residual) are drawn under this conditioned null while being framed as “isotropic.”
Required fix: Add an unconditioned isotropic-sky null: simulate sky-positions uniformly over the footprint (or rotate the map over the sphere), draw spiral counts from a homogeneous process matched to the global selection function, then assign CW/CCW by the specified p. Compare significances under the conditioned (per-pixel shuffle) and unconditioned nulls for all headline estimators. State clearly which null underlies each σ and why it is appropriate.

P4-META-M1
Severity: MAJOR
Section + page: Abstract and VI.B (Relation to Parity-Violating Sectors), pages 1 and 6
Why others missed it: Most reviewers accepted the parity framing at face value.
Specific problem: The manuscript asserts “the ℓ=1 observable is parity-EVEN … the parity-odd analog requires 3D spin-vector or polarization-rotation cross-correlation observables.” For a pseudoscalar 2D field A(n) (handedness), parity acts as A(n)→−A(−n), yielding aℓm→−(−1)ℓ aℓm; thus ℓ=1 is indeed parity-even, but parity-odd content lives in the even-ℓ multipoles of the same 2D map. No 3D spins or polarization are required to test for parity-odd structure in A(n). The paper actually measures ℓ=2 bandpower excess but never frames it as a parity-odd test.
Required fix: Correct the parity discussion: state that even-ℓ multipoles of the 2D pseudoscalar map are parity-odd and could constitute a direct parity test. Either (a) present a simple even-vs-odd ℓ decomposition of the MASTER spectrum (with appropriate nulls) and report bounds on the parity-odd sector, or (b) explicitly defer this analysis and remove the claim that such tests require 3D observables.

P4-META-M2
Severity: MAJOR
Section + page: Appendix C (Hemisphere asymmetry) and IV.E (Signal-hunt diagnostics), pages 8 and 5
Why others missed it: They noted lack of Gross–Vitells citation and pLEE quantization, but not the misuse of FDR.
Specific problem: The look-elsewhere correction is described as “Bonferroni/BH across ∼650 directions,” but Benjamini–Hochberg controls FDR for families of tests; it is not appropriate for calibrating the distribution of a global maximum statistic. Using BH here is methodologically incorrect and can under-correct the LEE.
Required fix: Drop BH for the maximum-over-directions statistic. Calibrate the max statistic exclusively by direct MC under a well-defined null (and grid resolution), or use the Gross–Vitells formalism for random fields. Report the dependence on the direction-grid resolution and show that conclusions are stable.

P4-META-M3
Severity: MAJOR
Section + page: II.A–III.D (Data and pixelization), IV.C (Dipole analysis), Appendix E.d, pages 2–4, 9
Why others missed it: Threshold robustness was mentioned only for one estimator; the selection-bias mechanism itself was not discussed.
Specific problem: The analysis includes only HEALPix pixels with ≥10 spirals, a selection applied after the classifier assigns spiral vs not-spiral. Because the classifier’s spiral/NS decision is depth- and PSF-dependent (and potentially orientation-dependent), this threshold induces a “missing-not-at-random” mask correlated with the observable. Appendix E.d reports robustness of the MASTER ℓ=1 result to threshold changes, but not for other estimators (real-space dipole, canonical residual, hemisphere max), nor is an injection showing invariance of selection to an injected dipole provided.
Required fix: Demonstrate that post-classification pixel selection does not bias any of the estimators: (i) repeat real-space dipole, canonical ℓ=1, and hemisphere-max under several thresholds (e.g., 5/10/20/50), (ii) run a dipole-injection test and show that selection retains linearity in amplitude, and (iii) evaluate an analysis without any pixel-count cut using inverse-variance weights.

P4-META-M4
Severity: MAJOR
Section + page: III.C (Test-Time Equivariant Averaging), Appendix B (flip consistency), pages 3 and 7–8
Why others missed it: They focused on tautology of the flip test, not on axis anisotropy.
Specific problem: Only horizontal reflection is used in production TTA, yet vertical reflection also flips chirality and would diagnose row/column or readout-axis systematics (e.g., PSF anisotropy, CTI) that are not averaged out by horizontal flips alone. No horizontal-vs-vertical flip ablation is shown.
Required fix: Add a horizontal-only vs vertical-only flip ablation: compare mean A_p, C1, and the canonical ℓ=2–4 bandpowers under H-only, V-only, H+V, and full D4. Demonstrate that the choice does not materially impact the cosmological estimators or the canonical residuals.

P4-META-M5
Severity: MAJOR
Section + page: III.D (Catalog tiers), IV.B (Global CW fraction), pages 3–4
Why others missed it: Calibration was noted only tangentially.
Specific problem: Platt calibration (Catalog B) measurably shifts the global CW fraction (to 0.504) relative to the raw classifier (0.5079) and the equivariant protocol (0.4974). A calibration trained on mixed/derived labels (67.6% CE-ResNet) can imprint prior class ratios into probabilities, affecting any analysis that thresholds or weights by peq. There is no demonstration that calibration preserves spatial neutrality or does not inject additional monopole.
Required fix: Either (a) remove calibrated probabilities from any part of the cosmological analysis (use only Catalog C), or (b) validate the calibration: show reliability diagrams on an independent hand-labelled set, demonstrate that calibration does not change A_p spatially (maps before/after), and quantify its effect on all estimators.

P4-META-M6
Severity: MAJOR
Section + page: I (Abstract claims), III.A (Declared hierarchy), IV.C–D (Mask choices), pages 1, 3–5
Why others missed it: They flagged mask nomenclature but not potential post-hoc selection.
Specific problem: The “strict-superset subsample mask” (fsky=0.659) is used for the headline MASTER −0.122σ, whereas the canonical mask (fsky≈0.49) shows a residual. No a priori rationale is given for promoting the subsample mask to “primary” beyond yielding a null, and the selection appears post hoc (“subsample” yet a strict superset). This is a classic garden-of-forking-paths risk.
Required fix: Pre-register or justify the mask choice: specify in Methods the pre-analysis criteria that define the subsample mask (e.g., apodization, minimum depth, allowed legs), report results on both masks in the main text, and include a sensitivity analysis showing that the headline conclusion does not depend on this particular mask choice.

P4-META-M7
Severity: MAJOR
Section + page: II.B (Training Labels) and cross-match, page 2–3
Why others missed it: They questioned the attribution/size, not the independence guarantee.
Specific problem: The paper asserts “234,282 disjoint matches” for the GZ1 cross-match used to set the 69.91% accuracy floor, while also using 6,637 GZ1 galaxies for training. No procedure is given to prove disjointness (e.g., ID lists, matching radii, or de-duplication rules), so leakage from training into the “independent” accuracy estimate cannot be excluded.
Required fix: Document the matching radius, the unique ID scheme, and provide an overlap count between the 6,637 GZ1 training objects and the 234,282 cross-match used for validation. If any overlap exists, recompute the accuracy floor on a strictly disjoint set and propagate its uncertainty to the sensitivity claims.

P4-META-M8
Severity: MAJOR
Section + page: VI.A (Sensitivity floor), Appendix A (MASTER), pages 6–7
Why others missed it: They flagged the missing “1.7%” derivation; the analytic C1–A mapping itself is absent.
Specific problem: There is no explicit analytic mapping between a real-space dipole amplitude A of the A_p field and the corresponding C1 expected under full/partial sky (e.g., C1=4πA^2/9 for a unit-normalized dipole, modified by mask coupling). Without this, the paper cannot convert injection amplitudes into expected C1 or vice versa, which also prevents a principled comparison to literature amplitudes.
Required fix: Provide the analytic A→C1 mapping for the specific field definition used (spirals-only denominator), validate it with injections, and use it consistently to (i) state the implied A for the canonical-mask residual and (ii) justify the quoted amplitude thresholds.

P4-META-N1
Severity: MINOR
Section + page: IV.C (Pixelization) and all estimator descriptions, pages 4–5
Why others missed it: They focused on other robustness sweeps.
Specific problem: No NSIDE stability test is shown. With NSIDE=64 and a ≥10-spiral cut, both A_p variance and mask geometry change with resolution. Several of the reported σ values could be sensitive to NSIDE.
Required fix: Add an NSIDE sweep (e.g., 32/64/128) for the headline estimators and the canonical ℓ=1–4 bandpowers, holding the physical per-pixel count threshold fixed (e.g., by rebinning), and report the stability.

P4-META-N2
Severity: MINOR
Section + page: Appendix A.a (MASTER setup), page 7
Why others missed it: The subtlety hides in implementation details.
Specific problem: “The MASTER mode-coupling matrix does NOT include ℓ=0 on either the input or output side.” Excluding ℓ=0 from the coupling matrix while also subtracting a weighted monopole is unusual; if the subtraction is imperfect under the chosen weights/mask, residual ℓ=0→ℓ=1 leakage cannot be modeled by the coupling matrix.
Required fix: Include ℓ=0 in the input side of the coupling matrix (even if you do not report C0), or demonstrate with simulations that the weighted monopole subtraction removes ℓ=0 leakage to numerical precision for both masks.

P4-META-N3
Severity: MINOR
Section + page: Data Availability, page 9
Why others missed it: They checked URL existence in principle, not licensing.
Specific problem: The parent sample is “Smith42/galaxies” (DESI Legacy cutouts) redistributed on HuggingFace. DESI Legacy imaging has specific redistribution terms; the manuscript does not state that these cutouts are redistributed in compliance with those licenses.
Required fix: Add a brief licensing statement confirming that all redistributed image cutouts comply with DESI Legacy/NOIRLab licensing (or remove redistributed imagery and instead distribute only derived catalogs with pointers to official cutout services).

Meta-review recommendation
MAJOR REVISIONS

Considering all six reviews, I count at least 10 blockers (your two ESSENTIAL items above, plus multiple ESSENTIAL/MAJOR items already raised: table arithmetic and null-definition inconsistencies; mask/moment-ratio σ misuse; injection-recovery limited to HC only; ambiguous field/weight definitions; orphan references; and abstract overclaims). My confidence that the paper would survive external, non-bigbounce peer review after addressing these is moderate: the core scientific result (a null dipole) is plausible and likely to hold, but the methodological presentation needs substantial tightening, corrected nulls, and clearer, reproducible mappings between amplitude and power.