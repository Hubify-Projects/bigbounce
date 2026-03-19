# Final Verdict: GR Contamination Claim Hardening

## 1. Does bounce remain strongly favored over tuned multifield after GR-aware analysis?

**YES.** Across ALL five GR treatment scenarios:
- Median BF vs tuned: 7.9-10.9 (strong in all cases)
- P(BF > 3): 86-95% (robust in all cases)
- The Occam penalty is INSENSITIVE to GR treatment because it compares total evidence, not point estimates

## 2. Does bounce remain strongly favored over standard single-field after GR correction/marginalization?

**YES — this resolves the earlier caveat.** Even in the most conservative scenario (GR marginalized with σ_GR = 1.0):
- Median BF vs SSFSR: **329** (very strong)
- P(BF > 3): **96%**
- P(BF > 100): **67%**

The earlier mock result (BF ~ 1 vs SSFSR) was an artifact of treating GR as an UNMODELED hidden bias rather than a KNOWN nuisance. Once GR is properly marginalized (adding σ_GR in quadrature to σ_stat), the comparison recovers strongly.

## 3. Which claims are fully robust, and which are conditional?

### ROBUST (hold in all GR scenarios):
- Bounce vs tuned multifield: median BF > 7
- Bounce vs SSFSR: median BF > 300 (even conservative)
- P(BF > 3) > 86% for both comparisons
- "Bounce provides the cleanest explanation" (0-parameter Occam advantage)
- "Detection of f_NL ≈ -4 would provide strong evidence favoring bounce"

### CONDITIONAL (on GR modeling quality):
- SPHEREx significance: degrades from ~6σ (ideal) to ~3.5-5σ (with GR marginalization)
- MegaMapper significance: degrades from ~8.75σ to ~3-5σ
- Exact Bayes factor magnitude depends on how well GR is modeled

### TOO STRONG (never use):
- "Proves bounce" / "rules out inflation" / "definitive discovery"
- Any claim that doesn't acknowledge GR modeling as a necessary ingredient

## 4. Is the science case now ready to draft?

**YES.** The GR hardening pass achieved ROBUST RESOLUTION:
- Bounce vs SSFSR: BF > 300 even conservatively (≥ 96% of realizations)
- Bounce vs tuned: BF > 7 robustly (≥ 86%)
- GR treatment is a KNOWN methodology requirement, not an unsolvable problem
- The claim structure is now clean: robust core + conditional sensitivity details

## 5. What exact next step should follow?

**DRAFT THE PAPER.** There is nothing left to compute. The full evidence base:

| Component | Status | Samples |
|-----------|--------|---------|
| Theory benchmark | ✅ Verified | — |
| ECH closure | ✅ Complete | — |
| Analytic Bayes factors | ✅ | 100,000 |
| Mock P(k) validation | ✅ | 200,000 |
| GR-aware Bayes factors | ✅ | 500,000 (5 scenarios × 100k) |
| Figures | ✅ 5 generated | — |
| Skeleton + claims table | ✅ | — |

**Total Monte Carlo evidence: 800,000 samples across analytic, mock-based, and GR-aware frameworks.**

All on laptop. No RunPod. No GPU. No MCMC.

The science is done. Write the paper.
