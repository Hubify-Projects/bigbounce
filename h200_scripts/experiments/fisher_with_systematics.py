#!/usr/bin/env python3
"""
Wave 14-II: P3 systematics-marginalization Fisher recompute.

Closes R42 P3-CM-M1 / P3-OA-B5 ("Quantitative systematics marginalization in f_NL
Fisher OR explicit zero-systematic caveat") at the FULL HARD FIX path: extend the
baseline single+multi-tracer Fisher (h200_scripts/experiments/fisher_forecast_spherex.py)
with a nuisance-parameter block and marginalize σ(f_NL) over Gaussian priors on:

  1. Linear-bias amplitude per tracer:   δb_i  (prior σ_δb = 0.05, i.e. 5%)
  2. Photo-z RMS damping:                 σ_z  (prior σ on σ_z = 0.003 SPHEREx, 0.001 DESI)
  3. Magnification-bias coefficient:      δs_i (prior σ = 0.1)
  4. Shot-noise mis-estimation per tr.:   δN_i (prior σ_log = 0.10)

For each survey config (SPHEREx / DESI / combined ± anomaly tracers) we report:
  - Unmarginalized σ(f_NL)  (matches baseline run)
  - Per-systematic-only marginalized σ(f_NL)
  - Fully marginalized σ(f_NL)  (all 4 systematic blocks at once)
  - Detection significance for f_NL = -4.375 (matter bounce)

Output: /workspace/bigbounce/outputs/fisher_with_systematics/result.json + log
"""

import json, os, sys, time
from pathlib import Path
import numpy as np

# ============================================================
# Cosmology + tracer specs (cloned from baseline to keep self-contained)
# ============================================================
H0 = 67.36; h = H0 / 100.0
OMEGA_M = 0.3153; OMEGA_L = 1.0 - OMEGA_M
N_S = 0.9649; SIGMA8 = 0.8111; DELTA_C = 1.686
C_LIGHT = 2.998e5

K_MIN, K_MAX, N_K = 1e-4, 0.2, 50
K_BINS = np.logspace(np.log10(K_MIN), np.log10(K_MAX), N_K + 1)
K_C    = np.sqrt(K_BINS[:-1] * K_BINS[1:])

Z_MIN, Z_MAX, DZ = 0.2, 3.0, 0.2
Z_E = np.arange(Z_MIN, Z_MAX + DZ/2, DZ)
Z_C = 0.5 * (Z_E[:-1] + Z_E[1:])
N_Z = len(Z_C)

F_NL_MATTER_BOUNCE = -4.375  # = -35/8 parameter-free prediction

def make_tracer(name, bias, nbar, zr, survey, photoz_sig=0.003, mag_s=0.5):
    return dict(name=name, bias=bias, nbar=nbar, z_range=zr, survey=survey,
                photoz_sig=photoz_sig, mag_s=mag_s)

