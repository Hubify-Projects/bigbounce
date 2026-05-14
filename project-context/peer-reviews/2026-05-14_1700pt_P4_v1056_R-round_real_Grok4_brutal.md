# P4 v1.0.56 6th VERIFY R-round — REAL — Grok-4 brutal-honesty

**Model**: `x-ai/grok-4-fast` (fallback after x-ai/grok-4 502)
**Wall time**: 28.4s
**Tokens**: prompt=50295, completion=1781, total=52076

---

```markdown
# Grok-4 Adversarial Peer Review: Chirality Catalog Paper

## No BLOCKER Findings
The central claim of a null dipole detection at sub-percent sensitivity holds; no fatal flaws undermine the parity-violation null or catalog construction.

## PAPER-GRO-M1: Abstract and Sec. 1 (Introduction)
Overclaims novelty by stating "the first published multi-test bias hardening audit suite for any galaxy chirality classifier" and "advances beyond CE-ResNet in three respects" including 1.6x larger spiral sample, but Jia et al. (2023) already performed equivariance audits and bias checks (e.g., flip consistency, rotation tests); the "audit suite" is not unprecedented, just more explicit. The like-for-like comparison inflates vs. Shamir (16x spirals) while downplaying vs. Jia (1.6x total galaxies, but CE-ResNet lacks NS class so effective chirality sample ratio is closer to 1:1 after excluding non-spirals). Fix: Remove "first published" qualifier; reframe advances as incremental (e.g., "extends CE-ResNet with NS class and explicit 8-test suite building on their equivariance checks"); cite Jia's bias tests directly in Sec. 1.

## PAPER-GRO-M2: Abstract and Sec. 4.2 (Global CW Fraction)
Headline sensitivity floor mixes statistical (0.29% Fisher) and empirical (0.5% injection-recovery) without clear primacy, leading to false confidence in sub-percent null; abstract claims "sub-percent sensitivity" but empirical floor is >0.5% with no 50% recovery shown at 3σ for A≤0.5%, and monopole offset (9.5σ from 50/50) survives TTA, questioning if dipole null is load-bearing over monopole bias. The 0.29% is asymptotic zero-systematics, not operational, yet abstract leads with it. Fix: Abstract and Sec. 4.2 should lead with empirical 0.5% as primary sensitivity (systematic-inclusive); demote Fisher to "statistical ceiling"; explicitly state dipole null holds despite unresolved monopole (e.g., "dipole null at p=0.30 independent of 0.26% monopole offset, attributed to label bias but unverified at scale").

## PAPER-GRO-m3: Sec. 3.2 (Training) and Sec. 4.1 (Catalog Statistics)
Validation accuracy 93.7% is inflated by 67.6% CE-ResNet pseudo-labels (circular), dropping to 69.91% on independent GZ1 cross-match (moderate κ=0.40); paper dodges by framing 93.7% as "internal consistency" but headlines it, understating domain gap and potential bias propagation in chirality (e.g., GZ1's known 1% CW bias). GZ1 agreement is against 75-85% human ceiling, but no error propagation to dipole sensitivity. Fix: Lead Sec. 3.2 with GZ1 69.91% as primary accuracy metric; propagate κ=0.40 uncertainty to sensitivity floor (e.g., inflate empirical 0.5% by √(1/0.40)≈1.6x); add SpArcFiRe cross-check results quantitatively, not just as "partial".

## PAPER-GRO-m4: Sec. 5.1 (Shamir Comparison)
Disfavors Shamir's 3% by "factor ~6-12 in amplitude" but admits no matched analysis (different classifier, selection, footprint), calling it "amplitude factor, not σ-level rejection"; this dodges reviewer scrutiny by avoiding formal tension metric, yet abstract/intro frame as "strongly disfavored" without quantifying incompatibility under joint likelihood. Literature (Iye 2020, Tadaki 2020) already nulls Shamir on smaller samples; not "unprecedented" resolution. Fix: Reframe as "incompatible at amplitude level under present pipeline; formal exclusion requires matched reanalysis" in abstract; add Bayesian tension metric (e.g., via savage-dickey ratio) in Sec. 5.1 using approximate posteriors.

## PAPER-GRO-n5: Sec. 4.5 (Sky Region Balance) and Table III
Regional balance claims "all within 0.5% of 50/50" using equatorial slabs, but admits not aligned with DESI imaging legs (BASS+MzLS/DECaLS/DES); per-leg tabulation deferred, potentially hiding leg-specific systematics (e.g., exposure differences). Table III bandpowers show χ²/dof=4.24 dominated by monopole leakage, not flagged as non-null for ℓ≥2. Fix: Add per-leg CW fractions in Table II (or appendix); interpret χ²/dof as expected under monopole+mask, not "null-consistency"; run/compute per-leg dipole as sensitivity check.

## PAPER-GRO-n6: Sec. 6.1 (Raw Dipole Systematic) and Fig. 6
Claims raw 6.48σ pseudo-Cℓ "fully removed by MASTER to -0.122σ null" as cautionary tale, but older buggy N_spiral=8.47M inflated to 16σ (now historical); narrative inflates pre-correction as "highly significant" without noting it's deterministic mask artifact, not stochastic signal. Axis alignment with Shamir (18.9°) called "coincidence" post-TTA, but pre-TTA match dodges deeper survey-geometry overlap explanation. Fix: Emphasize pseudo-Cℓ inflation as 100% predictable from mask+0.79% bias (add analytic prediction); quantify pre-TTA axis overlap probability under random bias direction.
```
## No Further Findings
Review complete; no additional issues warrant flagging. Central null claim is honest given literature, though novelty is modestly overstated.