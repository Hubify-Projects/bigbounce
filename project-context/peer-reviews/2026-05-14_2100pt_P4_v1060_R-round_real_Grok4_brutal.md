# P4 v1.0.60 10th VERIFY R-round — REAL — Grok-4 brutal-honesty

**Model**: `x-ai/grok-4-fast` (fallback)
**Wall time**: 17.0s
**Tokens**: prompt=51763, completion=1386, total=53149

---

# Grok-4 Adversarial Peer Review: Chirality Catalog Paper

No blocker-grade findings. The central null claim holds as a valid measurement under the authors' pipeline, though sensitivity is overstated due to uncorrected monopole bias. Five major/minor findings follow.

## PAPER-GRO-M1: Overclaimed Sensitivity Floor

**Section:** Abstract and Sec. 7.4 (Sensitivity Floor)

**Issue:** Empirical sensitivity floor of >0.5% at 3σ is presented as primary publication-grade limit, but residual 9.5σ monopole bias (0.26% CCW excess) exceeds this and remains uncorrected, inflating claimed sub-percent precision; Fisher 0.29% asymptote ignores this systematic entirely.

**Fix:** Demote empirical floor to >1% incorporating monopole as irreducible bias; report Fisher only as hypothetical zero-systematics bound, not achievable asymptote.

## PAPER-GRO-M2: Inflated Disfavoring of Shamir

**Section:** Abstract and Sec. 6.1 (Shamir Comparison)

**Issue:** Claims Shamir's ~3% asymmetry disfavored by factor ~6-12 under present pipeline, but admits no matched analysis (different classifier, selection, footprint); framing as amplitude-ratio rejection dodges lack of σ-level exclusion, overstating tension as methodological superiority without joint inference.

**Fix:** Rephrase as "inconsistent at amplitude level under unmatched pipelines; common-likelihood exclusion requires future matched reanalysis" – remove numerical factor to avoid implying statistical rejection.

## PAPER-GRO-M3: Non-Novel "First" Claims

**Section:** Introduction and Abstract

**Issue:** Labels as "first published multi-test bias hardening audit suite" and "most sensitive chirality measurement," but Jia et al. (2023) CE-ResNet already provides architectural equivariance (stronger than post-hoc TTA) on 1.95M galaxies with near-null; extension to 3.2M spirals and NS class is incremental, not unprecedented given prior nulls (Iye 2020, Tadaki 2020).

**Fix:** Qualify as "first comprehensive bias suite for ViT-based chirality on DESI DR8" and "largest sample to date," removing absolute "first/novel" framings; cite Jia/Iye as direct priors for null sensitivity.

## PAPER-GRO-minor1: Inconsistent Headline Numbers

**Section:** Abstract vs. Sec. 4.2 (CW Fraction)

**Issue:** Abstract quotes N_spiral=3,201,160 and 0.43σ dipole, but text reveals snapshot discrepancies (e.g., Table 2 uses superseded 3,321,795); monopole σ=9.5 uses rounded value, exact 9.47σ hidden in artifacts, creating non-load-bearing precision illusion.

**Fix:** Standardize all tables/sections to canonical N_spiral=3,201,160; report exact 9.47σ in text, not just artifacts, for transparency.

## PAPER-GRO-minor2: Dodgy Monopole Attribution

**Section:** Sec. 4.2 and Sec. 6.3 (SpArcFiRe)

**Issue:** Attributes 9.5σ monopole to GZ1 bias via CE-ResNet pathway as "leading working hypothesis," but partial SpArcFiRe cross-check (~140k galaxies) is inconclusive (no joint tabulation); claims independence from dipole null, yet uncorrected monopole contaminates sensitivity claims without independent >10^6-scale verification.

**Fix:** Explicitly state hypothesis unverified due to missing large-scale independent reference; bound sensitivity floor above monopole amplitude (e.g., >0.3%) until resolved.