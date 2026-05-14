# P4 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_1200pt
**Wall time**: 61.4s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=49869, completion=1264, total=51133

---

## PAPER-DEE-B1 (BLOCKER)
**Section:** Abstract, Sec. 4.1 (Catalog Statistics), Sec. 5.1 (Dipole Analysis), Table 2, Table 3, Fig. 1 caption.
**Issue:** The canonical spiral count `N_spiral = 3,201,160` is a load-bearing scalar for all Poisson uncertainties, shot-noise normalization (`C_ℓ^noise = 4π f_sky / N_spiral`), and significance calculations. The paper states this number supersedes an earlier snapshot (`3,321,795`). However, there is no traceable script or JSON artifact that reproduces `3,201,160` from the raw catalog data on disk. The abstract and conclusions present results (e.g., `σ_global ≈ 0.000279`, dipole significance) that depend on this number, but its provenance is opaque.
**Fix:** Provide a standalone reproducibility script (e.g., `scripts/verify_spiral_count.py`) that loads the production Parquet file, applies the documented selection (`class_eq in {CW, CCW}`), and prints the count. Deposit the script's output log as a companion artifact.

## PAPER-DEE-B2 (BLOCKER)
**Section:** Abstract, Sec. 5.1 (Dipole Analysis), Table 3.
**Issue:** The headline dipole significances (`0.43σ` real-space, `-0.122σ` post-MASTER) are derived from Monte Carlo runs (`N_MC = 10,000` and `500`). The paper cites companion artifacts (e.g., `outputs/dipole/summary.json`, `master_results/master_power_spectrum.json`) but does not specify the exact random seeds or the algorithm for generating null realizations (e.g., per-pixel label shuffling). Without seeds and code, the MC distributions are not reproducible.
**Fix:** In the code repository, document the exact random seed(s) used for each MC run (real-space dipole, pre-/post-MASTER). Provide a minimal script that regenerates one null realization and the corresponding test statistic, verifying the stored summary statistics match.

## PAPER-DEE-M3 (MAJOR)
**Section:** Abstract, Sec. 4.2 (Global CW Fraction), Table 2.
**Issue:** The global CW fraction `0.4974 ± 0.000279` and the `9.5σ` deviation from parity are calculated using `N_spiral = 3,201,160` and the binomial formula. The uncertainty `0.000279` is given to 6 significant figures, but the calculation `sqrt(0.4974*(1-0.4974)/3201160)` yields `0.0002792...`. The paper does not provide the exact floating-point value or the script that performed the calculation. The `9.5σ` figure (`(0.5000-0.49735)/0.000279`) also depends on an intermediate value (`0.49735`) not explicitly stated in the text.
**Fix:** Provide a small JSON artifact (`global_cw_fraction.json`) containing the exact `N_CW`, `N_CCW`, `N_spiral`, computed `p`, `sigma_binomial`, and the `sigma` deviation. Include the formula and a reference to the script that computes it.

## PAPER-DEE-M4 (MAJOR)
**Section:** Sec. 5.3 (Hemisphere Asymmetry), footnote 6.
**Issue:** The look-elsewhere-corrected p-value (`p_LEE < 10^-4`) is derived from a Monte Carlo run with `N_MC = 10,000` on an `NSIDE=8` pixelization. The result is cited as an upper bound, but the method for generating the null distribution (label shuffling) and the test statistic (`max_hat{n} |A(hat{n})|`) is only loosely described. The exact mapping from the `~650` hemisphere directions to the `768` pixel centers at `NSIDE=8` is not specified, making the trials factor ambiguous.
**Fix:** Provide the script that performs the hemisphere scan and the MC calibration. Specify the exact set of direction vectors (e.g., as a list of (l,b) pairs or HEALPix pixel indices) used for the maximum statistic. Deposit the null distribution array.

## PAPER-DEE-m5 (minor)
**Section:** Sec. 4.3 (Bias Hardening Suite), Table 4.
**Issue:** The bias test thresholds (e.g., T8: CW balance `50% ± 10%`) are described as "generous" relative to the target sub-percent sensitivity. However, the pass/fail results for individual tests (e.g., T2 rotation stability `89.8%`) are presented without uncertainties. The `89.8%` is a mean agreement across rotations; its standard error depends on the sample size used for the test, which is not stated.
**Fix:** For each bias test, report the sample size `N` used to compute the metric and a measure of uncertainty (e.g., standard error or confidence interval). Clarify whether the test was run on the validation set or a dedicated bias-audit subset.

## PAPER-DEE-m6 (minor)
**Section:** Sec. 5.6 (Confidence Stratification).
**Issue:** The stratification into high/mid/low confidence bins uses thresholds (`>0.9`, `0.6-0.9`, `0.5-0.6`) but the exact counts in each bin (`N = 471,049`, etc.) are not linked to a script that reproduces them from the catalog. The subsequent dipole significances per bin are therefore not traceable.
**Fix:** Provide a script that reads the catalog, applies the confidence cuts, and outputs the per-bin spiral counts and dipole fit results. Deposit the output as a small JSON file.
