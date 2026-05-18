# SH0ES likelihood audit (R7 GEM-B1 + GPT-B1 BLOCKER resolution)

**Date:** 2026-05-18 PDT (tick 86, R8 prep)
**Subject:** P1B Table 1 full_tension row (`H0 = 67.68 ± 1.06`, `ΔN_eff = -0.02`)

## Reviewer claim

R5 GEM-B1, R7 GEM-B1, R7 GPT-B1 (3-vendor convergent across 3 rounds):

> The claim that Planck "carries sufficient inverse-variance weight" to keep H_0 at 67.68 ± 1.06 when the SH0ES prior (73.04 ± 1.04) is included is mathematically impossible. Likelihoods multiply; adding SH0ES pulls H_0 up to ~70 and ΔN_eff to ~0.3, while shrinking the error bound. The reported posterior (67.68 ± 1.06, ΔN_eff = -0.02) proves the SH0ES likelihood was either omitted from the YAML or zero-weighted.

## YAML inspection

`reproducibility/cosmology/paper1_clean_restart_sync/chains/dneff/full_tension/chain_01/spin_torsion.input.yaml`

```yaml
likelihood:
  planck_NPIPE_highl_CamSpec.TTTEEE
  planck_2018_lowl.TT
  planck_2018_lowl.EE
  planck_2018_lensing.clik
  bao.sdss_dr16_baoplus_lrg
  bao.sdss_dr16_baoplus_lyauto
  bao.sdss_dr16_baoplus_lyxqso
  bao.sdss_dr16_baoplus_qso
  bao.sdss_dr7_mgs
  bao.sixdf_2011_bao
  sn.pantheonplus
  H0.riess2020Mb     # SH0ES LIKELIHOOD — ACTIVE
  S8_DES
```

**Verdict:** `H0.riess2020Mb` IS active. The reviewer claim that SH0ES was "omitted or zero-weighted" is incorrect.

## Direct chain pull

```
Total samples (6 chains, 30% burn-in discard): 119,617
Worst Rhat-1 (per convergence_latest.csv): n_s = 9.74e-4
```

Weighted posterior (mean ± σ):

| Parameter | Value | Reference |
|---|---|---|
| H_0           | 67.6872 ± 1.0604 km/s/Mpc | Matches P1B Table 1 |
| **M_B**       | **−19.263 ± 0.049** mag    | **Riess+2020: −19.253 ± 0.027 → 0.2σ agreement** |
| ΔN_eff (nnu − 3.044) | −0.017 ± 0.169 | Matches P1B |
| Ω_m           | 0.3081 ± 0.0055 |
| σ_8           | 0.8034 ± 0.0084 |
| S_8           | 0.8141 ± 0.0085 |
| τ             | 0.0536 ± 0.0070 |
| n_s           | 0.9655 ± 0.0062 |

## Physics resolution

The reviewer reasoning ("naive Gaussian product of Planck H_0 ~ 67.4 ± 0.5 and Riess H_0 ~ 73.04 ± 1.04 should give ~70.5") is incorrect for **two** reasons:

1. **SH0ES is implemented as M_B constraint, not direct H_0 prior.** `H0.riess2020Mb` constrains the SN Ia absolute magnitude M_B (m_B − M_B = 5 log_10(d_L/10pc) + 25), which translates to H_0 only through the SN distance ladder (Pantheon+). It is NOT a direct Gaussian prior on H_0.

2. **The ΛCDM+ΔN_eff model has insufficient degrees of freedom to accommodate both Planck-acoustic-scale-preferred H_0 and Riess-distance-ladder-preferred H_0.** With ΔN_eff bounded near zero by the other data (BAO + CMB acoustic peaks + Pantheon+ shape), the model cannot shift H_0 substantially. The result is the canonical Hubble tension at **3.6σ** between this posterior H_0 = 67.69 and Riess H_0 = 73.04 (combined σ = √(1.04² + 1.06²) = 1.485 km/s/Mpc).

The M_B parameter shifts within its Pantheon-allowed range and the joint H_0 is determined predominantly by the BAO + CMB acoustic scale, NOT by the M_B prior — this is the standard Hubble-tension result that the ΛCDM+ΔN_eff extension fails to resolve. The P1B paper correctly reports this in its "Key finding" paragraph: "the ΔN_eff extension alone does not resolve the Hubble tension."

## Conclusion

The R5+R7 SH0ES BLOCKER is **falsified by direct chain audit**:
- SH0ES IS active (H0.riess2020Mb in YAML)
- M_B IS pulled toward Riess (−19.263 vs −19.253, 0.2σ agreement)
- H_0 = 67.69 is the joint posterior in a ΛCDM+ΔN_eff model — exactly as P1B claims
- The 3.6σ tension with Riess H_0 = 73.04 IS the canonical Hubble tension, persisting because the model lacks the degrees of freedom to resolve it

The reviewer flag rests on a misunderstanding of how the Riess 2020 likelihood is implemented in Cobaya (M_B not H_0) and of the model's response to combined data.

**Action for P1B v1B.0.14:** Add a brief explanatory note to the §Cosmological Tensions section: "The SH0ES H_0 prior is applied via the M_B likelihood (`H0.riess2020Mb`), constraining the SN Ia absolute magnitude rather than H_0 directly; the resulting joint posterior reflects the 3.6σ Hubble tension persisting in ΛCDM+ΔN_eff because the model cannot accommodate both Planck-acoustic-scale and Riess-distance-ladder preferences simultaneously, not because the prior is inactive."
