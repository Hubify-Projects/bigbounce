# P4 v1.0.55 VERIFY R-round — REAL cross-vendor — Grok-4 brutal-honesty

**Model**: `x-ai/grok-4-fast` (fallback after x-ai/grok-4 502)
**Wall time**: 16.1s
**Tokens**: prompt=49660, completion=1484, total=51144

---

```markdown
# Grok-4 Adversarial Peer Review: P4 v1.0.55

## Overview
No BLOCKER findings. 4 MAJOR findings on overclaims, inconsistencies, and dodgy framings. Central claim (null dipole at ~0.5% empirical sensitivity) is solid but not revolutionary—builds directly on Jia (2023) null with larger sample and bias suite, while Iye (2020) already nullified Shamir's claims via bias correction. "First" and "unprecedented" framings inflate novelty; sensitivity mixes statistical asymptote with empirical floor misleadingly. Prior round closures hold (e.g., canonical N_spiral recount verified, MC seeds documented), but new issues emerge in narrative polish.

## PAPER-GRO-M1: Abstract & Sec. 1 (Overclaim on novelty vs. literature)
Concrete issue: Claims "first published multi-test bias hardening audit suite" and "advances beyond CE-ResNet in three respects" (scale, NS class, audit), but Jia (2023) already has architectural equivariance (stronger than post-hoc TTA) and implicit bias controls via symmetry guarantee; Iye (2020) audited citizen-science biases quantitatively. NS class is incremental, not transformative; scale gain (1.6x spirals) is honest but framed as "unprecedented" despite Shamir's smaller but multi-survey scope.  
Fix: Retract "first" and "unprecedented"; reframe as "extends Jia's equivariant null with 1.6x spirals, explicit NS rejection, and 8-test suite complementing architectural symmetry."

## PAPER-GRO-M2: Abstract & Sec. 5.5 (Sensitivity floor ambiguity and overconfidence)
Concrete issue: Abstract headlines "sub-percent sensitivity" blending empirical |A_dipole| ≳0.5% (50% recovery under shuffles, primary) with Fisher asymptote ≲0.29% (updated from 0.2%, zero-systematics), but MC injection-recovery shows <50% detection even at 0.5% (P(σ>2)=0.18), and 0.29% assumes perfect systematics removal unproven here (e.g., no full PSF/scan cross-correlation closure). Factor-of-2 convention update buried in conclusions deferral feels like post-hoc dodge.  
Fix: Lead with empirical 0.5% as sole operational limit; demote Fisher to appendix with explicit "unachieved asymptote" caveat; recompute MC to confirm 50% threshold explicitly.

## PAPER-GRO-M3: Sec. 4.2 & Table II (Monopole significance inflation via snapshot inconsistencies)
Concrete issue: 9.5σ monopole (CW=0.4974) uses canonical N_spiral=3,201,160, but Table II sky_balance retains superseded snapshot N=3,321,795 with footnote disambiguating; regional Δ≤0.32% shifts <4% under canonical but not recomputed explicitly, risking reader confusion on uniformity claim. Bootstrap on raw A confirms 28.8σ but ignores spatial correlations reducing N_eff.  
Fix: Recompute Table II fully at canonical N; add N_eff estimate via pixel variance; clarify 9.5σ as working hypothesis, not load-bearing for dipole null.

## PAPER-GRO-M4: Sec. 6.1 & Sec. 7 (Shamir disfavor as amplitude factor dodges sigma-level tension)
Concrete issue: Claims Shamir's ~3% disfavored by ~6-12x amplitude under "present pipeline," but avoids sigma exclusion citing mismatches (classifier, selection, footprint); this understates tension—Iye (2020) already ~3-5σ null vs. Shamir via bias correction on similar scales, and your 16x larger sample + TTA should enable matched-analysis p-value, not handwave. "Not constructed here" feels evasive.  
Fix: Compute joint-likelihood sigma under shared DESI subset (your 3.2M vs. Shamir's ~200k spirals); report as >5σ exclusion if valid, or justify non-comparability quantitatively.
```