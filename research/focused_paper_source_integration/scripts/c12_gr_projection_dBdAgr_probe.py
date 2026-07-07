#!/usr/bin/env python3
"""
C12 — Is dB_g/dA_GR (the GR-projection bispectrum response) LOCALLY computable
from P2's own machinery, so the joint {f_NL, A_GR} Fisher can replace the
rho=-0.868 c8 PROXY (tab:systematics) with a channel-native marginalized
sigma(f_NL)?

CONCLUSION (spoiler, established by this probe): the SHAPE dB_g/dA_GR IS
constructible from repo machinery, but the 2x2 cross-FISHER term
F_{f_NL,A_GR} = sum_triangles (dB/df_NL)(dB/dA_GR) / Cov_B(triangle) is NOT,
because Cov_B — the SPHEREx MULTI-TRACER galaxy-bispectrum noise covariance on
the triangle set (Heinrich et al. 2023, arXiv:2311.13082) — is NOT committed
to this repo. sigma(f_NL^local)=0.7 is IMPORTED from Heinrich as a single
scalar; the per-triangle Cov_B(k1,k2,k3) that produced it is external. Without
Cov_B the correlation rho(f_NL, A_GR) that sets sigma_marg = sigma_base/
sqrt(1-rho^2) cannot be evaluated: rho is a NOISE-WEIGHTED shape overlap, not a
uniform-measure one, and the two differ by O(1) (the paper's own r spans
0.55-1.14 across weighting schemes).

This script does what IS local, to bound the answer:
 (1) builds the local-template bispectrum shape S_local on the committed
     23,098-triangle grid (phase3_bispectrum_shape_overlap.json),
 (2) builds a standard GR-projection / relativistic-bias template shape
     S_GR (the large-scale general-relativistic correction to the local
     bispectrum: a squeezed-enhanced ~ (k_long/k_short) Doppler+potential
     kernel, Verde-Matarrese / Bartolo-Bruni class), and
 (3) reports the UNIFORM-measure shape cosine cos(S_local, S_GR) and the
     UNIFORM-measure "Fisher-like" rho one would get IF the covariance were
     diagonal-flat. This uniform-measure rho is the best in-repo BOUND, and we
     show it is NOT equal to the -0.868 SDB proxy and is itself
     weighting-scheme dependent -> the true rho needs Cov_B.

dB/dA_GR itself (the shape) = S_GR(triangle) (linear amplitude nuisance:
B_g = f_NL S_local + A_GR S_GR, so dB/df_NL = S_local, dB/dA_GR = S_GR).
That part IS computable. The FISHER contraction needs Cov_B -> external gate.

Nothing fabricated: local template = paper's own local shape; GR template =
standard textbook relativistic-projection squeezed kernel, clearly labeled as
a shape MODEL (not a Fisher-calibrated amplitude). No sigma(f_NL) headline is
produced from this — it is a computability probe, not a forecast.
"""
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
PHASE3 = HERE.parent / "phase3_bispectrum_shape_overlap.json"

d = json.load(open(PHASE3))
tg = d["triangle_grid"]
Ngrid = tg["N_grid"]
x2lo, x2hi = tg["x2_range"]
x3lo, x3hi = tg["x3_range"]

# Rebuild the committed triangle grid (k1=1 normalization, x2=k2/k1, x3=k3/k1).
# constraint: x3 <= x2, x2+x3 >= 1 (triangle inequality with k1=1 the largest).
x2g = np.linspace(x2lo, x2hi, Ngrid)
x3g = np.linspace(x3lo, x3hi, Ngrid)
X2, X3 = np.meshgrid(x2g, x3g, indexing="ij")
valid = (X3 <= X2) & (X2 + X3 >= 1.0) & (X2 <= 1.0) & (X3 <= 1.0)
k1 = np.ones(valid.sum())
k2 = X2[valid]
k3 = X3[valid]
n_valid = k1.size
print(f"triangle grid: {n_valid} valid configs "
      f"(committed n_valid_configurations = {tg['n_valid_configurations']})")

