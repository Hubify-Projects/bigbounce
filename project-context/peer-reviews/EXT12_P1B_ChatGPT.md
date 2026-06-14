# EXT12 Harvest — P1B — ChatGPT Pro Extended

- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5cf-db00-83e8-b824-21b626a0d9ab
- PDF md5: aa1a694e (paper1b_mcmc_companion_v1B.0.71.pdf)
- Submitted: ~17:23 PDT 2026-06-13
- Harvested: 2026-06-13 18:39 PDT
- EXT11 baseline: MINOR REVISIONS
- EXT12 verdict: **MINOR REVISIONS**

## Headline Verdict

Recommendation: MINOR REVISIONS — borderline ACCEPT after one final consistency pass.

## ChatGPT EXT12 Summary

"The scientific content is ready. I see no blockers and no need for new MCMC, NaMaster, or ALP
computations. The EXT11 closures were mostly successful: the ALP m≃40.5H_0 spectator-safe
wording is now correct, the internal audit labels are removed, v1B.0.71 is now reflected in
the data/reproducibility material, and the c15 rerun is now described much more accurately as
a release-pairing robustness rerun rather than an identical-likelihood rerun."

## Remaining Open Item (1 item)

**Release-pairing status is fixed locally in Sec. V.B, but still inconsistent globally.**

The fix correctly describes c15 in Sec. V.B but:
- Sec. III still says no release-pairing swap test has been run (too strong given c15)
- Conclusion still says ΔN_eff result lacks a release-consistency control run (too strong)
- "Caveat (e), Sec. III" cross-reference points to wrong caveat (DES-SN5YR, not Planck pairing)

Proposed fix (ChatGPT): "The primary frozen chains use Planck NPIPE/PR4 CamSpec high-ℓ TTTEEE
paired with Planck 2018 low-ℓ TT/EE and Planck 2018 lensing. We have not run a full
all-component release-pairing swap at frozen-chain depth. However, the c15 robustness rerun
replaces the low-ℓ EE and lensing components with planck_2020_lollipop.lowlE and planckpr4lensing,
while preserving the high-ℓ CamSpec and SDSS BAO blocks, and reproduces ΔN_eff at 0.04σ. Thus
the tested low-ℓ EE/lensing pairing mode is empirically small at the quoted precision; any
untested full-release-pairing bias remains outside the scope of this companion."

This is a text-only fix across 3 locations: Sec. III, Sec. V.B harmonization, and Conclusion.

## New Items Introduced by EXT12

3 new items introduced (all minor/editorial):
1. "caveat (e), Sec. III" cross-reference error (points to wrong caveat)
2. c15 described as "PR4-consistent low-ℓ/lensing" vs actual partial substitution
3. Commit/tag metadata check at final submission (not a review blocker)

## EXT13 Closure Effort

~20 min: harmonize release-pairing language across Sec. III + Sec. V.B + Conclusion +
fix cross-reference. High confidence ChatGPT → ACCEPT in EXT13.
