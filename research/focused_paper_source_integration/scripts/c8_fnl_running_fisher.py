#!/usr/bin/env python3
"""
C8 — Real, committed, reproducible joint (f_NL, n_fNL) scale-dependent-bias
Fisher forecast for SPHEREx. Replaces the unprovenance FW-1 artifact
(pipelines/p2_fnl_forecast/fw1_results/fw1_scale_dependent_fnl.json, commit
c58ed751) flagged SUSPECT by the C7 provenance audit
(project-context/peer-reviews/C7_C58ED751_PROVENANCE_AUDIT.md §1):
no generating script, no recorded n(z)/bias/b_phi/volume inputs, and an
implied unmarginalized sigma(f_NL)=0.114 that is ~6x sharper than any
published SPHEREx SDB forecast.

Paper: research/focused_paper_source_integration/02_full_draft.tex L581
(quotes sigma(n_fNL)=0.086, sigma_marg(f_NL)=0.44, rho=0.966, ~9.9sigma,
"testable to +/-0.09" — all sourced verbatim from the suspect artifact).

------------------------------------------------------------------------
PHYSICS (standard scale-dependent bias, Dalal+2008 / Slosar+2008 /
Barreira 2022 conventions; matches the paper's stated convention at
02_full_draft.tex L477: b_phi = 2 delta_c (b_1 - 1) universality):

  Delta b(k,z) = f_NL(k) * b_phi / M(k,z),    b_phi = 2 delta_c (b - p),  p = 1
  M(k,z)       = (2/3) k^2 T(k) D_md(z) c^2 / (Omega_m H0^2)
               = sqrt( P_m(k,z) / P_phi(k) )            [exact, used here]
  P_phi(k)     = (9/25) * (2 pi^2 / k^3) * P_R(k)       [Bardeen potential, MD]
  P_R(k)       = A_s (k / k_pivot_As)^(n_s - 1)         [primordial curvature]

i.e. Delta b(k,z) = 3 f_NL(k) (b-p) delta_c Omega_m H0^2 / (c^2 k^2 T(k) D_md(z)),
computed exactly from the CAMB linear P_m(k,z) and the primordial spectrum,
which removes all transfer-function / growth-normalization ambiguity
(D_md normalized to a in matter domination is implicit in the sqrt ratio).

Running parameterization (matches the paper / artifact):
  f_NL(k) = f_NL * (k / k_piv)^(n_fNL),   k_piv = 0.05 h/Mpc,
  fiducial f_NL = -35/8 = -4.375 (matter bounce), n_fNL = 0.

Multi-tracer Gaussian Fisher per z-bin, per k-shell:
  C_ij(k,z)  = btot_i btot_j W_i W_j P_m(k,z) + delta_ij / nbar_i
  btot_i     = b_i + Delta b_i(k,z)
  W_i(k,z)   = photo-z radial damping, monopole average of exp(-k_par^2 sig_chi^2):
               W = sqrt(pi)/2 * erf(k sig_chi) / (k sig_chi),
               sig_chi = c sigma_z (1+z)... see note: sigma_z table is already
               sigma_z/(1+z) upper bound, so sig_z_abs = sigz_rel*(1+z_c),
               sig_chi = c * sig_z_abs / H(z) in Mpc/h.
  F_ab      += N_modes * Tr[Cinv dC_a Cinv dC_b],
               N_modes = V_bin k^2 dk / (4 pi^2)   (independent complex modes)

------------------------------------------------------------------------
SURVEY INPUTS — every number sourced:

* n_i(z), b_i(z): official SPHEREx public forecast products v28
  (Dore et al. 2014, arXiv:1412.4872; machine-readable file
  galaxy_density_v28_base_cbe.txt from
  https://github.com/SPHEREx/Public-products, committed alongside this
  script at scripts/data/galaxy_density_v28_base_cbe.txt).
  5 galaxy samples defined by photo-z accuracy sigma_z/(1+z) <=
  {0.003, 0.01, 0.03, 0.1, 0.2} (worst-case per sample, per repo README),
  on 11 redshift bins. We use the first SIX bins (z = 0 - 1.6), matching the
  paper's stated "six redshift bins (z = 0.1-1.5)" configuration up to the
  official bin edges.
* f_sky = 0.75 (paper L581 + artifact; SPHEREx is all-sky, usable fraction
  after Galactic cuts ~0.75, consistent with Dore+2014 forecasts).
* k_max = 0.2 h/Mpc (artifact's stated range; linear regime).
* k_min per z-bin = max(1e-4, 2 pi / V_bin^(1/3)) — the fundamental mode of
  the bin volume. The artifact used a flat k_min = 1e-4 h/Mpc, which is NOT
  reachable in the z<0.2 bins; we report both choices.
* k_piv = 0.05 h/Mpc (artifact field "k_pivot_hMpc").
* Cosmology: Planck 2018 TT,TE,EE+lowE+lensing best fit
  (H0=67.36, ombh2=0.02237, omch2=0.1200, n_s=0.9649, A_s=2.100e-9,
  tau=0.0544, mnu=0.06) — same family as the repo's other Fisher scripts.

REPORTED CASES:
  A. f_NL-only, biases fixed                      (artifact "fnl_only" analog)
  B. joint (f_NL, n_fNL), biases fixed            (artifact "joint" analog)
  C. joint (f_NL, n_fNL) + free per-(sample,zbin) bias marginalization
     (30 nuisance params, no prior) — the honest forecast
  D. same as B/C but with the artifact's flat k_min = 1e-4 (sensitivity check)

Runtime: < 1 min CPU. Output:
  research/focused_paper_source_integration/outputs/c8_fnl_running_fisher.json
"""