SPHEREX = [
    make_tracer('SPHEREx_LRG', lambda z: 1.7+0.6*z,
                lambda z: 3e-4*np.exp(-((z-0.7)/0.3)**2), (0.2,1.5), 'SPHEREx', 0.003, 0.4),
    make_tracer('SPHEREx_ELG', lambda z: 0.84+0.4*z,
                lambda z: 1e-3*np.exp(-((z-1.0)/0.5)**2), (0.2,2.0), 'SPHEREx', 0.003, 0.5),
    make_tracer('SPHEREx_QSO', lambda z: 1.2+0.5*z,
                lambda z: 5e-5*np.exp(-((z-1.5)/0.8)**2), (0.5,3.0), 'SPHEREx', 0.003, 0.6),
]
DESI = [
    make_tracer('DESI_LRG', lambda z: 1.7+0.6*z,
                lambda z: 5e-4*np.exp(-((z-0.7)/0.3)**2), (0.2,1.2), 'DESI', 0.001, 0.4),
    make_tracer('DESI_ELG', lambda z: 0.84+0.4*z,
                lambda z: 4e-4*np.exp(-((z-1.3)/0.4)**2), (0.6,1.7), 'DESI', 0.001, 0.5),
    make_tracer('DESI_QSO', lambda z: 2.0+0.3*z,
                lambda z: 3e-5*np.exp(-((z-1.6)/0.7)**2), (0.8,2.5), 'DESI', 0.001, 0.6),
]
ANOMALY = [
    make_tracer('Anomaly_HighBias',     lambda z: 4.0+1.5*z,
                lambda z: 2e-6*np.exp(-((z-0.8)/0.4)**2), (0.2,2.0), 'Anomaly', 0.005, 0.7),
    make_tracer('Anomaly_UltraHighZ',   lambda z: 5.0+2.0*z,
                lambda z: 5e-7*np.exp(-((z-2.0)/0.6)**2), (1.0,3.0), 'Anomaly', 0.005, 0.7),
    make_tracer('Anomaly_XraySelected', lambda z: 3.5+1.0*z,
                lambda z: 8e-7*np.exp(-((z-0.6)/0.3)**2), (0.2,1.5), 'Anomaly', 0.005, 0.7),
]
F_SKY = dict(SPHEREx=0.75, DESI=0.34, Anomaly=0.34)

def hubble(z): return H0 * np.sqrt(OMEGA_M*(1+z)**3 + OMEGA_L)

def comoving_chi(z_max):
    zg = np.linspace(0, z_max, 1500)
    integrand = C_LIGHT / hubble(zg)
    return np.trapz(integrand, zg) * h

def growth(z):
    a = 1.0/(1.0+z)
    Om_z = OMEGA_M*(1+z)**3 / (OMEGA_M*(1+z)**3 + OMEGA_L)
    Ol_z = OMEGA_L / (OMEGA_M*(1+z)**3 + OMEGA_L)
    D = (5.0/2.0) * Om_z / (Om_z**(4.0/7.0) - Ol_z + (1+Om_z/2.0)*(1+Ol_z/70.0))
    D0 = (5.0/2.0) * OMEGA_M / (OMEGA_M**(4.0/7.0) - OMEGA_L + (1+OMEGA_M/2.0)*(1+OMEGA_L/70.0))
    return D / D0

def transfer(k):
    q = k / (OMEGA_M * h**2) * (2.728/2.7)**2
    L = np.log(2*np.e + 1.8*q); C = 14.2 + 731.0/(1 + 62.5*q)
    return L / (L + C * q**2)

def Pm_norm():
    kg = np.logspace(-4, 1, 1000); Tg = transfer(kg)
    Pg = kg**N_S * Tg**2
    R = 8.0; x = kg*R; W = 3*(np.sin(x)-x*np.cos(x))/x**3
    sig8sq = np.trapz(kg**2 * Pg * W**2, kg) / (2*np.pi**2)
    return SIGMA8**2 / sig8sq

A_NORM = Pm_norm()

def Pmatter(k, z):
    Tk = transfer(k); Dz = growth(z)
    return A_NORM * k**N_S * Tk**2 * Dz**2

def alpha_fnl(k, z):
    return (2.0/3.0) * k**2 * transfer(k) * growth(z) / OMEGA_M

def survey_volume(zlo, zhi, fsky):
    return (4.0/3.0)*np.pi*fsky * (comoving_chi(zhi)**3 - comoving_chi(zlo)**3)

# ============================================================
# Multi-tracer Fisher with nuisance-parameter block
# ============================================================
# Parameter ordering for each (z-bin, k-bin) cell:
#   θ = [f_NL, δb_1..δb_n, σ_z_1..σ_z_n, δs_1..δs_n, δlogN_1..δlogN_n]
# Block size per cell: 1 + 4n where n = number of active tracers in this z-bin.
#
# At fiducial values (f_NL=0, δb=0, δs=0, δlogN=0, σ_z=σ_z_fid):
#   b_obs_i = b_i (1 + δb_i)
#   W_zphot_i(k,z) = exp(-k_par^2 σ_z_i^2 / 2)  -> we use 1D (monopole) effective
#                    damping, integrated to give f_loss(k,z,σ_z) = exp(-(k σ_z c/H)^2/3)
#   shot_i = (1 + δlogN_i) / n_i
#   magbias change in scale-dep bias enters via δs (Slosar 2008): not detail-correct
#                    in this monopole code; we treat δs as adding ~ 2(δs)(b-1)*δ_c/α to
#                    Δb (small), which gives a finite F_(f_NL, δs) coupling.

