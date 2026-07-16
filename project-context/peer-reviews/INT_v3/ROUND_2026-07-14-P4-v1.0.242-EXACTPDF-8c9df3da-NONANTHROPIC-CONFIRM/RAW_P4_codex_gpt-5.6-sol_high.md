## (1) VERDICT: MINOR REVISIONS

The narrow Physical Review D claim—an observed-label real-space dipole consistent with its permutation null—is supported. Four bounded corrections are required for statistical and reproducibility precision; none demands a conceptual reanalysis or changes the null conclusion.

## (2) Numbered issues

1. **MINOR — NEW VERIFIED: declared mask and executed primary mask differ.**

   **Location/claim:** pp. 3, 5, and 9; Secs. III B and IV C; Table II. The PDF repeatedly defines the HC canonical mask as \(N_{\rm spiral}(p)\ge10\), reporting 23,600 pixels.

   **Evidence:** The load-bearing generator applies `mask = tot > MIN_PIX_COUNT` with `MIN_PIX_COUNT = 10`, hence \(N_{\rm spiral}>10\), not \(\ge10\), in [run_dipole_catalog_c.py](/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/run_dipole_catalog_c.py:133). The exact catalog has 23,600 pixels for \(>10\) and 23,682 for \(\ge10\): 82 ten-object pixels are silently excluded. The committed robustness panel confirms that the inclusive mask remains null-consistent: \(A=0.0045971\), \(z=0.536\), rank \(p=0.2699\) in its 2,000-permutation run.

   **Required fix:** Enforce the declared `tot >= 10`, rerun the exact 10,000-permutation primary calculation, and update every primary number; alternatively, explicitly redefine the mask everywhere as \(N_{\rm spiral}\ge11\). The former is preferable.

2. **MINOR — NEWLY VERIFIED ROOT CAUSE: Fig. 7 plots the wrong raw-catalog column.**

   **Location/claim:** p. 10, Fig. 7 and caption. The left panel is presented as the full Catalog A raw map and called the “methodology cornerstone.”

   **Evidence:** The rendered left panel is nearly empty. Its generator uses `class_raw_x` in [wave_14_fff_fig11_dpi_regen.py](/Users/houstongolden/Desktop/CODE_YOU/bigbounce/pipelines/p2_chirality/wave_14_fff_fig11_dpi_regen.py:37). In the exact 8,474,531-row catalog:

   - `class_raw_x` contains only 34,416 CW/CCW galaxies and produces 620 pixels with at least five raw spirals.
   - Full-coverage `class_raw_y` contains 3,321,795 CW/CCW galaxies and produces 24,158 such pixels.
   - Catalog C produces 24,154 pixels.
   - The full-coverage raw fraction is \(f_{\rm CW}=0.5078787\), matching Table IV’s Catalog A value; the sparse `raw_x` subset is not the displayed Catalog A population.

   The catalog-wide QC code itself defines the raw catalog by preferring `_y` and using `_x` only as fallback. The prior exact OpenAI review suspected a rendering problem; this audit verifies the data-column cause.

   **Required fix:** Regenerate Fig. 7 from the full-coverage raw definition—prefer `class_raw_y`, falling back to `class_raw_x` only where necessary—using a common pixel-support convention for both panels. Print raw/equivariant galaxy and valid-pixel counts in the caption or generation manifest.

3. **MINOR — CURRENT, INDEPENDENTLY CONFIRMED: the primary empirical-rank \(p\)-value is one-sided, not two-sided.**

   **Location/claim:** Introduction p. 2 and Conclusions pp. 15–16 say “two-sided \(p=0.31\)”; the abstract and Sec. IV C p. 9 say only rank \(p=0.31\).

   **Evidence:** The statistic is the nonnegative fitted dipole amplitude. The generator counts upper-tail null amplitudes and applies
   \[
   p=\frac{k+1}{N+1}.
   \]
   My independent exact-catalog recomputation obtained \(k=3{,}084\) of \(N=10{,}000\), hence
   \[
   p=\frac{3085}{10001}=0.308469,
   \]
   explicitly a **one-sided upper-tail empirical-rank value**. No two-sided construction yielding 0.31 is defined.

   **Required fix:** Remove “two-sided” from pp. 2 and 15–16. State the formula, \(k\), \(N\), seed, fitted amplitude, null moments, and pixel count in the primary table or Sec. IV C. If the direction is printed, label it equatorial, not Galactic.