import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.special import erf

import camb

# ============================================================
# Constants & configuration
# ============================================================
C_LIGHT = 299792.458  # km/s

# Planck 2018 best fit (TT,TE,EE+lowE+lensing)
H0 = 67.36
OMBH2 = 0.02237
OMCH2 = 0.1200
NS = 0.9649
AS = 2.100e-9
TAU = 0.0544
MNU = 0.06
KPIV_AS_MPC = 0.05  # 1/Mpc (CAMB primordial pivot)

h = H0 / 100.0
DELTA_C = 1.686
P_UNIV = 1.0  # universality p in b_phi = 2 delta_c (b - p); paper L477 uses p=1

F_NL_FID = -35.0 / 8.0  # = -4.375, matter-bounce prediction (paper headline)
N_FNL_FID = 0.0
K_PIV_FNL = 0.05  # h/Mpc, running pivot (artifact "k_pivot_hMpc")

F_SKY = 0.75
K_MAX = 0.2     # h/Mpc (artifact "k_range_hMpc" upper end; linear regime)
K_MIN_FLOOR = 1e-4  # h/Mpc, artifact's flat lower end (case D only)
N_K = 400       # log-spaced k-shells per z-bin

REPO = Path(__file__).resolve().parents[3]
DATA_FILE = Path(__file__).resolve().parent / "data" / "galaxy_density_v28_base_cbe.txt"
OUT_DIR = Path(__file__).resolve().parents[1] / "outputs"
OUT_FILE = OUT_DIR / "c8_fnl_running_fisher.json"

# Suspect FW-1 artifact numbers (for comparison block)
ARTIFACT = {
    "sigma_fnl_only": 0.114538,
    "sigma_fnl_marginalized": 0.443094,
    "sigma_nfnl": 0.085523,
    "correlation": 0.966013,
    "fnl_detection_sigma": 9.87,
    "fisher_matrix": [[76.22605338627889, -381.5023228871092],
                      [-381.5023228871092, 2046.0931846590872]],
}

# ============================================================
# Parse official SPHEREx public products table
# (https://github.com/SPHEREx/Public-products, v28_base_cbe)
# ============================================================
def parse_spherex_table(path):
    txt = Path(path).read_text()
    def grab(prefix, n=5):
        rows = []
        for i in range(1, n + 1):
            m = re.search(rf"{prefix}{i}\s*=\s*([^\n]+)", txt)
            rows.append([float(x) for x in m.group(1).split(",")])
        return np.array(rows)  # (5 samples, 11 z-bins)
    ndens = grab("numdens")
    bias = grab("galaxy_bias")
    zedges = []
    in_z = False
    for line in txt.splitlines():
        if line.startswith("#zmin"):
            in_z = True
            continue
        if in_z:
            p = line.split()
            if len(p) == 2:
                zedges.append((float(p[0]), float(p[1])))
    return ndens, bias, zedges

