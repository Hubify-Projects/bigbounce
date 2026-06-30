# Compute-to-ACCEPT queue (the real research that drives external ACCEPT)

<!-- last_updated: 2026-06-30 -->

The drive-to-ACCEPT round (2026-06-30, v*.91/.86/.82/.122/.200/.96) restructured
each paper around the reviewers' actual asks. But several reviewer demands
**cannot be satisfied by text edits — they require running new science**. This
is the honest path to full external ACCEPT. Each item below was flagged by the
paper-owner agents as compute-gated (not faked, not dismissed). Run on the pod;
fold real results into the paper; re-review.

## P1B (MCMC companion) — HIGHEST LEVERAGE (recurring blocker, 4/6 reviewers)
- [ ] **SN-overlap control chain A**: DESI + Planck + Pantheon+-only w0wa MCMC (drop the overlapping DES-Y5×Pantheon+ SNe). Demonstrates the quintom-B direction is/ isn't robust to double-counted SNe.
- [ ] **SN-overlap control chain B**: DESI + Planck + DES-SN5YR-only w0wa MCMC.
- [ ] **ALP prior-predictive fraction**: quantify the accommodation/prior-volume cost (the "tautological fit" ChatGPT-B2 concern) — fraction of prior that reproduces β_obs.

## P4 (chirality null) — win ChatGPT's MAJOR
- [ ] **GZ1-only classifier retrain**: retrain the flip-equivariant ViT on GZ1 labels only (no CE-ResNet pseudo-labels) → confirms the null isn't inherited from CE-ResNet. (ChatGPT M2.)
- [ ] **Empirical b/a (axis-ratio) cross-match**: test the edge-on directional-bias-exclusion argument empirically, not just analytically. (Gemini MAJOR.)
- [ ] **≥200-random-axis harmonic injection battery**: full look-elsewhere null for the harmonic channel. (OpenAI-INT M5.)

## P3 (anomaly catalog) — 3/3 MAJOR, needs reproducibility artifacts
- [ ] **Independent 6-way dedup artifact**: produce + commit the actual dedup table (OpenAI E1's "most critical").
- [ ] **Held-out re-score of DESI/Planck top-lists**: out-of-sample validation (E2/E6 option-a).
- [ ] **Native SDSS score histogram** (Grok M2) + **marginal-α posterior fold-in** (Grok M3).

## P2 (f_NL recast) — deepest, lowest-priority (recast is honest as-is)
- [ ] **Cubic in-in transfer through an explicit bounce** (the assumption-(d) uncertainty).
- [ ] **Heinrich Fisher re-run at the bounce fiducial** with the non-local template.
- [ ] **Joint bispectrum Fisher over systematics**.

## P1A (ECH theory) — mostly text; one optional calc
- [ ] **Boltzmann Γ_wash(T) washout calculation** (currently stated conditionally) — optional; the closure margin is ansatz-insensitive without it.

## P5 (DESI chirality) — NO compute needed
The Paper-IV self-containment appendix (v0.1.96) closed the one convergent
blocker from source numbers. P5 is the closest to 3/3 ACCEPT — re-review should
tell. If ChatGPT's MAJOR persists, read its NEW report for the residual.

---
**Protocol:** run these on RunPod (see `/runpod-lifecycle` + `/houston-method-v2`);
ALWAYS-backup results to local+HF+B2 (Lesson E); fold real numbers into the .tex;
NEVER fabricate a result to satisfy a reviewer. Mint Zenodo DOIs at submission
(the deferred-DOI flags are submission-time, not blockers).
