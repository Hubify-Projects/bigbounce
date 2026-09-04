"""
A3-M audit item DA3M-R5-15 -- the model's OWN FIRST-ORDER (primordial) tensor
background Omega_GW^(1) h^2 in the NANOGrav band, to be reported beside the
second-order (scalar-induced) background of
`sigw_nhz_from_lab_spectrum_2026_09_04.py`.

Question (R5 truth audit, item DA3M-R5-15): Channel I compares only the
scalar-INDUCED background, while Table II's gamma = 5 row is labelled
"prim. tensors".  The model's own first-order tensor amplitude at nHz is never
stated.  Which of the two dominates, and does the PTA null change?

Method
  (1) Primordial tensor spectrum on the same background:
          P_T(k) = r A_s (k/k_*)^{n_T},   A_s = 2.1e-9, k_* = 0.05 Mpc^-1
      TWO CASES are reported, because the matter-bounce tensor-to-scalar ratio
      is an OPEN item in this program (A3-4, the r = 0.84 re-derivation):
        CASE A (adopted, conservative): the CMB observational bound
          r < 0.036 at k_* (BICEP/Keck + Planck, Ade et al. 2021,
          PRL 127, 151301, arXiv:2110.00483) -- an UPPER LIMIT, so the
          resulting Omega_GW^(1) is an upper limit.
        CASE B (scenario, not adopted): r = 0.84, the matter-bounce value of
          Cai et al. 2009 quoted in this program's A3-4 as an open
          re-derivation.  Reported only to bracket the scenario; it is already
          excluded at k_* by CASE A's bound.
      Tensor tilt from the SAME near-dust background as the scalar spectrum:
          n_T = n_s - 1 = -0.0351 (Planck-anchored branch), and n_T = 0
          (pure-dust bracket; the paper's own "prim. tensors, n_T = 0,
          Omega_GW ~ f^0" convention at main.tex :550, :569, Table II).
  (2) f <-> k for a mode re-entering the horizon in radiation domination,
      identical convention to the companion SIGW script:
          k [Mpc^-1] = 2 pi f * Mpc_km / c_km_s.
  (3) Standard radiation-era propagation of a first-order tensor mode
      (Watanabe & Komatsu 2006, PRD 73, 123515, arXiv:astro-ph/0604176;
       Caprini & Figueroa 2018 review, arXiv:1801.04268, Sec. 2):
      deep inside the horizon in RD the oscillation-averaged energy density is
          Omega_GW(k) = P_T(k) / 24        (at production),
      redshifted to today with the SAME transfer prefactor the companion script
      uses for the induced background:
          Omega_GW,0 h^2 = 1.62e-5 * (g_*/106.75)^{-1/3} * Omega_GW(production).
      Baseline g_* = 106.75 (identical to the companion script, so the two
      channels are compared on one convention); the g_*(T ~ 0.2 GeV) ~ 20
      variant appropriate to nHz horizon entry is reported as a sensitivity.
  (4) Comparison targets: the committed induced amplitude
      Omega_GW h^2(f_yr) = 1.4545e-23 (Planck-anchored) / 5.8764e-23 (dust),
      and the NANOGrav 15-yr HD power law, Omega_GW h^2(f_yr) = 3.6235e-9.

INTEGRITY: no free parameter is tuned.  r is taken from a published CMB upper
bound (CASE A) or from the program's own open literature value (CASE B, clearly
labelled a scenario).  The propagation constant is the same one already
validated in the companion script against a published benchmark.

Venue: local (Apple silicon), CPU only, seconds, cost $0.
Output: outputs/r5_15_tensor_omega_nhz.json
"""
from __future__ import annotations
import json, time
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
OUTJ = HERE / "outputs/r5_15_tensor_omega_nhz.json"

C_KMS = 299792.458
MPC_KM = 3.0856775814913673e19
K_PER_HZ = 2.0 * np.pi * MPC_KM / C_KMS
OM_R0_H2_FACTOR = 1.62e-5
A_S, K_STAR = 2.1e-9, 0.05
F_YR = 1.0 / (365.25 * 24 * 3600)
F_LO, F_HI = 2e-9, 60e-9
NG_OM_H2_FYR = 3.6234654615493524e-09       # committed, sigw_...json
INDUCED = {"MB_anchored_ns0.9649": 1.454451049684014e-23,
           "pure_dust_ns1": 5.876402212251419e-23}
R_CASES = {"A_CMB_bound_r0.036": 0.036, "B_scenario_matter_bounce_r0.84": 0.84}
NT_CASES = {"MB_anchored_ns0.9649": 0.9649 - 1.0, "pure_dust_ns1": 0.0}

