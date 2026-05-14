# P4_v1063 R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_2245pt
**Wall time**: 52.6s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=57205, completion=1683, total=58888

---

## Adversarial Peer Review Findings (13th Round, v1.0.63)

**Overall Assessment:** The v1.0.63 edits successfully close the propagation and reframing tasks from the 12th round. The headline estimator chain is now internally consistent, the "mild excess" interpretation is load-bearing, the honest-interpretation list is clear, and the table expansion is unambiguous. No new BLOCKERs or MAJORs were introduced. However, several minor/nit issues persist regarding traceability and clarity of certain load-bearing scalars.

### PAPER-DEE-B1: BLOCKER — Abstract's "empirical $|A_{\rm dipole}|\!>\!0.5\%$" lacks explicit trace to on-disk MC result
**Location:** Abstract, line ~95.
**Issue:** The abstract states the "conservative, systematic-inclusive empirical injection-recovery sensitivity floor is $|A_{\rm dipole}|\!>\!0.5\%$" and cites "(at $A\!=\!0.5\%$ the per-pixel-shuffle MC gives $P(\sigma\!>\!2)\!=\!0.18$)". However, this specific $P(\sigma\!>\!2)\!=\!0.18$ number is not directly traceable to a committed JSON/NumPy file in the listed companion artifacts (`canonical_n_master_l1_direct.json`, `null_distribution.npy`, `mc_seed_manifest.json`). The manifest references hemisphere and MASTER nulls, but not the injection-recovery MC that produced the $0.18$ probability.
**Fix:** Commit the injection-recovery results JSON (e.g., `wave_14_nn_injection_recovery.json`) to `outputs/canonical_provenance/` and add its SHA to `mc_seed_manifest.json`. Update the abstract citation to point to this file.

### PAPER-DEE-M1: MAJOR — Conclusions item 1 conflates statistical and empirical floors without clear provenance
**Location:** Conclusions, item 1 (lines ~2420-2430).
**Issue:** The conclusion states: "we achieve a conservative empirical minimum detectable dipole of $\sim\!0.5\%$ at $3\sigmaunit$ ... the statistical-only Poisson floor ... is $0.2\%$ (corresponding to a full-amplitude $A$-floor of $0.4\%$ conservative, $\sim\!0.29\%$ Fisher exact)". The derivation of the $0.2\%$ (half-modulation) and $0.4\%/0.29\%$ (full-amplitude) numbers is described in Section IX (Sensitivity) but relies on arithmetic from Eq. (\ref{eq:sigma_dip}) ($\sigma=0.048\%$). The final rounded values ($0.2\%$, $0.4\%$) are not themselves stored in a canonical JSON. Their status as "conservative" rounded values is interpretive, not directly reproducible from a script output.
**Fix:** Add a canonical JSON file (e.g., `fisher_sensitivity_floor.json`) that records the raw $\sigma=0.048\%$ from Eq. (13), the $3\sigma$ ideal floor ($0.144\%$), the $f_{\rm sky}$ and $N_{\rm eff}$ correction factors applied, and the final rounded conservative floors ($0.2\%$, $0.4\%$). Cite this file in the conclusions.

### PAPER-DEE-M2: MAJOR — Table III footnote's pixel-weighted count (5,547,858) is untraceable
**Location:** Table III caption and footnote (lines ~1240-1245).
**Issue:** The footnote distinguishes the "subsample *pixel-weighted galaxy count* (5,547,858)" from the "underlying spiral catalog (3,201,160)". This 5.5M figure is critical for understanding the $-0.122\sigma$ result but is not present in any of the referenced companion artifacts (`master_power_spectrum.json`, `wave_14_pp_namaster_verification.json`). Its provenance is unclear.
**Fix:** Ensure the `master_power_spectrum.json` file contains an explicit field for `n_pixel_weighted_galaxies` (or equivalent) with value 5,547,858. Alternatively, create a separate verification file that documents how this count is derived from the analysis mask and catalog.

### PAPER-DEE-m3: minor — "9.5σ" monopole significance rounding is slightly inconsistent
**Location:** Abstract (line ~140) and Conclusions (line ~2422) vs. Section \ref{sec:cw_frac} (line ~1015).
**Issue:** The abstract and conclusions round the global CW fraction deviation to "$9.5\sigmaunit$". Section \ref{sec:cw_frac} gives the exact calculation: $(0.5000-0.49735)/0.000279 = 9.47\sigma$, rounded to $9.5\sigma$. This is fine, but the accompanying text in Sec. \ref{sec:cw_frac} says "rounded to $9.5\sigma$" while the abstract/conclusions present it as a direct figure. The `global_cw_fraction.json` artifact (line ~2365) reports the exact 9.47, providing traceability.
**Fix:** Minor clarity improvement. In the abstract/conclusions, consider adding "($\approx 9.5\sigma$)" or a footnote referencing the exact value in the provenance file. No change is strictly necessary as provenance exists.

### PAPER-DEE-m4: minor — Hemisphere LEE $p_{\rm LEE}\!\le\!10^{-4}$ provenance is indirect
**Location:** Abstract (line ~155) and Section \ref{sec:hemisphere} (footnote at lines ~1330-1340).
**Issue:** The $p_{\rm LEE}\!\le\!10^{-4}$ bound is derived from "zero of $10{,}000$ nulls reach the data". The companion artifact `results.json` and `max_null.npy` are referenced and hashed in the manifest. This is traceable. However, the abstract's statement "corresponding to post-LEE significance $\gtrsim\!3.7\sigmaunit$ under that specific null" is an *interpretation* (converting $p \le 10^{-4}$ to a Gaussian $Z$-score) not stored in an artifact.
**Fix:** The fix is optional. For perfect traceability, add a field in the `results.json` artifact like `"post_lee_gaussian_sigma_lower_bound": 3.7` calculated from the MC p-value. Currently, the raw MC result is traceable, which is sufficient.

### PAPER-DEE-n5: nit — "mild canonical-mask excess of $+1.85\sigmaunit$" p-value description is slightly ambiguous
**Location:** Abstract (line ~75) and Table III caption (line ~1235).
**Issue:** The text states the direct-MC yields "$+1.85\sigmaunit$" and is "below this paper's 3σ detection threshold". The Conclusions (line ~2395) add the empirical-rank p-value "$p_{\rm MC}=15/500=0.030$". The $1.85\sigma$ is a Gaussian-equivalent Z-score derived from $(C_1^{\rm data} - \langle C_1^{\rm null} \rangle)/\sigma_{\rm null}$. The $p=0.030$ is a one-tailed rank. The dual representation is clear but could cause a reader to mistakenly think $1.85\sigma$ corresponds to a two-tailed p=0.03.
**Fix:** Add a brief parenthetical in the abstract or Table III caption: "(Gaussian-equivalent $+1.85\sigma$; one-tailed empirical $p=0.030$)". This links the two numbers explicitly.