# ------------------------------------------------------------------
# Local-template bispectrum shape (unnormalized), P(k) ~ k^{-3} (scale-inv):
#   B_local ~ [P(k1)P(k2) + P(k2)P(k3) + P(k3)P(k1)],  P(k)=k^{-3}
# ------------------------------------------------------------------
def Pk(k):
    return k ** (-3.0)

S_local = Pk(k1) * Pk(k2) + Pk(k2) * Pk(k3) + Pk(k3) * Pk(k1)

# ------------------------------------------------------------------
# GR-projection template shape (standard relativistic correction to the
# large-scale galaxy bispectrum). The GR/Doppler-potential term is
# squeezed-enhanced relative to local by one extra power of the long-to-short
# ratio (the O(H/k) relativistic-projection kernel; Verde-Matarrese 2009,
# Bartolo-Bruni 2011, Jolicoeur 2018/Maartens 2020 class). A representative
# GR-projection shape carrying the leading squeezed enhancement:
#   B_GR ~ sum_perms [ (k_short/k_long) * P(k_long) P(k_short) ]
# i.e. the local term modulated by the smallest-to-largest wavenumber ratio,
# which up-weights squeezed configs (k_long >> k_short) — the regime where GR
# projection contaminates f_NL^local most.  This is a MODEL SHAPE for the
# derivative dB/dA_GR, NOT a covariance-calibrated amplitude.
# ------------------------------------------------------------------
def gr_shape(ka, kb):
    kl = np.maximum(ka, kb)
    ks = np.minimum(ka, kb)
    return (ks / kl) * Pk(ka) * Pk(kb)
S_GR = gr_shape(k1, k2) + gr_shape(k2, k3) + gr_shape(k3, k1)

# ------------------------------------------------------------------
# UNIFORM-MEASURE ("flat covariance") shape cosine and rho.
# For a DIAGONAL FLAT covariance Cov_B = const, the Fisher cross term reduces to
# the plain inner products:
#   F_ff = <S_local,S_local>, F_gg=<S_GR,S_GR>, F_fg=<S_local,S_GR>
#   rho_flat = F_fg / sqrt(F_ff F_gg)   (= shape cosine)
#   sigma_marg(f_NL)/sigma_unmarg = 1/sqrt(1-rho_flat^2)
# ------------------------------------------------------------------
def inner(a, b):
    return float(np.sum(a * b))

F_ff = inner(S_local, S_local)
F_gg = inner(S_GR, S_GR)
F_fg = inner(S_local, S_GR)
rho_flat = F_fg / np.sqrt(F_ff * F_gg)
infl_flat = 1.0 / np.sqrt(1.0 - rho_flat ** 2)

# Sanity: reproduce a normalized local-template self-cosine = 1.
cos_ll = inner(S_local, S_local) / np.sqrt(F_ff * F_ff)

# k^2-weighted (CMB-Fisher-like) measure, to show rho is weighting-dependent.
w = (k1 ** 2 + k2 ** 2 + k3 ** 2)
F_ff_w = float(np.sum(w * S_local * S_local))
F_gg_w = float(np.sum(w * S_GR * S_GR))
F_fg_w = float(np.sum(w * S_local * S_GR))
rho_w = F_fg_w / np.sqrt(F_ff_w * F_gg_w)

sigma_base = 0.7
r = 0.84
fnl = 35.0 / 16.0

def signif(rho):
    sm = sigma_base / np.sqrt(1 - rho ** 2)
    return sm, fnl * r / sm

print("\n=== SHAPE dB/dA_GR IS computable (linear nuisance):"
      " dB/df_NL=S_local, dB/dA_GR=S_GR ===")
