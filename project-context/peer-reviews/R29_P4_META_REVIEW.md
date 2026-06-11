# P4 R29 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 340.8s

---

META-REVIEW — PRD submission “Survey-Scale Galaxy Chirality with Equivariant TTA …” (v1.0.172)

Scope
I read the rendered PDF (22 pp) and all five prior referee reports. Below I list issues that none of the five reviewers raised. Each item includes an ID, severity, location, why it was missed, the concrete problem, and the required fix.

New findings (not raised by the 5 prior reviews)

P4-META-E1 — Possible train/validation leakage implied by augmentation arithmetic
- Severity: ESSENTIAL
- Section/page: II.B Training Labels (pp. 2–3) and Appendix B.a Training (p. 16)
- Why others missed it: Reviewers focused on statistical estimators and provenance; none audited the raw train/val arithmetic against the stated augmentation protocol.
- Problem (quote + analysis):
  - “The combined training set contains 6,637 + 17,153 + 2,000 = 25,790 source images; after flip augmentation of the training split the combined pool is 26,616 images (80/20 split: ntrain = 21,293, nval = 5,323; augmented duplicates contribute to the 826-image difference between the source manifest and the training pool).”
  - In Appendix B.a you also state “flip augmentation and the equivariance loss act on training batches only.” If augmentation is applied only after the 80/20 split (to the training split), the total pool size should not increase before the split, and the validation size should remain the 20% of 25,790 (≈5,158), not 5,323. The reported 80/20 split percentages (21,293/26,616 and 5,323/26,616) imply the 26,616 “pool” (including 826 augmented duplicates) was formed before the split, contradicting “training-only” augmentation and creating a potential leakage path (flipped twins of validation images landing in training).
- Required fix:
  - Clarify the exact order-of-operations for splitting and augmentation, and adjust the counts to match that protocol. If augmentation was performed before splitting, state this explicitly and demonstrate that no augmented twin of any validation image appears in the training set (e.g., by reporting an image-ID overlap check). If augmentation was performed after splitting (as Appendix B.a claims), correct the pool-size arithmetic and the reported train/val counts.

P4-META-M2 — Global CW-fraction “−9.5σ” uses a naive binomial variance that ignores spatial clustering/correlation
- Severity: MAJOR
- Section/page: IV.A–B (pp. 5–6), Table II
- Why others missed it: The paper dismisses the monopole as a classifier artifact, making the formal σ easy to overlook; however, the same monopole underpins the leakage argument.
- Problem:
  - The deviation fCW = 0.497353 ± 0.000279 is benchmarked with σ = √(f(1−f)/Nspiral), presuming independent Bernoulli trials. With strong galaxy clustering and correlated classifier outputs within bricks and seeing patches, the binomial underestimates the true variance. The “−9.5σ” overstates significance and is then used to motivate the monopole–mask leakage channel.
- Required fix:
  - Re-estimate the uncertainty on the global fCW using a spatial jackknife or block-bootstrap (e.g., HEALPix NSIDE=8 or brick-based blocks) and report the adjusted “Dev.(σ)”. The leakage generative null can still use the measured global rate as a point estimate, but the paper should not rely on a binomial σ for any significance characterization of the global monopole.

P4-META-M3 — Pixel-permutation “isotropic-bootstrap” null is not isotropic and does not preserve per-pixel noise geometry
- Severity: MAJOR
- Section/page: IV.C.a “Simple dipole” (p. 7)
- Why others missed it: Most reviewers accepted the label-shuffle cross-check as sufficient and did not interrogate the semantics of the primary (“isotropic-bootstrap”) null.
- Problem (quote):
  - “The null distribution is built from NMC = 10,000 isotropic realizations in which the per-pixel asymmetry values Ap are randomly permuted across the in-mask pixels (destroying any coherent dipole while preserving the one-point distribution).”
  - Randomly permuting Ap over a patchy mask yields an exchangeable-field null, not an isotropic one, and it does not condition on spatially varying shot noise (Nspiral(p)). It can under/over-weight fluctuations in sparse pixels relative to dense ones for a uniform-weight LS fit.
- Required fix:
  - Re-label this as a “pixel-permutation exchangeability null” and make the per-galaxy label-shuffle null the canonical isotropy-check for the headline. Report the headline (z, p) for both nulls side-by-side and state explicitly which one is primary for cosmological interpretation. Consider a hybrid null that permutes within Nspiral(p) strata to better preserve noise geometry when you choose to use the pixel-permutation null.