NDENS_ALL, BIAS_ALL, ZEDGES_ALL = parse_spherex_table(DATA_FILE)
# sigma_z/(1+z) worst-case per sample (Public-products README / Dore+2014)
SIGZ_REL = np.array([0.003, 0.01, 0.03, 0.1, 0.2])

# Use first SIX z-bins: z = 0-1.6 (paper: "six redshift bins, z = 0.1-1.5")
N_ZBINS = 6
ZEDGES = ZEDGES_ALL[:N_ZBINS]
Z_C = np.array([0.5 * (lo + hi) for lo, hi in ZEDGES])
NDENS = NDENS_ALL[:, :N_ZBINS]   # (5, 6) in (h/Mpc)^3
BIAS = BIAS_ALL[:, :N_ZBINS]     # (5, 6)
N_TR = 5

# ============================================================
# CAMB: linear P_m(k,z) + background
# ============================================================
pars = camb.set_params(H0=H0, ombh2=OMBH2, omch2=OMCH2, ns=NS, As=AS,
                       tau=TAU, mnu=MNU, WantTransfer=True)
pars.set_matter_power(redshifts=sorted(set(Z_C.tolist())) + [0.0], kmax=2.0)
pars.NonLinear = camb.model.NonLinear_none
results = camb.get_results(pars)
OMEGA_M = results.get_Omega('cdm') + results.get_Omega('baryon') + results.get_Omega('nu')

PK = camb.get_matter_power_interpolator(
    pars, nonlinear=False, hubble_units=True, k_hunit=True, kmax=2.0,
    var1='delta_tot', var2='delta_tot', zmax=5.0)

def P_m(k_h, z):
    """Linear matter power, (Mpc/h)^3, k in h/Mpc."""
    return PK.P(z, k_h)

def P_phi(k_h):
    """Bardeen-potential power spectrum (matter-dom convention), (Mpc/h)^3."""
    k_mpc = k_h * h  # 1/Mpc for the primordial pivot
    P_R = AS * (k_mpc / KPIV_AS_MPC) ** (NS - 1.0)
    return (9.0 / 25.0) * (2.0 * np.pi ** 2 / k_h ** 3) * P_R

def M_kz(k_h, z):
    """M(k,z) = sqrt(P_m / P_phi): delta_m = M * phi_primordial."""
    return np.sqrt(P_m(k_h, z) / P_phi(k_h))

def hubble_z(z):
    return results.hubble_parameter(z)  # km/s/Mpc

def comoving_mpc_h(z):
    return results.comoving_radial_distance(z) * h  # Mpc/h

def bin_volume(zlo, zhi, fsky):
    """Comoving volume of shell, (Mpc/h)^3."""
    return (4.0 / 3.0) * np.pi * fsky * (comoving_mpc_h(zhi) ** 3 -
                                         comoving_mpc_h(zlo) ** 3)

def photoz_window(k_h, z, sigz_rel):
    """Monopole-averaged radial photo-z damping:
    W = sqrt(pi)/2 * erf(x)/x, x = k * sigma_chi,
    sigma_chi = c * sigma_z_abs / H(z) in Mpc/h."""
    sig_z_abs = sigz_rel * (1.0 + z)
    sig_chi = C_LIGHT * sig_z_abs / hubble_z(z) * h  # Mpc/h
    x = np.atleast_1d(k_h * sig_chi)
    w = np.ones_like(x)
    big = x > 1e-8
    w[big] = 0.5 * np.sqrt(np.pi) * erf(x[big]) / x[big]
    return w if w.size > 1 else float(w[0])

