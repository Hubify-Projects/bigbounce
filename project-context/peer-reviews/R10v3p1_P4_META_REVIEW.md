# P4 R10v3p1 — META-REVIEW (synthesizes all 5 prior reviewers)

**Reviewer**: `meta_reviewer`
**Model**: `gpt-5-pro-2025-10-06`
**Input format**: NATIVE PDF + 5 prior reviewer reports as context
**Wall time**: 315.6s

---

META-REVIEW (new issues not caught by any of the 5 referees)

P4-META-E1
- Severity: ESSENTIAL
- Section/page: Table I (p. 4), Sec. IV C/D (pp. 4–5), Appendix A (p. 7)
- Why others missed it: Reviewers focused on arithmetic and cross-references, but did not sanity-check fsky against the DESI footprint or its meaning under weighted masks.
- Problem (quote): “fsky = 0.659 (subsample mask)… fsky = 0.49005 (canonical)” alongside a NaMaster “mask” defined as a weights map Wp = Nall(p) (non-binary; includes NS). DESI Legacy Surveys’ unique sky area is ~14–15k deg² (≈0.34–0.36 of full sky), so fsky ≈ 0.49–0.66 is implausible if fsky denotes the usual unweighted sky fraction. Moreover, fsky is undefined for non-binary masks unless a specific effective definition (e.g., ⟨W²⟩-normalized) is stated. The manuscript presents single fsky numbers without defining whether they are binary-area fractions or effective fsky(W) for a continuous (and unnormalized) weight field.
- Required fix: 
  - Define exactly how fsky is computed for each analysis (binary mask area fraction vs an “effective fsky” for weighted masks with the explicit formula, e.g., fsky,eff = ∫W² dΩ / 4π after normalizing W∈[0,1]).
  - Recompute and report physically consistent fsky values for DESI DR8; if an extended or surrogate footprint is used, document it with a footprint figure and numbers.
  - If a weighted mask is used in NaMaster, either normalize W to [0,1], quote the corresponding effective fsky with its definition, or drop fsky entirely from the text/tables to avoid misinterpretation.

P4-META-E2
- Severity: ESSENTIAL
- Section/page: Sec. IV D (p. 4–5), Table IV (p. 5), Methods/Appendix A (p. 7)
- Why others missed it: Reviewers noted “null conflation,” but did not pinpoint the n used in the binomial generative null.
- Problem (quote): “per-pixel CW count is drawn from Binomial(ntotal, pglobalCW) on the canonical mask,” while earlier Wp = Nall(p) includes NS (non-spirals). If ntotal = Nall was used (as implied by shared notation), the binomial trials incorrectly include NS galaxies when drawing CW/CCW counts, substantially understating the variance of Ap and inflating the “99.3% reproduced” claim.
- Required fix: 
  - Clarify that ntotal in the generative null is Nspiral(p), not Nall(p); if Nall was used, rerun the generative null with Nspiral(p) and update Table IV and any derived claims (e.g., 99.3% reproduction, z-values).
  - Document the exact per-pixel n used in both the permutation (label-shuffle) nulls and the binomial generative null, so they are auditable and consistent with Eq. (3).

P4-META-M3
- Severity: MAJOR
- Section/page: Appendix A(a) (p. 7), Sec. IV C (p. 4)
- Why others missed it: Some noted A-field denominator inconsistencies, but not the bias induced by subtracting a galaxy-weighted monopole computed with a different weight basis than the field itself.
- Problem (quote): “The NaMaster weight (mask) map assigns Wp = Nall… The asymmetry field is Ap = (NCW−NCCW)/(NCW+NCCW)… galaxy-weighted mask-mean subtraction ⟨A⟩mask,gw is subtracted.” The monopole of Ap (spiral-only) is subtracted using weights Wp built from all galaxies (spiral+NS), not spiral counts. This hidden conditioning couples the monopole removal to depth/NS fraction, potentially biasing low-ℓ modes—precisely where the analysis is most sensitive.
- Required fix:
  - Recompute A with three alternative monopole-removal schemes: (i) unweighted pixel mean, (ii) spiral-weighted mean (weights = Nspiral), and (iii) the current Nall-weighted mean. Show that the ℓ = 1 (and low-ℓ) results are stable across these choices (or adopt the scheme with demonstrably least bias).
  - Explicitly justify the chosen weighting for monopole subtraction relative to the field’s own definition.

