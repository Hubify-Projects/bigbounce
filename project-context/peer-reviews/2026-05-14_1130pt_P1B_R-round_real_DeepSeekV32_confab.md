# P1B R-round — REAL cross-vendor — DeepSeek-V3.2 confabulation-hunter

**Model**: `deepseek/deepseek-v3.2` (via OpenRouter)
**Round**: 2026-05-14_1130pt
**Wall time**: 45.8s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=11034, completion=1675, total=12709

---

## PAPER-DEE-B1: Abstract headline sample count mismatch

**BLOCKER** – Abstract vs. footnote vs. table inconsistency.

**Location:** Abstract (line ~30), footnote 1, Table 1.

**Issue:** Abstract states “309,789 frozen samples across two converged dataset combinations.” Footnote 1 stratifies this as 176,840 + 132,949 = 309,789 raw samples, then 123,129 post-burnin, then 119,617 thinned. Table 1 lists 176,840 + 132,949 = 309,789 total samples, matching the abstract. However, the “third Planck-only combination ongoing” is listed in Table 4 as having 114,992 samples. If this third run is “ongoing” and not aggregated into the frozen headline count, why is 114,992 mentioned in the same table? This creates ambiguity: is 114,992 part of the “frozen” count or not? The abstract’s “309,789 frozen samples” should be unambiguous; if the third run is ongoing, its samples should not be included in the frozen total. The text says it is “not aggregated into any frozen-posterior summary statistic,” but Table 4 lists it alongside frozen runs, blurring the line.

**Fix:** Clarify in abstract: “309,789 frozen samples across two converged dataset combinations (176,840 + 132,949). A third Planck-only run (114,992 samples) is ongoing and not included in frozen totals.” Remove the 114,992 row from Table 4 or move it to a separate “ongoing” table.

---

## PAPER-DEE-B2: Savage-Dickey ln B provenance missing

**BLOCKER** – No script or JSON for ln B = +4.8.

**Location:** Section 5 (Model Comparison), footnote 2.

**Issue:** The paper reports ln B = +4.8 (full tension) and –1.2 (Planck+BAO) from Savage-Dickey density ratio, but admits it is “significantly biased for the highly correlated posterior (r = –0.89 between ΔNeff and H0).” There is no reference to a script, JSON, or method that computes this ln B. The claim is load-bearing for the model comparison (ΔAIC = –5.9, ΔBIC = –0.7, ln B = +4.8). Without a reproducible Savage-Dickey calculation, the ln B is an untraceable scalar.

**Fix:** Provide a script (e.g., `compute_savage_dickey.py`) that reads the MCMC chains, computes the Savage-Dickey ratio, and outputs ln B with uncertainty. Cite this script in footnote 2. If the bias is acknowledged, also provide the correlation coefficient r = –0.89 from a reproducible source (e.g., `correlation_summary.json`).

---

## PAPER-DEE-B3: ΔAIC/ΔBIC arithmetic not reproducible from displayed values

**MAJOR** – ΔAIC/ΔBIC numbers cannot be derived from displayed χ²eff and k.

**Location:** Section 5, Table 3 and subsequent equations.

**Issue:** Table 3 lists χ²eff = 1156.2 for ΛCDM (k=6) and χ²eff = 1148.3 for ΛCDM+ΔNeff (k=7). The paper then states ΔAIC = 1162.3 – 1168.2 = –5.9 and ΔBIC = 1194.8 – 1195.5 = –0.7. However, AIC = χ²eff + 2k, so ΛCDM AIC should be 1156.2 + 2×6 = 1168.2 (matches), and ΛCDM+ΔNeff AIC should be 1148.3 + 2×7 = 1162.3 (matches). BIC = χ²eff + k ln n, where n is sample size. The paper does not state n. Without n, the BIC values (1194.8, 1195.5) cannot be reproduced. This is a load-scalar without provenance.

**Fix:** Either provide n (likely the effective sample size after thinning) in Table 3 or in a footnote, or provide a script that computes BIC from the chains and outputs the values. Reference that script.

---

## PAPER-DEE-B4: NaMaster recovery SNR (20.32) without MC seed provenance

**MAJOR** – High pipeline-recovery SNR claim lacks reproducible MC seeds.

**Location:** Section 4, Eq. (1).

**Issue:** The paper reports NaMaster pipeline recovery SNR = 20.32 for injected β = 0.27°, yielding β̂ = 0.238°. This is a methods validation claim. While the pipeline driver script is cited (`pipelines/h200_results/pod1_namaster_umap_2026-04-29/`), the 500 Monte Carlo realizations require specific seeds to reproduce the exact SNR. Without the seeds or a seed list, the SNR is not reproducible.

**Fix:** Provide a file (`mc_seeds.txt`) listing the 500 random seeds used for the noise realizations. Reference this file in Section 4. Alternatively, provide a script that generates the seeds deterministically (e.g., from a fixed seed) and runs the NaMaster pipeline.

---

## PAPER-DEE-B5: ALP MCMC parameter count mismatch

**minor** – ALP MCMC sample count inconsistency.

**Location:** Section 6 (Spectator-ALP consistency check), Table 4.

**Issue:** The text says “Dedicated MCMC sampling of the ALP parameter space (3 configurations, 9,720 total accepted samples).” Table 4 lists “ALP-MCMC (β fitting)” with 9,720 samples. However, the text also says “The coupling-misalignment product is C_aγ × θ_i = 3.4 ± 1.1.” This product presumably comes from the MCMC. But there is no mention of which parameters were sampled (e.g., C_aγ, θ_i, m, etc.) or their priors. The sample count is given, but the parameter space and priors are not, making the result irreproducible.

**Fix:** Provide the ALP MCMC YAML configuration or script that defines the sampled parameters and priors. Cite it in Section 6.

---

## PAPER-DEE-B6: Abstract H0 value mismatch with Table 1

**nit** – Abstract H0 = 67.68 ± 1.06 km/s/Mpc, but Table 1 lists 67.68 ± 1.06 for full-tension and 67.79 ± 1.09 for Planck+BAO+SN. The abstract only cites the full-tension value, which is fine, but the abstract also says “Both frozen dataset combinations find ΔNeff consistent with zero (–0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN) and H0 = 67.68 ± 1.06 km/s/Mpc.” This implies H0 is the same for both combinations, but Table 1 shows they differ slightly. The abstract should either report both H0 values or clarify that the given H0 is for the full-tension combination only.

**Fix:** Adjust abstract to: “Both frozen dataset combinations find ΔNeff consistent with zero (–0.020 ± 0.169 full-tension; +0.065 ± 0.17 Planck+BAO+SN) and H0 = 67.68 ± 1.06 km/s/Mpc (full-tension) / 67.79 ± 1.09 km/s/Mpc (Planck+BAO+SN).”