# ============================================================
# Fisher assembly
# ============================================================
def build_fisher(marg_bias, kmin_mode="fundamental",
                 zedges=None, ndens=None, bias=None):
    """Returns (F, pnames).
    Parameters: [f_NL, n_fNL] (+ ln b_(s,zbin) per nuisance if marg_bias).
    kmin_mode: 'fundamental' -> k_min = max(1e-4, 2pi/V^(1/3)) per bin;
               'flat1e-4'    -> k_min = 1e-4 (artifact's choice)."""
    zedges = ZEDGES if zedges is None else zedges
    ndens = NDENS if ndens is None else ndens
    bias_t = BIAS if bias is None else bias
    nzb = len(zedges)
    z_c = np.array([0.5 * (lo + hi) for lo, hi in zedges])
    pnames = ["f_NL", "n_fNL"]
    if marg_bias:
        for s in range(N_TR):
            for iz in range(nzb):
                pnames.append(f"lnb_s{s+1}_z{iz+1}")
    P = len(pnames)
    F = np.zeros((P, P))
    kmins = []

    for iz, (zlo, zhi) in enumerate(zedges):
        zc = z_c[iz]
        V = bin_volume(zlo, zhi, F_SKY)
        kf = 2.0 * np.pi / V ** (1.0 / 3.0)
        kmin = K_MIN_FLOOR if kmin_mode == "flat1e-4" else max(K_MIN_FLOOR, kf)
        kmins.append(kmin)
        kedges = np.logspace(np.log10(kmin), np.log10(K_MAX), N_K + 1)
        kc = np.sqrt(kedges[:-1] * kedges[1:])
        dk = np.diff(kedges)

        b = bias_t[:, iz]          # (5,)
        nbar = ndens[:, iz]        # (5,)
        Wz = np.array([photoz_window(kc, zc, SIGZ_REL[s]) for s in range(N_TR)])  # (5, Nk)
        Pm = P_m(kc, zc)           # (Nk,)
        M = M_kz(kc, zc)           # (Nk,)
        lnkp = np.log(kc / K_PIV_FNL)

        # f_NL(k) at fiducial n_fNL = 0:
        fnl_k = F_NL_FID * (kc / K_PIV_FNL) ** N_FNL_FID  # = F_NL_FID
        bphi = 2.0 * DELTA_C * (b[:, None] - P_UNIV)      # (5,1)
        beta = bphi / M[None, :]                          # (5,Nk): db/df per unit fNL(k)
        db = fnl_k[None, :] * beta                        # fiducial Delta b
        btot = b[:, None] + db                            # (5,Nk)

        # derivative of btot wrt params
        dbtot = {}
        dbtot["f_NL"] = beta * (kc / K_PIV_FNL)[None, :] ** N_FNL_FID
        dbtot["n_fNL"] = F_NL_FID * lnkp[None, :] * beta
        if marg_bias:
            # d btot_i / d ln b_i = b_i * (1 + 2 delta_c f_NL(k)/M)
            dlnb = b[:, None] * (1.0 + 2.0 * DELTA_C * fnl_k[None, :] / M[None, :])

        n_modes = V * kc ** 2 * dk / (4.0 * np.pi ** 2)

        for ik in range(len(kc)):
            bw = btot[:, ik] * Wz[:, ik]                  # (5,)
            C = np.outer(bw, bw) * Pm[ik] + np.diag(1.0 / nbar)
            Cinv = np.linalg.inv(C)

            # local derivative matrices
            dCs = []
            names_local = []
            for pname in ("f_NL", "n_fNL"):
                dbw = dbtot[pname][:, ik] * Wz[:, ik]
                dCs.append((np.outer(dbw, bw) + np.outer(bw, dbw)) * Pm[ik])
                names_local.append(pname)
            if marg_bias:
                for s in range(N_TR):
                    dbw = np.zeros(N_TR)
                    dbw[s] = dlnb[s, ik] * Wz[s, ik]
                    dCs.append((np.outer(dbw, bw) + np.outer(bw, dbw)) * Pm[ik])
                    names_local.append(f"lnb_s{s+1}_z{iz+1}")

            CdC = [Cinv @ d for d in dCs]
            idx = [pnames.index(nm) for nm in names_local]
            for a in range(len(dCs)):
                for bb in range(a, len(dCs)):
                    val = n_modes[ik] * np.trace(CdC[a] @ CdC[bb])
                    F[idx[a], idx[bb]] += val
                    if idx[a] != idx[bb]:
                        F[idx[bb], idx[a]] += val
    return F, pnames, kmins

