# P1B_v1B07 R-round — REAL cross-vendor — Gemini-3.1-Pro cosmology-physics reviewer

**Model**: `google/gemini-3.1-pro-preview` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-17_0200pt_P1B_v1B07_R3_R-round_real
**Wall time**: 46.7s
**Persona focus**: Theoretical physics: gauge-frame vs physical-frame distinctions, GR projection effects, model-class scope boundaries, EFT counting, consistency-relation applicability. Flag any 'mechanism-independent' claim that overstates UV-completion independence. Check parity-violation / ALP / Chern-Simons references against standard reviews.

---

**Tokens**: prompt=13508, completion=6316, reasoning=5240, total=19824

---

## Finding 1: BLOCKER - Zombie Model-Comparison Statistics in Conclusion
**Location:** Section 5.2 vs Section 8 (Conclusions)
**Issue:** Section 5.2 explicitly states that the $\chi^2_{\rm eff}$/AIC/BIC/$\ln B$ block was removed entirely from v1B.0.7 due to a 3-vendor convergent R2 BLOCKER regarding irreproducibility. However, Section 8 still prominently quotes these exact removed numbers ("The Savage-Dickey indicative figure $\ln B = +4.8$... AIC/BIC differences ($\Delta$AIC$=-5.9$, $\Delta$BIC$=-0.7$) are the primary cross-references"). This is a critical abstract/body/conclusion contradiction and a failed R2 remediation.
**Fix:** Delete the zombie model-comparison statistics from the Conclusions section to align with the explicit removal in Section 5.2.

## Finding 2: MAJOR - Parameter Counting Contradiction (14 vs 7 vs Nuisance)
**Location:** Section 5.1 and Table 1 (Footnote 2)
**Issue:** Section 5.1 claims the model is $\Lambda$CDM + $\Delta N_{\rm eff}$ with $k=7$ sampled parameters. However, Footnote 2 claims "all 14 sampled parameters across both frozen combinations satisfy $\hat{R}-1 < 3\times 10^{-3}$". If the 14 parameters include Planck nuisance parameters, 7 nuisance parameters is far too few for the Planck NPIPE CamSpec TTTEEE likelihood (which requires ~16+). If "14" refers to cosmological parameters, it contradicts $k=7$. 
**Fix:** Explicitly list the sampled nuisance parameters to justify the "14" count, or correct the number if it is a typo. Ensure the $k=7$ claim in Sec 5.1 explicitly refers to *cosmological* parameters only.

## Finding 3: MAJOR - Unphysical NaMaster Pipeline Noise Injection
**Location:** Section 4 (Foreground and noise model)
**Issue:** The text states the pipeline rotates the "Planck Commander $Q$/$U$ maps" by $e^{2i\beta}$ and then adds "ACT-noise level $\Delta_P=10\,\mu\text{K}\cdot\text{arcmin}$" to achieve a recovery SNR of 20.32. The Commander map already contains intrinsic Planck noise ($\sim 40\,\mu\text{K}\cdot\text{arcmin}$). Rotating a noisy map and adding *more* noise cannot yield an SNR of 20.32 (which requires a nearly noiseless base map). The pipeline must be rotating a noiseless *theory* realization, not the actual Commander map.
**Fix:** Clarify whether the MC realizations rotate a noiseless simulated CMB map or the actual Commander map. If the latter, correct the SNR calculation, as the intrinsic map noise strictly bounds the maximum achievable SNR.

## Finding 4: minor - Missing MCMC Diagnostics
**Location:** Table 1
**Issue:** While $\hat{R}-1$ and Min ESS are reported, the acceptance rate and autocorrelation length are missing. These are standard PRD/MNRAS requirements for MCMC transparency, especially for chains described elsewhere in the text as "slow-mixing".
**Fix:** Add the mean acceptance fraction and maximum autocorrelation length for the frozen chains to Table 1.

## Finding 5: minor - Stale DESI DR2 Snapshot vs Live State
**Location:** Table 3 and Section 7.1
**Issue:** The paper explicitly timestamps the DESI DR2 chain at a frozen snapshot of $N=59,832$ (2026-05-14). While technically compliant with a snapshot declaration, the live pod (`ijzftpy3klystt`) is already at $N=101,979$ with $\hat{R}-1=0.01176$. The snapshot is unnecessarily stale and underrepresents the current convergence state.
**Fix:** Update Table 3 and Section 7.1/8 to reflect the current $N=101,979$ state, as it is much closer to the $<0.01$ convergence target and provides a more accurate status for the P1A companion cross-reference.

## Finding 6: minor - ALP MCMC Likelihood Unspecified
**Location:** Section 6 (MCMC parameter estimation)
**Issue:** The text mentions "Dedicated MCMC sampling of the ALP parameter space... yields: $\beta_{\rm ALP} = 0.336^\circ\pm 0.107^\circ$". It is entirely unclear what likelihood or dataset this MCMC is evaluating. Is it fitting to the published $\beta$ summary statistics, or to raw CMB polarization spectra? 
**Fix:** Explicitly state the likelihood and dataset used for the "ALP parameter space" MCMC in Section 6.
