# EXT11 Harvest — P1B — ChatGPT

- Provider: ChatGPT
- Model/Effort: Pro Extended
- Chat URL: https://chatgpt.com/g/g-p-6881c7f354808191a36860ff4d29fa69-big-bounce-book/c/6a2dc5cf-db00-83e8-b824-21b626a0d9ab
- PDF md5: 03c33444 (paper1b_mcmc_companion_v1B.0.70_03c33444.pdf)
- Harvested: 2026-06-13 17:14 PDT

---

## Headline Verdict: MINOR REVISIONS (very close to ACCEPT)

The scientific closures are substantially successful. The remaining issues do not require new chains, new NaMaster runs, new ALP sampling, or major scientific rework. They are narrow text-consistency fixes in the reproducibility/scoping language. Would move to ACCEPT once the remaining one-sentence likelihood-stack contradiction is corrected.

## EXT10 Items Status

- **Likelihood-stack wording:** Mostly closed, one text inconsistency remains (see New Item 1 below).
- **ALP m~H₀ conclusion:** Closed. Conclusion now states median m ≃ 40.5H₀ in the Ω_a < 0.01 subset.
- **Spectator-status operational cut:** Closed. Text now says Ω_a < 0.01, 13% posterior mass.
- **w₀w_a / phantom-crossing caveat:** Closed for publication standards. One remaining "requires" could become "indicates within this product-likelihood posterior."
- **NaMaster "systematic floor" language:** Open only as polish. Replace remaining "NaMaster systematic floor" with "NaMaster pipeline-recovery bias floor."
- **Unweighted-estimator explanation:** Closed.
- **Data/code version pinning:** Closed for review; insert DOI/tag at final submission.

## New Items Introduced by Closures

### New Item 1 — Release-pairing note contradicts the c15 likelihood names (MINOR, required fix)

Sec. V.B first says the c15 low-ℓ EE and lensing likelihood names are `planck_2020_lollipop.lowlE` and `planckpr4lensing`, differing from the frozen names. The following release-pairing note then says both the primary frozen chains and the c15 verification chain use "Planck 2018 low-ℓ TT/EE and Planck 2018 lensing." This is a contradiction.

**Fix:** Change the release-pairing note to:
> "The primary frozen chains use Planck NPIPE/PR4 CamSpec high-ℓ TTTEEE paired with Planck 2018 low-ℓ TT/EE and Planck 2018 lensing. The c15 verification chain preserves the same high-ℓ CamSpec and SDSS BAO blocks but uses planck_2020_lollipop.lowlE and planckpr4lensing; it is therefore a release-pairing robustness rerun, not an identical-likelihood rerun. A fully PR4-consistent low-ℓ/lensing swap test has not been run."

### New Item 2 — Internal closure labels in journal prose (polish only)

Text contains labels such as "Release-pairing note (E3/E4)" and "H₀ note (E8)." Remove the parenthetical audit IDs and keep the scientific sentence.

### New Item 3 — Minor redundancy in the ALP conclusion (polish only)

"Within the Ω_a < 0.01 spectator-safe subset (13% of the posterior mass; median m ≃ 40.5H₀, Ω_a < 0.01)…" — the repeated Ω_a < 0.01 is redundant.

## Final Verdict

MINOR REVISIONS. Only one required fix (release-pairing note text contradiction). Everything else is copy-edit polish. Would recommend ACCEPT after that single sentence correction.