P4-META-M4
- Severity: MAJOR
- Section/page: Sec. IV C/D (pp. 4–5), Appendix A (p. 7)
- Why others missed it: Prior reviews questioned null choices but not the conditioning structure of the permutation null itself.
- Problem (quote): Multiple places refer to a “per-pixel random-label permutation null” (pp-shuffle). If the permutation is done within each pixel (conditioning on that pixel’s NCW, NCCW, or Nspiral), then the null artificially preserves the per-pixel depth/noise heteroscedasticity and any depth–asymmetry covariance, while erasing only cross-pixel correlations. For a masked-sky isotropy test, a fair null generally requires Poisson realizations using Nspiral(p) and a global pCW (or a spatially uniform Ap with proper pixel noise), not per-pixel label shuffles that can understate the null variance of bandpowers at low ℓ and induce heavy tails.
- Required fix:
  - Specify precisely how the permutation null is constructed. Provide a second null based on Poisson/binomial draws using Nspiral(p) and global pCW across the mask(s), and compare both null distributions for C1 and the bandpowers; adopt the more conservative null (or report both, clearly labeled).
  - If the per-pixel permutation is retained, justify it theoretically (e.g., as a conditional test on observed heteroscedasticity) and discuss its impact on tail behavior and p-values (this likely explains the “z vs empirical rank” discrepancies).

P4-META-M5
- Severity: MAJOR
- Section/page: Sec. II A (p. 2), Data Availability (p. 9)
- Why others missed it: The duplication problem was mentioned historically (Iye et al.) but not audited here.
- Problem (quote): “The dataset includes unique dr8 id identifiers; sky coordinates are obtained by cross-matching against the Galaxy Zoo DESI predictions catalog.” The manuscript assumes that “unique dr8 id” ensures physical de-duplication across overlapping bricks/legs, but offers no deduplication audit (e.g., near-duplicate RA/Dec within a small radius, moving-object/duplicate photometric IDs, or multi-epoch repeats). Given that the DESI Legacy imaging has overlap and the pipeline ingests a third-party HuggingFace set, catalogue-level duplication must be explicitly tested rather than assumed.
- Required fix:
  - Report a deduplication audit: nearest-neighbor RA/Dec matches within 1–2 arcsec across the full catalog, fraction flagged as duplicates, and impact on Ap maps if duplicates are removed.
  - If duplicates are found, re-run the key estimators on a de-duplicated set and update headline numbers if necessary.

P4-META-M6
- Severity: MAJOR
- Section/page: Sec. II A–B (pp. 2–3), Appendix B (p. 7)
- Why others missed it: Focus stayed on statistical presentation; the cross-matching key/astrometry mapping was not scrutinized.
- Problem: The cross-match to Galaxy Zoo DESI “predictions” is said to use a “unique dr8 id,” but GZ DESI typically indexes by LS source identifiers (e.g., ls_id) not always equal to “dr8 id” as used in third-party datasets. Without documenting the join key and an astrometric residual check (e.g., ΔRA/ΔDec histograms), there is a risk of mis-joins that would corrupt the HEALPix Ap map (especially near tile/brick boundaries). The very low “157 failed quality checks” out of 8.47M is implausibly optimistic without an astrometric sanity check.
- Required fix:
  - Document the exact join key(s) used and perform an astrometric offset validation: distribution of positional residuals for a sizeable random sample, with outlier rates. Quantify and remove mis-joins; re-run the dipole estimators post-cleaning.

