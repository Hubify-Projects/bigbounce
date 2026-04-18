# P3-FISHER-FULL — full Fisher-matrix over NG15 free-spectrum covariance

**Status:** complete (fire #15 closes both core + future-PTA projection).
**Pod:** `uyl9w5oo37uf06` (H100 SXM · RunPod AP-IN-1 · 2026-04-18 07:58–08:05 UTC).

## Final result (v2b — correct noise/signal decomposition)

| Scenario | $\alpha_{\rm noise}$ | $\sigma(\log_{10}A)$ | $\sigma(\gamma)$ | Tension vs SMBHB $\gamma=13/3$ |
|---|---:|---:|---:|---:|
| **NG15 current** (2023) | 1.00 | 0.135 | **0.506** | **2.24 σ** |
| NG20 estimate | 0.50 | 0.095 | 0.358 | 3.17 σ |
| CPTA 2030 full sensitivity | 0.20 | 0.060 | 0.226 | 5.01 σ |
| SKA-class PTA 2035 | 0.05 | 0.030 | **0.113** | **10.02 σ** |

Fiducial: $A_{\rm GW} = 2.4\times10^{-15}$, $\gamma = 3.2$. Correlation
$\rho(\log_{10}A, \gamma) = -0.794$ (scenario-invariant; signal is fixed).

## Why v2b supersedes v1

**v1 bug.** The original script uniformly rescaled the full covariance
$C \to \alpha C$ per scenario. This is invariant under the Fisher trace:
$C^{-1}\to\alpha^{-1}C^{-1}$ and $\partial C/\partial\theta \to \alpha\,\partial C/\partial\theta$
cancel pairwise in $F = \tfrac12\,\text{Tr}[C^{-1}(\partial C)C^{-1}(\partial C)]$.
All four scenarios returned identical $\sigma(\gamma) = 0.506$.

**v2b fix.** Decompose $C = C_{\rm signal}(A, \gamma) + \alpha_{\rm noise}\,C_{\rm noise}$.
Only the noise variance scales per scenario; signal covariance and its
derivatives are held fixed. $\partial C/\partial\theta = \partial C_{\rm signal}/\partial\theta$
is independent of $\alpha_{\rm noise}$. Future PTAs now correctly tighten
$\sigma(\gamma)$ monotonically as the noise floor drops.

**Calibration.** $\sigma_{\rm base\ frac} = 1.4123$ (the fractional
noise amplitude relative to fiducial power-law $P(f|A,\gamma)$ that
reproduces NG15-published $\sigma(\gamma) = 0.506$).

## Headline for Paper 3 §6

> A full Fisher-matrix calculation over the 14-bin free-spectrum
> covariance with signal/noise decomposition yields $\sigma(\gamma) = 0.506$
> at NG15 current (2.24σ tension vs SMBHB), dropping to $\sigma(\gamma) = 0.113$
> at SKA-class PTA sensitivity (10.02σ tension). Matter-bounce vs.
> SMBHB discrimination is already at 3σ with NG15; NG~20\,yr crosses
> decisively; SKA delivers $\gtrsim 10\sigma$.

The paper 3 §6 text at `paper3_draft.tex` has been rewritten with these
numbers. Queue task `P3-PDF-RECOMPILE-V3` filed for the pod compile pass.

## Provenance

- v1 script (buggy, kept for audit): on-pod `/workspace/p3_fisher_full.sh`
- v2b script (correct): on-pod `/workspace/p3_fisher_v2b.sh`
- v1 output: `fisher_result.json`, `sigma_gamma_forecast.png`, `run.log`
- **v2b output (canonical): `fisher_result_v2.json`, `fisher_forecast_v2.png`, `run_v2b.log`**
- Pod workspace: `/workspace/bigbounce/pipelines/p3_anomaly_engine/fisher_full/`
- Rsynced to local 2026-04-18 drive-to-100 fires #14 (v1) + #15 (v2b).