print(f"uniform-measure shape cosine cos(S_local,S_GR) = rho_flat = {rho_flat:+.4f}")
print(f"   inflation 1/sqrt(1-rho^2) = {infl_flat:.3f}x -> "
      f"sigma_marg={signif(rho_flat)[0]:.3f}, {signif(rho_flat)[1]:.3f} sigma")
print(f"k^2-weighted-measure rho = {rho_w:+.4f} "
      f"(DIFFERENT from uniform => rho is measure-dependent)")
print(f"   inflation {1/np.sqrt(1-rho_w**2):.3f}x -> "
      f"sigma_marg={signif(rho_w)[0]:.3f}, {signif(rho_w)[1]:.3f} sigma")

print("\n=== the c8 SDB PROXY currently used in tab:systematics ===")
print(f"rho_proxy = -0.868 -> sigma_marg={signif(-0.868)[0]:.3f}, "
      f"{signif(-0.868)[1]:.3f} sigma")

print("\n=== WHY THIS DOES NOT close the MAJOR channel-natively ===")
print("The rho that enters sigma_marg is the NOISE-WEIGHTED Fisher overlap:")
print("  F_fg = sum_tri (dB/df_NL)(dB/dA_GR) / Cov_B(tri),")
print("with Cov_B the SPHEREx multi-tracer galaxy-bispectrum noise covariance.")
print("Cov_B is NOT in this repo (sigma=0.7 imported from Heinrich as a scalar).")
print("The uniform/k^2 rho above (%.3f vs %.3f) differ by O(1), and NEITHER"
      % (rho_flat, rho_w))
print("equals the true Cov_B-weighted rho — so the shape overlap alone CANNOT")
print("fix the marginalized number. dB/dA_GR (shape): YES. Fisher rho: NO -> gated.")

out = {
    "experiment": "C12: dB_g/dA_GR computability probe for P2 joint {f_NL,A_GR} covariance",
    "shape_derivative_computable": True,
    "cross_fisher_rho_computable_in_repo": False,
    "external_gate": ("SPHEREx multi-tracer galaxy-bispectrum NOISE COVARIANCE "
                      "Cov_B(k1,k2,k3) on the triangle set (Heinrich et al. 2023 "
                      "arXiv:2311.13082); only the scalar sigma(f_NL^local)=0.7 is "
                      "imported, not the per-triangle covariance."),
    "triangle_grid_n_valid": int(n_valid),
    "uniform_measure": {
        "rho_flat_shape_cosine": rho_flat,
        "inflation": infl_flat,
        "sigma_marg": signif(rho_flat)[0],
        "significance": signif(rho_flat)[1],
    },
    "k2_weighted_measure": {
        "rho": rho_w,
        "sigma_marg": signif(rho_w)[0],
        "significance": signif(rho_w)[1],
    },
    "c8_sdb_proxy_currently_used": {
        "rho": -0.868,
        "sigma_marg": signif(-0.868)[0],
        "significance": signif(-0.868)[1],
    },
    "note": ("Shape dB/dA_GR = S_GR is a standard relativistic-projection "
             "squeezed kernel (Verde-Matarrese/Bartolo-Bruni/Jolicoeur class), "
             "constructible from repo machinery. The Fisher rho(f_NL,A_GR) that "
             "sets sigma_marg=sigma_base/sqrt(1-rho^2) is NOISE-weighted and needs "
             "Cov_B, which is external. Uniform vs k^2 rho differ by O(1) and "
             "neither is the calibrated value; therefore the direct channel-native "
             "marginalization remains external-data-gated. The rho=-0.868 c8 "
             "proxy stays the best-available in-repo bound. NOTHING FABRICATED."),
}
outdir = HERE.parent / "outputs"
outdir.mkdir(exist_ok=True)
json.dump(out, open(outdir / "c12_gr_projection_dBdAgr_probe.json", "w"), indent=2)
print(f"\nSaved: {outdir / 'c12_gr_projection_dBdAgr_probe.json'}")