P4-META-M7
- Severity: MAJOR
- Section/page: Appendix A (p. 7), throughout Results
- Why others missed it: Reviewers noted inconsistent σ vs p, but not the normalization of the weight field fed to NaMaster.
- Problem: The “mask” field passed to NaMaster is Wp = Nall(p), which has arbitrary, dimensional units (counts) and large dynamic range. NaMaster expects a window/weight function; while overall rescalings should cancel in a consistent pipeline, nontrivial dynamic-range differences (few to thousands) can alter the coupling matrix numerics and conditioning. The paper neither normalizes W nor shows a stability test under affine rescaling of W, leaving the decoupled Cℓ potentially dependent on an arbitrary choice of weight scale.
- Required fix:
  - Rescale W to [0,1] (or unity mean) and demonstrate the decoupled Cℓ (including ℓ=1) is invariant within numerical tolerance. If not invariant, adopt a normalized W and re-tabulate key results. State the normalization and its effect on “effective fsky.”

P4-META-m8
- Severity: MINOR
- Section/page: Sec. IV B (p. 4), Appendix E (p. 9)
- Why others missed it: Prior reviews discussed edge-on and dilution, but not the confounding of “quality bins” with classifier-internal probabilities.
- Problem (quote): “pe^q quality-quartile washout” and the “[0.5, 0.6) confidence bin” signal are used as discriminators against a cosmological dipole. However, these bins are defined on the model’s own softmax outputs (max(P_CW^eq, P_CCW^eq)), which correlate strongly with label noise by construction. Absence of monotonic scaling in these internal-probability bins is not an independent physics test and should not be weighted heavily as evidence against a sky signal.
- Required fix:
  - Rephrase these as classifier-internal sanity checks only; add a robustness test using an external quality proxy (e.g., axis ratio, PSF size, or S/N) to stratify the sample and report the corresponding dipole statistics.

P4-META-m9
- Severity: MINOR
- Section/page: Throughout; Data Availability (p. 9), Appendix A (p. 7)
- Why others missed it: Focus remained on numerical consistency rather than reproducibility semantics.
- Problem: The manuscript repeatedly uses “mask,” “weight,” and “fsky” interchangeably across estimators (real-space vs MASTER; canonical vs subsample; apodized vs binary) without a single consolidated definition table. This makes independent reproduction error-prone.
- Required fix:
  - Add a one-page “Mask/Weight glossary” table listing: field definition (Ap), numerator/denominator counts, mask type (binary vs weighted), W normalization (if any), monopole handling, fsky definition, and null used for each estimator. Cross-reference this table from the abstract and Sec. III.A.

P4-META-N10
- Severity: NIT
- Section/page: Appendix A(b) (p. 7)
- Why others missed it: They flagged “C 2 2°” notation as unclear, but not the single-ℓ binning inconsistency.
- Problem (quote): “single-multipole bin… nlb=1” alongside Table III that reports multi-ℓ bandpowers. The code-path for the single-ℓ headline versus the multi-ℓ diagnostic is not cleanly tied to separate binning configs, risking accidental cross-use.
- Required fix:
  - Provide the exact NaMaster binning objects (code snippet) used for single-ℓ and multi-ℓ runs, and confirm no accidental cross-contamination (e.g., a single-ℓ configuration used during a bandpower run).

## Meta-review recommendation
MAJOR REVISIONS

The union of all six reviews uncovers numerous blockers: arithmetic/cross-reference fixes, ambiguous/incorrect null constructions, inconsistent field/mask definitions, and (new here) physically implausible/undefined fsky for weighted masks, an apparently mis-specified binomial generative null (using Nall instead of Nspiral), and a bias-prone galaxy-weighted monopole subtraction for a spiral-only field. My estimate is 12–15 true blockers (≥ ESSENTIAL/MAJOR) across all reviews. Confidence that the paper would survive external peer review after addressing these is moderate, contingent on (i) rerunning the key NaMaster analyses with corrected masks/weights/monopole handling and (ii) providing a robust, footprint-consistent fsky and null framework.