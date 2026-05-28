# P1A R-round — REAL cross-vendor — DeepSeek-V4-Pro confabulation-hunter (reasoning mode)

**Model**: `deepseek/deepseek-v4-pro` (via OpenRouter)
**Reasoning effort**: `high`
**Round**: 2026-05-27_R-ext-maint-v3_P1A_v1A_0_35
**Wall time**: 175.0s
**Persona focus**: Paranoid about numbers without traceable sources. For every load-bearing scalar in the abstract and conclusions, ask: is there a JSON/script/dataset on disk that produces this number? Flag headline figures with no provenance and arithmetic that can't be reproduced from displayed values.

---

**Tokens**: prompt=28506, completion=5991, reasoning=4944, total=34497

---

## PAPER-DEE-B1 | Section: Abstract, l. 1–8, l. 12–17 | BLOCKER
**Issue:** The abstract and conclusions lean heavily on the claim that SPHEREx will test $\fnl=-35/8$ at “$3$–$5\sigma$ realistic significance”, yet no Fisher-forecast script, data file, or even a summary table is provided in this paper or its linked repository. The figure is attributed to a separate companion (Paper II) that is not part of this submission.  
**Fix:** Either (a) include a minimal self-contained forecast (e.g., a Jupyter notebook in the reproducibility repository) that reproduces the $3$–$5\sigma$ range from the stated inputs, or (b) downgrade the statement to “Paper II forecasts a detection significance in the range 3–5σ (details therein)” and remove the number from the headline claims.

## PAPER-DEE-B2 | Section: Abstract (H₀, ΔNeff), §Conclusions (H₀, σ₈, Ωₘ) | MAJOR
**Issue:** The cosmological parameter values $H_0=67.68\pm 1.06$, $\Delta\Neff\approx 0$, $\sigma_8=0.803\pm 0.008$, $\Omega_m=0.308\pm 0.005$ appear in the abstract and conclusions as headline results, yet their entire provenance is a companion MCMC paper (Paper I(b)). The linked reproducibility repository (Cobaya YAML configs) does not contain the chains, posterior samples, or convergence diagnostics needed to recalculate those numbers independently.  
**Fix:** Publish the MCMC chains and summary statistics alongside the paper, or restrict the abstract to qualitative statements (“recovers ΛCDM parameters consistent with Planck 2018”) and move the numerical values to the companion where they are directly verified.

## PAPER-DEE-M1 | §IV.D Route 4, §13 (Surviving tests), §14 (Conclusions) – β ≈ 0.27° | minor
**Issue:** The spectator-ALP birefringence central value $\beta\approx 0.27^\circ$ is quoted as a “prediction” or consistency check, but it was obtained from an ALP parameter fit described only in Paper I(b). No fitting code, chains, or parameter file is present in this paper’s materials.  
**Fix:** Either (a) place the fitting pipeline and output in the repository and reference it explicitly, or (b) label the number as “derived in Paper I(b) and reported here for completeness” and stop calling it a prediction of this work.

## PAPER-DEE-M2 | §2.2 (bounce), §12.1 – Ntot ≈ 92 as a “fitted parameter” | minor
**Issue:** The paper states that $N_{\rm tot}\approx 92$ is “a fitted parameter, not predicted” (l. 343–344) but no fitting procedure or likelihood is documented anywhere in this paper or its materials. The number is actually an algebraic consequence of $\Xi\approx 10^{-123}$ and the dilution prefactor—no data fitting is performed.  
**Fix:** Reword to “$N_{\rm tot}\approx 92$ is the order‑of‑magnitude e‑fold count required by the dilution ansatz (Eq. (18)), derived from the observed $\rho_\Lambda$; it is not a free parameter fitted to data.”

## PAPER-DEE-m1 | §10.6 Discrimination table, §13 (Surviving tests) – γ_PTA = 2.567 ± 0.382 | minor
**Issue:** The real‑KDE PTA spectral index $\gamma = 2.567\pm 0.382$ is presented as a result of this programme, yet the underlying GPU‑MCMC analysis and data are hosted in Companion Paper III; the number is not reproducible from the current repository.  
**Fix:** Add the real‑KDE chain and covariance matrix to the reproducibility package, or explicitly state that the number is a cross‑reference from Paper III and not verified within this manuscript.

## PAPER-DEE-n1 | §V (Galaxy spin null) and §VI (Systematics) – ViT‑Small classifier result | nit
**Issue:** The “confirmed null at the dipole level” and the refutation of Shamir’s 3% asymmetry are described qualitatively; any quantitative dipole significance, CW/CCW fractions, and classifier accuracy are deferred to Paper IV. The paper’s own repository includes the galaxy‑spin pipeline code, but no output metrics file or summary table is present to directly verify the null statement.  
**Fix:** Add a small CSV or JSON file with the dipole significance, CW‑fraction monopole, and classifier validation accuracy to the repository, so the null claim can be traced to a specific dataset.