P4-META-M4 — Lack of pre-registration/evidence for the peq > 0.6 threshold that flips the qualitative verdict
- Severity: MAJOR
- Section/page: IV.C.a (p. 7–8), III.B (p. 4)
- Why others missed it: The authors state “the generator script has used [peq > 0.6] throughout,” which can appear sufficient; none asked for a pre-specified rationale.
- Problem:
  - The unthresholded sample shows a 0.57% dipole at z ≈ 4.2–4.4; the result becomes null at peq > 0.6. There is no pre-registration or independent rationale for 0.6 specifically. Without it, the risk of an ex post choice tuned to remove the apparent signal remains.
- Required fix:
  - Provide an a priori justification for the peq > 0.6 cut (e.g., decided before looking at dipole results based on classifier calibration properties), or adopt a “threshold-insensitive” headline: present the estimator across a pre-declared ladder (e.g., peq ∈ {0.5, 0.6, 0.7, 0.8}) with a correction for multiple looks, and base claims on stability across that ladder. Alternatively, define the primary estimator on the full sample and treat thresholding strictly as a systematic diagnostic.

P4-META-M5 — Missing independence test vs CE-ResNet map (imprinting risk)
- Severity: MAJOR
- Section/page: II.B (p. 2), Discussion VI.C (p. 13)
- Why others missed it: Reviewers noted non-independence in training labels qualitatively but did not call for a direct map-level independence test.
- Problem:
  - 66.5% of training labels come from CE-ResNet pseudo-labels. You explicitly note that label-shuffle nulls do not test independence from survey-correlated structure “inherited through CE-ResNet.” Yet there is no quantitative cross-map test presented (e.g., cross-spectrum of your Ap with CE-ResNet’s Ap on a matched footprint).
- Required fix:
  - Compute the MASTER-decoupled cross-spectrum (and/or pixel-space correlation) between your Ap and CE-ResNet’s Ap on a matched mask, and report rℓ (or an integrated low-ℓ cross-correlation) with an appropriate null. This directly bounds imprinting from the pseudo-labels.

P4-META-M6 — Unaddressed camera-angle/orientation-phase systematics despite 21.4% argmax flips under D4-TTA
- Severity: MAJOR
- Section/page: Appendix B.c (p. 16), Fig. 2 (p. 6)
- Why others missed it: The D4 test was treated as a classifier robustness check; no one connected it to possible large-scale orientation-phase patterns in the survey tiling.
- Problem:
  - You report “per-galaxy argmax labels flip in 21.4% of cases between Z2 and D4 on borderline galaxies.” DESI-LS bricks have preferred camera orientations and scan angles that vary across the footprint; a rotation-sensitive borderline fraction at the 20% level risks coherent low-ℓ artifacts if orientation-phase correlates with depth or footprint geometry. No brick-orientation template or per-brick angle test is included in the eight-anchor systematics analysis.
- Required fix:
  - Add a test regressing Ap against per-brick camera orientation (or a sine/cosine pair of the orientation angle) and/or include an “orientation-phase” template in the joint WLS fit. Report whether including this template reduces the ℓ = 1 residuals or changes the WLS dipole coefficient.

P4-META-M7 — Domain-shift of “ground truth” for chirality accuracy floor (GZ1 vs DESI-LS imaging) is unquantified
- Severity: MAJOR
- Section/page: II.B (p. 2), Appendix B.e (p. 17)
- Why others missed it: Reviewers accepted the 69.91% as a lower-bound and focused on downstream propagation; none challenged the domain mismatch.
- Problem:
  - The 69.91% chirality accuracy floor is derived from Galaxy Zoo 1 labels (SDSS gri, 0.396″/pix) cross-matched at 1″ to DESI-LS grz cutouts (0.262″/pix, different depths/PSFs). Chirality is visually subtle and can be bandpass/resolution sensitive; using GZ1 as “truth” for DESI-LS imagery may bias the accuracy floor. You cite Galaxy Zoo DESI [Walmsley et al. 2023] for coordinates, but you do not use GZ DESI morphology labels to calibrate chirality accuracy on matched imaging.
- Required fix:
  - Add a calibration using Galaxy Zoo DESI (where available) to check the 69.91% floor on the same imaging and footprint, or explicitly quantify the domain-shift effect (e.g., accuracy computed separately for GZ1 galaxies imaged within the DECaLS sub-footprint). If not feasible, clearly downgrade the strength of any g-factor inference that leans on the GZ1-only floor.

