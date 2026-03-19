# 04: Robust vs Conditional Claims Table

## The GR Caveat Is RESOLVED

The earlier mock-based analysis showed bounce-vs-SSFSR was weak (median BF ~ 1). This was because the mock injected GR contamination into the DATA but used the WRONG sigma (not inflated for GR) in the inference.

The GR-aware analysis shows: once GR contamination is properly treated (either marginalized or corrected), **bounce vs SSFSR is STRONGLY favored across ALL scenarios:**

| GR Treatment | Median BF vs SSFSR | P(BF>3) | P(BF>100) |
|-------------|-------------------|---------|-----------|
| Ideal (no GR) | 3.3M | 98% | 92% |
| Unmodeled (worst case) | 2.6M | 97% | 91% |
| Marginalized (σ_GR=0.5) | 41k | 97% | 87% |
| **Marginalized (σ_GR=1.0, conservative)** | **329** | **96%** | **67%** |
| Corrected (10% residual) | 3.3M | 98% | 92% |

Even in the MOST CONSERVATIVE scenario (GR marginalized with σ_GR = 1.0 — adding 1.0 in quadrature to the statistical error), the bounce is favored at 329:1 median and >3:1 in 96% of realizations.

**The GR caveat does NOT kill the bounce-vs-SSFSR comparison. It degrades it from "utterly decisive" to "still very strong."**

## Why the Earlier Mock Gave a Weak Result

The earlier mock-based code injected GR shift into the data but used σ_stat (not σ_eff = √(σ_stat² + σ_GR²)) in the Bayes factor computation. This treated GR as a HIDDEN BIAS rather than a KNOWN NUISANCE — equivalent to the experimentalist not knowing about GR effects at all.

In reality, GR projection effects are KNOWN and COMPUTABLE. The observer will either:
(a) Model and subtract them (leaving ~10% residual), or
(b) Marginalize over them (inflating the error bar by √(1 + σ_GR²/σ_stat²))

Both treatments preserve the science case.

## Final Claims Classification

| Claim | Classification | Justification |
|-------|---------------|---------------|
| "Bounce vs tuned multifield: median BF > 7" | **ROBUST** | Holds across ALL GR scenarios (7.9-10.9) |
| "P(BF>3 vs tuned) > 86%" | **ROBUST** | Holds in all scenarios |
| "Bounce vs SSFSR: median BF > 300" | **ROBUST** | Even conservative GR marginalization gives 329 |
| "P(BF>3 vs SSFSR) > 95%" | **ROBUST** | Holds in all scenarios |
| "SPHEREx significance ~6σ" | **CONDITIONAL on GR modeling** | With marginalization: effective σ inflates to ~0.9-1.3 → significance 3.4-4.9σ |
| "Detection would provide strong evidence for bounce" | **ROBUST** | True regardless of GR treatment |
| "Detection would prove bounce uniquely" | **TOO_STRONG_DO_NOT_USE** | Exotic multi-field can still accommodate |
| "MegaMapper at 8.75σ" | **CONDITIONAL on GR correction + multi-tracer** | Degrades to 3-5σ with GR marginalization |
| "f_NL = -35/8 is the cleanest explanation" | **ROBUST** | 0-parameter prediction wins Occam comparison in all scenarios |
