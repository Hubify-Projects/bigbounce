# P5 R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v3_P5_v0_1_32
**Wall time**: 230.2s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=27850, completion=9439, reasoning=8613, total=37289

---

## PAPER-DEE-B1 (BLOCKER) – Abstract per-class n sum contradiction
**Location:** Abstract (lines ~65–75) and Table II; also §VII.C (monopole residual discussion).  
**Issue:** The abstract presents the per-class CW fractions “on the 791,635 chirality-relevant matched spirals” with explicit n values: void 428, wall 6,673, filament 408,187, cluster 397,505. The sum is 812,793, which exceeds 791,635 by 21,158 (2.7%). The paper later acknowledges that the V-Web pipeline uses a “relaxed env-label confidence” that produces a superset of 812,793, while the 791,635 headline subsample excludes those 21,158 galaxies. The headline numbers in the abstract are therefore from the superset, not the claimed 791,635.  
**Fix:** Either (a) re-derive the per-class counts using the strict 791,635 subsample and update the abstract and Table II accordingly, or (b) state the sample size as 812,793 (the env-classified superset) and explain that the subset with relaxed environment assignments includes 2.7% more galaxies, with no impact on the science verdict.

## PAPER-DEE-M1 (MAJOR) – Incorrect monopole offset in abstract
**Location:** Abstract, phrase “catalog-monopole offset of ~0.2 pp”.  
**Issue:** The Paper IV catalog-monopole offset used throughout the manuscript is Δf_CW = −0.0026 = 0.26 percentage points. Rounding to 0.2 pp understates the offset by ~30% and misrepresents the sensitivity floor from which the environment independence is argued. The value appears nowhere else as “0.2 pp”.  
**Fix:** Change “~0.2 pp” to “~0.26 pp” (or “~0.3 pp”) to match the actual offset.

## PAPER-DEE-M2 (MAJOR) – Arithmetic error in filament σ_pred
**Location:** Section VI.A (Results / Cosmic-web environment), statement “predicting σ_pred from Δf_CW = −0.0026 gives σ_pred(filament) ≈ −3.16”.  
**Issue:** Using the paper’s own formula σ_pred = 2·Δf_CW·√N with N = 408,187 gives |σ_pred| = 2·0.0026·√408,187 ≈ 3.32, not 3.16. The miscalculation (off by 0.16) is not a rounding difference; it undermines the claim that the observed filament σ (−2.61) “tracks” the predicted monopole offset with the quoted numeric proximity.  
**Fix:** Recompute and correct the predicted value to ≈ −3.32, and adjust the discussion of how well the observed −2.61 follows it.

## PAPER-DEE-m1 (minor) – Ambiguous “~2σ” statement for void in abstract
**Location:** Abstract, parenthetical “~2σ on the binomial null” when describing the void class counting-statistics floor.  
**Issue:** The abstract explicitly reports the void deviation as −0.68σ, so “~2σ” is contradictory. It likely intends to convey that the 5 pp counting-statistics uncertainty roughly corresponds to a 2σ half-width of the binomial interval, but the phrasing is easily misread as the significance of the void deviation itself.  
**Fix:** Rephrase, e.g., “counting-statistics-limited ~5 pp (void n=428, −0.68σ)” or explain that the 5 pp corresponds to the ~2σ uncertainty (not the deviation).
