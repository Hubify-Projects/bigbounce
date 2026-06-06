# P4 auto-2026-06-06_0004pt — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 344.9s

---

Below are issues I identified that none of the five prior reviewers flagged. Each item includes severity, location, why it was missed, a precise problem statement with a quote, and a required fix.

P4-META-E1
- Severity: ESSENTIAL
- Section + page: Appendix A (p. 7); Sec. IV C–D (pp. 4–5)
- Why others missed it: Reviewers focused on Ap vs fCW scaling and null definitions but not on preprocessing parity between data and MC nulls.
- Problem: Monopole subtraction is described only for the data vector; it is never stated that each MC realization has its own monopole removed before MASTER. Quote: “The monopole subtraction is performed at the data-vector construction step so that the ℓ = 0 mode is removed from the input field … Null distribution: 500 per-pixel random-label permutation realizations.” If the data vector has its (galaxy-weighted) monopole removed, but permutation/binomial MC draws do not have their own monopole removed in the same way, the null distribution’s ℓ=1 leakage will not match the data preprocessing, biasing z at ℓ=1.
- Required fix: Explicitly state and implement that every MC realization (for both label-shuffle and binomial generative nulls) undergoes the identical monopole-subtraction step (recompute and subtract <A>mask,gw per realization) before MASTER. Recompute all quoted ℓ=1 z-scores under this consistent preprocessing.

P4-META-E2
- Severity: ESSENTIAL
- Section + page: Appendix A (p. 7); Table I (p. 4); Sec. IV D (p. 4)
- Why others missed it: Reviewers flagged null ambiguity but not a logical impossibility in the stated “permutation” procedure.
- Problem: The paper repeatedly refers to “per-pixel random-label permutation” as the null. A literal permutation within a pixel leaves the multiset of labels unchanged, so Ap is unchanged and the null is degenerate. Quote: “Null distribution: 500 per-pixel random-label permutation realizations.” That cannot generate a null unless permutation actually means re-draws from a symmetric Bernoulli (binomial) within each pixel.
- Required fix: Replace “permutation” with the mathematically correct operation (independent Bernoulli re-draws per galaxy in pixel p with p=0.5, or with p=pglobal if that is the intended null), and confirm the implementation. Update the text and captions wherever “permutation” is used to avoid implying a no-op.

P4-META-M1
- Severity: MAJOR
- Section + page: Appendix A (p. 7); Sec. IV E (p. 5)
- Why others missed it: Prior reviews noted dimensional issues in cross-spectra but not endogeneity from weight reuse.
- Problem: The field Ap is analyzed with NaMaster using weights Wp = Nall(p); the diagnostic cross-spectrum uses ntotal (i.e., essentially the same Nall) as the template: “The NaMaster weight (mask) map assigns Wp = Nall … direct cross-spectrum C(Ap × ntotal) at ℓ = 2 gives r = −0.65.” This reuses the same depth field both as an analysis weight and as the regressor, inducing endogeneity (a built-in correlation structure) and compromising the interpretation of rℓ.
- Required fix: Repeat the cross-spectrum using either (i) uniform weights, or (ii) weights based on Nspiral only (distinct from the ntotal template), or (iii) a whitened/normalized depth template orthogonalized against the weights. Report rℓ and uncertainties under these de-endogenized configurations.

P4-META-M2
- Severity: MAJOR
- Section + page: Appendix A (p. 7); Table I (p. 4)
- Why others missed it: Others flagged denominator ambiguity; none flagged the weight mis-specification for inverse-variance weighting of Ap.
- Problem: For the scalar field Ap = (NCW − NCCW)/(NCW + NCCW), the per-pixel variance scales ~1/Nspiral(p). Using Wp = Nall(p) (which includes NS) for NaMaster field weighting is a mis-specified inverse-noise proxy and can improperly emphasize elliptical-rich regions with few spirals, biasing low-ℓ estimates and their null scatter.
- Required fix: Provide a control analysis with Wp = Nspiral(p), and report ℓ=1 amplitudes and z under this weight. If results change materially, motivate and justify the final choice of weight based on variance modeling.

