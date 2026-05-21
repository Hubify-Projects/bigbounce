# paper1b R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-21_R24_P1B_v1B_0_20
**Wall time**: 127.6s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=19929, completion=14824, reasoning=13970, total=34753

---

0 BLOCKERs found. The theoretical physics boundaries are well-respected, the MCMC interpretations (especially the $M_B$ offset explanation of the Hubble tension) are physically sound, and the NaMaster scope is properly restricted. The findings below are primarily version-control artifacts and one mangled paragraph.

## PAPER-GEM-M1 (MAJOR): Unsynchronized Dataset Configuration
* **Section:** 5.1 (Datasets and Configuration) vs Table 2
* **Issue:** Section 5.1 explicitly lists four dataset combinations using "DESI 2024 DR1 BAO" and no DES-Y5 SN. However, Table 2 reports the converged iter2 chain using "DESI DR2 BAO" and "DES-Y5". The methodology section completely fails to document the likelihood stack used for the paper's headline $w_0 w_a$ result.
* **Fix:** Update Section 5.1 to explicitly include the iter2 likelihood stack (DESI DR2 + DES-Y5 + Pantheon+ + Planck).

## PAPER-GEM-M2 (MAJOR): Mangled ALP MCMC Text and Missing Appendix Content
* **Section:** 6 (Cosmic Birefringence: Spectator ALP Consistency Check)
* **Issue:** The text describing $\beta_{\rm free}$ is a contradictory copy-paste error: it claims "configurations $C_{a\gamma}=4,8,12$ ... with $\beta$ as a free parameter". If $\beta$ is a free parameter in a model-independent fit, it does not depend on $C_{a\gamma}$. Furthermore, it cites Appendix A for "full priors and dataset details", but Appendix A contains no such details.
* **Fix:** Separate the description of the model-independent free-$\beta$ fit from the ALP-parameter ($m, \theta_i$) fits where $C_{a\gamma}$ is fixed and $\beta$ is derived. Add the missing priors to Appendix A or remove the pointer.

## PAPER-GEM-m1 (minor): Stale Version Number in Table 3
* **Section:** 7 (Cross-Paper Verification Status), Table 3
* **Issue:** The document header defines the version as `v1B.0.20`, but Table 3 lists the P1(b) readiness version as `v1B.0.13`. 
* **Fix:** Update the P1(b) row in Table 3 to reflect the current `v1B.0.20` version.

## PAPER-GEM-m2 (minor): Stale Version Number in Caveats
* **Section:** 3 (Caveats paragraph)
* **Issue:** The text reads "The robust Bayesian evidence / Bayes factor $\ln B$ against LCDM is NOT reported in this v1B.0.14", but the current document is v1B.0.20.
* **Fix:** Change "v1B.0.14" to "v1B.0.20" (or "the current version").

## PAPER-GEM-n1 (nit): Riess 2020 vs 2021/2022 Nomenclature
* **Section:** 3 (Caveats paragraph)
* **Issue:** The text refers to $M_B = -19.253 \pm 0.027$ mag as the "Riess+2020 SH0ES value". While the Cobaya likelihood alias might be `H0.riess2020Mb`, the physical value $-19.253 \pm 0.027$ is the baseline result from the Riess et al. 2021 (published 2022) paper, not the 2020 paper.
* **Fix:** Change "Riess+2020 SH0ES value" to "Riess+2021/2022 SH0ES value".
