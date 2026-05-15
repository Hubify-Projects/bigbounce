# P4_v1078_R3 R-round — REAL cross-vendor — GPT-5 methodology reviewer

**Model**: `openai/gpt-5.5` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-15_1645pt
**Wall time**: 114.5s
**Persona focus**: Methodology rigor: derivations, dimensional analysis, statistical-method scrutiny, internal arithmetic consistency. Flag overclaim of statistical significance. Check that error bars propagate correctly through the systematic budget. Audit any 'Bayes factor' / 'likelihood ratio' framing for proper marginalization vs parameter-shift.

---

**Tokens**: prompt=71878, completion=7312, reasoning=6214, total=79190

---

## PAPER-GPT-B1 — BLOCKER — Title / Abstract ¶3 / Sec. `prereg` / Sec. `sensitivity` / Table `mc_injection` / Conclusions

Concrete issue: The sensitivity headline is internally inconsistent. Title says `|A_dipole| < 0.5%`; abstract says the sweep never crosses 50% recovery up to 2%; Sec. `prereg` says first 50%-recovery-at-3σ threshold is `A=0.75%`; Sec. `sensitivity` still shows only the stale five-amplitude sweep through `0.5%` and concludes only `>0.5%`.

Fix: Replace the title/abstract/conclusions with “systematic-inclusive 50%-recovery 3σ threshold `A≈0.75%`” or “sub-percent sensitivity”; remove any `<0.5%` upper-limit language. Insert the nine-amplitude table with `P(σ>3)` and retire the stale five-amplitude table.

## PAPER-GPT-B2 — BLOCKER — Table `headline_summary` / Sec. `dipole` / Table `face_on` / Sec. `hemisphere`

Concrete issue: The headline estimator bookkeeping is not self-consistent. The “primary” real-space dipole is quoted as `+0.43σ, p=0.30`, but Table `face_on` reports “Catalog C full” as `+4.31σ, p=0.001`; hemisphere LEE is also described both as `<1σ post-LEE` and as direct-MC `p_LEE≤10^-4`.

Fix: Make one reconciliation table with estimator, mask, map, weighting, null, MC count, and data vector for every quoted sigma. Do not call a statistic “consistent with null” under a null that the direct max-statistic MC rejects.

## PAPER-GPT-B3 — BLOCKER — Abstract / Table `monopole_mask_null` / Sec. `monopole_mask_null` / Conclusions first paragraph

Concrete issue: The central 99.3% monopole-mask reproduction claim has broken arithmetic and stale prose. Table gives `(1.685±0.068)×10^-2`, which implies `z≈0.16`, not `+1.69`; text elsewhere uses `±6.8×10^-5`; Conclusions still say “reproduces ~30%” and “controversy is resolved.”

Fix: Correct the uncertainty notation to the value that actually yields `z=+1.69`, update all stale 30% text to 99.3%, and explicitly document why the N=25 smoke observed value `4.23×10^-2` became `1.696×10^-2`. Remove “resolves prior claims”; say “demonstrates this-pipeline leakage channel.”

## PAPER-GPT-M4 — MAJOR — Sec. `dipole` / Table `multipole` / Sec. `namaster_config`

Concrete issue: The low-ℓ MASTER treatment is not methodologically closed. The leakage is explicitly ℓ=0 monopole → ℓ=1 mask coupling, but the analysis alternates between unmonopole-subtracted maps, `f_CW-0.5` maps, single-mode ℓ=1, and bandpowers where `ℓ_eff=4` spans `[2,6]`; null means and units are not consistently reported.

Fix: Re-run with a single declared data vector: subtract or marginalize the global monopole, include ℓ=0 in the mode-coupling treatment or justify its exclusion, use one mask/apodization for the headline, and report data/null mean/std/units for every bandpower. Do not describe `[2,6]` as an ℓ=1 estimator.

## PAPER-GPT-M5 — MAJOR — Sec. `tta` / Sec. `systematic_dipole`

Concrete issue: The TTA guarantee is overstated. Eq. `(tta)` enforces flip covariance of the output protocol; it does not force `p_CW^eq=p_CCW^eq`, does not make the soft chirality score zero per galaxy, and does not eliminate classifier bias “by construction” or “to machine precision.”

Fix: Replace all “eliminates bias by construction” language with “enforces flip equivariance and empirically suppresses the large-scale mode.” Treat the residual monopole and argmax label asymmetry as nuisance systematics, not as contradictions-free byproducts of TTA.

## PAPER-GPT-m6 — minor — Bibliography / Data Availability

Concrete issue: Bibliography/provenance is not clean. `Shamir:2022DESI` lacks final journal volume/page/DOI despite saying it is published; several manual bibliography entries appear uncited/irrelevant; Data Availability still refers to `paper4-v1.0` / “until the tag is cut” while the round context says `paper4-v1.0.78` is already released.

Fix: Pin the exact `paper4-v1.0.78` release/commit/DOI everywhere, complete Shamir DESI metadata, remove uncited companion/theory refs not used in the text, and keep the corrected Jia metadata.