P4-META-M3
- Severity: MAJOR
- Section + page: Sec. IV C.a (p. 4)
- Why others missed it: Focus was on bootstrap definition, not on estimator efficiency.
- Problem: The “simple dipole” fit does not state whether pixels are inverse-variance weighted. Quote: “the fitted dipole has amplitude significance 0.43σ (p = 0.30 from the isotropic-null bootstrap).” Given strong heteroskedasticity in Nspiral per pixel, an unweighted fit is suboptimal and can downweight high-signal pixels.
- Required fix: Specify and adopt inverse-variance pixel weighting (e.g., weights ∝ Nspiral(p)) for the real-space dipole fit; report results side-by-side with the unweighted fit to demonstrate robustness.

P4-META-M4
- Severity: MAJOR
- Section + page: Sec. II A (p. 2); Data flow throughout
- Why others missed it: Others scrutinized mask geometry and nulls, not catalog-level duplication risks.
- Problem: Possible object duplication is not ruled out. Quote: “The dataset includes unique dr8 id identifiers; sky coordinates are obtained by cross-matching against the Galaxy Zoo DESI predictions catalog.” The paper does not state that rows are unique by dr8 id (or BRICK_PRIMARY) after cross-match. Overlaps or multiple cutouts per id would introduce position-dependent weighting and brick-boundary artifacts (the latter are observed in Appendix C.d), contaminating large-scale modes.
- Required fix: Add and report a strict de-duplication step keyed by DR8 unique identifiers (and/or BRICK_PRIMARY=1), verify unique-object counts equal catalog row counts, and re-run headline estimators on the deduplicated catalog. Quantify any changes in ℓ=1 and diagnostics.

P4-META-M5
- Severity: MAJOR
- Section + page: Appendix A (p. 7)
- Why others missed it: Ap vs fCW scaling issues drew attention away from linear-algebra stability.
- Problem: The stability of the MASTER deconvolution at ℓ=1 is not documented. With a patchy, binary mask (canonical) and even with apodization (subsample mask), the ℓ=1 row of the mode-coupling matrix can be ill-conditioned, making z at ℓ=1 sensitive to small mask changes.
- Required fix: Report the condition number of the MASTER coupling matrix (or its ℓ=1 row’s effective window function), and demonstrate numerical stability via (i) small mask perturbations (e.g., ±1 count thresholds), (ii) mild bin widening around ℓ=1, and (iii) Tikhonov regularization checks. Confirm that the −0.12σ headline is stable to these variations.

P4-META-M6
- Severity: MAJOR
- Section + page: Sec. III C (p. 3); Appendix B (p. 7–8)
- Why others missed it: Others noted the absence of full D4 TTA but not instrument-angle systematics tied to rotation non-equivariance.
- Problem: The justification for using Z2-only TTA ignores the possibility that rotation non-equivariance can couple to orientation systematics that vary over the sky (e.g., camera angle distributions, scan strategy), leaking into low-ℓ modes even if chirality per se is rotation-invariant. The small D4-TTA hold-outs (N≈1.6–2.0k) do not probe this at survey scale.
- Required fix: Include a sky-map test of Ap versus the local distribution of image orientation angles (from cutout WCS/HEADER) or per-leg camera angle proxies. Alternatively, run a limited D4-TTA on a stratified sky sample (spanning all legs and depths) and report ℓ=1 stability versus Z2-TTA.

P4-META-M7
- Severity: MAJOR
- Section + page: Sec. IV B, Table II (p. 4)
- Why others missed it: Others checked arithmetic on z but not the variance model behind it.
- Problem: The 9.5σ “Dev. (σ)” for the global CW fraction in Catalog C uses a pure binomial σ = sqrt(p(1−p)/N) with N = 3,201,160. However, counts are based on argmax labels from a noisy classifier (69.91% agreement to GZ1), inflating variance beyond binomial. The quoted σ thus overstates significance for the global monopole.
- Required fix: Provide an overdispersion-corrected σ (e.g., via a beta-binomial or a bootstrap over galaxies using the soft probabilities), and recompute “Dev. (σ)” for Table II. Emphasize that the monopole is a classifier artifact and avoid assigning unwarranted high z to it.

