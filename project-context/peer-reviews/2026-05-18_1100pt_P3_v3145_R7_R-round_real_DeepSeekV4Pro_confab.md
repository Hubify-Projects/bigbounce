# P3_v3145_R7 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-18_1100pt
**Wall time**: 84.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=57254, completion=5374, reasoning=4251, total=62628

---

# Adversarial Peer Review — Provenance Audit

## PAPER-ADV-B1 (BLOCKER) — Headline `378,280` dedup count is arithmetically unclosed and unproduced

- **Location:** Abstract, §3.4, §6.4 deferral (a), conclusions.  
- **Issue:** The paper’s primary unique‑anomaly number `378,280` is reported as canonical, yet §6.4 explicitly states that under the all‑pairwise assumption the arithmetic upper bound is `387,856` (a `9,576`‑object shortfall) and that the published `378,280` is “frozen … pending a full intra‑survey duplicate recompute.” No script, union‑find manifest, or dataset that actually produces `378,280` is provided. A load‑bearing headline figure is thus being released without a closed, reproducible derivation.  
- **Fix:** Remove `378,280` from the abstract and conclusions until the union‑find recompute is committed; quote the verified upper‑bound `387,856` or release the cluster manifest that proves the lower number.

## PAPER-ADV-M1 (MAJOR) — Abstract falsely attributes 98% blue‑excess contamination to the native LAMOST autoencoder

- **Location:** Abstract, paragraph “LAMOST native contributes ~113,000 additional unique objects …”  
- **Issue:** The abstract states “the native LAMOST autoencoder retains a ~98 % blue‑excess instrumental contamination signature in the released anomaly scores.” This directly contradicts §3.7 and Table 1 footnotes, which show the native retrain reduced the cross‑transfer 98 % blue‑excess to a negligible level and compressed the anomaly rate by 21.5×. The claim incorrectly labels the native‑retrain output as equally contaminated, undermining the paper’s tier‑separation logic and misinforming users.  
- **Fix:** Correct the abstract to state that the native retrain removed the 98 % blue‑excess (the LAMOST contribution remains exploratory‑tier due to low injection‑recovery, not because of a residual 98 % artifact).  

## PAPER-ADV-M2 (MAJOR) — 17.8% genuine novelty fraction lacks any traceable artifact

- **Location:** Abstract, §4.1, §6.3, conclusions.  
- **Issue:** The paper reports a headline novelty fraction of `178/1000` for the DESI top‑1,000 anomalies cross‑matched against “20 curated all‑sky catalogs via CDS X‑Match.” No companion artifact (e.g., a JSON file listing the 822 matches, the queried catalog list, or a script that performs the cross‑match) is cited. Without a traceable output, this key discovery‑rate number has zero provenance.  
- **Fix:** Deposit the cross‑match manifest (e.g., `desi_top1000_cds_novelty.json`) and reference it explicitly in the text; compute the fraction directly from that file so that a reviewer can reproduce the 822/1000 split.

## PAPER-ADV-M3 (MAJOR) — OOD‑sample anomaly‑rate preservation claim is unsubstantiated

- **Location:** Abstract (OOD validation paragraph), §3.2.  
- **Issue:** The abstract asserts “the 0.87 % anomaly rate is preserved on this independent OOD sample,” yet the OOD analysis (§3.2) only reports MSE distribution statistics (median, percentiles). No explicit count or fraction of the 100k OOD spectra that exceed the `S>5` threshold is given. The claim therefore rests on an unvalidated inference, and the paper acknowledges the computation is deferred (item (b) in §6.4).  
- **Fix:** Compute and report the exact anomaly rate (number of OOD spectra with `S>5` divided by 100k) together with the half‑width of its binomial confidence interval. Until that number is published, delete the unsupported “preserved” statement.

## PAPER-ADV-m1 (minor) — Linear‑Fisher CI extrapolation may over‑reach for negative α

- **Location:** Abstract, §5.  
- **Issue:** The 95 % confidence interval for σ(fNL) `[3.64, 12.93]` is obtained by linearly mapping the α interval `[-1.08, 1.46]` through σ(fNL) = 8.98 − 3.66 α. This linear relation was calibrated near α = 0.15; the interval spans α as low as −1.08, where the linear‑bias assumption may no longer hold. The paper does not provide any Fisher‑grid verification that the mapping remains valid for strongly negative bias enhancements. While not a fatal error, the number’s provenance is weaker at those extremes.  
- **Fix:** Either restrict the CI to the domain where the linear scaling was explicitly tested (e.g., α ∈ [0.05, 0.50]) or run a few extra Fisher‑grid points at α = −1.08 to confirm the extrapolation.
