# P4_v1064_R2 R-round — REAL cross-vendor — Grok-4 brutal-honesty reviewer

**Model**: `x-ai/grok-4` (via OpenRouter)
**Round**: 2026-05-15_0200pt
**Wall time**: 137.3s
**Persona focus**: Cut through narrative inflation. Flag overclaim, false confidence, headline numbers that aren't load-bearing, anything written to dodge a reviewer rather than to be true. Is the central claim actually new? Are 'first', 'novel', 'unprecedented' framings honest given the actual literature?

---

**Tokens**: prompt=55869, completion=944, total=56813

---

## PAPER-GRO-B1: Abstract and §IX (per-pixel-null preservation)
MAJOR. Abstract claims shuffle "does NOT destroy global-monopole × canonical-mask-geometry leakage" but §IX details show shuffle destroys per-galaxy correlations while preserving per-pixel counts/edges, implying it DOES destroy some leakage forms—narrative inflates to dodge reviewer by overclaiming "preservation." Fix: Revise abstract to "shuffle destroys per-galaxy depth-CW correlations but preserves global-monopole leakage via per-pixel mask geometry," and clarify in §IX that +1.85σ is this preserved leakage, not primordial.

## PAPER-GRO-B2: §Confidence Stratification (reframe consistency)
minor. HC-spiral 0.3σ reframed as "stability-cross-check" not "primary," but unstratified 0.43σ/-0.122σ/+1.85σ still load-bearing; reframe is consistent but underplays that HC is weaker (0.3σ < 0.43σ), supporting noise over signal—honest but could flag as evidence against overconfidence. Fix: Add sentence noting HC weakening supports noise interpretation, ensuring reframe doesn't hide this.

## PAPER-GRO-B3: Abstract and §VIII.F (hemisphere derivation distinction)
nit. Hemisphere 0.17% half-difference correctly derived as A/2 → A=0.34%, explicitly distinguished from max-over-768-directions 0.853% as different statistic; reads cleanly without contradiction. Fix: None needed; distinction is clear.

## PAPER-GRO-B4: §VI.D and §VIII.F (TTT-spin reconciliation)
MAJOR. §VI.D flags Motloch+2021 as "marginal correlation," §VIII.F reconciles as "systematic-contaminated" but doesn't specify which systematic (e.g., reading-bias); reconciliation is consistent but vague, overclaims resolution without evidence—central claim isn't new if just relabeling prior marginality. Fix: Specify systematic (e.g., "consistent with Iye+2020 reading-direction bias") and cite evidence for contamination dismissal.

## PAPER-GRO-B5: v1.0.64 edits (new BLOCKERs/MAJORs)
minor. No new BLOCKERs/MAJORs introduced; edits close prior issues cleanly (e.g., JSON provenance committed, shuffle language reconciled). Fix: None; endorse as robust.

## PAPER-GRO-B6: Bibliography (metadata audit)
nit. Shamir2022 arXiv ID missing (prior wrong pointer removed); Jia2023 arXiv absent; other fused-arXiv-IDs clean per prior catches. Fix: Verify and add correct arXiv IDs for Shamir2022/Jia2023 if preprints exist, or note "no arXiv" explicitly.