P4-META-m1
- Severity: MINOR
- Section + page: Sec. IV D; Table IV (p. 5)
- Why others missed it: Others questioned numbers but not the field mismatch in the leakage demo chain.
- Problem: The leakage demo compares pre-MASTER pseudo-Cℓ at ℓ=1 computed on the “un-monopole-subtracted CW-fraction map” (i.e., fCW) to a binomial generative model with pglobalCW = 0.4974. This is fine, but it should be stated explicitly that these are fCW-based pseudo-Cℓ (not Ap), otherwise the 10^2–10^3 scale jump relative to Ap-based Cℓ obscures interpretability.
- Required fix: In Table IV and the surrounding text, label the field explicitly as fCW (not Ap), and add a one-line crosswalk explaining the scale difference relative to the monopole-subtracted Ap results.

P4-META-m2
- Severity: MINOR
- Section + page: Sec. VI C (p. 6)
- Why others missed it: Others suggested adding more systematics but didn’t pinpoint specific, high-signal templates left out.
- Problem: The “open follow-up” list omits Galactic dust extinction E(B−V), which is a prime driver of footprint-correlated morphology/photometry systematics and is implicated by the SGP > NGP asymmetry (Appendix C.b).
- Required fix: Add an extinction template (e.g., SFD E(B−V)) to the cross-spectrum and the WLS template set, and report its partial correlation at low ℓ and the impact on ℓ=1 residuals.

P4-META-m3
- Severity: MINOR
- Section + page: Sec. II B (p. 2–3), Sec. III D (p. 3)
- Why others missed it: The training–inference split was taken at face value.
- Problem: The manuscript uses CE-ResNet pseudo-labels for 67.6% of training data and then deploys on a DESI footprint largely overlapping Galaxy Zoo DESI; there is no explicit assurance that training labels are disjoint from the deployed catalog beyond the 234,282 “independent GZ1 cross-match” used for evaluation. Without a hard train–test separation on sky, small leakage (even via near-duplicates) can bias large-scale anisotropy tests.
- Required fix: Document a strict spatial/ID-based split ensuring no training object (or near-duplicate) appears in the deployed catalog used for cosmology. Provide counts and a leakage check (e.g., hash-based deduplication, WCS-based near-duplicate pruning).

P4-META-m4
- Severity: MINOR
- Section + page: Sec. VI A (p. 6)
- Why others missed it: Others focused on Fisher arithmetic but not on the injection protocol itself.
- Problem: The injection–recovery description does not state whether injection is applied to soft probabilities or hard labels, nor whether injection preserves per-pixel Nspiral and mask geometry during Monte Carlo. This matters for mapping Atrue → Aobs under classifier noise and masking.
- Required fix: Specify the injection mechanism (additive modulation of soft pCW/pCCW vs relabeling), whether it’s applied at the galaxy level before pixelization, and confirm that per-pixel Nspiral and masking are held fixed. Provide a brief validation showing Aobs scales linearly with Ainjected over the tested range.

P4-META-n1
- Severity: NIT
- Section + page: Sec. III C (p. 3)
- Why others missed it: They focused on D4 vs Z2 content, not coordinate semantics.
- Problem: The paper assumes a “horizontal reflection” is the appropriate chirality-flipping operation for all cutouts, which presumes consistent image orientation (north up, east left). This is likely true for Legacy cutouts but is not stated.
- Required fix: Add a one-sentence note confirming all cutouts are oriented consistently (north up, east left), so a horizontal pixel reflection corresponds to a physical mirror operation on the sky image for chirality.

## Meta-review recommendation
MAJOR REVISIONS

Given the union of all six reviews, I count at least a dozen load-bearing issues that require revision: inconsistent or ambiguous null construction and preprocessing (including potential monopole-subtraction mismatch), ambiguous “permutation” null semantics, endogeneity in cross-spectra due to reusing weights as regressors, weight mis-specification for inverse-noise purposes, lack of de-duplication proof for DR8 objects, missing estimator-weighting details, and unproven numerical stability at ℓ=1. I am moderately confident that the headline qualitative conclusion (no ℓ=1 dipole under the authors’ primary estimator) will survive external peer review after these corrections, but the reported significances and several diagnostics will likely shift once the analysis is made internally consistent and fully specified.