P4-META-m8 — “Harmonic-channel completeness” axis phrase suggests a limited set of axes (“coordinate axes”) rather than area-uniform coverage
- Severity: MINOR
- Section/page: VII.a (p. 14)
- Why others missed it: Others asked for tables/quantiles, but not for axis-sampling semantics in this sentence.
- Problem:
  - “Injected Ap = 1.7% yields median recovered significance z ≈ 68–218 (axis-dependent).” The phrase “across coordinate axes” in the same sentence (and lack of protocol here) could be read as using only special axes (e.g., cardinal RA/Dec), not area-uniform random axes as in Sec. VI.A.
- Required fix:
  - Specify the axis protocol used for the reported range (area-uniform random axes vs fixed cardinal axes), and report median [16, 84]% z explicitly, consistent with Sec. VI.A conventions.

P4-META-m9 — Small cross-reference mismatch: Table I row (vi) “+1.68σ” vs Table IV “+1.69σ”
- Severity: MINOR
- Section/page: Table I (p. 5) vs Table IV (p. 11)
- Why others missed it: One-digit rounding; reviewers focused on larger discrepancies.
- Problem:
  - Row (vi) lists “+1.68” while Table IV reports “+1.69.” This is trivially cosmetic but avoidable.
- Required fix:
  - Harmonize to a single rounded value.

P4-META-m10 — Mean-subtraction weight for MASTER uses Wp = Nall while the field is defined on spirals; risk of over/under-subtraction in spiral-sparse pixels is only partially addressed
- Severity: MINOR
- Section/page: Appendix A.a (pp. 14–15)
- Why others missed it: Reviewers acknowledged the weight sweep; none asked for a like-for-like mean-sub subtraction test for spiral-only support.
- Problem:
  - The apodized MASTER channel uses Wp = Nall and a W-weighted mask mean subtraction on an Ap field defined on spirals. You note a weight-map sweep including Wp = Nspiral, but do not quantify whether the choice materially rotates the ℓ=1 direction or shifts C1 beyond ±1σ.
- Required fix:
  - Add a short summary (Δz, ΔC1, Δaxis) for Wp = Nspiral vs Wp = Nall to demonstrate that the mean-subtraction weight choice does not drive the ℓ = 1 residual.

P4-META-M11 — “Isotropy-null” language for the hemisphere scan not matched to a pure isotropy null (uses label-shuffle only)
- Severity: MAJOR
- Section/page: Appendix C.c (p. 17), Table I row (v) (p. 5)
- Why others missed it: Most attention went to double-penalization; not to the null semantics.
- Problem:
  - The hemisphere-max statistic is assessed against a per-galaxy label-shuffle null (correctly handled with a max-statistic MC). But the language “isotropy” is used in the main text for this diagnostic. The label-shuffle null preserves the observed footprint and depth pattern and can transmit any survey-correlated structure from the classifier into the null; it is an exchangeability null, not a strict isotropy null.
- Required fix:
  - Re-label the null as “label-exchangeable under the observed footprint” and add a sentence clarifying that this test is diagnostic for classifier/systematics structure, not a pure cosmological isotropy test.

## Meta-review recommendation
MAJOR REVISIONS

Rationale: The paper is methodologically ambitious and, on balance, careful, but there are several unaddressed issues that cut across data handling (potential augmentation leakage), null semantics (pixel-permutation and hemisphere tests), selection conditioning (peq > 0.6), and missing independence/systematics tests (CE-ResNet imprint; camera orientation-phase). These are fixable, but they must be addressed clearly in the main text (with concise quantitative additions) before publication.

Union-of-reviews summary
Counting the union of the six reviews (the five prior plus this meta-review), I see roughly:
- Essential blockers: 2–3 (this meta: augmentation leakage; others: frozen DOIs; removal of internal versioning/paths)
- Major blockers: ≈10–14 (block-size bootstrap robustness; σ comparability cleanup; falsification amplitude conventions; abstract/figure reconciliation; independence/systematics tests; pre-registration of thresholds; null semantics clarifications)
- Minor/nits: many (bibliography titles, small rounding, figure captions).

Confidence the paper would survive external peer review after revisions: moderate to high, provided the authors (i) remove internal-audit scaffolding and freeze artifacts with DOIs, (ii) demonstrate no train/val leakage, (iii) add the missing independence/orientation tests and block-size robustness, and (iv) standardize null semantics and σ reporting. The scientific conclusions are likely to hold, but editorial and methodological tightening is required.