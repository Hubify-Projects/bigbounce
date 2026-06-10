# P4 auto-2026-06-08_1144pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 296.7s

---

ID: P4-META-E1
Severity: ESSENTIAL
Section + page: Sec. IV.D (Table IV), p. 5; Sec. IV.C/Table III cross-reference, p. 4–5
Why others missed it: Everyone focused on significance mismatches but not on units/normalization coherence between pre- and post-MASTER spectra.
Problem: Table IV lists the “Pre-MASTER pseudo-C(ℓ=1)ℓ (canonical mask)” as 1.696×10−2 with no units, while Table III’s Cℓ are O(10−6) “(sr)”. The 10^4 jump in magnitude without a declared unit or normalization change signals a unit/normalization inconsistency between the pre-MASTER pseudo-spectrum and the (post-)MASTER Cℓ. The manuscript never states the unit for the Table IV entry nor why the scalings differ by orders of magnitude.
Required fix: State explicitly the units and normalization for the pre-MASTER pseudo-Cℓ in Table IV and reconcile them with the (post-)MASTER Cℓ units in Table III. If different normalizations (e.g., NaMaster conventions vs custom) are used, describe them and convert all reported power values to a single, consistent unit system (e.g., “sr” for a dimensionless field) so that amplitudes are comparable across pre/post-MASTER results.

ID: P4-META-E2
Severity: ESSENTIAL
Section + page: Sec. VI.A (Sensitivity Floor), p. 6
Why others missed it: Reviewers noted N-mismatch between Fisher floor and injection but not the fsky inconsistency itself.
Problem: The Fisher 3σ floor is quoted as “∼ 0.29% ... at Nspiral = 3,201,160, fsky = 0.46,” yet nowhere else is fsky = 0.46 defined (masks elsewhere are fsky = 0.49005 and 0.659). This is a cross-reference inconsistency that affects any sensitivity scaling and the headline “floor.”
Required fix: Specify which exact mask (and NSIDE, pixel threshold) underlies fsky = 0.46 or correct the value to match a defined mask. Recompute the Fisher floor consistently for the same N and fsky used in the headline estimators and update the quoted 0.29% if needed.

ID: P4-META-E3
Severity: ESSENTIAL
Section + page: Sec. IV.D (Monopole+Mask Generative Null), p. 4–5
Why others missed it: Prior reviews focused on Ap field inconsistencies, not on the Binomial N used in the generative model.
Problem: The generative null states “per-pixel CW count is drawn from Binomial(ntotal, pglobal CW) on the exact canonical mask,” but “ntotal” is ambiguous. If ntotal is the all-galaxy count N(p)all (used as weights elsewhere), the generative model incorrectly allows non-spirals to contribute to CW counts. The Ap map uses spiral counts only, so the generative null must draw from the per-pixel spiral count N(p)spiral, not N(p)all.
Required fix: Explicitly define ntotal as N(p)spiral (CW+CCW only) and confirm that the generative realizations use the true per-pixel spiral counts. If not, rerun the generative null with N(p)spiral and update Table IV and all dependent claims (e.g., the “99.3% reproduction” figure).

ID: P4-META-M1
Severity: MAJOR
Section + page: Appendix E.a (Morphology Systematics: Edge-on contamination), p. 9
Why others missed it: Others questioned label calibration and systematics but not this internal contradiction.
Problem: The text says “65.7% of visually identified edge-on systems (b/a < 0.3) receive CW or CCW...” This conflates a visual identification with a quantitative axis-ratio threshold (b/a < 0.3), which requires photometric shape parameters not available in the main pipeline (and later described as “canonical follow-up”). The paper cannot both claim a visual identification and simultaneously enforce a numeric b/a cut without stating the source of b/a.
Required fix: Clarify the source of axis ratios: either (i) provide the catalog cross-match and fields used (e.g., DR8 SERSIC/EXP ellipse parameters) and the sample size, or (ii) remove the b/a < 0.3 claim and restrict to a purely visual statement with reproducible criteria. If quantitative, include a reproducible selection and its uncertainties.

ID: P4-META-M2
Severity: MAJOR
Section + page: Throughout (peq usage): Abstract, Sec. III.D p. 3; Sec. IV.E p. 5; Appendix E.b p. 9
Why others missed it: Notation inconsistency was noted, but not the definitional ambiguity of peq itself.
Problem: The manuscript repeatedly uses “peq” without a precise definition: is peq = max(PCW, PCCW) conditional on “spiral,” or max over {CW, CCW, NS}? Several results (e.g., “HC pipeline,” “peq > 0.6/0.8/0.9” subsamples, 1.87M galaxies in the [0.5, 0.6) bin) critically depend on this. Given a three-class model, the difference is substantial.
Required fix: Define peq formally (e.g., peq = max over {PCW, PCCW} conditional on PNS below a stated threshold; or peq = max over all three classes). State the exact filtering used before binning by peq for all “HC” subsamples and reproduce the counts (e.g., 471,049 at peq > 0.9) under this definition.

