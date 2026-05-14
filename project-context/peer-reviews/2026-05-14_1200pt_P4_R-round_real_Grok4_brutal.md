# P4 R-round — REAL cross-vendor — Grok-4 brutal-honesty reviewer

**Model**: `x-ai/grok-4-fast` (fallback after x-ai/grok-4 returned 502 capacity)
**Wall time**: 15.3s
**Tokens**: prompt=47041, completion=1524, total=48565

---

# Grok-4 Adversarial Peer Review: Galaxy Chirality Catalog Null Detection

## Overview
No BLOCKER findings. The central claim—a null dipole detection at sub-percent sensitivity using the largest chirality catalog—is new, as prior works (e.g., Jia et al. 2023 with 1.95M galaxies; Iye et al. 2020 with ~10^5) lack this scale, NS class, and bias audit suite. "First" and "novel" framings for the audit and scale are honest given literature. However, 4 MAJOR findings flag overclaims on exclusion, sensitivity, and bias attribution that inflate narrative confidence.

## PAPER-GRO-M1: Abstract & Sec. V (Results)
Overclaims Shamir's ~3% asymmetry excluded at >5σ (all-sky) and ~20σ (regional) using empirical 0.5% sensitivity floor as comparator; this dodges methodological mismatch—Shamir's Ganalyzer lacks NS class, bias audit, and equivariant TTA, so exclusion is pipeline-specific, not a direct falsification of Shamir's signal. Reframe as "under present pipeline, Shamir amplitudes disfavored by factor ~6–12 in amplitude" without σ claims, emphasizing non-equivalent methods.

## PAPER-GRO-M2: Abstract, Sec. I (Intro), & Sec. IX.C (Sensitivity)
Headline Fisher-floor sensitivity of 0.2% at 3σ is statistical Poisson asymptote assuming zero systematic dipole projection, but empirical injection-recovery (systematic-inclusive) floor is ≥0.5%; presenting 0.2% as "sub-percent sensitivity" headline misleads by understating the conservative, achievable limit. Clarify in abstract/intro: "statistical floor ~0.2%; empirical systematic-inclusive floor ≥0.5% (50% recovery threshold)" and adopt 0.5% as primary sensitivity metric throughout.

## PAPER-GRO-M3: Sec. IV.B (Training) & Sec. V.B (CW Fraction)
Attributes 9.5σ monopole (0.26% CCW excess in Catalog C) primarily to GZ1 human bias via CE-ResNet pseudo-labels (67.6% of training), but McNemar Z=13.4 on 117k GZ1 cross-match shows Catalog C is 2.1pp less CW-leaning than GZ1, contradicting direct propagation; no independent ≥10^6-galaxy reference exists to confirm. State as "consistent with but not proven by partial SpArcFiRe cross-check; origin unresolved without new reference dataset" and demote to working hypothesis without false confidence.

## PAPER-GRO-M4: Sec. I (Intro) & Sec. VIII.A (Shamir Comparison)
Claims "16× larger than largest prior chirality catalog (Shamir 2022, ~200k spirals)" inflates novelty—Jia et al. 2023 has 1.95M galaxies (all CW/CCW, no NS), closer to 1.6× scale; Shamir's total is ~1.3M but spiral subset smaller. Correct to "1.6× larger spiral sample than CE-ResNet (Jia et al. 2023); ~16× Shamir's spiral subset" and cite Jia as state-of-the-art baseline, not Shamir.

## PAPER-GRO-m1: Sec. V.D (Scale Dependence) & Sec. IX.B (Hemisphere)
3.05σ hemisphere asymmetry dismissed as fluctuation post-LEE (p_LEE <10^{-4} via MC), but amplitude 0.17% is below even empirical 0.5% floor and survives no directional test; look-elsewhere uses conservative Bonferroni/BH but MC bound is resolution-limited upper bound, not precise p-value. Add: "MC resolution floors p_LEE at 10^{-4}; direct analytic Gross-Vitells trials factor needed for exact correction" to avoid overconfidence in null.