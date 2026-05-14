# P4 v1.0.57 7th VERIFY R-round — REAL — Grok-4 brutal-honesty

**Model**: `x-ai/grok-4-fast` (fallback)
**Wall time**: 22.9s
**Tokens**: prompt=50823, completion=1516, total=52339

---

# Grok-4 Adversarial Peer Review: Chirality Catalog Paper

## Overview
No blockers. The central claim—a null dipole detection at sub-percent sensitivity on a larger sample than Jia et al. (2023)—is new in scale and rigor (1.6× spirals, NS class, bias suite), though it extends rather than revolutionizes prior nulls (e.g., Iye 2020, Jia 2023). Overclaims on "first" audits and sensitivity framings inflate narrative; monopole offset undermines "null" purity without stronger independence proof.

## PAPER-GRO-M1: Abstract & Sec. 1 (Overclaim on novelty)
The paper claims "first published multi-test bias hardening audit suite for any galaxy chirality classifier" (Sec. 1) and "advances beyond CE-ResNet in three respects" including this suite, but Jia et al. (2023) document architectural equivariance tests and validation against GZ1, which function as implicit bias audits; no evidence this is truly "first."  
Fix: Remove "first published" qualifier; reframe as "first explicit multi-test suite with predefined thresholds" to avoid false primacy given prior equivariance validations.

## PAPER-GRO-M2: Abstract & Sec. 5.3 (Inflated sensitivity floor)
Abstract headlines "sub-percent sensitivity" with Fisher floor ~0.29% at 3σ, but empirical injection-recovery floor is >0.5% (strict inequality, no 50% recovery shown at 3σ); the 0.29% is a statistical asymptote assuming zero systematics, yet 9.5σ monopole shows uncorrected bias survives TTA.  
Fix: Lead with empirical >0.5% as primary operational limit; demote Fisher to appendix as "idealized ceiling," clarifying it assumes perfect bias removal unproven here.

## PAPER-GRO-M3: Sec. 4.2 & Conclusions (Monopole undermines null claim)
9.5σ global CW deficit (0.26%) is called "consistent with null" for parity (dipole prior), but lacks independent >10^6-galaxy verification beyond partial SpArcFiRe cross-check; attribution to GZ1 bias via CE-ResNet pathway (67.6% labels) is circular without non-GZ1 reference, dodging monopole as potential signal or irreducible systematic.  
Fix: Explicitly state monopole as unresolved systematic floor contaminating dipole sensitivity; require future non-trained-classifier reference for closure before claiming dipole independence.

## PAPER-GRO-m1: Sec. 1 & Sec. 6.1 (Shamir disfavor overclaim)
Claims Shamir's ~3% asymmetry "disfavored by factor ~6–12" in amplitude, but admits no common-likelihood exclusion due to classifier/selection/footprint differences; this dodges quantitative tension by framing as "amplitude ratio" rather than assessing if Shamir's signal survives under this pipeline.  
Fix: Report as "incompatible at amplitude level under matched footprint" only after deferred matched-analysis; otherwise, state as qualitative methodological contrast without numeric factor.

## PAPER-GRO-m2: Throughout (Inconsistent N_spiral snapshots)
Canonical N_spiral=3,201,160 supersedes prior 3,321,795 snapshot, but tables/figures mix them (e.g., Table II uses old for regions, new for global); this creates load-bearing inconsistencies in σ calculations and comparisons (e.g., older 2.75σ pseudo-C_ℓ vs. new 6.48σ).  
Fix: Recompute all tables/figures with canonical N; add appendix reconciling snapshots with impact on σ (e.g., +>2σ shift in raw pseudo-C_ℓ).

## PAPER-GRO-n1: Sec. 5.4 (Minor LEE correction ambiguity)
Hemisphere max 3.05σ reduced to <1σ post-Bonferroni (~650 trials), but MC LEE p≤10^{-4} (zero/10k nulls) rejects random-label null at >3.7σ; paper attributes to systematics but doesn't quantify if pixel-shuffle preserves mask edges enough for fair null.  
Fix: Add MC null diagnostic (e.g., KS test on depth variance) showing pixel-shuffle underestimates variance by X%; clarify LEE as artifact, not detection.