ID: P4-META-M3
Severity: MAJOR
Section + page: Appendix D.b–c (Cross-spectrum/correlation diagnostics), p. 8–9
Why others missed it: Others flagged sign conventions; none asked for a precise estimator definition.
Problem: The cross-spectrum correlation is reported as “direct cross-spectrum C(Ap×ntotal) at ℓ = 2 gives r = −0.65 with σ = −2.89,” but the construction of r is unspecified (Pearson correlation across m-modes? normalized cross-power rℓ = Cℓ(A,B)/sqrt(Cℓ(A)Cℓ(B))? one- or two-sided?). The null used for σ is also not defined. Without an estimator definition, the result is not reproducible.
Required fix: Provide the precise estimator for rℓ, including normalization, treatment of mode coupling (MASTER or not), and the null ensemble used to derive σ. Replace “C(Ap×ntotal)” with standard notation Cℓ(Ap, ntotal) and give the numeric autopowers used to form rℓ.

ID: P4-META-M4
Severity: MAJOR
Section + page: Sec. III.A (Declared analysis hierarchy), p. 3; Sec. IV.C–D, p. 4–5
Why others missed it: Mask under-specification was flagged, but not the selection effect/conditioning across masks.
Problem: The “headline” null relies on a “strict-superset subsample mask (fsky = 0.659)” chosen after diagnosing a canonical-mask (fsky ≈ 0.49) residual. This opens a hidden conditioning issue: multiple mask choices were explored, but the trials factor for mask selection (and apodization variants) is nowhere accounted for. Without pre-registration or a penalty for mask-tuning, the “headline” null may be over-optimistic.
Required fix: State whether the subsample mask and its apodization were pre-registered. If not, quantify the mask-selection trials (including canonical vs subsample, apodized vs binary) and report an adjusted significance for the ℓ = 1 null on the headline estimator reflecting this choice. Alternatively, adopt a single pre-declared mask and relegate other masks to diagnostics only.

ID: P4-META-M5
Severity: MAJOR
Section + page: Sec. VI.A (Injection–recovery), p. 6
Why others missed it: Others focused on amplitudes/sensitivity, not the missing procedural specification.
Problem: The dipole injection procedure is not specified: how was the A ≈ 0.75% modulation implemented on a masked, depth-weighted sky with per-pixel varying Nspiral? Was injection performed in fCW or Ap; were the probabilities per galaxy perturbed, or counts per pixel resampled; was the global monopole preserved? Without this, the 50%-recovery@3σ threshold is not reproducible.
Required fix: Document the exact injection recipe (mathematical form, e.g., fCW(n̂) = f0 + (A/2) n̂·d̂; how per-pixel counts were generated; whether classifier probabilities or labels were modified; whether the mask/weights were held fixed). Provide pseudocode or a repository script reference and re-state the null used for σ in these tests.

ID: P4-META-m1
Severity: MINOR
Section + page: Abstract p. 1; Table I p. 4
Why others missed it: Variable-name semantics can be overlooked amid larger statistical issues.
Problem: The abstract uses “strict-superset subsample mask (n = 5,547,858)” and Table I labels this as Nmap weighted, not the number of spiral sources. Using “n” for a weighted-sum-of-counts (over all classes) is confusing and can be mistaken for the number of spirals.
Required fix: Rename n = 5,547,858 consistently as Nmap,weighted (or similar) everywhere, and avoid bare “n” for anything other than a literal object count. Add a footnote in the abstract clarifying that this quantity is a weight-sum, not a source count.

ID: P4-META-m2
Severity: MINOR
Section + page: Appendix C.e (Per-imaging-leg), p. 8
Why others missed it: P-value arithmetic here is easy to gloss over.
Problem: The text reports a “family-corrected p-value 0.0086 (≈ 2.4σ family-wise).” Two-sided Gaussian p = 0.0086 corresponds to |z| ≈ 2.64, not 2.4σ. This is a small but systematic arithmetic inconsistency.
Required fix: Correct the σ-equivalent or report only the p-value. If using one-sided mapping, state so explicitly; otherwise, for two-sided, use z ≈ 2.64.

ID: P4-META-m3
Severity: MINOR
Section + page: Sec. III.C (Test-Time Equivariant Averaging), p. 3; Appendix B.d p. 7
Why others missed it: The number looks innocuous because TTA enforces a symmetry by construction.
Problem: “flip-swap correlation = 1.000” is reported without defining the correlation metric or the sample over which it is computed. With floating-point arithmetic and finite data, exactly 1.000 is implausible unless the statistic is deterministically constructed to be identical, in which case it is tautological and uninformative.
Required fix: Define the statistic (e.g., Pearson r between PCW^orig and PCCW^flip across galaxies) and report to sufficient precision (e.g., 0.999997). If it is identically 1 by construction of peq, say so and remove it as a validation metric.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, I count at least 10 essential/major blockers: (i) field-definition inconsistencies (spirals-only vs all-galaxy denominator), (ii) Table III significance arithmetic and configuration mismatches, (iii) LEE accounting ambiguities, (iv) σ vs p contradictions for the canonical residual, (v) undefined/underspecified masks and potential mask-selection conditioning, (vi) missing formal upper limit on the dipole amplitude, (vii) broken/uncertain data/code availability, (viii) training-label circularity and calibration gaps, (ix) bibliographic inconsistencies, and (x) the new issues above (units mismatch in Table IV; fsky inconsistency; ambiguous Binomial N in the generative null; contradictory edge-on/b/a claim; undefined peq; unspecified cross-spectrum estimator; un-documented injection method). My confidence that, after addressing all of these, the paper would survive external peer review is moderate: the core analysis appears salvageable, but it requires a careful, end-to-end clarification pass, recomputation of several results, and tighter statistical hygiene.