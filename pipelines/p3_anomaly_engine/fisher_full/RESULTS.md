# P3-FISHER-FULL — full Fisher-matrix over NG15 free-spectrum covariance

**Status:** core result landed, future-PTA scaling flagged for rework.
**Pod:** `uyl9w5oo37uf06` (H100 SXM · RunPod AP-IN-1 · 2026-04-18 07:58 UTC).

## Core NG15-current result (ready for Paper 3 §6)

| Quantity | Value |
|---|---|
| Fiducial $A_{\rm GW}$ | $2.4\times10^{-15}$ |
| Fiducial $\gamma$ | 3.2 |
| $\sigma(\log_{10} A)$ | 0.135 |
| $\sigma(\gamma)$ | **0.506** |
| $\rho(\log_{10} A, \gamma)$ | $-0.794$ |
| Tension vs SMBHB $\gamma=13/3$ | **2.24 σ** |

Built from a full 14-bin free-spectrum covariance with off-diagonal
leakage terms, replacing the scaling-only forecast in
`fisher_forecast_gamma_future_ptas.md`. The NG15-current column of that
note now has a proper covariance-level derivation, not a handwaved
$1/\sqrt{T}$ rescaling.

## Known issue — future-PTA scaling panel

The run also reported identical $\sigma(\gamma)=0.506$ for NG20,
CPTA_2030, and SKA_PTA_2035. That is wrong, and the failure mode is a
genuine bug in the run script, not a physical result:

The implementation uniformly rescaled the full covariance matrix $C$ by
a `cov_scale` factor for each future scenario. But
$F_{\theta\theta'} = \tfrac12\,\text{Tr}\!\left[C^{-1}\frac{\partial C}{\partial\theta}\,C^{-1}\frac{\partial C}{\partial\theta'}\right]$
is invariant under $C\to\alpha C$ because
$C^{-1}\to\alpha^{-1}C^{-1}$ and $\partial C/\partial\theta\to\alpha\,\partial C/\partial\theta$
cancel pairwise. Hence every scenario reported the same $\sigma(\gamma)$.

**Correct future-PTA scaling** decomposes $C = C_{\rm signal}(A,\gamma) + C_{\rm noise}$
and scales only $C_{\rm noise}$ by the projected white-noise / cadence
improvement factor. $\partial C/\partial\theta = \partial C_{\rm signal}/\partial\theta$
is invariant; the signal remains the same, only the noise floor drops.

Follow-up `P3-FISHER-FULL-FIX` filed in `queue.md`. Intended rerun on
the same pod, same script, with `build_covariance(..., scale_noise=α, scale_signal=1.0)`.

## Provenance

- Script: on-pod `/workspace/fisher.py` (not yet committed; will be
  committed after the scaling fix lands)
- Output: `fisher_result.json`, `sigma_gamma_forecast.png`, `run.log`
- Pod workspace: `/workspace/bigbounce/pipelines/p3_anomaly_engine/fisher_full/`
- Rsynced to local 2026-04-18 drive-to-100 fire #14.