def Wphot_loss(k, z, sigz):
    """Approximate radial photo-z damping integrated over isotropic modes
       (analytic monopole average of exp(-k_par^2 sigz_chi^2)):
       = sqrt(pi)/2 * erf(k*sigz_chi) / (k*sigz_chi),  sigz_chi = c sigz / H(z)
       For our purposes the key is that it suppresses high-k power; we use the
       leading approximation 1 - (k sigz_chi)^2 / 6 in the small-arg regime, exact
       erf form otherwise. SciPy not assumed -> tabulate via numpy.
    """
    if sigz <= 0:
        return 1.0
    sigz_chi = (C_LIGHT * sigz) / hubble(z) * h   # convert to Mpc/h
    x = k * sigz_chi
    if x < 1e-6:
        return 1.0 - x**2 / 6.0
    # erf via Abramowitz-Stegun rational approximation
    t = 1.0 / (1.0 + 0.3275911 * x)
    erf = 1.0 - (((((1.061405429*t - 1.453152027)*t) + 1.421413741)*t - 0.284496736)*t + 0.254829592)*t * np.exp(-x**2)
    return 0.5 * np.sqrt(np.pi) * erf / x

def compute_fisher_block(tracers_all, f_sky, prior_db=0.05, prior_dlogN=0.10,
                         prior_ds=0.10, prior_sigz_extra=0.001):
    """Compute the per-cell Fisher block over (f_NL, nuisance params) and assemble
    the global Fisher matrix.
    Returns: F_global (param_dim x param_dim), list of param names.
    """
    n = len(tracers_all)
    # Parameter ordering globally: f_NL, δb_1..n, δs_1..n, δlogN_1..n, σ_z_1..n
    # σ_z is given a prior on the *deviation* from fiducial (so prior on Δσ_z = prior_sigz_extra)
    pnames = ['f_NL'] + [f'db_{t["name"]}' for t in tracers_all] \
                       + [f'ds_{t["name"]}' for t in tracers_all] \
                       + [f'dlogN_{t["name"]}' for t in tracers_all] \
                       + [f'dsigz_{t["name"]}' for t in tracers_all]
    P = len(pnames)
    F = np.zeros((P, P))

    name_to_idx = {nm: i for i, nm in enumerate(pnames)}

    for iz, z in enumerate(Z_C):
        zlo, zhi = Z_E[iz], Z_E[iz+1]
        Veff = survey_volume(zlo, zhi, f_sky)
        # active tracers
        active_idx = [i for i, t in enumerate(tracers_all)
                      if t['z_range'][0] <= z <= t['z_range'][1]]
        if not active_idx:
            continue
        bs   = np.array([tracers_all[i]['bias'](z) for i in active_idx])
        nbs  = np.array([tracers_all[i]['nbar'](z) for i in active_idx])
        sigz = np.array([tracers_all[i]['photoz_sig'] for i in active_idx])
        ms   = np.array([tracers_all[i]['mag_s']    for i in active_idx])
        names = [tracers_all[i]['name'] for i in active_idx]
        nA = len(active_idx)

        for ik, k in enumerate(K_C):
            dk = K_BINS[ik+1] - K_BINS[ik]
            Pk_lin = Pmatter(k, z)
            alpha  = alpha_fnl(k, z)
            n_modes = k**2 * dk * Veff / (2*np.pi**2)
            if n_modes <= 0 or alpha < 1e-12:
                continue
            # Photo-z window per tracer
            Wp = np.array([Wphot_loss(k, z, sigz[a]) for a in range(nA)])
            Pk_eff_per_tr = Pk_lin * Wp**2  # power as seen by each tracer

            # Effective auto/cross power: P_ij = b_i b_j sqrt(P_eff_i * P_eff_j)
            # For simplicity (single-window approximation), use mean window per pair:
            Wmean = np.outer(Wp, Wp)
            C = np.outer(bs, bs) * Pk_lin * Wmean + np.diag((1.0/np.maximum(nbs,1e-12)))
            try:
                Cinv = np.linalg.inv(C)
            except np.linalg.LinAlgError:
                continue

            # ---- derivatives ----
            # dC/df_NL:  Δb_i = (b_i - 1) δ_c / α; dC_ij = (Δb_i b_j + b_i Δb_j) Pk_lin Wmean_ij
            db_fNL = (bs - 1.0) * DELTA_C / alpha
            dC_fNL = (np.outer(db_fNL, bs) + np.outer(bs, db_fNL)) * Pk_lin * Wmean

            # dC/dδb_i:  δb_i scales b_i -> b_i (1+δb_i); evaluate at fiducial 0:
            #   dC_ij/dδb_i = (b_i b_j δ_{ij}-style coupling) -> for diagonal i:
            #     dC_ii/dδb_i = 2 b_i^2 Pk_lin Wmean_ii (W=1 for same tracer pair? no: window enters via window-for-i squared = Wp_i^2)
            # General expression:
            #   C_ij = b_i b_j (1+δb_i)(1+δb_j) P_lin W_i W_j + δ_ij/n_i
            #   dC_ij/dδb_k = b_i b_j P_lin W_i W_j * (δ_ki (1+δb_j) + δ_kj (1+δb_i))
            # at fiducial δb=0:
            #   dC_ij/dδb_k = b_i b_j P_lin W_i W_j * (δ_ki + δ_kj)
            dC_db = []  # list of n matrices
            for kidx in range(nA):
                M = np.zeros((nA, nA))
                # row k
                M[kidx, :] += bs[kidx] * bs * Pk_lin * Wp[kidx] * Wp
                # col k
                M[:, kidx] += bs * bs[kidx] * Pk_lin * Wp * Wp[kidx]
                dC_db.append(M)

            # dC/dδlogN_i: shot noise term (1+δlogN_i)/n_i, derivative at 0 is 1/n_i for diagonal
            dC_dlogN = []
            for kidx in range(nA):
                M = np.zeros((nA, nA))
                M[kidx, kidx] = 1.0 / max(nbs[kidx], 1e-12)
                dC_dlogN.append(M)

            # dC/dσ_z_i: derivative of W_i wrt σ_z_i at fiducial.
            # Use finite-difference numerical derivative of Wp_i(k, z, σ_z_i) wrt σ_z_i:
            dC_dsigz = []
            eps = 1e-4
            for kidx in range(nA):
                Wp_plus = Wp.copy()
                Wp_plus[kidx] = Wphot_loss(k, z, sigz[kidx] + eps)
                Wmean_plus = np.outer(Wp_plus, Wp_plus)
                C_plus = np.outer(bs, bs) * Pk_lin * Wmean_plus + np.diag(1.0/np.maximum(nbs,1e-12))
                dC_dsigz.append((C_plus - C) / eps)

            # dC/dδs_i: magnification-bias modulation enters scale-dep bias as
            #   Δb_mag_i = 2 (δs_i) (b_i - 1) δ_c / α (linear order; standard Liu/Slosar form)
            # so dC_ij/dδs_k at fiducial 0 contributes (only when f_NL ≠ 0 fiducially or via
            # cross-coupling) — at f_NL=0 fiducial this gives an OFF-DIAGONAL coupling
            # F_(f_NL, δs_k) but ZERO direct dC/dδs term. To capture the cross coupling,
            # we add an explicit dC/dδs that mirrors the f_NL derivative scaled by 2(b-1)/α
            # weighted by δ_ki:
            dC_ds = []
            for kidx in range(nA):
                ds_db = np.zeros(nA)
                ds_db[kidx] = 2.0 * (bs[kidx] - 1.0) * DELTA_C / alpha
                M = (np.outer(ds_db, bs) + np.outer(bs, ds_db)) * Pk_lin * Wmean
                dC_ds.append(M)

            # ---- assemble local Fisher block ----
            # For each pair of derivatives (X, Y): F_XY += (n_modes/2) * Tr[Cinv dC_X Cinv dC_Y]
            # Build local list of (param_name, dC):
            local_params = [('f_NL', dC_fNL)]
            for kidx, nm in enumerate(names):
                local_params.append((f'db_{nm}',    dC_db[kidx]))
            for kidx, nm in enumerate(names):
                local_params.append((f'ds_{nm}',    dC_ds[kidx]))
            for kidx, nm in enumerate(names):
                local_params.append((f'dlogN_{nm}', dC_dlogN[kidx]))
            for kidx, nm in enumerate(names):
                local_params.append((f'dsigz_{nm}', dC_dsigz[kidx]))

            # Precompute Cinv @ dC_X for each
            CinvdC = [Cinv @ dC for (_, dC) in local_params]

            for a, (na, _) in enumerate(local_params):
                ia = name_to_idx[na]
                for b, (nb, _) in enumerate(local_params):
                    ib = name_to_idx[nb]
                    F[ia, ib] += 0.5 * n_modes * np.trace(CinvdC[a] @ CinvdC[b])

    # ---- prior matrix on nuisance parameters ----
    Lambda_inv = np.zeros_like(F)
    for nm, idx in name_to_idx.items():
        if nm == 'f_NL':
            continue
        if nm.startswith('db_'):
            Lambda_inv[idx, idx] = 1.0 / prior_db**2
        elif nm.startswith('ds_'):
            Lambda_inv[idx, idx] = 1.0 / prior_ds**2
        elif nm.startswith('dlogN_'):
            Lambda_inv[idx, idx] = 1.0 / prior_dlogN**2
        elif nm.startswith('dsigz_'):
            Lambda_inv[idx, idx] = 1.0 / prior_sigz_extra**2

    F_with_prior = F + Lambda_inv
    return F, F_with_prior, pnames