def summarize_joint(F, pnames):
    """Extract (f_NL, n_fNL) constraints after marginalizing everything else."""
    Finv = np.linalg.inv(F)
    i, j = pnames.index("f_NL"), pnames.index("n_fNL")
    sub = Finv[np.ix_([i, j], [i, j])]
    s_f = float(np.sqrt(sub[0, 0]))
    s_n = float(np.sqrt(sub[1, 1]))
    rho = float(sub[0, 1] / (s_f * s_n))
    s_f_unmarg = float(1.0 / np.sqrt(F[i, i]))
    s_n_unmarg = float(1.0 / np.sqrt(F[j, j]))
    return {
        "sigma_fnl_marginalized": s_f,
        "sigma_fnl_unmarginalized": s_f_unmarg,
        "sigma_nfnl_marginalized": s_n,
        "sigma_nfnl_unmarginalized": s_n_unmarg,
        "correlation": rho,
        "fnl_detection_sigma_marg": abs(F_NL_FID) / s_f,
        "degradation_factor": s_f / s_f_unmarg,
        "fisher_2x2_fNL_nfNL": [[float(F[i, i]), float(F[i, j])],
                                [float(F[j, i]), float(F[j, j])]],
    }

# ============================================================
# Main
# ============================================================
def main():
    t0 = time.time()
    os.makedirs(OUT_DIR, exist_ok=True)
    try:
        git_hash = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO,
                                  capture_output=True, text=True).stdout.strip()
    except Exception:
        git_hash = "unknown"

    print("=" * 72)
    print("C8 — joint (f_NL, n_fNL) SPHEREx SDB Fisher (real, reproducible)")
    print("=" * 72)
    print(f"Omega_m = {OMEGA_M:.4f}, fiducial f_NL = {F_NL_FID}, n_fNL = {N_FNL_FID}")
    print(f"Samples: 5 SPHEREx sigma_z samples x {N_ZBINS} z-bins "
          f"(z edges {ZEDGES[0][0]}-{ZEDGES[-1][1]}), f_sky = {F_SKY}")

    # --- Case A/B: biases fixed, fundamental-mode k_min ---
    F_fix, pn_fix, kmins = build_fisher(marg_bias=False, kmin_mode="fundamental")
    caseB = summarize_joint(F_fix, pn_fix)
    caseA = {"sigma_fnl_only": caseB["sigma_fnl_unmarginalized"],
             "fnl_detection_sigma": abs(F_NL_FID) / caseB["sigma_fnl_unmarginalized"]}

    # --- Case C: + free bias marginalization ---
    F_mb, pn_mb, _ = build_fisher(marg_bias=True, kmin_mode="fundamental")
    caseC = summarize_joint(F_mb, pn_mb)
    # f_NL-only with bias marginalized (drop n_fNL row/col = fix n_fNL)
    keep = [k for k in range(len(pn_mb)) if pn_mb[k] != "n_fNL"]
    Fsub = F_mb[np.ix_(keep, keep)]
    s_f_only_margb = float(np.sqrt(np.linalg.inv(Fsub)[0, 0]))

    # --- Case D: artifact's flat k_min = 1e-4 (both bias treatments) ---
    F_flat, pn_flat, _ = build_fisher(marg_bias=False, kmin_mode="flat1e-4")
    caseD_fix = summarize_joint(F_flat, pn_flat)
    F_flat_mb, pn_flat_mb, _ = build_fisher(marg_bias=True, kmin_mode="flat1e-4")
    caseD_mb = summarize_joint(F_flat_mb, pn_flat_mb)

    # --- Validation against Dore+2014: f_NL-only, ALL 11 z-bins (z=0-4.6) ---
    F_v, pn_v, _ = build_fisher(marg_bias=False, kmin_mode="fundamental",
                                zedges=ZEDGES_ALL, ndens=NDENS_ALL, bias=BIAS_ALL)
    iF = pn_v.index("f_NL")
    s_val_fix = float(1.0 / np.sqrt(F_v[iF, iF]))
    F_vmb, pn_vmb, _ = build_fisher(marg_bias=True, kmin_mode="fundamental",
                                    zedges=ZEDGES_ALL, ndens=NDENS_ALL, bias=BIAS_ALL)
    keep_v = [k for k in range(len(pn_vmb)) if pn_vmb[k] != "n_fNL"]
    s_val_mb = float(np.sqrt(np.linalg.inv(F_vmb[np.ix_(keep_v, keep_v)])[0, 0]))
    validation = {
        "config": "f_NL-only, all 11 SPHEREx z-bins (z=0-4.6), full Dore+2014 sample set",
        "sigma_fnl_biases_fixed": s_val_fix,
        "sigma_fnl_bias_marginalized": s_val_mb,
        "published_benchmark": "Dore+2014 sigma(f_NL) ~ 0.9 (multi-tracer SDB)",
    }

    elapsed = time.time() - t0

    out = {
        "experiment": "C8: joint (f_NL, n_fNL) SPHEREx scale-dependent-bias Fisher forecast",
        "replaces": "pipelines/p2_fnl_forecast/fw1_results/fw1_scale_dependent_fnl.json (FW-1, SUSPECT per C7 audit)",
        "provenance": {
            "script": "research/focused_paper_source_integration/scripts/c8_fnl_running_fisher.py",
            "git_hash_at_run": git_hash,
            "date_utc": datetime.now(timezone.utc).isoformat(),
            "camb_version": camb.__version__,
            "python": sys.version.split()[0],
            "runtime_seconds": round(elapsed, 2),
        },
        "inputs": {
            "cosmology": {"H0": H0, "ombh2": OMBH2, "omch2": OMCH2, "ns": NS,
                          "As": AS, "tau": TAU, "mnu_eV": MNU,
                          "Omega_m_derived": float(OMEGA_M),
                          "source": "Planck 2018 TT,TE,EE+lowE+lensing best fit"},
            "survey": {
                "name": "SPHEREx (5 photo-z samples, multi-tracer)",
                "f_sky": F_SKY,
                "n_z_bins_used": N_ZBINS,
                "z_bin_edges": [list(e) for e in ZEDGES],
                "z_bin_centers": Z_C.tolist(),
                "sigma_z_over_1plusz_per_sample": SIGZ_REL.tolist(),
                "number_density_hMpc3_per_sample_per_zbin": NDENS.tolist(),
                "galaxy_bias_per_sample_per_zbin": BIAS.tolist(),
                "source": ("Official SPHEREx public forecast products v28_base_cbe "
                           "(Dore et al. 2014, arXiv:1412.4872; "
                           "github.com/SPHEREx/Public-products, file "
                           "galaxy_density_v28_base_cbe.txt committed at "
                           "scripts/data/)"),
            },
            "fisher_setup": {
                "k_max_hMpc": K_MAX,
                "k_min_mode_baseline": "max(1e-4, 2pi/V_bin^(1/3)) per z-bin",
                "k_min_per_zbin_hMpc": [float(k) for k in kmins],
                "k_piv_hMpc": K_PIV_FNL,
                "n_k_shells": N_K,
                "bphi_convention": "b_phi = 2 delta_c (b - p), p = 1, delta_c = 1.686 (paper L477 universality)",
                "Delta_b": "Delta b = f_NL (k/k_piv)^n_fNL * b_phi / M(k,z), M = sqrt(P_m/P_phi) from CAMB",
                "photo_z": "monopole-averaged radial damping W = sqrt(pi)/2 erf(k sig_chi)/(k sig_chi)",
                "fiducial": {"f_NL": F_NL_FID, "n_fNL": N_FNL_FID},
                "rsd": "not included (real-space monopole; standard for SDB forecasts)",
            },
        },
        "results": {
            "A_fnl_only_biases_fixed": caseA,
            "B_joint_fnl_nfnl_biases_fixed": caseB,
            "C_joint_fnl_nfnl_bias_marginalized_free": {
                **caseC,
                "n_nuisance_params": len(pn_mb) - 2,
                "sigma_fnl_only_bias_marg_nfnl_fixed": s_f_only_margb,
            },
            "D_sensitivity_flat_kmin_1e-4": {
                "biases_fixed": caseD_fix,
                "bias_marginalized": caseD_mb,
                "note": "artifact's flat k_min=1e-4 is below the fundamental mode of every z-bin volume; shown only to bound the artifact's possible k_min advantage",
            },
            "validation_vs_Dore2014": validation,
        },
        "comparison": {
            "suspect_artifact_FW1": ARTIFACT,
            "published_benchmarks": {
                "Dore+2014_arXiv:1412.4872": "sigma(f_NL) ~ 0.9 (SPHEREx multi-tracer SDB, all 5 samples)",
                "literature_SDB_range": "sigma(f_NL) ~ 0.5-2 (Dore+2014, Munchmeyer+2019, Heinrich+2024)",
            },
        },
    }

    # comparison ratios
    real = out["results"]["C_joint_fnl_nfnl_bias_marginalized_free"]
    out["comparison"]["artifact_vs_real"] = {
        "sigma_nfnl: artifact / real(C)": ARTIFACT["sigma_nfnl"] / real["sigma_nfnl_marginalized"],
        "sigma_fnl_marg: artifact / real(C)": ARTIFACT["sigma_fnl_marginalized"] / real["sigma_fnl_marginalized"],
        "detection_sigma: artifact 9.87 vs real(C)": real["fnl_detection_sigma_marg"],
    }

    with open(OUT_FILE, "w") as f:
        json.dump(out, f, indent=2)

    # console report
    print(f"\nk_min per z-bin (h/Mpc): {[f'{k:.2e}' for k in kmins]}")
    print("\n--- A. f_NL-only, biases fixed ---")
    print(f"  sigma(f_NL) = {caseA['sigma_fnl_only']:.4f}  "
          f"({caseA['fnl_detection_sigma']:.2f} sigma for f_NL=-4.375)")
    print("\n--- B. joint (f_NL, n_fNL), biases fixed ---")
    for k, v in caseB.items():
        print(f"  {k} = {v}")
    print("\n--- C. joint + free bias marginalization (30 nuisances) ---")
    for k, v in caseC.items():
        print(f"  {k} = {v}")
    print(f"  sigma(f_NL) bias-marg, n_fNL fixed = {s_f_only_margb:.4f}")
    print("\n--- D. flat k_min = 1e-4 sensitivity (artifact's choice) ---")
    print(f"  biases fixed:    sigma(n_fNL) = {caseD_fix['sigma_nfnl_marginalized']:.4f}, "
          f"sigma_marg(f_NL) = {caseD_fix['sigma_fnl_marginalized']:.4f}, "
          f"rho = {caseD_fix['correlation']:.4f}")
    print(f"  bias-marg:       sigma(n_fNL) = {caseD_mb['sigma_nfnl_marginalized']:.4f}, "
          f"sigma_marg(f_NL) = {caseD_mb['sigma_fnl_marginalized']:.4f}")
    print("\n--- Validation vs Dore+2014 (all 11 z-bins, f_NL-only) ---")
    print(f"  sigma(f_NL) biases fixed = {s_val_fix:.4f}, bias-marg = {s_val_mb:.4f} "
          f"(published ~0.9)")
    print("\n--- Artifact (SUSPECT FW-1) ---")
    print(f"  sigma(n_fNL) = {ARTIFACT['sigma_nfnl']}, "
          f"sigma_marg(f_NL) = {ARTIFACT['sigma_fnl_marginalized']}, "
          f"rho = {ARTIFACT['correlation']}, det = {ARTIFACT['fnl_detection_sigma']} sigma")
    print(f"\nSaved: {OUT_FILE}")
    print(f"Elapsed: {elapsed:.1f} s")

if __name__ == "__main__":
    main()