4. **MINOR — CURRENT CONSISTENCY DEFECT: uncalibrated pilot results are still called a recovery threshold.**

   **Location/claim:** Sec. III B p. 3, Table II p. 5, and Data Availability p. 24 call \(A=0.75\%\) a “50%-recovery-at-\(3\sigma\) threshold” or “sensitivity floor.” Sections VI B and VII, pp. 13–16, correctly say the finite grids are not calibrated recovery thresholds or physical limits.

   **Evidence:** The quoted evidence is a finite pilot: 16/20 deterministic axes at \(A=0.75\%\), plus convention-dependent 100-injection score fractions. It does not determine population recovery, coverage, or a physical amplitude limit.

   **Required fix:** Replace the remaining “threshold” and “sensitivity floor” language with the actual pilot score fractions. Do not recommend \(0.75\%\) as a precision-parity boundary without calibrated signal-plus-noise coverage.

5. **STANDING DISCLOSED LIMITATIONS — NOT NEW DEFECTS.**

   **Location:** Abstract p. 1; Sec. VI pp. 13–15; Appendices B and D, pp. 18–23.

   **Evidence:** The paper explicitly discloses the missing spatially resolved confusion/physical transfer model, lack of a matched-footprint independent-estimator comparison, missing joint real-space–harmonic–nuisance covariance, inherited pseudo-label limitations, and absence of external preregistration/blinding. These prevent promotion of the observed-label null into a physical or primordial parity constraint.

   **Required fix:** None for the narrow observed-label claim; retain these disclosures. They must be closed before making a calibrated physical-amplitude or primordial-parity claim.

6. **SUBMISSION-TIME ARCHIVE/DOI GATE — NOT A SCIENTIFIC DEFECT.**

   **Location:** Data Availability p. 24.

   **Evidence:** The immutable release, exact commit manifest, catalog/artifact checksums, and Zenodo DOI are prospective.

   **Required fix:** Before submission, mint the immutable archive/DOI and replace the prospective text with the exact release tag, commit, PDF/catalog hashes, and DOI.

7. **STALE/CLOSED FINDINGS — NOT REOPENED.**

   The exact v1.0.242 text correctly limits WLS and harmonic channels to diagnostics, removes the former physical \(1.7\%\) exclusion, uses the full-amplitude \(A_p=2(f_{\rm CW}-1/2)\) convention, states that \(\ell=1\) is parity-even, and disowns calibrated \(A_{50}/A_{95}\) or primordial bounds. The earlier edge-on square-root penalty error is also corrected. No further fix is required except the residual threshold wording in issue 4.

## (3) Central-claim support

**Supported.** The frozen PDF hash matches the requested SHA-256 exactly, and the local catalog contains exactly 8,474,531 rows.

Using the exact declared HC label selection and the generator’s executed strict \(N_{\rm spiral}>10\) mask, I independently obtained:

- \(N_{\rm HC}=949{,}584\): 471,049 CW and 478,535 CCW.
- 23,600 fitted pixels.
- \(A_{\rm dip}=0.00442297186793\).
- Null mean \(0.00373675659638\).
- Null standard deviation \(0.00168207339374\).
- \(z_{\rm mom}=+0.407958\).
- \(k=3{,}084\), giving one-sided upper-tail rank \(p=0.308469\).
- The recomputed 10,000-element null array agrees with the committed array to maximum absolute difference \(3.1\times10^{-16}\).

Thus the observed hard-label HC field is consistent with its specified isotropic pixel-permutation null. The inclusive-mask cross-check also remains plainly null-consistent. The Fig. 7 error affects the raw-versus-equivariant visualization, not this primary Catalog C calculation.

This supports only an **observed-label null under the stated classifier, selection, footprint, and permutation null**. It does not constrain primordial parity violation. WLS and harmonic results remain systematics diagnostics and do not alter the primary inference.

## (4) Fresh verified MAJOR blocker

**No. There is no fresh verified MAJOR blocker to the narrow observed-label null.** The fresh mask-contract and Fig. 7 defects are mandatory but bounded MINOR corrections: both are locally repairable, and neither reverses or materially weakens the central null result.