def marginalized_sigma_fNL(F_with_prior, pnames):
    try:
        Finv = np.linalg.inv(F_with_prior)
    except np.linalg.LinAlgError:
        return float('inf')
    idx_f = pnames.index('f_NL')
    var = Finv[idx_f, idx_f]
    return float(np.sqrt(max(var, 0)))

def unmarginalized_sigma_fNL(F, pnames):
    idx_f = pnames.index('f_NL')
    if F[idx_f, idx_f] <= 0:
        return float('inf')
    return float(1.0 / np.sqrt(F[idx_f, idx_f]))

def per_systematic_sigma(F, pnames, prefix, prior):
    """σ(f_NL) marginalizing over only ONE systematic block (e.g., 'db_*')."""
    keep_idx = [i for i, nm in enumerate(pnames)
                if nm == 'f_NL' or nm.startswith(prefix)]
    Fsub = F[np.ix_(keep_idx, keep_idx)].copy()
    sub_names = [pnames[i] for i in keep_idx]
    Lam = np.zeros_like(Fsub)
    for j, nm in enumerate(sub_names):
        if nm == 'f_NL':
            continue
        Lam[j, j] = 1.0 / prior**2
    return marginalized_sigma_fNL(Fsub + Lam, sub_names)

# ============================================================
# Main
# ============================================================
def main():
    OUTDIR = "/workspace/bigbounce/outputs/fisher_with_systematics"
    os.makedirs(OUTDIR, exist_ok=True)
    print("=" * 70)
    print("Wave 14-II — P3 systematics-marginalization Fisher recompute")
    print("=" * 70)
    t0 = time.time()

    configs = {
        'SPHEREx_only':                {'tr': SPHEREX,                      'fsky': F_SKY['SPHEREx']},
        'SPHEREx_plus_anomaly':        {'tr': SPHEREX + ANOMALY,            'fsky': F_SKY['SPHEREx']},
        'DESI_only':                   {'tr': DESI,                         'fsky': F_SKY['DESI']},
        'DESI_plus_anomaly':           {'tr': DESI + ANOMALY,               'fsky': F_SKY['DESI']},
        'SPHEREx_DESI_combined':       {'tr': SPHEREX + DESI,               'fsky': max(F_SKY['SPHEREx'], F_SKY['DESI'])},
        'SPHEREx_DESI_plus_anomaly':   {'tr': SPHEREX + DESI + ANOMALY,     'fsky': max(F_SKY['SPHEREx'], F_SKY['DESI'])},
    }

    PRIORS = dict(prior_db=0.05, prior_dlogN=0.10, prior_ds=0.10, prior_sigz_extra=0.001)

    results = {'priors': PRIORS, 'configs': {}}
    print(f"\nPriors: {PRIORS}")

    for cname, cfg in configs.items():
        print(f"\n--- {cname} ---  tracers={len(cfg['tr'])}, f_sky={cfg['fsky']:.2f}")
        F, F_full, pnames = compute_fisher_block(cfg['tr'], cfg['fsky'], **PRIORS)

        sig_unmarg  = unmarginalized_sigma_fNL(F, pnames)
        sig_full    = marginalized_sigma_fNL(F_full, pnames)
        sig_db      = per_systematic_sigma(F, pnames, 'db_',     PRIORS['prior_db'])
        sig_ds      = per_systematic_sigma(F, pnames, 'ds_',     PRIORS['prior_ds'])
        sig_dlogN   = per_systematic_sigma(F, pnames, 'dlogN_',  PRIORS['prior_dlogN'])
        sig_dsigz   = per_systematic_sigma(F, pnames, 'dsigz_',  PRIORS['prior_sigz_extra'])

        det_unmarg = abs(F_NL_MATTER_BOUNCE) / sig_unmarg if sig_unmarg > 0 else 0
        det_full   = abs(F_NL_MATTER_BOUNCE) / sig_full   if sig_full   > 0 else 0
        degrad_pct = 100.0 * (sig_full - sig_unmarg) / sig_unmarg if sig_unmarg > 0 else 0

        results['configs'][cname] = {
            'n_tracers':            len(cfg['tr']),
            'f_sky':                cfg['fsky'],
            'sigma_fNL_unmarg':     round(sig_unmarg, 4),
            'sigma_fNL_marg_db':    round(sig_db, 4),
            'sigma_fNL_marg_ds':    round(sig_ds, 4),
            'sigma_fNL_marg_dlogN': round(sig_dlogN, 4),
            'sigma_fNL_marg_dsigz': round(sig_dsigz, 4),
            'sigma_fNL_marg_full':  round(sig_full, 4),
            'sigma_degradation_pct': round(degrad_pct, 2),
            'detection_sigma_unmarg':   round(det_unmarg, 2),
            'detection_sigma_marg_full': round(det_full, 2),
        }
        print(f"  σ_unmarg = {sig_unmarg:.4f}  →  σ_full-marg = {sig_full:.4f}  "
              f"(degradation {degrad_pct:+.2f}%)")
        print(f"  matter-bounce detection: {det_unmarg:.2f}σ → {det_full:.2f}σ")

    elapsed = time.time() - t0
    results['runtime_seconds'] = round(elapsed, 1)
    results['F_NL_target'] = F_NL_MATTER_BOUNCE
    results['n_k_bins'] = N_K
    results['n_z_bins'] = N_Z
    results['k_max'] = K_MAX
    print(f"\nElapsed: {elapsed:.1f}s")

    out = Path(OUTDIR) / "result.json"
    with open(out, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out}")

if __name__ == "__main__":
    main()