def p_T(k, r, nT):
    return r * A_S * (np.asarray(k, float) / K_STAR) ** nT

def omega_today_h2(om_prod, g=106.75):
    return OM_R0_H2_FACTOR * (g / 106.75) ** (-1.0 / 3.0) * om_prod

def main():
    t0 = time.time()
    f = np.array([F_LO, F_YR, F_HI])
    k = K_PER_HZ * f
    out = {"task": "DA3M-R5-15 -- first-order (primordial) tensor Omega_GW h^2 "
                   "at nHz for this lab's matter-bounce background",
           "date": "2026-09-04",
           "conventions": {
               "Omega_GW_production": "P_T(k)/24 (RD, oscillation-averaged; "
                   "Watanabe & Komatsu 2006; Caprini & Figueroa 2018 Sec. 2)",
               "transfer_to_today": "1.62e-5 * (g_*/106.75)^{-1/3}, identical to "
                   "sigw_nhz_from_lab_spectrum_2026_09_04.py",
               "g_star_baseline": 106.75,
               "r_case_A_source": "Ade et al. (BICEP/Keck) 2021, PRL 127, 151301, "
                   "arXiv:2110.00483 -- r < 0.036 (95% CL) at k_*=0.05 Mpc^-1; "
                   "an UPPER LIMIT, so CASE A Omega_GW^(1) is an upper limit",
               "r_case_B_source": "Cai et al. 2009 matter-bounce r = 0.84, this "
                   "program's OPEN item A3-4 (re-derivation unresolved); reported "
                   "as a scenario only, already excluded at k_* by CASE A"},
           "f_Hz": f.tolist(), "k_Mpc-1": k.tolist(),
           "induced_reference_Omega_GW_h2_at_f_yr": INDUCED,
           "nanograv_Omega_GW_h2_at_f_yr": NG_OM_H2_FYR,
           "cases": {}}
    for rname, r in R_CASES.items():
        for bname, nT in NT_CASES.items():
            om0 = omega_today_h2(p_T(k, r, nT) / 24.0)
            i = 1
            nO = np.log(om0[2] / om0[0]) / np.log(f[2] / f[0])
            out["cases"][f"{rname}|{bname}"] = {
                "r": r, "n_T": nT,
                "Omega_GW1_h2_at_2nHz": float(om0[0]),
                "Omega_GW1_h2_at_f_yr": float(om0[i]),
                "Omega_GW1_h2_at_60nHz": float(om0[2]),
                "n_Omega_local_slope": float(nO),
                "gamma_pred_first_order": float(5.0 - nO),
                "log10_ratio_first_order_over_induced_at_f_yr":
                    float(np.log10(om0[i] / INDUCED[bname])),
                "log10_shortfall_vs_NANOGrav_at_f_yr":
                    float(np.log10(NG_OM_H2_FYR / om0[i])),
                "g_star20_variant_Omega_GW1_h2_at_f_yr":
                    float(omega_today_h2(p_T(k[i], r, nT) / 24.0, g=20.0))}
    a = out["cases"]["A_CMB_bound_r0.036|MB_anchored_ns0.9649"]
    b = out["cases"]["B_scenario_matter_bounce_r0.84|pure_dust_ns1"]
    out["verdict"] = {
        "which_dominates": "first-order (primordial) tensors, by "
            f"{a['log10_ratio_first_order_over_induced_at_f_yr']:.1f} decades "
            "even at the CMB upper bound r < 0.036",
        "does_the_PTA_null_change": "NO. Both channels remain far below the "
            f"NANOGrav band: the first-order upper limit is 10^"
            f"{a['log10_shortfall_vs_NANOGrav_at_f_yr']:.1f} below "
            f"Omega_GW h^2(f_yr) = {NG_OM_H2_FYR:.4e} (CASE A), and 10^"
            f"{b['log10_shortfall_vs_NANOGrav_at_f_yr']:.1f} below even in the "
            "excluded r = 0.84 scenario.",
        "slope_test_unchanged": "n_T = n_s - 1 gives gamma_first-order = "
            f"{a['gamma_pred_first_order']:.3f}, within 0.04 of the induced "
            "gamma_pred = 5.070, so adding the first-order channel does not "
            "move the Channel I slope comparison against gamma_HD = 3.2 +- 0.6."}
    out["wall_seconds"] = time.time() - t0
    OUTJ.parent.mkdir(parents=True, exist_ok=True)
    OUTJ.write_text(json.dumps(out, indent=2))
    print(json.dumps(out["cases"], indent=2))
    print(json.dumps(out["verdict"], indent=2))

if __name__ == "__main__":
    main()
